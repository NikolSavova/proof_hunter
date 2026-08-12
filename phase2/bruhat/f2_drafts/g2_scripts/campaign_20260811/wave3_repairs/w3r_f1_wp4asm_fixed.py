#!/usr/bin/env python3
"""w3r_f1_wp4asm_fixed.py — wave-3 repair F1 (referee_numerics_wp4 §4 item 1).

FIXED COPY of g2_scripts/campaign_20260811/wp4_assembly/wp4asm_chain.py
tables [1]/[2]/[3] + [1b]. The ONLY change is display direction: the
`total<=` column is CEIL-printed, the `margin` column FLOOR-printed, and
the per-row `T/c_A` and headline effective-C* CEIL-printed, all at 4
decimals (the original used nearest-rounding, which printed rows W2/W3/W7
of table [1] with `total<=` BELOW the exact certified total). Every
Fraction computation, comparison, and PASS/FAIL verdict is identical in
logic to the original — no certified quantity moves. Also prints the
5-digit floor of the W1 margin (knock-on text repair "0.8655" headline is
already safe: exact 0.8655270). The [4] ESTIMATES block of the original
is float-labeled, not proof-bearing, and unaffected by F1 — not copied.
"""
from fractions import Fraction as F
import math

def exp_lb(x, N=140):
    s = F(1); t = F(1)
    for n in range(1, N + 1):
        t *= F(x) / n
        s += t
    return s

def sqrt_ub(x, digits=8):
    num = F(x) * 10**(2 * digits)
    r = math.isqrt(int(num))
    while F(r, 10**digits)**2 < F(x):
        r += 1
    return F(r, 10**digits)

def sqrt_lbv(x, digits=8):
    num = F(x) * 10**(2 * digits)
    r = math.isqrt(int(num))
    while F(r, 10**digits)**2 > F(x):
        r -= 1
    return F(r, 10**digits)

def ceil_p(x, digits=4):
    return math.ceil(x * 10**digits) / 10**digits

def floor_p(x, digits=4):
    return math.floor(x * 10**digits) / 10**digits

BANDS = [
    ("W1 (4,5]",   F(28, 100), F(1),      F(8, 10),  F(3)),
    ("W2 (5,6]",   F(35, 100), F(12, 10), F(14, 10), F(3)),
    ("W3 (6,8]",   F(42, 100), F(15, 10), F(26, 10), F(3)),
    ("W4 (8,10]",  F(52, 100), F(17, 10), F(35, 10), F(3)),
    ("W5 (10,20]", F(60, 100), F(2),      F(52, 10), F(3)),
    ("W6b (20,40]",F(70, 100), F(21, 10), F(6),      F(3)),
    ("W7 (40,inf)",F(80, 100), F(22, 10), F(66, 10), F(8)),
]
MID = F(3192, 1000)
CRO = F(287, 100)
CROE = F(556, 10000)

def r5_ub(C5, A0):
    target = (F(32, 5) * C5)**2
    val = (F(32, 5) * C5) / sqrt_lbv(A0)
    r = F(math.ceil(val * 10**4), 10**4)
    assert r**2 * A0 >= target
    return r

def table(mfloor, budgetC, i2u_mode, far_val, tag):
    print(f"\n[{tag}] ledger recompute (F1-FIXED ceil/floor display), m-floor = {mfloor}, "
          f"budget C* = {budgetC}, I2u = {i2u_mode}, far slot = {float(far_val):.3g}")
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
        else:
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
              f"{float(far):8.3g} {ceil_p(tot):8.4f} {float(budget):7.2f} {floor_p(budget-tot):8.4f} "
              f"{ceil_p(eff):7.4f} {'PASS' if ok else 'FAIL'}")
        if name.startswith("W1"):
            print(f"   (W1 margin, 5-digit FLOOR: {floor_p(budget-tot, 5):.5f}; exact {budget-tot} = {float(budget-tot):.7f})")
    print(f"  all rows PASS: {allpass};  effective C* = max_W T(W)/c_A(W) <= {ceil_p(worst):.4f} "
          f"(exact {worst.numerator}/{worst.denominator})  vs budget {budgetC}")
    return worst

c1 = table(401, 20, "0.2", F(1, 100), "1: harmonized architected slots (3.192/0.2/0.01), m>=401 vs C*=20")
c2 = table(401, 20, "P2", F(13, 10**8), "2: sharper SL3 slots (3.192/P2-band/1.3e-7), m>=401 vs C*=20")
c3 = table(1581, 136, "0.2", F(1, 100), "3: m>=1581 worst case vs relaxed C*=136")
print(f"\n[R2 repair check] variant [3] exact effective C* = {c3.numerator}/{c3.denominator}"
      f" ; == 201619/20000: {c3 == F(201619, 20000)} ; CEIL 3-decimal display = {math.ceil(c3*1000)/1000}"
      f"  (composite §7 must print 10.081, not 10.08)")

A0 = F(28, 100) * 401
i_319 = F(319, 100) * sqrt_ub(A0) / exp_lb(A0 / 32)
i_3192 = MID * sqrt_ub(A0) / exp_lb(A0 / 32)
print(f"\n[1b] D1 impact at W1: I1u(3.19) <= {ceil_p(i_319, 6):.6f} -> I1u(3.192) <= {ceil_p(i_3192, 6):.6f}; "
      f"delta = {float(i_3192 - i_319):.6f}  (absorbed: W1 margin ~0.8655)")
