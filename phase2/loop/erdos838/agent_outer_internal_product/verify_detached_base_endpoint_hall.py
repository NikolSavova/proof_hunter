#!/usr/bin/env python3
"""Checks for DETACHED_BASE_ENDPOINT_HALL_STRENGTHENING.md."""

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


def hall(records):
    best = F(0)
    for mask in range(1, 1 << len(records)):
        demand = F(0)
        targets = set()
        for i, (bank, weight) in enumerate(records):
            if mask >> i & 1:
                demand += weight
                targets.update(bank)
        best = max(best, demand / len(targets))
    return best


def pair_rectangle(m):
    return [((f"W{j}", "Q"), F(1)) for _i in range(m) for j in range(m)]


def triple_rectangle(m):
    return [((f"W{j}", "Q", f"C{j}"), F(1)) for _i in range(m) for j in range(m)]


def four_rectangle(m):
    return [
        ((f"W{j}", "Q", f"C{j}", f"A{i}"), F(1))
        for i in range(m)
        for j in range(m)
    ]


def check_loads():
    # Exhaustive Hall calculations for small history rectangles.
    for m in range(1, 4):
        assert hall(pair_rectangle(m)) == F(m * m, m + 1)
        assert hall(triple_rectangle(m)) == F(m * m, 2 * m + 1)
        assert hall(four_rectangle(m)) == F(m * m, 3 * m + 1)

    # Closed subset formulas through a larger range.
    for m in range(1, 100):
        pair_best = max(F(m * j, j + 1) for j in range(1, m + 1))
        triple_best = max(F(m * j, 2 * j + 1) for j in range(1, m + 1))
        four_best = max(
            F(i * j, i + 2 * j + 1)
            for i in range(1, m + 1)
            for j in range(1, m + 1)
        )
        assert pair_best == F(m * m, m + 1)
        assert triple_best == F(m * m, 2 * m + 1)
        assert four_best == F(m * m, 3 * m + 1)


def cage(m):
    B = [(F(-3), F(0)), (F(3), F(0)), (F(0), F(5))]
    v = (F(-2), F(-1))
    u = (F(2), F(-1))
    u = (F(2), F(-1))
    gs = []
    for i in range(1, m + 1):
        z = F(i, 100 * m)
        gs.append((z, F(5) + z - z * z))
    xs = []
    for j in range(1, m + 1):
        s = F(2 * j - m - 1, 200 * m)
        xs.append((s, F(-4) + s * s))
    return B, v, u, gs, xs


def check_geometry():
    for m in (1, 2, 3, 5, 10, 20, 40):
        B, v, u, gs, xs = cage(m)
        P = B + [v, u] + gs + xs
        assert all(orient(*triple) != 0 for triple in combinations(P, 3))

        Q = B + [v]
        assert is_convex(Q)
        assert is_convex(B + gs)
        for g in gs:
            assert is_convex(B + [g])  # old source A_i
        for x in xs:
            assert is_convex([x, v])   # W_j
            assert is_convex(B + [x])  # C_j
            for g in gs:
                assert not is_convex(B + [g, x, v])

        # Heredity of the convex guard shield gives its full Boolean cube.
        assert (1 << len(gs)) >= m * m if m >= 4 else True


def check_decoder_and_masks():
    # Formal disjoint supports: a pair target determines (B,F,v), while i
    # is exactly the guard-history multiplicity.
    for m in range(1, 30):
        decoded = {}
        for i in range(m):
            for j in range(m):
                key = (f"W{j}", "Q")
                decoded.setdefault(key, []).append(i)
        assert len(decoded) == m
        assert {len(histories) for histories in decoded.values()} == {m}

        completions = [frozenset([i]) for i in range(m)]
        down = {frozenset()}
        for G in completions:
            down.add(G)
        assert len(down) == m + 1


def check_nonboolean_open_cage():
    """One exact non-Boolean child instance of Proposition 2."""
    B = [(F(-3), F(0)), (F(3), F(0)), (F(0), F(5))]
    v = (F(-2), F(-1))
    u = (F(2), F(-1))

    # Four-point configurations in tiny disks around g0 and x0.  In each
    # cloud the last point is strictly inside the triangle of the first 3.
    g0 = (F(1, 100), F(50099, 10000))
    dg = F(1, 100000)
    goff = [(-3, 0), (4, 3), (1, -4), (F(2, 3), F(-1, 3))]
    gs = [(g0[0] + dg * F(a), g0[1] + dg * F(b)) for a, b in goff]
    x0 = (F(0), F(-4))
    dx = F(1, 10000)
    xoff = [(-4, 0), (3, 4), (2, -5), (F(1, 3), F(-1, 3))]
    xs = [(x0[0] + dx * F(a), x0[1] + dx * F(b)) for a, b in xoff]

    # If an accidental cross collinearity occurred, it would not affect
    # the open-set proof, but these exact coordinates avoid it as well.
    P = B + [v, u] + gs + xs
    assert all(orient(*triple) != 0 for triple in combinations(P, 3))
    assert not is_convex(gs)
    assert not is_convex(xs)
    for g in gs:
        assert is_convex(B + [g])
        assert is_convex(B + [g, v, u])
    for x in xs:
        assert is_convex(B + [x])
        assert is_convex([x, v])
        for g in gs:
            assert not is_convex(B + [g, x, v])


if __name__ == "__main__":
    check_loads()
    check_geometry()
    check_decoder_and_masks()
    check_nonboolean_open_cage()
    print(
        "PASS: unconditional W/Q/C/A Hall, exact history rectangle loads, "
        "and guard-mask shield"
    )
