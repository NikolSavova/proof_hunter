#!/usr/bin/env python3
"""Exact checks for DILATED_INTERNAL_PAIR_SUM_CHARGE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points, side_length
from verify_ambient_third_energy_centroid_gate import (
    add,
    subtract,
    unordered_triple_fibres,
)
from verify_orthogonal_energy_product_ruler_barrier import squared_distance_sidon
from verify_third_additive_energy_barrier import parabola
from verify_transverse_closure_witness import POINTS
from verify_transverse_row_source_c4 import SOURCE_POINTS


Point = tuple[int, int]
Profile = tuple[int, int, Point, int, int, int, int, int, int]


def clean_start_fibres(points: list[Point]) -> dict[Point, list[Point]]:
    output: dict[Point, list[Point]] = defaultdict(list)
    for members in unordered_triple_fibres(points).values():
        for first, second in combinations(members, 2):
            assert set(first).isdisjoint(second)
            for left, right in ((first, second), (second, first)):
                for distinguished_left in left:
                    start = (
                        sum(
                            points[index][0]
                            for index in left
                            if index != distinguished_left
                        ),
                        sum(
                            points[index][1]
                            for index in left
                            if index != distinguished_left
                        ),
                    )
                    for distinguished_right in right:
                        difference = subtract(
                            points[distinguished_left],
                            points[distinguished_right],
                        )
                        output[difference].append(start)

    assert all(len(starts) == len(set(starts)) for starts in output.values())
    return output


def dilation(point: Point) -> Point:
    return 3 * (point[0] - point[1]), 3 * (point[0] + point[1])


def difference_representations(values: list[Point]) -> Counter[Point]:
    return Counter(subtract(first, second) for first in values for second in values)


def profile(points: list[Point]) -> Profile:
    assert squared_distance_sidon(points)
    k = len(points)
    m = side_length(points)
    fibres = clean_start_fibres(points)
    difference = max(fibres, key=lambda value: len(fibres[value]))
    starts = fibres[difference]
    pair_sums = [
        add(points[first], points[second])
        for first, second in combinations(range(k), 2)
    ]
    assert len(pair_sums) == len(set(pair_sums))

    loads: Counter[Point] = Counter()
    for start in starts:
        for pair_sum in pair_sums:
            loads[add(start, dilation(pair_sum))] += 1

    mass = len(starts) * len(pair_sums)
    energy = sum(load * load for load in loads.values())
    assert energy >= mass
    assert len(loads) * energy >= mass * mass
    assert len(loads) <= (14 * m + 1) ** 2

    # On the moderate families, independently check the resonance formula
    # E=sum_w r_(Sigma-Sigma)(w) r_(H-H)(-Lambda w).
    if k <= 43:
        pair_differences = difference_representations(pair_sums)
        start_differences = difference_representations(starts)
        resonance_energy = sum(
            multiplicity
            * start_differences.get(
                tuple(-coordinate for coordinate in dilation(difference)),
                0,
            )
            for difference, multiplicity in pair_differences.items()
        )
        assert resonance_energy == energy
        assert pair_differences[(0, 0)] * start_differences[(0, 0)] == mass

    return (
        k,
        m,
        difference,
        len(starts),
        len(pair_sums),
        mass,
        len(loads),
        energy,
        max(loads.values()),
    )


def transformed_parabola_43() -> list[Point]:
    return [
        (31 * x - 42 * y, -3 * x + 4 * y)
        for x, y in parabola(43)
    ]


def main() -> None:
    families: list[tuple[str, list[Point], Profile]] = [
        (
            "closure-30",
            POINTS[:30],
            (30, 150, (-15, -19), 14, 435, 6_090, 6_075, 6_120, 2),
        ),
        (
            "closure-40",
            POINTS[:40],
            (40, 223, (-12, -18), 23, 780, 17_940, 17_836, 18_148, 2),
        ),
        (
            "closure-80",
            POINTS[:80],
            (80, 719, (-2, 0), 63, 3_160, 199_080, 197_022, 203_248, 3),
        ),
        (
            "closure-120",
            POINTS[:120],
            (120, 1_514, (66, 14), 127, 7_140, 906_780, 891_299, 938_304, 4),
        ),
        (
            "source-45",
            SOURCE_POINTS,
            (45, 324, (-45, -21), 22, 990, 21_780, 21_573, 22_200, 3),
        ),
        (
            "perpendicular-ruler-40",
            ruler_points(),
            (40, 3_202, (0, -314), 14, 780, 10_920, 10_920, 10_920, 1),
        ),
        (
            "Costas-22",
            transformed_costas(23),
            (22, 131, (13, 21), 34, 231, 7_854, 7_818, 7_926, 2),
        ),
        (
            "parabola-image-43",
            transformed_parabola_43(),
            (43, 2_586, (396, -38), 171, 903, 154_413, 153_120, 156_999, 2),
        ),
    ]

    for name, points, expected in families:
        actual = profile(points)
        assert actual == expected, (name, actual, expected)
        mass = actual[5]
        energy = actual[7]
        print(
            name,
            actual,
            "normalized-energy",
            energy / mass,
            "image-density",
            actual[6] / mass,
        )

    print("dilated internal pair-sum charge: PASS")


if __name__ == "__main__":
    main()
