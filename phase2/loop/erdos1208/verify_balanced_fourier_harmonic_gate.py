#!/usr/bin/env python3
"""Finite-torus checks for the balanced harmonic Fourier gate."""

from __future__ import annotations

from collections import defaultdict
from cmath import exp, pi

from search_rotated_support import is_distance_sidon
from verify_determinant_prime_costas_resonance import ROWS, apply, welch
from verify_transverse_closure_witness import POINTS as CLOSURE_POINTS


Point = tuple[int, int]

RULER_POINTS = [
    (0, 0),
    (1, 0),
    (4, 0),
    (9, 0),
    (0, 16),
    (0, 23),
    (0, 33),
    (0, 35),
]


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def safe_prime(points: list[Point]) -> int:
    spans = [
        max(point[coordinate] for point in points)
        - min(point[coordinate] for point in points)
        for coordinate in (0, 1)
    ]
    candidate = 4 * max(spans) + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def fourier_square_table(points: list[Point], modulus: int) -> list[list[float]]:
    roots = [exp(-2j * pi * residue / modulus) for residue in range(modulus)]
    table: list[list[float]] = []
    for first in range(modulus):
        row = []
        for second in range(modulus):
            value = sum(
                roots[(first * x + second * y) % modulus]
                for x, y in points
            )
            row.append(value.real * value.real + value.imag * value.imag)
        table.append(row)
    return table


def profile(points: list[Point]) -> tuple[int, float, float, float]:
    assert is_distance_sidon(points)
    modulus = safe_prime(points)
    table = fourier_square_table(points, modulus)
    total_cross = 0.0
    total_square = 0.0
    total_harmonic = 0.0
    total_balanced = 0.0
    for first in range(modulus):
        for second in range(modulus):
            left = table[first][second]
            right = table[-second % modulus][first]
            total_cross += left * right
            total_square += left * left
            balanced = left * right * min(left, right)
            denominator = left + right
            harmonic = 0.0 if denominator < 1e-24 else (
                left * left * right * right / denominator
            )
            assert harmonic <= balanced + 1e-7
            assert 2 * harmonic + 1e-7 >= balanced
            total_harmonic += harmonic
            total_balanced += balanced

    scale = modulus * modulus
    total_cross /= scale
    total_square /= scale
    total_harmonic /= scale
    total_balanced /= scale
    size = len(points)
    assert abs(total_cross - size * size) < 1e-6
    assert abs(total_square - (2 * size * size - size)) < 1e-6
    assert total_harmonic <= total_balanced + 1e-7
    return modulus, total_harmonic, total_cross, total_square


def verify_horizontal_cover(points: list[Point], modulus: int) -> None:
    lines: dict[int, list[int]] = defaultdict(list)
    for x, y in points:
        lines[y].append(x)
    roots = [exp(-2j * pi * residue / modulus) for residue in range(modulus)]
    values = []
    for frequency in range(modulus):
        value = 0.0
        for coordinates in lines.values():
            line_sum = sum(roots[(frequency * x) % modulus] for x in coordinates)
            value += line_sum.real * line_sum.real + line_sum.imag * line_sum.imag
        values.append(value)
    first = sum(values) / modulus
    second = sum(value * value for value in values) / modulus
    size = len(points)
    predicted = size * size + sum(len(line) ** 2 for line in lines.values()) - size
    assert abs(first - size) < 1e-7
    assert abs(second - predicted) < 1e-6


def main() -> None:
    costas = [apply(ROWS[11][0], point) for point in welch(11)]
    witnesses = [
        ("closure", CLOSURE_POINTS[:20]),
        ("perpendicular-ruler", list(RULER_POINTS)),
        ("determinant-prime-Costas", costas),
    ]
    for name, points in witnesses:
        modulus, harmonic, cross, square = profile(points)
        size = len(points)
        assert harmonic < 2 * size**3
        verify_horizontal_cover(points, modulus)
        print(
            name,
            (size, modulus, harmonic / size**3, cross, square),
        )
    print("balanced Fourier harmonic gate: PASS")


if __name__ == "__main__":
    main()
