# ref_sl3p_r3_e6_probe.py — NUMERICS REFEREE, wave4_sl3p. Adversarial probes of
# Certificate E.6 (W7 termwise domination) + fp grid-edge audit + reproduction
# of the draft's recorded d-lam = 0.002 coarse-grid FAIL (honesty note, §5.2).
#  (a) off-grid fine scan of F(lam) - F(x) over [0.30,0.89] x [0.58,0.8] x
#      [2 lam, 7.85] with irrational-offset grids (nothing shared with the
#      cell edges); global min must be > 0; corner (0.30, 0.58) resolved fine.
#  (b) tail: max F(x) on x in [7.85, 60] x tau-grid vs eps_t; min F(lam) on
#      the B-region vs eps_t (independent fine grid).
#  (c) Part A condition C: continuous margin on an off-grid lam scan.
#  (d) small-tau side: direct F(lam)-F(x) >= 0 for tau <= 0.58 off-grid.
#  (e) fp arange edge audit for scripts B and C grids.
#  (f) coarse d-lam = 0.002 Part-B rerun: does it FAIL as recorded?
import numpy as np

GAM = 0.32
def h(x):  return (x/2.0)**2/np.sinh(x/2.0)**2
def F(x, tau):
    return np.log1p(np.sin(tau*x/2.0)**2/np.sinh(x/2.0)**2) - 2*GAM*tau**2*h(x)

print("== ref_sl3p_r3: E.6 adversarial probes ==")
# ---- (a) off-grid scan, tau in [0.58, 0.8] ----
d1, d2, d3 = 0.00097, 0.00113, 0.00351   # irrational-ish offsets/steps
lams = np.arange(0.30, 0.89 + 1e-12, d1); lams[-1] = 0.89
taus = np.arange(0.58, 0.80 + 1e-12, d2); taus[-1] = 0.80
gmin = 9e9; gloc = None
for la in lams:
    xs = np.arange(2*la, 7.85 + 1e-12, d3); xs[-1] = 7.85
    Fx = F(xs[None, :], taus[:, None])          # (nt, nx)
    Fl = F(np.array([[la]]), taus[:, None])     # (nt, 1)
    slack = Fl - Fx
    k = int(np.argmin(slack))
    if slack.flat[k] < gmin:
        gmin = float(slack.flat[k])
        gloc = (float(la), float(taus[k // xs.size]), float(xs[k % xs.size]))
print("(a) off-grid scan (%d lam x %d tau x ~%d x): min F(lam)-F(x) = %+.6f at "
      "(lam,tau,x)=(%.5f, %.5f, %.5f)  PASS(>0): %s"
      % (lams.size, taus.size, int((7.85-0.6)/d3), gmin, *gloc, gmin > 0))
# corner refinement near (0.30, 0.58)
la = 0.30
xs = np.arange(0.60, 1.2, 0.0001)
tv = np.arange(0.58, 0.60, 0.0001)
sl = F(np.array([[la]]), tv[:, None]) - F(xs[None, :], tv[:, None])
k = int(np.argmin(sl))
print("    corner refine lam=0.30: min slack = %+.6f at (tau,x)=(%.4f, %.4f)"
      "   [draft's 'true corner slack ~0.004']"
      % (float(sl.flat[k]), float(tv[k // xs.size]), float(xs[k % xs.size])))

# ---- (b) tail vs eps_t ----
eps_t = float(1/np.sinh(3.925)**2)
xs = np.arange(7.85, 60.0, 0.001)
tvs = np.arange(0.0005, 0.8 + 1e-12, 0.0005); tvs[-1] = 0.8
mx = -9e9
for tv in tvs:
    mx = max(mx, float(F(xs, tv).max()))
lam_g = np.arange(0.30, 0.89 + 1e-12, 0.0005); lam_g[-1] = 0.89
tv_g = np.arange(0.58, 0.80 + 1e-12, 0.0005); tv_g[-1] = 0.8
Fl = F(lam_g[None, :], tv_g[:, None])
print("(b) tail: max F(x), x in [7.85,60], all tau <= 0.8: %+.6e  <= eps_t = %.6e: %s"
      % (mx, eps_t, mx <= eps_t))
print("    min F(lam) on [0.30,0.89]x[0.58,0.8] (fine grid): %.6f  >= eps_t: %s  "
      "(draft floor 0.066061)" % (float(Fl.min()), float(Fl.min()) >= eps_t))

# ---- (c) Part A condition C, continuous off-grid ----
T0 = 0.58
la = np.arange(0.30, 0.89 + 1e-12, 1.3e-5); la[-1] = 0.89
lhs = (h(la) - h(2*la))*(1 - 2*GAM - 2*GAM*T0**2)
rhs = h(la)*T0**2*la**2/12.0
r = lhs/rhs
j = int(np.argmin(r))
print("(c) condition C(lam, 0.58) continuous scan: min lhs/rhs = %.4f at lam=%.5f"
      "  (>1: %s)  [cell-certified min was 1.1294]" % (float(r[j]), float(la[j]), r[j] > 1))

# ---- (d) small-tau side off-grid (E.6a conclusion), tau in (0, 0.58] ----
gmin2 = 9e9; gloc2 = None
tv2 = np.arange(0.013, 0.58 + 1e-12, 0.013); tv2[-1] = 0.58
for la in np.arange(0.30, 0.89 + 1e-12, 0.0037):
    xs = np.arange(2*la, 7.85, 0.0071)
    slk = F(np.array([[la]]), tv2[:, None]) - F(xs[None, :], tv2[:, None])
    k = int(np.argmin(slk))
    if slk.flat[k] < gmin2:
        gmin2 = float(slk.flat[k]); gloc2 = (float(la), float(tv2[k // xs.size]), float(xs[k % xs.size]))
print("(d) tau <= 0.58 off-grid scan: min F(lam)-F(x) = %+.3e at (%.4f, %.3f, %.4f)"
      "  PASS(>0): %s" % (gmin2, *gloc2, gmin2 > 0))

# ---- (e) fp arange edge audit ----
print("(e) fp arange top-edge audit:")
for nm, start, step in [("B/W5", 0.55, 0.0025), ("B/W6b", 0.675, 0.0025),
                        ("B/W7", 0.7275, 0.0025)]:
    te = np.arange(start, 0.8 + 1e-12, step)
    print("    script B %-5s: last tau edge = %.17f  (0.8 - last = %.2e; appended-0.8: %s)"
          % (nm, te[-1], 0.8 - te[-1], te[-1] < 0.8 - 1e-12))
teC = np.arange(0.58, 0.80 + 1e-12, 0.0005)
leC = np.concatenate([np.arange(0.30, 0.40, 0.0002),
                      np.arange(0.40, 0.60, 0.0005),
                      np.arange(0.60, 0.89 + 1e-12, 0.001)])
print("    script C: last tau edge = %.17f (0.8 - last = %.2e); last lam edge = %.17f"
      " (0.89 - last = %.2e); n_lam_edges = %d (printed rows = len-1 = %d)"
      % (teC[-1], 0.8 - teC[-1], leC[-1], 0.89 - leC[-1], leC.size, leC.size - 1))
leA = np.arange(0.30, 0.89 + 1e-12, 0.0025)
print("    script C Part A: last lam edge = %.17f (0.89 - last = %.2e)"
      % (leA[-1], 0.89 - leA[-1]))

# ---- (f) coarse d-lam = 0.002 Part-B rerun (draft §5.2 honesty note) ----
X0 = 7.85; DT = 0.0005; GUARD = 1e-6
tedges = np.arange(0.58, 0.80 + 1e-12, DT)
t1 = tedges[:-1][:, None]; t2 = tedges[1:][:, None]
ledges = np.arange(0.30, 0.89 + 1e-12, 0.002)
minslack = 9e9; nfail = 0; floc = None
for i in range(len(ledges)-1):
    la, lb = ledges[i], ledges[i+1]
    xe = np.concatenate([np.arange(2*la, 2*la+0.4, 0.005),
                         np.arange(2*la+0.4, 4.0, 0.01),
                         np.arange(4.0, X0, 0.02), [X0]])
    x1 = xe[:-1][None, :]; x2 = xe[1:][None, :]
    Flb = (np.log1p(np.sin(t1[:, 0]*la/2.0)**2/np.sinh(lb/2.0)**2)
           - 2*GAM*t2[:, 0]**2*h(la))
    a = t1*x1/2.0; bb = t2*x1/2.0
    k = np.ceil((a - np.pi/2)/np.pi)
    crosses = (np.pi/2 + k*np.pi) <= bb
    s2m = np.where(crosses, 1.0, np.maximum(np.sin(a)**2, np.sin(bb)**2))
    psi_ub = np.minimum(s2m/np.sinh(x1/2.0)**2, t2**2*h(x1))
    Fub = np.log1p(psi_ub) - 2*GAM*t1**2*h(x2)
    slack = Flb - Fub.max(axis=1)
    sm = float(slack.min())
    if sm < minslack:
        minslack = sm; floc = (float(la), float(tedges[int(np.argmin(slack))]))
    nfail += int((slack < GUARD).sum())
print("(f) coarse d-lam=0.002 rerun: min cell slack = %+.6f at %s; cells<guard: %d"
      "  -> recorded first-pass FAIL is %s" %
      (minslack, floc, nfail, "REPRODUCED" if nfail > 0 else "NOT reproduced"))
print("== end r3 ==")
