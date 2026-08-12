"""rep_t2_numerics.py -- repairs_20260811, T2 numeric-referee repairs
F2, F5, F6, F7, F8 (STATUS.md 3).  F1 is rep_t2f1_blam_chain.py; F3's
threshold recomputation is in rep_wp1c_repairs.py (R5); F4 is certified by
re-running the original t2_nc10_far.py (output quoted in repairs_20260811.md);
F9 is an observation/flag, no number changes.

  F2: (T.9''c)'s constant chain evaluates to 2.6113e-4 > printed 2.61e-4
      (unsafe rounding); corrected print: 2.62e-4.  (T.9''b)'s 2.8e6 IS safe.
  F5: T.9'' step-2 parenthetical "m <= 0.01 (m+1)^{r+1}/(r+1), r >= 3,
      m >= 4" is FALSE at (4,3), (5,3); TRUE for all m >= 6 (certified
      m = 6..1000 at r = 3, and r = 3..12 at m = 6..40).
  F6: T.4's crude clause chain needs S_4/(m^2 lambda) <= 12: value 17.0 at
      m = 2 (chain fails), 11.879 at m = 3 (chain works, m >= 3); the clause
      itself is TRUE at m = 2 by direct evaluation (deficit 0.4301 <=
      pi^2/20 = 0.4935).
  F7: T.4's lower-bound display drops -(lam^2/240) m w^2/19; its relative
      size 5w^2/(19 m^4) <= 3.3e-6 at m >= 30, w <= pi -- absorbed by the
      0.02857 -> 0.0285 rounding.  Display fix; certified here.
  F8: (i) g'' series is u/120 - u^3/1512 + u^5/28800 - ... (exact Bernoulli
      arithmetic: the u^7-coefficient of g is 1/1209600, and 42/1209600 =
      1/28800; NOT 1/43200);
      (ii) E U^2 at lam = 1/2 (untruncated geometric) = q(1+q)/(1-q)^2 =
      6.294 (not 6.31); 2000/6.294 = 317.8 so "m <= 316 forces lam < 1/2"
      survives a fortiori;
      (iii) sin^2(1/8) = 0.015544 (nc5 docstring's 0.015549 is a typo; the
      draft text is right).

Run: python3 rep_t2_numerics.py
"""
from fractions import Fraction

import mpmath as mp

mp.mp.dps = 30


def f2():
    z4 = mp.zeta(4)
    first = mp.mpf("2.02") * z4 / (20 * (2 * mp.pi) ** 4)
    total = first / mp.mpf("0.2686")
    # (T.9''b) side: first term (m+1)^8|t|^7 coefficient
    z = mp.mpf("2.02") * mp.mpf("1.0084") / (56 * (2 * mp.pi) ** 7)
    denom_b = mp.mpf("0.2686") / z
    print(f"F2: (T.9''c) chain: first tail term coeff = {mp.nstr(first, 6)} "
          f"(draft: 7.02e-5); /0.2686 = {mp.nstr(total, 6)}")
    print(f"    -> printed 2.61e-4 is UNSAFE (chain gives 2.6113e-4); "
          f"corrected print 2.62e-4: {total <= mp.mpf('2.62e-4')}")
    print(f"    (T.9''b) denominator check: chain gives "
          f"{mp.nstr(denom_b, 5)} >= 2.8e6 (printed value safe): "
          f"{denom_b >= mp.mpf('2.8e6')}")
    return total <= mp.mpf("2.62e-4") and denom_b >= mp.mpf("2.8e6")


def f5():
    def cond(m, r):
        return Fraction(1, 100) * Fraction((m + 1) ** (r + 1), r + 1) >= m
    bad = [(m, r) for m in (4, 5) for r in (3,) if not cond(m, r)]
    ok6 = all(cond(m, 3) for m in range(6, 1001)) and \
        all(cond(m, r) for m in range(6, 41) for r in range(3, 13))
    print(f"F5: 'm <= 0.01(m+1)^(r+1)/(r+1)' FALSE at {bad} "
          f"(0.01*5^4/4 = {float(Fraction(625, 400)):.4f} < 4; "
          f"0.01*6^4/4 = {float(Fraction(1296, 400)):.4f} < 5)")
    print(f"    TRUE for all m >= 6 (exact Fractions, m = 6..1000 at r = 3; "
          f"r = 3..12 at m = 6..40): {ok6}  -> fix parenthetical to m >= 6; "
          f"lemma scope m >= 30 unaffected.")
    return len(bad) == 2 and ok6


def f6():
    vals = {}
    for m in (2, 3):
        S4 = sum(Fraction(j) ** 4 for j in range(1, m + 1))
        lamv = Fraction(m * (m - 1) * (2 * m + 5), 72)
        vals[m] = S4 / (m * m * lamv)
    # direct clause check at m = 2, w = pi (lam = pi/2):
    lam = mp.pi / 2
    p = mp.e ** (-lam) / (1 + mp.e ** (-lam))
    s2 = p * (1 - p)              # only the j = 2 factor has variance
    deficit = 1 - s2 / mp.mpf(0.25)
    gate = mp.pi ** 2 / 20
    print(f"F6: S_4/(m^2 lambda) = {float(vals[2]):.3f} at m = 2 (> 12: chain"
          f" fails), {float(vals[3]):.3f} at m = 3 (<= 12: chain OK, m >= 3)")
    print(f"    direct check m = 2, w = pi: deficit = {mp.nstr(deficit, 5)} "
          f"<= pi^2/20 = {mp.nstr(gate, 5)}: {deficit <= gate} "
          f"(clause TRUE at m = 2 by direct evaluation)")
    return vals[2] > 12 and vals[3] <= 12 and deficit <= gate


def f7():
    worst = 0.0
    for m in (30, 60, 120):
        for w in (1.0, 2.0, float(mp.pi)):
            rel = 5 * w * w / (19 * m ** 4)
            worst = max(worst, rel)
    print(f"F7: dropped term -(lam^2/240) m w^2/19: relative size "
          f"5w^2/(19 m^4) <= {worst:.2e} at m >= 30, w <= pi "
          f"(<= 3.3e-6: {worst <= 3.3e-6}) -- absorbed by the "
          f"0.02857 -> 0.0285 rounding; display fix recorded.")
    return worst <= 3.3e-6


def f8():
    # (i) exact Bernoulli series of g and its second derivative
    # g(u) = 1/2 - u/12 + u^3/720 - u^5/30240 + u^7/1209600 - u^9/47900160
    c7 = Fraction(1, 1209600)
    c_g2_5 = 42 * c7                     # 7*6 * u^5-coefficient
    ok_i = c_g2_5 == Fraction(1, 28800) and c_g2_5 != Fraction(1, 43200)
    # numeric confirmation of the limit (dps 60 and u = 0.05, away from the
    # closed form's catastrophic-cancellation zone; next correction ~ 1e-4 rel)
    mp.mp.dps = 60
    u = mp.mpf("0.05")
    g2 = (lambda x: 2 / x**3 - mp.e**x * (mp.e**x + 1) / (mp.e**x - 1) ** 3)
    lim = (g2(u) - u / 120 + u**3 / 1512) / u**5
    mp.mp.dps = 30
    print(f"F8(i): g'' u^5-coefficient = 42/1209600 = 1/28800 = "
          f"{float(c_g2_5):.4e} (not 1/43200 = {1/43200:.4e}): {ok_i}; "
          f"numeric limit {mp.nstr(lim, 5)}")
    # (ii) E U^2 at lam = 1/2
    q = mp.e ** mp.mpf("-0.5")
    eu2 = q * (1 + q) / (1 - q) ** 2
    ok_ii = abs(eu2 - mp.mpf("6.2941")) < 1e-3
    print(f"F8(ii): E U^2 at lam = 1/2 = q(1+q)/(1-q)^2 = {mp.nstr(eu2, 5)} "
          f"(draft said 6.31); 2000/{mp.nstr(eu2, 5)} = "
          f"{mp.nstr(2000 / eu2, 5)} -> 'm <= 316 forces lam < 1/2' survives "
          f"a fortiori: {2000 / eu2 > 316}")
    # (iii) sin^2(1/8)
    s = mp.sin(mp.mpf(1) / 8) ** 2
    ok_iii = abs(s - mp.mpf("0.015544")) < 5e-7
    print(f"F8(iii): sin^2(1/8) = {mp.nstr(s, 6)} -> 0.015544 (nc5 docstring"
          f" 0.015549 is a typo; draft text correct): {ok_iii}")
    return ok_i and ok_ii and ok_iii


if __name__ == "__main__":
    oks = [f2(), f5(), f6(), f7(), f8()]
    print()
    print("REP-T2-NUMERICS VERDICT:", "PASS" if all(oks) else f"CHECK {oks}")
