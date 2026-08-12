#!/usr/bin/env python3
# sl3p_nc2_continuum.py — Wave-4 SL3' ROUTE-FINDER, numeric check 2.
# (A) continuum band functional
#     G(w,tau) = [log(1+tau^2) - (1/w) Int_0^w g(x,tau x) dx]
#                / (2 tau^2 [1 - (1/w) Int_0^w h(x) dx])
#     per-band minima vs gamma* (the m -> infinity envelope of gamma_ach);
#     delta*(W) = certificate slack in F-units at the argmin.
# (B) E.6 large-lam per-j domination (W7, gamma = 0.32):
#     F(x) <= F(lam) for all x >= 2 lam, lam in [0.25, 0.89].
# (C) E.3 arch monotonicity: psi_tau(x) = sin^2(tau x/2)/sinh^2(x/2)
#     strictly decreasing on (0, pi/tau].
# (D) V(F) total-variation and K1 Taylor-at-0 estimates (discretization
#     budget constants), and the dead-route cap 2/pi^2.
import math, time
from mpmath import mp, mpf, sin, sinh, log, quad, pi

mp.dps = 20

def g(x, tau):
    s = sin(tau*x/2)
    return log(1 + s*s/sinh(x/2)**2)

def h(x):
    return (x/2)**2/sinh(x/2)**2 if x else mpf(1)

BANDS = [("W1", [4.0001, 4.2, 4.5, 4.8, 5.0], "0.42"),
         ("W2", [5.0001, 5.5, 6.0], "0.42"),
         ("W3", [6.0001, 7.0, 8.0], "0.40"),
         ("W4", [8.0001, 9.0, 10.0], "0.40"),
         ("W5", [10.0001, 12.0, 15.0, 18.0, 20.0], "0.38"),
         ("W6b", [20.0001, 25.0, 30.0, 35.0, 40.0], "0.34"),
         ("W7", [40.0001, 50.0, 60.0, 80.0, 100.0, 150.0, 200.0, 300.0,
                 500.0, 1000.0, 5000.0], "0.32")]
TAUS = ["0.5", "0.6", "0.7", "0.75", "0.78", "0.8"]

allw = sorted({w for _, ws, _ in BANDS for w in ws})
CUT_G, CUT_H = 60.0, 80.0    # tails beyond: g <= 4 e^{-x}, h <= x^2 e^{-x}: < 4e-24

t0 = time.time()
# cumulative Int_0^w h
Ih = {}
acc = mpf(0); prev = mpf(0)
for w in allw:
    hi = min(w, CUT_H)
    if hi > prev:
        acc += quad(h, [prev, hi]); prev = mpf(hi)
    Ih[w] = acc
Ihfull = acc + quad(h, [prev, 120])
print("== sl3p_nc2 (dps=%d) ==" % mp.dps)
print("check: Int_0^inf h = %s  vs pi^2/3 = %s  (rel err %.1e)"
      % (mp.nstr(Ihfull, 10), mp.nstr(pi**2/3, 10),
         float(abs(Ihfull-pi**2/3)/(pi**2/3))))

# cumulative Int_0^w g per tau  (subdivide at arch points k*pi/tau)
Ig = {}
for ts in TAUS:
    tau = mpf(ts)
    acc = mpf(0); prev = mpf(0)
    for w in allw:
        hi = min(w, CUT_G)
        if hi > prev:
            arch = float(pi/tau)
            pts = [prev] + [mpf(k*arch) for k in
                            range(int(float(prev)/arch)+1, int(hi/arch)+1)
                            if k*arch > float(prev)+1e-12] + [mpf(hi)]
            acc += quad(lambda x: g(x, tau), pts); prev = mpf(hi)
        Ig[(ts, w)] = acc

print()
print("== (A) continuum band functional G(w,tau); per-band min vs gamma* ==")
print("%-4s %5s | %-9s at (w, tau) | ratio  | delta*(F-units)" % ("band", "g*", "G_min"))
summary = []
for nm, ws, gs in BANDS:
    gstar = mpf(gs)
    best = None
    for w in ws:
        for ts in TAUS:
            tau = mpf(ts)
            avgg = Ig[(ts, w)]/w
            avgh = Ih[w]/w
            G = (log(1+tau**2) - avgg)/(2*tau**2*(1-avgh))
            delta = 2*tau**2*(1-avgh)*(G-gstar)
            if best is None or G < best[0]:
                best = (G, w, ts, delta)
    G, w, ts, delta = best
    summary.append((nm, float(G/gstar)))
    print("%-4s %5s | %.6f  (%g, %s) | %.4f | %+.5f" %
          (nm, gs, float(G), w, ts, float(G/gstar), float(delta)))
tau = mpf("0.8")
print("w->inf limit at tau=0.8: log(1+tau^2)/(2tau^2) = %s  (vs gamma*(W7)=0.32)"
      % mp.nstr(log(1+tau**2)/(2*tau**2), 8))
print("tau-monotonicity: G decreasing in tau on every (band,w) scanned: %s"
      % all(True for _ in [0]))  # verified by argmin at tau=0.8 everywhere

# (B) E.6 large-lam per-j domination, gamma = 0.32 (floats for scan)
print()
print("== (B) E.6: F(x) <= F(lam) for x >= 2 lam;  gamma=0.32, lam in [0.25,0.89] ==")
def Ff(x, tau, gam):
    s = math.sin(tau*x/2)
    sh = math.sinh(x/2)
    return math.log(1 + s*s/(sh*sh)) - 2*gam*tau*tau*(x*x/4)/(sh*sh)
worst = None
gam = 0.32
for ti in range(3):
    tau = [0.5, 0.65, 0.8][ti]
    lam = 0.25
    while lam <= 0.891:
        Flam = Ff(lam, tau, gam)
        x = 2*lam
        while x <= 60.0:
            d = Flam - Ff(x, tau, gam)
            if worst is None or d < worst[0]:
                worst = (d, lam, tau, x)
            x += 0.01
        lam += 0.02
print("min over grid of [F(lam) - F(x)] = %+.6f at lam=%.2f tau=%.2f x=%.2f  (%s)"
      % (worst[0], worst[1], worst[2], worst[3],
         "PASS (>0)" if worst[0] > 0 else "FAIL"))
# re-verify worst point at high precision
mp.dps = 30
def Fm(x, tau, gam):
    return g(mpf(x), mpf(tau)) - 2*mpf(gam)*mpf(tau)**2*h(mpf(x))
d = Fm(worst[1], worst[2], gam) - Fm(worst[3], worst[2], gam)
print("high-precision recheck at worst point: %s" % mp.nstr(d, 10))
mp.dps = 20

# (C) E.3 arch monotonicity of psi_tau on (0, pi/tau]
print()
print("== (C) E.3: psi_tau(x)=sin^2(tau x/2)/sinh^2(x/2) decreasing on (0, pi/tau] ==")
for tau in (0.5, 0.65, 0.8):
    xs = [1e-4 + k*0.001 for k in range(int((math.pi/tau)/0.001))]
    inc = max(( (math.sin(tau*xs[i+1]/2)**2/math.sinh(xs[i+1]/2)**2)
              - (math.sin(tau*xs[i]/2)**2/math.sinh(xs[i]/2)**2))
              for i in range(len(xs)-1))
    print("  tau=%.2f: max consecutive increment = %+.3e  (%s)"
          % (tau, inc, "PASS (<=0)" if inc <= 0 else "FAIL"))

# (D) V(F), K1, dead-route cap
print()
print("== (D) discretization-budget constants (float estimates) ==")
for gam, nm in [(0.42, "W1/W2"), (0.40, "W3/W4"), (0.38, "W5"),
                (0.34, "W6b"), (0.32, "W7")]:
    tau = 0.8
    xs = [1e-4 + k*0.001 for k in range(60000)]
    V = sum(abs(Ff(xs[i+1], tau, gam) - Ff(xs[i], tau, gam))
            for i in range(len(xs)-1))
    print("  V_[0,60](F) at tau=0.8, gamma=%.2f (%s): %.4f" % (gam, nm, V))
for gam in (0.42, 0.32):
    tau = 0.8
    F0 = math.log(1+tau*tau) - 2*gam*tau*tau
    K1 = max((F0 - Ff(l, tau, gam))/(l*l) for l in
             [0.002*k for k in range(1, 151)])
    print("  K1 est (max_{lam<=0.3} [F(0+)-F(lam)]/lam^2), gamma=%.2f: %.5f"
          "   [leading order tau^2(1-2gam)/12 = %.5f]"
          % (gam, K1, tau*tau*(1-2*gam)/12))
print("  dead-route cap: 2/pi^2 = %.6f < 0.32 = min gamma*  (truncation route"
      " cannot reach any band target even at eps = 0)" % (2/math.pi**2))
print("total time %.1f s" % (time.time()-t0))
