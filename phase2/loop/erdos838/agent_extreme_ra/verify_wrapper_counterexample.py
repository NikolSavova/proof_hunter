#!/usr/bin/env python3
"""Exact certificate killing RA and whole-onion amortization for Erdos 838."""

from __future__ import annotations

import sys
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
GEOMETRY = HERE.parent / "agent_geometry"
sys.path.insert(0, str(GEOMETRY))
from audit_geometry import Point, det, glue, min_slope, normalized  # noqa: E402


def core(depth: int) -> tuple[Point, ...]:
    points = (Point(Fraction(0), Fraction(0)),)
    for _ in range(depth):
        points = glue(points, points)
    return normalized(points)


def monotone_hull(points: tuple[Point, ...]) -> tuple[int, ...]:
    ids = sorted(range(len(points)), key=lambda i: (points[i].x, points[i].y))
    lower: list[int] = []
    for i in ids:
        while len(lower) >= 2 and det(points[lower[-2]], points[lower[-1]], points[i]) <= 0:
            lower.pop()
        lower.append(i)
    upper: list[int] = []
    for i in reversed(ids):
        while len(upper) >= 2 and det(points[upper[-2]], points[upper[-1]], points[i]) <= 0:
            upper.pop()
        upper.append(i)
    return tuple(lower[:-1] + upper[:-1])


def recurrence(depth: int) -> tuple[int, Fraction, int, Fraction]:
    # Nonempty C(1), C(1/2), W(1), W(1/2); U=C by symmetry.
    c_one = 1
    c_half = Fraction(1, 2)
    w_one = 1
    w_half = Fraction(1, 2)
    for d in range(depth):
        n = 1 << d
        old_c_one, old_c_half = c_one, c_half
        old_w_one, old_w_half = w_one, w_half
        c_one = old_c_one * (2 + n)
        c_half = old_c_half * (2 + Fraction(n, 2))
        w_one = 2 * old_w_one + old_c_one * old_c_one
        w_half = 2 * old_w_half + old_c_half * old_c_half
    return c_one, c_half, w_one, w_half


def main() -> None:
    depth = 7
    q = core(depth)
    n = len(q)
    assert n == 128
    mu = min_slope(q)
    assert mu is not None and mu > 0
    big = int(Fraction(4, 1) / mu) + 10

    left_top = Point(Fraction(-big - 1), Fraction(2))
    left_bottom = Point(Fraction(-big), Fraction(-1))
    right = Point(Fraction(big), Fraction(1, 2))
    wrapped = (left_top, left_bottom) + q + (right,)

    # Full exact general-position and hull checks.
    for a, b, c in combinations(wrapped, 3):
        assert det(a, b, c) != 0
    assert set(monotone_hull(wrapped)) == {0, 1, len(wrapped) - 1}

    # The one-sided signs used in the classification proof.
    for a, b in combinations(q, 2):
        assert det(left_top, a, b) > 0
        assert det(left_bottom, a, b) > 0
        assert det(a, b, right) < 0

    c_one, c_half, w_one, w_half = recurrence(depth)
    assert c_one == 29_082_240
    assert c_half == 550_800
    assert w_one == 194_501_650_656
    assert w_half == 264_094_555

    z_core_half = 1 + w_half
    short = 1 + n + comb(n, 2)
    chain = 1 + c_one
    layer_upper = 4 * chain + 3 * short
    left_root_upper = 2 * chain + 2 * short
    right_root_upper = chain + 3 * short
    root_upper = max(left_root_upper, right_root_upper)

    # ORA would require 2|layer| >= 3 Z_core(1/2), even after dropping
    # its other positive half-weight term.  RA would require
    # 4 R_e(1) >= 2 Z_core(1/2), even after dropping its other terms.
    assert 2 * layer_upper == 232_707_470
    assert 3 * z_core_half == 792_283_668
    assert 2 * layer_upper < 3 * z_core_half
    assert 4 * root_upper == 232_723_984
    assert 2 * z_core_half == 528_189_112
    assert 4 * root_upper < 2 * z_core_half

    print("skinny-wrapper RA/ORA counterexample: PASS")
    print(f"core={n}, parent={n + 3}, L={big}, mu={mu}")
    print(f"2 layer_upper={2 * layer_upper} < 3 Z_core(1/2)={3 * z_core_half}")
    print(f"4 root_upper={4 * root_upper} < 2 Z_core(1/2)={2 * z_core_half}")


if __name__ == "__main__":
    main()
