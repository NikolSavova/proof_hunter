"""NC-T4: Lemma T.5 — variance lower bound along the mean curve.

  (a) (**): for ANY nonincreasing weight vector on {0,...,j-1},
        Var U >= (E U)^2/3 + (E U)/3 ,
      exact Fraction arithmetic, adversarial random staircases + structured
      cases (uniform = equality case, near-degenerate, geometric-like).
  (b) (T.5-final): sigma_{lam(k)}^2 >= (k/6)(1 + k/m) for every interior
      k <= N/2, m in {30, 60}; lam(k) solved by bisection on mu(lam) = k.
      Reports min_k ratio (float; slack is ~2x so double precision suffices;
      per-factor formulas evaluated in overflow-safe / series-switched form).

stdlib only. Run: python3 t2_nc4_varlower.py
"""
from fractions import Fraction
import math, random, sys

def g(u):
    if u < 1e-3:
        return 0.5 - u/12 + u**3/720 - u**5/30240
    if u > 500:
        return 1.0/u
    return 1.0/u - math.exp(-u)/(-math.expm1(-u))

def qf(u):  # q(u) = -g'(u) > 0
    if u < 1e-3:
        return 1.0/12 - u*u/240 + u**4/6048
    if u > 500:
        return 1.0/(u*u)
    em = math.exp(-u); om = -math.expm1(-u)
    return 1.0/(u*u) - em/(om*om)

def mu(m, lam):
    gl = g(lam)
    return sum(j*g(lam*j) - gl for j in range(1, m+1))

def sig2(m, lam):
    ql = qf(lam)
    return sum(j*j*qf(lam*j) - ql for j in range(1, m+1))

def var_mean_frac(w):
    z = sum(w)
    m1 = sum(Fraction(i)*w[i] for i in range(len(w)))/z
    m2 = sum(Fraction(i*i)*w[i] for i in range(len(w)))/z
    return m2 - m1*m1, m1

def main():
    ok = True
    print("NC-T4 (a): (**) on nonincreasing weights, exact Fractions")
    random.seed(20260805)
    worst = None
    trials = 0
    cases = []
    for j in (2, 3, 5, 8, 12):
        cases.append([Fraction(1)]*j)                     # uniform (equality)
        cases.append([Fraction(1)] + [Fraction(1, 10**6)]*(j-1))  # near-degenerate
        cases.append([Fraction(2, 3)**i for i in range(j)])       # geometric
        for _ in range(400):                              # random staircases
            steps = sorted((random.randint(0, 100) for _ in range(j)), reverse=True)
            if steps[0] == 0: steps[0] = 1
            cases.append([Fraction(s + 1) for s in steps])
    for w in cases:
        trials += 1
        var, m1 = var_mean_frac(w)
        margin = var - m1*m1/3 - m1/3
        if margin < 0:
            ok = False
            print("   VIOLATION:", w)
        if worst is None or margin < worst[0]:
            worst = (margin, len(w))
    print(f"  {trials} weight vectors, min margin Var - (EU)^2/3 - EU/3 ="
          f" {float(worst[0]):.3e} (>= 0; equality at uniform)  ok={ok}")

    print("NC-T4 (b): (T.5-final) sigma_lam(k)^2 >= (k/6)(1+k/m)")
    for m in (30, 60):
        N = m*(m-1)//2
        ratios = []
        for k in range(1, N//2 + 1):
            lo, hi = 1e-9, 200.0           # mu decreasing: mu(lo)~N/2, mu(hi)~0
            for _ in range(200):
                mid = 0.5*(lo+hi)
                if mu(m, mid) > k: lo = mid
                else: hi = mid
            lam = 0.5*(lo+hi)
            s2 = sig2(m, lam)
            bound = (k/6.0)*(1 + k/m)
            ratios.append(s2/bound)
        mn = min(ratios)
        print(f"  m={m}: min_k sigma_lam^2 / [(k/6)(1+k/m)] = {mn:.4f}  "
              f"{'ok' if mn >= 1 else 'FAIL'}")
        ok &= mn >= 1
    print(f"NC-T4 VERDICT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
