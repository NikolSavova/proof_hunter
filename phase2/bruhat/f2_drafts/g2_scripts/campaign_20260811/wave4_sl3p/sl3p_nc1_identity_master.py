#!/usr/bin/env python3
# sl3p_nc1_identity_master.py — Wave-4 SL3' ROUTE-FINDER, numeric check 1.
# (a) Lemma E.1 (exact log-modulus identity) vs direct O(m^2) termwise cf
#     summation (independent computational path).
# (b) finite-m achieved mid-exponent gamma_ach(m, w, tau) at band edges,
#     worst measured points, and larger m; master-inequality slack at gamma*.
# gamma_ach(m,w,tau) := sum_j [g(lam,tau lam)-g(j lam,tau j lam)]
#                       / (2 tau^2 sum_j [h(lam)-h(j lam)])
# with g(x,y) = log(1+sin^2(y/2)/sinh^2(x/2)), h(x) = (x/2)^2/sinh^2(x/2).
# SL3'(W) at t = tau*lam  <=>  gamma_ach >= gamma*(W).
import time
from mpmath import mp, mpf, mpc, sin, sinh, log, exp, fabs

mp.dps = 25

BANDS = [("W1", 4.0, 5.0, "0.42"), ("W2", 5.0, 6.0, "0.42"),
         ("W3", 6.0, 8.0, "0.40"), ("W4", 8.0, 10.0, "0.40"),
         ("W5", 10.0, 20.0, "0.38"), ("W6b", 20.0, 40.0, "0.34"),
         ("W7", 40.0, float("inf"), "0.32")]

def band_of(w):
    for nm, lo, hi, gs in BANDS:
        if lo < w <= hi:
            return nm, mpf(gs)
    raise ValueError(w)

def g(x, y):
    s = sin(y/2)
    return log(1 + s*s/sinh(x/2)**2)

def h(x):
    return (x/2)**2/sinh(x/2)**2 if x != 0 else mpf(1)

def sums(m, w, tau):
    """Sg = sum_j [g(lam,t)-g(jlam,jt)], Sh = sum_j [h(lam)-h(jlam)], t=tau*lam."""
    lam = mpf(w)/m
    t = tau*lam
    glam, hlam = g(lam, t), h(lam)
    Sg = Sh = mpf(0)
    for j in range(2, m+1):          # j=1 term is identically 0
        Sg += glam - g(j*lam, j*t)
        Sh += hlam - h(j*lam)
    return lam, t, Sg, Sh

def logphi_direct(m, lam, t):
    """log|phi| by direct termwise summation of each factor's finite series."""
    q = exp(-lam); qe = q*exp(mpc(0, 1)*t)
    logP = mpf(0)
    s = mpc(0, 0); term = mpc(1, 0)
    for j in range(1, m+1):
        s += term                    # s = sum_{i=0}^{j-1} (q e^{it})^i
        term *= qe
        logP += log((1-q)/(1-q**j)*abs(s))
    return logP

print("== sl3p_nc1: (a) Lemma E.1 identity check (independent path, dps=%d) ==" % mp.dps)
for (m, w, taus) in [(401, "4.05", "0.8"), (401, "4.05", "0.5"),
                     (401, "356.89", "0.8"), (401, "20.0", "0.65")]:
    tau = mpf(taus); lam = mpf(w)/m; t = tau*lam
    _, _, Sg, _ = sums(m, w, tau)
    lp = logphi_direct(m, lam, t)
    rel = fabs(Sg - (-2*lp))/fabs(Sg)
    print("  m=%d w=%s tau=%s: -2log|phi|=%s  identity=%s  rel.err=%.3e"
          % (m, w, taus, mp.nstr(-2*lp, 12), mp.nstr(Sg, 12), float(rel)))

print()
print("== (b) finite-m achieved mid-exponent gamma_ach; min over tau in {0.3,0.5,0.65,0.75,0.8} ==")
print("%-6s %-8s %-4s %5s | %-9s at tau | ratio  | slack@gamma* (min over tau)" %
      ("m", "w", "band", "g*", "gamma_min"))
TAUS = [mpf(x) for x in ("0.3", "0.5", "0.65", "0.75", "0.8")]
PTS = [(401, "4.05"), (401, "4.5"), (401, "5.0"), (401, "5.05"), (401, "6.0"),
       (401, "6.05"), (401, "8.0"), (401, "8.05"), (401, "10.0"), (401, "10.05"),
       (401, "20.0"), (401, "20.05"), (401, "40.0"), (401, "40.05"), (401, "45.0"),
       (401, "120.0"), (401, "356.89"),
       (2000, "4.05"), (2000, "5.0"), (2000, "10.0"), (2000, "20.0"),
       (2000, "40.0"), (2000, "45.0"), (2000, "100.0"),
       (20000, "5.0"), (20000, "20.0"), (20000, "40.0"), (20000, "45.0")]
t0 = time.time()
worst_ratio = None
for (m, ws) in PTS:
    w = float(ws)
    nm, gstar = band_of(w)
    gmin, targ, smin = None, None, None
    for tau in TAUS:
        _, _, Sg, Sh = sums(m, ws, tau)
        gam = Sg/(2*tau**2*Sh)
        slack = Sg - 2*gstar*tau**2*Sh
        if gmin is None or gam < gmin:
            gmin, targ = gam, tau
        if smin is None or slack < smin:
            smin = slack
    ratio = gmin/gstar
    if worst_ratio is None or ratio < worst_ratio[0]:
        worst_ratio = (ratio, m, ws, nm)
    print("%-6d %-8s %-4s %5s | %.6f  %4s  | %.4f | %+.5f  %s" %
          (m, ws, nm, mp.nstr(gstar, 3), float(gmin), mp.nstr(targ, 3),
           float(ratio), float(smin), "PASS" if smin > 0 else "FAIL"))
print("worst ratio gamma_min/gamma* over all points: %.4f at m=%d w=%s (%s)"
      % (float(worst_ratio[0]), worst_ratio[1], worst_ratio[2], worst_ratio[3]))
print("total time %.1f s" % (time.time()-t0))
