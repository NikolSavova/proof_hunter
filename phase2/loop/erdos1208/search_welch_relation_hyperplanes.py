#!/usr/bin/env python3
"""Deterministic hyperplane sampling inside the N=60 Welch relation system.

This is a falsification/search artifact, not an exhaustive certificate.  It
samples codimension-one row spans, extracts their non-affine kernel direction,
and records how many full-system relations it preserves versus how many point
labels that direction moves modulo similarities.
"""

from __future__ import annotations

import random

from analyze_affine_costas_energy import welch
from verify_welch_relation_rigidity import (
    MODULUS,
    SQRT_MINUS_ONE,
    relation_rows,
    row_dot,
)


def row_basis(rows: list[dict[int, int]], target: int):
    basis: dict[int, dict[int, int]] = {}
    for source in rows:
        row = dict(source)
        while row:
            pivot = min(row)
            coefficient = row[pivot]
            if pivot not in basis:
                inverse = pow(coefficient, -1, MODULUS)
                basis[pivot] = {
                    index: value * inverse % MODULUS
                    for index, value in row.items()
                }
                break
            for index, value in basis[pivot].items():
                new_value = (
                    row.get(index, 0) - coefficient * value
                ) % MODULUS
                if new_value:
                    row[index] = new_value
                else:
                    row.pop(index, None)
        if len(basis) == target:
            return basis
    return basis


def nullspace_basis(basis: dict[int, dict[int, int]], size: int):
    pivots = sorted(basis)
    vectors: list[list[int]] = []
    for free in (index for index in range(size) if index not in basis):
        vector = [0] * size
        vector[free] = 1
        for pivot in reversed(pivots):
            vector[pivot] = -sum(
                value * vector[index]
                for index, value in basis[pivot].items()
                if index != pivot
            ) % MODULUS
        vectors.append(vector)
    return vectors


def residual_support(vector: list[int], coordinates: list[int]) -> int:
    """Hamming support after subtracting the best affine function a+b*z."""

    size = len(vector)
    most_matches = 0
    for left in range(size):
        for right in range(left + 1, size):
            slope = (vector[left] - vector[right]) * pow(
                (coordinates[left] - coordinates[right]) % MODULUS,
                -1,
                MODULUS,
            ) % MODULUS
            intercept = (vector[left] - slope * coordinates[left]) % MODULUS
            matches = sum(
                value == (intercept + slope * coordinate) % MODULUS
                for value, coordinate in zip(vector, coordinates)
            )
            most_matches = max(most_matches, matches)
    return size - most_matches


def main() -> None:
    points = welch(61)
    rows = relation_rows(points, (3, -1))
    coordinates = [
        (x + SQRT_MINUS_ONE * y) % MODULUS for x, y in points
    ]
    rng = random.Random(8)
    observations: list[tuple[int, int]] = []

    for _ in range(100):
        shuffled = rows[:]
        rng.shuffle(shuffled)
        basis = row_basis(shuffled, len(points) - 3)
        assert len(basis) == len(points) - 3
        for vector in nullspace_basis(basis, len(points)):
            preserved = sum(row_dot(row, vector) == 0 for row in rows)
            if preserved == len(rows):
                continue
            observations.append(
                (residual_support(vector, coordinates), preserved)
            )

    thresholds = {
        support: max(
            preserved
            for residual, preserved in observations
            if residual >= support
        )
        for support in (1, 2, 3, 5)
    }
    assert thresholds == {1: 1431, 2: 1351, 3: 1273, 5: 67}
    for support, preserved in thresholds.items():
        print(support, preserved)
    print("SAMPLED PASS")


if __name__ == "__main__":
    main()
