#!/usr/bin/env python3
"""Checks for QUADRATIC_BASE_WORD_DETACHED_REUSE_BARRIER.md."""

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


def construction(q, D, m):
    l = (F(-3), F(0))
    r = (F(3), F(0))
    t = (F(0), F(5))
    v = (F(-2), F(-1))
    u = (F(2), F(-1))
    anchors = [l, r, t]

    eps = F(1, 10**8 * q**4 * D**4)
    cells = []
    for k in range(1, q + 1):
        s = F(k, q + 1)
        bend = s * (1 - s)
        z = (F(-3) + 3 * s - bend, 5 * s + bend)
        cell = []
        for d in range(1, D + 1):
            # Tiny rational general-position perturbations of the macro
            # vertex; only one point per cell is used in a base word.
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


def check_geometry():
    for q, D, m in ((2, 2, 2), (3, 3, 3), (4, 3, 3), (5, 3, 3)):
        anchors, v, u, cells, G, X = construction(q, D, m)
        all_points = anchors + [v, u] + G + X + [p for cell in cells for p in cell]
        assert len(all_points) == len(set(all_points))
        assert all(orient(*triple) != 0 for triple in combinations(all_points, 3))

        lr = frozenset((anchors[0], anchors[1]))
        rt = frozenset((anchors[1], anchors[2]))
        words = list(product(range(D), repeat=q))
        assert len(words) == D**q
        bases = []
        for word in words:
            B = anchors + [cells[k][word[k]] for k in range(q)]
            bases.append(frozenset(B))
            assert is_convex(B)
            assert all(insertion_edge(B, x) == lr for x in X)
            assert all(insertion_edge(B, g) == rt for g in G)
            assert is_convex(B + [v])
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
                    assert insertion_edge(B + [x], g) == rt
                    assert insertion_edge(B + [g], x) == lr
            assert all(not is_convex(B + list(pair)) for pair in combinations(G, 2))
            assert all(not is_convex(B + list(pair)) for pair in combinations(X, 2))

        assert len(set(bases)) == D**q

        # Named target and exact base-retaining bank counts.
        M = D**q
        assert M * m * m == len(words) * len(G) * len(X)
        Q = {frozenset(B | {v}) for B in bases}
        A = {frozenset(B | {g}) for B in bases for g in G}
        C = {frozenset(B | {x}) for B in bases for x in X}
        E = {frozenset(B | {g, v, u}) for B in bases for g in G}
        W = {frozenset((x, v)) for x in X}
        mixed = {
            frozenset(B | SG | SX)
            for B in bases
            for SG in [frozenset()] + [frozenset((g,)) for g in G]
            for SX in [frozenset()] + [frozenset((x,)) for x in X]
        }
        assert len(Q) == M
        assert len(A) == len(C) == len(E) == M * m
        assert len(W) == m
        assert len(mixed) == M * (m + 1) ** 2


def check_decoder_bound():
    for q in range(2, 10):
        for D in (2, 3, 5, 11):
            M = D**q
            for h in range(q + 1):
                Sh = sum(comb(q, s) * D**s for s in range(h + 1))
                assert Sh <= (q + 1) * 2**q * D**h
                lower = F(M, Sh)
                coarse = F(D ** (q - h), (q + 1) * 2**q)
                assert lower >= coarse
                if h < q:
                    assert D ** (q - h) >= 1


if __name__ == "__main__":
    check_geometry()
    check_decoder_bound()
    print(
        "PASS: quadratic base words, all target/gap states, exact baseline bank, "
        "and decoder load"
    )
