#!/usr/bin/env python3
# REFEREE (numerics, wave4_sliver): independent verification of Lemma SLV.1
# and the block-[C] diagnostics of sliver_sizing.py, with DIFFERENT machinery:
#   * mpmath dps-60 "true" values (display, not proof-bearing);
#   * an independent exact-Fraction certificate re-implementation using
#     different Taylor depths (N = 320), different sqrt bracketing (isqrt on
#     scaled integers, 14 digits), and a different remainder cap for exp_ub
#     (ratio bound with N+1 only);
#   * a single-crossing scan (no earlier dip below the slot, none after);
#   * adversarial off-grid probes: w -> 4+ edge, w = 4.51, m = 401, and the
#     m = 449/450/451/452 boundary.
# Entry form under audit (composite SS5.3 SL4' display, cap m^3/w^2):
#     far'(m, w) = sqrt(2pi) * m^{11/2} * e^{-0.0741 m} / w^3 .
from fractions import Fraction as F
import math

from mpmath import mp, mpf, sqrt as msqrt, exp as mexp, pi as mpi
mp.dps = 60

SLOT = F(1, 20)
Q = F(741, 10000)

# ---------------- true values (mpmath dps 60) ----------------
def far_true(m, w=4):
    return msqrt(2 * mpi) * mpf(m) ** mpf('5.5') * mexp(-mpf('0.0741') * m) / mpf(w) ** 3

print("[T] mpmath dps-60 true values of far'(m, w)")
for m, w in [(449, 4), (450, 4), (451, 4), (452, 4), (496, 4), (555, 4),
             (561, 4), (401, 4), (401, 4.51), (451, 4.51), (450, 4.0000001)]:
    v = far_true(m, w)
    print(f"  far'({m}, {w}) = {mp.nstr(v, 12)}   vs slot 0.05 -> "
          f"{'UNDER' if v <= mpf('0.05') else 'OVER'}  (slot/value = {mp.nstr(mpf('0.05')/v, 8)})")

# draft's quoted floats to verify: 2.859e-03 (m=496), 4.556e-05 (m=561),
# safety 17.5x / 1097.6x; far'(451,4) ~ 4.755e-02, margin factor 1.0515 (vs UB)
for m, quoted in [(451, '4.755e-02'), (496, '2.859e-03'), (561, '4.556e-05')]:
    v = far_true(m, 4)
    print(f"  quoted {quoted} at m={m}: true {mp.nstr(v, 4)}; safety {mp.nstr(mpf('0.05')/v, 5)}x")

# ---------------- independent exact certificate ----------------
print("\n[E] independent exact-Fraction certificate (different depths/brackets)")

def exp_lb2(x, N=320):
    x = F(x); s = F(1); t = F(1)
    for n in range(1, N + 1):
        t *= x / n
        s += t
    return s  # <= e^x

def exp_ub2(x, N=320):
    # partial sum + tail: sum_{n>N} x^n/n! <= t_N * sum_{k>=1} (x/(N+1))^k
    x = F(x); assert 0 <= x < N + 1
    s = F(1); t = F(1)
    for n in range(1, N + 1):
        t *= x / n
        s += t
    q = x / (N + 1)
    return s + t * q / (1 - q)  # >= e^x  (coarser tail than the draft's; still valid)

def sqrt_ub2(x, digits=14):
    num = F(x) * 10 ** (2 * digits)
    r = math.isqrt(int(num))
    while F(r, 10 ** digits) ** 2 < F(x):
        r += 1
    return F(r, 10 ** digits)

def sqrt_lb2(x, digits=14):
    num = F(x) * 10 ** (2 * digits)
    r = math.isqrt(int(num)) + 1
    while F(r, 10 ** digits) ** 2 > F(x):
        r -= 1
    return F(r, 10 ** digits)

# independent 2pi brackets (12 digits): 6.283185307179 <= 2pi <= 6.283185307180
TP_LB = F(6283185307179, 10 ** 12)
TP_UB = F(6283185307180, 10 ** 12)
# sanity: mpmath check of the brackets
assert mpf(TP_LB.numerator) / mpf(TP_LB.denominator) <= 2 * mpi <= mpf(TP_UB.numerator) / mpf(TP_UB.denominator)

def far_ub2(m):
    m = F(m)
    return sqrt_ub2(TP_UB) * m ** 5 * sqrt_ub2(m) / 64 / exp_lb2(Q * m)

def far_lb2(m):
    m = F(m)
    return sqrt_lb2(TP_LB) * m ** 5 * sqrt_lb2(m) / 64 / exp_ub2(Q * m)

u451 = far_ub2(451)
l450 = far_lb2(450)
print(f"  far'(451,4) <= {float(u451):.8f}  (<= 0.05: {u451 <= SLOT}; margin factor {float(SLOT/u451):.4f})")
print(f"  far'(450,4) >= {float(l450):.8f}  (>  0.05: {l450 > SLOT})")
assert u451 <= SLOT and l450 > SLOT

# m-monotonicity, independent route: certify ratio(m)^2 < 1 at m = 451 via
# (452/451)^11 < e^{0.1482} using a DIFFERENT lower bound on e^x:
# Bernoulli (1 + x/n)^n <= e^x for n = 2^20.
n = 2 ** 20
bern = (1 + F(1482, 10000) / n) ** n
lhs = F(452, 451) ** 11
print(f"  (452/451)^11 = {float(lhs):.9f} < (1+0.1482/2^20)^(2^20) = {float(bern):.9f} <= e^0.1482 : {lhs < bern}")
assert lhs < bern
# algebraic step: ((m+1)/m)^11 is strictly decreasing in m (d/dm log = 11*(1/(m+1)-1/m) < 0)
print("  ((m+1)/m)^11 strictly decreasing in m: algebraic (log-derivative < 0) -> ratio < 1 for ALL m >= 451")

# ---------------- single-crossing scan ----------------
print("\n[S] single-crossing scan (floats for location; exact at the boundary)")
# m^{5.5} e^{-0.0741 m} is increasing for m < 5.5/0.0741 = 74.22.., decreasing after;
# so on m >= 401 far'(m,4) is strictly decreasing -> at most one crossing.
peak = 5.5 / 0.0741
under = [m for m in range(401, 461) if far_true(m, 4) <= mpf('0.05')]
print(f"  stationary point of m^5.5 e^-0.0741m at m = {peak:.2f} (< 401) -> strictly decreasing on [401, inf)")
print(f"  first integer m in [401, 460] with far'(m,4) <= 0.05: {min(under)} (expect 451)")
assert min(under) == 451
# no re-crossing later (monotone): check a sparse tail
tail_ok = all(far_true(m, 4) < mpf('0.05') for m in (600, 800, 1200, 2000, 5000))
print(f"  sparse tail m = 600..5000 all under slot: {tail_ok}")

# ---------------- block [C] cross-checks ----------------
print("\n[C-check] crude orphan floor and closure points")
qW = (2.025 - 1) / (2 * 2.025) * (math.log(2) - 1 / 2.025)
print(f"  qW(4.05) = {qW:.6f}  (draft prints 0.05045); m*qW at m=401: {401*qW:.2f} (orphan quote 20.23)")
def far_crude(m, w=4.0):
    return math.sqrt(2 * math.pi) * m ** 5.5 * math.exp(-qW * m) / w ** 3
first = next(m for m in range(401, 2000) if far_crude(m) <= 0.05)
print(f"  crude-floor closure (this cap, w=4): m = {first}  (draft: 712)")
# A3 floor at m = 401 (composite quote 29.71):
print(f"  0.0741*401 = {0.0741*401:.4f}  (composite quote 29.71)")

# arithmetic in the note
print("\n[N] note arithmetic: 536-450 =", 536-450, "; 560-450 =", 560-450,
      "; 0.05/0.047550 =", f"{0.05/0.047550:.4f}")
print("\nOVERALL: PASS (all assertions held)")
