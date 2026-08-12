#!/usr/bin/env python3
# ref_rp_c_R1R2.py -- wave-5 numerics referee on wave4_sl4p_repaired:
# independent rebuild + truth attack on the NEW analytic content, Lemmas
# R.1 (crossover-exponent floor 0.0176) and R.2 (W1 analytic tail m >= 700).
# Written FROM THE DRAFT TEXT (SS5.3/SS5.4), not copied from sl4pr_c_xtail.py;
# dps 60; denser cells (2740 at width 1e-4 vs the prover's 548 at 5e-4).
#
# [C1] epsilon audit re-derived: theta_max^2/6, (lam/2)_max^2/5, the eps_r
#      compound -- exact comparisons at dps 60.
# [C2] elementary-bracket validity spot checks: sin(th) >= th(1 - th^2/6)
#      and sinh(x) <= x(1 + x^2/5) on dense grids of the used range.
# [C3] INDEPENDENT cell certificate, 2740 cells width 1e-4 (and the
#      prover's own 548 x 5e-4 re-derived): min cell bound, >= 0.0176?
# [C4] TRUTH attack on the floor: direct minimization of the true
#      x(w, tau; m) over adversarial (m, w) x fine tau grids; global min
#      must be >= 0.0176 and ~ 0.0177554 at (m=561, w->4+, tau=0.8).
# [C5] Lemma R.2 constants exact at dps 60: K_Xn, K_Xd, w-power cancelation
#      at sample points, B(m) monotone m in [700, 3000] step 1, rowbound(m)
#      re-derived from the draft's display (own code) at m = 700 and
#      monotone-decreasing scan m in [700, 1500]; certify <= 0.9115.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'wave5_sl4prepair'))
import mpmath as mp
mp.mp.dps = 60

print("== [C1] epsilon audit (independent, dps 60) ==")
theta_max = mp.mpf('1.074') * mp.mpf('2.5') / 561
epsM = mp.mpf('4e-6'); epsS = mp.mpf('4e-6'); eps_r = mp.mpf('1.7e-5')
print(f"  theta_max = {mp.nstr(theta_max, 10)};  theta_max^2/6 = "
      f"{mp.nstr(theta_max**2/6, 8)} <= 4e-6: {theta_max**2/6 <= epsM}")
xh = mp.mpf('2.5') / 561
print(f"  (lam/2)_max^2/5 = {mp.nstr(xh**2/5, 8)} <= 4e-6: {xh**2/5 <= epsS}")
lhs = (1 - epsM)**2 / (1 + epsS)**2
print(f"  (1-epsM)^2/(1+epsS)^2 = {mp.nstr(lhs, 14)} >= 1 - 1.7e-5 = "
      f"{mp.nstr(1-eps_r, 14)}: {lhs >= 1 - eps_r}")

print("\n== [C2] elementary brackets on the used range ==")
ok1 = ok2 = True
for k in range(1, 1001):
    th = theta_max * k / 1000
    if mp.sin(th) < th * (1 - th**2/6): ok1 = False
    x = xh * k / 1000
    if mp.sinh(x) > x * (1 + x**2/5): ok2 = False
# and the sinh bracket's full claimed range 0 < x <= 1:
for k in range(1, 1001):
    x = mp.mpf(k) / 1000
    if mp.sinh(x) > x * (1 + x**2/5): ok2 = False
print(f"  sin(th) >= th(1 - th^2/6) on (0, theta_max], 1000 pts: {ok1}")
print(f"  sinh(x) <= x(1 + x^2/5) on (0, 1], 1000 pts (incl. used range): {ok2}")

print("\n== [C3] independent cell certificate ==")
def cell_min(ncell):
    lo = mp.mpf('0.8'); hi = mp.mpf('1.074'); h = (hi - lo) / ncell
    xmin = mp.inf; argc = None; allpos = True
    for i in range(ncell):
        t1 = lo + i*h; t2 = t1 + h
        M1 = 2 * t1 * (1 - epsM)
        f1 = mp.mpf('0.5') - 1/(2*M1)
        f2 = mp.log(1 + t1**2 * (1 - eps_r)) - t2**2 / M1
        if f2 <= 0 or f1 <= 0: allpos = False
        v = f1 * f2
        if v < xmin: xmin = v; argc = t1
    return xmin, argc, allpos
for n in (548, 2740):
    xmin, argc, allpos = cell_min(n)
    print(f"  ncell = {n}: all factors positive: {allpos};  min bound = "
          f"{mp.nstr(xmin, 7)} at tau1 = {mp.nstr(argc, 6)};  >= 0.0176: {xmin >= mp.mpf('0.0176')}")

print("\n== [C4] truth attack: direct min of x(w, tau; m) over adversarial grids ==")
def x_true(w, tau, m):
    lam = mp.mpf(w)/m; t = tau*lam
    M = m*mp.sin(t/2); s = mp.sin(t/2)**2; S = mp.sinh(lam/2)**2
    return (M-1)/(2*M)*(mp.log(1+s/S) - s/(S*M))
gmin = mp.inf; garg = None
ms = [561, 562, 600, 699, 700, 1000, 10**4, 10**6]
ws = [mp.mpf('4')+mp.mpf('1e-12'), mp.mpf('4')+mp.mpf('1e-9'), mp.mpf('4.001'),
      mp.mpf('4.25'), mp.mpf('4.5'), mp.mpf('4.75'), mp.mpf('5.0')]
ntau = 200
for m in ms:
    for w in ws:
        for k in range(ntau + 1):
            tau = mp.mpf('0.8') + (mp.mpf('1.074') - mp.mpf('0.8')) * k / ntau
            v = x_true(w, tau, m)
            if v < gmin: gmin = v; garg = (m, mp.nstr(w, 8), mp.nstr(tau, 5))
print(f"  points: {len(ms)*len(ws)*(ntau+1)};  global min x = {mp.nstr(gmin, 7)} at "
      f"(m, w, tau) = {garg}")
print(f"  min >= floor 0.0176: {gmin >= mp.mpf('0.0176')};  draft's corner truth "
      f"0.0177554: x(4+1e-9, 0.8; 561) = {mp.nstr(x_true(mp.mpf('4')+mp.mpf('1e-9'), mp.mpf('0.8'), 561), 6)}")

print("\n== [C5] Lemma R.2 re-derived (own code, dps 60) ==")
SQ2PI = mp.sqrt(2*mp.pi)
K_Xn = SQ2PI/mp.pi * (mp.mpf('1.074')**3 - mp.mpf('0.8')**3) / 3
K_Xd = SQ2PI/mp.pi * (mp.mpf('1.074') - mp.mpf('0.8'))
print(f"  K_Xn = {mp.nstr(K_Xn, 10)} <= 0.19332: {K_Xn <= mp.mpf('0.19332')};"
      f"  K_Xd = {mp.nstr(K_Xd, 10)} <= 0.21863: {K_Xd <= mp.mpf('0.21863')}")
# w-power cancelation: m (m^3/w^2)^{3/2} lam^3 == m^{5/2} exactly
canc = True
for (m, w) in ((700, mp.mpf('4.123')), (999, mp.mpf('5')), (561, mp.mpf('4')+mp.mpf('1e-9'))):
    lam = mp.mpf(w)/m
    lhs = m * (mp.mpf(m)**3/mp.mpf(w)**2)**mp.mpf('1.5') * lam**3
    if abs(lhs/mp.mpf(m)**mp.mpf('2.5') - 1) > mp.mpf('1e-50'): canc = False
print(f"  w-power cancelation m*(m^3/w^2)^1.5*lam^3 = m^2.5 exact at 3 samples: {canc}")
XM = mp.mpf('0.0176')
def B(m): return (mp.mpf('0.19332')*mp.mpf(m)**mp.mpf('2.5')
                  + mp.mpf('0.21863')*mp.mpf(m)**mp.mpf('1.5'))*mp.e**(-XM*m)
monoB = all(B(m+1) < B(m) for m in range(700, 3000))
print(f"  B(m) strictly decreasing on [700, 3000] step 1: {monoB}"
      f"  (log-deriv < 0 iff m > 2.5/0.0176 = {mp.nstr(mp.mpf('2.5')/XM, 6)})")
# rowbound re-derived from the draft display (independent of sl4pr_c code):
INFL = mp.mpf('1.10'); QUADF = mp.mpf('0.09')
def efac(C5): return (mp.mpf('0.5')/(mp.mpf('0.5')-mp.mpf(C5)/8))**4
def dec_W1(m):
    A0 = mp.mpf('0.28')*m
    main = mp.mpf('0.8')/2 + mp.mpf('0.3')*mp.mpf('1.0')**2 + (mp.mpf(5)/m)**2/2
    r5n = 48*SQ2PI/mp.pi*mp.mpf('0.05')*efac('0.05')/mp.sqrt(A0)
    r5d = 8*SQ2PI/mp.pi*mp.mpf('0.05')*efac('0.05')/mp.sqrt(A0)
    cube = mp.mpf('2.37')/mp.sqrt(A0)
    cross = (mp.mpf('2.13')*mp.mpf('0.8')+mp.mpf('0.56')*mp.mpf('0.64'))/mp.sqrt(A0)
    g = mp.mpf('0.42')
    midn = SQ2PI/mp.pi*A0**mp.mpf('1.5')/(4*g)*mp.e**(-g*A0/4)*(1+2/(g*A0))
    midd = SQ2PI/mp.pi*mp.sqrt(A0)/g*mp.e**(-g*A0/4)
    return main + INFL*(r5n + cube + cross + midn + r5d + midd)
def far(m):
    lam = mp.mpf(4)/m; s2max = m/(4*mp.sinh(lam/2)**2)
    Fn = 2*SQ2PI*m*s2max**mp.mpf('1.5')*mp.e**(-mp.mpf('0.0741')*m)
    Fd = m*mp.sqrt(2*mp.pi*s2max)*mp.e**(-mp.mpf('0.0741')*m)
    return Fn + Fd
def rowbound(m):
    return (1+QUADF)*(dec_W1(m)/(20*mp.mpf('0.28')) + INFL*(B(m)+far(m))/20)
rb700 = rowbound(700)
print(f"  rowbound(700) = {mp.nstr(rb700, 8)}  [prover: 0.911407]  <= 0.9115: {rb700 <= mp.mpf('0.9115')}")
monoRB = all(rowbound(m+1) < rowbound(m) for m in range(700, 1500))
print(f"  rowbound strictly decreasing on [700, 1500] step 1: {monoRB}")
# crude-bound-dominates-actual sanity at an off-sample point:
from sl4pr_common import X_w6
for (m, wtag) in ((750, '4.2'), (700, '4.000003')):
    Xn, Xd, _ = X_w6(mp.mpf(wtag), m, mp.mpf(m))
    print(f"  X_w6(w={wtag}, m={m}) Xn+Xd = {mp.nstr(Xn+Xd, 6)} <= B({m}) = "
          f"{mp.nstr(B(m), 6)}: {Xn+Xd <= B(m)}")
