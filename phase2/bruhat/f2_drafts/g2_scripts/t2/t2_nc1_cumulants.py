"""NC-T1: closed forms (2.2)-(2.5) of g2_draft_t2 vs direct exact moment sums.

Checks, in 60-digit Decimal arithmetic:
  (a) mu(lam)      = sum_j [ j g(lam j) - g(lam) ]
      sigma_lam^2  = sum_j [ g'(lam) - j^2 g'(lam j) ]
      kappa_3(lam) = sum_j [ j^3 g''(lam j) - g''(lam) ]
      kappa_4(lam) = sum_j [ g'''(lam) - j^4 g'''(lam j) ]
    against cumulants computed directly from the truncated-geometric weights
    e^{-lam i}, i = 0..j-1 (moment sums + moment->cumulant recursion).
    NOTE: this check certifies the SIGN CONVENTION g''(u) = +u/120 - u^3/1512 + ...,
    g'''(u) = +1/120 - u^2/504 + ... (the draft's first-pass series display had
    these two signs flipped; formulas (2.2)-(2.5) themselves are correct).
  (b) untilted limits: mu(0)=N/2, sigma_0^2=lambda, kappa_3(0)=0,
      kappa_4(0) = -(S_4-m)/120.
  (c) Lemma T.1(ii) tilt invariance of r(k), EXACT rational arithmetic
      (theta = 3/5), m = 12.

stdlib only. Run: python3 t2_nc1_cumulants.py
"""
from decimal import Decimal, getcontext
from fractions import Fraction
import math, os, sys

getcontext().prec = 60

D = Decimal

def g0(u):
    e = u.exp()
    return 1/u - 1/(e-1)

def g1(u):
    e = u.exp()
    return -1/(u*u) + e/((e-1)**2)

def g2(u):
    e = u.exp()
    return 2/(u**3) - e*(e+1)/((e-1)**3)

def g3(u):
    e = u.exp()
    return -6/(u**4) + e*(e*e+4*e+1)/((e-1)**4)

def closed_cumulants(m, lam):
    mu = D(0); var = D(0); k3 = D(0); k4 = D(0)
    gl, g1l, g2l, g3l = g0(lam), g1(lam), g2(lam), g3(lam)
    for j in range(1, m+1):
        u = lam*j
        mu  += j*g0(u) - gl
        var += g1l - j*j*g1(u)
        k3  += j**3*g2(u) - g2l
        k4  += g3l - j**4*g3(u)
    return mu, var, k3, k4

def weight_cumulants(m, lam):
    """Cumulants of X = sum_j U_j^{lam} from the weights directly."""
    tot = [D(0)]*5
    for j in range(1, m+1):
        w = [(-lam*i).exp() for i in range(j)]
        z = sum(w)
        mom = [sum((D(1) if p == 0 else D(i)**p)*w[i] for i in range(j))/z
               for p in range(5)]  # raw moments (0^0 := 1)
        # raw moments -> cumulants (standard recursion)
        k = [D(0)]*5
        k[1] = mom[1]
        k[2] = mom[2] - mom[1]**2
        k[3] = mom[3] - 3*mom[1]*mom[2] + 2*mom[1]**3
        k[4] = (mom[4] - 4*mom[3]*mom[1] - 3*mom[2]**2
                + 12*mom[2]*mom[1]**2 - 6*mom[1]**4)
        for r in range(1,5):
            tot[r] += k[r]
    return tot[1], tot[2], tot[3], tot[4]

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
    print("NC-T1 (a): closed forms vs direct weight cumulants (60-digit Decimal)")
    worst = D(0); worst_at = None
    for m in (10, 30):
        for lam_s in ("0.001","0.01","0.1","0.5"):
            lam = D(lam_s)
            c = closed_cumulants(m, lam)
            w = weight_cumulants(m, lam)
            for name, a, b in zip(("mu","var","k3","k4"), c, w):
                denom = abs(b) if abs(b) > 0 else D(1)
                rel = abs(a-b)/denom
                if rel > worst: worst, worst_at = rel, (m, lam_s, name)
            print(f"  m={m:3d} lam={lam_s:6s}  mu={float(c[0]):.6f} var={float(c[1]):.6f}"
                  f" k3={float(c[2]):.6e} k4={float(c[3]):.6e}")
    print(f"  max relative discrepancy: {float(worst):.3e} at {worst_at}")
    # 60 working digits; g'''(u) = -6/u^4 + ... at u = 1e-3 cancels ~14 digits,
    # so genuine agreement shows up as ~1e-44 relative. Threshold 1e-40.
    ok_a = worst < D("1e-40")

    print("NC-T1 (b): untilted limits (lam -> 0 via lam = 1e-8, vs exact)")
    ok_b = True
    for m in (10, 30):
        lam = D("1e-8")
        mu, var, k3, k4 = closed_cumulants(m, lam)
        N = m*(m-1)//2
        lamb = Fraction(m*(m-1)*(2*m+5), 72)
        S4 = sum(j**4 for j in range(1, m+1))
        k4ex = Fraction(-(S4-m), 120)
        e1 = abs(mu - D(N)/2); e2 = abs(var - D(lamb.numerator)/D(lamb.denominator))
        e3 = abs(k3); e4 = abs(k4 - D(k4ex.numerator)/D(k4ex.denominator))
        print(f"  m={m}: |mu-N/2|={float(e1):.2e} |var-lambda|={float(e2):.2e}"
              f" |k3|={float(e3):.2e} |k4+S4*/120|={float(e4):.2e}")
        # linear-in-lam drift expected ~ lam * scale; scales: var~m^3, k3'~m^4, ...
        ok_b &= e1 < D("1e-2") and e2 < D("1e-1") and e3 < D("1e-1") and e4 < D(1)
    print(f"  (limits approached at the expected O(lam) rate: {ok_b})")

    print("NC-T1 (c): tilt invariance of r(k), exact rationals, m=12, theta=3/5")
    m = 12; a = mahonian(m); th = Fraction(3,5)
    ok_c = True
    for k in range(1, len(a)-1):
        r0 = Fraction(a[k]*a[k], a[k-1]*a[k+1])
        tk = [Fraction(a[k+d])*th**(k+d) for d in (-1,0,1)]
        r1 = tk[1]*tk[1]/(tk[0]*tk[2])
        if r0 != r1: ok_c = False
    print(f"  exact equality at every interior k: {ok_c}")

    verdict = ok_a and ok_b and ok_c
    print(f"NC-T1 VERDICT: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1

if __name__ == "__main__":
    sys.exit(main())
