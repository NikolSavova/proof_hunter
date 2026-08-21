#!/usr/bin/env python3
"""Verify the mixed projected-key multiplicity collapse."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from random import Random


def choose2(value: int) -> int:
    return value * (value - 1) // 2


def audit(groups: list[tuple[frozenset[int], frozenset[int]]]) -> None:
    v_keys = sorted(set().union(*(row[0] for row in groups))) if groups else []
    w_keys = sorted(set().union(*(row[1] for row in groups))) if groups else []

    mixed_codegrees = Counter()
    for v_set, w_set in groups:
        for v in v_set:
            for w in w_set:
                mixed_codegrees[v, w] += 1
    incidence = sum(len(v_set) * len(w_set) for v_set, w_set in groups)
    assert incidence == sum(mixed_codegrees.values())
    support = len(mixed_codegrees)
    mixed_collision = sum(choose2(value) for value in mixed_codegrees.values())

    v_load = {v: sum(v in v_set for v_set, _ in groups) for v in v_keys}
    w_load = {w: sum(w in w_set for _, w_set in groups) for w in w_keys}
    l_v = sum(choose2(value) for value in v_load.values())
    l_w = sum(choose2(value) for value in w_load.values())

    vv_codegrees = Counter()
    ww_codegrees = Counter()
    for v_set, w_set in groups:
        for pair in combinations(sorted(v_set), 2):
            vv_codegrees[pair] += 1
        for pair in combinations(sorted(w_set), 2):
            ww_codegrees[pair] += 1
    c_vv = sum(choose2(value) for value in vv_codegrees.values())
    c_ww = sum(choose2(value) for value in ww_codegrees.values())

    v_overlap = Counter()
    w_overlap = Counter()
    for first, second in combinations(range(len(groups)), 2):
        v_overlap[first, second] = len(groups[first][0] & groups[second][0])
        w_overlap[first, second] = len(groups[first][1] & groups[second][1])
    assert l_v == sum(v_overlap.values())
    assert l_w == sum(w_overlap.values())
    assert c_vv == sum(choose2(value) for value in v_overlap.values())
    assert c_ww == sum(choose2(value) for value in w_overlap.values())
    assert mixed_collision == sum(
        v_overlap[pair] * w_overlap[pair] for pair in v_overlap
    )

    collision_upper = c_vv + c_ww + min(l_v, l_w)
    assert mixed_collision <= collision_upper
    assert incidence <= support + mixed_collision
    assert incidence <= support + collision_upper
    assert incidence * incidence <= support * (incidence + 2 * mixed_collision)

    minimum_load_sum = sum(
        min(v_load[v], w_load[w]) for v, w in mixed_codegrees
    )
    layer_sum = 0
    for level in range(1, max([0, *v_load.values(), *w_load.values()]) + 1):
        layer_sum += sum(
            v_load[v] >= level and w_load[w] >= level
            for v, w in mixed_codegrees
        )
    assert minimum_load_sum == layer_sum
    assert incidence <= minimum_load_sum


def audit_parts(
    groups: list[
        tuple[dict[int, int], dict[int, int]]
    ]
) -> None:
    """Check the common-key neighbour-fibre multigraph decomposition."""

    for role_index in (0, 1):
        full_collision = 0
        cross_collision = 0
        star_upper = 0
        cross_codegrees = Counter()
        for first_group, second_group in combinations(range(len(groups)), 2):
            first_parts = groups[first_group][role_index]
            second_parts = groups[second_group][role_index]
            common_keys = sorted(set(first_parts) & set(second_parts))
            edge_count = len(common_keys)
            full_collision += choose2(edge_count)
            left_degrees = Counter(first_parts[key] for key in common_keys)
            right_degrees = Counter(second_parts[key] for key in common_keys)
            pair_multiplicity = Counter(
                (first_parts[key], second_parts[key]) for key in common_keys
            )
            disjoint_pairs = (
                choose2(edge_count)
                - sum(choose2(value) for value in left_degrees.values())
                - sum(choose2(value) for value in right_degrees.values())
                + sum(choose2(value) for value in pair_multiplicity.values())
            )
            assert disjoint_pairs >= 0
            maximum_degree = max(
                [0, *left_degrees.values(), *right_degrees.values()]
            )
            assert choose2(edge_count) <= (
                disjoint_pairs + edge_count * max(0, maximum_degree - 1)
            )
            cross_collision += disjoint_pairs
            star_upper += edge_count * max(0, maximum_degree - 1)

        all_keys = sorted(
            set().union(*(set(group[role_index]) for group in groups))
        ) if groups else []
        for first_key, second_key in combinations(all_keys, 2):
            load = sum(
                first_key in group[role_index]
                and second_key in group[role_index]
                and group[role_index][first_key]
                != group[role_index][second_key]
                for group in groups
            )
            if load:
                cross_codegrees[first_key, second_key] = load
        assert cross_collision == sum(
            choose2(value) for value in cross_codegrees.values()
        )
        assert full_collision <= cross_collision + star_upper


def audit_physical_bundles(
    groups: list[tuple[dict[int, int], dict[int, int]]],
    physical: tuple[dict[int, int], dict[int, int]],
) -> None:
    """Check the exact bundle identity when parts encode physical edges."""

    for role_index in (0, 1):
        full_collision = 0
        cross_collision = 0
        bundle_collision = 0
        for first_group, second_group in combinations(range(len(groups)), 2):
            first_parts = groups[first_group][role_index]
            second_parts = groups[second_group][role_index]
            common_keys = sorted(set(first_parts) & set(second_parts))
            for first_key, second_key in combinations(common_keys, 2):
                same_physical = (
                    physical[role_index][first_key]
                    == physical[role_index][second_key]
                )
                assert (first_parts[first_key] == first_parts[second_key]) == (
                    second_parts[first_key] == second_parts[second_key]
                ) == same_physical
                full_collision += 1
                if same_physical:
                    bundle_collision += 1
                else:
                    cross_collision += 1
        assert full_collision == cross_collision + bundle_collision


def exhaustive() -> None:
    subsets = [frozenset(i for i in range(2) if mask & (1 << i)) for mask in range(4)]
    group_types = list(product(subsets, repeat=2))
    for number_groups in range(1, 5):
        for rows in product(group_types, repeat=number_groups):
            audit(list(rows))


def random_checks() -> None:
    rng = Random(1208)
    for _ in range(10_000):
        nv = rng.randrange(1, 9)
        nw = rng.randrange(1, 9)
        groups = []
        for _ in range(rng.randrange(1, 13)):
            v_set = frozenset(v for v in range(nv) if rng.randrange(3) == 0)
            w_set = frozenset(w for w in range(nw) if rng.randrange(3) == 0)
            groups.append((v_set, w_set))
        audit(groups)

        parted_groups = []
        for v_set, w_set in groups:
            parted_groups.append(
                (
                    {key: rng.randrange(4) for key in v_set},
                    {key: rng.randrange(4) for key in w_set},
                )
            )
        audit_parts(parted_groups)

        physical = (
            {key: rng.randrange(max(1, nv // 2)) for key in range(nv)},
            {key: rng.randrange(max(1, nw // 2)) for key in range(nw)},
        )
        bundle_groups = []
        for group_index, (v_set, w_set) in enumerate(groups):
            # The group-dependent prefix makes the part map injective on
            # distinct physical edges while keeping equal physical edges
            # in one part.
            bundle_groups.append(
                (
                    {
                        key: 100 * group_index + physical[0][key]
                        for key in v_set
                    },
                    {
                        key: 100 * group_index + physical[1][key]
                        for key in w_set
                    },
                )
            )
        audit_physical_bundles(bundle_groups, physical)


def integer_kernel() -> None:
    for a in range(40):
        for b in range(40):
            assert a * b <= choose2(a) + choose2(b) + min(a, b)
            if abs(a - b) in (0, 1):
                assert a * b == choose2(a) + choose2(b) + min(a, b)


def main() -> None:
    integer_kernel()
    exhaustive()
    random_checks()
    print("SWAP MIXED MULTIPLICITY SAME-SIDE COLLAPSE: PASS")


if __name__ == "__main__":
    main()
