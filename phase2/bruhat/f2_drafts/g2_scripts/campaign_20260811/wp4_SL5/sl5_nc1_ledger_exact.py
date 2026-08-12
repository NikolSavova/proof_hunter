#!/usr/bin/env python3
"""NC-SL5-1: exact-rational certification of the SL5 ledger table and side facts.

All proof-bearing arithmetic is in fractions.Fraction (exact). Transcendental
bounds are one-sided by construction:
  * e^x  >= P_N(x) := sum_{n=0}^N x^n/n!   (x >= 0, positive terms)  =>
    e^{-x} <= 1/P_N(x)   -- a certified UPPER bound for any N;
  * sqrt(a) <= s  certified by  s^2 >= a  (exact Fraction comparison);
  * sqrt(a) >= s  certified by  s^2 <= a.
Sections:
  [1] the 7 ledger rows at the worst point A = c_A*401 (Theorem SL5.2 table):
      each entry is replaced by a certified rational UPPER bound, the total is
      compared with 20*c_A in exact rationals.
  [2] far-entry certificate (Lemma SL5.0 + SL5.1(iii)): 0.36*m^{3/2}e^{-0.0373m}
      <= 1/100 at m=401 (exact), and the ratio test (1+1/m)^3 <= (402/401)^3
      < 1 + 746/10000 <= e^{2*0.0373} (exact) => decreasing for m >= 401.
  [3] SL2(iii) chain floor: s2 >= (7/25)*401/(89/100)^2 >= 141 > 79 (exact).
  [4] P.8-consistency: log(17/7) <= 0.8874 <= 0.89 and log 2 <= 0.6932 <= 0.89,
      certified via  e^{0.8874} >= 17/7,  e^{0.6932} >= 2  (partial sums).
  [5] I1u-monotonicity domain check: A_min = c_A*401 > 32 for every band, and
      c_A <= 1 (so the band [c_A*m, m] for A is non-empty), exact.
"""
from fractions import Fraction as F
from math import isqrt

def exp_lower(x: F, N: int = 120) -> F:
    """Partial Taylor sum P_N(x) <= e^x for x >= 0 (exact Fraction)."""
    assert x >= 0
    s = F(1)
    term = F(1)
    for n in range(1, N + 1):
        term *= x / n
        s += term
    return s

def sqrt_upper(a: F, digits: int = 4) -> F:
    """Smallest n/10^digits with (n/10^digits)^2 >= a (certified upper bound)."""
    d = 10 ** digits
    num = a.numerator * d * d
    den = a.denominator
    n = isqrt(num // den)
    while F(n * n) < F(num, den):
        n += 1
    assert F(n, d) ** 2 >= a
    return F(n, d)

m0 = 401
# band name, w-range, c_A, R31*, R42*, C5   (SL1(i)/SL2(ii)/SL1(ii) constants)
bands = [
    ("(4,5]",   F(7, 25),  F(1),      F(4, 5),  3),
    ("(5,6]",   F(7, 20),  F(6, 5),   F(7, 5),  3),
    ("(6,8]",   F(21, 50), F(3, 2),   F(13, 5), 3),
    ("(8,10]",  F(13, 25), F(17, 10), F(7, 2),  3),
    ("(10,20]", F(3, 5),   F(2),      F(26, 5), 3),
    ("(20,40]", F(7, 10),  F(21, 10), F(6),     3),
    ("(40,inf)", F(4, 5),  F(11, 5),  F(33, 5), 8),
]
I2u = F(1, 5)     # SL3(ii) W.6 piece
SLOP = F(1)       # SL4 assembly slop S_alg
FAR = F(1, 100)   # certified in [2] below (Lemma SL5.0 route)

print("[1] Ledger rows at A = c_A*401 (all entries certified rational UPPER bounds; exact comparison to 20*c_A)")
print(f"{'band':9s} {'c_A':>5s} {'A=cA*401':>9s} {'k4/2':>6s} {'0.3R31^2':>8s} "
      f"{'R5<=':>7s} {'I1u<=':>7s} {'I2u':>4s} {'slop':>4s} {'far<=':>5s} "
      f"{'total<=':>8s} {'20c_A':>6s} {'margin>=':>8s}  verdict")
all_pass = True
for name, cA, R31, R42, C5 in bands:
    A = cA * m0
    # R5 = 6.4*C5/sqrt(A):  certified ub r with r^2 * A >= (32*C5/5)^2
    R5ub = sqrt_upper((F(32, 5) * C5) ** 2 / A)
    # I1u = 3.19*sqrt(A)*e^{-A/32} <= 3.19 * sqrt_upper(A) / P_N(A/32)
    sA = sqrt_upper(A)
    I1ub = F(319, 100) * sA / exp_lower(A / 32)
    tot = R42 / 2 + F(3, 10) * R31 ** 2 + R5ub + I1ub + I2u + SLOP + FAR
    bud = 20 * cA
    ok = tot <= bud
    all_pass &= ok
    print(f"{name:9s} {float(cA):5.2f} {float(A):9.2f} {float(R42/2):6.3f} "
          f"{float(F(3,10)*R31**2):8.3f} {float(R5ub):7.4f} {float(I1ub):7.4f} "
          f"{float(I2u):4.1f} {float(SLOP):4.1f} {float(FAR):5.2f} "
          f"{float(tot):8.4f} {float(bud):6.1f} {float(bud-tot):8.4f}  "
          f"{'PASS' if ok else 'FAIL'}")
print(f"all 7 rows PASS (exact Fraction comparison): {all_pass}")

print("\n[2] Far entry, Lemma SL5.0 route (A <= m):  far <= 0.36*m^{3/2}*e^{-0.0373 m}")
xf = F(373, 10000) * m0                       # 0.0373*401 = 14.9573 exactly
sf = sqrt_upper(F(m0 ** 3))                   # sqrt(401^3) <= sf
far401 = F(9, 25) * sf / exp_lower(xf)
print(f"  0.0373*401 = {xf} = {float(xf)} ;  e^-x <= 1/P_120(x) = {float(1/exp_lower(xf)):.4e}")
print(f"  far(401) <= (9/25)*{float(sf):.2f}*e^-14.9573 <= {float(far401):.6e}  <= 1/100 : {far401 <= F(1,100)}")
lhs = F(402, 401) ** 3
rhs = F(10746, 10000)                          # 1 + 2*0.0373 <= e^{2*0.0373}
print(f"  ratio test: (402/401)^3 = {float(lhs):.6f} < 1 + 746/10000 = {float(rhs):.4f} : {lhs < rhs}")
print(f"  => (F(m+1)/F(m))^2 = (1+1/m)^3 e^(-0.0746) <= (402/401)^3/(1+0.0746) < 1 for m >= 401 (exact),")
print(f"     so 0.36 m^1.5 e^(-0.0373 m) decreases on m >= 401; value at 401 above. far <= 0.01 certified.")

print("\n[3] SL2(iii) chain floor: s2 >= c_A*m/lam^2 >= (7/25)*401/(89/100)^2")
floor = (F(7, 25) * m0) / (F(89, 100) ** 2)
print(f"  = {floor} = {float(floor):.4f} ;  >= 141: {floor >= 141} ;  > 126: {floor > 126} ;  > 79: {floor > 79}")

print("\n[4] P.8-consistency certificates (partial sums, N=60)")
for tag, xr, target in [("e^0.8874 >= 17/7 (i.e. log(17/7) <= 0.8874)", F(8874, 10000), F(17, 7)),
                        ("e^0.89   >= 17/7 (i.e. log(17/7) <= 0.89)  ", F(89, 100), F(17, 7)),
                        ("e^0.6932 >= 2    (i.e. log 2     <= 0.6932)", F(6932, 10000), F(2))]:
    lo = exp_lower(xr, 60)
    print(f"  {tag}:  P_60 = {float(lo):.7f} >= {float(target):.7f} : {lo >= target}")

print("\n[5] Domain checks (exact): A_min = c_A*401 > 32 and c_A <= 1, every band")
print("  ", all(cA * m0 > 32 and cA <= 1 for _, cA, _, _, _ in bands))
