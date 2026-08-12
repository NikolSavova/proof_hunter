#!/usr/bin/env python3
"""NC-P2 (wp3-a2): certify the Lemma P.4 / Theorem P.5 constant chain and
measure its slack against exact truth.

Proved chain (draft §2), parametrized by c = k_max/m, standing m >= 30,
2 <= k <= min(c*m, m-1):

  x+ = (k+1)/(m+k) <= xc(c) := (c*30+1)/((1+c)*30)   [worst m = 30; for c = 1
        use k <= m-1: x+ <= m/(2m-1) <= 30/59]
  Phi_min(c) := 1 - xc - xc^2
  C_d(c) := sigma1p(xc)/xc,   sigma1p(x) = sum_{g in G+} g x^g   (G+ = pentagonal >= 1)
  C_A(c) := 4 + 6 * sum_{g in G+, g >= 5} g^2 xc^{g-2}
  C_P(c) := C_A/Phi_min + C_d^2/Phi_min^2
  m_p(c) := smallest integer m >= 30 with  3*C_P(c)*c*(1+c) <= m - 1
            (then r(k)-1 >= (m-1)/(2k(m+k)) on the whole range)

All sums in exact Fractions over pentagonal g <= 400 with an explicit
all-integer geometric tail bound added (printed).  Then: measured maxima of
m^2|Delta^2 Psi|, m*max|d_pm|, m^2|D_Phi| over exact binomial-ratio Phi.
"""
from fractions import Fraction
from math import comb, log

def pent_ge1(limit=400):
    out = []
    n = 1
    while True:
        g1 = n * (3 * n - 1) // 2
        g2 = n * (3 * n + 1) // 2
        if g1 > limit and g2 > limit:
            break
        if g1 <= limit: out.append(g1)
        if g2 <= limit: out.append(g2)
        n += 1
    return sorted(out)

G = pent_ge1()

def tail_bound(x, G0=400):
    # all-integer tail sum_{g>G0} g^2 x^{g-2} <= x^{G0-1} * sum_{j>=0}(G0+1+j)^2 x^j
    # <= x^{G0-1} * ( (G0+1)^2/(1-x) + 2(G0+1)x/(1-x)^2 + 2x/(1-x)^3 )  -- crude, fine
    xf = float(x)
    return xf ** (G0 - 1) * ((G0 + 1) ** 2 / (1 - xf) + 2 * (G0 + 1) * xf / (1 - xf) ** 2
                             + 2 * xf / (1 - xf) ** 3)

def chain(c_num, c_den, cap_c1=False):
    """Return dict of proved constants for c = c_num/c_den (exact)."""
    c = Fraction(c_num, c_den)
    if cap_c1:
        xc = Fraction(30, 59)                      # c = 1: k <= m-1, m >= 30
    else:
        xc = (c * 30 + 1) / ((1 + c) * 30)
    s1p = sum(Fraction(g) * xc ** g for g in G)            # sigma1'(xc)
    s2r = sum(Fraction(g * g) * xc ** (g - 2) for g in G if g >= 5)
    tb = tail_bound(xc)
    Phimin = 1 - xc - xc * xc
    Cd = s1p / xc
    CA = 4 + 6 * (s2r + Fraction(int(tb * 10**30) + 1, 10**30))
    CP = CA / Phimin + Cd * Cd / (Phimin * Phimin)
    # threshold: smallest m >= 30 with 3*CP*c*(1+c) <= m-1
    thr = 3 * CP * c * (1 + c) + 1
    mp = max(30, -(-thr.numerator // thr.denominator))     # ceil
    return dict(c=c, xc=xc, Phimin=Phimin, Cd=Cd, CA=CA, CP=CP, mp=mp, tail=tb)

def measure(mlist):
    """Measured maxima over exact pentagonal-Phi: m^2|A|, m*dmax, m^2|D_Phi|,
    restricted to k <= m-1, reported also per c-range."""
    print("== measured truth (exact binomial Phi; floats only in report) ==")
    print("   m   max m^2|A|   max m*d   max m^2|D_Phi|   (over 2<=k<=m-1)")
    for m in mlist:
        T = lambda j: comb(m - 1 + j, m - 1) if j >= 0 else 0
        def Phi(kk):
            s = Fraction(0)
            s += 1
            sign_of = {}
            n = 1
            while n * (3 * n - 1) // 2 <= kk:
                for g in (n * (3 * n - 1) // 2, n * (3 * n + 1) // 2):
                    if g <= kk:
                        num = 1; den = 1
                        for i in range(g):
                            num *= (kk - i); den *= (m + kk - 1 - i)
                        s += (-1) ** n * Fraction(num, den)
                n += 1
            return s
        maxA = maxd = maxD = 0.0
        argA = argd = argD = None
        prev = {1: Phi(1), 2: Phi(2)}
        vals = {}
        for k in range(1, m + 1):
            vals[k] = Phi(k)
        for k in range(2, m):
            Pk, Pm, Pp = vals[k], vals[k - 1], vals[k + 1]
            A = float((Pp - Pk) + (Pm - Pk))      # Delta^2 Psi = -Delta^2 Phi ... sign-free abs
            dp = abs(float(Pp - Pk)); dm = abs(float(Pm - Pk))
            D = 2 * log(float(Pk)) - log(float(Pm)) - log(float(Pp))
            if abs(A) * m * m > maxA: maxA, argA = abs(A) * m * m, k
            if max(dp, dm) * m > maxd: maxd, argd = max(dp, dm) * m, k
            if abs(D) * m * m > maxD: maxD, argD = abs(D) * m * m, k
        print(f"  {m:4d}   {maxA:9.4f}(k={argA:3d})  {maxd:7.4f}(k={argd:3d})  "
              f"{maxD:9.4f}(k={argD:3d})")

def main():
    print("== proved constants per c (exact Fractions, tail bound added) ==")
    print("    c      xc      Phi_min     C_d      C_A       C_P      m_p(c)   s2-floor v(c)=c(1+c)/6")
    rows = [ (Fraction(1,4), False), (Fraction(1,2), False), (Fraction(7,10), False),
             (Fraction(3,4), False), (Fraction(1,1), True) ]
    for c, cap in rows:
        d = chain(c.numerator, c.denominator, cap_c1=cap)
        v = c * (1 + c) / 6
        print(f"  {float(c):5.2f}  {float(d['xc']):.4f}   {float(d['Phimin']):.4f}   "
              f"{float(d['Cd']):7.4f}  {float(d['CA']):7.3f}  {float(d['CP']):8.2f}   "
              f"{d['mp']:6d}    {float(v):.4f}  (tail add {d['tail']:.1e})")
    measure([30, 60, 120, 200, 400])

if __name__ == "__main__":
    main()
