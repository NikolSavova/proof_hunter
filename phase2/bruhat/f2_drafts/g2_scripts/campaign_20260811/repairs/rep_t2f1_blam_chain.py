"""rep_t2f1_blam_chain.py -- repairs_20260811, repair T2-F1 (the only repair
with mathematical content).

TARGET (referee_t2_numerics.md F1): Theorem T.9 Step 2's chain for
  B_lam = B_m (1 + theta * 0.35 w^2)
used the FALSE display "(1-delta)^{-2} <= 1 + 2.1 delta for delta <= 0.35"
(false for delta >= ~0.025).  This script certifies a VALID replacement chain,
restated for |w| <= 1 (the scope Theorem A's region-3 handoff actually needs,
w_0 <= 1), per the referee's repair option (a) + STATUS.md item 1:

  NEW LEMMA (T.9-Step2', |w| <= 1, m >= 30):
      |B_lam/B_m - 1| <= 0.362 w^2 .
  Chain, every constant named:
    (1) B_lam/B_m = ratio * R,  ratio := kappa_4(lam)/kappa_4(0),
        R := (lambda/s2)^2 = (1-delta)^{-2},  delta := 1 - s2/lambda in [0,1).
    (2) |ratio - 1| <= c_A w^2,  c_A := 600/2200 = 3/11
        [T.4' recentred: |kappa_4(lam)-kappa_4(0)| <= w^2 m^5/2200 on
         |w| <= pi, m >= 30; |kappa_4(0)| = S*_4/120 >= m^5/600 from the
         certified S*_4 >= m^5/5 (m >= 8)].
    (3) delta <= c_D w^2,  c_D := 0.0330
        [wp2-b Lemma W.1(i), PROVED all real w, m >= 30 -- see repair B5].
    (4) (1-d)^{-2} <= 1 + 2d + 3.5 d^2  for 0 <= d <= 0.033:
        identity (1-d)^{-2} - 1 - 2d = d^2 * phi(d),
        phi(d) := 3/(1-d) + d/(1-d)^2, phi increasing, phi(0.033) < 3.5.
    (5) => 1 <= R <= 1 + c_R w^2 on |w| <= 1, c_R := 2 c_D + 3.5 c_D^2 <= 0.0699.
    (6) upper: (1 + c_A w^2)(1 + c_R w^2) <= 1 + (c_A + c_R + c_A c_R) w^2
        <= 1 + 0.362 w^2  (w^2 <= 1);  lower: >= 1 - c_A w^2.  QED
  Downstream: T2's combination "0.35 + 0.09 < 0.5" becomes
  "0.362 + 0.09 = 0.452 < 0.5" -- the c_w = 1/2 sub-claim still closes on
  |w| <= 1.  For 1 < |w| <= 4 the envelope is superseded by wp2-b Prop W.6
  (grid-certified c_w(1) = 0.407, c_w(2) = 0.466, c_w(4) = 1), the campaign's
  authoritative envelope.

Certifications below (exact Fraction arithmetic for every rational step;
truth measurement in BOTH float (fixed lib) and mpmath dps=50 -- house
dual-precision rule):
  (a) the old display is FALSE at delta = 0.033 (reproduces the referee);
  (b) step (4) at the endpoint in exact rationals + monotonicity of phi;
  (c) the assembled constant 0.362 in exact rationals;
  (d) measured truth max |B_lam/B_m - 1|/w^2 over m in {30, 60, 120},
      w-grid (0, pi] -- referee's value 0.1134 reproduced; the |w| <= 1
      restriction of the max, and margin vs 0.362.

Run: python3 rep_t2f1_blam_chain.py
"""
import math
import os
import sys
from fractions import Fraction

import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wp2b_lib_fixed as lib

mp.mp.dps = 50


# ---------- (a) the broken display is false ----------
def check_a():
    print("(a) OLD display '(1-d)^{-2} <= 1 + 2.1 d' (claimed for d <= 0.35):")
    for d in (Fraction(33, 1000), Fraction(1, 10), Fraction(35, 100)):
        lhs = 1 / (1 - d) ** 2
        rhs = 1 + Fraction(21, 10) * d
        print(f"    d = {float(d):5.3f}: (1-d)^-2 = {float(lhs):.5f}  vs  "
              f"1+2.1d = {float(rhs):.5f}   holds: {lhs <= rhs}")
    print("    -> FALSE already at d = 0.033 (the value (T.4)/W.1 actually "
          "delivers at w = 1): the old chain is broken, as the referee found.")


# ---------- (b) the corrected inequality, exact ----------
def check_b():
    d0 = Fraction(33, 1000)
    # identity: (1-d)^{-2} - 1 - 2d == d^2 * (3/(1-d) + d/(1-d)^2)  (exact)
    for d in (Fraction(1, 97), d0, Fraction(1, 5)):
        lhs = 1 / (1 - d) ** 2 - 1 - 2 * d
        rhs = d * d * (3 / (1 - d) + d / (1 - d) ** 2)
        assert lhs == rhs, d
    phi0 = 3 / (1 - d0) + d0 / (1 - d0) ** 2
    # phi(d) = 3/(1-d) + d/(1-d)^2: both summands are increasing on [0,1)
    # (1/(1-d) increasing; d/(1-d)^2 = sum_{k>=1} k d^k has positive coeffs),
    # so phi <= phi(d0) on [0, d0].
    print("(b) corrected inequality (1-d)^{-2} <= 1 + 2d + 3.5 d^2 on [0, 0.033]:")
    print(f"    identity (1-d)^-2 - 1 - 2d == d^2 phi(d) verified exactly (3 pts)")
    print(f"    phi(0.033) = {float(phi0):.6f} = "
          f"{phi0} <= 3.5: {phi0 <= Fraction(7, 2)}")
    print("    phi increasing on [0,1) (both summands have positive power-series"
          " coefficients) -> inequality PROVED on [0, 0.033].")
    return phi0 <= Fraction(7, 2)


# ---------- (c) the assembled constant, exact ----------
def check_c():
    cA = Fraction(600, 2200)            # = 3/11, from T.4' + S*_4 >= m^5/5
    cD = Fraction(330, 10000)           # 0.0330, wp2-b Lemma W.1(i)
    cR = 2 * cD + Fraction(7, 2) * cD * cD
    total = cA + cR + cA * cR
    print("(c) assembled constants (exact rationals):")
    print(f"    c_A = 600/2200 = {float(cA):.6f}")
    print(f"    c_R = 2 c_D + 3.5 c_D^2 = {float(cR):.7f} <= 0.0699: "
          f"{cR <= Fraction(699, 10000)}")
    print(f"    c_A + c_R + c_A c_R = {float(total):.6f} <= 0.362: "
          f"{total <= Fraction(362, 1000)}")
    print(f"    downstream: 0.362 + 0.09 = 0.452 < 0.5 (c_w = 1/2 still closes "
          f"on |w| <= 1): {Fraction(362,1000)+Fraction(9,100) < Fraction(1,2)}")
    return total <= Fraction(362, 1000)


# ---------- (d) truth measurement, dual precision ----------
def g1_mp(u):
    if abs(u) < mp.mpf("1e-3"):
        return (mp.mpf(-1) / 12 + u * u / 240 - u ** 4 / 6048
                + u ** 6 / 172800)
    e = mp.e ** u
    return -1 / (u * u) + e / (e - 1) ** 2


def g3_mp(u):
    if abs(u) < mp.mpf("1e-3"):
        return (mp.mpf(1) / 120 - u * u / 504 + u ** 4 / 5760
                - u ** 6 / 95040)
    e = mp.e ** u
    return -6 / u ** 4 + e * (e * e + 4 * e + 1) / (e - 1) ** 4


def s2_k4_mp(m, lam):
    s2 = k4 = mp.mpf(0)
    g1l, g3l = g1_mp(mp.mpf(lam)), g3_mp(mp.mpf(lam))
    for j in range(1, m + 1):
        u = mp.mpf(lam) * j
        s2 += g1l - j * j * g1_mp(u)
        k4 += g3l - j ** 4 * g3_mp(u)
    return s2, k4


def check_d():
    print("(d) measured truth |B_lam/B_m - 1|/w^2 (float fixed-lib vs mpmath "
          "dps=50):")
    best_all = best_w1 = (0.0, None)
    for m in (30, 60, 120):
        lamvar = float(lib.lam_var(m))
        k40 = None
        for iw in range(1, 158):        # w = 0.02 .. 3.14
            w = 0.02 * iw
            lam = w / m
            # float route (fixed lib)
            _, s2f, _, k4f, _, _ = lib.cumulants(m, lam)
            # mp route
            s2m, k4m = s2_k4_mp(m, lam)
            if k40 is None:
                s20m, k40 = s2_k4_mp(m, 1e-12)  # ~untilted
            # B_lam/B_m = [k4(lam)/k4(0)] * (lambda/s2)^2
            _, s20f, _, k40f, _, _ = lib.cumulants(m, 1e-12)
            rf = (k4f / k40f) * (lamvar / s2f) ** 2
            rm = (k4m / k40) * (mp.mpf(lamvar) / s2m) ** 2
            dev = abs(float(rm) - rf)
            assert dev < 2e-5, (m, w, dev)     # dual-precision agreement
            val = abs(float(rm) - 1.0) / (w * w)
            if val > best_all[0]:
                best_all = (val, (m, w))
            if w <= 1.0 and val > best_w1[0]:
                best_w1 = (val, (m, w))
    print(f"    max over w in (0, pi], m in {{30,60,120}}: {best_all[0]:.4f} "
          f"at (m, w) = {best_all[1]}   [referee measured 0.1134]")
    print(f"    max over |w| <= 1:                        {best_w1[0]:.4f} "
          f"at (m, w) = {best_w1[1]}")
    print(f"    proved new bound on |w| <= 1: 0.362  -> margin factor "
          f"{0.362 / best_w1[0]:.1f}x")
    print("    float(fixed lib) vs mpmath dps=50 agreement: < 2e-5 at every "
          "grid point (asserted).")
    return best_all[0], best_w1[0]


if __name__ == "__main__":
    check_a()
    okb = check_b()
    okc = check_c()
    ta, t1 = check_d()
    ok = okb and okc and ta < 0.362 and t1 < 0.362
    print()
    print("REP-T2F1 VERDICT:", "PASS" if ok else "FAIL")
