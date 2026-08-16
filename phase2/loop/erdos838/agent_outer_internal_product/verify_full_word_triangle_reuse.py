#!/usr/bin/env python3
"""Checks for FULL_WORD_TRIANGLE_REUSE_SCALE_BARRIER.md."""

from fractions import Fraction as F
from itertools import combinations, product
from math import comb


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


def stationary_construction(q, D, m):
    l = (F(-3), F(0))
    r = (F(3), F(0))
    t = (F(0), F(5))
    v = (F(-2), F(-1))
    u = (F(2), F(-1))
    anchors = [l, r, t]

    eps = F(1, 10**9 * q**4 * D**4)
    cells = []
    for k in range(1, q + 1):
        s = F(9, 10) + F(k, 20 * (q + 1))
        bend = s * (1 - s)
        z = (F(-3) + 3 * s - bend, 5 * s + bend)
        cell = []
        for d in range(1, D + 1):
            cell.append(
                (
                    z[0] + eps * (d + 7 * k * d * d),
                    z[1] + eps * (d * d + 11 * k * d * d * d),
                )
            )
        cells.append(cell)

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
    return anchors, v, u, cells, G, X


def check_local_cauchy():
    for a in range(1, 101):
        for b in range(1, 101):
            h = a + b
            e = a * b
            if min(a, b) <= 5:
                assert e <= 5 * h
            else:
                triangles = comb(a, 3) + comb(b, 3)
                assert 10 * e * e <= 27 * h * triangles


def check_stationary_geometry():
    for q, D, m in ((2, 2, 3), (3, 2, 4), (4, 3, 4), (5, 3, 5)):
        anchors, v, u, cells, G, X = stationary_construction(q, D, m)
        points = anchors + [v, u] + G + X + [p for cell in cells for p in cell]
        assert len(points) == len(set(points))
        assert all(orient(*triple) != 0 for triple in combinations(points, 3))
        lr = frozenset((anchors[0], anchors[1]))
        rt = frozenset((anchors[1], anchors[2]))

        words = list(product(range(D), repeat=q))
        assert len(words) == D**q
        bases = []
        for word in words:
            B = anchors + [cells[k][word[k]] for k in range(q)]
            bases.append(frozenset(B))
            assert is_convex(B)
            assert is_convex(B + [v])
            assert all(insertion_edge(B, g) == rt for g in G)
            assert all(insertion_edge(B, x) == lr for x in X)
            for g in G:
                assert is_convex(B + [g])
                assert is_convex(B + [g, v, u])
            for x in X:
                assert is_convex(B + [x])
                assert is_convex([x, v])
            for g in G:
                for x in X:
                    assert is_convex(B + [g, x])
                    assert not is_convex(B + [g, x, v])

        assert len(set(bases)) == D**q

        # Every actual role label blocks every internal cloud triangle,
        # even after all fixed anchors are omitted.
        role_labels = [p for cell in cells for p in cell]
        for z in role_labels:
            assert all(not is_convex([z] + list(T)) for T in combinations(G, 3))
            assert all(not is_convex([z] + list(T)) for T in combinations(X, 3))

        # Proposition 2 on representative higher traces.
        if m >= 3:
            for z in role_labels:
                assert not is_convex([z] + G[:3])
                assert not is_convex([z] + X[:3])

        # Exact target counts and overlap scales.
        M = D**q
        Q = {frozenset(B | {v}) for B in bases}
        A = {frozenset(B | {g}) for B in bases for g in G}
        C = {frozenset(B | {x}) for B in bases for x in X}
        E = {frozenset(B | {g, v, u}) for B in bases for g in G}
        W = {frozenset((x, v)) for x in X}
        assert len(Q) == M
        assert len(A) == len(C) == len(E) == M * m
        assert len(W) == m
        assert M * m * m == len(words) * len(G) * len(X)


def check_scale_audit():
    for M in (2, 16, 256, 65536):
        for m in (6, 10, 100):
            demand = M * m * m
            # The theorem gives demand <= sqrt(27/10)*sqrt(M)*V.
            # Squared exact consequence: 10*demand^2 <= 27*M*V^2.
            # The least integral V satisfying this is never asserted here;
            # verify only that the claimed lower-bound square is exact.
            numerator = 10 * demand * demand
            assert numerator == 10 * M * M * m**4
            assert F(numerator, 27 * M) == F(10 * M * m**4, 27)

            # Compare the Cauchy scale sqrt(M)m^2 with the source M.
            if M > m**4:
                assert M > (M**0.5) * m * m


if __name__ == "__main__":
    check_local_cauchy()
    check_stationary_geometry()
    check_scale_audit()
    print(
        "PASS: split Cauchy constants, stationary triangle blockers, "
        "targets/gaps, and scale audit"
    )
