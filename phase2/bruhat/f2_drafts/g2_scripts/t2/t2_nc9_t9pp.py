"""NC-T9: Lemma T.9'' (tilted 6th-order model remainder) — proof verification.

The lemma proved in the draft (route: partial fractions
  g(u) = 1/2 - sum_{n>=1} [ 1/(u - 2 pi i n) + 1/(u + 2 pi i n) ] ,
so |g^{(r)}(u)| <= 2 r! zeta(r+1)/(2pi)^{r+1} for ALL real u):

  (a) uniform cumulant bound, every real lam, r >= 3:
        |kappa_r(lam)| <= 2 (r-1)! zeta(r) (S_r + m) / (2pi)^r          (T.9''a)
      checked for r = 3..10, m in {10, 30}, lam in {0.01, 0.1, 0.5, 1, 3}
      (60-digit Decimal, per-factor moment->cumulant recursion).
  (b) 6th-order remainder, |t| <= t_1 = sqrt(2) pi/m, m >= 30, all real lam:
        R_7(t) := log phi_lam^c(t) - sum_{r=2}^{6} kappa_r (it)^r / r!
        |R_7(t)| <= (m+1)^8 |t|^7 / 2.8e6                               (T.9''b)
      checked at m = 30, lam in {0.01, 0.1, 0.5, 2}, t in [t_1/8, t_1]
      (double-precision complex; bound >> 1e-12 float noise on this range).
  (c) low-order corollary (used to extend T.8's core to |t| <= t_1):
        |log phi_lam^c(t) + s2 t^2/2 + i kappa_3 t^3/6| <= 2.61e-4 (m+1)^5 t^4
      same range.

numpy-free, stdlib only. Run: python3 t2_nc9_t9pp.py
"""
from decimal import Decimal, getcontext
import cmath, math, sys

getcontext().prec = 60
D = Decimal
ZETA = {3: 1.2020569031595943, 4: 1.0823232337111382, 5: 1.0369277551433699,
        6: 1.0173430619844491, 7: 1.0083492773819228, 8: 1.0040773561979443,
        9: 1.0020083928260822, 10: 1.0009945751278181}

def comb(n, k):
    return math.comb(n, k)

def factor_cumulants(j, lam, R):
    """kappa_1..kappa_R of U_j^{lam} (Decimal), moment->cumulant recursion."""
    w = [(-lam*i).exp() for i in range(j)]
    z = sum(w)
    mom = [D(1)] + [sum((D(i)**p if i else D(0))*w[i] for i in range(j))/z
                    for p in range(1, R+1)]
    kap = [D(0)]*(R+1)
    for n in range(1, R+1):
        s = mom[n]
        for k in range(1, n):
            s -= comb(n-1, k-1)*kap[k]*mom[n-k]
        kap[n] = s
    return kap

def total_cumulants(m, lam, R):
    tot = [D(0)]*(R+1)
    for j in range(1, m+1):
        kj = factor_cumulants(j, lam, R)
        for r in range(1, R+1):
            tot[r] += kj[r]
    return tot

def main():
    ok = True
    print("NC-T9 (a): uniform cumulant bound (T.9''a), r = 3..10")
    worst = 0.0; wat = None
    for m in (10, 30):
        Sr = {r: sum(j**r for j in range(1, m+1)) for r in range(3, 11)}
        for lam_s in ("0.01", "0.1", "0.5", "1", "3"):
            kap = total_cumulants(m, D(lam_s), 10)
            for r in range(3, 11):
                bound = 2*math.factorial(r-1)*ZETA[r]*(Sr[r]+m)/(2*math.pi)**r
                ratio = abs(float(kap[r]))/bound
                if ratio > worst: worst, wat = ratio, (m, lam_s, r)
    print(f"  max |kappa_r|/bound = {worst:.4f} at (m, lam, r) = {wat}")
    ok &= worst <= 1.0

    print("NC-T9 (b): remainder bound (T.9''b) at m = 30, t in [t_1/8, t_1]")
    m = 30; t1 = math.sqrt(2)*math.pi/m
    for lam_s in ("0.01", "0.1", "0.5", "2"):
        lam = float(lam_s)
        kap = [float(x) for x in total_cumulants(m, D(lam_s), 6)]
        mu = kap[1]
        def logphi_c(t):
            s = 0j
            for j in range(1, m+1):
                zj = sum(math.exp(-lam*i) for i in range(j))
                nu = sum(cmath.exp((1j*t-lam)*i) for i in range(j))/zj
                muj = sum(i*math.exp(-lam*i) for i in range(j))/zj
                s += cmath.log(nu*cmath.exp(-1j*t*muj))
            return s
        r7max = 0.0; r4max = 0.0
        for i in range(1, 81):
            t = t1/8 + (t1 - t1/8)*i/80
            lp = logphi_c(t)
            model6 = sum(kap[r]*(1j*t)**r/math.factorial(r) for r in range(2, 7))
            R7 = abs(lp - model6)
            r7max = max(r7max, R7/((m+1)**8*t**7/2.8e6))
            lo = abs(lp + kap[2]*t*t/2 + 1j*kap[3]*t**3/6)
            r4max = max(r4max, lo/(2.61e-4*(m+1)**5*t**4))
        print(f"  lam={lam_s}: max |R_7|/bound = {r7max:.4f}   "
              f"(c) low-order max ratio = {r4max:.4f}")
        ok &= r7max <= 1.0 and r4max <= 1.0
    print(f"NC-T9 VERDICT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
