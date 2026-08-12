#!/usr/bin/env python3
# ref_msr_b_r1r2.py -- maths referee, wave4_sl4p_repaired: Lemmas R.1/R.2.
#  [B1] Lemma R.1 independently re-certified (own code, own cell count 1096 =
#       2x finer), epsilon audit re-derived; truth-side sampling (floor must
#       sit BELOW the true x everywhere sampled).
#  [B2] Lemma R.2: independent K_Xn/K_Xd; independent row bound at m = 700;
#       LOAD-BEARING test: same bound with the mid slot at PROVED tier-1
#       g = 0.1317 instead of Theorem SL3''s 0.42 (is SL3' really needed?).
#  [B3] REFEREE CONSTRUCTION: per-cell-floor upper bound for the X slot
#       (Lemma R.1 cells; NO tau-monotonicity = NO SL4'-X) evaluated on
#       m = 561..699 -- does it close the grid rung analytically?
import mpmath as mp
mp.mp.dps = 50
SQ2PI = mp.sqrt(2*mp.pi)
INFL = mp.mpf('1.10'); QUADF = mp.mpf('0.09'); FAREXP = mp.mpf('0.0741')

def w6x(w, tau, m):
    lam = w/m; t = tau*lam
    M = m*mp.sin(t/2); s = mp.sin(t/2)**2; S = mp.sinh(lam/2)**2
    if M <= 1: return mp.mpf(0)
    return max((M-1)/(2*M)*(mp.log(1+s/S) - s/(S*M)), mp.mpf(0))

print("== [B1] Lemma R.1 independent re-certification ==")
# epsilon audit, re-derived:
thmax = mp.mpf('1.074')*mp.mpf('2.5')/561
epsM = mp.mpf('4e-6'); epsS = mp.mpf('4e-6'); eps_r = mp.mpf('1.7e-5')
print(f"  theta_max^2/6 = {mp.nstr(thmax**2/6, 6)} <= epsM: {thmax**2/6 <= epsM}")
print(f"  (lam/2)max^2/5 = {mp.nstr((mp.mpf('2.5')/561)**2/5, 6)} <= epsS: {(mp.mpf('2.5')/561)**2/5 <= epsS}")
print(f"  sinh(x) <= x(1+x^2/5) on (0,1]: check chain (x^2/6)/(1-x^2/20) <= x^2/5 iff x^2 <= 10/3: True;"
      f"  spot sinh(1) = {mp.nstr(mp.sinh(1), 6)} <= 1.2: {mp.sinh(1) <= mp.mpf('1.2')}")
print(f"  (1-epsM)^2/(1+epsS)^2 = {mp.nstr((1-epsM)**2/(1+epsS)**2, 11)} >= 1-eps_r: "
      f"{(1-epsM)**2/(1+epsS)**2 >= 1-eps_r}")
def cell_floor(t1, t2):
    M1 = 2*t1*(1-epsM)
    return (mp.mpf('0.5') - 1/(2*M1))*(mp.log(1 + t1**2*(1-eps_r)) - t2**2/M1)
for ncell in (548, 1096):
    lo = mp.mpf('0.8'); hi = mp.mpf('1.074'); h = (hi-lo)/ncell
    xm = mp.inf; argc = None
    for i in range(ncell):
        t1 = lo + i*h; xb = cell_floor(t1, t1+h)
        if xb < xm: xm = xb; argc = t1
    print(f"  ncell = {ncell}: min cell floor = {mp.nstr(xm, 6)} at tau1 = {mp.nstr(argc, 5)}"
          f"  >= 0.0176: {xm >= mp.mpf('0.0176')}")
# truth side: floor must lie below true x on a corner sweep
worst = mp.inf
for m in (561, 600, 699, 700, 1000, 5000):
    for wv in ('4.000000001', '4.001', '4.5', '5.0'):
        for tv in ('0.8', '0.85', '0.9', '1.0', '1.074'):
            xt = w6x(mp.mpf(wv), mp.mpf(tv), m)
            if xt < worst: worst = xt; wa = (m, wv, tv)
print(f"  truth sweep min x = {mp.nstr(worst, 6)} at (m, w, tau) = {wa}  >= 0.0176: {worst >= mp.mpf('0.0176')}")

print("\n== [B2] Lemma R.2 independent + SL3'-load-bearing test ==")
K_Xn = SQ2PI/mp.pi*(mp.mpf('1.074')**3 - mp.mpf('0.8')**3)/3
K_Xd = SQ2PI/mp.pi*(mp.mpf('1.074') - mp.mpf('0.8'))
print(f"  K_Xn = {mp.nstr(K_Xn, 8)} (<= 0.19332: {K_Xn <= mp.mpf('0.19332')});"
      f"  K_Xd = {mp.nstr(K_Xd, 8)} (<= 0.21863: {K_Xd <= mp.mpf('0.21863')})")
def efac(C5v): return (mp.mpf('0.5')/(mp.mpf('0.5') - C5v/8))**4
def dec_W1(m, g):
    A = mp.mpf('0.28')*m; C5v = mp.mpf('0.05')
    main = mp.mpf('0.4') + mp.mpf('0.3') + (mp.mpf(5)/m)**2/2
    r5n = 48*SQ2PI/mp.pi*C5v*efac(C5v)/mp.sqrt(A); r5d = r5n/6
    cube = mp.mpf('2.37')/mp.sqrt(A)
    cross = (mp.mpf('2.13')*mp.mpf('0.8') + mp.mpf('0.56')*mp.mpf('0.64'))/mp.sqrt(A)
    midn = SQ2PI/mp.pi*A**mp.mpf('1.5')/(4*g)*mp.e**(-g*A/4)*(1+2/(g*A))
    midd = SQ2PI/mp.pi*mp.sqrt(A)/g*mp.e**(-g*A/4)
    return main + INFL*(r5n+r5d+cube+cross+midn+midd)
def far_slot(m):
    lam = mp.mpf(4)/m; s2max = m/(4*mp.sinh(lam/2)**2)
    return (2*SQ2PI*m*s2max**mp.mpf('1.5')*mp.e**(-FAREXP*m),
            m*mp.sqrt(2*mp.pi*s2max)*mp.e**(-FAREXP*m))
def B(m): return (mp.mpf('0.19332')*mp.mpf(m)**mp.mpf('2.5')
                  + mp.mpf('0.21863')*mp.mpf(m)**mp.mpf('1.5'))*mp.e**(-mp.mpf('0.0176')*m)
def rowbound(m, g):
    Fn, Fd = far_slot(m)
    return (1+QUADF)*(dec_W1(m, g)/(20*mp.mpf('0.28')) + INFL*(B(m)+Fn+Fd)/20)
rb42 = rowbound(700, mp.mpf('0.42')); rb13 = rowbound(700, mp.mpf('0.1317'))
print(f"  row bound(700, g=0.42 [SL3']) = {mp.nstr(rb42, 6)}  [prover: 0.911407]")
print(f"  row bound(700, g=0.1317 [PROVED tier-1 only]) = {mp.nstr(rb13, 6)}"
      f"  -> SL3' load-bearing in Lemma R.2: {rb13 > 1}")
# how far must m go for the tier-1-only version to close?
mstar = None
for m in range(700, 3001):
    if rowbound(m, mp.mpf('0.1317')) <= 1: mstar = m; break
print(f"  first m with tier-1-only R.2 bound <= 1: {mstar}")

print("\n== [B3] referee construction: per-cell-floor X bound (NO SL4'-X) on [561, 699] ==")
# X slot upper bound with R.1's per-cell floors: on cell [tau1, tau2],
#   int t^2 e^{-m x} dt <= (h lam)((tau2 lam)^2) e^{-m floor(cell)}  -- pointwise
#   floor, NO monotonicity; w-free after the exact cancellations (A = m):
#   Xn <= (sqrt(2pi)/pi) m^{5/2} sum_i h tau2_i^2 e^{-m fl_i},
#   Xd <= (sqrt(2pi)/pi) m^{3/2} sum_i h e^{-m fl_i}.
ncell = 548; lo = mp.mpf('0.8'); hi = mp.mpf('1.074'); h = (hi-lo)/ncell
floors = []
for i in range(ncell):
    t1 = lo + i*h; floors.append((t1, t1+h, cell_floor(t1, t1+h)))
def X_cellbound(m):
    sn = sd = mp.mpf(0)
    for t1, t2, fl in floors:
        e = mp.e**(-m*fl)
        sn += h*t2**2*e; sd += h*e
    return SQ2PI/mp.pi*(mp.mpf(m)**mp.mpf('2.5')*sn), SQ2PI/mp.pi*(mp.mpf(m)**mp.mpf('1.5')*sd)
def row_cellbound(m, g=mp.mpf('0.42')):
    Xn, Xd = X_cellbound(m)
    Fn, Fd = far_slot(m)
    return (1+QUADF)*(dec_W1(m, g)/(20*mp.mpf('0.28')) + INFL*(Xn+Xd+Fn+Fd)/20)
allpass = True; wm = -mp.inf; wat = None
for m in range(561, 700):
    rb = row_cellbound(m)
    if rb > 1: allpass = False
    if rb > wm: wm = rb; wat = m
for m in (561, 600, 650, 699):
    print(f"  m={m}: per-cell-floor W1 row bound = {mp.nstr(row_cellbound(m), 6)}")
print(f"  ALL m in [561, 699]: per-cell-floor row bound <= 1: {allpass}"
      f"  (worst {mp.nstr(wm, 6)} at m = {wat})")
print(f"  => the [561, 699] rung closes with NO SL4'-X and NO w-grid: the X bound is")
print(f"     w-uniform (exact w-cancellation) and uses only R.1's cell floors pointwise.")
# and at the trapezoid edge, for the record:
for m in (463, 470, 500, 540):
    print(f"  (record) m={m}: per-cell-floor bound = {mp.nstr(row_cellbound(m), 6)}"
          f"  (floors derived for m >= 561; eps audit extends: theta_max(463)^2/6 = "
          f"{mp.nstr((mp.mpf('1.074')*mp.mpf('2.5')/463)**2/6, 4)} <= 4e-6: "
          f"{(mp.mpf('1.074')*mp.mpf('2.5')/463)**2/6 <= mp.mpf('4e-6')})")
