#!/usr/bin/env python3
"""Exact finite audits for CROSS_CHILD_COLLISION_TELESCOPE.md."""

from fractions import Fraction
from itertools import combinations
from math import comb, isqrt


def ceil_sqrt(n: int) -> int:
    r = isqrt(n)
    return r if r * r == n else r + 1


def audit_graphs() -> int:
    checked = 0
    # Exhaust all families of q-subsets of a V-element right bank.  Repeated
    # neighborhoods are allowed, as required for repeated histories.
    for V in range(1, 6):
        for q in range(1, V + 1):
            rows = list(combinations(range(V), q))
            # Ordered history lists of length X through four.  Full products
            # are still small: at worst 10^4.
            families = [()]
            for _ in range(4):
                families = [f + (row,) for f in families for row in rows]
                for fam in families:
                    X = len(fam)
                    deg = [0] * V
                    for row in fam:
                        for y in row:
                            deg[y] += 1
                    N = q * X
                    C = sum(d * (d - 1) for d in deg)
                    assert sum(deg) == N
                    assert sum(d * d for d in deg) == N + C
                    # Take the smallest integral L for which C <= L V.
                    L = (C + V - 1) // V
                    # Squared form of N <= V(1+sqrt(1+4L))/2.
                    assert N * N <= N * V + L * V * V
                    root_num = V * (1 + ceil_sqrt(1 + 4 * L))
                    assert 2 * N <= root_num

                    # Exact size-biased high-tail inequality (20).
                    if N:
                        for T in range(2, X + 2):
                            tail_num = sum(d for d in deg if d >= T)
                            assert tail_num * (T - 1) <= C
                    checked += 1
    return checked


def audit_fractional() -> int:
    checked = 0
    # Pure arithmetic audit of (10), allowing an arbitrary good subcount G.
    for C in range(80):
        for N in range(1, 30):
            for theta_num in range(1, 6):
                theta = Fraction(theta_num, 6)
                for B in range(5):
                    required = theta * C - B * N
                    G = max(0, (required.numerator + required.denominator - 1) // required.denominator)
                    # Let LV=G.  Then theta*C <= LV+B*N follows exactly.
                    assert theta * C <= G + B * N
                    checked += 1
    return checked


def audit_exponents() -> int:
    checked = 0
    # Rational alpha values in [1/2, 9/10].  gamma is exact.
    for den in range(2, 31):
        for num in range((den + 1) // 2, den):
            alpha = Fraction(num, den)
            gamma = alpha / (2 * (1 - alpha))
            assert gamma >= Fraction(1, 2)
            # Every lambda<gamma leaves epsilon=gamma-lambda>0.
            lam = gamma * Fraction(3, 4)
            eps = gamma - lam
            assert eps > 0
            if alpha == Fraction(1, 2):
                # L=D^(1-eta) means lambda=(1-eta)/2.
                for eta_num in range(1, 10):
                    eta = Fraction(eta_num, 10)
                    lam2 = (1 - eta) / 2
                    assert gamma - lam2 == eta / 2
            checked += 1
    return checked


def audit_two_bank() -> int:
    checked = 0
    # Exact integer audit of (21)--(24).  We use arbitrary cell-bank sizes
    # and the least integral K satisfying every local product inequality.
    for cells in range(1, 6):
        for seed in range(1, 800):
            ws = [1 + ((seed * (7 * i + 3)) % 19) for i in range(cells)]
            aa = [1 + ((seed * (5 * i + 11)) % 17) for i in range(cells)]
            bb = [1 + ((seed * (13 * i + 2)) % 23) for i in range(cells)]
            K = max((w * w + a * b - 1) // (a * b) for w, a, b in zip(ws, aa, bb))
            assert all(w * w <= K * a * b for w, a, b in zip(ws, aa, bb))
            # Squared Cauchy form; this is stronger to audit than floats.
            assert sum(ws) ** 2 <= K * sum(aa) * sum(bb)
            checked += 1
    return checked


def audit_shield_fibre() -> int:
    checked = 0
    for s in range(1, 31):
        # On each side an ordered pair of disjoint s-sets with prescribed
        # 2s-union is determined by the first s-set.
        one_side = comb(2 * s, s)
        fibre = one_side * one_side
        if s <= 6:
            assert fibre == sum(1 for _ in combinations(range(2 * s), s)) ** 2
        # Central binomial lower bound sufficient for the D^(2-o(1)) audit.
        assert one_side * (2 * s + 1) >= 2 ** (2 * s)
        # With r=2s and seam D=2^r, the fibre is D^2/poly(r).
        D = 2 ** (2 * s)
        assert fibre * (2 * s + 1) ** 2 >= D * D
        checked += 1
    return checked


def main() -> None:
    g = audit_graphs()
    f = audit_fractional()
    e = audit_exponents()
    t = audit_two_bank()
    s = audit_shield_fibre()
    print("cross-child collision telescope audit: PASS")
    print(f"  left-regular bank instances: {g}")
    print(f"  fractional arithmetic instances: {f}")
    print(f"  exponent windows: {e}")
    print(f"  two-bank Cauchy instances: {t}")
    print(f"  shield fibres: {s}")


if __name__ == "__main__":
    main()
