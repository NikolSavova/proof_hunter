#!/usr/bin/env python3
"""Exact 63-point barrier to scalar hull-rooted Tutte induction.

Sixty rational points lie on the unit circle inside a large rational outer
triangle.  The inner point set is Boolean (every subset is convex), but each
outer vertex sees only a tangent arc.  Consequently every hull vertex fails
the rooted-amortization inequality, and deleting the whole hull also fails.
All determinants and partition-function evaluations are exact rationals.
"""

from __future__ import annotations

from fractions import Fraction as Q
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
from reflection_trace import determinant, slope_order  # noqa: E402


# Rational approximations to tan(theta/2), in cyclic angular order.  Feeding
# t into ((1-t^2)/(1+t^2), 2t/(1+t^2)) lies exactly on the unit circle.
T_NUMERATORS = (
    7173, 59604, 112362, 165746, 220066, 275652, 332869, 392117,
    453852, 518594, 586955, 659654, 737560, 821731, 913478, 1014451,
    1126763, 1253172, 1397352, 1564318, 1761106, 1997912, 2290108,
    2662009, 3154501, 3842083, 4876373, 6620789, 10218990, 22115403,
    -139403398, -16777506, -8899776, -6033322, -4544101, -3627757,
    -3004185, -2550258, -2203363, -1928289, -1703709, -1515946,
    -1355822, -1216944, -1094718, -985755, -887498, -797975, -715639,
    -639256, -567825, -500523, -436661, -375656, -317007, -260275,
    -205070, -151039, -97857, -45217,
)


def configuration():
    outer = [(Q(-1000), Q(-1000)), (Q(1001), Q(-997)), (Q(1, 7), Q(1002))]
    inner = []
    for numerator in T_NUMERATORS:
        t = Q(numerator, 10**6)
        inner.append(((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)))
    return outer, inner


def z_value(points, activity):
    points = sorted(points)
    n = len(points)
    edges = slope_order(points)
    cups = [[Q(i == j) for j in range(n)] for i in range(n)]
    for _, i, j in edges:
        cups[j] = [a + activity * b for a, b in zip(cups[j], cups[i])]
    caps = [[Q(i == j) for j in range(n)] for i in range(n)]
    for _, i, j in reversed(edges):
        caps[j] = [a + activity * b for a, b in zip(caps[j], caps[i])]
    # Include the empty face.
    return (
        1
        + n * activity
        + sum(cups[i][j] * caps[i][j] for i in range(n) for j in range(n))
        - n
    )


def same_side_of_oriented_triangle(triangle, point):
    sign = determinant(*triangle)
    return all(
        determinant(triangle[i], triangle[(i + 1) % 3], point) * sign > 0
        for i in range(3)
    )


def main():
    outer, inner = configuration()
    points = outer + inner
    n = len(points)
    m = len(inner)
    assert n == 63 and m == 60 and len(set(points)) == n
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                assert determinant(points[i], points[j], points[k]) != 0
    assert all(same_side_of_oriented_triangle(outer, point) for point in inner)
    assert all(x * x + y * y == 1 for x, y in inner)

    v_parent = z_value(points, Q(1))
    w_parent = z_value(points, Q(1, 2))
    v_inner = Q(2**m)
    w_inner = Q(3, 2) ** m

    # Whole-hull/onion inequality:
    # 3 W(I) + n(W(P)-W(I)) <= 2(V(P)-V(I)).
    onion_lhs = 3 * w_inner + n * (w_parent - w_inner)
    onion_rhs = 2 * (v_parent - v_inner)
    assert onion_lhs > onion_rhs

    rooted_ratios = []
    for e in range(3):
        child = points[:e] + points[e + 1 :]
        v0 = z_value(child, Q(1))
        w0 = z_value(child, Q(1, 2))
        d = v_parent - v0
        w_link = 2 * (w_parent - w0)
        rooted_lhs = 2 * w0 + n * w_link
        rooted_rhs = 4 * d
        assert rooted_lhs > rooted_rhs
        rooted_ratios.append(rooted_lhs / rooted_rhs)

    # The original HW2 inequality is nowhere near failing.
    assert n * w_parent < 2 * v_parent

    print("outer-triangle scalar-induction barrier: PASS")
    print(f"n={n}, inner={m}, onion ratio={float(onion_lhs/onion_rhs):.12g}")
    print("rooted RA ratios=", [float(value) for value in rooted_ratios])
    print(f"original n Z(1/2)/(2 Z(1))={float(n*w_parent/(2*v_parent)):.12g}")


if __name__ == "__main__":
    main()
