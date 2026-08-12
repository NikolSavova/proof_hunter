#!/usr/bin/env python3
"""Referee (numerics, wp3-a2): exact verification of the Theorem S / NC-P4
arithmetic and of the unscripted side-claims in the stitching sections.

 (1) B_m exact (Fraction): is B_m <= 1.08/m on m >= 100 (used in R3 note 2 and
     in NC-P4's '1.08/m' line)?  Where does B_m*m peak?
 (2) The R3 w^2-bracket  6.85E(4)(1 - 17 B_m - C/m^2) - B_m  with exact B_m,
     E4 = 0.00248992 (verified lower bound), C = 10.71: true crossover m
     (draft claims 'm >= ~68 with it'; NC-P4 prints only the 63.3 proxy), and
     its value at m = 401 vs the draft's '0.01628 - 0.00270'.
 (3) R2 budget with SAFE rho: rho4_safe = 1 - 6.85*16*E4 rounded UP at 6 d.p.;
     eps* = 1 - 1.02*rho4; check 20/79.5 <= eps* and the conclusion >= 1.02.
     Floors: v(7/10)*401, v(1)*1581 exact; C* caps 20 / 136 reproduced.
 (4) Tilt caps as exact inequalities (Decimal ln, 40 digits): log(3) <= 1.0987,
     log(17/7) <= 0.8874, log(2) <= 0.6932; and >= the draft's NC-P3a floats.
 (5) R1 margins exact: (m-1)^2 (2m+5) / (144 c(1+c) m) at (401, 7/10) and
     (1581, 1) — are '1879' and '17364' safe (i.e. rounded DOWN)?
 (6) legacy rows: (24*2000)^2 = 2.304e9; 6*2000/(1*2) = 6000; ratio 3.84e5.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec = 40

def S4(m): return m * (m + 1) * (2 * m + 1) * (3 * m * m + 3 * m - 1) // 30
def lam_var(m): return F(m * (m - 1) * (2 * m + 5), 72)
def B(m): return F(S4(m) - m, 1) / (240 * lam_var(m) ** 2)

# ---------- (1) ----------
peak = None
bad1 = []
for m in list(range(30, 501)) + [1000, 1581, 10**4, 10**5]:
    Bm = B(m)
    v = Bm * m
    if peak is None or v > peak[0]: peak = (v, m)
    if m >= 100 and v > F(108, 100): bad1.append(m)
print(f"(1) max of B_m*m over tested m: {float(peak[0]):.6f} at m={peak[1]}"
      f"  (limit 1296/1200 = 1.08)")
print(f"    B_m <= 1.08/m for m >= 100: {'PASS' if not bad1 else f'FAIL at {bad1[:5]}'}")
print(f"    B_401 = {float(B(401)):.8f} (draft: 0.00270);  B_401*401 = {float(B(401)*401):.6f}")

# ---------- (2) ----------
E4 = F(248992, 10**8)          # verified lower bound of E(4)
C = F(1071, 100)               # 5.30 + 5.04 + 0.37
coef = F(685, 100) * E4        # 6.85 E(4)
cross = None
for m in range(30, 200):
    br = coef * (1 - 17 * B(m) - C / (m * m)) - B(m)
    if br > 0 and cross is None:
        # confirm it stays positive for the next 3000 m (B_m*m decreasing there)
        if all(coef * (1 - 17 * B(mm) - C / (mm * mm)) - B(mm) > 0 for mm in range(m, m + 300)):
            cross = m
            break
print(f"(2) true crossover of the R3 w^2-bracket: m = {cross}  (draft says '~68'; proxy 63.3)")
br401 = coef * (1 - 17 * B(401) - C / (401 * 401)) - B(401)
print(f"    bracket at m=401: {float(coef * (1 - 17*B(401) - C/401**2)):.5f} - {float(B(401)):.5f}"
      f" = {float(br401):.5f} > 0: {br401 > 0}  (draft: 0.01628 - 0.00270)")

# ---------- (3) ----------
rho4_exact = 1 - F(685, 100) * 16 * E4      # using the VERIFIED E4 lower bd
rho4_safe = F(727106, 10**6)                # 0.727106 >= rho4_exact (round UP)
assert rho4_safe >= rho4_exact
eps_star = 1 - F(102, 100) * rho4_safe
budget = F(20, 1) / (F(7, 10) * F(17, 10) / 6 * 401)   # 20 / (v(7/10)*401)
concl = (1 - budget) / rho4_safe
floor1 = F(7, 10) * F(17, 10) / 6 * 401
floor2 = F(1, 3) * 1581
print(f"(3) rho(4) exact-from-E4 = {float(rho4_exact):.8f}; draft quotes 0.7271 "
      f"(UNSAFE by {float(F(7271,10**4)-rho4_exact):.2e}); safe 0.727106 used here")
print(f"    eps* = 1 - 1.02*rho4_safe = {float(eps_star):.6f} (draft 0.2584)")
print(f"    floors: v(0.7)*401 = {float(floor1):.4f} (>=79: {floor1 >= 79}), "
      f"v(1)*1581 = {float(floor2):.1f} (=527: {floor2 == 527})")
print(f"    budget 20/floor = {float(budget):.6f} <= eps*: {budget <= eps_star}")
print(f"    R2 conclusion (1-budget)/rho4_safe = {float(concl):.6f} >= 1.02: {concl >= F(102,100)}")
cmax2 = eps_star * floor2
print(f"    C* cap on [1581,inf): floor(eps* * 527) = {int(cmax2)} (draft 136)")

# ---------- (4) ----------
ln = lambda x: Decimal(x).ln()
l3, l177, l2 = ln(3), (Decimal(17) / 7).ln(), ln(2)
print(f"(4) log3 = {str(l3)[:12]} <= 1.0987: {l3 <= Decimal('1.0987')};  "
      f"log(17/7) = {str(l177)[:12]} <= 0.8874: {l177 <= Decimal('0.8874')};  "
      f"log2 = {str(l2)[:12]} <= 0.6932: {l2 <= Decimal('0.6932')}")
print(f"    also 0.8873 <= log(17/7): {Decimal('0.8873') <= l177} (NC-P4's cap print), "
      f"0.6931 <= log2: {Decimal('0.6931') <= l2}")

# ---------- (5) ----------
for (m, cn, cd, drafted) in ((401, 7, 10, 1879), (1581, 1, 1, 17364)):
    c = F(cn, cd)
    val = F((m - 1) ** 2 * (2 * m + 5), 1) / (144 * c * (1 + c) * m)
    safe = "safe (drafted <= exact)" if drafted <= val else f"**OVERSTATED: exact {float(val):.2f} < {drafted}**"
    print(f"(5) R1 margin at (m={m}, c={float(c):.1f}): exact {float(val):.3f}; drafted {drafted}: {safe}")

# ---------- (6) ----------
old = (24 * 2000) ** 2
new = 6 * 2000 // 2
print(f"(6) OLD threshold (24*2000)^2 = {old:.3e} (draft 2.3e9); NEW 6*2000/(c(1+c))|c=1 = {new}"
      f"; ratio = {old/new:.2e} (draft 3.8e5)")
