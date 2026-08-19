#!/usr/bin/env python3
"""Checks for ENDPOINT_FOURIER_COMPENSATION_LEMMA.md."""

from __future__ import annotations

import cmath
from itertools import combinations


Point = tuple[int, int]


def difference(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def is_vector_sidon(points: list[Point]) -> bool:
    seen: set[Point] = set()
    for left, right in combinations(range(len(points)), 2):
        value = difference(points[left], points[right])
        if value in seen or (-value[0], -value[1]) in seen:
            return False
        seen.add(value)
    return True


def difference_set(points: list[Point]) -> set[Point]:
    return {difference(left, right) for left in points for right in points}


def verify_autocorrelation(points: list[Point]) -> None:
    assert is_vector_sidon(points)
    k = len(points)
    differences = difference_set(points)
    counts = {
        value: sum(
            difference(left, right) == value
            for left in points
            for right in points
        )
        for value in differences
    }
    assert counts[(0, 0)] == k
    assert all(
        multiplicity == 1
        for value, multiplicity in counts.items()
        if value != (0, 0)
    )
    assert len(differences) == k * (k - 1) + 1


def parity_transform(values: set[Point], frequency: Point) -> int:
    return sum(
        -1 if (frequency[0] * x + frequency[1] * y) % 2 else 1
        for x, y in values
    )


def verify_exact_parity_compensation(points: list[Point]) -> None:
    """Exhaust all subsets for a small test and all four parity characters."""
    differences = sorted(difference_set(points))
    k = len(points)
    size = len(differences)
    for mask in range(1 << size):
        subset = {
            differences[index]
            for index in range(size)
            if (mask >> index) & 1
        }
        remainder = set(differences) - subset
        for frequency in ((0, 0), (1, 0), (0, 1), (1, 1)):
            subset_hat = parity_transform(subset, frequency)
            full_hat = parity_transform(set(differences), frequency)
            remainder_hat = parity_transform(remainder, frequency)
            assert full_hat == subset_hat + remainder_hat
            assert full_hat >= -(k - 1)
            deficit = max(0, -(k - 1) - subset_hat)
            assert deficit <= abs(remainder_hat) <= len(remainder)


def transform(values: set[Point], q: int, a: int, b: int) -> complex:
    return sum(
        cmath.exp(-2j * cmath.pi * (a * x + b * y) / q)
        for x, y in values
    )


def verify_finite_torus_l2(points: list[Point], subsets: list[set[Point]]) -> None:
    """Numerically check the torus analogue on a fine exact residue model."""
    differences = difference_set(points)
    k = len(points)
    q = 31
    # The difference box is smaller than q/2, so reduction is injective.
    assert all(2 * max(abs(x), abs(y)) < q for x, y in differences)
    for subset in subsets:
        assert subset <= differences
        remainder = differences - subset
        deficit_square = 0.0
        remainder_square = 0.0
        for a in range(q):
            for b in range(q):
                subset_hat = transform(subset, q, a, b)
                full_hat = transform(differences, q, a, b)
                remainder_hat = transform(remainder, q, a, b)
                assert abs(full_hat - subset_hat - remainder_hat) < 1e-9
                assert full_hat.real >= -(k - 1) - 1e-9
                deficit = max(0.0, -(k - 1) - subset_hat.real)
                assert deficit <= abs(remainder_hat) + 1e-9
                deficit_square += deficit * deficit
                remainder_square += abs(remainder_hat) ** 2
        deficit_square /= q * q
        remainder_square /= q * q
        assert deficit_square <= remainder_square + 1e-8
        # Discrete Parseval; the residue embedding is injective.
        assert abs(remainder_square - len(remainder)) < 1e-8
        assert deficit_square <= len(remainder) + 1e-8


def main() -> None:
    small = [(0, 0), (1, 0), (0, 2)]
    medium = [(0, 0), (1, 0), (0, 2), (3, 3), (-2, 4)]
    verify_autocorrelation(small)
    verify_autocorrelation(medium)
    verify_exact_parity_compensation(small)

    medium_differences = difference_set(medium)
    subsets = [
        set(),
        {(0, 0)},
        {value for value in medium_differences if value[0] % 2},
        {value for value in medium_differences if value[1] >= 0},
        set(medium_differences),
    ]
    verify_finite_torus_l2(medium, subsets)
    print("endpoint Fourier compensation: PASS")


if __name__ == "__main__":
    main()
