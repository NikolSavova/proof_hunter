#!/usr/bin/env python3
"""Exact reverse-product trace evaluator for Erdős 838.

For points in increasing x-order, sort all chord edges by slope and put
T_(i,j) = I + E_(j,i).  The increasing-slope product counts cups by their two
endpoints, the decreasing-slope product counts caps, and their Frobenius inner
product is the number of nonempty convex-position subsets.

This is intentionally a small first-stage checker.  The planned search driver
will add reduced-word input and graded polynomial matrices; see
PLAN_OF_ATTACK_20260813.md.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path


Point = tuple[Fraction, Fraction]
Edge = tuple[Fraction, int, int]


def read_points(path: Path) -> list[Point]:
    points: list[Point] = []
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        x, y = line.replace(",", " ").split()[:2]
        points.append((Fraction(x), Fraction(y)))
    points = sorted(points)
    if len(set(points)) != len(points):
        raise ValueError("duplicate points")
    if any(points[i][0] >= points[i + 1][0] for i in range(len(points) - 1)):
        raise ValueError("x-coordinates must be distinct")
    return points


def determinant(p: Point, q: Point, r: Point) -> Fraction:
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def slope_order(points: list[Point]) -> list[Edge]:
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if determinant(points[i], points[j], points[k]) == 0:
                    raise ValueError(f"collinear triple {i},{j},{k}")

    edges = sorted(
        (
            (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]),
            i,
            j,
        )
        for i in range(n)
        for j in range(i + 1, n)
    )

    # General position makes equal-slope edges disjoint, so their elementary
    # matrices commute and the arbitrary lexicographic tie break is harmless.
    for first, second in zip(edges, edges[1:]):
        if first[0] == second[0] and len({first[1], first[2], second[1], second[2]}) < 4:
            raise ValueError("equal slopes on incident edges")
    return edges


def transvection_product(n: int, edges: list[Edge]) -> list[list[int]]:
    """Return successive left product of I+E_(j,i) for the supplied edges."""
    matrix = [[int(i == j) for j in range(n)] for i in range(n)]
    for _, i, j in edges:
        matrix[j] = [matrix[j][k] + matrix[i][k] for k in range(n)]
    return matrix


def evaluate(points: list[Point]) -> tuple[int, int, int, int]:
    n = len(points)
    edges = slope_order(points)
    cups = transvection_product(n, edges)
    caps = transvection_product(n, list(reversed(edges)))
    cup_total = sum(map(sum, cups))
    cap_total = sum(map(sum, caps))
    convex_total = sum(
        cups[row][column] * caps[row][column]
        for row in range(n)
        for column in range(n)
    )
    endpoint_max = max(
        [1]
        + [
            cups[row][column] * caps[row][column]
            for row in range(n)
            for column in range(row)
        ]
    )
    return cap_total, cup_total, convex_total, endpoint_max


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
    points = sorted(pascal_cell(4, 2, Fraction(1, 97)))
    result = evaluate(points)
    expected = (31, 31, 50, 9)
    if result != expected:
        raise AssertionError(f"T_(4,2): got {result}, expected {expected}")
    print(f"T_(4,2) reverse-product trace: (C,U,V,M)={result} -> PASS")

    outer_epsilon = Fraction(1, 16384)
    composition = sorted(
        (
            macro_x + outer_epsilon * outer_epsilon * micro_x,
            macro_y + outer_epsilon * micro_y,
        )
        for macro_x, macro_y in points
        for micro_x, micro_y in points
    )
    result = evaluate(composition)
    expected = (14136, 14136, 441399, 24336)
    if result != expected:
        raise AssertionError(f"36-point composition: got {result}, expected {expected}")
    print(f"36-point reverse-product trace: (C,U,V,M)={result} -> PASS")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("points", nargs="?", type=Path)
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        selftest()
    if args.points is not None:
        print("C,U,V,max_endpoint_product =", evaluate(read_points(args.points)))
    if not args.selftest and args.points is None:
        parser.error("supply --selftest or a coordinate file")


if __name__ == "__main__":
    main()
