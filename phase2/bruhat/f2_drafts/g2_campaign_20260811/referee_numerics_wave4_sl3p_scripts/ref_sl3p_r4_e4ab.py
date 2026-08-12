# ref_sl3p_r4_e4ab.py — NUMERICS REFEREE, wave4_sl3p. Direct verification of
# the two discretization lemmas as INEQUALITIES (not their proof steps):
#  (a) E.4a:  sum_{j=1}^m F(j lam) <= (1/lam) Int_0^w F + 2 g* tau^2
#                                     + m * 1.03 e^{-2 pi/tau}
#      at adversarial (m, w, tau, gamma*) incl. lam = 0.3 (W7 split edge),
#      band tops, small tau, both gamma extremes.  mpmath quad with arch
#      subdivision; slack printed.
#  (b) E.4b:  F(0) - F(lam) <= K1'(g*) tau^2 lam^2, K1' = (1.65-1.98 g*)/12,
#      corner checks at lam = 0.3 / tau = 0.8 (mpmath dps 30) + off-grid
#      random numpy grid (10^6 points per gamma).
#  (c) constant audit: 4.04*(1/4 + 1/401) vs the draft's "= 1.0202" print.
import numpy as np
from mpmath import mp, mpf, quad, log, sin, sinh, exp, pi

mp.dps = 30

def gmp(x, tau): return log(1 + sin(tau*x/2)**2/sinh(x/2)**2)
def hmp(x): return (x/2)**2/sinh(x/2)**2 if x != 0 else mpf(1)
def Fmp(x, tau, g): return gmp(x, tau) - 2*g*tau**2*hmp(x)

print("== ref_sl3p_r4: E.4a / E.4b direct inequality checks ==")
print("(a) E.4a slack = RHS - sum  (must be >= 0):")
CASES = [(401, "4.05", "0.8", "0.42"), (401, "4.05", "0.3", "0.42"),
         (401, "4.05", "0.8", "0.32"), (401, "5.0", "0.42", "0.42"),
         (401, "20.0", "0.8", "0.38"), (401, "40.0", "0.65", "0.34"),
         (401, "120.3", "0.8", "0.32"), (401, "120.3", "0.73", "0.32"),
         (401, "120.3", "0.05", "0.32"), (2000, "20.0", "0.8", "0.38"),
         (1000, "300.0", "0.8", "0.32")]
allok = True
for m, ws, ts, gs in CASES:
    w, tau, g = mpf(ws), mpf(ts), mpf(gs)
    lam = w/m
    S = sum(Fmp(j*lam, tau, g) for j in range(1, m+1))
    arch = pi/tau
    top = min(w, mpf(80))
    pts = [mpf(0)] + [k*arch for k in range(1, int(top/arch)+1) if k*arch < top] + [top]
    I = quad(lambda x: Fmp(x, tau, g) if x != 0 else log(1+tau**2) - 2*g*tau**2, pts)
    if w > top:
        I += quad(lambda x: Fmp(x, tau, g), [top, w])
    RHS = I/lam + 2*g*tau**2 + m*mpf("1.03")*exp(-2*pi/tau)
    sl = RHS - S
    ok = sl >= 0; allok &= ok
    print("  m=%-5d w=%-7s tau=%-5s g*=%s: sum = %s  RHS = %s  slack = %s  %s"
          % (m, ws, ts, gs, mp.nstr(S, 8), mp.nstr(RHS, 8), mp.nstr(sl, 6),
             "PASS" if ok else "FAIL"))
print("E.4a all cases PASS: %s" % allok)

print()
print("(b) E.4b corner + random off-grid:")
rng = np.random.default_rng(20260812)
for gs in ["0.32", "0.34", "0.38", "0.40", "0.42"]:
    g = mpf(gs); K1 = (mpf("1.65") - mpf("1.98")*g)/12
    # corner lam = 0.3, tau = 0.8 (worst measured direction)
    corner = (log(1+mpf("0.64")) - 2*g*mpf("0.64")) - Fmp(mpf("0.3"), mpf("0.8"), g)
    bnd = K1*mpf("0.64")*mpf("0.09")
    # random grid
    lamr = rng.uniform(1e-6, 0.3, 1000000); taur = rng.uniform(1e-6, 0.8, 1000000)
    gf = float(g); K1f = float(K1)
    F0 = np.log1p(taur**2) - 2*gf*taur**2
    Fl = (np.log1p(np.sin(taur*lamr/2)**2/np.sinh(lamr/2)**2)
          - 2*gf*taur**2*(lamr/2)**2/np.sinh(lamr/2)**2)
    ratio = (F0 - Fl)/(K1f*taur**2*lamr**2)
    print("  g*=%s: corner (0.3,0.8): F(0)-F(lam) = %s <= K1' t^2 l^2 = %s "
          "(ratio %s); random 1e6 max ratio = %.5f  PASS=%s"
          % (gs, mp.nstr(corner, 6), mp.nstr(bnd, 6), mp.nstr(corner/bnd, 4),
             float(ratio.max()), bool(ratio.max() <= 1.0)))

print()
c = 4.04*(0.25 + 1.0/401)
print("(c) 4.04*(1/4 + 1/401) = %.6f  (draft prints '= 1.0202'; true value "
      "1.020075 -> the '=' is a round-UP; <= 1.03 used in eps_env: %s)"
      % (c, c <= 1.03))
print("== end r4 ==")
