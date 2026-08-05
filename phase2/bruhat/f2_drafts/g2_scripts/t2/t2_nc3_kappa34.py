"""NC-T3: Lemma T.4' third/fourth-cumulant bounds, 60-digit Decimal.

  (a) pointwise kernel bounds on (0, pi] (CORRECTED SIGNS: g'' = +u/120 - ...,
      g''' = +1/120 - ...; the draft's first-pass series display had them flipped):
        |g''(u) - u/120|  <= |u|^3/1500
        |g'''(u) - 1/120| <= u^2/500
  (b) |kappa_3(lam)| <= |w| m^4/284           (m in {30,60}, w grid to pi)
  (c) |kappa_4(lam) + S*_4/120| <= w^2 m^5/2200
  (d) |kappa_4(lam)| <= m^5/480
Reports the actually-attained max ratios (bound sharpness).

stdlib only. Run: python3 t2_nc3_kappa34.py
"""
from decimal import Decimal, getcontext
import sys

getcontext().prec = 60
D = Decimal
PI = D("3.14159265358979323846264338327950288419716939937510582097494")

def g2f(u):
    e = u.exp()
    return 2/(u**3) - e*(e+1)/((e-1)**3)

def g3f(u):
    e = u.exp()
    return -6/(u**4) + e*(e*e+4*e+1)/((e-1)**4)

def kappa34(m, lam):
    g2l, g3l = g2f(lam), g3f(lam)
    k3 = sum(j**3*g2f(lam*j) - g2l for j in range(1, m+1))
    k4 = sum(g3l - j**4*g3f(lam*j) for j in range(1, m+1))
    return k3, k4

def main():
    ok = True
    print("NC-T3 (a): pointwise g'', g''' bounds on (0, pi], 300-point grid")
    r2 = r3 = D(0)
    for i in range(1, 301):
        u = PI*i/300
        r2 = max(r2, abs(g2f(u) - u/120)/(u**3/1500))
        r3 = max(r3, abs(g3f(u) - D(1)/120)/(u*u/500))
    print(f"  max |g''-u/120|/(u^3/1500) = {float(r2):.4f}   "
          f"max |g'''-1/120|/(u^2/500) = {float(r3):.4f}")
    ok &= r2 <= 1 and r3 <= 1

    print("NC-T3 (b,c,d): cumulant bounds, w grid (0, pi], m in {30, 60}")
    rb = rc = rd = D(0)
    for m in (30, 60):
        S4s = sum(j**4 for j in range(1, m+1)) - m
        for i in range(1, 33):
            w = PI*i/32
            lam = w/m
            k3, k4 = kappa34(m, lam)
            rb = max(rb, abs(k3)/(w*D(m)**4/284))
            rc = max(rc, abs(k4 + D(S4s)/120)/(w*w*D(m)**5/2200))
            rd = max(rd, abs(k4)/(D(m)**5/480))
        # d) also at w -> 0 (kappa_4(0) = -S*_4/120 is the max candidate)
        rd = max(rd, (D(S4s)/120)/(D(m)**5/480))
    print(f"  (b) max |k3| /(w m^4/284)        = {float(rb):.4f}")
    print(f"  (c) max |k4+S4*/120|/(w^2m^5/2200)= {float(rc):.4f}")
    print(f"  (d) max |k4| /(m^5/480)          = {float(rd):.4f}  (incl. w=0)")
    ok &= rb <= 1 and rc <= 1 and rd <= 1

    print(f"NC-T3 VERDICT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
