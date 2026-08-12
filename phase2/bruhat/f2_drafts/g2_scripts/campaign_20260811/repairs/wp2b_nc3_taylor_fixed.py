"""NC-W3: the Taylor-remainder bucket for the 6-term tilted model (Lemma W.4).

Bucket being certified: in the chain
   s2 log F(0) = 1 - B_lam + N(0)/P(0)^2 + theta_T * T,   |theta_T| <= 1,
   F(0) := e^{1/s2} P(0)^2 / (P(-h) P(h)),  h := s2^{-1/2},  L := log P,
the Taylor remainder is  T := sup_{|y| <= h} |L''''(y)| / (12 s2)   (B.7'-form,
fourth-order symmetric Taylor with integral remainder; odd orders cancel).

Proved upper bound assembled here (everything from NC-W2's boxes):
  s2 >= s2min := c_K lambda(m)  (c_1=0.967, c_2=0.868, c_4=0.60);  hmax = 1/sqrt(s2min);
  |a| <= amax := (K/m)(S_4+m)/120/(6 s2min^{3/2}),  |b| <= bmax := (S_4+m)/120/(24 s2min^2),
  |d| <= dmax := C5 (S_5+m)/(120 s2min^{5/2}),      |g| <= gmax := C6 (S_6+m)/(720 s2min^3);
  Hermite sups on |y| <= h (exact for h <= 1/2):
    |He1|<=h, |He2|<=1, |He3|<=3h, |He4|<=3, |He5|<=15h, |He6|<=15, |He7|<=105h, |He8|<=105;
  p1 <= 3a + 12bh + 15d + 90(g+a^2/2)h + 105ab + 840(b^2/2+ad)h
  p2 <= 6ah + 12b + 60dh + 90(g+a^2/2) + 630abh + 840(b^2/2+ad)
  p3 <= 6a + 24bh + 60d + 360(g+a^2/2)h + 630ab + 5040(b^2/2+ad)h
  p4 <= 24b + 120dh + 360(g+a^2/2) + 2520abh + 5040(b^2/2+ad)
  Pmin >= 1 - [3ah + 3b + 15dh + 15(g+a^2/2) + 105abh + 105(b^2/2+ad)]
  supL4 <= p4/Pm + 4 p3 p1/Pm^2 + 3 p2^2/Pm^2 + 12 p2 p1^2/Pm^3 + 6 p1^4/Pm^4
  T(K, m) (as C_R contribution, x m^2)  <=  m^2 supL4 / (12 s2min).

Checks:
 (1) Hermite sup constants: dense-grid certificate on |y| <= 0.05 (largest h
     in the table is h(30, K=4) = 0.0461).
 (2) The bucket table T(K, m) for K in {1,2,4}, m in {30,60,120,180,500,2000};
     monotone decrease in m verified on a log grid to 3000.
 (3) TRUTH: at sample (m, w), true scaled coefficients -> true remainder
     R_T := |2L(0) - L(h) - L(-h) + h^2 L''(0)|, check R_T <= (h^4/12) supL4_true
     (direct grid sup of |L''''| on J) and s2 R_T m^2 <= T(K, m) with the ratio
     printed (expected: large slack, the bound is a crude quotient-rule bound).
 (4) Fourier-rule quadrature check at (m=30, w=1): phat(x) := (1/2pi) int
     phihat_lam(t) e^{-itx} dt computed by mpmath.quad vs Z(y) P(y) at x=0,+-1,
     and the exact-ratio identity phat(0)^2/(phat(-1)phat(1)) = e^{1/s2}
     P(0)^2/(P(-h)P(h)).

Run: python3 wp2b_nc3_taylor.py
"""
import math
import os
import sys

import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wp2b_lib_fixed as lib  # REPAIRED library (repairs_20260811)

mp.mp.dps = 30

C5UP = 5.08266e-3   # certified >= 48 zeta(5)/(2pi)^5   (NC-W2)
C6UP = 3.96835e-3   # certified >= 240 zeta(6)/(2pi)^6  (NC-W2)
CK = {1: 0.967, 2: 0.868, 4: 0.60}   # variance floors (NC-W2 (e))


def boxes(K, m):
    lamv = float(lib.lam_var(m))
    s2min = CK[K] * lamv
    S4 = float(lib.S(4, m)); S5 = float(lib.S(5, m)); S6 = float(lib.S(6, m))
    a = (K / m) * (S4 + m) / 120 / (6 * s2min**1.5)
    b = (S4 + m) / 120 / (24 * s2min**2)
    d = C5UP * (S5 + m) / (120 * s2min**2.5)
    g = C6UP * (S6 + m) / (720 * s2min**3)
    h = 1 / math.sqrt(s2min)
    return a, b, d, g, h, s2min


def taylor_bucket(K, m):
    a, b, d, g, h, s2min = boxes(K, m)
    ga = g + a * a / 2
    e8 = b * b / 2 + a * d
    p1 = 3*a + 12*b*h + 15*d + 90*ga*h + 105*a*b + 840*e8*h
    p2 = 6*a*h + 12*b + 60*d*h + 90*ga + 630*a*b*h + 840*e8
    p3 = 6*a + 24*b*h + 60*d + 360*ga*h + 630*a*b + 5040*e8*h
    p4 = 24*b + 120*d*h + 360*ga + 2520*a*b*h + 5040*e8
    Pm = 1 - (3*a*h + 3*b + 15*d*h + 15*ga + 105*a*b*h + 105*e8)
    if Pm <= 0:
        return None
    supL4 = (p4/Pm + 4*p3*p1/Pm**2 + 3*p2**2/Pm**2 + 12*p2*p1**2/Pm**3
             + 6*p1**4/Pm**4)
    return dict(bucket=m*m*supL4/(12*s2min), supL4=supL4, Pmin=Pm, h=h,
                a=a, b=b, d=d, g=g)


def main():
    ok = True

    # (1) Hermite sup constants on |y| <= 0.05 (covers every h in the table)
    sups = {1: (1.0, 1), 2: (1.0, 0), 3: (3.0, 1), 4: (3.0, 0), 5: (15.0, 1),
            6: (15.0, 0), 7: (105.0, 1), 8: (105.0, 0)}
    worst = 0.0
    for n, (c, hpow) in sups.items():
        for i in range(-500, 501):
            y = 0.05 * i / 500
            lim = c * (0.05 ** hpow) if hpow else c
            worst = max(worst, abs(lib.He(n, y)) / lim)
    print(f"(1) Hermite sup certificates on |y|<=0.05: max ratio = {worst:.4f} (<= 1: {worst <= 1})")
    ok &= worst <= 1

    # (2) bucket table
    print("(2) Taylor bucket T(K, m) = m^2 sup|L''''|/(12 s2min)  [C_R contribution]:")
    print(f"    {'m':>5s}  {'K=1':>10s} {'K=2':>10s} {'K=4':>10s}   (Pmin at K=4)")
    table = {}
    for m in (30, 60, 120, 180, 500, 2000):
        row = []
        for K in (1, 2, 4):
            r = taylor_bucket(K, m)
            row.append(r["bucket"] if r else float("nan"))
            table[(K, m)] = r
        p4 = table[(4, m)]
        print(f"    {m:5d}  {row[0]:10.5f} {row[1]:10.5f} {row[2]:10.5f}   ({p4['Pmin']:.4f})")
    mono_ok = True
    for K in (1, 2, 4):
        prev = None
        for m in range(30, 3001, 10):
            r = taylor_bucket(K, m)
            if r is None:
                mono_ok = False
                break
            if prev is not None and r["bucket"] > prev + 1e-15:
                mono_ok = False
                print(f"    NON-MONOTONE at K={K}, m={m}")
                break
            prev = r["bucket"]
    print(f"    decreasing in m on 30..3000 (step 10), all K: {mono_ok}")
    ok &= mono_ok

    # (3) truth vs bound
    print("(3) true Taylor remainder vs bound (samples):")
    print(f"    {'m':>4s} {'K':>2s} {'w':>4s}  {'s2*R_T*m^2':>12s} {'bucket bound':>12s} {'ratio':>8s}  {'RT<=h4/12*supL4tr':>18s}")
    for m in (30, 60, 120):
        for K in (1, 2, 4):
            for w in (K / 2, K):
                a, b, d, g, s2 = lib.scaled_coeffs(m, w / m)
                h = 1 / math.sqrt(s2)
                L = lambda yy: math.log(lib.P_eval(a, b, d, g, yy))
                # L''(0) exactly from P-derivatives
                P0 = lib.P_eval(a, b, d, g, 0.0)
                P1 = lib.P_eval(a, b, d, g, 0.0, 1)
                P2 = lib.P_eval(a, b, d, g, 0.0, 2)
                L2 = (P2 * P0 - P1 * P1) / P0**2
                RT = abs(2 * L(0.0) - L(h) - L(-h) + h * h * L2)
                # direct sup of |L''''| on J by grid
                supt = 0.0
                for i in range(-40, 41):
                    yy = h * i / 40
                    Pv = [lib.P_eval(a, b, d, g, yy, r) for r in range(5)]
                    l4 = (Pv[4]/Pv[0] - (4*Pv[3]*Pv[1] + 3*Pv[2]**2)/Pv[0]**2
                          + 12*Pv[2]*Pv[1]**2/Pv[0]**3 - 6*Pv[1]**4/Pv[0]**4)
                    supt = max(supt, abs(l4))
                bound = taylor_bucket(K, m)["bucket"]
                tru = s2 * RT * m * m
                within = RT <= h**4 / 12 * supt * (1 + 1e-9) + 1e-18
                print(f"    {m:4d} {K:2d} {w:4.1f}  {tru:12.3e} {bound:12.5f} "
                      f"{tru/bound:8.1e}  {str(within):>18s}")
                ok &= tru <= bound and within

    # (4) Fourier-rule quadrature check at (m=30, w=1)
    m30, w = 30, 1.0
    a, b, d, g, s2 = lib.scaled_coeffs(m30, w / m30)
    s2m = mp.mpf(s2)
    al, be = mp.mpf(a) * s2m**mp.mpf(1.5), mp.mpf(b) * s2m**2
    de, ga = mp.mpf(d) * s2m**mp.mpf(2.5), mp.mpf(g) * s2m**3

    def phihat(t):
        E = (-1j * al * t**3 - be * t**4 + 1j * de * t**5
             + (-ga - al * al / 2) * t**6 + 1j * al * be * t**7
             + (be * be / 2 + al * de) * t**8)
        return mp.e ** (-s2m * t * t / 2) * (1 + E)

    def phat(x):
        f = lambda t: (phihat(t) * mp.e ** (-1j * t * x)).real
        return mp.quad(f, [-mp.inf, 0, mp.inf]) / (2 * mp.pi)

    Z = lambda y: mp.e ** (-y * y / 2) / mp.sqrt(2 * mp.pi * s2m)
    vals, worst4 = {}, mp.mpf(0)
    for x in (0, 1, -1):
        y = mp.mpf(x) / mp.sqrt(s2m)
        model = Z(y) * lib.P_eval(a, b, d, g, float(y))
        got = phat(x)
        vals[x] = got
        worst4 = max(worst4, abs(got - model) / abs(model))
    ratio_quad = vals[0] ** 2 / (vals[1] * vals[-1])
    h2 = 1 / s2m
    ratio_form = (mp.e ** h2 * lib.P_eval(a, b, d, g, 0.0) ** 2
                  / (lib.P_eval(a, b, d, g, float(mp.sqrt(h2)))
                     * lib.P_eval(a, b, d, g, -float(mp.sqrt(h2)))))
    dev = abs(ratio_quad - ratio_form) / ratio_form
    print(f"(4) quadrature check (m=30, w=1): max rel dev phat vs Z*P = {mp.nstr(worst4, 3)};"
          f" ratio identity rel dev = {mp.nstr(dev, 3)}   (float-precision comparison)")
    ok &= worst4 < mp.mpf('1e-12') and dev < mp.mpf('1e-12')

    print("\nNC-W3 VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
