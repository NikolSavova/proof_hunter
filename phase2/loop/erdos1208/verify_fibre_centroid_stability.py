#!/usr/bin/env python3
"""Exact checks for FIBRE_CENTROID_STABILITY.md."""

from __future__ import annotations

from collections import defaultdict
from math import ceil, sqrt

from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Record = tuple[Point, Point, Point]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def scale(multiplier: int, point: Point) -> Point:
    return multiplier * point[0], multiplier * point[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def point_sum(points: set[Point] | list[Point]) -> Point:
    return sum(point[0] for point in points), sum(point[1] for point in points)


def squared_norm(point: Point) -> int:
    return point[0] ** 2 + point[1] ** 2


def main() -> None:
    points = list(POINTS[:20])
    point_set = set(points)
    size = len(points)
    total = point_sum(points)
    side = max(
        max(point[coordinate] for point in points)
        - min(point[coordinate] for point in points)
        for coordinate in (0, 1)
    )

    fibres: dict[Point, list[Record]] = defaultdict(list)
    for first in points:
        for second in points:
            for third in points:
                if second == third:
                    continue
                output = add(first, rotate(subtract(second, third)))
                fibres[output].append((first, second, third))

    for output, fibre in fibres.items():
        coordinate_sets = [
            {record[coordinate] for record in fibre}
            for coordinate in range(3)
        ]
        height = len(fibre)
        assert all(len(coordinates) == height for coordinates in coordinate_sets)
        complements = [point_set - coordinates for coordinates in coordinate_sets]
        defect = size - height
        assert all(len(complement) == defect for complement in complements)

        first_complement, second_complement, third_complement = map(
            point_sum,
            complements,
        )
        right = add(
            subtract(total, first_complement),
            rotate(subtract(third_complement, second_complement)),
        )
        assert scale(height, output) == right

        # Multiply the centered identity by k to retain integer arithmetic.
        left_centered = scale(height, subtract(scale(size, output), total))
        first_centered = subtract(scale(size, first_complement), scale(defect, total))
        second_centered = subtract(scale(size, second_complement), scale(defect, total))
        third_centered = subtract(scale(size, third_complement), scale(defect, total))
        right_centered = add(
            scale(-1, first_centered),
            rotate(subtract(third_centered, second_centered)),
        )
        assert left_centered == right_centered
        assert squared_norm(left_centered) <= 18 * size**2 * defect**2 * side**2

    for defect in range(size):
        actual = sum(
            1 for fibre in fibres.values() if len(fibre) >= size - defect
        )
        radius = 3 * sqrt(2) * side * defect / (size - defect)
        bound = ceil((2 * radius + 2) ** 2)
        assert actual <= bound

    print(
        "fibre centroid stability",
        (size, len(fibres), max(map(len, fibres.values())), side),
    )
    print("fibre centroid stability: PASS")


if __name__ == "__main__":
    main()
