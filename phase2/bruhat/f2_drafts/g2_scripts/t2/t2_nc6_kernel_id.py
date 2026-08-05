"""NC-T6: (T.8a) complex kernel identity at the tilted mean.

For m = 12, k in {12, 20, 28} (interior, lam(k) > 0), with lam solved from
mu(lam) = k (bisection, ~1e-13):

  D := P_lam(X=k)^2 - P_lam(X=k-1) P_lam(X=k+1)      [exact tilted row]
     = (1/4pi^2) intint_{[-pi,pi]^2} phi(s) phi(t) (1 - cos(s-t)) ds dt   [(T.8a)]

and  P_{k-1}P_{k+1} = (1/4pi^2) intint phi(s) phi(t) cos(s-t) ds dt ,

phi = centered tilted cf (complex; kappa_3 != 0). The double integral is done by
2-D trapezoid on a 1024^2 grid — phi is a trigonometric polynomial of degree
N = 66, so trapezoid with > 2N+1 nodes is exact up to roundoff; any residual
mismatch is the (mu - k) ~ 1e-13 centering error. numpy + stdlib.

Run: python3 t2_nc6_kernel_id.py
"""
import math, sys
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

def main():
    m = 12
    a = np.array(mahonian(m), dtype=float)
    N = len(a) - 1
    ks = np.arange(N+1, dtype=float)
    ok = True
    print("NC-T6: (T.8a) at the tilted mean, m = 12 (N = %d)" % N)
    for k in (12, 20, 28):
        lo, hi = 1e-12, 50.0
        for _ in range(200):
            mid = 0.5*(lo+hi)
            wgt = a*np.exp(-mid*ks)
            if (ks*wgt).sum()/wgt.sum() > k: lo = mid
            else: hi = mid
        lam = 0.5*(lo+hi)
        wgt = a*np.exp(-lam*ks); Z = wgt.sum()
        p = wgt/Z
        mu = (ks*p).sum()
        D_row = p[k]**2 - p[k-1]*p[k+1]
        PP_row = p[k-1]*p[k+1]

        M = 1024
        t = -math.pi + 2*math.pi*np.arange(M)/M          # periodic trapezoid
        phi = (p[None, :]*np.exp(1j*np.outer(t, ks - mu))).sum(axis=1)
        F = np.outer(phi, phi)
        SmT = t[:, None] - t[None, :]
        w2 = (2*math.pi/M)**2
        D_int = (F*(1 - np.cos(SmT))).sum()*w2/(4*math.pi**2)
        PP_int = (F*np.cos(SmT)).sum()*w2/(4*math.pi**2)
        e1 = abs(D_int.real - D_row)/abs(D_row)
        e2 = abs(PP_int.real - PP_row)/abs(PP_row)
        e3 = abs(D_int.imag) + abs(PP_int.imag)
        print(f"  k={k:2d} lam={lam:.6f} |mu-k|={abs(mu-k):.1e}: "
              f"rel dev D = {e1:.2e}, P-P+ = {e2:.2e}, imag = {e3:.1e}")
        ok &= e1 < 1e-9 and e2 < 1e-9 and e3 < 1e-12
    print(f"NC-T6 VERDICT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
