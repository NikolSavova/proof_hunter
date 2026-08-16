#!/usr/bin/env python3
"""Audits for CROSS_CORE_DOWNSHADOW.md."""

from fractions import Fraction
from itertools import combinations
from math import comb, ceil, log2


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    def half(seq):
        out = []
        for p in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    lo = half(pts)
    hi = half(reversed(pts))
    return lo[:-1] + hi[:-1]


def inside_triangle_strict(p, a, b, c):
    vals = (orient(a, b, p), orient(b, c, p), orient(c, a, p))
    return all(x > 0 for x in vals) or all(x < 0 for x in vals)


def hall_audit(n=4, r=2):
    """Exhaust all nonempty source subfamilies for a small set system."""
    sources = list(combinations(range(n), r))
    checked = 0
    for source_mask in range(1, 1 << len(sources)):
        fam = [sources[i] for i in range(len(sources))
               if (source_mask >> i) & 1]
        # Give source A between one and three records deterministically.
        records = []
        for idx, A in enumerate(fam):
            for copy in range(1 + idx % 3):
                records.append((idx, copy, A))

        for t in range(r + 1):
            b = comb(r, t)
            neighbours = []
            degrees = {}
            for _, _, A in records:
                ns = {tuple(S) for S in combinations(A, r - t)}
                assert len(ns) == b
                neighbours.append(ns)
                for S in ns:
                    degrees[S] = degrees.get(S, 0) + 1
            Delta = max(degrees.values())
            K = ceil(Delta / b)

            # Exhaust every record subfamily and check duplicated Hall.
            q = len(records)
            for mask in range(1, 1 << q):
                U = [i for i in range(q) if (mask >> i) & 1]
                NU = set().union(*(neighbours[i] for i in U))
                assert len(U) <= K * len(NU)
            checked += 1
    return checked


def geometry_and_shadow_audit(m=7, N=6, k=3, d=3):
    u = (Fraction(-1), Fraction(0))
    v = (Fraction(1), Fraction(0))
    Y = []
    for q in range(1, m + 1):
        x = Fraction(-1) + Fraction(2 * q, m + 1)
        Y.append((x, x * x - 1))

    X = [(Fraction(i, 20 * N), Fraction(2**i))
         for i in range(1, N + 2)]

    all_sources = []
    for inds in combinations(range(m), k):
        B = [u, v] + [Y[i] for i in inds]
        assert len(hull(B)) == len(B)
        assert len(hull(B + [X[0]])) == len(B) + 1
        for j in range(1, d + 1):
            assert inside_triangle_strict(X[0], u, v, X[j])
            assert set(hull(B + [X[0], X[j]])) == set(B + [X[j]])
        all_sources.append(frozenset(B + [X[0]]))

    r = k + 3
    assert len(all_sources) == comb(m, k)
    for t in range(r + 1):
        actual = set()
        for A in all_sources:
            for S in combinations(sorted(A), r - t):
                actual.add(frozenset(S))
        formula = sum(comb(3, a) * comb(m, r - t - a)
                      for a in range(0, min(3, r - t) + 1)
                      if 0 <= r - t - a <= min(k, m))
        assert len(actual) == formula
        demand = d * comb(m, k)
        assert ceil(demand / len(actual)) >= 1
    return len(all_sources)


def entropy_threshold_audit():
    # alpha<1/2: log_2 d / r=(1-alpha)/alpha>1, beyond all 2^r downfaces.
    for alpha in (0.1, 0.25, 0.4, 0.49):
        assert (1 - alpha) / alpha > 1

    # alpha=1/2: central binomial loss is subexponential in r.
    for r in (20, 40, 80, 160):
        loss_log = r - log2(comb(r, r // 2))
        assert loss_log < log2(r) + 1
        assert loss_log / r < 0.25

    # For alpha>1/2, some binomial layer beats d exponentially.
    for alpha in (0.55, 0.6, 0.75, 0.9):
        r = 400
        best = log2(comb(r, r // 2)) / r
        assert best > (1 - alpha) / alpha

    # Coefficient-scale source-pair loss is linear, hence o(r^2).
    for alpha in (0.1, 0.25, 0.5, 0.9):
        for r in (100, 1000, 10000):
            log_d2 = 2 * (1 - alpha) / alpha * r
            if r >= 10000:
                assert log_d2 / (r * r) < 0.01 / alpha


if __name__ == "__main__":
    checked = hall_audit()
    sources = geometry_and_shadow_audit()
    entropy_threshold_audit()
    print("PASS cross-core proper-downshadow audit")
    print(f"  duplicated-Hall source systems checked: {checked}")
    print(f"  exact rational planar sources checked: {sources}")
    print("  exact shadow union and alpha-threshold audits: verified")
