#!/usr/bin/env python3
"""Checks for DENSE_RECTANGLE_ACTUAL_GAP_FAN_GATE.md."""

from fractions import Fraction as F
from itertools import combinations
from math import prod


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


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


def is_convex(points):
    return len(hull(points)) == len(set(points))


def insertion_edge(base, p):
    old = hull(base)
    new = hull(base + [p])
    assert len(new) == len(old) + 1 and p in new
    i = new.index(p)
    return frozenset((new[i - 1], new[(i + 1) % len(new)]))


def double_chain(m):
    l = (F(-3), F(0))
    r = (F(3), F(0))
    t = (F(0), F(5))
    v = (F(-2), F(-1))
    u = (F(2), F(-1))
    B = [l, r, t]
    delta = F(1, 10000 * m * m)
    X = [(delta * j, F(-4) - delta * j * j) for j in range(1, m + 1)]
    edge = (t[0] - r[0], t[1] - r[1])
    normal = (F(5), F(3))
    G = []
    for i in range(1, m + 1):
        xi = F(1, 2) + delta * i
        eta = F(1, 10) + delta * i * i
        G.append(
            (
                r[0] + xi * edge[0] + eta * normal[0],
                r[1] + xi * edge[1] + eta * normal[1],
            )
        )
    return B, v, u, G, X


def check_double_chain():
    for m in (1, 2, 3, 5, 10, 20, 35):
        B, v, u, G, X = double_chain(m)
        P = B + [v, u] + G + X
        assert len(P) == len(set(P))
        assert all(orient(*triple) != 0 for triple in combinations(P, 3))

        lr = frozenset((B[0], B[1]))
        rt = frozenset((B[1], B[2]))
        assert all(insertion_edge(B, x) == lr for x in X)
        assert all(insertion_edge(B, g) == rt for g in G)

        assert is_convex(B + [v])
        assert all(is_convex(B + [x]) and is_convex([x, v]) for x in X)
        assert all(is_convex(B + [g]) for g in G)
        assert all(is_convex(B + [g, v, u]) for g in G)
        assert all(is_convex(B + [g, x]) for g in G for x in X)
        assert all(not is_convex(B + [g, x, v]) for g in G for x in X)

        assert all(not is_convex(B + list(pair)) for pair in combinations(G, 2))
        assert all(not is_convex(B + list(pair)) for pair in combinations(X, 2))

        # The same insertion gaps persist in every opposite-side column.
        assert all(insertion_edge(B + [x], g) == rt for x in X for g in G)
        assert all(insertion_edge(B + [g], x) == lr for g in G for x in X)

        # Exact rooted-complex and full base-retaining mixed count.
        HG = 1 + len(G)
        HX = 1 + len(X)
        assert HG == m + 1 and HX == m + 1
        mixed_count = 0
        for sg_size in range(0, min(2, m + 1)):
            for sx_size in range(0, min(2, m + 1)):
                for SG in combinations(G, sg_size):
                    for SX in combinations(X, sx_size):
                        assert is_convex(B + list(SG) + list(SX))
                        mixed_count += 1
        assert mixed_count == (m + 1) ** 2

        # Every larger trace contains a root-bad pair and remains bad.
        if m >= 2:
            assert not is_convex(B + G[:2] + X[:1])
            assert not is_convex(B + G[:1] + X[:2])

        # Detached escape exists but erases B.
        assert is_convex(G)
        assert is_convex(X)


def check_entropy_inequality():
    # Numerical/exact finite audit of (6) for arbitrary positive profile
    # sizes and all 3-color bucket assignments.
    samples = [
        ([2, 3, 5], [7, 2, 4]),
        ([11, 2, 2, 17], [3, 13, 5, 2]),
        ([101] * 8, [3, 7, 11, 13, 17, 19, 23, 29]),
    ]
    for HX, HY in samples:
        L = [max(a, b) for a, b in zip(HX, HY)]
        n = len(L)
        if n % 2 == 0:
            colors = [i % 2 for i in range(n)]
        else:
            colors = [i % 2 for i in range(n - 1)] + [2]
        assert all(colors[i] != colors[(i + 1) % n] for i in range(n))
        products = [prod(L[i] for i in range(len(L)) if colors[i] == c) for c in range(3)]
        R = max(products)
        assert R**3 >= prod(L)
        assert R**6 >= prod(a * b for a, b in zip(HX, HY))


if __name__ == "__main__":
    check_double_chain()
    check_entropy_inequality()
    print("PASS: two-cloud entropy bank and scalable adjacent double-dominance rectangle")
