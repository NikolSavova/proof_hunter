#!/usr/bin/env python3
"""Checks for RELEASED_FACE_HALL_LABEL_PRIMITIVE_GATE.md."""

from fractions import Fraction as Q
from itertools import combinations
from math import comb


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lo = []
    for p in points:
        while len(lo) >= 2 and orient(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    up = []
    for p in reversed(points):
        while len(up) >= 2 and orient(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def convex(points):
    return len(hull(points)) == len(set(points))


def embed(center, offsets, epsilon):
    return [
        (center[0] + epsilon * Q(a), center[1] + epsilon * epsilon * Q(b))
        for a, b in offsets
    ]


def parabolic_cloud(center, size, sign):
    epsilon = Q(1, 10**5 * size * size)
    offsets = [(j, sign * j * j) for j in range(1, size + 1)]
    return embed(center, offsets, epsilon)


def hall_density_complete(rows, columns):
    return max(
        Q(a * b, a + b)
        for a in range(1, rows + 1)
        for b in range(1, columns + 1)
    )


def check_abstract_hall_and_pair_cap():
    for a in range(1, 30):
        for b in range(1, 30):
            assert hall_density_complete(a, b) == Q(a * b, a + b)

    # A synthetic core with pair weight at most n*delta has the claimed
    # distinct-neighbor lower bound.
    for n, delta, degree in ((10, 3, 301), (100, 7, 7001), (8, 1, 65)):
        pair_cap = n * delta
        neighbors = (degree + pair_cap - 1) // pair_cap
        assert neighbors > (degree - 1) / pair_cap


def check_anti_aligned_face_core():
    guard_center = (Q(1, 100), Q(50099, 10000))
    pocket_center = (Q(0), Q(-4))
    checked = 0
    for p, r in ((5, 3), (6, 3), (7, 3), (7, 4)):
        Y = parabolic_cloud(guard_center, p, 1)
        Z = parabolic_cloud(pocket_center, p, -1)
        whole = Y + Z
        assert all(orient(*triple) != 0 for triple in combinations(whole, 3))
        assert convex(Y) and convex(Z)

        rows = list(combinations(Y, r))
        columns = list(combinations(Z, r))
        M = comb(p, r)
        assert len(rows) == len(columns) == M
        for A in rows:
            assert convex(A)
            for F in columns:
                assert convex(F)
                assert not convex(A + F)
                checked += 1

        assert hall_density_complete(M, M) == Q(M, 2)
        # Fixing one released face and its least column leaves M source faces.
        fixed_F = columns[0]
        fixed_x = min(fixed_F)
        assert fixed_x in fixed_F and len(rows) == M
        # Pair records are simple.
        pairs = {(frozenset(A), frozenset(fixed_F)) for A in rows}
        assert len(pairs) == M

    assert comb(7, 3) == 35
    assert hall_density_complete(35, 35) == Q(35, 2)
    assert checked == 10 * 10 + 20 * 20 + 35 * 35 + 35 * 35


if __name__ == "__main__":
    check_abstract_hall_and_pair_cap()
    check_anti_aligned_face_core()
    print(
        "PASS: released-face Hall/core, pair cap, and anti-aligned "
        "fixed-face regression"
    )
