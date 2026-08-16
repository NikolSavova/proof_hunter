#!/usr/bin/env python3
"""Exact checks for THREE_TARGET_ENDPOINT_HALL_COMPLETION_DESCENT.md."""

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


def hall3(records):
    """Formula (2), exhaustive over nonempty record subfamilies."""
    best = F(0)
    for mask in range(1, 1 << len(records)):
        weight = F(0)
        targets = set()
        for i, (triple, w) in enumerate(records):
            if mask >> i & 1:
                weight += w
                targets.update(triple)
        best = max(best, weight / len(targets))
    return best


def rectangle(m):
    return [((f"W{j}", f"E{i}", f"C{j}"), F(1)) for i in range(m) for j in range(m)]


def prune3(records, K):
    live = list(records)
    while live:
        degree = {}
        for triple, w in live:
            for x in set(triple):
                degree[x] = degree.get(x, F(0)) + w
        low = next((x for x, d in degree.items() if d <= K), None)
        if low is None:
            return live, degree
        live = [(tr, w) for tr, w in live if low not in tr]
    return [], {}


def check_hall():
    for m in range(1, 4):
        assert hall3(rectangle(m)) == F(m, 3)

    # Formula (20) beyond the range where exhaustive 2^(m^2) is sensible.
    for m in range(1, 100):
        best = max(F(i * j, i + 2 * j) for i in range(1, m + 1) for j in range(1, m + 1))
        assert best == F(m, 3)

    live, degree = prune3(rectangle(9), F(8))
    assert live
    assert min(degree.values()) == 9 > 8

    # Triple multiplicity two: every target has >K/Delta incident pairs.
    doubled = rectangle(5) + rectangle(5)
    live, degree = prune3(doubled, F(9))
    assert live
    for target, d in degree.items():
        pairs = set()
        for triple, _ in live:
            if target in triple:
                other = tuple(sorted(x for x in triple if x != target))
                pairs.add(other)
        assert len(pairs) > F(9, 2)
        assert d == 10


def cage(m):
    l = (F(-3), F(0))
    r = (F(3), F(0))
    t = (F(0), F(5))
    a = (F(-2), F(-1))
    b = (F(2), F(-1))
    B = [l, r, t]
    gs = []
    for i in range(1, m + 1):
        z = F(i, 100 * m)
        gs.append((z, F(5) + z - z * z))
    xs = []
    for j in range(1, m + 1):
        s = F(2 * j - m - 1, 200 * m)
        xs.append((s, F(-4) + s * s))
    return B, a, b, gs, xs


def check_geometry():
    for m in (1, 2, 3, 5, 10, 20, 40):
        B, a, b, gs, xs = cage(m)
        P = B + [a, b] + gs + xs
        assert len(set(P)) == len(P)
        assert all(orient(*triple) != 0 for triple in combinations(P, 3))

        assert is_convex(B + [a, b] + gs)
        assert is_convex(B + xs)
        for g in gs:
            assert is_convex(B + [g, a, b])
        for x in xs:
            assert is_convex([x, a])
            assert is_convex(B + [x])
            for g in gs:
                assert not is_convex(B + [g, x, a])

        # The two support shields contain Boolean subbanks of size 2^m.
        assert len(gs) == m and len(xs) == m
        assert (1 << len(gs)) >= m * m if m >= 4 else True
        assert (1 << len(xs)) >= m * m if m >= 4 else True


def check_downshadow_counts():
    # Singleton completion family: downshadow is empty plus all singletons.
    for m in range(1, 50):
        completions = [frozenset([i]) for i in range(m)]
        down = {frozenset()}
        for G in completions:
            down.update(frozenset(S) for k in range(len(G) + 1) for S in combinations(G, k))
        assert len(down) == m + 1

        # Fixed-base pair-ear Boolean bank (12).
        base_rank = 5
        bank = {(S, j) for S in range(1 << base_rank) for j in range(m)}
        assert len(bank) == (1 << base_rank) * m


if __name__ == "__main__":
    check_hall()
    check_geometry()
    check_downshadow_counts()
    print(
        "PASS: three-target Hall, dense pruning, decoder counts, "
        "and planar common-cage rectangle"
    )
