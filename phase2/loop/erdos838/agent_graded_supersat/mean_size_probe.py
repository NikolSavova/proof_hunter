#!/usr/bin/env python3
"""Exact first-moment evaluator for the convex-subset partition function.

For a slope order e_1,...,e_M and T_e(z)=I+z E_(j,i), this computes the
values and derivatives at z=1 of the forward and reverse products.  Hence

    Z_P(z) = n z + <A(z),B(z)>_F - n

and ``Z'_P(1)/Z_P(1)`` is the mean size of a uniformly random nonempty
convex-position subset.  The included rational Horton generator is the
audited family from ``campaign_lower_break_lemma_20260813.md``.
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction


Point = tuple[Fraction, Fraction]
Root = tuple[int, int]


def dyadic_horton(level: int) -> list[Point]:
    ys = [Fraction(0)]
    for m in range(1, level + 1):
        epsilon = Fraction(1, 2 ** (m + 4))
        new_ys = [Fraction(0)] * (2**m)
        for j, value in enumerate(ys):
            new_ys[2 * j] = epsilon * value
            new_ys[2 * j + 1] = 1 + epsilon * value
        ys = new_ys
    return [(Fraction(i), y) for i, y in enumerate(ys)]


def determinant(p: Point, q: Point, r: Point) -> Fraction:
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def slope_roots(points: list[Point]) -> list[Root]:
    edges = sorted(
        (
            (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]),
            i,
            j,
        )
        for i in range(len(points))
        for j in range(i + 1, len(points))
    )
    for left, right in zip(edges, edges[1:]):
        if left[0] == right[0] and len({left[1], left[2], right[1], right[2]}) < 4:
            raise ValueError("collinear triple/equal incident slopes")
    return [(i, j) for _, i, j in edges]


def value_derivative(n: int, roots: list[Root]) -> tuple[list[list[int]], list[list[int]]]:
    values = [[int(i == j) for j in range(n)] for i in range(n)]
    derivatives = [[0] * n for _ in range(n)]
    for i, j in roots:
        old_j = values[j]
        old_dj = derivatives[j]
        values[j] = [a + b for a, b in zip(old_j, values[i])]
        derivatives[j] = [
            a + b + c for a, b, c in zip(old_dj, values[i], derivatives[i])
        ]
    return values, derivatives


def evaluate(points: list[Point]) -> tuple[int, int, float]:
    n = len(points)
    roots = slope_roots(points)
    cups, cup_derivatives = value_derivative(n, roots)
    caps, cap_derivatives = value_derivative(n, list(reversed(roots)))
    value = sum(cups[i][j] * caps[i][j] for i in range(n) for j in range(n))
    first_moment = n + sum(
        cup_derivatives[i][j] * caps[i][j]
        + cups[i][j] * cap_derivatives[i][j]
        for i in range(n)
        for j in range(n)
    )
    return value, first_moment, first_moment / value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--horton-level", type=int, nargs="+", default=list(range(1, 8)))
    args = parser.parse_args()
    for level in args.horton_level:
        points = dyadic_horton(level)
        value, moment, mean = evaluate(points)
        n = len(points)
        print(
            f"H_{level}: n={n:4d} V={value} Zprime={moment} "
            f"mu={mean:.9f} mu-log2n={mean-math.log2(n):+.9f} "
            f"mu/log2n={mean/math.log2(n):.9f}",
            flush=True,
        )


if __name__ == "__main__":
    main()
