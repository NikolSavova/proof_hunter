#!/usr/bin/env python3
"""Exact audits for QUADRATIC_CROSS_CORE_SHIELD.md."""

from fractions import Fraction
from itertools import combinations
from math import comb


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


def is_face(points):
    return len(hull(points)) == len(points)


def inside_triangle_strict(p, a, b, c):
    vals = (orient(a, b, p), orient(b, c, p), orient(c, a, p))
    return all(v > 0 for v in vals) or all(v < 0 for v in vals)


def circle_point(t):
    return (2 * t / (1 + t * t), (t * t - 1) / (1 + t * t))


def construction(M=4, N=6):
    eta = Fraction(1, 10**6)
    delta = Fraction(1, 10**8)
    u = circle_point(Fraction(-1))
    v = circle_point(Fraction(1))
    left = [circle_point(Fraction(-1) + q * eta)
            for q in range(1, M + 1)]
    right = [circle_point(Fraction(1) - q * eta)
             for q in range(1, M + 1)]
    pocket = [(delta * i * i, Fraction(i)) for i in range(1, N + 1)]
    return u, v, left, right, pocket


def geometry_audit(M=4, s=2, N=6):
    u, v, left, right, pocket = construction(M, N)
    all_points = [u, v] + left + right + pocket
    assert all(orient(*triple) != 0 for triple in combinations(all_points, 3))

    lower = [u, v] + left + right
    assert is_face(lower)
    assert all(is_face(lower + [x]) for x in pocket)

    for i, j in combinations(range(N), 2):
        assert inside_triangle_strict(pocket[i], u, v, pocket[j])
        for ell in left:
            for rr in right:
                assert inside_triangle_strict(pocket[i], ell, rr, pocket[j])

    cores = []
    for ls in combinations(left, s):
        for rs in combinations(right, s):
            core = (u, v) + ls + rs
            cores.append((frozenset(ls), frozenset(rs), core))
            assert is_face(core)
            for x in pocket:
                assert is_face(core + (x,))
            for i, j in combinations(range(N), 2):
                h = set(hull(core + (pocket[i], pocket[j])))
                assert h == set(core + (pocket[j],))

    assert len(cores) == comb(M, s) ** 2
    return (u, v, left, right, pocket, cores)


def local_face_audit(M=4, s=2, N=6):
    u, v, left, right, pocket, cores = geometry_audit(M, s, N)
    d = N // 2
    selected = [(i, j) for i in range(d) for j in range(d, N)]
    assert all(sum(1 for a, _ in selected if a == i) == d for i in range(d))
    assert len(selected) == d * d

    universe = set()
    checked = 0
    for ls, rs, core in cores:
        for i, j in selected:
            base = list(core)
            # Exhaust every local candidate containing both pocket labels.
            for mask in range(1 << len(base)):
                f = [base[q] for q in range(len(base)) if (mask >> q) & 1]
                f += [pocket[i], pocket[j]]
                checked += 1
                if not is_face(f):
                    continue
                fs = frozenset(f)
                universe.add(fs)
                assert not (fs & ls) or not (fs & rs)

    A = sum(comb(M, a) for a in range(s + 1))
    bound = 8 * comb(N, 2) * A
    assert len(universe) <= bound

    K = comb(M, s) ** 2
    e = d * d
    demand = K * e
    cross_demand = K * (K - 1) * e * e
    assert demand / max(len(universe), 1) >= demand / bound
    assert cross_demand / max(len(universe) ** 2, 1) >= cross_demand / (bound * bound)
    return checked, len(universe), bound, demand, cross_demand


def scaling_audit():
    # With source rank rho=2s+3 and M=2^(lambda rho),
    # log K / rho^2 tends to lambda.  Choosing
    # d=2^((lambda-1)rho), N=2d is within a constant of n/2^rho.
    rows = []
    lam = 2
    for rho in range(11, 84, 2):
        s = (rho - 3) // 2
        log2_M = lam * rho
        M = 1 << log2_M
        K = comb(M, s) ** 2
        ratio = K.bit_length() / (rho * rho)
        rows.append(ratio)
        d = 1 << ((lam - 1) * rho)
        N = 2 * d
        n = 2 * M + N + 2
        natural_cap = Fraction(n, 1 << rho)
        assert d <= natural_cap <= 3 * d
    assert rows[-1] > 1.8
    assert rows[-1] > rows[0]


if __name__ == "__main__":
    checked, actual, bound, demand, cross = local_face_audit()
    scaling_audit()
    print("PASS quadratic crossing-core shield audit")
    print(f"  exact local candidates checked: {checked}")
    print(f"  actual local universe / theorem bound: {actual} / {bound}")
    print(f"  capped single-record demand: {demand}")
    print(f"  ordered cross-core pair demand: {cross}")
    print("  strict geometry, shield erasure, and quadratic scaling: verified")
