# ref_sl3p_r2_e53_indep.py — NUMERICS REFEREE, wave4_sl3p. Independent rebuild
# of Certificate E.5.3 (script B) with:
#   (1) exact-rational budget b(W) via Fractions (audit of the printed b);
#   (2) an independent cell-certificate implementation at FINER quadrature
#       D = 0.0005 (same cell layout, freshly written code) — certified minima
#       must PASS and land near (>= is expected, sharper quadrature) the
#       draft's numbers;
#   (3) mpmath ground truth: delta_norm(w,tau) evaluated by quadrature at the
#       worst cell's corners for every band — must exceed the certified min
#       (lower-bound property) and quantify the certificate's concession.
from fractions import Fraction as Fr
import numpy as np
from mpmath import mp, mpf, quad, log, sin, sinh, pi

mp.dps = 25

# ---- (1) exact b(W) audit ----
print("== (1) exact-rational b(W) audit:  b = (1.65-1.98g)/12 * lam_max^2 + 1/1600 + 2g/401 ==")
BANDS = [("W1", Fr(21,50), Fr(5,401), 4.0, 5.0, 0.005),
         ("W2", Fr(21,50), Fr(6,401), 5.0, 6.0, 0.005),
         ("W3", Fr(2,5),  Fr(8,401), 6.0, 8.0, 0.010),
         ("W4", Fr(2,5),  Fr(10,401), 8.0, 10.0, 0.010),
         ("W5", Fr(19,50), Fr(20,401), 10.0, 20.0, 0.020),
         ("W6b", Fr(17,50), Fr(40,401), 20.0, 40.0, 0.040),
         ("W7", Fr(8,25),  Fr(3,10),  40.0, None, None)]
DRAFT_B = {"W1": "0.002730", "W2": "0.002735", "W3": "0.002648", "W4": "0.002664",
           "W5": "0.002706", "W6b": "0.003131", "W7": "0.009844"}
DRAFT_MIN = {"W1": 0.036055, "W2": 0.036214, "W3": 0.041498, "W4": 0.028654,
             "W5": 0.032532, "W6b": 0.094264, "W7": 0.078395}
bexact = {}
for nm, g, lmax, *_ in BANDS:
    K1 = (Fr(165,100) - Fr(198,100)*g)/12
    b = K1*lmax**2 + Fr(1,1600) + 2*g/401
    bexact[nm] = b
    print("  %-4s: b = %s = %.9f  (draft prints %s; nearest-6dp of exact = %.6f;"
          " match: %s)" % (nm, b, float(b), DRAFT_B[nm], float(b),
                           ("%.6f" % float(b)) == DRAFT_B[nm]))

# ---- (2) independent finer-quadrature certificate ----
print()
print("== (2) independent E.5.3 rebuild, quadrature D = 0.0005 (draft used 0.001) ==")
D = 0.0005
XMAX = 40.0
n = int(round(XMAX/D))
xs = np.arange(0, n+1)*D
x_safe = xs.copy(); x_safe[0] = 1.0
sh2 = np.sinh(x_safe/2.0)**2
hg = (x_safe/2.0)**2/sh2; hg[0] = 1.0
ch_left = np.concatenate([[0.0], np.cumsum(hg[:-1])*D])    # >= int h
ch_right = np.concatenate([[0.0], np.cumsum(hg[1:])*D])    # <= int h
def ix(w): return int(round(w/D))
DTAU = 0.0025
allpass = True
print("band  b(W)      tau_start  min_delta_cert   draft_min   diff      PASS")
worst_cells = {}
for nm, gfr, lmaxfr, w1, w2, dw in BANDS:
    g = float(gfr); b = float(bexact[nm])
    q = 1.0 - ch_left[ix(w1)]/w1
    tauc = np.sqrt(1.0/(2*g + b/q) - 1.0)
    tau_start = np.floor((tauc - 0.005)/DTAU)*DTAU
    assert q*(1.0/(1.0+tau_start**2) - 2*g) >= b, nm
    te = np.arange(tau_start, 0.8 + 1e-12, DTAU)
    if te[-1] < 0.8 - 1e-12: te = np.append(te, 0.8)
    if w2 is None:
        wl = np.array([w1]); one_minus_ah = np.array([1.0])
    else:
        nw = int(round((w2-w1)/dw))
        wl = w1 + np.arange(nw)*dw
        wr = wl + dw
        one_minus_ah = np.array([1.0 - ch_right[ix(v)]/v for v in wr])
    wlix = np.array([ix(v) for v in wl])
    dmin = 9e9; loc = None
    for i in range(len(te)-1):
        t1, t2 = te[i], te[i+1]
        xstar = np.pi/t2
        p2 = np.sin(t2*x_safe/2.0)**2/sh2
        cap = np.minimum(t2*t2*hg, 1.0/sh2)
        ps = np.where(xs <= xstar, p2, cap); ps[0] = t2*t2
        gu = np.log1p(ps)
        cg = np.concatenate([[0.0], np.cumsum(gu[:-1])*D])
        Ag = cg[wlix]/wl
        num = np.log1p(t1*t1) - Ag
        assert num.min() > 0, (nm, t1)
        dc = num/(t2*t2) - 2*g*one_minus_ah
        k = int(np.argmin(dc))
        if dc[k] < dmin: dmin, loc = float(dc[k]), (float(wl[k]), float(t1), float(t2))
    ok = dmin >= b; allpass &= ok
    worst_cells[nm] = (loc, g, b, dmin)
    print("%-4s  %.6f  %.4f     %.6f       %.6f   %+.2e  %s   worst cell %s"
          % (nm, b, tau_start, dmin, DRAFT_MIN[nm], dmin - DRAFT_MIN[nm],
             "PASS" if ok else "FAIL", loc))
print("ALL BANDS PASS (independent rebuild): %s" % allpass)

# ---- (3) mpmath ground truth at worst cells ----
print()
print("== (3) ground-truth delta_norm at worst-cell corners (mpmath quad, dps 25) ==")
def delta_norm_true(w, tau, g):
    w = mpf(w); tau = mpf(tau); g = mpf(g)
    arch = pi/tau
    pts = [mpf(0)] + [k*arch for k in range(1, int(w/arch)+1)] + [w]
    pts = sorted(set([p for p in pts if p <= w]))
    Ig = quad(lambda x: log(1 + sin(tau*x/2)**2/sinh(x/2)**2), pts)
    Ihh = quad(lambda x: (x/2)**2/sinh(x/2)**2 if x != 0 else mpf(1), [0, w])
    N = log(1+tau**2) - Ig/w
    return N/tau**2 - 2*g*(1 - Ihh/w)
okall = True
for nm, (loc, g, b, dmin) in worst_cells.items():
    w1c, t1, t2 = loc
    _, gfr, lmaxfr, w1, w2, dw = [bb for bb in BANDS if bb[0] == nm][0]
    w2c = w1c + (dw if dw else 0.0)
    vals = []
    for wv in ([w1c, w2c] if dw else [w1c, 4*w1c]):
        for tv in [t1, t2]:
            vals.append(float(delta_norm_true(wv, tv, g)))
    mn = min(vals)
    ok = mn >= dmin - 1e-12
    okall &= ok
    print("  %-4s worst cell %s: true delta_norm corners min = %.6f  "
          "certified = %.6f  concession = %.6f  (cert <= truth: %s)"
          % (nm, loc, mn, dmin, mn - dmin, ok))
print("lower-bound property holds at every probed corner: %s" % okall)
print("== end r2 ==")
