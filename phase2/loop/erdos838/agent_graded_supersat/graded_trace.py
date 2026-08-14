#!/usr/bin/env python3
"""Exact polynomial reverse-product trace for Erdős 838.

Given rational points in increasing x-order, form the chord-slope order and
the two opposite products of T_(i,j)(z)=I+zE_(j,i).  The resulting histogram
is the exact number of convex subsets of every cardinality.
"""

from __future__ import annotations

from fractions import Fraction

from mean_size_probe import Point, slope_roots


Poly = tuple[int, ...]


def add_shift(left: Poly, right: Poly) -> Poly:
    result = [0] * max(len(left), len(right) + 1)
    for i, value in enumerate(left):
        result[i] += value
    for i, value in enumerate(right):
        result[i + 1] += value
    while len(result) > 1 and not result[-1]:
        result.pop()
    return tuple(result)


def multiply(left: Poly, right: Poly) -> Poly:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if a:
            for j, b in enumerate(right):
                if b:
                    result[i + j] += a * b
    return tuple(result)


def product(n: int, roots: list[tuple[int, int]]) -> list[list[Poly]]:
    matrix = [[(1,) if i == j else (0,) for j in range(n)] for i in range(n)]
    for i, j in roots:
        matrix[j] = [add_shift(matrix[j][column], matrix[i][column]) for column in range(n)]
    return matrix


def graded_profile(points: list[Point]) -> tuple[int, ...]:
    n = len(points)
    roots = slope_roots(points)
    cups = product(n, roots)
    caps = product(n, list(reversed(roots)))
    profile = [0]
    for row in range(n):
        for column in range(n):
            term = multiply(cups[row][column], caps[row][column])
            if len(profile) < len(term):
                profile.extend([0] * (len(term) - len(profile)))
            for degree, value in enumerate(term):
                profile[degree] += value
    # The diagonal identity paths contributed n at degree zero.  Singletons
    # instead have vertex weight z.
    profile[0] -= n
    if len(profile) < 2:
        profile.append(0)
    profile[1] += n
    while len(profile) > 1 and not profile[-1]:
        profile.pop()
    return tuple(profile)


def strong_glue(left: list[Point], right: list[Point], epsilon: Fraction) -> list[Point]:
    return [
        (epsilon * epsilon * x, epsilon * y) for x, y in left
    ] + [
        (1 + epsilon * epsilon * x, 1 + epsilon * y) for x, y in right
    ]


def pascal_cell(m: int, i: int, epsilon: Fraction) -> list[Point]:
    if i in (0, m):
        return [(Fraction(0), Fraction(0))]
    return strong_glue(
        pascal_cell(m - 1, i - 1, epsilon),
        pascal_cell(m - 1, i, epsilon),
        epsilon,
    )


def selftest() -> None:
    cell = sorted(pascal_cell(4, 2, Fraction(1, 97)))
    profile = graded_profile(cell)
    expected = (0, 6, 15, 20, 9)
    if profile != expected:
        raise AssertionError((profile, expected))
    print("T_(4,2) graded reverse trace:", profile, "PASS")


if __name__ == "__main__":
    selftest()
