#!/usr/bin/env python3
"""Checks for DETACHED_LOAD_SOURCE_EAR_HALL.md."""

from fractions import Fraction as F
from itertools import combinations


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    points = sorted(set(points))
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


def hall_load(edges):
    """Exact formula (2) by exhaustive nonempty edge subfamilies."""
    best = F(0)
    m = len(edges)
    for mask in range(1, 1 << m):
        weight = F(0)
        vertices = set()
        for i, (u, v, w) in enumerate(edges):
            if mask >> i & 1:
                weight += w
                vertices.add(u)
                vertices.add(v)
        best = max(best, weight / len(vertices))
    return best


def prune_core(edges, K):
    live = list(edges)
    while live:
        degree = {}
        for u, v, w in live:
            degree[u] = degree.get(u, F(0)) + w
            if v != u:
                degree[v] = degree.get(v, F(0)) + w
        low = next((x for x, d in degree.items() if d <= K), None)
        if low is None:
            return live, degree
        live = [e for e in live if e[0] != low and e[1] != low]
    return [], {}


def check_hall():
    # Fixed-W star: raw detached load m, exact fractional load m/(m+1).
    for m in range(1, 9):
        star = [("W", f"E{j}", F(1)) for j in range(m)]
        assert hall_load(star) == F(m, m + 1)

    # Deliberate weighted dense core.  Formula >K implies pruning leaves a
    # core of weighted minimum degree >K.
    dense = []
    for i in range(3):
        for j in range(4):
            dense.append((f"W{i}", f"E{j}", F(5, 2)))
    lam = hall_load(dense)
    assert lam == F(30, 7)
    core, degree = prune_core(dense, F(4))
    assert core and min(degree.values()) > 4

    # Collision multiplicity Delta=2: distinct degree is weighted
    # degree/Delta in the unweighted integral example.
    multi = []
    for i in range(3):
        for j in range(3):
            multi += [(f"w{i}", f"e{j}", F(1))] * 2
    core, degree = prune_core(multi, F(5))
    assert core
    for x, d in degree.items():
        neighbors = set()
        for u, v, _ in core:
            if u == x:
                neighbors.add(v)
            if v == x:
                neighbors.add(u)
        assert len(neighbors) > F(5, 2)


def check_cage():
    l = (F(-3), F(0))
    r = (F(3), F(0))
    t = (F(0), F(5))
    a = (F(-2), F(-1))
    x = (F(0), F(-4))
    B = [l, r, t]
    for m in (1, 2, 3, 5, 10, 20, 50):
        eps = F(1, 100 * m * m)
        bs = [(F(2) + eps * j, F(-1) + eps * j * j) for j in range(1, m + 1)]
        P = B + [a, x] + bs
        assert all(orient(*triple) != 0 for triple in combinations(P, 3))
        assert is_convex([x, a])
        assert not is_convex(B + [x, a])
        ears = []
        for b in bs:
            E = B + [a, b]
            assert is_convex(E)
            ears.append(tuple(sorted(E)))
        assert len(set(ears)) == m


if __name__ == "__main__":
    check_hall()
    check_cage()
    print(
        "PASS: exact Hall loads; fixed-W stars route through source ears; "
        "rational cages retain bad attachment"
    )
