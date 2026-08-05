"""NC-T2: Lemma T.4 ingredients, 60-digit Decimal.

  (a) kernel two-sided (T.4a''): with q(u) = 1/u^2 - e^u/(e^u-1)^2 and
      E(u) = (1/12 - q(u))/u^2:
        (1/240)(1 - u^2/19) <= E(u) <= 1/240  on (0, pi], and E decreasing.
      Also records the TRUE values E(1), E(2), E(pi) (the draft's first-pass
      quoted values were wrong; corrected in the draft from this run).
  (b) S*_4 bracket:  m^5/5 <= S_4 - m <= (m^5/5)(1 + 3/m), exact Fractions,
      scan m = 8..5000 + closed-form positivity of the difference polynomials
      (upper difference = m^4/10 - m^3/3 + 31m/30, positive for m >= 4;
       lower difference = m^4/2 + m^3/3 - 31m/30, positive for m >= 2).
  (c) Lemma (T.4) two-sided deficit vs exact closed-form sigma_lam^2:
        0.0285 w^2 (1 - w^2/19) <= 1 - sigma_lam^2/lambda
                                <= 0.0300 w^2 (1 + 3/m + w^2/18)
      at m in {30, 60, 120}, w in {0.1, 0.5, 1, 2, 3}.
  (d) crude clauses: 1 - sigma_lam^2/lambda <= w^2/20 and sigma_lam^2 >= lambda/2
      at w = pi (checked at m = 30, 60, 120).

stdlib only. Run: python3 t2_nc2_kernel.py
"""
from decimal import Decimal, getcontext
from fractions import Fraction
import sys

getcontext().prec = 60
D = Decimal
PI = D("3.14159265358979323846264338327950288419716939937510582097494")

def q(u):
    e = u.exp()
    return 1/(u*u) - e/((e-1)**2)

def E(u):
    return (D(1)/12 - q(u))/(u*u)

def g1(u):  # g'(u)
    e = u.exp()
    return -1/(u*u) + e/((e-1)**2)

def sigma2(m, lam):
    g1l = g1(lam)
    return sum(g1l - j*j*g1(lam*j) for j in range(1, m+1))

def main():
    ok = True
    print("NC-T2 (a): E(u) two-sided on (0, pi], 400-point grid")
    lo_margin = D(10); up_margin = D(10); prev = None; mono = True
    for i in range(1, 401):
        u = PI*i/400
        e = E(u)
        lo = (D(1)/240)*(1 - u*u/19)
        up = D(1)/240
        lo_margin = min(lo_margin, e - lo)
        up_margin = min(up_margin, up - e)
        if prev is not None and e > prev + D("1e-50"):
            mono = False
        prev = e
    print(f"  min (E - lower) = {float(lo_margin):.3e}  min (upper - E) = {float(up_margin):.3e}"
          f"  E decreasing on grid: {mono}")
    print(f"  true values: E(1) = {float(E(D(1))):.8f}  E(2) = {float(E(D(2))):.8f}"
          f"  E(pi) = {float(E(PI)):.8f}   (1/240 = {1/240:.8f})")
    ok &= lo_margin > 0 and up_margin >= 0 and mono

    print("NC-T2 (b): S*_4 bracket, exact, m = 8..5000")
    okb = True
    for m in range(8, 5001):
        S4 = sum(j**4 for j in range(1, m+1))
        lo = Fraction(m**5, 5); up = Fraction(m**5, 5) + Fraction(3*m**4, 5)
        if not (lo <= S4 - m <= up): okb = False; print("   FAIL at m =", m)
    # closed-form differences (exact polynomial identities, checked at m = 8):
    m = 8; S4 = sum(j**4 for j in range(1, m+1))
    up_diff = Fraction(m**4,10) - Fraction(m**3,3) + Fraction(31*m,30)
    lo_diff = Fraction(m**4,2) + Fraction(m**3,3) - Fraction(31*m,30)
    okb &= (Fraction(m**5,5) + Fraction(3*m**4,5) - (S4-m) == up_diff)
    okb &= ((S4-m) - Fraction(m**5,5) == lo_diff)
    print(f"  scan clean: {okb}; difference-polynomial identities verified at m=8;"
          f" both polys positive for m >= 4 (m^4/10 >= m^3/3 for m >= 4).")
    ok &= okb

    print("NC-T2 (c): (T.4) two-sided deficit, closed-form sigma_lam^2")
    okc = True
    for m in (30, 60, 120):
        lamb = D(m*(m-1)*(2*m+5))/72
        for ws in ("0.1","0.5","1","2","3"):
            w = D(ws); lam = w/m
            s2 = sigma2(m, lam)
            defi = 1 - s2/lamb
            lo = D("0.0285")*w*w*(1 - w*w/19)
            up = D("0.0300")*w*w*(1 + D(3)/m + w*w/18)
            good = lo <= defi <= up
            okc &= good
            print(f"  m={m:4d} w={ws:4s}: deficit={float(defi):.6f} "
                  f"in [{float(lo):.6f}, {float(up):.6f}]  {'ok' if good else 'FAIL'}")
    ok &= okc

    print("NC-T2 (d): crude clauses at w = pi")
    okd = True
    for m in (30, 60, 120):
        lamb = D(m*(m-1)*(2*m+5))/72
        s2 = sigma2(m, PI/m)
        defi = 1 - s2/lamb
        good = defi <= PI*PI/20 and s2 >= lamb/2
        okd &= good
        print(f"  m={m:4d}: deficit(w=pi)={float(defi):.6f} <= pi^2/20={float(PI*PI/20):.4f},"
              f" s2/lambda={float(s2/lamb):.4f} >= 0.5  {'ok' if good else 'FAIL'}")
    ok &= okd

    print(f"NC-T2 VERDICT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
