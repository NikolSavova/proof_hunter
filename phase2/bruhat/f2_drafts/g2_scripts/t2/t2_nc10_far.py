"""NC-T10: Lemma T.7c — small-tilt far-region bound, and its honest thresholds.

Lemma T.7c (proved in the draft): for |w| = |lam| m <= K and
t_1 = sqrt(2) pi/m <= |t| <= pi, m >= 64:

    |phi_lam(t)| <= exp( - 0.06 e^{-2K} m ) .

Ingredients checked here:
  (a) grid certificate:  1 - |F_j(t)|^2 >= 0.35  for all j >= 2, jt >= 2.8,
      |t| <= pi  (scan j = 2..512 and j in {1000, 5000}; min and argmin reported);
  (b) counting: #{j <= m : jt >= 2.8} >= 0.35 m on [t_1, pi] for m >= 64
      (worst case t = t_1: 1 - 2.8/(m t_1) = 1 - 0.6302 = 0.3698, minus lattice 1);
  (c) direct check of the T.7c bound at m in {30, 60}, w in {1, 3};
  (d) honest threshold: smallest m for which the far bucket
      16 sqrt(2pi) (1.05 m^3/36)^{3/2} exp(-0.06 e^{-2K} m) <= 0.2/m^2
      (the g1_draft_b-style superpoly criterion), reported for K = 1, 2, 4.

stdlib only. Run: python3 t2_nc10_far.py
"""
import math, sys

def Fj2(j, t):
    s = math.sin(t/2)
    if s == 0: return 1.0
    return (math.sin(j*t/2)/(j*s))**2

def nu_mod2(j, lam, t):
    num = (-math.expm1(-lam*j))**2 + 4*math.exp(-lam*j)*math.sin(j*t/2)**2
    zj = (-math.expm1(-lam*j))/(-math.expm1(-lam))
    den = zj*zj*((-math.expm1(-lam))**2 + 4*math.exp(-lam)*math.sin(t/2)**2)
    return num/den

def main():
    ok = True
    print("NC-T10 (a): cert  1-|F_j|^2 >= 0.35 on jt >= 2.8, t <= pi")
    mn = 10.0; arg = None
    for j in list(range(2, 513)) + [1000, 5000]:
        t0 = 2.8/j
        if t0 > math.pi: continue
        for i in range(6000):
            t = t0 + (math.pi-t0)*i/5999
            v = 1 - Fj2(j, t)
            if v < mn: mn, arg = v, (j, t)
    print(f"  min = {mn:.4f} at j={arg[0]}, t={arg[1]:.4f}  (>= 0.35: {mn >= 0.35})")
    ok &= mn >= 0.35

    print("NC-T10 (b): count >= 0.35 m on [t_1, pi]")
    okb = True
    for m in (64, 100, 200, 1000):
        t1 = math.sqrt(2)*math.pi/m
        worst = min(sum(1 for j in range(1, m+1) if j*(t1 + (math.pi-t1)*i/200) >= 2.8)
                    for i in range(201))
        okb &= worst >= 0.35*m
        print(f"  m={m}: min count = {worst}  (0.35m = {0.35*m:.0f})")
    ok &= okb

    print("NC-T10 (c): T.7c bound directly, m in {30,60}, w in {1,3}")
    for m in (30, 60):
        t1 = math.sqrt(2)*math.pi/m
        for w in (1.0, 3.0):
            lam = w/m
            bound = math.exp(-0.06*math.exp(-2*w)*m)
            mx = 0.0
            for i in range(3001):
                t = t1 + (math.pi-t1)*i/3000
                p2 = 1.0
                for j in range(1, m+1):
                    p2 *= nu_mod2(j, lam, t)
                mx = max(mx, math.sqrt(p2))
            print(f"  m={m} w={w}: max|phi| on [t1,pi] = {mx:.3e}  bound = {bound:.4f}"
                  f"  ok = {mx <= bound}")
            ok &= mx <= bound

    print("NC-T10 (d): honest m_2(K) from the proved far exponent")
    for K in (1, 2, 4):
        c = 0.06*math.exp(-2*K)
        m = 100
        while True:
            lhs = 16*math.sqrt(2*math.pi)*(1.05*m**3/36)**1.5*math.exp(-c*m)
            if lhs <= 0.2/m**2: break
            m = int(m*1.05) + 1
            if m > 10**8: break
        print(f"  K={K}: far bucket <= 0.2/m^2 from m_2 ~ {m}"
              f"   (vs g1_draft_b's m_1 = 180; the far exponent is the sole binding constant)")
    print(f"NC-T10 VERDICT: {'PASS' if ok else 'FAIL'} "
          "(thresholds in (d) are reported facts, not pass/fail)")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
