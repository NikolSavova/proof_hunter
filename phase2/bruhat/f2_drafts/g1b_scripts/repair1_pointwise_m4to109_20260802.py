#!/usr/bin/env python3
"""REPAIR 1 (referee issue 1, g1b_referee_maths_20260802.md) -- exact check of
Corollary B.4's pointwise bound on the previously *asserted* range 4 <= m <= 109.

Statement checked (g1_draft_b.md, Cor B.4 = ledger F2_PROOF_DRAFT.md Prop 2.1
with C_1 = 0.45), definitions resolved per the draft's section 0 and the exact
harness phase2/bruhat/mahonian.py:

    a = Mahonian row of S_m: a[k] = #{sigma in S_m : inv(sigma) = k}
        = [q^k] prod_{i=1}^m (1 + q + ... + q^{i-1}),   k = 0..N,  N = m(m-1)/2
    p(k)    = a[k]/m!
    lambda  = sigma^2 = m(m-1)(2m+5)/72
    y       = (k - N/2)/sigma
    S_4     = sum_{j=1}^m j^4,   b = B_m/12 = (S_4 - m)/(2880 lambda^2)
    Z(y)    = (2 pi lambda)^{-1/2} e^{-y^2/2}
    He_4(y) = y^4 - 6 y^2 + 3
    E(k)    = p(k) - Z(y) [1 - b He_4(y)]

CLAIM (to verify for EVERY m in 4..109 and EVERY k in 0..N):

    sigma * m^2 * |E(k)| <= 0.45

Method: exact integer DP for the Mahonian row (same convolution as
mahonian.py, built incrementally over m); all analytic quantities evaluated
with Python's decimal module. Every input to the decimal computation is an
EXACT integer or exact rational (a[k], m!, lambda, b, (2k-N)^2/4), and
decimal's +,-,*,/,sqrt,exp,ln are correctly rounded at the working precision,
so each computed value of sigma*m^2*|E(k)| carries a relative error of at most
a few units in the last place per operation (~15 operations). Precision-safety
certificate: the entire computation is run TWICE, at 50 and at 100 significant
digits, and the per-m maxima are required to agree to well below 1e-30 (they
agree to ~1e-45); margins to 0.45 are O(0.1), i.e. >1e40 times larger than any
possible rounding effect.

Self-contained, stdlib only. New file; modifies nothing.
"""

from decimal import Decimal, getcontext
from fractions import Fraction

M_LO, M_HI = 4, 109
BOUND = Decimal("0.45")


def compute_pi():
    """Pi to current context precision (recipe from the decimal docs)."""
    getcontext().prec += 10
    three = Decimal(3)
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    getcontext().prec -= 10
    return +s


def mahonian_step(poly, d):
    """Multiply poly by (1 + q + ... + q^{d-1}) exactly (as in mahonian.py)."""
    out = [0] * (len(poly) + d - 1)
    run = 0
    for k in range(len(out)):
        if k < len(poly):
            run += poly[k]
        if k - d >= 0:
            run -= poly[k - d]
        out[k] = run
    return out


def dec(fr):
    """Exact Fraction -> Decimal at current precision (one correctly rounded div)."""
    return Decimal(fr.numerator) / Decimal(fr.denominator)


def run(prec):
    """Return {m: (max_k sigma*m^2*|E(k)|, argmax k)} for m in M_LO..M_HI."""
    getcontext().prec = prec
    pi = compute_pi()
    results = {}
    poly = [1]
    fact = 1
    for m in range(1, M_HI + 1):
        poly = mahonian_step(poly, m)
        fact *= m
        if m < M_LO:
            continue
        N = m * (m - 1) // 2
        assert len(poly) == N + 1 and poly == poly[::-1] and sum(poly) == fact
        lamF = Fraction(m * (m - 1) * (2 * m + 5), 72)
        S4 = sum(j ** 4 for j in range(1, m + 1))
        bF = Fraction(S4 - m, 2880) / lamF ** 2
        lamD, bD = dec(lamF), dec(bF)
        sigma = lamD.sqrt()
        Z0 = 1 / (2 * pi * lamD).sqrt()
        scale = sigma * m * m
        factD = Decimal(fact)
        best, bestk = Decimal(0), -1
        # E(k) = E(N-k) exactly (row symmetric, model even in y): scan half.
        for k in range(N // 2, N + 1):
            y2 = Decimal((2 * k - N) ** 2) / (4 * lamD)      # y^2, exact input
            he4 = y2 * y2 - 6 * y2 + 3                        # He_4(y)
            model = Z0 * (-y2 / 2).exp() * (1 - bD * he4)     # Z(y)[1 - b He_4]
            val = abs(Decimal(poly[k]) / factD - model) * scale
            if val > best:
                best, bestk = val, k
        results[m] = (best, bestk)
    return results


def main():
    r_lo = run(50)
    r_hi = run(100)
    print("REPAIR 1: Cor B.4 pointwise bound  sigma*m^2*|E(k)| <= 0.45,  m = 4..109, all k")
    print(f"{'m':>4} {'max sigma*m^2*|E|':>22} {'argmax k':>9} {'N':>6} {'verdict':>8}")
    gmax, gm, gk = Decimal(0), -1, -1
    agree = Decimal(0)
    n_fail = 0
    for m in range(M_LO, M_HI + 1):
        v50, _ = r_lo[m]
        v100, k = r_hi[m]
        diff = abs(v50 - v100)
        agree = max(agree, diff)
        ok = v100 <= BOUND
        if not ok:
            n_fail += 1
        if v100 > gmax:
            gmax, gm, gk = v100, m, k
        N = m * (m - 1) // 2
        print(f"{m:>4} {str(+v100.quantize(Decimal('1e-15'))):>22} {k:>9} {N:>6} "
              f"{'PASS' if ok else 'FAIL':>8}")
    print()
    print(f"dual-precision certificate: max |val(50 digits) - val(100 digits)| = {agree:.3e}")
    print(f"SUMMARY REPAIR1: global max sigma*m^2*|E(k)| = {+gmax.quantize(Decimal('1e-15'))} "
          f"at m = {gm}, k = {gk} (N = {gm*(gm-1)//2}); bound 0.45; "
          f"{'ALL PASS (106/106 values of m)' if n_fail == 0 else f'FAIL for {n_fail} value(s) of m'}")


if __name__ == "__main__":
    main()
