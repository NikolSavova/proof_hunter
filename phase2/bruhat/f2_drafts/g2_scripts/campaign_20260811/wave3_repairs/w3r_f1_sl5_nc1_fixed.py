#!/usr/bin/env python3
"""w3r_f1_sl5_nc1_fixed.py — wave-3 repair F1 (referee_numerics_wp4 §4 item 1).

FIXED COPY of g2_scripts/campaign_20260811/wp4_SL5/sl5_nc1_ledger_exact.py.
The ONLY change is display direction: columns headed `<=` are now
CEIL-printed and columns headed `>=` FLOOR-printed at the shown precision
(the original used %.4f nearest-rounding, which printed some certified
upper bounds BELOW their exact value: SL5 rows W1/W3/W4/W7). Every
Fraction computation, every comparison, and every PASS/FAIL verdict is
byte-identical in logic to the original — no certified quantity moves.
Also prints the 5-digit floor of the W1 margin (the knock-on text repair:
"0.8662" -> "0.86615").
"""
from fractions import Fraction as F
from math import isqrt, ceil, floor

def exp_lower(x: F, N: int = 120) -> F:
    assert x >= 0
    s = F(1)
    term = F(1)
    for n in range(1, N + 1):
        term *= x / n
        s += term
    return s

def sqrt_upper(a: F, digits: int = 4) -> F:
    d = 10 ** digits
    num = a.numerator * d * d
    den = a.denominator
    n = isqrt(num // den)
    while F(n * n) < F(num, den):
        n += 1
    assert F(n, d) ** 2 >= a
    return F(n, d)

def ceil_p(x: F, digits: int = 4) -> float:
    """CEIL-print for a certified upper bound (never prints below exact)."""
    return ceil(x * 10 ** digits) / 10 ** digits

def floor_p(x: F, digits: int = 4) -> float:
    """FLOOR-print for a certified lower bound (never prints above exact)."""
    return floor(x * 10 ** digits) / 10 ** digits

m0 = 401
bands = [
    ("(4,5]",   F(7, 25),  F(1),      F(4, 5),  3),
    ("(5,6]",   F(7, 20),  F(6, 5),   F(7, 5),  3),
    ("(6,8]",   F(21, 50), F(3, 2),   F(13, 5), 3),
    ("(8,10]",  F(13, 25), F(17, 10), F(7, 2),  3),
    ("(10,20]", F(3, 5),   F(2),      F(26, 5), 3),
    ("(20,40]", F(7, 10),  F(21, 10), F(6),     3),
    ("(40,inf)", F(4, 5),  F(11, 5),  F(33, 5), 8),
]
I2u = F(1, 5)
SLOP = F(1)
FAR = F(1, 100)

print("[1-FIXED] NC-SL5-1 ledger rows, ceil/floor display (arithmetic identical to sl5_nc1_ledger_exact.py [1])")
print(f"{'band':9s} {'c_A':>5s} {'A=cA*401':>9s} {'k4/2':>6s} {'0.3R31^2':>8s} "
      f"{'R5<=':>7s} {'I1u<=':>7s} {'I2u':>4s} {'slop':>4s} {'far<=':>5s} "
      f"{'total<=':>8s} {'20c_A':>6s} {'margin>=':>8s}  verdict")
all_pass = True
w1_margin = None
for name, cA, R31, R42, C5 in bands:
    A = cA * m0
    R5ub = sqrt_upper((F(32, 5) * C5) ** 2 / A)
    sA = sqrt_upper(A)
    I1ub = F(319, 100) * sA / exp_lower(A / 32)
    tot = R42 / 2 + F(3, 10) * R31 ** 2 + R5ub + I1ub + I2u + SLOP + FAR
    bud = 20 * cA
    ok = tot <= bud
    all_pass &= ok
    if name == "(4,5]":
        w1_margin = bud - tot
    print(f"{name:9s} {float(cA):5.2f} {float(A):9.2f} {float(R42/2):6.3f} "
          f"{float(F(3,10)*R31**2):8.3f} {float(R5ub):7.4f} {ceil_p(I1ub):7.4f} "
          f"{float(I2u):4.1f} {float(SLOP):4.1f} {float(FAR):5.2f} "
          f"{ceil_p(tot):8.4f} {float(bud):6.1f} {floor_p(bud-tot):8.4f}  "
          f"{'PASS' if ok else 'FAIL'}")
print(f"all 7 rows PASS (exact Fraction comparison): {all_pass}")
print(f"W1 margin, 5-digit FLOOR (text repair '0.8662' ->): {floor_p(w1_margin, 5):.5f}"
      f"  (exact value = {float(w1_margin):.7f}..., 7-digit floor {floor_p(w1_margin, 7):.7f})")
