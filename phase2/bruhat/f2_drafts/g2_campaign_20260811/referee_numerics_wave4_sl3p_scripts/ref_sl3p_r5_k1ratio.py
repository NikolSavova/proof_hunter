# ref_sl3p_r5_k1ratio.py — NUMERICS REFEREE, wave4_sl3p. Pin down the TRUE
# sup of (F(0)-F(lam))/(K1' tau^2 lam^2) on (0,0.3] x (0,0.8], g* = 0.32
# (draft §3 comments "true ratio <= 0.355"; script A's grid gave 0.35419;
# referee random probe found 0.35675 — locate the sup and its boundary).
import numpy as np
from mpmath import mp, mpf, log, sin, sinh, limit

mp.dps = 30
g = 0.32; K1 = (1.65 - 1.98*g)/12.0

def ratio(lam, tau):
    F0 = np.log1p(tau**2) - 2*g*tau**2
    Fl = (np.log1p(np.sin(tau*lam/2)**2/np.sinh(lam/2)**2)
          - 2*g*tau**2*(lam/2)**2/np.sinh(lam/2)**2)
    return (F0 - Fl)/(K1*tau**2*lam**2)

# dense edge-focused grids
best = (0, None)
for lam in np.concatenate([np.geomspace(1e-7, 0.01, 2000),
                           np.arange(0.01, 0.3000001, 0.0001)]):
    taus = np.concatenate([np.geomspace(1e-7, 0.01, 500),
                           np.arange(0.01, 0.8000001, 0.0005)])
    r = ratio(lam, taus)
    k = int(np.nanargmax(r))
    if r[k] > best[0]:
        best = (float(r[k]), (float(lam), float(taus[k])))
print("dense scan: max ratio = %.6f at (lam, tau) = %s" % best)

# the lam->0, tau->0 analytic limit: F(0)-F(lam) ~ tau^2 lam^2 [(tau^2+1)/12
#  - 2 g/12]  /(K1 tau^2 lam^2) -> (1 - 2g)/(12 K1) as tau->0
print("analytic lam,tau->0 limit: (1-2g)/(12*K1) = %.6f" % ((1-2*g)/(12*K1)))
# tau->0, lam=0.3 edge and tau=0.8, lam->0 edge via mpmath
lam = mpf("0.3")
def r_mp(lam, tau):
    F0 = log(1+tau**2) - 2*mpf(str(g))*tau**2
    Fl = (log(1 + sin(tau*lam/2)**2/sinh(lam/2)**2)
          - 2*mpf(str(g))*tau**2*(lam/2)**2/sinh(lam/2)**2)
    return (F0 - Fl)/(mpf(str(K1))*tau**2*lam**2)
for lv, tv in [("0.3", "1e-6"), ("1e-6", "1e-6"), ("1e-6", "0.8"), ("0.3", "0.8")]:
    print("  ratio(lam=%s, tau=%s) = %s" % (lv, tv, mp.nstr(r_mp(mpf(lv), mpf(tv)), 6)))
