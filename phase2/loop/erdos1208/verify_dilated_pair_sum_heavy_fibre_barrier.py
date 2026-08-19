#!/usr/bin/env python3
"""Exact finite checks for the dilated pair-sum heavy-fibre barrier."""

from __future__ import annotations

from collections import Counter

from verify_orthogonal_energy_product_ruler_barrier import (
    difference_set,
    erdos_turan,
    is_sidon,
    squared_distance_sidon,
)


Point = tuple[int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def linear_l(point: Point) -> Point:
    # (I + J)(x,y) for J(x,y)=(-y,x).
    return point[0] - point[1], point[0] + point[1]


def scalar_difference_representations(values: set[int]) -> Counter[int]:
    return Counter(left - right for left in values for right in values)


def dilated_pair_sum_support(points: list[Point]) -> set[Point]:
    pair_sums = {add(left, right) for left in points for right in points}
    return {
        subtract(pair_sum, linear_l(third))
        for pair_sum in pair_sums
        for third in points
    }


def overlap(differences: set[Point], shift: Point) -> int:
    return sum(subtract(point, shift) in differences for point in differences)


def diagonal_support(ruler: list[int], center: int) -> set[Point]:
    diagonal = [(center + mark, center + mark) for mark in ruler]
    return dilated_pair_sum_support(diagonal)


def profile(prime: int, side: int, center: int) -> tuple[int, ...]:
    ruler = erdos_turan(prime, side)
    assert is_sidon(ruler)

    scalar_differences = {left - right for left in ruler for right in ruler}
    reps = scalar_difference_representations(scalar_differences)
    positive = [shift for shift in reps if shift > 0]
    h = max(positive, key=lambda shift: (reps[shift], -abs(shift), shift))

    points = [(0, 0), (h, 0)] + [
        (center + mark, center + mark) for mark in ruler
    ]
    assert len(set(points)) == side + 2
    assert squared_distance_sidon(points)

    differences = difference_set(points)
    d = (h, 0)
    ld = linear_l(d)
    assert d in differences
    assert ld == (h, h)
    dilated_overlap = overlap(differences, ld)
    assert dilated_overlap >= reps[h]

    support = dilated_pair_sum_support(points)
    diag_support = diagonal_support(ruler, center)
    exact_diagonal_count = side * side * (side + 1) // 2
    assert len(diag_support) == exact_diagonal_count
    assert diag_support <= support

    return (
        side,
        prime,
        max(ruler),
        h,
        reps[h],
        center,
        len(points),
        len(differences),
        dilated_overlap,
        len(support),
        len(diag_support),
    )


def main() -> None:
    expected = [
        (4, 5, 34, 10, 6, 45, 6, 31, 10, 120, 40),
        (8, 11, 159, 24, 24, 184, 10, 91, 28, 537, 288),
        (12, 13, 290, 27, 52, 318, 14, 183, 56, 1_448, 936),
        (20, 23, 890, 47, 172, 938, 22, 463, 176, 5_509, 4_200),
        (40, 41, 3_202, 163, 628, 3_366, 42, 1_723, 632, 37_741, 32_800),
    ]
    actual = [profile(row[1], row[0], row[5]) for row in expected]
    assert actual == expected
    for row in actual:
        print("profile", *row)
    print("dilated pair-sum heavy-fibre barrier: PASS")


if __name__ == "__main__":
    main()
