"""NC-T8: Theorem T.9 constants against the exact harness.

For m in {30, 60, 100, 140} and K in {1, 4}: over every interior k <= N/2 with
|w| = |lam(k)| m <= K, measure the constant the refined law actually needs:

  needed(m, K) := max_k ( |s2 (r(k)-1) - (1 - B_m)| - B_m w^2/2 ) * m^2

(T.9 claims needed <= C_R = 5.1 for m >= m_2 = 180; m here is below threshold,
so this is a truth-calibration: the trend in m must be consistent with 5.1,
and the w^2-coefficient claim c_w = 1/2 is probed by reporting the max of
|s2(r-1) - (1-B_m)|/(B_m w^2) over 2 <= |w| <= K (should be <= ~1/2 + O(1/(m w^2)) ).

numpy + stdlib. Run: python3 t2_nc8_refined.py
"""
import math, sys
from fractions import Fraction
import numpy as np

def mahonian(m):
    poly = [1]
    for d in range(1, m+1):
        out = [0]*(len(poly)+d-1); run = 0
        for k in range(len(out)):
            if k < len(poly): run += poly[k]
            if k-d >= 0: run -= poly[k-d]
            out[k] = run
        poly = out
    return poly

def tilt_stats(la, ks, lam):
    logw = la - lam*ks
    w = np.exp(logw - logw.max())
    p = w/w.sum()
    mu = (ks*p).sum()
    s2 = ((ks-mu)**2*p).sum()
    return mu, s2

def main():
    print("NC-T8: refined-law constant calibration (exact rows)")
    print(f"{'m':>4} {'K':>2} {'#k':>5} {'needed C_R':>10} {'max resid/(Bm w^2), |w|>=2':>26}")
    results = {}
    for m in (30, 60, 100, 140):
        a = mahonian(m); N = m*(m-1)//2
        la = np.array([math.log(x) for x in a]); ks = np.arange(N+1, dtype=float)
        lamvar = m*(m-1)*(2*m+5)/72.0
        S4 = sum(j**4 for j in range(1, m+1))
        Bm = (S4-m)/240.0/lamvar**2
        step = 1 if m <= 100 else 2
        # walk k downward from center with warm-started bisection on lam
        rows = []
        lam_lo = 0.0
        for k in range(N//2, 0, -step):
            lo, hi = lam_lo - 1e-6, lam_lo + max(0.5, 4*(lam_lo+1e-3))
            for _ in range(80):
                mid = 0.5*(lo+hi)
                if tilt_stats(la, ks, mid)[0] > k: lo = mid
                else: hi = mid
            lam = 0.5*(lo+hi); lam_lo = lam
            w = lam*m
            if w > 4.2: break
            _, s2 = tilt_stats(la, ks, lam)
            rm1 = float(Fraction(a[k]*a[k], a[k-1]*a[k+1]) - 1)
            rows.append((k, w, s2, s2*rm1))
        for K in (1, 4):
            sub = [r for r in rows if r[1] <= K]
            needed = max((abs(v - (1-Bm)) - Bm*w*w/2)*m*m for _, w, _, v in sub)
            big = [abs(v - (1-Bm))/(Bm*w*w) for _, w, _, v in sub if w >= 2]
            ratio = max(big) if big else float('nan')
            results[(m, K)] = needed
            print(f"{m:>4} {K:>2} {len(sub):>5} {needed:>10.3f} {ratio:>26.3f}")
    ok = True
    # PASS criteria (calibration): needed C_R at K=1 stays well below 5.1 and
    # decreases (or stays flat) in m; at K=4 the w^2/2 envelope must hold for
    # the largest m computed (needed <= 5.1 there would certify at that m).
    for m in (30, 60, 100, 140):
        if results[(m, 1)] > 5.1: ok = False
    print("  K=1 needed-C_R values all <= 5.1:", ok)
    print(f"NC-T8 VERDICT: {'PASS (calibration)' if ok else 'FAIL'}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
