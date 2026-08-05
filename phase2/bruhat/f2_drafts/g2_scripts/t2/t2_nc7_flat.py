"""NC-T7: ledger NC-9 reproduced and extended (tilted flatness).

For m in {30, 40, 50}: sigma_lam^2 (r(k) - 1) with lam = lam(k) solved from the
exact tilted row (mu(lam) = k), across the bulk; reproduces the merged draft's
NC-9 values at m = 30 (k = 216, 210, 200, 160, 120, 40, 5) and reports the
bulk flatness band vs 1 - B_m on |w| <= 4 for each m.

numpy + stdlib. Run: python3 t2_nc7_flat.py
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

def lam_of_k(la, ks, k):
    lo, hi = -5.0, 50.0
    for _ in range(120):
        mid = 0.5*(lo+hi)
        if tilt_stats(la, ks, mid)[0] > k: lo = mid
        else: hi = mid
    return 0.5*(lo+hi)

def main():
    ok = True
    for m in (30, 40, 50):
        a = mahonian(m); N = m*(m-1)//2
        la = np.array([math.log(x) for x in a]); ks = np.arange(N+1, dtype=float)
        lamvar = m*(m-1)*(2*m+5)/72.0
        S4 = sum(j**4 for j in range(1, m+1))
        Bm = (S4-m)/240.0/lamvar**2
        if m == 30:
            print("NC-T7: NC-9 reproduction, m=30 (ledger: 0.9648 0.9647 0.9646"
                  " 0.9631 0.9615 0.9669 0.9677)")
            vals = []
            for k in (216, 210, 200, 160, 120, 40, 5):
                lam = lam_of_k(la, ks, k)
                _, s2 = tilt_stats(la, ks, lam)
                rm1 = float(Fraction(a[k]*a[k], a[k-1]*a[k+1]) - 1)
                vals.append(s2*rm1)
            print("  reproduced:", " ".join(f"{v:.4f}" for v in vals))
            ref = [0.9648, 0.9647, 0.9646, 0.9631, 0.9615, 0.9669, 0.9677]
            ok &= all(abs(v-r) < 6e-4 for v, r in zip(vals, ref))
        # flatness band on |w| <= 4
        lo_v, hi_v = 10.0, -10.0
        for k in range(1, N//2+1):
            lam = lam_of_k(la, ks, k)
            if abs(lam*m) > 4: continue
            _, s2 = tilt_stats(la, ks, lam)
            rm1 = float(Fraction(a[k]*a[k], a[k-1]*a[k+1]) - 1)
            v = s2*rm1
            lo_v, hi_v = min(lo_v, v), max(hi_v, v)
        print(f"  m={m}: on |w|<=4, sigma_lam^2(r-1) in [{lo_v:.4f}, {hi_v:.4f}]"
              f"  (1 - B_m = {1-Bm:.4f}); band width {hi_v-lo_v:.4f}")
        ok &= hi_v - lo_v < 6.0/m**2 + Bm*8  # width <= B_m*w^2/2 span + m^-2 room
    print(f"NC-T7 VERDICT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
