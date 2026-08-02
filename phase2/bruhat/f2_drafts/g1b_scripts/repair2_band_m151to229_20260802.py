#!/usr/bin/env python3
"""REPAIR 2 (referee issue 2, g1b_referee_maths_20260802.md) -- close the band
150 < m < m_1(y_0) of the window law by direct exact computation, m = 151..229.

Statement checked (g1_draft_b.md, Theorem B.8 / Corollary B.9 = ledger
F2_PROOF_DRAFT.md Prop 2.2), definitions resolved per the draft's section 0,
Theorem B.8, and the exact harness phase2/bruhat/mahonian.py (which the
previous m <= 150 verification used):

    a = Mahonian row of S_m (a[k] = [q^k] prod_{i=1}^m (1+q+...+q^{i-1}))
    r(k)   = p(k)^2 / (p(k-1) p(k+1)) = a[k]^2 / (a[k-1] a[k+1])
             [the LOG-CONCAVITY ratio: Thm B.8 defines r via
              r(k) - 1 = D(k)/(p(k-1)p(k+1)), D = p(k)^2 - p(k-1)p(k+1);
              identical to mahonian.py's min_ratio -- NOT a_k/a_{k-1}]
    N = m(m-1)/2,  lambda = sigma^2 = m(m-1)(2m+5)/72,  y = (k - N/2)/sigma
    B_m    = 12 b = (S_4 - m)/(240 lambda^2),  S_4 = sum_{j=1}^m j^4
    E_1(k) = sigma^2 log r(k) - 1 - B_m (y^2 - 1)

CLAIM (Cor B.9 with the section-6 constants table): for each table row
(y_0, m_1, C_2) and every m >= m_1, every k with |y| <= y_0:
    m^2 |E_1(k)| <= C_2(y_0).
The draft proves this for m >= m_1; the exact harness had verified m <= 150.
This script verifies EVERY m in the open band 151 <= m <= m_1 - 1 for every
table row:
    (y_0, m_1, C_2) = (0.1, 180, 1.1), (0.5, 180, 1.6), (1.0, 180, 3.1),
                      (2.0, 200, 38), (3.0, 230, 3940).
[The sixth row (3.0, 2000, 475) claims the constant 475 only for m >= 2000;
on 230 <= m <= 1999 the law already holds with the proved constant 3940 of the
(3.0, 230) row, so the only open band below any m_1 is 151..229, all covered
here. The y_0 = 3 band maximum is additionally reported against 475 for
information.]

Method: exact integer DP for the Mahonian rows, built ONCE incrementally over
m = 1..229 (each intermediate row IS the S_m row); window membership decided by
EXACT rational comparison (k in window iff (2k-N)^2 <= 4 y_0^2 lambda). For
each interior k, r(k) is the exact rational a[k]^2/(a[k-1]a[k+1]); its log is
computed in decimal as ln(num/den) -- num/den = 1 + O(1/lambda), so there is NO
catastrophic cancellation: one correctly rounded big-integer division plus one
correctly rounded ln near 1. lambda, B_m, y^2 enter as exact rationals.
Precision-safety certificate: the whole computation is run at 50 and at 100
significant digits and the per-(row, m) maxima must agree to below 1e-30
(rounding analysis: relative error ~1e-prec on ln(r) ~ 1e-6 gives absolute
error < 1e-50 on E_1, ~1e-40 after the m^2 lambda scaling -- margins are O(0.1)
or larger). E_1(k) = E_1(N-k) exactly (row symmetric, window symmetric), so
only k >= N/2 is scanned.

Self-contained, stdlib only. New file; modifies nothing.
"""

from decimal import Decimal, getcontext
from fractions import Fraction

M_LO, M_HI = 151, 229

# (y_0 as exact Fraction, m_1, C_2) -- section 6 table of g1_draft_b.md.
ROWS = [
    (Fraction(1, 10), 180, Decimal("1.1")),
    (Fraction(1, 2), 180, Decimal("1.6")),
    (Fraction(1), 180, Decimal("3.1")),
    (Fraction(2), 200, Decimal("38")),
    (Fraction(3), 230, Decimal("3940")),
]
INFO_C2_Y3 = Decimal("475")  # (3.0, 2000) row, informational only on this band


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
    return Decimal(fr.numerator) / Decimal(fr.denominator)


def eval_m(m, a, prec):
    """Return list over ROWS of (max m^2|E_1| over the row's window, argmax k),
    entry None if m >= m_1 (band already proved).  Exact inputs, decimal evals."""
    getcontext().prec = prec
    N = m * (m - 1) // 2
    lamF = Fraction(m * (m - 1) * (2 * m + 5), 72)
    S4 = sum(j ** 4 for j in range(1, m + 1))
    BmF = Fraction(S4 - m, 240) / lamF ** 2
    lamD, BmD = dec(lamF), dec(BmF)
    m2 = Decimal(m * m)
    four_lam = 4 * lamF
    # exact window thresholds: k in window(y0) iff (2k-N)^2 <= 4 y0^2 lambda
    thr = [y0 * y0 * four_lam for (y0, _, _) in ROWS]
    thr_max = max(t for t, (_, m1, _) in zip(thr, ROWS) if m < m1)
    out = [[Decimal(0), -1] if m < m1 else None for (_, m1, _) in ROWS]
    k = N // 2
    while k <= N - 1:
        x2sq = Fraction((2 * k - N) ** 2)          # (2k-N)^2, exact
        if x2sq > thr_max:
            break
        num = a[k] * a[k]
        den = a[k - 1] * a[k + 1]
        lnr = (Decimal(num) / Decimal(den)).ln()   # log r(k), no cancellation
        y2 = Decimal((2 * k - N) ** 2) / (4 * lamD)
        e1 = m2 * abs(lamD * lnr - 1 - BmD * (y2 - 1))
        for i, (t, o) in enumerate(zip(thr, out)):
            if o is not None and x2sq <= t and e1 > o[0]:
                o[0], o[1] = e1, k
        k += 1
    return out


def run(prec):
    getcontext().prec = prec
    res = {}
    poly = [1]
    fact = 1
    for m in range(1, M_HI + 1):
        poly = mahonian_step(poly, m)
        fact *= m
        if M_LO <= m <= M_HI:
            N = m * (m - 1) // 2
            assert len(poly) == N + 1 and poly[0] == 1 and poly == poly[::-1] \
                and sum(poly) == fact
            res[m] = eval_m(m, poly, prec)
    return res


def main():
    r_lo = run(50)
    r_hi = run(100)
    labels = [f"y0={float(y0):g} (m1={m1}, C2={c2})" for (y0, m1, c2) in ROWS]
    print("REPAIR 2: Cor B.9 window law  m^2|E_1(k)| <= C_2(y_0) on |y| <= y_0,")
    print("band 151 <= m <= m_1(y_0) - 1 for every section-6 table row.")
    print(f"{'m':>4}", *[f"{l:>28}" for l in labels], sep="")
    agree = Decimal(0)
    band_max = [[Decimal(0), -1, -1] for _ in ROWS]   # val, m, k
    n_fail = 0
    for m in range(M_LO, M_HI + 1):
        cells = []
        for i, (_, m1, c2) in enumerate(ROWS):
            lo, hi = r_lo[m][i], r_hi[m][i]
            if hi is None:
                cells.append(f"{'- (proved, m>=m1)':>28}")
                continue
            agree = max(agree, abs(lo[0] - hi[0]))
            ok = hi[0] <= c2
            if not ok:
                n_fail += 1
            if hi[0] > band_max[i][0]:
                band_max[i] = [hi[0], m, hi[1]]
            cells.append(f"{str(+hi[0].quantize(Decimal('1e-6'))):>21} "
                         f"{'PASS' if ok else 'FAIL':>6}")
        print(f"{m:>4}", *cells, sep="")
    print()
    print(f"dual-precision certificate: max |val(50 digits) - val(100 digits)| = {agree:.3e}")
    print("SUMMARY REPAIR2 (per-row band maxima of m^2|E_1| over 151 <= m <= m_1-1):")
    all_ok = True
    for (y0, m1, c2), bm in zip(ROWS, band_max):
        v, m, k = bm
        ok = v <= c2
        all_ok = all_ok and ok
        print(f"  y0 = {float(y0):>3g}, band m = 151..{m1 - 1}: "
              f"max m^2|E_1| = {+v.quantize(Decimal('1e-6'))} at m = {m}, k = {k}  "
              f"<= C_2 = {c2} : {'PASS' if ok else 'FAIL'}")
    v3 = band_max[-1][0]
    print(f"  [info] y0 = 3 band max {+v3.quantize(Decimal('1e-6'))} vs the m>=2000 row's "
          f"C_2 = 475: {'below' if v3 <= INFO_C2_Y3 else 'ABOVE'} "
          f"(that row is only claimed for m >= 2000; 230 <= m <= 1999 is covered "
          f"by the proved (y0=3, m1=230) constant 3940)")
    print(f"FINAL VERDICT REPAIR2: "
          f"{'ALL PASS' if n_fail == 0 and all_ok else f'{n_fail} FAIL cell(s)'}")


if __name__ == "__main__":
    main()
