"""NC-W2: the dictionary lemmas feeding the Taylor bucket and the assembly.

 (a) Kernel values: E(u) := (1/12 - q(u))/u^2, q(u) = 1/u^2 - e^u/(e^u-1)^2.
     Certify E decreasing on [0, 4] (grid, 40-digit mpmath) and the upper
     decimals E(1) <= 0.00400694, E(2) <= 0.00358720, E(3) <= (printed).
 (b) Lemma W.2a (global |g''| bound): |g''(u)| <= |u|/120 for |u| <= 4
     (proof: partial fractions, valid |u| <= 2 pi sqrt(3); here grid-certified
     on |u| <= 4 at 40 digits, plus the analytic ratio printed).
 (c) Lemma W.2b (global g''' recentring): |g'''(u) - 1/120| <= u^2/273 on
     |u| <= 4 (proof: partial-fraction derivative bound; grid-certified).
 (d) Lemma W.3 boxes, verified against closed-form cumulants on a (m, w) grid
     with w up to 4:
       |kappa_3(lam)|            <= lam (S_4+m)/120        [W.2a]  and <= |w| m^4/545  (m>=30)
       |kappa_4(lam)|            <= (S_4+m)/120            [T.9''a, r=4, sharp]
       |kappa_4(lam)-kappa_4(0)| <= lam^2 (S_6+m)/273      [W.2b]  and <= w^2 m^5/1500 (m>=30)
       |kappa_5(lam)|            <= C5 (S_5+m),  C5 = 48 zeta(5)/(2pi)^5   [T.9''a]
       |kappa_6(lam)|            <= C6 (S_6+m),  C6 = 240 zeta(6)/(2pi)^6  [T.9''a]
 (e) Lemma W.1 (variance floor to |w| <= 4): the four-band bound
       1 - s2/lambda <= lam^2 [ Q(n1)/240 + (Q(n2)-Q(n1)) E(w/4)
                     + (Q(n3)-Q(n2)) E(w/2) + (Q(m)-Q(n3)) E(3w/4) ] / lambda,
     Q(n) = sum_{j<=n} j^4 exact, n1 = floor(m/4), n2 = floor(m/2),
     n3 = floor(3m/4).  Certify: bound >= true deficit on the grid; the
     grid-max of the bound over m >= 30, |w| <= 4 is <= 0.45  =>  s2 >= 0.55 lambda.
     Also the simple quadratic clause: 1 - s2/lambda <= coef(m) w^2 with
     coef(m) = S_4/(240 m^2 lambda) <= 0.0330 for m >= 30 (exact Fractions),
     giving c_1 = 0.967 (K=1), c_2 = 0.868 (K=2).
 (f) Constant certificates: (S_4+m)*545 <= 120 m^5 and (S_6+m)*1500 <= 273 m^7
     for m >= 30 (exact Fraction check on a grid + leading-coefficient note).

Run: python3 wp2b_nc2_dictionary.py
"""
import os
import sys
from fractions import Fraction

import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wp2b_lib_fixed as lib  # REPAIRED library (repairs_20260811)

mp.mp.dps = 40


def q_mp(u):
    return 1 / u**2 - mp.e**u / (mp.e**u - 1) ** 2


def E_mp(u):
    if u == 0:
        return mp.mpf(1) / 240
    return (mp.mpf(1) / 12 - q_mp(u)) / u**2


def g2_mp(u):
    return 2 / u**3 - mp.e**u * (mp.e**u + 1) / (mp.e**u - 1) ** 3


def g3_mp(u):
    eu = mp.e**u
    return -6 / u**4 + eu * (eu * eu + 4 * eu + 1) / (eu - 1) ** 4


def main():
    ok = True

    # (a) kernel values, monotonicity
    grid = [mp.mpf(i) / 100 for i in range(1, 401)]
    Ev = [E_mp(u) for u in grid]
    mono = all(Ev[i] >= Ev[i + 1] for i in range(len(Ev) - 1))
    E1, E2, E3 = E_mp(mp.mpf(1)), E_mp(mp.mpf(2)), E_mp(mp.mpf(3))
    print("(a) E decreasing on (0,4] (400-pt grid):", mono)
    print(f"    E(1) = {mp.nstr(E1, 10)}  (<= 0.00400694: {E1 <= mp.mpf('0.00400694')})")
    print(f"    E(2) = {mp.nstr(E2, 10)}  (<= 0.00358720: {E2 <= mp.mpf('0.00358720')})")
    print(f"    E(3) = {mp.nstr(E3, 10)}  (<= 0.00304100: {E3 <= mp.mpf('0.00304100')})")
    ok &= mono and E1 <= mp.mpf('0.00400694') and E2 <= mp.mpf('0.00358720') \
        and E3 <= mp.mpf('0.00304100')

    # (b) |g''(u)| <= |u|/120 on (0, 4]
    worst_b = mp.mpf(0)
    for u in grid:
        worst_b = max(worst_b, abs(g2_mp(u)) / (u / 120))
    print(f"(b) max |g''(u)|/(|u|/120) on (0,4]: {mp.nstr(worst_b, 8)}  (<= 1: {worst_b <= 1})")
    ok &= worst_b <= 1

    # (c) |g'''(u) - 1/120| <= u^2/273 on (0, 4]
    worst_c = mp.mpf(0)
    for u in grid:
        worst_c = max(worst_c, abs(g3_mp(u) - mp.mpf(1) / 120) / (u**2 / 273))
    print(f"(c) max |g'''(u)-1/120|/(u^2/273) on (0,4]: {mp.nstr(worst_c, 8)}  (<= 1: {worst_c <= 1})")
    ok &= worst_c <= 1

    # certified zeta constants (rounded UP at 12 digits)
    C5 = 2 * 24 * mp.zeta(5) / (2 * mp.pi) ** 5
    C6 = 2 * 120 * mp.zeta(6) / (2 * mp.pi) ** 6
    C5_up, C6_up = mp.mpf('5.08266e-3'), mp.mpf('3.96835e-3')
    print(f"    C5 = 48 zeta(5)/(2pi)^5 = {mp.nstr(C5, 10)} (<= {C5_up}: {C5 <= C5_up})")
    print(f"    C6 = 240 zeta(6)/(2pi)^6 = {mp.nstr(C6, 10)} (<= {C6_up}: {C6 <= C6_up})")
    ok &= C5 <= C5_up and C6 <= C6_up

    # (d) cumulant boxes vs closed forms
    print("(d) cumulant bounds vs closed forms (ratios must be <= 1):")
    r3 = r3c = r4 = r4r = r4rc = r5 = r6 = 0.0
    for m in (30, 60, 120, 300):
        S4 = float(lib.S(4, m)); S5 = float(lib.S(5, m)); S6 = float(lib.S(6, m))
        k40 = -(S4 - m) / 120.0
        for wi in range(1, 41):
            w = 4.0 * wi / 40
            lam = w / m
            _, s2, k3, k4, k5, k6 = lib.cumulants(m, lam)
            r3 = max(r3, abs(k3) / (lam * (S4 + m) / 120))
            r3c = max(r3c, abs(k3) / (w * m**4 / 545))
            r4 = max(r4, abs(k4) / ((S4 + m) / 120))
            r4r = max(r4r, abs(k4 - k40) / (lam**2 * (S6 + m) / 273))
            r4rc = max(r4rc, abs(k4 - k40) / (w**2 * m**5 / 1500))
            r5 = max(r5, abs(k5) / (float(C5) * (S5 + m)))
            r6 = max(r6, abs(k6) / (float(C6) * (S6 + m)))
    print(f"    |kappa_3| / [lam(S_4+m)/120]      max ratio = {r3:.4f}")
    print(f"    |kappa_3| / [w m^4/545]           max ratio = {r3c:.4f}")
    print(f"    |kappa_4| / [(S_4+m)/120]         max ratio = {r4:.4f}")
    print(f"    |kappa_4-kappa_4(0)| / [lam^2(S_6+m)/273] max ratio = {r4r:.4f}")
    print(f"    |kappa_4-kappa_4(0)| / [w^2 m^5/1500]     max ratio = {r4rc:.4f}")
    print(f"    |kappa_5| / [C5 (S_5+m)]          max ratio = {r5:.4f}")
    print(f"    |kappa_6| / [C6 (S_6+m)]          max ratio = {r6:.4f}")
    ok &= max(r3, r3c, r4, r4r, r4rc, r5, r6) <= 1.0
    # report kappa_4 sign behaviour at large w (informational)
    for m in (60,):
        for w in (2.0, 3.0, 4.0):
            _, s2, k3, k4, k5, k6 = lib.cumulants(m, w / m)
            k40 = -(float(lib.S(4, m)) - m) / 120.0
            print(f"    [info] m={m} w={w}: kappa_4(lam)/kappa_4(0) = {k4/k40:.4f}")

    # (e) Lemma W.1 variance floor
    print("(e) four-band deficit bound (Lemma W.1):")
    Q = lambda n: sum(Fraction(j) ** 4 for j in range(1, n + 1))
    worst_bound, worst_at, viol = 0.0, None, 0.0
    for m in (30, 40, 50, 60, 80, 100, 150, 200, 300, 500, 1000, 3000):
        lamv = float(lib.lam_var(m))
        n1, n2, n3 = m // 4, m // 2, (3 * m) // 4
        Q1, Q2, Q3, Q4 = float(Q(n1)), float(Q(n2)), float(Q(n3)), float(Q(m))
        for wi in range(1, 81):
            w = 4.0 * wi / 80
            lam = w / m
            bound = lam * lam * (Q1 / 240 + (Q2 - Q1) * float(E_mp(mp.mpf(w) / 4))
                                 + (Q3 - Q2) * float(E_mp(mp.mpf(w) / 2))
                                 + (Q4 - Q3) * float(E_mp(3 * mp.mpf(w) / 4))) / lamv
            _, s2, *_ = lib.cumulants(m, lam)
            true_def = 1 - s2 / lamv
            viol = max(viol, true_def - bound)
            if bound > worst_bound:
                worst_bound, worst_at = bound, (m, w)
    print(f"    max PROVED deficit bound over grid = {worst_bound:.4f} at (m,w)={worst_at}"
          f"  (<= 0.40, giving c_4 = 0.60: {worst_bound <= 0.40})")
    print(f"    max (true deficit - bound) = {viol:.2e}  (must be <= 0)")
    ok &= worst_bound <= 0.40 and viol <= 0
    # simple quadratic clause
    coef30 = Fraction(lib.S(4, 30)) / (240 * 30**2 * lib.lam_var(30))
    dec = all(
        Fraction(lib.S(4, m)) / (240 * m**2 * lib.lam_var(m))
        >= Fraction(lib.S(4, m + 10)) / (240 * (m + 10) ** 2 * lib.lam_var(m + 10))
        for m in range(30, 300, 10))
    print(f"    coef(30) = S_4/(240 m^2 lambda) = {float(coef30):.6f} (<= 0.0330:"
          f" {coef30 <= Fraction(330, 10000)}), decreasing on 30..300 step 10: {dec}")
    ok &= coef30 <= Fraction(330, 10000) and dec

    # floors c_K vs true s2/lambda
    floors = {1: 0.967, 2: 0.868, 4: 0.60}
    print("    floors: true min s2/lambda vs c_K:")
    for K, cK in floors.items():
        worst = 1.0
        for m in (30, 60, 120, 300):
            lamv = float(lib.lam_var(m))
            for wi in range(1, 41):
                w = K * wi / 40
                _, s2, *_ = lib.cumulants(m, w / m)
                worst = min(worst, s2 / lamv)
        print(f"      K={K}: true min s2/lambda = {worst:.4f}  (>= c_{K} = {cK}: {worst >= cK})")
        ok &= worst >= cK

    # (f) polynomial constant certificates (exact, m = 30..2000)
    c1 = all((lib.S(4, m) + m) * 545 <= 120 * Fraction(m) ** 5
             for m in list(range(30, 200)) + [500, 1000, 2000])
    c2 = all((lib.S(6, m) + m) * 1500 <= 273 * Fraction(m) ** 7
             for m in list(range(30, 200)) + [500, 1000, 2000])
    print(f"(f) (S_4+m)*545 <= 120 m^5 (m=30..2000 sample): {c1};  "
          f"(S_6+m)*1500 <= 273 m^7: {c2}")
    ok &= c1 and c2

    print("\nNC-W2 VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
