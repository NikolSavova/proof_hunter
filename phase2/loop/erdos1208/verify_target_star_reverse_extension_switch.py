#!/usr/bin/env python3
"""Verify the target-star/reverse-extension switches for the #1208 gate."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_high_codegree_replacement_completion import add, subtract, tables
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Profile = tuple[int, ...]


def endpoint_families(
    points: list[Point],
    edge_at_sum: dict[Point, tuple[int, int]],
    anchor: dict[Point, tuple[int, int]],
) -> tuple[dict[Point, set[Point]], dict[Point, set[Point]], dict[Point, set[Point]]]:
    pair_sums = set(edge_at_sum)
    stars: dict[Point, set[Point]] = {}
    disjoint: dict[Point, set[Point]] = {}
    boundary: dict[Point, set[Point]] = {}
    for g, (head, tail) in anchor.items():
        x, y = points[tail], points[head]
        star = {
            add(x, points[leaf])
            for leaf in range(len(points))
            if leaf not in (head, tail)
        }
        meeting = {
            start
            for start in pair_sums
            if add(start, g) in pair_sums
            and set(edge_at_sum[start]) & set(edge_at_sum[add(start, g)])
        }
        assert meeting == star
        assert len(star) == len(points) - 2

        bad = {
            start
            for start in pair_sums
            if add(start, g) in pair_sums
            and not (set(edge_at_sum[start]) & set(edge_at_sum[add(start, g)]))
        }
        wrong = {
            start
            for start in bad
            if head in edge_at_sum[start] or tail in edge_at_sum[add(start, g)]
        }
        stars[g] = star
        disjoint[g] = bad
        boundary[g] = wrong
        assert len(wrong) <= 2 * (len(points) - 2)
    return stars, disjoint, boundary


def profile(points: list[Point]) -> Profile:
    edge_at_sum, _, anchor = tables(points)
    fibres = clean_start_fibres(points)
    fibre_sets = {q: set(starts) for q, starts in fibres.items()}
    stars, disjoint, boundary = endpoint_families(points, edge_at_sum, anchor)

    # The abstract partition is checked independently of records.
    max_boundary = 0
    for g in anchor:
        clean = fibre_sets.get(g, set())
        assert clean <= disjoint[g]
        assert disjoint[g] == clean | boundary[g]
        assert not (clean & boundary[g])
        max_boundary = max(max_boundary, len(boundary[g]))

    common: dict[tuple[Point, Point], list[Point]] = defaultdict(list)
    replacement_clean = replacement_boundary = 0
    for q, starts in fibres.items():
        for first in starts:
            for second in starts:
                if first == second:
                    continue
                common[first, second].append(q)
                first_target = add(first, q)
                second_target = add(second, q)
                if not (
                    set(edge_at_sum[first_target])
                    & set(edge_at_sum[second_target])
                ):
                    continue
                g = subtract(second, first)
                assert g in anchor
                assert first_target in stars[g]
                # Fixed-fibre star-to-matching: the source is on the
                # disjoint side of the canonical three-way partition.
                assert first in disjoint[g]
                assert second == add(first, g)
                if first in fibre_sets.get(g, set()):
                    replacement_clean += 1
                else:
                    assert first in boundary[g]
                    replacement_boundary += 1

    one_clean = one_boundary = 0
    for (first, second), translations in common.items():
        # Use one source orientation.  The old D_one sum contains the two
        # V orientations but has the same geometric base records.
        if second < first:
            continue
        for q, q_prime in combinations(sorted(translations), 2):
            first_q = set(edge_at_sum[add(first, q)])
            first_q_prime = set(edge_at_sum[add(first, q_prime)])
            second_q = set(edge_at_sum[add(second, q)])
            second_q_prime = set(edge_at_sum[add(second, q_prime)])
            first_good = bool(first_q & first_q_prime)
            second_good = bool(second_q & second_q_prime)
            if first_good == second_good:
                continue

            good, bad = (first, second) if first_good else (second, first)
            g = subtract(q_prime, q)
            assert g in anchor
            v, w = add(good, q), add(bad, q)

            # Exact reverse-target-fibre switch.
            assert v in stars[g]
            assert w in disjoint[g]
            assert good in fibre_sets[q] & fibre_sets[q_prime]
            assert bad in fibre_sets[q] & fibre_sets[q_prime]
            assert add(v, g) == add(good, q_prime)
            assert add(w, g) == add(bad, q_prime)
            assert subtract(v, q) == good
            assert subtract(w, q) == bad

            head, tail = anchor[g]
            wrong_side = head in edge_at_sum[w] or tail in edge_at_sum[add(w, g)]
            if w in fibre_sets.get(g, set()):
                assert not wrong_side
                one_clean += 2
            else:
                assert wrong_side and w in boundary[g]
                one_boundary += 2

    clean_mass = sum(map(len, fibres.values()))
    k = len(points)
    N = k * (k - 1) // 2
    assert replacement_clean + replacement_boundary <= 2 * (k - 2) * clean_mass
    assert one_clean + one_boundary <= 4 * (k - 2) * sum(
        len(starts) * (len(starts) - 1) for starts in fibres.values()
    )
    assert one_clean + one_boundary <= 4 * (k - 2) * (N - 1) * clean_mass

    return (
        len(points),
        sum(map(len, fibres.values())),
        replacement_clean,
        replacement_boundary,
        one_clean,
        one_boundary,
        max_boundary,
    )


def main() -> None:
    families = [
        # The 16-point prefix retains nontrivial closure fibres while
        # avoiding the deliberately enormous full-closure stress, whose
        # 36 million ordered within-fibre pairs add no new local cases.
        ("closure-16", POINTS[:16]),
        ("Costas-22", transformed_costas(23)),
        ("parabola-19", transformed_parabola_43()[:19]),
        ("ruler-40", ruler_points()),
    ]
    profiles = {name: profile(points) for name, points in families}
    for name, result in profiles.items():
        print(name, result)

    # The transformed parabola has genuine wrong-side records, so the
    # boundary term in the theorem cannot be deleted.
    assert profiles["parabola-19"][5] == 156
    assert profiles["parabola-19"][4] == 1366
    print("target-star reverse extension switch: PASS")


if __name__ == "__main__":
    main()
