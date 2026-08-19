#!/usr/bin/env python3
"""Exact finite checks for the asymptotic balanced-Fourier ruler barrier."""

from __future__ import annotations

from fractions import Fraction


Point = tuple[int, int]


def erdos_turan(prime: int, count: int) -> list[int]:
    assert count <= prime
    return [2 * prime * index + (index * index % prime) for index in range(count)]


def is_sidon(values: list[int]) -> bool:
    sums: set[int] = set()
    for first, left in enumerate(values):
        for right in values[first:]:
            value = left + right
            if value in sums:
                return False
            sums.add(value)
    return True


def is_distance_sidon(points: list[Point]) -> bool:
    distances: set[int] = set()
    for first, left in enumerate(points):
        for right in points[:first]:
            distance = (left[0] - right[0]) ** 2 + (left[1] - right[1]) ** 2
            if distance in distances:
                return False
            distances.add(distance)
    return True


def first_offset(first: list[int], second: list[int]) -> tuple[int, list[Point]]:
    offset = max(first + second) + 1
    while True:
        points = [(value, 0) for value in first] + [
            (0, offset + value) for value in second
        ]
        if is_distance_sidon(points):
            return offset, points
        offset += 1


def profile(prime: int, side: int) -> tuple[int, int, int, Fraction]:
    ruler = erdos_turan(prime, 2 * side)
    assert is_sidon(ruler)
    first, second = ruler[:side], ruler[side:]
    offset, points = first_offset(first, second)
    assert is_distance_sidon(points)

    maximum = max(max(first), offset + max(second))
    minimum = min(min(first), offset + min(second), 0)
    ambient = maximum - minimum

    # Section 4 uses a good eta-set of measure at least 1-32/s and the
    # xi-interval of length 1/(8M).  For the finite rows below the former
    # lower bound need not yet be positive; all constant arithmetic is
    # nevertheless exact.
    asymptotic_good_measure = Fraction(max(side - 32, 0), side)
    lower_bound = Fraction(side**6, 128 * 9**4 * ambient)
    normalized = lower_bound / (2 * side) ** 4

    # The explicit rows exhibit the required quadratic-height scale.  The
    # asymptotic theorem in PERPENDICULAR_RULER_OBSTRUCTION.md supplies the
    # s^(2+o(1)) version for every sufficiently large s.
    assert ambient < 32 * side * side
    return offset, ambient, asymptotic_good_measure.numerator, normalized


def main() -> None:
    for prime, side in [(17, 8), (41, 20), (83, 40)]:
        offset, ambient, good_numerator, normalized = profile(prime, side)
        print(
            "balanced ruler barrier",
            (prime, side, offset, ambient, good_numerator, float(normalized)),
        )
    print("balanced Fourier ruler barrier: PASS")


if __name__ == "__main__":
    main()
