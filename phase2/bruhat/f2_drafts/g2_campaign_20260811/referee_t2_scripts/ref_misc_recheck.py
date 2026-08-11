"""Referee re-checks (numerics referee, T2 draft, 2026-08-11) of hand-arithmetic
displays in g2_draft_t2_20260803.md that no saved script covers, plus fine-grid
upgrades of two tight grid certificates.

Items:
 (a) T.4' pointwise kernel bounds |g''(u)-u/120| <= |u|^3/1500 and
     |g'''(u)-1/120| <= u^2/500 on (0, pi]: 30000-point grid at 30 digits
     (draft used 300 points, max ratio 0.9921 -- tight).  Also documents that
     the max ratio is the u->0 LIMIT 1500/1512 = 500/504 = 0.99206... (the
     bounds are alternating-series-provable: |g''-u/120| <= u^3/1512 exactly).
 (b) g'' series 5th-order coefficient: draft SS2 (T.4' proof) prints
     "g'' = u/120 - u^3/1512 + u^5/43200 - ...": check the true coefficient
     (expect 1/28800, i.e. the draft's 43200 is a typo; t2_item4's g2() uses
     28800).
 (c) T.6iii first-pass WRONG SIGN reproduction: the draft says the wrong sign
     fails "with ratio up to 6.4" but the saved script only tests the corrected
     sign.  Reproduce the failure.
 (d) Theorem T.9 Step 2 display "(1-delta)^{-2} <= 1 + 2.1 delta for
     delta <= 0.35": counterexamples, and the corrected coefficient of the
     "B_lam = B_m (1 + theta 0.35 w^2)" chain at w = 1 and w = pi.  Then
     measure the TRUTH: |B_lam/B_m - 1| / w^2 from exact cumulant closed forms
     (60-digit Decimal) at m in {30, 120}, w-grid to pi.
 (e) T.8-final's condition (V): the draft's parenthetical "numerically (V) then
     holds for m >~ 2.5e5" has no script.  Compute the actual thresholds at
     s2 = C_0 = 2000 (most favorable) and s2 = lambda (least favorable).
 (f) SS4 Step 3 note "b2 evaluates to 18*2.61e-4 (m+1)^5/s2^2 <= 27/m for
     s2 >= lambda/2": check at m = 30, 50, 100 (expect FALSE at m = 30).
 (g) T.9'' step-2 side condition "m <= 0.01 (m+1)^{r+1}/(r+1) for r >= 3,
     m >= 4": check m = 4..10 at r = 3 (expect FALSE at m = 4, 5).
 (h) Step 0 constant: E[U^2] for the untruncated geometric at lam = 1/2
     (draft says 6.31; expect 6.294) and the resulting forcing threshold.
 (i) T.4 crude clause "deficit <= w^2/20 for all m >= 2": the chain constant
     S_4/(m^2 lambda) at m = 2, 3, 4 (chain needs <= 12; expect 17 at m = 2)
     and a DIRECT check of the clause at m = 2, w = pi.
 (j) NC-T10c slack range: recompute bound/measured from the rerun values and
     compare with the draft's SS6 quote "24x-4e7x".
 (k) T.9'' displayed constant arithmetic: 1/1.063e7, 1/2.8e6, 2.61e-4, 0.7314,
     and the kappa_3^2 dimensional constant 4.6.
 (l) T.9''a adversarial extension: r = 11..14, lam in {5, 10}, m = 10
     (the saved script stops at r = 10, lam = 3).

stdlib + mpmath. Run: python3 ref_misc_recheck.py
"""
import cmath
import math
import sys
from decimal import Decimal, getcontext

import mpmath as mp

getcontext().prec = 60
D = Decimal
PI = D("3.14159265358979323846264338327950288419716939937510582097494")


# ---- Decimal closed-form cumulant machinery (same formulas as t2_nc1, re-typed)
def g0d(u):
    e = u.exp()
    return 1 / u - 1 / (e - 1)


def g1d(u):
    e = u.exp()
    return -1 / (u * u) + e / ((e - 1) ** 2)


def g2d(u):
    e = u.exp()
    return 2 / (u**3) - e * (e + 1) / ((e - 1) ** 3)


def g3d(u):
    e = u.exp()
    return -6 / (u**4) + e * (e * e + 4 * e + 1) / ((e - 1) ** 4)


def sig2_d(m, lam):
    g1l = g1d(lam)
    return sum(g1l - j * j * g1d(lam * j) for j in range(1, m + 1))


def kap4_d(m, lam):
    g3l = g3d(lam)
    return sum(g3l - j**4 * g3d(lam * j) for j in range(1, m + 1))


def main():
    ok_report = True

    print("(a) fine-grid T.4' kernel bounds, 30000 points, 30 digits")
    mp.mp.dps = 30
    r2 = mp.mpf(0)
    r3 = mp.mpf(0)
    at2 = at3 = None
    for i in range(1, 30001):
        u = mp.pi * i / 30000
        g2v = 2 / u**3 - mp.e**u * (mp.e**u + 1) / (mp.e**u - 1) ** 3
        g3v = -6 / u**4 + mp.e**u * (mp.e ** (2 * u) + 4 * mp.e**u + 1) / (mp.e**u - 1) ** 4
        q2 = abs(g2v - u / 120) / (u**3 / 1500)
        q3 = abs(g3v - mp.mpf(1) / 120) / (u * u / 500)
        if q2 > r2:
            r2, at2 = q2, u
        if q3 > r3:
            r3, at3 = q3, u
    print(f"  max ratio g'': {mp.nstr(r2, 8)} at u = {mp.nstr(at2, 6)}"
          f"   max ratio g''': {mp.nstr(r3, 8)} at u = {mp.nstr(at3, 6)}")
    print(f"  u->0 limits: 1500/1512 = {1500/1512:.6f}, 500/504 = {500/504:.6f}"
          "  (the sup IS the limit; bounds alternating-series-provable)")
    ok_report &= r2 <= 1 and r3 <= 1

    print("(b) g'' fifth-order coefficient: (g''(u) - u/120 + u^3/1512)/u^5 as u->0")
    for us in ("0.1", "0.05", "0.02"):
        u = mp.mpf(us)
        g2v = 2 / u**3 - mp.e**u * (mp.e**u + 1) / (mp.e**u - 1) ** 3
        c5 = (g2v - u / 120 + u**3 / 1512) / u**5
        print(f"  u={us}: coeff = {mp.nstr(c5, 8)}  (1/28800 = {1/28800:.8f};"
          f" draft's 1/43200 = {1/43200:.8f})")

    print("(c) T.6iii with the FIRST-PASS (wrong) sign: expect ratio > 1 (draft: up to 6.4)")

    def sig2_f(m, lam):
        def qf(u):
            if u < 1e-3:
                return 1 / 12 - u * u / 240 + u**4 / 6048
            em = math.exp(-u)
            om = -math.expm1(-u)
            return 1 / (u * u) - em / (om * om)

        ql = qf(lam)
        return sum(j * j * qf(lam * j) - ql for j in range(1, m + 1))

    def kap3_f(m, lam):
        def g2f(u):
            if u < 1e-2:
                return u / 120 - u**3 / 1512
            e = math.exp(u)
            return 2 / u**3 - e * (e + 1) / (e - 1) ** 3

        g2l = g2f(lam)
        return sum(j**3 * g2f(lam * j) - g2l for j in range(1, m + 1))

    def logphi_c(m, lam, t):
        s = 0j
        mu = 0.0
        for j in range(1, m + 1):
            zj = sum(math.exp(-lam * i) for i in range(j))
            nu = sum(cmath.exp((1j * t - lam) * i) for i in range(j)) / zj
            muj = sum(i * math.exp(-lam * i) for i in range(j)) / zj
            s += cmath.log(nu)
            mu += muj
        return s - 1j * t * mu

    worst_wrong = 0.0
    for m in (30,):
        for w in (0.001, 0.5, 1.0, 3.0):
            lam = w / m
            s2 = sig2_f(m, lam)
            k3 = kap3_f(m, lam)
            for i in range(1, 101):
                t = (1 / (20 * m)) + (i / 100) * (1 / (2 * m) - 1 / (20 * m))
                lhs = abs(logphi_c(m, lam, t) + s2 * t * t / 2 - 1j * k3 * t**3 / 6)
                worst_wrong = max(worst_wrong, lhs / ((m - 1) ** 2 * s2 * t**4 / 6))
    print(f"  wrong-sign max ratio (m=30) = {worst_wrong:.2f}"
          "  (draft claims 'up to 6.4'; corrected sign passes at 0.017)")

    print("(d) Step 2 display '(1-d)^-2 <= 1+2.1d for d <= 0.35':")
    for d in (0.033, 0.1, 0.35):
        lhs = (1 - d) ** -2
        rhs = 1 + 2.1 * d
        print(f"  d={d}: (1-d)^-2 = {lhs:.6f} vs 1+2.1d = {rhs:.6f}  "
              f"{'OK' if lhs <= rhs else 'FALSE'}")
    print("  corrected multiplicative chain (delta <= 0.0300 w^2 (1+3/m+w^2/18), m=180):")
    for w in (1.0, math.pi):
        d = 0.0300 * w * w * (1 + 3 / 180 + w * w / 18)
        first = (600 / 2200) * w * w
        second = (1 - d) ** -2 - 1
        total = (1 + first) * (1 + second) - 1
        print(f"  w={w:.3f}: delta<= {d:.4f}, chain gives |B_lam/B_m - 1| <= {total:.4f}"
              f" = {total/w**2:.4f} w^2   (draft claims 0.35 w^2)")
    print("  TRUTH from exact closed forms: |B_lam/B_m - 1|/w^2 :")
    for m in (30, 120):
        lamb = D(m * (m - 1) * (2 * m + 5)) / 72
        k40 = kap4_d(m, D("1e-9"))
        worst_true = 0.0
        for wi in range(1, 33):
            w = PI * wi / 32
            lam = w / m
            s2 = sig2_d(m, lam)
            k4 = kap4_d(m, lam)
            Bratio = (k4 / k40) * (lamb / s2) ** 2
            dev = abs(float(Bratio) - 1) / float(w) ** 2
            worst_true = max(worst_true, dev)
        print(f"    m={m}: max over w-grid (0, pi] = {worst_true:.4f}"
              f"  ({'inside' if worst_true <= 0.35 else 'OUTSIDE'} 0.35)")

    print("(e) condition (V): exp(-(m/pi-1)/4730) <= s2^{-3/2}/(2 min(m, s2))")
    for tag, s2_of_m in (("s2 = 2000 (most favorable)", lambda m: 2000.0),
                         ("s2 = lambda (least favorable)",
                          lambda m: m * (m - 1) * (2 * m + 5) / 72)):
        m = 1000
        while m < 5 * 10**6:
            s2 = s2_of_m(m)
            lhs = math.exp(-(m / math.pi - 1) / 4730)
            rhs = s2 ** -1.5 / (2 * min(m, s2))
            if lhs <= rhs:
                break
            m = int(m * 1.02) + 1
        print(f"  {tag}: (V) first holds at m ~ {m:.3g}  (draft quotes 'm >~ 2.5e5')")

    print("(f) 'b2 <= 27/m for s2 >= lambda/2': value of m * b2 at s2 = lambda/2")
    for m in (30, 50, 100):
        s2 = m * (m - 1) * (2 * m + 5) / 144
        b2m = 18 * 2.61e-4 * (m + 1) ** 5 / s2**2 * m
        print(f"  m={m}: m*b2 = {b2m:.2f}  ({'<= 27 OK' if b2m <= 27 else '> 27 FALSE'})")

    print("(g) 'm <= 0.01 (m+1)^{r+1}/(r+1)' at r = 3:")
    for m in range(4, 11):
        rhs = 0.01 * (m + 1) ** 4 / 4
        print(f"  m={m}: 0.01(m+1)^4/4 = {rhs:.3f}  "
              f"{'OK' if m <= rhs else 'FALSE'}")

    print("(h) untruncated geometric E[U^2] at lam = 1/2:")
    q = math.exp(-0.5)
    eu2 = q * (1 + q) / (1 - q) ** 2
    print(f"  E U^2 = {eu2:.4f}  (draft says 6.31); forcing m > {2000/eu2:.1f}"
          "  (draft says m > 316)")

    print("(i) T.4 crude-clause chain constant S_4/(m^2 lambda) (chain needs <= 12):")
    for m in (2, 3, 4):
        S4 = sum(j**4 for j in range(1, m + 1))
        lamb = m * (m - 1) * (2 * m + 5) / 72
        print(f"  m={m}: {S4/(m*m*lamb):.2f}")
    # direct check of the clause itself at m = 2, w = pi:
    lam = math.pi / 2
    p = math.exp(-lam) / (1 + math.exp(-lam))
    s2 = p * (1 - p)   # only the j=2 factor has variance
    lamb = 0.25
    print(f"  DIRECT m=2, w=pi: deficit = {1 - s2/lamb:.4f} <= pi^2/20 = "
          f"{math.pi**2/20:.4f} : {1 - s2/lamb <= math.pi**2/20}"
          "  (clause TRUE; the displayed chain only proves it for m >= 3)")

    print("(j) NC-T10c slack range from this rerun:")
    pairs = [(0.7838, 9.729e-05), (0.9955, 1.262e-03),
             (0.6143, 1.447e-08), (0.9911, 1.981e-06)]
    slacks = sorted(b / v for b, v in pairs)
    print(f"  slacks = {['%.3g' % s for s in slacks]}  (draft SS6 quotes '24x-4e7x';"
          " actual min is ~789x -- misquote, conservative direction)")

    print("(k) T.9'' displayed constants, recomputed at 50 digits:")
    mp.mp.dps = 50
    z7 = mp.zeta(7)
    c1 = 2 * mp.mpf("1.01") * z7 / (7 * 8 * (2 * mp.pi) ** 7)
    print(f"  first-term r=7 coeff = 1/{mp.nstr(1/c1, 8)}  (draft: 1/1.063e7)")
    c1t = c1 / mp.mpf("0.2686")
    print(f"  after tail division   = 1/{mp.nstr(1/c1t, 8)}  (draft: >= 1/2.8e6:"
          f" {1/c1t >= 2.8e6})")
    z4 = mp.zeta(4)
    c2 = 2 * mp.mpf("1.01") * z4 / (4 * 5 * (2 * mp.pi) ** 4) / mp.mpf("0.2686")
    print(f"  low-order coeff       = {mp.nstr(c2, 8)}  (draft: 2.61e-4;"
          f" claim valid iff true <= 2.61e-4: {c2 <= mp.mpf('2.61e-4')})")
    tr = mp.sqrt(2) * 31 / 60
    print(f"  term ratio at m=30    = {mp.nstr(tr, 8)}  (draft bound 0.7314:"
          f" {tr <= mp.mpf('0.7314')})")
    print(f"  kappa_3^2 dimensional const 72^3/284^2 = {72**3/284**2:.3f}"
          "  (draft: 4.6)")

    print("(l) T.9''a adversarial extension: r = 11..14, lam in {5, 10}, m = 10")
    ZETA = {r: float(mp.zeta(r)) for r in range(11, 15)}

    def factor_cumulants(j, lam, R):
        w = [(-lam * i).exp() for i in range(j)]
        z = sum(w)
        mom = [D(1)] + [sum((D(i) ** p if i else D(0)) * w[i]
                            for i in range(j)) / z for p in range(1, R + 1)]
        kap = [D(0)] * (R + 1)
        for n in range(1, R + 1):
            s = mom[n]
            for k in range(1, n):
                s -= math.comb(n - 1, k - 1) * kap[k] * mom[n - k]
            kap[n] = s
        return kap

    worst = 0.0
    m10 = 10
    for lam_s in ("5", "10"):
        tot = [D(0)] * 15
        for j in range(1, m10 + 1):
            kj = factor_cumulants(j, D(lam_s), 14)
            for r in range(1, 15):
                tot[r] += kj[r]
        for r in range(11, 15):
            Sr = sum(j**r for j in range(1, m10 + 1))
            bound = 2 * math.factorial(r - 1) * ZETA[r] * (Sr + m10) / (2 * math.pi) ** r
            worst = max(worst, abs(float(tot[r])) / bound)
    print(f"  max |kappa_r|/bound = {worst:.4f}  (<= 1: {worst <= 1})")
    ok_report &= worst <= 1

    print(f"\nREF-MISC overall: fine-grid/extension checks all consistent"
          f" ({'no violations' if ok_report else 'VIOLATIONS FOUND'});"
          " the itemized hand-arithmetic findings are reported above inline.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
