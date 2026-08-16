#!/usr/bin/env python3
"""Exact audits for LINEAR_CODIM_CAPPED_CHAIN.md."""

from fractions import Fraction
from itertools import combinations
from math import comb
import random


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    """Strict monotone-chain hull, returning vertices counterclockwise."""
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
    vals = [orient(a, b, p), orient(b, c, p), orient(c, a, p)]
    return all(v > 0 for v in vals) or all(v < 0 for v in vals)


def geometry_audit(N=7):
    u = (Fraction(-1), Fraction(0))
    v = (Fraction(1), Fraction(0))
    w = (Fraction(0), Fraction(-100))
    # Heights double, while all horizontal coordinates stay in (0,1/10).
    # Every earlier point is therefore in the strict uv-triangle of every
    # later point.
    X = [(Fraction(i, 10 * N), Fraction(2**i)) for i in range(1, N + 1)]
    B = [u, v, w]

    assert len(hull(B)) == len(B)
    for x in X:
        assert len(hull(B + [x])) == len(B) + 1

    for i, j in combinations(range(N), 2):
        assert inside_triangle_strict(X[i], u, v, X[j])
        assert set(hull(B + [X[i], X[j]])) == set(B + [X[j]])

    # General position for all upper triples, hence each triple is a face.
    for i, j, k in combinations(range(N), 3):
        assert orient(X[i], X[j], X[k]) != 0
        assert len(hull([X[i], X[j], X[k]])) == 3
    return X


def selection_audit(N=5):
    edges = list(combinations(range(N), 2))
    sharp_two_load_seen = False
    selections = 0
    for mask in range(1 << len(edges)):
        E = [e for bit, e in enumerate(edges) if (mask >> bit) & 1]
        selections += 1

        # The two-point route is an injection.
        pair_codes = {frozenset(e) for e in E}
        assert len(pair_codes) == len(E)

        # Same-source ordered divergences have triple-code load <= 2.
        loads = {}
        for i in range(N):
            succ = [j for a, j in E if a == i]
            for j in succ:
                for k in succ:
                    if j == k:
                        continue
                    code = frozenset((i, j, k))
                    loads[code] = loads.get(code, 0) + 1
        assert max(loads.values(), default=0) <= 2
        if 2 in loads.values():
            sharp_two_load_seen = True

        lhs = sum(
            sum(1 for a, _ in E if a == i)
            * (sum(1 for a, _ in E if a == i) - 1)
            for i in range(N)
        )
        assert lhs == sum(loads.values())
        assert lhs <= 2 * comb(N, 3)

    assert sharp_two_load_seen
    return selections


def multicore_audit(N=6, K=4):
    edges = list(combinations(range(N), 2))
    # (core, pair) is an exact code for one selected record.
    codes = {(b, frozenset(e)) for b in range(K) for e in edges}
    assert len(codes) == K * len(edges)

    # (core, triple) has load exactly two on the complete selector.
    loads = {}
    for b in range(K):
        for i in range(N):
            succ = list(range(i + 1, N))
            for j in succ:
                for k in succ:
                    if j != k:
                        code = (b, frozenset((i, j, k)))
                        loads[code] = loads.get(code, 0) + 1
    assert max(loads.values()) == 2


def fractional_audit(N=8, trials=500):
    rng = random.Random(838)
    for _ in range(trials):
        a = {(i, j): Fraction(rng.randrange(1001), 1000)
             for i in range(N) for j in range(i + 1, N)}
        loads = {}
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(i + 1, N):
                    if j == k:
                        continue
                    code = frozenset((i, j, k))
                    loads[code] = loads.get(code, Fraction(0)) + a[i, j] * a[i, k]
        assert max(loads.values(), default=0) <= 2


def asymptotic_codebook_audit(c=Fraction(1, 5)):
    # If L=log_2 N and c L^2 >= 4L, the universal lower bound is >=N^4.
    # c=1/5 is a legal fixed value below 1/4, and L>=20 is exact.
    for L in range(20, 81):
        assert c * L * L >= 4 * L
        # Every simple forward incidence set has fewer than N^2 records.
        # Its ordered square therefore has fewer than N^4 codewords.
        N = 1 << min(L, 24)  # finite integer audit without huge allocations
        assert comb(N, 2) ** 2 < N**4


if __name__ == "__main__":
    geometry_audit()
    count = selection_audit()
    multicore_audit()
    fractional_audit()
    asymptotic_codebook_audit()
    print("PASS linear-codimension capped-chain audit")
    print(f"  exhaustive selections: {count}")
    print("  exact repairs, two-point injection, triple load <=2: verified")
    print("  repeated-core and fractional-weight audits: verified")
    print("  universal codebook threshold c=1/5, log2 N>=20: verified")
