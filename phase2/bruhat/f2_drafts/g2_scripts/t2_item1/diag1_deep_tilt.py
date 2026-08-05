"""Diagnostic (NOT a proof, NOT a PASS/FAIL cert) for G2 item 1: why the far-region
bound (T.7b-final / T.7c) does not extend to lam in (pi/m, 1/2].

Reuses phi_mod/sig2 from ../t2/t2_nc5_cf.py (exact double-precision product
formula for |phi_lam(t)|, via the T.6(i) identity).

Three findings, each reproduced here:

(1) At the near/far boundary t = pi/m itself, |phi_lam(pi/m)| -> 1 as m -> oo
    for FIXED lam > 0 (not the shallow-tilt lam ~ 1/m regime). So no bound of
    the form exp(-c(lam)*m) can hold uniformly on the closed interval
    [pi/m, pi] -- any correct far-region lemma for deep tilt MUST start its
    t-domain strictly above pi/m (or use a lam-dependent threshold that -> pi/m
    only as lam -> 0).

(2) T.6(ii)'s Gaussian bound exp(-sigma_lam^2 t^2/5), which IS proved for all
    lam on |t| <= pi/m, does NOT extend validly beyond pi/m: the ratio
    |phi_lam(t)| / exp(-s2 t^2/5) blows up (super-exponentially) once t leaves
    a shrinking neighborhood of 0. So "just use the same Gaussian bound
    further out" is not a repair route.

(3) T.7c's pairwise-tilt-comparison technique (E_lam sin^2 >= e^{-2 lam(j-1)}
    E_0 sin^2) carries a prefactor e^{-2 lam(j-1)} that is only bounded
    (by e^{-2K}) when lam*m = w <= K is FIXED. For deep tilt (lam = Theta(1),
    so w = Theta(m)), this prefactor is e^{-Theta(m)} -- it kills the bound
    it's trying to prove. This is why T.7c's hypothesis is "|w| <= K", not
    "lam >= c": the technique is small-tilt-only by construction, not
    deep-tilt-capable.

Run: python3 diag1_deep_tilt.py
"""
import math, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "t2"))
from t2_nc5_cf import phi_mod, sig2  # noqa: E402


def finding1():
    print("(1) |phi_lam(pi/m)| as m grows, lam FIXED (deep tilt):")
    for lam in (0.1, 0.3, 0.5):
        row = []
        for m in (30, 100, 300, 1000):
            t = math.pi / m
            row.append(phi_mod(m, lam, t))
        print(f"    lam={lam}: {[f'{v:.4f}' for v in row]}  (m=30,100,300,1000 -- INCREASING toward 1)")


def finding2():
    print("(2) exp(-s2 t^2/5) validity ratio (should be <=1 everywhere if the bound held):")
    for lam, m in ((0.3, 100), (0.5, 300)):
        s2 = sig2(m, lam)
        worst = 0.0
        worst_t = None
        for i in range(1, 2001):
            t = math.pi * i / 2000
            v = phi_mod(m, lam, t)
            exponent = -s2 * t * t / 5
            bound = math.exp(exponent) if exponent > -700 else 0.0
            if bound > 1e-300:
                r = v / bound
                if r > worst:
                    worst, worst_t = r, t
        print(f"    lam={lam} m={m}: worst finite ratio = {worst:.3e} at t={worst_t:.4f} "
              f"(pi/m={math.pi/m:.4f}) -- bound is violated far past pi/m")


def finding3():
    print("(3) T.7c prefactor e^{-2 lam(j-1)} at j=m, deep tilt (w = lam*m):")
    for lam in (0.1, 0.3, 0.5):
        for m in (30, 100, 300):
            w = lam * m
            print(f"    lam={lam} m={m:4d}: w={w:7.1f}  e^{{-2w}} = {math.exp(-2*w):.3e}  "
                  f"(this prefactor multiplies the whole per-factor bound -> useless once w >> 1)")


if __name__ == "__main__":
    finding1()
    finding2()
    finding3()
