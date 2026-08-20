#!/usr/bin/env python3
"""Exact finite certificates for the bilinear edge-charge barrier."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from verify_orthogonal_energy_product_ruler_barrier import (
    erdos_turan,
    squared_distance_sidon,
)


Point = tuple[int, int]

GADGET: list[Point] = [
    (0, 2),
    (2, 31),
    (17, 25),
    (70, 14),
    (39, 9),
    (46, 1),
]
PARAMETERS: dict[int, tuple[int, Point, int]] = {
    1: (9_741, (93, 45), 508_751),
    3: (3_014, (77, 3), 389_409),
    18: (8_611, (41, 59), 826_258),
    43: (4_201, (-37, -40), 73_645),
}


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def scale(factor: int, point: Point) -> Point:
    return factor * point[0], factor * point[1]


def charge(left: Point, right: Point, coefficient: int) -> int:
    dot = left[0] * right[0] + left[1] * right[1]
    determinant = left[0] * right[1] - left[1] * right[0]
    return dot + coefficient * determinant


def clean_sources(points: list[Point]) -> tuple[Point, list[Point]]:
    difference = subtract(points[0], points[1])
    pair_by_sum = {
        add(points[first], points[second]): (first, second)
        for first, second in combinations(range(len(points)), 2)
    }
    starts: list[Point] = []
    for pair_sum, (first, second) in pair_by_sum.items():
        target = pair_by_sum.get(add(pair_sum, difference))
        if target is None:
            continue
        if len({0, 1, first, second, *target}) == 6:
            starts.append(subtract(points[first], points[second]))
    return difference, starts


def construction(coefficient: int) -> list[Point]:
    source = subtract(GADGET[2], GADGET[3])
    null_direction = (
        source[1] + coefficient * source[0],
        -source[0] + coefficient * source[1],
    )
    assert charge(source, null_direction, coefficient) == 0

    length_scale, translation_direction, translation_scale = PARAMETERS[coefficient]
    translation = scale(translation_scale, translation_direction)
    ruler = erdos_turan(17, 8)
    arm = [
        add(translation, scale(length_scale * mark, null_direction))
        for mark in ruler
    ]
    return GADGET + arm


def profile(coefficient: int) -> tuple[int, int, Point, int, int, int, int]:
    points = construction(coefficient)
    assert squared_distance_sidon(points)
    difference, sources = clean_sources(points)
    assert len(sources) == 1

    all_edges = [
        subtract(points[first], points[second])
        for first, second in combinations(range(len(points)), 2)
    ]
    loads = Counter(
        charge(source, edge, coefficient)
        for source in sources
        for edge in all_edges
    )
    mass = len(sources) * len(all_edges)
    energy = sum(load * load for load in loads.values())
    return (
        coefficient,
        len(points),
        difference,
        len(sources),
        mass,
        energy,
        max(loads.values()),
    )


def main() -> None:
    for coefficient in PARAMETERS:
        actual = profile(coefficient)
        expected = (coefficient, 14, (-2, -29), 1, 91, 1_183, 28)
        assert actual == expected, (actual, expected)
        print(actual, "normalized", actual[5] / actual[4])
    print("bilinear edge-charge barrier: PASS")


if __name__ == "__main__":
    main()
