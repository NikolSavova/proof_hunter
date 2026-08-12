#!/usr/bin/env python3
# sl3p_nc3_split.py — Wave-4 SL3' ROUTE-FINDER, numeric check 3.
# (a) E.6 large-lam per-j domination with tau^2-normalized slack
#     [F(lam)-F(x)]/tau^2  (the correct small-tau invariant: as tau -> 0,
#     F -> tau^2 (1-2 gamma) h + O(tau^4) and h is strictly decreasing, so
#     the normalized slack tends to (1-2 gamma)[h(lam)-h(x)] > 0).
# (b) W7 regime-split budget: continuum-route requirement
#     delta*(W7) >= K1*lam_split^2 + V/m at m = 401.
import math

def Ff(x, tau, gam):
    s = math.sin(tau*x/2); sh = math.sinh(x/2)
    return math.log(1 + s*s/(sh*sh)) - 2*gam*tau*tau*(x*x/4)/(sh*sh)

print("== sl3p_nc3: E.6 normalized slack + W7 split budget ==")
gam = 0.32
for lam_lo in (0.25, 0.30):
    worst = None
    for tau in [0.05*k for k in range(2, 17)]:      # tau in {0.10, ..., 0.80}
        lam = lam_lo
        while lam <= 0.891:
            Flam = Ff(lam, tau, gam)
            x = 2*lam
            while x <= 60.0:
                d = (Flam - Ff(x, tau, gam))/(tau*tau)
                if worst is None or d < worst[0]:
                    worst = (d, lam, tau, x)
                x += 0.005
            lam += 0.01
    print("E.6 min [F(lam)-F(x)]/tau^2, lam in [%.2f,0.89]: %+.6f at "
          "lam=%.2f tau=%.2f x=%.3f  (%s)"
          % (lam_lo, worst[0], worst[1], worst[2], worst[3],
             "PASS (>0)" if worst[0] > 0 else "FAIL"))
print("small-tau limit of normalized slack at (lam, x)=(0.30, 0.60): "
      "(1-2*0.32)*(h(0.3)-h(0.6)) = %+.6f"
      % (0.36*((0.15**2/math.sinh(0.15)**2) - (0.3**2/math.sinh(0.3)**2))))
K1, V = 0.01920, 0.1901
for ls in (0.30, 0.35):
    need = K1*ls*ls + V/401
    print("W7 split budget, lam_split=%.2f: delta*(W7)=0.08511 vs "
          "K1*lam_split^2 + V/401 = %.5f  (headroom %.0fx)"
          % (ls, need, 0.08511/need))

# consumer impact: honest kernel-weighted mid entry (SL4' §5.3 shape)
# mid' = sqrt(2/pi) A^{3/2} e^{-gamma A/4} (1 + 2/(gamma A)) / (2 gamma)
print()
print("consumer impact: SL4' honest mid' at A0 = c_A(W)*401:")
for nm, A0, gs in [("W1", 0.28*401, 0.42), ("W4", 0.52*401, 0.40),
                   ("W5", 0.60*401, 0.38), ("W7", 0.80*401, 0.32)]:
    for gam in ([0.42, 0.1317] if nm == "W1" else [gs]):
        mid = (math.sqrt(2/math.pi)*A0**1.5*math.exp(-gam*A0/4)
               * (1 + 2/(gam*A0))/(2*gam))
        print("  %s A0=%.2f gamma=%.4f: exp(-gamma*A0/4)=e^-%.2f=%.3e"
              "  mid' = %.4g" % (nm, A0, gam, gam*A0/4,
                                 math.exp(-gam*A0/4), mid))
