#!/usr/bin/env python3
"""REF-D: display-rounding audit (finding F1).  Reconstructs, in exact
Fractions, (1) the assembler's table [1] rows (wp4asm_chain.py conventions:
R5 = ceil@1e-4 of 6.4*C5/sqrt_lb(A0), I1u = ceil@1e-6 of 3.192*sqrt_ub(A0)/
P_140(A0/32)) and (2) SL5's NC-SL5-1 rows (R5ub = sqrt_upper@4dp of
(32C5/5)^2/A, I1ub = 3.19*sqrt_upper@4dp(A)/P_120(A/32)); then compares the
exact totals/margins/entries against the %.4f-printed columns of the archived
outputs.  UNSAFE = a column headed 'total<=' printing BELOW the exact value,
or 'margin>='/'margin' printing ABOVE it (nearest-rounding artifacts).
All PASS/FAIL verdicts in both scripts are exact-Fraction comparisons and are
unaffected; this audit concerns the printed digits only.
"""
from fractions import Fraction as F
import math
from math import isqrt

def exp_lb(x, N):
    s = F(1); t = F(1)
    for n in range(1, N + 1):
        t *= F(x) / n; s += t
    return s

def sqrt_ub8(x, digits=8):
    num = F(x) * 10 ** (2 * digits)
    r = isqrt(int(num))
    while F(r, 10 ** digits) ** 2 < F(x): r += 1
    return F(r, 10 ** digits)

def sqrt_lb8(x, digits=8):
    num = F(x) * 10 ** (2 * digits)
    r = isqrt(int(num))
    while F(r, 10 ** digits) ** 2 > F(x): r -= 1
    return F(r, 10 ** digits)

def sqrt_ub4(a):
    d = 10 ** 4; num = a.numerator * d * d; den = a.denominator
    n = isqrt(num // den)
    while F(n * n) < F(num, den): n += 1
    return F(n, d)

def P4(s): return F(int(s.replace('.', '')), 10 ** 4)

BANDS = [("W1", F(28,100), F(1), F(8,10), 3), ("W2", F(35,100), F(12,10), F(14,10), 3),
         ("W3", F(42,100), F(15,10), F(26,10), 3), ("W4", F(52,100), F(17,10), F(35,10), 3),
         ("W5", F(60,100), F(2), F(52,10), 3), ("W6b", F(70,100), F(21,10), F(6), 3),
         ("W7", F(80,100), F(22,10), F(66,10), 8)]

print("(1) assembler table [1] (printed cols from out_wp4asm_chain.txt):")
asm_tot = {"W1":'4.7345',"W2":'4.4335',"W3":'4.8790',"W4":'5.2249',"W5":'6.2748',"W6b":'6.6873',"W7":'8.8231'}
asm_mar = {"W1":'0.8655',"W2":'2.5665',"W3":'3.5210',"W4":'5.1751',"W5":'5.7252',"W6b":'7.3127',"W7":'7.1769'}
for name, cA, R31, R42, C5 in BANDS:
    A0 = cA * 401
    r5 = F(math.ceil((F(32,5) * C5 / sqrt_lb8(A0)) * 10**4), 10**4)
    i1 = F(math.ceil((F(3192,1000) * sqrt_ub8(A0) / exp_lb(A0/32, 140)) * 10**6), 10**6)
    tot = R42/2 + F(3,10)*R31**2 + r5 + i1 + F(1,5) + 1 + F(1,100)
    mar = 20*cA - tot
    print(f"  {name}: exact tot = {float(tot):.7f} printed {asm_tot[name]}"
          f"{' UNSAFE' if P4(asm_tot[name]) < tot else ' ok'};"
          f"  exact mar = {float(mar):.7f} printed {asm_mar[name]}"
          f"{' UNSAFE' if P4(asm_mar[name]) > mar else ' ok'}")

print("(2) SL5 NC-SL5-1 table (printed cols from out_sl5_nc1.txt):")
sl5 = {"W1":('4.7338','0.8662','1.0118'), "W2":('4.4333','2.5667','0.4706'),
       "W3":('4.8789','3.5211','0.2144'), "W4":('5.2248','5.1752','0.0681'),
       "W5":('6.2748','5.7252','0.0269'), "W6b":('6.6873','7.3127','0.0083'),
       "W7":('8.8231','7.1769','0.0025')}
for name, cA, R31, R42, C5 in BANDS:
    A = cA * 401
    R5ub = sqrt_ub4((F(32,5) * C5) ** 2 / A)
    I1ub = F(319,100) * sqrt_ub4(A) / exp_lb(A/32, 120)
    tot = R42/2 + F(3,10)*R31**2 + R5ub + I1ub + F(1,5) + 1 + F(1,100)
    mar = 20*cA - tot
    pt, pm, pi1 = sl5[name]
    print(f"  {name}: tot={float(tot):.7f} [{pt}{' UNSAFE' if P4(pt) < tot else ' ok'}] "
          f"mar={float(mar):.7f} [{pm}{' UNSAFE' if P4(pm) > mar else ' ok'}] "
          f"I1u={float(I1ub):.7f} [{pi1}{' UNSAFE' if P4(pi1) < I1ub else ' ok'}]")
print("note: worst printed-vs-exact gap in either table is < 5e-5; every")
print("PASS/FAIL and every budget comparison is exact-Fraction and unaffected.")
