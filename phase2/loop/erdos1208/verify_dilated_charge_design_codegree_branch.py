#!/usr/bin/env python3
"""Exact checks for the design-codegree branch of the dilated charge."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_dilated_internal_pair_sum_charge import (
    add,
    dilation,
    transformed_parabola_43,
)
from verify_orthogonal_energy_product_ruler_barrier import squared_distance_sidon
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Pattern = tuple[int, ...]
Profile = tuple[int, int, Point, int, int, int, int]


COEFFICIENTS: tuple[Point, ...] = (
    (1, 0),
    (1, 0),
    (-1, 0),
    (-1, 0),
    (3, 3),
    (3, 3),
    (-3, -3),
    (-3, -3),
)


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def gaussian_multiply(left: Point, right: Point) -> Point:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def equality_pattern(row: tuple[int, ...]) -> Pattern:
    blocks: dict[int, int] = {}
    output: list[int] = []
    for label in row:
        if label not in blocks:
            blocks[label] = len(blocks)
        output.append(blocks[label])
    return tuple(output)


def merged_coefficients(pattern: Pattern) -> tuple[Point, ...]:
    coefficients = [(0, 0) for _ in range(max(pattern) + 1)]
    for block, coefficient in zip(pattern, COEFFICIENTS):
        coefficients[block] = add(coefficients[block], coefficient)
    active = tuple(value for value in coefficients if value != (0, 0))
    assert sum(value[0] for value in active) == 0
    assert sum(value[1] for value in active) == 0
    return active


def collision_rows(points: list[Point]) -> tuple[Point, int, list[tuple[int, ...]]]:
    pair_by_sum = {
        add(points[first], points[second]): (first, second)
        for first, second in combinations(range(len(points)), 2)
    }
    assert len(pair_by_sum) == len(points) * (len(points) - 1) // 2
    difference_endpoints = {
        subtract(points[first], points[second]): (first, second)
        for first in range(len(points))
        for second in range(len(points))
        if first != second
    }

    best_difference: Point | None = None
    best_starts: list[tuple[Point, tuple[int, int]]] = []
    for difference, fixed_endpoints in difference_endpoints.items():
        starts: list[tuple[Point, tuple[int, int]]] = []
        for start, start_endpoints in pair_by_sum.items():
            end_endpoints = pair_by_sum.get(add(start, difference))
            if end_endpoints is None:
                continue
            if len({*fixed_endpoints, *start_endpoints, *end_endpoints}) == 6:
                starts.append((start, start_endpoints))
        if len(starts) > len(best_starts):
            best_difference = difference
            best_starts = starts

    assert best_difference is not None
    loads: dict[Point, list[tuple[tuple[int, int], tuple[int, int]]]] = defaultdict(list)
    for start, start_endpoints in best_starts:
        for pair_sum, pair_endpoints in pair_by_sum.items():
            loads[add(start, dilation(pair_sum))].append(
                (start_endpoints, pair_endpoints)
            )

    rows: list[tuple[int, ...]] = []
    for records in loads.values():
        for first in records:
            for second in records:
                if first == second:
                    continue
                row = (*first[0], *second[0], *first[1], *second[1])

                # Check c+d-c'-d'+lambda(x+y-x'-y')=0.
                total = (0, 0)
                for role, coefficient in zip(row, COEFFICIENTS):
                    total = add(total, gaussian_multiply(coefficient, points[role]))
                assert total == (0, 0)
                rows.append(row)

    return best_difference, len(best_starts), rows


def profile(points: list[Point]) -> Profile:
    assert squared_distance_sidon(points)
    difference, height, rows = collision_rows(points)
    by_pattern: dict[Pattern, list[tuple[int, ...]]] = defaultdict(list)
    for row in rows:
        by_pattern[equality_pattern(row)].append(row)

    maximum_codegree = 0
    for pattern, pattern_rows in by_pattern.items():
        active = merged_coefficients(pattern)
        assert len(active) >= 3
        for first, second in combinations(range(8), 2):
            codegrees = Counter(
                (row[first], row[second]) for row in pattern_rows
            )
            maximum_codegree = max(
                maximum_codegree,
                max(codegrees.values(), default=0),
            )

    assert len(rows) <= 2048 * 4140 * len(points) ** 2 * maximum_codegree
    return (
        len(points),
        len(points) * (len(points) - 1) // 2,
        difference,
        height,
        len(rows),
        len(by_pattern),
        maximum_codegree,
    )


def main() -> None:
    families: list[tuple[str, list[Point], Profile]] = [
        (
            "closure-30",
            POINTS[:30],
            (30, 435, (15, 19), 14, 30, 7, 6),
        ),
        (
            "closure-40",
            POINTS[:40],
            (40, 780, (-12, -18), 23, 208, 29, 22),
        ),
        (
            "Costas-22",
            transformed_costas(23),
            (22, 231, (13, 21), 34, 72, 25, 11),
        ),
        (
            "parabola-image-43",
            transformed_parabola_43(),
            (43, 903, (-396, 38), 171, 2_586, 65, 107),
        ),
    ]

    for name, points, expected in families:
        actual = profile(points)
        assert actual == expected, (name, actual, expected)
        print(name, actual)

    print("dilated charge design-codegree branch: PASS")


if __name__ == "__main__":
    main()
