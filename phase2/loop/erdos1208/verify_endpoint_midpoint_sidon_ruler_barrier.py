#!/usr/bin/env python3
"""Exact finite checks for the Sidon-ruler midpoint-charge barrier."""

from __future__ import annotations

from collections import Counter
from math import log

Point = tuple[int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def negate(point: Point) -> Point:
    return -point[0], -point[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def linear(point: Point) -> Point:
    """Multiplication by 1+i."""
    return point[0] - point[1], point[0] + point[1]


def norm(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def next_prime(value: int) -> int:
    while not is_prime(value):
        value += 1
    return value


def dense_sidon_ruler(size: int) -> tuple[int, list[int]]:
    """The Erdos--Turan ruler 2*pi*j+(j^2 mod pi)."""
    prime = next_prime(size)
    ruler = [
        2 * prime * index + (index * index % prime)
        for index in range(size)
    ]
    pair_sums: dict[int, tuple[int, int]] = {}
    for first in range(size):
        for second in range(first + 1):
            value = ruler[first] + ruler[second]
            assert value not in pair_sums
            pair_sums[value] = first, second
    assert max(ruler) < 2 * prime * prime
    return prime, ruler


def is_distance_sidon(points: list[Point]) -> bool:
    squared_distances: set[int] = set()
    for first in range(len(points)):
        for second in range(first):
            value = norm(subtract(points[first], points[second]))
            if value in squared_distances:
                return False
            squared_distances.add(value)
    return True


def construction(
    side: int,
) -> tuple[list[Point], list[Point], list[Point], list[Point], Point, Point]:
    _, ruler = dense_sidon_ruler(2 * side)
    base = [(value, 0) for value in ruler]
    left = base[:side]
    right = base[side:]

    common = (123_457 + 17 * side, 234_569 + 31 * side)
    translation = (10**9 + 101 * side, 2 * 10**9 + 103 * side)
    segment_translation = (10**15 + 107 * side, 3 * 10**15 + 109 * side)
    selected = (common[1], -common[0])

    first_copy = [
        add(add(translation, common), negate(linear(point)))
        for point in left
    ]
    second_copy = [
        add(translation, negate(linear(point)))
        for point in right
    ]
    points = (
        base
        + first_copy
        + second_copy
        + [segment_translation, add(segment_translation, selected)]
    )
    return points, base, first_copy, second_copy, selected, translation


def verify_side(side: int) -> None:
    points, base, first_copy, second_copy, selected, translation = (
        construction(side)
    )
    assert len(points) == 4 * side + 2
    assert is_distance_sidon(points)
    differences = {
        subtract(first, second)
        for first in points
        for second in points
    }
    number = len(points) * (len(points) - 1) + 1
    assert len(differences) == number

    intended: list[tuple[Point, Point]] = []
    midpoint_sums: list[Point] = []
    for first_index, first in enumerate(base[:side]):
        for second_index, second in enumerate(base[side:]):
            difference = subtract(first, second)
            opposite = negate(difference)
            fourth = subtract(
                first_copy[first_index], second_copy[second_index]
            )
            assert difference in differences
            assert opposite in differences
            assert fourth in differences
            assert add(selected, rotate(fourth)) == add(
                difference, rotate(opposite)
            )
            intended.append((difference, fourth))
            midpoint_sums.append(add(first, second))

    assert len(intended) == side * side
    assert len(set(midpoint_sums)) == side * side
    charge_counts = Counter(
        subtract(first, second)
        for first in midpoint_sums
        for second in midpoint_sums
        if first != second
    )
    pair_count = side * side * (side * side - 1)
    assert sum(charge_counts.values()) == pair_count
    assert len(charge_counts) <= 4 * max(point[0] for point in base) + 1

    # A Cartesian family of ordinary sums certifies quadratic support.
    support_witnesses: set[Point] = set()
    for first in range(side):
        for second in range(first + 1):
            for base_first in range(2 * side):
                for base_second in range(base_first + 1):
                    first_difference = subtract(
                        first_copy[first], base[base_first]
                    )
                    second_difference = subtract(
                        first_copy[second], base[base_second]
                    )
                    assert first_difference in differences
                    assert second_difference in differences
                    support_witnesses.add(add(
                        first_difference, second_difference
                    ))
    expected_support = (
        side * (side + 1) // 2
        * (2 * side) * (2 * side + 1) // 2
    )
    assert len(support_witnesses) == expected_support
    assert expected_support > side**4 // 2

    print(
        "side", side,
        "points", len(points),
        "N", number,
        "fibre", len(intended),
        "charge_pairs", pair_count,
        "charge_image", len(charge_counts),
        "charge_average", pair_count / len(charge_counts),
        "charge_max", max(charge_counts.values()),
        "support_witnesses", expected_support,
        "support_exponent_lower", log(expected_support) / log(number),
    )


def main() -> None:
    for side in (4, 6, 8, 10, 12):
        verify_side(side)
    print("endpoint midpoint Sidon-ruler barrier: PASS")


if __name__ == "__main__":
    main()
