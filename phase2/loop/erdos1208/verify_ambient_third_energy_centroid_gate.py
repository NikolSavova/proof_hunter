#!/usr/bin/env python3
"""Exact regression checks for AMBIENT_THIRD_ENERGY_CENTROID_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points, side_length
from verify_orthogonal_energy_product_ruler_barrier import squared_distance_sidon
from verify_third_additive_energy_barrier import parabola, transform
from verify_transverse_closure_witness import POINTS
from verify_transverse_row_source_c4 import SOURCE_POINTS


Point = tuple[int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def norm(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def third_representations(points: list[Point]) -> Counter[Point]:
    pair_sums: Counter[Point] = Counter(
        add(first, second) for first in points for second in points
    )
    triples: Counter[Point] = Counter()
    for pair_sum, multiplicity in pair_sums.items():
        for point in points:
            triples[add(pair_sum, point)] += multiplicity
    return triples


def difference_set(points: list[Point]) -> set[Point]:
    return {subtract(first, second) for first in points for second in points}


def unordered_triple_fibres(
    points: list[Point],
) -> dict[Point, list[tuple[int, int, int]]]:
    fibres: dict[Point, list[tuple[int, int, int]]] = defaultdict(list)
    for indices in combinations(range(len(points)), 3):
        total = (sum(points[i][0] for i in indices), sum(points[i][1] for i in indices))
        fibres[total].append(indices)
    return fibres


def profile(points: list[Point]) -> tuple[int, int, int, int, int, int]:
    assert squared_distance_sidon(points)
    k = len(points)
    m = side_length(points)
    triples = third_representations(points)
    energy = sum(value * value for value in triples.values())

    # Exact complete-difference expansion (3.4).
    differences = difference_set(points)
    n = len(differences)
    assert n == k * (k - 1) + 1
    c = k - 1
    triple_difference_count = energy - (c**3 + 3 * c * c + 3 * c * n)
    assert triple_difference_count >= 0

    fibres = unordered_triple_fibres(points)
    unordered_collisions = 0
    inertia_loads: Counter[int] = Counter()
    for total, members in fibres.items():
        # Pair-sum uniqueness makes every common-sum class a matching.
        for first, second in combinations(members, 2):
            assert set(first).isdisjoint(second)
            unordered_collisions += 1

            first_moment = sum(norm(points[i]) for i in first)
            second_moment = sum(norm(points[i]) for i in second)
            relative_inertia_sum = (
                3 * (first_moment + second_moment) - 2 * norm(total)
            )
            assert 0 <= relative_inertia_sum <= 12 * m * m
            inertia_loads[relative_inertia_sum] += 1

    six_distinct = 36 * 2 * unordered_collisions
    # sum_s t_s(t_s-1) is twice the unordered pair count.
    assert six_distinct == 36 * sum(
        len(members) * (len(members) - 1) for members in fibres.values()
    )

    # Every six-distinct ordered configuration is part of the full energy.
    assert six_distinct <= energy
    # Integer form of E_3 >= k^6/(512m^2).
    assert 512 * m * m * energy >= k**6

    maximum_inertia_load = max(inertia_loads.values(), default=0)
    return (
        k,
        m,
        energy,
        six_distinct,
        max((len(members) for members in fibres.values()), default=0),
        maximum_inertia_load,
    )


def main() -> None:
    families = [
        ("closure-30", POINTS[:30], (30, 150, 172_866, 15_264, 3, 2)),
        ("closure-40", POINTS[:40], (40, 223, 427_252, 49_680, 5, 2)),
        ("closure-80", POINTS[:80], (80, 719, 3_596_786, 544_536, 6, 2)),
        (
            "closure-120",
            POINTS[:120],
            (120, 1_514, 12_824_964, 2_489_760, 6, 3),
        ),
        ("source-45", SOURCE_POINTS, (45, 324, 586_101, 51_336, 4, 2)),
        (
            "perpendicular-ruler-40",
            ruler_points(),
            (40, 3_202, 396_988, 19_656, 3, 1),
        ),
        ("Costas-22", transformed_costas(23), (22, 131, 106_222, 37_368, 4, 2)),
        (
            "parabola-image-127",
            transform(parabola(127)),
            (127, 20_831, 86_658_955, 72_011_880, 28, 3),
        ),
    ]

    for name, points, expected in families:
        actual = profile(points)
        assert actual == expected, (name, actual, expected)
        k, m, energy, six_distinct, maximum_fibre, inertia_load = actual
        print(
            name,
            actual,
            "energy/(k^3+m^2)",
            energy / (k**3 + m * m),
            "C6/m^2",
            six_distinct / (m * m),
            "max-fibre",
            maximum_fibre,
            "max-inertia-load",
            inertia_load,
        )

    print("ambient third-energy centroid gate: PASS")


if __name__ == "__main__":
    main()
