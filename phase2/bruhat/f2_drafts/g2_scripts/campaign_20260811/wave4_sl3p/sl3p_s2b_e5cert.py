# sl3p_s2b_e5cert.py — Stage-2 SL3': Certificate E.5.3, per-band monotone-cell
# lower bounds on delta_norm(w,tau) := [log(1+tau^2) - avg_g(w,tau)]/tau^2
#                                      - 2 gamma* (1 - avg_h(w)),
# for w in band, tau in (0, 0.8]. Small tau (tau <= tau_c'(W)) is covered
# ANALYTICALLY by Lemma E.5.2: delta_norm >= (1-avg_h(w))(1/(1+tau^2)-2gamma*).
# Cells cover [tau_start(W), 0.8] x band. Cell bound (all rigorous directions):
#   delta_norm >= [log(1+tau1^2) - Ag_ub(w1c, tau2)]/tau2^2 - 2g*(1-Ah_lb(w2c))
# using: avg_g decreasing in w (Lemma E.5.1), psi_tau <= psi_tau2 on x<=pi/tau2,
# psi_tau <= min(tau2^2 h, 1/sinh^2(x/2)) beyond, left-Riemann upper sums for
# decreasing integrands, right-Riemann lower sums for h. Budget target:
#   b(W) = K1'(g*) lam_max(W)^2 + eps_hat + 2 g*/401 ,  eps_hat = 6.25e-4.
# PASS iff certified min delta_norm >= b(W). Output: out_sl3p_s2b.txt. 2026-08-12.
import numpy as np

D = 0.001                      # quadrature step (grid-aligned with w edges)
XMAX = 40.0
xs = np.arange(0, int(round(XMAX/D))+1)*D
xs0 = xs.copy(); xs0[0] = 1.0  # avoid 0-division; values at 0 set explicitly
sh2 = np.sinh(xs0/2.0)**2
hgrid = (xs0/2.0)**2/sh2; hgrid[0] = 1.0
cum_h_left  = np.concatenate([[0.0], np.cumsum(hgrid[:-1])*D])   # >= int_0^{kD} h
cum_h_right = np.concatenate([[0.0], np.cumsum(hgrid[1:])*D])    # <= int_0^{kD} h

def idx(w): return int(round(w/D))

def Ah_ub(w):   # upper bound on avg_h(w), w = grid multiple
    return cum_h_left[idx(w)]/w
def Ah_lb(w):
    return cum_h_right[idx(w)]/w

def Ag_ub_array(tau2):
    """cum left-sum array for g_ub(x; tau2) (decreasing majorant of every
    log(1+psi_tau), tau<=tau2, valid at all w after Lemma E.5.1)."""
    xstar = np.pi/tau2
    psi2 = np.sin(tau2*xs0/2.0)**2/sh2
    cap = np.minimum(tau2**2*hgrid, 1.0/sh2)
    ps = np.where(xs <= xstar, psi2, cap)
    ps[0] = tau2**2
    gub = np.log1p(ps)
    return np.concatenate([[0.0], np.cumsum(gub[:-1])*D])        # >= int_0^{kD} g_ub

K1p = lambda g: (1.65 - 1.98*g)/12.0
EPS_HAT = 6.25e-4
DTAU = 0.0025

# name, w1, w2 (None = unbounded), gamma*, lam_max, w-cell step
BANDS = [("W1", 4.0, 5.0, 0.42, 5/401, 0.005),
         ("W2", 5.0, 6.0, 0.42, 6/401, 0.005),
         ("W3", 6.0, 8.0, 0.40, 8/401, 0.010),
         ("W4", 8.0, 10.0, 0.40, 10/401, 0.010),
         ("W5", 10.0, 20.0, 0.38, 20/401, 0.020),
         ("W6b", 20.0, 40.0, 0.34, 40/401, 0.040),
         ("W7", 40.0, None, 0.32, 0.30, None)]

print("=== SL3' Stage 2, script B: Certificate E.5.3 (per-band cells) ===")
print(f"quadrature step D={D}, tau-cell width {DTAU}; eps_hat={EPS_HAT}")
print("band  gamma*  b(W)      q(W)     tau_c'   tau_start  cells(w x tau)  min delta_cert  ratio  PASS")
allpass = True
rows = []
for name, w1, w2, gam, lmax, dw in BANDS:
    b = K1p(gam)*lmax**2 + EPS_HAT + 2*gam/401.0
    q = 1.0 - Ah_ub(w1)          # lower bound of (1-avg_h(w)) over band
    tauc2 = 1.0/(2*gam + b/q) - 1.0
    tauc = np.sqrt(tauc2)
    tau_start = np.floor((tauc - 0.005)/DTAU)*DTAU
    # analytic check at tau_start (covers tau <= tau_start):
    ana = q*(1.0/(1.0+tau_start**2) - 2*gam)
    assert ana >= b, (name, ana, b)
    tedges = np.arange(tau_start, 0.8 + 1e-12, DTAU)
    if tedges[-1] < 0.8 - 1e-12: tedges = np.append(tedges, 0.8)
    if w2 is None:
        wl = np.array([w1]); wr = None
        ahl = np.array([0.0])            # 1-avg_h(w) <= 1
    else:
        nw = int(round((w2-w1)/dw))
        wl = w1 + np.arange(nw)*dw; wr = wl + dw
        ahl = np.array([Ah_lb(v) for v in wr])
    wlix = np.array([idx(v) for v in wl])
    dmin = 9e9; loc = None
    for i in range(len(tedges)-1):
        t1, t2 = tedges[i], tedges[i+1]
        cg = Ag_ub_array(t2)
        Ag = cg[wlix]/wl
        num = np.log1p(t1**2) - Ag
        assert num.min() > 0
        dc = num/t2**2 - 2*gam*(1.0 - ahl)
        j = int(np.argmin(dc))
        if dc[j] < dmin: dmin, loc = float(dc[j]), (float(wl[j]), t1, t2)
    ok = dmin >= b; allpass &= ok
    rows.append((name, gam, b, dmin))
    print(f"{name:4s}  {gam:.2f}   {b:.6f}  {q:.5f}  {tauc:.4f}   {tau_start:.4f}   "
          f"{len(wl)}x{len(tedges)-1}      {dmin:.6f}   {dmin/b:5.2f}x  {'PASS' if ok else 'FAIL'}  worst cell (w1c,t1,t2)={loc}")
print(f"ALL BANDS PASS: {allpass}")
print()
print("E.7 small-lam budget recap (delta_cert vs b(W) = K1' lam_max^2 + eps_hat + 2gamma*/401):")
for name, gam, b, dmin in rows:
    print(f"  {name:4s}: certified delta_norm >= {dmin:.6f} >= b = {b:.6f}  (headroom {dmin/b:.2f}x)")
print("=== end script B ===")
