#!/usr/bin/env python3
"""Exact checks for RANK_SAFE_ENDPOINT_SURPLUS_GATE.md."""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations
from math import comb, log2
from random import Random


def det(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def is_convex(indices, points):
    if len(indices) <= 3:
        return True
    for x in indices:
        others = [z for z in indices if z != x]
        for a, b, c in combinations(others, 3):
            signs = (det(points[a], points[b], points[x]),
                     det(points[b], points[c], points[x]),
                     det(points[c], points[a], points[x]))
            if all(s > 0 for s in signs) or all(s < 0 for s in signs):
                return False
    return True


def endpoint_identity(points):
    n = len(points)
    order = tuple(sorted(range(n), key=lambda i: points[i][0]))
    pos = {x: i for i, x in enumerate(order)}
    caps = {(i, j): 0 for i in range(n) for j in range(i, n)}
    cups = {(i, j): 0 for i in range(n) for j in range(i, n)}
    faces = 0
    rank = 0
    for mask in range(1, 1 << n):
        inds = [x for x in order if mask >> x & 1]
        signs = [det(points[a], points[b], points[c])
                 for a, b, c in combinations(inds, 3)]
        cap = all(s < 0 for s in signs)
        cup = all(s > 0 for s in signs)
        key = (pos[inds[0]], pos[inds[-1]])
        caps[key] += cap
        cups[key] += cup
        if is_convex(inds, points):
            faces += 1
            rank = max(rank, len(inds))
    ctotal, utotal = sum(caps.values()), sum(cups.values())
    fibres = {e: caps[e] * cups[e] for e in caps}
    assert faces == sum(fibres.values())
    m = max(fibres.values())
    assert ctotal * utotal * m >= faces * faces
    capacity = sum(comb(n - 2, j) for j in range(max(0, rank - 1)))
    assert m <= capacity
    return ctotal, utotal, faces, rank, m, capacity


def finite_endpoint_audit():
    rng = Random(838)
    rows = []
    for n in range(5, 10):
        points = []
        while len(points) < n:
            p = (F(rng.randrange(-200, 201)), F(rng.randrange(-200, 201)))
            if p in points:
                continue
            if all(det(points[i], points[j], p)
                   for i, j in combinations(range(len(points)), 2)):
                points.append(p)
        rows.append((n, *endpoint_identity(points)))
    return rows


def pascal_dp(dmax):
    caps = [[0] * (d + 1) for d in range(dmax + 1)]
    faces = [[0] * (d + 1) for d in range(dmax + 1)]
    caps[0][0] = faces[0][0] = 1
    for d in range(1, dmax + 1):
        caps[d][0] = caps[d][d] = 1
        faces[d][0] = faces[d][d] = 1
        for i in range(1, d):
            caps[d][i] = (caps[d - 1][i]
                          + (1 + comb(d - 1, i)) * caps[d - 1][i - 1])
    for d in range(1, dmax + 1):
        for i in range(1, d):
            faces[d][i] = (faces[d - 1][i - 1] + faces[d - 1][i]
                           + caps[d - 1][i - 1]
                           * caps[d - 1][d - 1 - i])
    return caps, faces


def pascal_strong_glue_audit():
    # B=T(t,t/4), A=T(11t/20,3(11t/20)/4), and P=A prec B.
    caps, faces = pascal_dp(240)
    rows = []
    for t in (80, 160, 240):
        s = 11 * t // 20
        ia, ib = 3 * s // 4, t // 4
        a, b = comb(s, ia), comb(t, ib)
        ca, ua = caps[s][ia], caps[s][s - ia]
        cb, ub = caps[t][ib], caps[t][t - ib]
        va, vb = faces[s][ia], faces[t][ib]
        c = cb + (b + 1) * ca
        u = ua + (a + 1) * ub
        v = va + vb + ca * ub
        # Exact strong-glue recurrence and the simple polynomial upper bound
        # once the two desired directional terms dominate.
        if t >= 160:
            assert cb <= (b + 1) * ca
            assert ua <= (a + 1) * ub
            assert c * u <= 4 * (a + 1) * (b + 1) * ca * ub
            assert c * u <= 4 * (a + 1) * (b + 1) * v
            assert (log2(c) + log2(u) - log2(v)) / log2(a + b) < log2(3)
        rows.append({
            "t": t,
            "sizes": (a, b),
            "rank_bound": s + t,
            "sigma_exponent": (log2(c) + log2(u) - log2(v)) / log2(a + b),
            "face_coefficient": log2(v) / log2(a + b) ** 2,
        })
    return rows


def main():
    endpoint_rows = finite_endpoint_audit()
    pascal_rows = pascal_strong_glue_audit()
    print("PASS: rank-safe endpoint identity and Pascal fixed-chart barrier")
    print("endpoint rows:", endpoint_rows)
    print("Pascal rows:", pascal_rows)


if __name__ == "__main__":
    main()
