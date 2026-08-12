#!/usr/bin/env python3
"""Referee (numerics, wp3-a2): OFF-GRID checks of Theorem P.5's inequality.

Draft NC-P1(c) verified  r(k)-1 >= (m-1)/(2k(m+k))  exactly on 8 <= m <= 200.
The proved thresholds cover m >= m_p(c) (30/83/300/1581 by clause), so at
c = 1 the band 200 < m < 1581 is neither grid-checked nor proved (the stitch
uses the c = 7/10 clause there, proved for m >= 300 — but 201..299 at
k in (0.7m, m) relies on... nothing in the draft except the harness to 400).
Checks here, all exact integer arithmetic in the verdict path:
 (a) row sanity: sum I_m(k) = m!, symmetry, small-m rows vs known Mahonian
     triangle (independent generator cross-check);
 (b) full exact check m = 201..400, all 2 <= k <= m-1 (extends the grid 2x);
     track global min ratio and min over the c=1 band k in (0.7m, m-1];
 (c) large-m closed-form probe at k = 2..4 (where Phi = 1 - x_1 - x_2 exactly,
     since g=5 > 4): exact-Fraction ratio at m = 10^3, 10^4, 10^5, 10^6 —
     does the observed global-min corner (k = 2) ever dip below 2, i.e. can
     the min ratio approach the P.5 constant from above or cross it?
"""
from fractions import Fraction as F
from math import factorial

def rows_upto(mmax):
    poly = [1]
    for m in range(1, mmax + 1):
        old = poly; new = [0] * (len(old) + m - 1); run = 0
        for k in range(len(new)):
            if k < len(old): run += old[k]
            if 0 <= k - m < len(old): run -= old[k - m]
            new[k] = run
        yield m, new
        poly = new

# ---------- (a) row sanity ----------
known5 = [1, 4, 9, 15, 20, 22, 20, 15, 9, 4, 1]   # m = 5 Mahonian row (A008302)
ok_a = True
for m, row in rows_upto(60):
    if m == 5 and row != known5:
        ok_a = False; print("  m=5 row mismatch!")
    if m in (20, 40, 60):
        if sum(row) != factorial(m): ok_a = False; print(f"  sum != {m}!")
        if row != row[::-1]: ok_a = False; print(f"  m={m} not symmetric")
print(f"(a) row sanity: {'PASS' if ok_a else 'FAIL'}")

# ---------- (b) m = 201..400 exact ----------
viol = 0
gmin = None
gmin_band = None   # k in (0.7 m, m-1]
for m, row in rows_upto(400):
    if m < 201:
        continue
    for k in range(2, m):
        a0, am, ap = row[k], row[k - 1], row[k + 1]
        lhs = (a0 * a0 - am * ap) * 2 * k * (m + k)
        rhs = (m - 1) * am * ap
        if lhs < rhs:
            viol += 1
            if viol < 5: print(f"  VIOLATION m={m} k={k}")
        ratio = lhs / rhs
        if gmin is None or ratio < gmin[0]: gmin = (ratio, m, k)
        if k > 0.7 * m and (gmin_band is None or ratio < gmin_band[0]):
            gmin_band = (ratio, m, k)
print(f"(b) m=201..400, all 2<=k<=m-1: violations = {viol}")
print(f"    global min ratio {gmin[0]:.6f} at (m,k)=({gmin[1]},{gmin[2]})")
print(f"    min over c=1 band k>0.7m: {gmin_band[0]:.6f} at (m,k)=({gmin_band[1]},{gmin_band[2]})")

# ---------- (c) large-m closed form at k = 2, 3 ----------
# For k <= 4: I(k) = T(k) - T(k-1) - T(k-2)  (pentagonal g = 1, 2 only), so
# r(k) is an exact rational in m; probe the k=2 corner (the observed argmin).
from math import comb
def I_small(m, k):
    def T(j): return comb(m - 1 + j, m - 1) if j >= 0 else 0
    return T(k) - T(k - 1) - T(k - 2)
print("(c) exact ratio (r-1)/[(m-1)/(2k(m+k))] at the k=2 corner, large m:")
for m in (10**3, 10**4, 10**5, 10**6):
    for k in (2, 3):
        a0, am, ap = I_small(m, k), I_small(m, k - 1), I_small(m, k + 1)
        num = a0 * a0 - am * ap
        ratio = F(num * 2 * k * (m + k), (m - 1) * am * ap)
        flag = "OK(>=1)" if ratio >= 1 else "**VIOLATION**"
        print(f"    m={m:>8} k={k}: ratio = {float(ratio):.8f}  {flag}")
