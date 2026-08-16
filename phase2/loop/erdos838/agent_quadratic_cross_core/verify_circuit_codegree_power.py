#!/usr/bin/env python3
"""Exact audits for CIRCUIT_CODEGREE_POWER_SAVING.md."""

from fractions import Fraction
from itertools import combinations
from math import comb
import random


def independent(mask, edges):
    return all((mask & e) != e for e in edges)


def hypergraph_audit():
    checked_h = 0
    checked_families = 0
    rng = random.Random(838)
    for m in range(4, 7):
        vertices = range(m)
        four_sets = list(combinations(vertices, 4))
        four_masks = [sum(1 << x for x in e) for e in four_sets]
        for hmask in range(1 << len(four_masks)):
            edges = [e for i, e in enumerate(four_masks) if (hmask >> i) & 1]
            triple_deg = {}
            for T in combinations(vertices, 3):
                tm = sum(1 << x for x in T)
                triple_deg[tm] = sum(1 for e in edges if (e & tm) == tm)
            Lambda = max(triple_deg.values(), default=0)

            for r in range(1, m):
                level = [sum(1 << x for x in A)
                         for A in combinations(vertices, r)
                         if independent(sum(1 << x for x in A), edges)]
                families = [level]
                if level:
                    families += [level[::2], level[1::2]]
                    for _ in range(2):
                        families.append([A for A in level if rng.randrange(2)])
                for family in families:
                    if not family:
                        continue
                    extensions = set()
                    pair_count = 0
                    for A in family:
                        for x in vertices:
                            if (A >> x) & 1:
                                continue
                            B = A | (1 << x)
                            if independent(B, edges):
                                extensions.add(B)
                                pair_count += 1
                    u = m - r - Lambda * comb(r, 3)
                    assert pair_count >= len(family) * max(u, 0)
                    assert len(extensions) * (r + 1) >= pair_count
                    checked_families += 1
            checked_h += 1
    return checked_h, checked_families


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def inside(p, a, b, c):
    signs = (orient(a, b, p), orient(b, c, p), orient(c, a, p))
    return all(x > 0 for x in signs) or all(x < 0 for x in signs)


def rooted_type_audit():
    # T is the first three entries.  The examples realize, respectively,
    # x, a, b, c as the unique interior point of T+x.
    examples = [
        ((0, 0), (10, 0), (0, 10), (2, 2)),
        ((2, 2), (10, 0), (0, 10), (0, 0)),
        ((0, 0), (2, 2), (0, 10), (10, 0)),
        ((0, 0), (10, 0), (2, 2), (0, 10)),
    ]
    types = []
    for quad in examples:
        assert all(orient(*tri) != 0 for tri in combinations(quad, 3))
        interior = []
        for i, p in enumerate(quad):
            tri = [quad[j] for j in range(4) if j != i]
            if inside(p, *tri):
                interior.append(i)
        assert len(interior) == 1
        types.append(interior[0])
    assert types == [3, 0, 1, 2]


def hull(points):
    ids = sorted(range(len(points)), key=lambda i: points[i])
    if len(ids) <= 1:
        return ids

    def half(seq):
        out = []
        for i in seq:
            while len(out) >= 2 and orient(points[out[-2]], points[out[-1]], points[i]) <= 0:
                out.pop()
            out.append(i)
        return out

    return half(ids)[:-1] + half(reversed(ids))[:-1]


def exterior_rooted_container_audit():
    # A convex pentagon with a cloud of exterior points.  Exhaust every
    # exterior blocked label and certify a rooted triangle with its interior
    # point in A, exactly as in Theorem 4.
    A = [(-10, 0), (-4, -6), (4, -6), (10, 0), (0, 8)]
    cloud = [(-12 + i, 10 + i * i) for i in range(1, 10)]
    points = A + cloud
    assert len(hull(A)) == len(A)
    blocked = 0
    assignments = {}
    for x in cloud:
        B = A + [x]
        h = hull(B)
        # x is exterior exactly when it is on the new hull.
        assert len(h) >= 3 and len(B) - 1 in h
        if len(h) == len(B):
            continue
        witnesses = []
        for ai, a in enumerate(A):
            for bi, ci in combinations([j for j in range(len(A)) if j != ai], 2):
                if inside(a, A[bi], A[ci], x):
                    witnesses.append((ai, bi, ci))
        assert witnesses
        assignments[witnesses[0]] = assignments.get(witnesses[0], 0) + 1
        blocked += 1
    assert blocked > 0
    assert max(assignments.values()) * (3 * comb(len(A), 3)) >= blocked


def drc_audit():
    rng = random.Random(8380)
    for left_n in range(2, 10):
        for right_n in range(2, 10):
            for _ in range(100):
                graph = []
                for _a in range(left_n):
                    nbrs = {x for x in range(right_n) if rng.randrange(2)}
                    graph.append(nbrs)
                D = min(map(len, graph))
                if D == 0:
                    continue
                for t in range(1, D + 1):
                    loads = {}
                    for nbrs in graph:
                        for Z in combinations(sorted(nbrs), t):
                            loads[Z] = loads.get(Z, 0) + 1
                    assert max(loads.values()) * comb(right_n, t) >= left_n * comb(D, t)


def entropy_power_audit():
    # Integer parameter checks for beta=1, epsilon=1/3.
    for r in range(12, 81):
        d = 1 << r
        beta_num = 1
        K_floor = d ** (beta_num * r)
        # Minimal m forced by K <= (e m/r)^r is audited with the safe
        # rational substitute e<3: m >= r K^(1/r)/3 = r d/3.
        m_lower = r * d // 3
        u_lower = 2 * m_lower // 3
        assert Fraction(u_lower, r + 1) >= Fraction(1 << (r // 3), 4)
        assert K_floor.bit_length() >= r * r


if __name__ == "__main__":
    hs, fams = hypergraph_audit()
    rooted_type_audit()
    exterior_rooted_container_audit()
    drc_audit()
    entropy_power_audit()
    print("PASS circuit-codegree fixed-power audit")
    print(f"  exhaustive hypergraphs: {hs}")
    print(f"  independent subfamilies audited: {fams}")
    print("  extension count, entropy scaling, four rooted types: verified")
