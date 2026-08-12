#!/usr/bin/env python3
# sl4pr_c_xtail.py -- wave-5 SL4' repair, script [C]: the W1 analytic tail.
#
# [C1] Lemma R.1 (crossover-exponent floor): for all m >= 561, w in (4, 5],
#      tau in [0.8, 1.074]:  x(w, tau) >= 0.0176,  where x is the wp1-c W.6
#      exponent (M = m sin(tau lam/2), r = sin^2(tau lam/2)/sinh^2(lam/2),
#      x = ((M-1)/(2M)) (log(1+r) - r/M)).  Certified by a 548-cell interval
#      computation in tau with explicit safe epsilons:
#        theta := tau lam/2 <= 1.074*2.5/561 = 0.0047861,
#        sin(theta) >= theta (1 - theta^2/6)         -> epsM = 4e-6,
#        sinh(x) <= x (1 + x^2/5) for 0 < x <= 1     -> epsS = 4e-6,
#        M  >= 2 tau1 (1 - epsM)                  (w > 4),
#        r  in [tau1^2 (1 - eps_r), tau2^2],  eps_r = 1.7e-5
#            (since (1-epsM)^2/(1+epsS)^2 >= 1 - 1.7e-5),
#      cell bound (both factors positive, each minimized separately, valid
#      because (M-1)/(2M) and -r/M are increasing in M and r-range is
#      tau-only):  x >= (1/2 - 1/(2 M1)) * (log(1 + r_lo) - r_hi/M1),
#      M1 = 2 tau1 (1 - epsM).  NOTE: this floor needs NO tau-monotonicity
#      (no SL4'-X input).
# [C2] Lemma R.2 (analytic W1 tail): for all m >= 700 and ALL w in (4, 5],
#      with A = m (share worst case), s2 <= m^3/w^2 (Lemma C.1 + A <= m),
#      t_0 <= 1.074 lam (Lemma SL3.C), |phi| <= e^{-m x} <= e^{-0.0176 m} on
#      the crossover ([W.6] + [C1]):
#        Xn <= K_Xn m^{5/2} e^{-0.0176 m},  K_Xn = (sqrt(2pi)/pi)(1.074^3-0.8^3)/3 <= 0.19332
#        Xd <= K_Xd m^{3/2} e^{-0.0176 m},  K_Xd = (sqrt(2pi)/pi)(1.074-0.8)   <= 0.21863
#      (both w-free), and the W1 row bound closes at m = 700 with margin,
#      decreasing in m.  SL4'-X is NOT consumed anywhere in [C1]-[C2].
# [C3] sanity: the tail bound B(m) dominates the X_w6 grid values (display).
import mpmath as mp
from sl4pr_common import (BANDS, row, X_w6, far_ent, e_R5n, e_R5d, e_cube,
                          e_cross, e_midn, e_midd, INFL, QUADF, SQ2PI)
mp.mp.dps = 40

print("== [C1] Lemma R.1: cell-certified floor x(w, tau) >= 0.0176 on [0.8, 1.074] ==")
epsM = mp.mpf('4e-6'); eps_r = mp.mpf('1.7e-5')
# epsilon audit (m >= 561, w <= 5, tau <= 1.074):
theta_max = mp.mpf('1.074')*mp.mpf('2.5')/561
print(f"  theta_max = 1.074*2.5/561 = {mp.nstr(theta_max, 6)};  theta_max^2/6 = "
      f"{mp.nstr(theta_max**2/6, 6)} <= epsM = 4e-6: {theta_max**2/6 <= epsM}")
xh = mp.mpf('2.5')/561
print(f"  (lam/2)_max^2/5 = {mp.nstr(xh**2/5, 6)} <= epsS = 4e-6: {xh**2/5 <= mp.mpf('4e-6')}")
chk = (1-epsM)**2/(1+mp.mpf('4e-6'))**2
print(f"  (1-epsM)^2/(1+epsS)^2 = {mp.nstr(chk, 10)} >= 1 - eps_r = {mp.nstr(1-eps_r, 10)}: {chk >= 1-eps_r}")
ncell = 548; lo = mp.mpf('0.8'); hi = mp.mpf('1.074'); h = (hi-lo)/ncell
xmin = mp.inf; argc = None; allpos = True
for i in range(ncell):
    t1 = lo + i*h; t2 = t1 + h
    M1 = 2*t1*(1-epsM)
    r_lo = t1**2*(1-eps_r); r_hi = t2**2
    br = mp.log(1+r_lo) - r_hi/M1
    if br <= 0: allpos = False
    xb = (mp.mpf('0.5') - 1/(2*M1))*br
    if xb < xmin: xmin = xb; argc = (t1, t2)
print(f"  cells: {ncell} (width {mp.nstr(h, 4)});  all cell brackets positive: {allpos}")
print(f"  min cell lower bound = {mp.nstr(xmin, 6)} at tau-cell [{mp.nstr(argc[0],5)}, {mp.nstr(argc[1],5)}]")
print(f"  CERTIFIED: x(w, tau) >= 0.0176 for all m >= 561, w in (4, 5], tau in [0.8, 1.074]: {xmin >= mp.mpf('0.0176')}")
# spot truth vs floor (display): the true corner value
def w6_x_direct(w, tau, m):
    lam = mp.mpf(w)/m; t = tau*lam
    M = m*mp.sin(t/2); s = mp.sin(t/2)**2; S = mp.sinh(lam/2)**2
    return (M-1)/(2*M)*(mp.log(1+s/S) - s/(S*M))
print(f"  spot truth: x(4+1e-9, 0.8, 561) = {mp.nstr(w6_x_direct(mp.mpf('4')+mp.mpf('1e-9'), mp.mpf('0.8'), 561), 6)}"
      f"  (floor 0.0176; the floor is tight at the (w -> 4+, tau = 0.8) corner)")

print("\n== [C2] Lemma R.2: analytic W1 tail, m >= 700, all w in (4, 5] ==")
K_Xn = SQ2PI/mp.pi*(mp.mpf('1.074')**3 - mp.mpf('0.8')**3)/3
K_Xd = SQ2PI/mp.pi*(mp.mpf('1.074') - mp.mpf('0.8'))
print(f"  K_Xn = (sqrt(2pi)/pi)(1.074^3-0.8^3)/3 = {mp.nstr(K_Xn, 7)} <= 0.19332: {K_Xn <= mp.mpf('0.19332')}")
print(f"  K_Xd = (sqrt(2pi)/pi)(0.274)         = {mp.nstr(K_Xd, 7)} <= 0.21863: {K_Xd <= mp.mpf('0.21863')}")
XM = mp.mpf('0.0176')
def B(m): return (mp.mpf('0.19332')*mp.mpf(m)**mp.mpf('2.5')
                  + mp.mpf('0.21863')*mp.mpf(m)**mp.mpf('1.5'))*mp.e**(-XM*m)
print(f"  B(m) log-derivative 2.5/m - 0.0176 < 0 iff m > {mp.nstr(mp.mpf('2.5')/XM, 6)}"
      f"  -> B nonincreasing on m >= 143 (a fortiori on m >= 700)")
def dec_W1(m):
    A0 = mp.mpf('0.28')*m
    main = mp.mpf('0.8')/2 + mp.mpf('0.3') + (mp.mpf(5)/m)**2/2
    return main + INFL*(e_R5n('0.05',A0)+e_cube('1.0',A0)+e_cross('1.0','0.8',A0)
                        +e_midn(mp.mpf('0.42'),A0)+e_R5d('0.05',A0)+e_midd(mp.mpf('0.42'),A0))
def rowbound(m):
    Fn, Fd = far_ent(4, m)
    return (1+QUADF)*(dec_W1(m)/(20*mp.mpf('0.28')) + INFL*(B(m)+Fn+Fd)/20)
for m in (700, 750, 800, 1000, 2000, 5000):
    rb = rowbound(m)
    print(f"  m={m}: B(m) = {mp.nstr(B(m), 6)};  dec_W1 = {mp.nstr(dec_W1(m), 6)};"
          f"  W1 row bound = {mp.nstr(rb, 6)}  {'PASS' if rb <= 1 else 'FAIL'}"
          + (f"  (margin {mp.nstr(1-rb, 4)})" if m == 700 else ""))
rb700 = rowbound(700)
print(f"  monotonicity of the m = 700 bound in m: every piece closed-form nonincreasing --")
print(f"    main: (5/m)^2/2 decreasing; 1/sqrt(0.28 m) entries decreasing;")
print(f"    mid(g=0.42): decreasing for A0 >= 6/0.42 = 14.29 (used A0 >= 196);")
print(f"    B: nonincreasing for m >= 143;  far: nonincreasing for m >= 75.")
print(f"  CERTIFIED: W1 row <= {mp.nstr(rb700, 5)} for ALL m >= 700 and ALL w in (4, 5]"
      f"  [inputs: W.6 pointwise + Lemma R.1 + C.1 + A2 + SL1'-w + SL4'-E; NO SL4'-X]")

slot561 = (1 - (1+QUADF)*dec_W1(561)/(20*mp.mpf('0.28')))*20/((1+QUADF)*INFL)
print(f"  why the grid rung [561, 699] is needed: B(561) = {mp.nstr(B(561), 5)} vs the")
print(f"  available X-slot at m = 561 ~ {mp.nstr(slot561, 5)} (flat-exponent bound too crude there)")

print("\n== [C3] sanity: tail bound vs X_w6 grid values at m = 700 (display only) ==")
for wtag in ('4.000000001', '4.5', '5.0'):
    Xn, Xd, _ = X_w6(mp.mpf(wtag), 700, mp.mpf(700))
    print(f"  w={wtag}: X_w6 Xn+Xd = {mp.nstr(Xn+Xd, 6)}  vs  B(700) = {mp.nstr(B(700), 6)}"
          f"  (bound/actual = {mp.nstr(B(700)/(Xn+Xd), 4)}x)")
tau0_at = 2*mp.asin(mp.sinh(mp.mpf('5')/(2*561)))/(mp.mpf('5')/561)
print(f"  tau0(lam) at m=561, w=5: {mp.nstr(tau0_at, 8)} <= 1.074 (SL3.C): {tau0_at <= mp.mpf('1.074')}")
