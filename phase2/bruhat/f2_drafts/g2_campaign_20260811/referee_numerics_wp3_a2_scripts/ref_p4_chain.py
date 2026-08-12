#!/usr/bin/env python3
"""Referee (numerics, wp3-a2): exact-Fraction verification of the Lemma P.2/P.4
identities, the per-g bounds, the end-to-end P.4 conclusions, and an
INDEPENDENT recomputation of the C_d/C_A/C_P/m_p table (draft section 2).

All verdict-path arithmetic is exact int/Fraction.
Parts:
 (1) P.2(iii) shift-difference identities + Delta^2 closed forms (g=1, g=2,
     general g) against direct exact evaluation, all m in {30,45,101}, all
     k in 2..m-1, all pentagonal g <= k+1.
 (2) per-g bounds of the P.4 proof: |d_g+| <= g x+^g/(k+1), |d_g-| <= g x(k)^g/k,
     |D2 x_1| <= 2/m^2, |D2 x_2| <= 2/m^2, |D2 x_g| <= 6 g^2 x+^{g-2}/m^2 (g>=5).
 (3) end-to-end: |d_pm| <= C_d(c)/m, |A| <= C_A(c)/m^2, D_Phi >= -C_P(c)/m^2
     with exact binomial Phi, for (c, m) in {(1/4,30),(1/2,45),(7/10,60),(1,60)}
     and m=101 at c=7/10, all admissible k.
 (4) independent C_d/C_A/C_P/m_p: pentagonal sums to g <= 600 with EXACT
     Fraction tail bounds for BOTH sigma_1' and sigma_2^- (the draft script
     omitted the sigma_1' tail and used a float tail for sigma_2^-);
     check printed table values and their rounding directions.
"""
from fractions import Fraction as F
from math import comb

def pent_list(limit):
    out = []
    n = 1
    while n * (3 * n - 1) // 2 <= limit:
        for g in (n * (3 * n - 1) // 2, n * (3 * n + 1) // 2):
            if g <= limit:
                out.append((g, (-1) ** n))
        n += 1
    return sorted(out)

def xg(m, k, g):
    if g > k:
        return F(0)
    num = den = 1
    for i in range(g):
        num *= (k - i); den *= (m + k - 1 - i)
    return F(num, den)

# ---------- (1) identities ----------
bad = 0
for m in (30, 45, 101):
    for k in range(2, m):
        for g, _ in pent_list(k + 1):
            up = xg(m, k + 1, g) - xg(m, k, g)
            dn = xg(m, k, g) - xg(m, k - 1, g)
            # identity forms (draft P.2(iii)), valid for g <= k+1 resp g <= k
            if g <= k + 1:
                rhs = xg(m, k + 1, g) * F(g * (m - 1), (k + 1) * (m + k - g))
                if up != rhs: bad += 1; print(f"ID-up FAIL m={m} k={k} g={g}")
            if g <= k:
                rhs = xg(m, k, g) * F(g * (m - 1), k * (m + k - 1 - g))
                if dn != rhs: bad += 1; print(f"ID-dn FAIL m={m} k={k} g={g}")
            D2 = up - dn
            if g == 1:
                rhs = F(-2 * (m - 1), (m + k - 1) * (m + k) * (m + k - 2))
                if D2 != rhs: bad += 1; print(f"D2x1 FAIL m={m} k={k}")
            if g == 2 and k >= 2:
                rhs = F(2 * (m - 1) * (m - 2 * k),
                        (m + k) * (m + k - 1) * (m + k - 2) * (m + k - 3))
                if D2 != rhs: bad += 1; print(f"D2x2 FAIL m={m} k={k}")
            if 5 <= g <= k - 1:   # general formula needs k+1-g >= 1 and k-g >= 1
                rhs = xg(m, k, g) * F(g * (m - 1) * ((g - 1) * (m + k) - (g + 1) * k),
                                      (k + 1 - g) * k * (m + k) * (m + k - 1 - g))
                if D2 != rhs: bad += 1; print(f"D2gen FAIL m={m} k={k} g={g}")
print(f"(1) identity checks: {'PASS (0 mismatches)' if bad == 0 else f'FAIL ({bad})'}")

# ---------- (2) per-g bounds ----------
bad2 = 0
for m in (30, 45, 101):
    for k in range(2, m):
        xp = F(k + 1, m + k)
        xk = F(k, m + k - 1)
        for g, _ in pent_list(k + 1):
            up = xg(m, k + 1, g) - xg(m, k, g)
            dn = xg(m, k, g) - xg(m, k - 1, g)
            if not (0 <= up <= F(g) * xp ** g / (k + 1)): bad2 += 1; print(f"d+ bd FAIL {m},{k},{g}")
            if not (0 <= dn <= F(g) * xk ** g / k): bad2 += 1; print(f"d- bd FAIL {m},{k},{g}")
            D2 = abs(up - dn)
            if g in (1, 2):
                if D2 > F(2, m * m): bad2 += 1; print(f"D2 g={g} bd FAIL {m},{k}")
            elif g >= 5:
                if D2 > F(6 * g * g) * xp ** (g - 2) / (m * m):
                    bad2 += 1; print(f"D2 g={g} bd FAIL {m},{k}")
print(f"(2) per-g bound checks: {'PASS (0 violations)' if bad2 == 0 else f'FAIL ({bad2})'}")

# ---------- (4) independent constants (needed for (3)) ----------
GMAX = 600
def consts(xc):
    """Exact C_d, C_A upper bounds: pentagonal sums to GMAX plus EXACT tails
    over ALL integers g > GMAX (safe overcount)."""
    G = [g for g, _ in pent_list(GMAX)]
    s1 = sum(F(g) * xc ** g for g in G)
    s2 = sum(F(g * g) * xc ** (g - 2) for g in G if g >= 5)
    # exact tails, summing over ALL integers g >= GMAX+1:
    # sum_{g>N} g x^g = x^{N+1} [ (N+1) - N x ] / (1-x)^2
    N = GMAX
    t1 = xc ** (N + 1) * ((N + 1) - N * xc) / (1 - xc) ** 2
    # sum_{g>N} g^2 x^{g-2}: shift j = g-(N+1):
    # = x^{N-1} sum_j (N+1+j)^2 x^j = x^{N-1} [ (N+1)^2/(1-x) + 2(N+1)x/(1-x)^2 + x(1+x)/(1-x)^3 ]
    t2 = xc ** (N - 1) * ((N + 1) ** 2 / (1 - xc) + 2 * (N + 1) * xc / (1 - xc) ** 2
                          + xc * (1 + xc) / (1 - xc) ** 3)
    Cd = (s1 + t1) / xc
    CA = 4 + 6 * (s2 + t2)
    Phimin = 1 - xc - xc * xc
    CP = CA / Phimin + Cd * Cd / (Phimin * Phimin)
    return Cd, CA, Phimin, CP

table = {}
print("(4) independent constants (exact, tails included):")
print("    c     C_d           C_A           Phimin        C_P           m_p")
for cn, cd, xc in ((1, 4, F(F(1,4)*30+1, 30*F(5,4))), (1, 2, F(16, 45)),
                   (7, 10, F(22, 51)), (1, 1, F(30, 59))):
    c = F(cn, cd)
    Cd, CA, Phimin, CP = consts(xc)
    thr = 3 * CP * c * (1 + c) + 1
    mp = max(30, -(-thr.numerator // thr.denominator))
    table[c] = (Cd, CA, Phimin, CP, xc)
    print(f"  {float(c):5.2f}  {float(Cd):.9f}  {float(CA):.9f}  {float(Phimin):.9f}"
          f"  {float(CP):.9f}  {mp}")
# draft-printed values and rounding directions (upper-bound constants: printed
# must be >= true to be quotable as-is; Phimin lower bound: printed <= true)
drafted = {F(1,4): ("1.4675", "5.923", "0.7220", "12.34", 30),
           F(1,2): ("1.8053", "12.443", "0.5180", "36.17", 83),
           F(7,10): ("2.0823", "20.649", "0.3825", "83.61", 300),
           F(1,1): ("2.4804", "34.920", "0.2329", "263.23", 1581)}
for c, (dCd, dCA, dPh, dCP, dmp) in drafted.items():
    Cd, CA, Phimin, CP, xc = table[c]
    thr = 3 * CP * c * (1 + c) + 1
    mp = max(30, -(-thr.numerator // thr.denominator))
    msgs = []
    if F(dCd) < Cd: msgs.append(f"C_d printed {dCd} < true {float(Cd):.6f} (UNSAFE as an upper bd)")
    if F(dCA) < CA: msgs.append(f"C_A printed {dCA} < true {float(CA):.6f} (UNSAFE)")
    if F(dPh) > Phimin: msgs.append(f"Phimin printed {dPh} > true {float(Phimin):.6f} (UNSAFE as lower bd)")
    if F(dCP) < CP: msgs.append(f"C_P printed {dCP} < true {float(CP):.6f} (UNSAFE)")
    if mp != dmp: msgs.append(f"m_p mismatch: recomputed {mp} vs draft {dmp}")
    print(f"  c={float(c):4.2f}: " + ("all printed values safe-direction, m_p reproduced"
                                       if not msgs else "; ".join(msgs)))

# ---------- (3) end-to-end P.4 conclusions with exact binomial Phi ----------
def mahonian_row(m):
    poly = [1]
    for mm in range(1, m + 1):
        old = poly; new = [0] * (len(old) + mm - 1); run = 0
        for k in range(len(new)):
            if k < len(old): run += old[k]
            if 0 <= k - mm < len(old): run -= old[k - mm]
            new[k] = run
        poly = new
    return poly

from math import log
bad3 = 0
worst = {}
for c, mlist in ((F(1,4), [30, 101]), (F(1,2), [45, 101]), (F(7,10), [60, 101]), (F(1,1), [60, 101])):
    Cd, CA, Phimin, CP, xc = table[c]
    for m in mlist:
        row = mahonian_row(m)
        T = lambda j: comb(m - 1 + j, m - 1)
        kmax = min(int(c * m), m - 1)
        for k in range(2, kmax + 1):
            Pk = F(row[k], T(k)); Pm_ = F(row[k - 1], T(k - 1)); Pp = F(row[k + 1], T(k + 1))
            dplus = (1 - Pp) - (1 - Pk); dminus = (1 - Pm_) - (1 - Pk)
            A = dplus + dminus
            if abs(dplus) > Cd / m or abs(dminus) > Cd / m:
                bad3 += 1; print(f"P.4(i) FAIL c={c} m={m} k={k}")
            if abs(A) > CA / (m * m):
                bad3 += 1; print(f"P.4(ii) FAIL c={c} m={m} k={k}")
            D = 2 * log(Pk) - log(Pm_) - log(Pp)   # float, measurement of margin only
            if D < -float(CP) / (m * m) * (1 + 1e-12):
                bad3 += 1; print(f"P.4(iii) FAIL c={c} m={m} k={k}: D={D}")
            # exact P.4(iii) check without logs: need Phi(k-1)Phi(k+1) <= Phi(k)^2 e^{CP/m^2};
            # sufficient exact surrogate: Phi(k-1)Phi(k+1) <= Phi(k)^2 (1 + CP/m^2)  since e^x >= 1+x
            if Pm_ * Pp > Pk * Pk * (1 + CP / (m * m)):
                bad3 += 1; print(f"P.4(iii)-exact FAIL c={c} m={m} k={k}")
print(f"(3) end-to-end P.4 checks: {'PASS (0 violations)' if bad3 == 0 else f'FAIL ({bad3})'}")
