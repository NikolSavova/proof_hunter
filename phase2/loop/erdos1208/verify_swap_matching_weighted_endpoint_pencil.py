#!/usr/bin/env python3
"""Exact checks for the weighted endpoint-pencil gate."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import sys

from analyze_affine_costas_energy import is_distance_sidon, welch
from analyze_swap_optimal_nested_cores import profile, transformed_costas
from verify_closed_fibre_q_height_layered_barrier import (
    lifted_residue_parabola,
)
from verify_orthogonal_two_support_gate import difference_set
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rotate,
    subtract,
)
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]


def weighted_pencil_statistics(
    endpoint_sets: dict[int, frozenset[int]],
    weights: dict[tuple[int, int], int],
) -> tuple[int, int, int, Fraction]:
    adjacency: dict[int, dict[int, int]] = {
        vertex: {} for vertex in endpoint_sets
    }
    for (first, second), weight in weights.items():
        assert first < second and weight > 0
        assert endpoint_sets[first].isdisjoint(endpoint_sets[second])
        adjacency[first][second] = weight
        adjacency[second][first] = weight

    edge_mass = sum(weights.values())
    contact_wedges = 0
    pencil_mass = 0
    lambda_sum = 0
    theta = Fraction(0)
    for centre, neighbours in adjacency.items():
        rows = list(neighbours.items())
        contact_wedges += sum(
            first_weight * second_weight
            for (
                (first, first_weight),
                (second, second_weight),
            ) in combinations(rows, 2)
            if endpoint_sets[first] & endpoint_sets[second]
        )
        for endpoint in set().union(
            *(endpoint_sets[neighbour] for neighbour in neighbours)
        ):
            local_weights = [
                weight
                for neighbour, weight in rows
                if endpoint in endpoint_sets[neighbour]
            ]
            load = sum(local_weights)
            pair_mass = (
                load * load
                - sum(weight * weight for weight in local_weights)
            ) // 2
            lambda_sum += load
            pencil_mass += pair_mass
            if load:
                theta = max(theta, Fraction(pair_mass, load))

    assert contact_wedges <= pencil_mass
    assert lambda_sum <= 8 * edge_mass
    assert pencil_mass <= 8 * theta * edge_mass
    return edge_mass, contact_wedges, pencil_mass, theta


def verify_finite_weighted_systems() -> None:
    endpoint_sets = {
        0: frozenset((0, 1, 2, 3)),
        1: frozenset((4, 5, 6, 7)),
        2: frozenset((0, 8, 9, 10)),
        3: frozenset((4, 11, 12, 13)),
        4: frozenset((1, 11, 14, 15)),
        5: frozenset((5, 8, 16, 17)),
    }
    allowed = [
        pair
        for pair in combinations(endpoint_sets, 2)
        if endpoint_sets[pair[0]].isdisjoint(endpoint_sets[pair[1]])
    ]
    for mask in range(1 << len(allowed)):
        weights = {
            pair: 1 + ((mask + index) % 3)
            for index, pair in enumerate(allowed)
            if mask >> index & 1
        }
        weighted_pencil_statistics(endpoint_sets, weights)

    # A single heavy parallel fibre contributes no contact-pencil pair mass.
    result = weighted_pencil_statistics(
        {0: frozenset(range(4)), 1: frozenset(range(4, 8))},
        {(0, 1): 1000},
    )
    assert result == (1000, 0, 0, Fraction(0))
    weighted_pencil_statistics(
        {
            0: frozenset(),
            1: frozenset((0, 1)),
            2: frozenset((2, 3, 4, 5)),
        },
        {(0, 1): 7, (0, 2): 11},
    )


def edge_roles(
    component: Point,
    centre: Point,
    p_value: Point,
    q_value: Point,
) -> tuple[Point, ...]:
    ell = add(component, linear(centre))
    base = subtract(centre, q_value)
    neighbour = add(centre, subtract(p_value, q_value))
    radius = add(component, rotate(add(centre, p_value)))
    return (
        base,
        neighbour,
        centre,
        add(neighbour, radius),
        add(centre, radius),
        add(component, linear(neighbour)),
        ell,
    )


def verify_centre_normal_form() -> None:
    component = (11, -7)
    centre = (3, 8)
    p_value = (-5, 4)
    q_value = (6, -2)
    ell = add(component, linear(centre))
    roles = edge_roles(component, centre, p_value, q_value)
    assert roles == (
        subtract(centre, q_value),
        add(centre, subtract(p_value, q_value)),
        centre,
        subtract(add(ell, linear(p_value)), q_value),
        add(ell, rotate(p_value)),
        add(ell, linear(subtract(p_value, q_value))),
        ell,
    )
    base, neighbour = roles[:2]
    assert subtract(centre, base) == q_value
    assert subtract(neighbour, base) == p_value


def verify_same_oriented_endpoint_collision() -> None:
    component = (13, -4)
    centre = (-2, 7)
    endpoint = (19, 11)
    other_first = (5, -3)
    other_second = (-8, 6)
    first_neighbour = subtract(endpoint, other_first)
    second_neighbour = subtract(endpoint, other_second)
    first_q = (4, -9)
    second_q = (-7, 3)
    first_p = add(first_q, subtract(first_neighbour, centre))
    second_p = add(second_q, subtract(second_neighbour, centre))

    first_roles = edge_roles(component, centre, first_p, first_q)
    second_roles = edge_roles(component, centre, second_p, second_q)
    delta = subtract(first_neighbour, second_neighbour)
    rho = rotate(subtract(first_p, second_p))
    differences = tuple(
        subtract(first_roles[index], second_roles[index])
        for index in (0, 1, 4, 3, 5)
    )
    assert differences == (
        add(delta, rotate(rho)),
        delta,
        rho,
        add(delta, rho),
        linear(delta),
    )
    assert delta == subtract(other_second, other_first)
    assert subtract(first_p, second_p) == tuple(-x for x in rotate(rho))
    assert subtract(first_q, second_q) == tuple(
        -x for x in add(delta, rotate(rho))
    )


def verify_role_refined_key_rigidity() -> None:
    # The integer parabola is vector-Sidon: a nonzero directed difference
    # recovers both the index difference and the index sum.
    points = [(index, index * index) for index in range(7)]
    differences = {}
    for first, second in product(range(len(points)), repeat=2):
        if first == second:
            continue
        value = subtract(points[first], points[second])
        assert value not in differences
        differences[value] = first, second

    centre = (17, -9)
    endpoint = points[0]
    displacements = {
        index: subtract(subtract(endpoint, points[index]), centre)
        for index in range(1, len(points))
    }
    q_fibres = {
        index: [
            (3 * index + offset, 5 * index - 2 * offset)
            for offset in range(1 + index % 3)
        ]
        for index in displacements
    }

    key_neighbour_pairs: dict[
        tuple[Point, Point], set[tuple[int, int]]
    ] = {}
    for first_index, second_index in product(displacements, repeat=2):
        if first_index == second_index:
            continue
        first_t = displacements[first_index]
        second_t = displacements[second_index]
        for first_q in q_fibres[first_index]:
            for second_q in q_fibres[second_index]:
                first_p = add(first_q, first_t)
                second_p = add(second_q, second_t)
                key = (
                    subtract(first_t, second_t),
                    rotate(subtract(first_p, second_p)),
                )
                key_neighbour_pairs.setdefault(key, set()).add(
                    (first_index, second_index)
                )
    assert all(len(rows) == 1 for rows in key_neighbour_pairs.values())


def verify_common_r_unification() -> None:
    component = (9, -14)
    centre = (7, 2)
    first_t = (-5, 8)
    second_t = (6, -3)
    first_q = (4, 11)
    second_q = (-8, 5)
    first_p = add(first_q, first_t)
    second_p = add(second_q, second_t)
    first_roles = edge_roles(component, centre, first_p, first_q)
    second_roles = edge_roles(component, centre, second_p, second_q)

    displacement = subtract(first_t, second_t)
    eta = subtract(first_q, second_q)
    middle = rotate(add(eta, displacement))
    last = add(middle, displacement)
    assert (
        subtract(first_roles[0], second_roles[0]),
        subtract(first_roles[4], second_roles[4]),
        subtract(first_roles[3], second_roles[3]),
    ) == (tuple(-entry for entry in eta), middle, last)

    common_r = last
    common_displacement = tuple(-entry for entry in displacement)
    assert add(common_r, common_displacement) == middle
    assert rotate(add(common_r, linear(common_displacement))) == tuple(
        -entry for entry in eta
    )
    assert add(
        common_r,
        subtract(rotate(middle), middle),
    ) == tuple(-entry for entry in eta)


def verify_key_support_collision_fork() -> None:
    # Each entry is the multiplicity of one decorated key.  Exhausting
    # small lists checks both the local Cauchy fork and its global sum.
    local_rows: list[tuple[int, int, int]] = []
    for length in range(1, 6):
        for loads in product(range(1, 5), repeat=length):
            mass = sum(loads)
            support = len(loads)
            collisions = sum(load * (load - 1) // 2 for load in loads)
            assert mass * mass <= support * (mass + 2 * collisions)
            local_rows.append((mass, support, collisions))
    for first in local_rows[::97]:
        for second in local_rows[::113]:
            mass = first[0] + second[0]
            support = first[1] + second[1]
            collisions = first[2] + second[2]
            assert mass * mass <= support * (mass + 2 * collisions)
            if mass > 2 * support:
                assert collisions * 4 * support >= mass * mass


def verify_collision_orthogonal_switch() -> None:
    component = (5, -12)
    centre = (8, 3)
    first_t = (-4, 9)
    second_t = (7, -6)
    first_q = (11, -2)
    second_q = (-3, 10)
    shift = (6, 5)
    first_q_prime = subtract(first_q, shift)
    second_q_prime = subtract(second_q, shift)
    ell = add(component, linear(centre))

    for displacement, q_value, q_prime in (
        (first_t, first_q, first_q_prime),
        (second_t, second_q, second_q_prime),
    ):
        x_value = subtract(centre, q_value)
        x_prime = subtract(centre, q_prime)
        y_value = add(ell, rotate(add(q_value, displacement)))
        y_prime = add(ell, rotate(add(q_prime, displacement)))
        z_value = add(ell, add(rotate(q_value), linear(displacement)))
        z_prime = add(ell, add(rotate(q_prime), linear(displacement)))
        assert subtract(x_value, x_prime) == tuple(-entry for entry in shift)
        assert subtract(y_value, y_prime) == rotate(shift)
        assert subtract(z_value, z_prime) == rotate(shift)

    assert subtract(first_q, second_q) == subtract(
        first_q_prime, second_q_prime
    )
    assert add(first_q, second_q_prime) == add(
        first_q_prime, second_q
    )

    representation_keys: dict[
        tuple[Point, Point, Point, Point], tuple[Point, Point]
    ] = {}
    for q_value in product(range(-2, 3), repeat=2):
        for displacement in product(range(-2, 3), repeat=2):
            p_value = add(q_value, displacement)
            x_value = subtract(centre, q_value)
            y_value = add(ell, rotate(p_value))
            key = (
                x_value,
                add(x_value, shift),
                y_value,
                subtract(y_value, rotate(shift)),
            )
            assert key not in representation_keys
            representation_keys[key] = q_value, displacement
            recovered_q = subtract(centre, key[0])
            rotated_p = subtract(key[2], ell)
            recovered_p = (rotated_p[1], -rotated_p[0])
            assert recovered_q == q_value
            assert recovered_p == p_value
            assert subtract(recovered_p, recovered_q) == displacement


def verify_second_generation_pencil_identity() -> None:
    universe = tuple((index, index * index + 1) for index in range(4))
    subsets = [
        frozenset(
            universe[index]
            for index in range(len(universe))
            if mask >> index & 1
        )
        for mask in range(1, 1 << len(universe))
    ]
    for fibres in product(subsets, repeat=3):
        key_collisions = 0
        for first_index, second_index in combinations(range(3), 2):
            cross = Counter(
                subtract(first, second)
                for first in fibres[first_index]
                for second in fibres[second_index]
            )
            key_collisions += sum(
                load * (load - 1) // 2
                for load in cross.values()
            )

        internal = [
            Counter(
                subtract(first, second)
                for first in fibre
                for second in fibre
                if first != second
            )
            for fibre in fibres
        ]
        switches = set().union(*(set(row) for row in internal))
        switch_pencil = 0
        switch_lambda = 0
        for switch in switches:
            weights = [row[switch] for row in internal if row[switch]]
            load = sum(weights)
            switch_lambda += load
            pair_mass = (
                load * load - sum(weight * weight for weight in weights)
            ) // 2
            switch_pencil += pair_mass
            assert pair_mass <= (load - max(weights)) * load
        assert switch_pencil == 2 * key_collisions
        assert switch_lambda == sum(
            len(fibre) * (len(fibre) - 1)
            for fibre in fibres
        )


def verify_genuine_profiles() -> None:
    expected = {
        17: (
            (5, 129, 202, (6, 5)),
            (5, 2, 3, 4, 2, 4, 2, 6, 1),
            (202, 200, 2),
            (4, 3_320, (1, 2), 1, 8, 428),
            (("nonpopular", 0, 160, 0, 0), ("popular", 4, 3_160, 1, 8)),
        ),
        23: (
            (12, 53_281, 70_261, (53, 12)),
            (12, 4, 4, 10, 3, 9, 3, 50, 2),
            (70_261, 67_245, 3_140),
            (6_280, 542_212, (5, 4), 2, 11_748, 67_882),
            (
                ("nonpopular", 0, 2_840, 0, 0),
                ("popular", 6_280, 539_372, 2, 11_748),
            ),
        ),
    }
    for prime, (
        target,
        copy_target,
        key_target,
        switch_target,
        cutoff_target,
    ) in expected.items():
        points, differences = transformed_costas(prime)
        _, summary, _ = profile(differences, points)
        actual = dict(summary["matching_weighted_endpoint_pencil_profile"])
        row = (
            actual["maximum_weighted_endpoint_pencil"],
            actual["endpoint_contact_weighted_wedges"],
            actual["endpoint_pencil_wedge_upper"],
            actual["maximum_contact_pencil_ratio"],
        )
        assert row == target, (prime, row, target)
        copy_row = summary["matching_endpoint_pencil_copy_profiles"][0][0]
        assert copy_row[:9] == copy_target, (prime, copy_row, copy_target)
        key_row = dict(summary["matching_endpoint_key_dichotomy"])
        assert (
            key_row["pair_mass"],
            key_row["support"],
            key_row["collisions"],
        ) == key_target
        assert key_row["pair_mass"] == actual["endpoint_pencil_wedge_upper"]
        assert key_row["pair_mass"] ** 2 <= key_row["support"] * (
            key_row["pair_mass"] + 2 * key_row["collisions"]
        )
        switch_row = dict(summary["matching_endpoint_collision_switch"])
        assert (
            switch_row["switch_pencil"],
            switch_row["switch_lambda"],
            switch_row["maximum_switch_ratio"],
            switch_row["maximum_switch_residual"],
            switch_row["switch_residual_product"],
            switch_row["parallel_wedges"],
        ) == switch_target
        assert switch_row["switch_pencil"] == 2 * key_row["collisions"]
        assert switch_row["switch_lambda"] <= 8 * switch_row["parallel_wedges"]
        assert (
            summary["matching_endpoint_collision_switch_cutoff"]
            == cutoff_target
        )


def verify_larger_profile() -> None:
    points, differences = transformed_costas(37)
    _, summary, _ = profile(differences, points)
    actual = dict(summary["matching_weighted_endpoint_pencil_profile"])
    assert actual["maximum_weighted_endpoint_pencil"] == 15
    assert actual["endpoint_contact_weighted_wedges"] == 617_488
    assert actual["endpoint_pencil_wedge_upper"] == 713_968
    assert actual["maximum_contact_pencil_ratio"] == (38, 7)
    copy_row = summary["matching_endpoint_pencil_copy_profiles"][0][0]
    assert copy_row[:9] == (15, 3, 6, 8, 3, 10, 3, 50, 5)
    key_row = dict(summary["matching_endpoint_key_dichotomy"])
    assert (
        key_row["pair_mass"],
        key_row["support"],
        key_row["collisions"],
    ) == (713_968, 672_204, 44_110)
    assert key_row["pair_mass"] == actual["endpoint_pencil_wedge_upper"]
    assert key_row["pair_mass"] ** 2 <= key_row["support"] * (
        key_row["pair_mass"] + 2 * key_row["collisions"]
    )
    switch_row = dict(summary["matching_endpoint_collision_switch"])
    assert (
        switch_row["switch_pencil"],
        switch_row["switch_lambda"],
        switch_row["maximum_switch_ratio"],
        switch_row["maximum_switch_residual"],
        switch_row["switch_residual_product"],
        switch_row["parallel_wedges"],
    ) == (88_220, 5_293_108, (11, 6), 3, 163_592, 661_754)
    assert switch_row["switch_pencil"] == 2 * key_row["collisions"]
    assert switch_row["switch_lambda"] <= 8 * switch_row["parallel_wedges"]
    assert summary["matching_endpoint_collision_switch_cutoff"] == (
        ("nonpopular", 72, 15_472, 1, 144),
        ("popular", 88_148, 5_277_636, 3, 163_448),
    )


def verify_closure_switch_profiles() -> None:
    expected = {
        40: (
            (212, 72_056, (2, 3), 9_184),
            (34_776, 34_670, 106),
            (
                ("nonpopular", 32, 44_400, 1, 56),
                ("popular", 180, 27_656, 1, 344),
            ),
        ),
        50: (
            (12, 7_232, (1, 2), 932),
            (3_803, 3_797, 6),
            (
                ("nonpopular", 8, 5_856, 1, 16),
                ("popular", 4, 1_376, 1, 8),
            ),
        ),
    }
    for size, (switch_target, key_target, cutoff_target) in expected.items():
        points = POINTS[:size]
        _, summary, _ = profile(difference_set(points), points)
        switch_row = dict(summary["matching_endpoint_collision_switch"])
        assert (
            switch_row["switch_pencil"],
            switch_row["switch_lambda"],
            switch_row["maximum_switch_ratio"],
            switch_row["parallel_wedges"],
        ) == switch_target
        key_row = dict(summary["matching_endpoint_key_dichotomy"])
        assert (
            key_row["pair_mass"],
            key_row["support"],
            key_row["collisions"],
        ) == key_target
        assert (
            summary["matching_endpoint_collision_switch_cutoff"]
            == cutoff_target
        )


def verify_lifted_parabola_switch_profile() -> None:
    points = lifted_residue_parabola(43)
    _, summary, _ = profile(difference_set(points), points)
    assert summary["matching_endpoint_key_dichotomy"] == (
        ("pair_mass", 87),
        ("support", 87),
        ("collisions", 0),
    )
    assert summary["matching_endpoint_collision_switch"] == (
        ("switch_pencil", 0),
        ("switch_lambda", 1_728),
        ("maximum_switch_ratio", (0, 1)),
        ("maximum_switch_residual", 0),
        ("switch_residual_product", 0),
        ("parallel_wedges", 216),
    )
    assert summary["matching_endpoint_collision_switch_cutoff"] == (
        ("nonpopular", 0, 0, 0, 0),
        ("popular", 0, 1_728, 0, 0),
    )


def verify_affine_neighbourhood_kill_search() -> None:
    rows = (
        (11, (-2, -3, -1, -1), (0, 20, 0)),
        (11, (-2, -3, -1, -2), (0, 0, 0)),
        (17, (-7, 4, -2, -2), (0, 476, 0)),
        (17, (-8, 5, -3, -1), (0, 84, 0)),
    )
    for prime, matrix, target in rows:
        a_value, b_value, c_value, d_value = matrix
        points = [
            (
                a_value * x_value + b_value * y_value,
                c_value * x_value + d_value * y_value,
            )
            for x_value, y_value in welch(prime)
        ]
        assert is_distance_sidon(points)
        _, summary, _ = profile(difference_set(points), points)
        switch_row = dict(summary["matching_endpoint_collision_switch"])
        assert (
            switch_row["switch_residual_product"],
            switch_row["parallel_wedges"],
            switch_row["maximum_switch_residual"],
        ) == target


def main() -> None:
    verify_finite_weighted_systems()
    verify_centre_normal_form()
    verify_same_oriented_endpoint_collision()
    verify_role_refined_key_rigidity()
    verify_common_r_unification()
    verify_key_support_collision_fork()
    verify_collision_orthogonal_switch()
    verify_second_generation_pencil_identity()
    verify_genuine_profiles()
    verify_lifted_parabola_switch_profile()
    verify_affine_neighbourhood_kill_search()
    if "--larger" in sys.argv:
        verify_larger_profile()
        verify_closure_switch_profiles()
    print("SWAP MATCHING WEIGHTED ENDPOINT-PENCIL GATE: PASS")


if __name__ == "__main__":
    main()
