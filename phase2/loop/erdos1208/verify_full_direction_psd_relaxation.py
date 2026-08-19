#!/usr/bin/env python3
"""Exact checks for FULL_DIRECTION_PSD_RELAXATION_BARRIER.md."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import isqrt


Point = tuple[int, int]


def profile(side: int) -> tuple[int, int, int]:
    points = [(x, y) for x in range(side + 1) for y in range(side + 1)]
    number = len(points)
    autocorrelation: Counter[Point] = Counter(
        (x1 - x2, y1 - y2)
        for x1, y1 in points
        for x2, y2 in points
    )
    shells: dict[int, list[Point]] = {}
    for displacement in autocorrelation:
        if displacement == (0, 0):
            continue
        radius = displacement[0] ** 2 + displacement[1] ** 2
        shells.setdefault(radius, []).append(displacement)
    maximum_shell = max(map(len, shells.values()))

    size = isqrt((number - 1) // maximum_shell)
    while (size + 1) * size * maximum_shell <= number - 1:
        size += 1
    while size * (size - 1) * maximum_shell > number - 1:
        size -= 1
    assert size >= 2

    coefficient = Fraction(size * (size - 1), number * (number - 1))
    values = {
        displacement: (
            Fraction(size) if displacement == (0, 0)
            else coefficient * multiplicity
        )
        for displacement, multiplicity in autocorrelation.items()
    }
    assert sum(values.values()) == size * size
    assert values[(0, 0)] == size
    assert all(value >= 0 for value in values.values())
    for displacements in shells.values():
        assert sum(values[item] for item in displacements) <= 1

    # Formula (3.3): the Fourier transform is a nonnegative multiple of
    # |hat(1_X)|^2 plus this nonnegative constant.
    constant_term = Fraction(size) - coefficient * number
    assert constant_term >= 0
    assert coefficient >= 0
    return number, maximum_shell, size


def main() -> None:
    expected = {
        4: (25, 8, 2),
        8: (81, 16, 2),
        16: (289, 16, 4),
        32: (1089, 24, 7),
        64: (4225, 32, 12),
    }
    for side, answer in expected.items():
        result = profile(side)
        assert result == answer
        print("m,M,R,k", side, *result)
    print("PASS")


if __name__ == "__main__":
    main()
