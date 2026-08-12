#!/usr/bin/env python3
"""NC-P1 (wp3-a2): exact checks of the pentagonal toolkit and of Theorem P.5's
inequality against exact Mahonian rows.

(a) Pentagonal identity  I_m(k) = sum_n (-1)^n T(k - g_n), T(j) = C(m-1+j, m-1),
    for ALL 0 <= k <= m, exact integers, m in a test set.
(b) Bracketing  1 - x_1 - x_2 <= Phi(k) := I(k)/T(k) <= 1 - x_1 - x_2 + x_5 + x_7,
    and the floor Phi >= 1 - x - x^2 with x = k/(m+k-1), exact Fractions.
(c) Theorem P.5 truth: r(k) - 1 >= (m-1)/(2 k (m+k)) for 2 <= k <= m-1,
    exact integer cross-multiplication, every m in 8..MMAX; also the min of
    (r(k)-1) * k(m+k)/(m-1)  (float report) over three k-ranges.
(d) Extremes: min over m of the margin, worst (m, k).

Everything in the verdict path is exact int/Fraction arithmetic.
"""
import sys
from fractions import Fraction
from math import comb, isqrt

MMAX = 200

def mahonian_rows(mmax):
    """Yield (m, row) with row[k] = I_m(k), exact ints, incremental product."""
    poly = [1]
    for m in range(1, mmax + 1):
        # multiply by (1 + q + ... + q^{m-1}) via running-sum convolution
        old = poly
        n_new = len(old) + m - 1
        new = [0] * n_new
        run = 0
        for k in range(n_new):
            if k < len(old):
                run += old[k]
            if k - m >= 0 and k - m < len(old):
                run -= old[k - m]
            new[k] = run
        poly = new
        yield m, poly

def pent_exponents(limit):
    """Pentagonal numbers g_n = n(3n-1)/2, n = 1, -1, 2, -2, ... with signs,
    up to limit; returns list of (g, sign) sorted by g, plus g_0 = 0."""
    out = [(0, 1)]
    n = 1
    while True:
        g1 = n * (3 * n - 1) // 2
        g2 = n * (3 * n + 1) // 2
        s = -1 if n % 2 == 1 else 1
        added = False
        if g1 <= limit:
            out.append((g1, s)); added = True
        if g2 <= limit:
            out.append((g2, s)); added = True
        if not added:
            break
        n += 1
    return sorted(out)

def main():
    test_ms_identity = [4, 8, 12, 20, 30, 40, 60]
    print("== (a) pentagonal identity, exact, k <= m ==")
    rows = {}
    for m, row in mahonian_rows(max(test_ms_identity)):
        if m in test_ms_identity:
            rows[m] = list(row)
    ok_all = True
    for m in test_ms_identity:
        row = rows[m]
        pents = pent_exponents(m)
        bad = 0
        for k in range(0, m + 1):
            s = 0
            for g, sg in pents:
                if g <= k:
                    s += sg * comb(m - 1 + k - g, m - 1)
            if s != row[k]:
                bad += 1
        print(f"  m={m}: mismatches over k=0..{m}: {bad}")
        ok_all = ok_all and bad == 0
    print(f"  (a) VERDICT: {'PASS' if ok_all else 'FAIL'}")

    print("== (b) bracketing and floor, exact Fractions ==")
    ok_b = True
    worst_floor = None
    for m in [12, 30, 60]:
        row = rows.get(m)
        if row is None:
            for mm, r in mahonian_rows(m):
                if mm == m:
                    row = list(r)
        for k in range(2, m):
            T = lambda j: comb(m - 1 + j, m - 1) if j >= 0 else 0
            Phi = Fraction(row[k], T(k))
            def xg(g, kk):
                num = 1; den = 1
                for i in range(g):
                    num *= (kk - i); den *= (m + kk - 1 - i)
                return Fraction(num, den) if num > 0 else Fraction(0)
            x1 = xg(1, k); x2 = xg(2, k); x5 = xg(5, k) if k >= 5 else Fraction(0)
            x7 = xg(7, k) if k >= 7 else Fraction(0)
            lo = 1 - x1 - x2; hi = 1 - x1 - x2 + x5 + x7
            x = Fraction(k, m + k - 1)
            floor = 1 - x - x * x
            if not (lo <= Phi <= hi and Phi >= floor):
                ok_b = False
                print(f"  VIOLATION m={m} k={k}")
            marg = float(Phi - floor)
            if worst_floor is None or marg < worst_floor[0]:
                worst_floor = (marg, m, k, float(Phi))
    print(f"  brackets+floor hold on tested (m,k); min (Phi - (1-x-x^2)) = "
          f"{worst_floor[0]:.5f} at (m,k)=({worst_floor[1]},{worst_floor[2]}), Phi={worst_floor[3]:.5f}")
    print(f"  (b) VERDICT: {'PASS' if ok_b else 'FAIL'}")

    print(f"== (c) P.5 truth on exact rows, m = 8..{MMAX}, 2 <= k <= m-1 ==")
    viol = 0
    global_min_full = None   # min of (r-1)*2k(m+k)/(m-1)  (PASS iff >= 1)
    min_by_range = {"k<=m/4": None, "k<=m/2": None, "k<=3m/4": None, "k<=m-1": None}
    for m, row in mahonian_rows(MMAX):
        if m < 8:
            continue
        for k in range(2, m):
            a0, am, ap = row[k], row[k - 1], row[k + 1]
            # r - 1 = (a0^2 - am*ap)/(am*ap);  target (m-1)/(2k(m+k))
            num = a0 * a0 - am * ap
            den = am * ap
            # exact: num*2k(m+k) >= (m-1)*den ?
            lhs = num * 2 * k * (m + k)
            rhs = (m - 1) * den
            if lhs < rhs:
                viol += 1
                if viol < 10:
                    print(f"  VIOLATION m={m} k={k}")
            ratio = lhs / rhs  # float ok for reporting
            if global_min_full is None or ratio < global_min_full[0]:
                global_min_full = (ratio, m, k)
            for nm, frac in (("k<=m/4", 0.25), ("k<=m/2", 0.5), ("k<=3m/4", 0.75), ("k<=m-1", 1.0)):
                if k <= frac * m:
                    if min_by_range[nm] is None or ratio < min_by_range[nm][0]:
                        min_by_range[nm] = (ratio, m, k)
    print(f"  exact violations of  r(k)-1 >= (m-1)/(2k(m+k)):  {viol}")
    print(f"  global min of (r-1)/[(m-1)/(2k(m+k))] = {global_min_full[0]:.4f} "
          f"at (m,k)=({global_min_full[1]},{global_min_full[2]})")
    for nm in min_by_range:
        r_, m_, k_ = min_by_range[nm]
        print(f"  range {nm:8s}: min ratio {r_:.4f} at (m,k)=({m_},{k_})")
    print(f"  (c) VERDICT: {'PASS' if viol == 0 else 'FAIL'}")

    print("NC-P1 OVERALL:", "PASS" if (ok_all and ok_b and viol == 0) else "FAIL")

if __name__ == "__main__":
    main()
