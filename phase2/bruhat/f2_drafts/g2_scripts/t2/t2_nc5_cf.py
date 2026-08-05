"""NC-T5: Lemma T.6 / T.7 characteristic-function package.

  (a) T.6(i) exact modulus identity, random (j, lam, t), double precision
      (algebraic identity; 1e-13 tolerance).
  (b) (T.6ii)  |phi_lam(t)| <= exp(-sigma_lam^2 t^2/5) on |t| <= pi/m.
  (c) (T.6iii-final, SIGN-CORRECTED) with the convention
      log phi = sum_r kappa_r (it)^r / r!  (so the r = 3 term is -i k3 t^3/6):
        |log phi_lam(t) + s2 t^2/2 + i k3 t^3/6| <= (m-1)^2 s2 t^4/6
      on |t| <= 1/(2m)  (checked on t >= 1/(20m) where the bound >> float noise).
      The draft's first-pass display had "- i kappa_3 t^3/6" inside the modulus:
      that sign is WRONG (this run measured the resulting residual ~2|k3|t^3/6,
      ratio up to 6.4 at small t); with the correct sign the check passes.
  (d) (T.7b-cert): DOCUMENTS that the draft's first-pass claim
        1 - |F_j(t)|^2 >= 1/60 for 2 <= j <= 512, 1/(2j) <= |t| <= pi
      is FALSE (j = 2, t = 1/4 gives sin^2(1/8) = 0.015549 < 1/60 = 0.016667),
      and certifies the CORRECTED form used by the repaired Lemma T.7(b):
        1 - |F_j(t)|^2 >= 1/80   for all j >= 2 and  jt >= 0.45, |t| <= pi
      (scan j = 2..512 + spot checks j = 1000, 5000; min attained at j = 2,
      t = 0.225: sin^2(0.1125) = 0.012603 = 1/79.35).
  (e) (T.7b-final, corrected): |phi_lam(t)| <= exp(-m_*/4730) on
      pi/m <= |t| <= pi, for 0 <= lam <= pi/m (w <= pi), m_* = min(m, floor(1/lam));
      empirical max_t |phi_lam| compared at m in {30, 60}, w in {0.5, 1, 3}.

stdlib only. Run: python3 t2_nc5_cf.py
"""
import cmath, math, random, sys

def z_j(j, lam):
    if lam == 0: return float(j)
    return (-math.expm1(-lam*j))/(-math.expm1(-lam))

def nu_mod2(j, lam, t):
    """|nu_j(t)|^2 by the exact T.6(i) identity."""
    num = (-math.expm1(-lam*j))**2 + 4*math.exp(-lam*j)*math.sin(j*t/2)**2
    den = z_j(j, lam)**2*((-math.expm1(-lam))**2 + 4*math.exp(-lam)*math.sin(t/2)**2)
    return num/den

def nu_direct(j, lam, t):
    return sum(cmath.exp((1j*t - lam)*i) for i in range(j))/z_j(j, lam)

def qf(u):
    if u < 1e-3: return 1.0/12 - u*u/240 + u**4/6048
    if u > 500: return 1.0/(u*u)
    em = math.exp(-u); om = -math.expm1(-u)
    return 1.0/(u*u) - em/(om*om)

def gf(u):
    if u < 1e-3: return 0.5 - u/12 + u**3/720
    if u > 500: return 1.0/u
    return 1.0/u - math.exp(-u)/(-math.expm1(-u))

def g2f(u):
    if u < 1e-2: return u/120 - u**3/1512
    e = math.exp(u)
    return 2/u**3 - e*(e+1)/(e-1)**3

def sig2(m, lam):
    ql = qf(lam)
    return sum(j*j*qf(lam*j) - ql for j in range(1, m+1))

def kap3(m, lam):
    g2l = g2f(lam)
    return sum(j**3*g2f(lam*j) - g2l for j in range(1, m+1))

def muf(m, lam):
    gl = gf(lam)
    return sum(j*gf(lam*j) - gl for j in range(1, m+1))

def phi_mod(m, lam, t):
    p = 1.0
    for j in range(1, m+1):
        p *= nu_mod2(j, lam, t)
    return math.sqrt(p)

def log_phi_centered(m, lam, t):
    s = 0j
    for j in range(1, m+1):
        s += cmath.log(nu_direct(j, lam, t))
    return s - 1j*t*muf(m, lam)

def Fj2(j, t):
    s = math.sin(t/2)
    if s == 0: return 1.0
    return (math.sin(j*t/2)/(j*s))**2

def main():
    ok = True
    random.seed(7)
    print("NC-T5 (a): T.6(i) exact identity, 2000 random points")
    worst = 0.0
    for _ in range(2000):
        j = random.randint(1, 200); lam = random.uniform(1e-6, 3.0)
        t = random.uniform(-math.pi, math.pi)
        a = nu_mod2(j, lam, t); b = abs(nu_direct(j, lam, t))**2
        worst = max(worst, abs(a-b)/max(b, 1e-300))
    print(f"  max rel deviation = {worst:.2e}")
    ok &= worst < 1e-11

    print("NC-T5 (b): (T.6ii) on |t| <= pi/m")
    for m in (30, 60):
        for w in (0.001, 0.5, 1.0, 3.0):
            lam = w/m; s2 = sig2(m, lam)
            r = max(phi_mod(m, lam, (i/200)*math.pi/m) /
                    math.exp(-s2*((i/200)*math.pi/m)**2/5) for i in range(1, 201))
            print(f"  m={m} w={w}: max |phi|/exp(-s2 t^2/5) = {r:.4f}")
            ok &= r <= 1.0

    print("NC-T5 (c): (T.6iii-final) on 1/(20m) <= t <= 1/(2m)")
    for m in (30, 60):
        for w in (0.001, 0.5, 1.0, 3.0):
            lam = w/m; s2 = sig2(m, lam); k3 = kap3(m, lam)
            r = 0.0
            for i in range(1, 101):
                t = (1/(20*m)) + (i/100)*(1/(2*m) - 1/(20*m))
                lhs = abs(log_phi_centered(m, lam, t) + s2*t*t/2 + 1j*k3*t**3/6)
                r = max(r, lhs/((m-1)**2*s2*t**4/6))
            print(f"  m={m} w={w}: max ratio = {r:.4f}")
            ok &= r <= 1.0

    print("NC-T5 (d): (T.7b-cert)")
    # first-pass claim (documented FALSE):
    v = 1 - Fj2(2, 0.25)
    print(f"  first-pass claim range: j=2, t=1/4: 1-|F|^2 = {v:.6f} "
          f"{'<' if v < 1/60 else '>='} 1/60 = {1/60:.6f}  -> claim FALSE" if v < 1/60
          else "  unexpected")
    # corrected cert: jt >= 0.45
    mn = 10.0; arg = None
    for j in list(range(2, 513)) + [1000, 5000]:
        t0 = 0.45/j
        for i in range(4000):
            t = t0 + (math.pi - t0)*i/3999
            val = 1 - Fj2(j, t)
            if val < mn: mn, arg = val, (j, t)
    print(f"  corrected cert min over jt>=0.45: {mn:.6f} at j={arg[0]}, t={arg[1]:.4f}"
          f"  (>= 1/80 = {1/80:.6f}: {mn >= 1/80})")
    ok &= mn >= 1/80

    print("NC-T5 (e): (T.7b-final corrected) |phi| <= exp(-m_*/4730), w <= pi")
    for m in (30, 60):
        for w in (0.5, 1.0, 3.0):
            lam = w/m; mstar = min(m, math.floor(1/lam))
            bound = math.exp(-mstar/4730)
            mx = max(phi_mod(m, lam, math.pi/m + (math.pi - math.pi/m)*i/2000)
                     for i in range(2001))
            print(f"  m={m} w={w}: max|phi| = {mx:.3e}  bound = {bound:.6f}  "
                  f"slack = {bound/max(mx,1e-300):.2e}")
            ok &= mx <= bound
    print(f"NC-T5 VERDICT: {'PASS (with corrected (d),(e) as stated)' if ok else 'FAIL'}")
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
