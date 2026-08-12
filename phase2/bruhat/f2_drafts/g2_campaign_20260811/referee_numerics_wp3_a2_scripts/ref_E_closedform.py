#!/usr/bin/env python3
"""Referee (numerics, wp3-a2): independent high-precision check of the E(u)
"certified lower decimals" (draft Lemma P.7 table / NC-P3b).

The draft's NC-P3 computes E(u) = sum_{n>=1} 2(3 v_n^2 + u^2)/(v_n^2 (v_n^2+u^2)^2),
v_n = 2 pi n, as a 50000-term float partial sum and claims (a) the printed
8-decimal values are LOWER bounds, (b) truncation "< 2e-21".

Independent route, NO pi and NO series: the partial-fraction identity gives
   q(u) = 1/u^2 - e^u/(e^u - 1)^2   and   E(u) = (1/12 - q(u))/u^2
so E(u) = (1/12 - 1/u^2 + e^u/(e^u-1)^2)/u^2, computable to 50 digits with
Decimal.exp (correctly rounded). We check, for u = 1..8:
  1. E_true (50-digit Decimal) vs the draft script's float partial sum;
  2. whether the printed 8-decimal value is a valid LOWER bound of E_true;
  3. the TRUE truncation tail = E_true - partial_sum vs the claimed 2e-21;
  4. rounding direction of the derived "deficit >= 6.85 w0^2 E" and
     "rho(w0) <=" table entries in the draft (4-decimal prints).
"""
from decimal import Decimal, getcontext
from math import pi

getcontext().prec = 60

def E_true(u):
    """(1/12 - 1/u^2 + e^u/(e^u-1)^2)/u^2 in 60-digit Decimal."""
    ud = Decimal(u)
    eu = ud.exp()
    q = 1 / (ud * ud) - eu / ((eu - 1) ** 2)
    return (Decimal(1) / 12 - q) / (ud * ud)

def E_partial(u, N=50000):
    s = 0.0
    for n in range(1, N + 1):
        v2 = (2 * pi * n) ** 2
        s += 2 * (3 * v2 + u * u) / (v2 * (v2 + u * u) ** 2)
    return s

# printed 8-decimal values from the draft's NC-P3(b) output
printed = {1: "0.00400693", 2: "0.00358719", 3: "0.00304036", 4: "0.00248992",
           5: "0.00200652", 6: "0.00161241", 7: "0.00130283", 8: "0.00106319"}
# draft P.7 table: deficit >= and rho <= (4 decimals), w0 = 1..6
deficit_printed = {1: "0.0274", 2: "0.0983", 3: "0.1874", 4: "0.2729",
                   5: "0.3436", 6: "0.3976"}

print("u   E_true (20 digits)          partial sum (float)    printed<=E_true?  true tail")
for u in range(1, 9):
    Et = E_true(u)
    Ep = E_partial(u)
    pr = Decimal(printed[u])
    tail = Et - Decimal(repr(Ep))
    ok = "OK(lower bd)" if pr <= Et else "**NOT a lower bound**"
    print(f"{u}   {str(Et)[:22]}   {Ep:.17f}   {ok}   {float(tail):.3e}")

print()
print("derived 4-decimal table entries (draft P.7): deficit floor 6.85*w0^2*E_true")
for u in range(1, 7):
    Et = E_true(u)
    ded = Decimal("6.85") * u * u * Et
    rho = 1 - ded
    dp = Decimal(deficit_printed[u])
    okd = "safe (printed <= true floor)" if dp <= ded else f"**UNSAFE: printed {dp} > true floor {str(ded)[:10]}**"
    rho_pr = 1 - dp
    okr = "safe" if rho_pr >= rho else f"**UNSAFE: printed rho {rho_pr} < true bound {str(rho)[:10]}**"
    print(f"w0={u}: floor_true={str(ded)[:12]}  printed {dp}: {okd};  rho printed {rho_pr}: {okr}")

print()
print("claimed truncation '< 2e-21' vs script's own crude '3x first omitted term':")
N = 50000
v2 = (2 * pi * (N + 1)) ** 2
first = 2 * (3 * v2) / (v2 * v2 ** 2)  # ~ u-independent scale
# rigorous integral tail: sum_{n>N} ~ 6/(2pi)^4 * sum n^-4 <= 6/(2pi)^4 * (1/(3N^3))
tail_int = 6 / (2 * pi) ** 4 / (3 * N ** 3)
print(f"  first omitted term ~ {first:.3e}; script printed ~3x = {3*first:.3e}")
print(f"  rigorous tail bound (integral) ~ {tail_int:.3e}  <- true scale, ~1e-17 NOT 2e-21")
