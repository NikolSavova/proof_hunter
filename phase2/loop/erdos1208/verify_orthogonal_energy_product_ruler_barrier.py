#!/usr/bin/env python3
"""Exact checks for the perpendicular-ruler energy-product barrier."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction


Point = tuple[int, int]


def erdos_turan(prime: int, count: int) -> list[int]:
    assert count <= prime
    return [2 * prime * index + (index * index % prime) for index in range(count)]


def is_sidon(values: list[int]) -> bool:
    seen: set[int] = set()
    for first, left in enumerate(values):
        for right in values[first:]:
            total = left + right
            if total in seen:
                return False
            seen.add(total)
    return True


def squared_distance_sidon(points: list[Point]) -> bool:
    seen: set[int] = set()
    for first, left in enumerate(points):
        for right in points[:first]:
            dx = left[0] - right[0]
            dy = left[1] - right[1]
            norm = dx * dx + dy * dy
            if norm in seen:
                return False
            seen.add(norm)
    return True


def difference_set(points: list[Point]) -> set[Point]:
    return {
        (left[0] - right[0], left[1] - right[1])
        for left in points
        for right in points
    }


def representations(values: set[int]) -> Counter[int]:
    return Counter(left - right for left in values for right in values)


def scalar_lower_profile(prime: int, side: int) -> tuple[int, int, int, Fraction]:
    ruler = erdos_turan(prime, 2 * side)
    assert is_sidon(ruler)
    first = ruler[:side]
    second = ruler[side:]
    positive_first = {abs(left - right) for left in first for right in first if left != right}
    positive_second = {abs(left - right) for left in second for right in second if left != right}
    assert positive_first.isdisjoint(positive_second)

    p_set = {left - right for left in first for right in first}
    q_set = {left - right for left in second for right in second}
    p_reps = representations(p_set)
    q_reps = representations(q_set)
    ordinary = sum(value * value for value in p_reps.values())
    common = sum(value * q_reps.get(shift, 0) for shift, value in p_reps.items())
    point_count = 2 * side
    difference_count = point_count * (point_count - 1) + 1
    normalized_lower = Fraction(ordinary * common, difference_count**5)
    return len(p_set), ordinary, common, normalized_lower


def full_profile() -> tuple[int, int, int, Fraction]:
    # This exact 40-point member was already used throughout the #1208 audit.
    ruler = erdos_turan(41, 40)
    first, second = ruler[:20], ruler[20:]
    points = [(mark, 0) for mark in first] + [(0, mark) for mark in second]
    assert squared_distance_sidon(points)
    differences = difference_set(points)
    assert len(differences) == len(points) * (len(points) - 1) + 1
    reps = Counter(
        (left[0] - right[0], left[1] - right[1])
        for left in differences
        for right in differences
    )
    ordinary = sum(value * value for value in reps.values())
    common = sum(value * reps.get((-shift[1], shift[0]), 0) for shift, value in reps.items())
    normalized = Fraction(ordinary * common, len(differences) ** 5)
    return len(differences), ordinary, common, normalized


def main() -> None:
    # Increasing exact scalar lower bounds.  The theorem proves that the
    # normalized value grows as Omega(side^2); these finite rows calibrate it.
    for prime, side in [(17, 8), (41, 20), (83, 40)]:
        size, ordinary, common, normalized = scalar_lower_profile(prime, side)
        print(
            "scalar",
            prime,
            side,
            size,
            ordinary,
            common,
            float(normalized),
        )

    difference_count, ordinary, common, normalized = full_profile()
    assert (difference_count, ordinary, common) == (1_561, 39_056_177, 17_767_185)
    print(
        "full-40",
        difference_count,
        ordinary,
        common,
        float(normalized),
    )
    print("orthogonal energy-product ruler barrier: PASS")


if __name__ == "__main__":
    main()
