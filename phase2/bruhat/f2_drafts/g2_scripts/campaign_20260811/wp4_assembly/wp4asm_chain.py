#!/usr/bin/env python3
# wp4 ASSEMBLY cross-check (wave 3 assembler).  All new numeric claims in
# wp4_draft_composite.md come from THIS file's printed output.
#
# [1] EXACT (Fraction end-to-end): the SL5 ledger table RECOMPUTED with the
#     constants SL3 actually delivered (mid 3.192, not the architected 3.19;
#     I2u slot 0.2 as delivered by SL3's three-slot form; far slot 0.01,
#     doubly covered by SL5.1(iii) and SL3's P3 <= 1.3e-7).  Rows vs 20*c_A;
#     effective C* = max_W T(W)/c_A(W).
# [2] EXACT: sharper variant using SL3's per-band P2 column (crossover
#     2.87 sqrt(A) e^{-0.0556A}) and far 1.3e-7.
# [3] EXACT: the m >= 1581 worst case (A0 = c_A*1581) vs relaxed budget 136.
# [4] ESTIMATES (mpmath, labeled, NOT proof-bearing): sizing of the orphaned
#     SL4 script's normalization finding — honest kernel-weighted numerator
#     transfer of the tail/R5 slots vs the architected T_u slots; the far
#     sliver with SL3's certified floor q(2,1) >= 0.0741 in place of the
#     orphan's cruder W.3d floor.
from fractions import Fraction as F
import math

# ---------- exact helpers (safe direction) ----------
def exp_lb(x, N=140):
    # partial sum P_N(x) <= e^x for rational x >= 0  (all terms positive)
    s = F(1); t = F(1)
    for n in range(1, N + 1):
        t *= F(x) / n
        s += t
    return s                       # e^{-x} <= 1/exp_lb(x)

def sqrt_ub(x, digits=8):
    # rational s with s^2 >= x (upper bound on sqrt(x)), ~1e-digits tight
    num = F(x) * 10**(2 * digits)
    r = math.isqrt(int(num))
    while F(r, 10**digits)**2 < F(x):
        r += 1
    return F(r, 10**digits)

BANDS = [
    # name, c_A, R31*, R42*, C5
    ("W1 (4,5]",   F(28, 100), F(1),      F(8, 10),  F(3)),
    ("W2 (5,6]",   F(35, 100), F(12, 10), F(14, 10), F(3)),
    ("W3 (6,8]",   F(42, 100), F(15, 10), F(26, 10), F(3)),
    ("W4 (8,10]",  F(52, 100), F(17, 10), F(35, 10), F(3)),
    ("W5 (10,20]", F(60, 100), F(2),      F(52, 10), F(3)),
    ("W6b (20,40]",F(70, 100), F(21, 10), F(6),      F(3)),
    ("W7 (40,inf)",F(80, 100), F(22, 10), F(66, 10), F(8)),
]
MID = F(3192, 1000)     # SL3-delivered mid constant (D1: 3.19 -> 3.192)
CRO = F(287, 100)       # SL3 P2 constant
CROE = F(556, 10000)    # SL3 P2 exponent coefficient

def r5_ub(C5, A0):
    # upper bound on 6.4*C5/sqrt(A0): least 4-decimal r with r^2*A0 >= (32C5/5)^2
    target = (F(32, 5) * C5)**2
    lo, hi = F(0), F(10)
    r = F(1)
    # simple search on 1e-4 grid via ceil of exact value
    val = (F(32, 5) * C5) / sqrt_lbv(A0)
    r = F(math.ceil(val * 10**4), 10**4)
    assert r**2 * A0 >= target
    return r

def sqrt_lbv(x, digits=8):
    # rational s with s^2 <= x (lower bound on sqrt(x))
    num = F(x) * 10**(2 * digits)
    r = math.isqrt(int(num))
    while F(r, 10**digits)**2 > F(x):
        r -= 1
    return F(r, 10**digits)

def table(mfloor, budgetC, i2u_mode, far_val, tag):
    print(f"\n[{tag}] ledger recompute, m-floor = {mfloor}, budget C* = {budgetC}, "
          f"I2u = {i2u_mode}, far slot = {float(far_val):.3g}  (exact Fractions, safe rounding)")
    print(" band          c_A    A0      k4/2   0.3R31^2  R5<=    I1u<=   I2u<=   slop  far<=    total<=   C*c_A   margin   T/c_A")
    worst = F(0); allpass = True
    for name, cA, R31, R42, C5 in BANDS:
        A0 = cA * mfloor
        k42 = R42 / 2
        k32 = F(3, 10) * R31**2
        r5 = r5_ub(C5, A0)
        i1 = MID * sqrt_ub(A0) / exp_lb(A0 / 32)
        i1 = F(math.ceil(i1 * 10**6), 10**6)
        if i2u_mode == "0.2":
            i2 = F(1, 5)
        else:  # SL3 per-band P2
            i2 = CRO * sqrt_ub(A0) / exp_lb(CROE * A0)
            i2 = F(math.ceil(i2 * 10**6), 10**6)
        slop = F(1)
        far = F(far_val)
        tot = k42 + k32 + r5 + i1 + i2 + slop + far
        budget = budgetC * cA
        ok = tot <= budget
        allpass = allpass and ok
        eff = tot / cA
        worst = max(worst, eff)
        print(f" {name:13s} {float(cA):.2f}  {float(A0):7.2f} {float(k42):6.3f}  {float(k32):6.3f}  "
              f"{float(r5):7.4f} {float(i1):8.6f} {float(i2):8.6f} {float(slop):4.1f} "
              f"{float(far):8.3g} {float(tot):8.4f} {float(budget):7.2f} {float(budget-tot):8.4f} "
              f"{float(eff):7.3f} {'PASS' if ok else 'FAIL'}")
    print(f"  all rows PASS: {allpass};  effective C* = max_W T(W)/c_A(W) = {float(worst):.4f} "
          f"(exact {worst.numerator}/{worst.denominator})  vs budget {budgetC}")
    return worst

# ---------- [1][2][3] ----------
c1 = table(401, 20, "0.2", F(1, 100), "1: harmonized architected slots (3.192/0.2/0.01), m>=401 vs C*=20")
c2 = table(401, 20, "P2", F(13, 10**8), "2: sharper SL3 slots (3.192/P2-band/1.3e-7), m>=401 vs C*=20")
c3 = table(1581, 136, "0.2", F(1, 100), "3: m>=1581 worst case vs relaxed C*=136")

# delta of the 3.19 -> 3.192 correction on the W1 I1u entry:
A0 = F(28, 100) * 401
i_319 = F(319, 100) * sqrt_ub(A0) / exp_lb(A0 / 32)
i_3192 = MID * sqrt_ub(A0) / exp_lb(A0 / 32)
print(f"\n[1b] D1 impact at W1: I1u(3.19) = {float(i_319):.6f} -> I1u(3.192) = {float(i_3192):.6f}; "
      f"delta = {float(i_3192 - i_319):.6f}  (absorbed: W1 margin ~0.865)")

# ---------- [4] ESTIMATES (floats/mpmath-free; labeled, NOT proof-bearing) ----------
print("\n[4] ESTIMATES (floats, labeled; sizing the orphaned wp4_SL4/sl4_nc1.py finding)")
SQ2PI = math.sqrt(2 * math.pi)

def honest_mid(gam, A):
    # orphaned-script entry_num_mid: kernel-weighted numerator mid-tail transfer
    return SQ2PI / math.pi * A**1.5 / (2 * gam) * math.exp(-gam * A / 4) * (1 + 2 / (gam * A))

A1 = 0.28 * 401
pm = 3.192 * math.sqrt(A1) * math.exp(-A1 / 32)
hm8 = honest_mid(1 / 8, A1)
hm42 = honest_mid(0.42, A1)
print(f"  honest mid entry, W1 (A={A1:.2f}): gamma=1/8 -> {hm8:.2f}  "
      f"(architected slot {pm:.4f}; ratio {hm8/pm:.1f}, ~A x)")
print(f"  honest mid entry, W1, gamma=0.42 -> {hm42:.4f}  (closes; SL3 PROVED gamma = 0.1317 only; "
      f"measured truth on mid range 0.3794-0.4923, NC-SL3-2)")

def honest_r5(C5, A):
    return 48 * SQ2PI / math.pi * C5 * math.e / math.sqrt(A)

print(f"  honest R5 numerator entry, W1, C5=3 (SL1 architected): {honest_r5(3, A1):.2f}  "
      f"(architected slot 6.4*3/sqrt(A) = {6.4*3/math.sqrt(A1):.2f}; ratio {honest_r5(3,A1)/(6.4*3/math.sqrt(A1)):.1f}); "
      f"C5*=0.05 -> {honest_r5(0.05, A1):.3f}")

# honest far entry with SL3's certified floor q(2,1) >= 0.0741 (vs orphan's cruder
# W.3d floor 0.0504 at w=4.05), A <= m (Lemma SL5.0/SL3.B), two s2-caps:
def honest_far(m, w, s2cap):
    return SQ2PI * m * s2cap**1.5 * math.exp(-0.0741 * m)

for m in (401, 420, 430, 440, 460, 500):
    w = 4.05
    s2_b0i = 1.05 * m**3 / 36          # B.0(i) cap (untilted; NOT in citable wp4 inventory)
    s2_sl50 = m**3 / w**2              # ~ m/(4 sinh^2(lam/2)) cap at small lam (SL5.0, citable)
    print(f"  honest far entry (exp 0.0741m), w=4.05, m={m}: with s2<=1.05m^3/36 -> "
          f"{honest_far(m, w, s2_b0i):.4f} ; with s2<=m^3/w^2 (SL5.0) -> {honest_far(m, w, s2_sl50):.4f}")
# orphan reproduction: crude exponent m*qW(4.05) = 20.23 at m=401
qW = (2.025 - 1) / (2 * 2.025) * (math.log(2) - 1 / 2.025)
print(f"  orphan far floor at w=4.05: qW = {qW:.5f}, m*qW = {401*qW:.2f} "
      f"(vs SL3 floor 0.0741*401 = {0.0741*401:.2f}); orphan far entry 1191 (archived out_sl4_nc1.txt)")
# sliver boundary with the SL3 floor and SL5.0 cap:
for tag, cap in (("B.0(i)", lambda m: 1.05 * m**3 / 36), ("SL5.0", lambda m: m**3 / 4.05**2)):
    lo = None
    for m in range(401, 800):
        if honest_far(m, 4.05, cap(m)) <= 0.05:
            lo = m; break
    print(f"  honest-far sliver (<=0.05) closes at m = {lo} with cap {tag} "
          f"(orphan, cruder floor: m=560-class)")
print("  (all of [4] is measurement/sizing of the UNREFEREED orphaned SL4 evidence, "
      "not a certified bound)")
