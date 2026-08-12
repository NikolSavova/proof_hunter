#!/usr/bin/env python3
# scout_s1_targets.py -- WAVE 6 constants scout (design, not proof), F2 campaign.
#
# Task: re-architect the per-band (S1) targets R31*(W)/R42*(W) to maximize the
# worst-band PROOF margin (target vs measured truth sup over m >= 561), spending
# the composed-chain slack (C* = 18.2281 vs budget 20 on [561, 1580]; budget 136
# for m >= 1581), while keeping every chain constraint intact:
#   (a) W2-W7 ledger rows <= RESERVE at m = 561 (entries nonincreasing in m);
#   (b) W1 ladder: per-cell-floor rung (referee M3 construction) on [561, 699]
#       AND Lemma R.2 crude tail at m = 700 both <= RESERVE;
#   (c) Theorem E re-certification: REM*(W) <= 0.3 R31*(W)^2 + positivity
#       (exact Fractions, port of e1_pricing_certificate.py);
#   (d) (S3) recalibration: J0(W) = J*(W) - REM*(W) recomputed, margins vs truth;
#   (e) INFL/QUADF bootstrap (referee M2 chord/monotone-iteration): contraction
#       at the target and seed basin x_seed >= 0.89 at the NEW worst rows.
# (S2): C5* unchanged on W1-W6b; ONE adjustment C5*(W7): 0.80 -> 0.50 (design
# trade, corroborated by a kappa_5 leading-order truth estimate; see block [S2]).
#
# Row machinery = sl4pr_common.py (twice-validated engine), imported unmodified.
# Truth cumulants = closed-form factor cumulants (same closed forms as
# e2_truth_margins.py, independently re-implemented here with expm1 guards).
import sys, math
sys.path.insert(0, '/Users/sihaohuang/Desktop/Coding/proof_hunter/phase2/bruhat/'
                   'f2_drafts/g2_scripts/campaign_20260811/wave5_sl4prepair')
import mpmath as mp
import sl4pr_common as C
from fractions import Fraction as F

mp.mp.dps = 40
SQ2PI = C.SQ2PI; INFL = C.INFL; QUADF = C.QUADF
RESERVE = mp.mpf('0.98')     # designed row cap at m = 561 (2% assembly reserve)
CAP     = mp.mpf('1.35')     # comfort cap: no band target exceeds 1.35x truth sup

def ns(x, n=6): return mp.nstr(mp.mpf(x), n)

# ---------- truth cumulants (closed forms; expm1-guarded) ----------
def phis(x):
    q = mp.e**(-x); r = -mp.expm1(-x)          # r = 1 - q, exact small-x
    return q/r**2, q*(1+q)/r**3, q*(1+4*q+q*q)/r**4
def phi5(x):
    q = mp.e**(-x); r = -mp.expm1(-x)
    return q*(1 + 11*q + 11*q*q + q**3)/r**5
def cums(m, lam):
    p2, p3, p4 = phis(lam)
    s2 = m*p2; k3 = m*p3; k4 = m*p4
    for j in range(1, m+1):
        jl = j*lam
        if jl > 140 and j > 1: break           # j^4 e^{-jl} < 1e-52: negligible
        q2, q3, q4 = phis(jl)
        s2 -= j*j*q2; k3 -= j**3*q3; k4 -= j**4*q4
    return s2, k3, k4
def ratios(m, w):
    lam = mp.mpf(w)/m
    s2, k3, k4 = cums(m, lam)
    return abs(k3)*lam/s2, k4*lam*lam/s2
def r31geo(lam):
    q = mp.e**(-lam); r = -mp.expm1(-lam)
    return lam*(1+q)/r
def r42geo(lam):
    q = mp.e**(-lam); r = -mp.expm1(-lam)
    return lam*lam*(1+4*q+q*q)/r**2

# ---------- W1 ladder machinery (R.2 + referee-M3 cell rung), parameterized ----
def dec_W1(m, R31, R42, C5=mp.mpf('0.05'), g=mp.mpf('0.42')):
    A0 = mp.mpf('0.28')*m
    main = R42/2 + mp.mpf('0.3')*R31**2 + (mp.mpf(5)/m)**2/2
    return main + INFL*(C.e_R5n(C5, A0) + C.e_cube(R31, A0) + C.e_cross(R31, R42, A0)
                        + C.e_midn(g, A0) + C.e_R5d(C5, A0) + C.e_midd(g, A0))
def Btail(m):
    return (mp.mpf('0.19332')*mp.mpf(m)**mp.mpf('2.5')
            + mp.mpf('0.21863')*mp.mpf(m)**mp.mpf('1.5'))*mp.e**(-mp.mpf('0.0176')*m)
def R2bound(m, R31, R42, C5=mp.mpf('0.05')):
    Fn, Fd = C.far_ent(4, m)
    return (1+QUADF)*(dec_W1(m, R31, R42, C5)/(20*mp.mpf('0.28'))
                      + INFL*(Btail(m)+Fn+Fd)/20)
epsM = mp.mpf('4e-6'); eps_r = mp.mpf('1.7e-5')
def cell_floor(t1, t2):
    M1 = 2*t1*(1-epsM)
    return (mp.mpf('0.5') - 1/(2*M1))*(mp.log(1 + t1**2*(1-eps_r)) - t2**2/M1)
NCELL = 548; LO = mp.mpf('0.8'); HI = mp.mpf('1.074'); H = (HI-LO)/NCELL
FLOORS = []
for i in range(NCELL):
    t1 = LO + i*H; FLOORS.append((t1, t1+H, cell_floor(t1, t1+H)))
def cellrow(m, R31, R42, C5=mp.mpf('0.05')):
    sn = sd = mp.mpf(0)
    for t1, t2, fl in FLOORS:
        e = mp.e**(-m*fl); sn += H*t2*t2*e; sd += H*e
    Xn = SQ2PI/mp.pi*mp.mpf(m)**mp.mpf('2.5')*sn
    Xd = SQ2PI/mp.pi*mp.mpf(m)**mp.mpf('1.5')*sd
    Fn, Fd = C.far_ent(4, m)
    return (1+QUADF)*(dec_W1(m, R31, R42, C5)/(20*mp.mpf('0.28'))
                      + INFL*(Xn+Xd+Fn+Fd)/20)

# ---------- band frame ----------
# (name, wlo, whi, cA, cAd, C5_old, C5_new, gam)
FRAME = [('W1', 4, 5,  '0.28','0.28','0.05','0.05','0.42'),
         ('W2', 5, 6,  '0.35','0.35','0.06','0.06','0.42'),
         ('W3', 6, 8,  '0.42','0.42','0.08','0.08','0.40'),
         ('W4', 8, 10, '0.52','0.52','0.10','0.10','0.40'),
         ('W5', 10, 20,'0.60','0.60','0.15','0.15','PROVED'),
         ('W6b',20, 40,'0.70','0.70','0.25','0.25','PROVED'),
         ('W7', 40, 0, '0.80','0.85','0.80','0.50','PROVED')]
OLD = {'W1': ('1.0','0.8'), 'W2': ('1.2','1.4'), 'W3': ('1.5','2.6'),
       'W4': ('1.7','3.5'), 'W5': ('2.0','5.2'), 'W6b': ('2.1','6.0'),
       'W7': ('2.2','6.6')}
def mkband(name, R31, R42, C5=None):
    for (n, wlo, whi, cA, cAd, c5o, c5n, gam) in FRAME:
        if n == name:
            return (n, wlo, whi, R31, R42, cA, cAd,
                    (C5 if C5 is not None else c5n), gam)
    raise KeyError(name)

print("== [G] GUARDS: reproduce the wave-5 chain numbers before touching anything ==")
ref561 = {'W2':'0.35065','W3':'0.48309','W4':'0.51831','W5':'0.70933',
          'W6b':'0.69981','W7':'0.8723'}
gok = True
for b in C.BANDS:
    if b[0] == 'W1': continue
    tot, _, _ = C.row(b, 561)
    match = abs(tot - mp.mpf(ref561[b[0]])) < mp.mpf('5e-5')
    gok = gok and match
    print(f"  old row({b[0]}, 561) = {ns(tot)}  [compose: {ref561[b[0]]}]  match: {match}")
r2o = R2bound(700, mp.mpf('1.0'), mp.mpf('0.8'))
co  = cellrow(561, mp.mpf('1.0'), mp.mpf('0.8'))
print(f"  old R.2 bound(700) = {ns(r2o)}  [prover/referee: 0.911407]  match: {abs(r2o-mp.mpf('0.911407'))<mp.mpf('5e-6')}")
print(f"  old cell-rung row(561) = {ns(co)}  [referee M3: 0.416537]  match: {abs(co-mp.mpf('0.416537'))<mp.mpf('5e-6')}")
mn = min(fl for _, _, fl in FLOORS)
print(f"  min cell floor = {ns(mn)}  [R.1: 0.0176601]  >= 0.0176: {mn >= mp.mpf('0.0176')}")
r31c, r42c = ratios(561, mp.mpf('5.0'))
print(f"  truth r31/r42 (561, w=5.0) = {ns(r31c,5)}/{ns(r42c,5)}  [e2: 0.8864/0.6506]")
r31d, r42d = ratios(561, mp.mpf('499.29'))
print(f"  truth r31/r42 (561, w=499.29) = {ns(r31d,5)}/{ns(r42d,5)}  [e2: 2.1240/6.3713]")
g4 = 6*mp.mpf(4) - mp.quad(lambda x: x**4*phis(x)[2], [0, 4])
print(f"  G_4(4) via integral = {ns(g4,7)}  [Lemma E.4: 0.2323483]")
print(f"  r31geo(0.89) = {ns(r31geo(mp.mpf('0.89')),6)}  r42geo(0.89) = {ns(r42geo(mp.mpf('0.89')),6)}"
      f"  [STATUS geometric limits: 2.1303/6.4113]")
print(f"  ALL GUARDS OK: {gok}")

print()
print("== [T] TRUTH: per-band sup of r31/r42 over the band x {m >= 561} ==")
EDGE = {'W1': '5.0', 'W2': '6.0', 'W3': '8.0', 'W4': '10.0', 'W5': '20.0', 'W6b': '40.0'}
SCAN = {'W1': ['4.001','4.3','4.6','4.9','5.0'],
        'W2': ['5.001','5.3','5.6','5.9','6.0'],
        'W3': ['6.001','6.5','7.0','7.5','8.0'],
        'W4': ['8.001','8.7','9.3','10.0'],
        'W5': ['10.001','12','15','18','20.0'],
        'W6b':['20.001','25','30','35','40.0'],
        'W7': ['40.001','60','100','200','350','450','499.29']}
TSUP = {}; JMAX = {}
for W in ['W1','W2','W3','W4','W5','W6b']:
    t31 = t42 = jm = mp.mpf(-1)
    for ws in SCAN[W]:
        r31, r42 = ratios(561, mp.mpf(ws))
        t31 = max(t31, r31); t42 = max(t42, r42); jm = max(jm, r31*r31 - r42/2)
    e31_561, e42_561 = ratios(561, mp.mpf(EDGE[W]))
    e31_1k,  e42_1k  = ratios(1000, mp.mpf(EDGE[W]))
    e31_25,  e42_25  = ratios(2500, mp.mpf(EDGE[W]))
    dec31 = (e31_561 >= e31_1k >= e31_25); dec42 = (e42_561 >= e42_1k >= e42_25)
    TSUP[W] = (t31, t42); JMAX[W] = jm
    print(f"  {W:3s}: sup@561 r31 = {ns(t31,5)} (edge), r42 = {ns(t42,5)} (edge);"
          f"  m-direction at edge DEcreasing (561 >= 1000 >= 2500): r31 {dec31}, r42 {dec42}"
          f"  [edge@2500: {ns(e31_25,5)}/{ns(e42_25,5)}]")
# W7: sup = geometric limit at lam = 0.89 (finite-m below, increasing in m)
t31 = t42 = jm = mp.mpf(-1)
for ws in SCAN['W7']:
    r31, r42 = ratios(561, mp.mpf(ws))
    t31 = max(t31, r31); t42 = max(t42, r42); jm = max(jm, r31*r31 - r42/2)
print(f"  W7 : max on 561-scan r31 = {ns(t31,5)}, r42 = {ns(t42,5)} (at the lam = 0.89 corner)")
corner = []
for m in (561, 1581, 5000):
    r31, r42 = ratios(m, mp.mpf('0.89')*m)
    corner.append((m, r31, r42))
    print(f"       corner (m={m}, lam=0.89): r31 = {ns(r31,6)}, r42 = {ns(r42,6)}")
g31 = r31geo(mp.mpf('0.89')); g42 = r42geo(mp.mpf('0.89'))
inc = all(corner[i][1] < corner[i+1][1] and corner[i][2] < corner[i+1][2] for i in range(2))
below = all(r31 < g31 and r42 < g42 for _, r31, r42 in corner)
mono_lam = all(r31geo(mp.mpf(a)) < r31geo(mp.mpf(b)) and r42geo(mp.mpf(a)) < r42geo(mp.mpf(b))
               for a, b in [('0.1','0.3'),('0.3','0.5'),('0.5','0.7'),('0.7','0.89')])
print(f"       m-INcreasing toward the geometric limit: {inc};  all finite-m below limit: {below};"
      f"  geo curves lam-increasing on (0, 0.89]: {mono_lam}")
TSUP['W7'] = (g31, g42); JMAX['W7'] = jm
print(f"       => T31sup(W7) = r31geo(0.89) = {ns(g31,6)}, T42sup(W7) = r42geo(0.89) = {ns(g42,6)} (sup, not attained)")
print("  NOTE (sl4pe-numerics F1): W1-W6b sups are attained AT m = 561 (m-direction decreasing,")
print("  checked above at three m per band edge); no uniform 5e-4 limit-gap budget is used anywhere.")

print()
print("== [D] DESIGN: per-band equal-margin targets, x = min(row-cap @ 0.98, 1.35) ==")
def row_at(W, x, m=561):
    T31, T42 = TSUP[W]
    b = mkband(W, x*T31, x*T42)
    if W == 'W1':
        return max(cellrow(m, x*T31, x*T42), R2bound(700, x*T31, x*T42))
    return C.row(b, m)[0]
NEW = {}
for W in ['W1','W2','W3','W4','W5','W6b','W7']:
    lo, hi = mp.mpf(1), mp.mpf(4)
    for _ in range(60):
        mid = (lo+hi)/2
        if row_at(W, mid) <= RESERVE: lo = mid
        else: hi = mid
    xcap = lo; xuse = min(xcap, CAP)
    T31, T42 = TSUP[W]
    R31n = mp.mpf(math.floor(float(xuse*T31)*100))/100     # floor to 2 dp (safe direction)
    R42n = mp.mpf(math.floor(float(xuse*T42)*100))/100
    NEW[W] = (R31n, R42n)
    m31 = (R31n/T31 - 1)*100; m42 = (R42n/T42 - 1)*100
    print(f"  {W:3s}: x_cap(row<=0.98) = {ns(xcap,5)}  x_used = {ns(xuse,5)}"
          f"  ->  R31* = {ns(R31n,4)} (margin {ns(m31,4)}%), R42* = {ns(R42n,4)} (margin {ns(m42,4)}%)")
print("  (W7 designed with C5*(W7) = 0.50, the single (S2) adjustment -- block [S2];")
print("   W1 capped by BOTH its rungs: cell rung at 561 and Lemma R.2 tail at 700.)")

print()
print("== [C] CHAIN CERTIFICATE with the new targets ==")
worst561 = mp.mpf(0); rows_tbl = {}
for m in (561, 601, 1581):
    vals = []
    for W in ['W2','W3','W4','W5','W6b','W7']:
        R31n, R42n = NEW[W]
        tot, _, _ = C.row(mkband(W, R31n, R42n), m)
        vals.append((W, tot))
    rows_tbl[m] = dict(vals)
    print(f"  m={m}:  " + "  ".join(f"{W}={ns(t,6)}" for W, t in vals))
mono = all(rows_tbl[561][W] >= rows_tbl[601][W] >= rows_tbl[1581][W]
           for W in ['W2','W3','W4','W5','W6b','W7'])
ok561 = all(rows_tbl[561][W] <= RESERVE for W in rows_tbl[561])
print(f"  all W2-W7 rows at 561 <= 0.98: {ok561};  m-monotone spot (561 >= 601 >= 1581): {mono}")
print("  (structural m-monotonicity: every dec/far/X entry is the same closed form the")
print("   wave-4/5 referees certified nonincreasing on the used range; the new constants")
print("   scale terms without changing any m-dependence.)")
R31n, R42n = NEW['W1']
wc = mp.mpf(-1); wat = None; allc = True
for m in range(561, 700):
    rb = cellrow(m, R31n, R42n)
    if rb > wc: wc = rb; wat = m
    if rb > 1: allc = False
print(f"  W1 cell rung, every integer m in [561, 699]: worst = {ns(wc,6)} at m = {wat};  all <= 1: {allc}"
      f"  (<= 0.98: {wc <= RESERVE})")
r2vals = [(m, R2bound(m, R31n, R42n)) for m in (700, 750, 1000, 1581)]
print("  W1 Lemma R.2 tail (new constants): " +
      "  ".join(f"m={m}: {ns(v,6)}" for m, v in r2vals) +
      f"   (B(m) nonincreasing for m >= 142.05)")
worst_all = max(max(rows_tbl[561].values()), wc, r2vals[0][1])
cstar = 20*worst_all
w1581 = max(max(rows_tbl[1581].values()), r2vals[3][1])
c1581 = 20*w1581
print(f"  COMPOSED worst row bound on m >= 561 = {ns(worst_all,6)}  ->  C*(m >= 561) = {ns(cstar,6)} <= 20: {cstar <= 20}")
print(f"  m >= 1581: worst row = {ns(w1581,6)}  ->  C*(m >= 1581) = {ns(c1581,6)} <= 136: {c1581 <= 136}"
      f"  (headroom {ns(136/c1581,4)}x)")

print()
print("== [E] THEOREM E RE-CERTIFICATION (exact Fractions; port of e1) with new targets ==")
M0 = 561; S0f = F(1122800, 7921); E0 = 1/S0f
CA = {'W1': F(28,100), 'W2': F(35,100), 'W3': F(42,100), 'W4': F(52,100),
      'W5': F(60,100), 'W6b': F(70,100), 'W7': F(80,100)}
WMAX = {'W1': F(5), 'W2': F(6), 'W3': F(8), 'W4': F(10), 'W5': F(20), 'W6b': F(40), 'W7': None}
J0NEW = {}; REMNEW = {}
allE = True
for W in ['W1','W2','W3','W4','W5','W6b','W7']:
    R31 = F(int(round(float(NEW[W][0])*100)), 100)
    R42 = F(int(round(float(NEW[W][1])*100)), 100)
    A0 = CA[W]*M0
    Lam = (WMAX[W]/M0) if WMAX[W] is not None else F(89,100)
    Jst = R42/2 + F(3,10)*R31**2
    R42d = max(R42, 2*Jst)
    bb = R42d/(24*A0); a2b = R31**2/(36*A0); cb = a2b/2
    xb = 3*bb + 15*cb; sb = 6*bb + 30*cb
    db = 2*xb + xb**2 + 9*E0*a2b
    Dlo = (1-xb)**2 - 9*E0*a2b
    eb_ = E0/(1-E0); ph = (eb_ + db)/(1 - db)
    Cb_hi = 6*(2+sb); Cb_lo = (6-E0)*(2-sb)
    e_b = max(Cb_hi/24 - F(1,2), F(1,2) - Cb_lo/24)
    Ca_hi = 9 - (45-15*E0)*(1-sb/2); Ca_lo = 9 - 6*E0 - 45*(1+sb/2)
    e_a = max(abs(Ca_hi+36), abs(Ca_lo+36))/36
    M0cap = max(R42/2, Jst)
    Mdev = e_b*R42d + e_a*R31**2
    REM2 = (1+ph)*Mdev + ph*M0cap
    d1 = Lam**2*E0/(6*(1-E0/4))
    REMs = REM2 + d1; J0n = Jst - REMs
    upok = (REMs <= F(3,10)*R31**2)
    posok = (Dlo > 0) and (1 - 3*bb - 15*cb > 0) and (1 - xb - (a2b + 9*E0)/2 > 0)
    allE = allE and upok and posok
    J0NEW[W] = J0n; REMNEW[W] = REMs
    print(f"  {W:3s}: J* = {float(Jst):.6g}  REM* = {float(REMs):.6g}  J0 = {float(J0n):.6g}"
          f"   REM* <= 0.3 R31*^2: {upok}   positivity(D, qhat): {posok}")
print(f"  exact J0 fractions: " + " ; ".join(
      f"{W}={J0NEW[W].numerator}/{J0NEW[W].denominator}" for W in J0NEW))
print(f"  ALL Theorem-E side conditions hold at the new targets: {allE}")

print()
print("== [J] (S3) RECALIBRATION: measured J max (m = 561 scan) vs the NEW J0(W) ==")
for W in ['W1','W2','W3','W4','W5','W6b','W7']:
    j0 = mp.mpf(J0NEW[W].numerator)/J0NEW[W].denominator
    marg = (1 - JMAX[W]/j0)*100
    print(f"  {W:3s}: J_max(561) = {ns(JMAX[W],5)}  vs J0_new = {ns(j0,6)}   margin {ns(marg,4)}%")
jgeo = g31*g31 - g42/2
j07 = mp.mpf(J0NEW['W7'].numerator)/J0NEW['W7'].denominator
print(f"  W7 geometric-limit J at the corner = {ns(jgeo,5)} vs J0_new = {ns(j07,6)}"
      f"  (margin {ns((1-jgeo/j07)*100,4)}%; J INcreases in m on W7 -- budget off the limit)")

print()
print("== [B] BOOTSTRAP (referee M2 chord/monotone-iteration) at the NEW worst rows ==")
dboot = mp.mpf('0.0350') + 1/(2*mp.mpf('141.7497'))
print(f"  d = dHe + dq = {ns(dboot,6)};  INFL/QUADF validity at m >= 561: 20/561 + d = "
      f"{ns(mp.mpf(20)/561 + dboot,5)} <= 1 - 1/1.10 = {ns(1 - 1/mp.mpf('1.10'),5)} (INFL) "
      f"and <= 0.09 (QUADF): {mp.mpf(20)/561 + dboot <= min(1 - 1/mp.mpf('1.10'), mp.mpf('0.09'))}")
def boot(name, m, tot, main, cAd):
    B0 = mp.mpf(20)/m
    mainc = main/(20*mp.mpf(cAd))*mp.mpf('1.09')
    infc = tot - mainc
    def G(x):
        I = 1/(1 - x - dboot)
        return B0*(mainc*(1 + x + dboot)/mp.mpf('1.09')
                   + infc*(I/mp.mpf('1.10'))*((1 + x + dboot)/mp.mpf('1.09')))
    gB = G(B0); lo2, hi2 = B0, mp.mpf('0.96') - dboot
    for _ in range(80):
        mid = (lo2+hi2)/2
        if G(mid) <= mid: lo2 = mid
        else: hi2 = mid
    print(f"  {name}: tot = {ns(tot,5)}  G(20/m) = {ns(gB,6)} < 20/m = {ns(B0,6)}: {gB < B0}"
          f" (margin {ns((1-gB/B0)*100,4)}%);  x_seed = {ns(lo2,5)} >= 0.89: {lo2 >= mp.mpf('0.89')}")
    return gB < B0 and lo2 >= mp.mpf('0.89')
okB = True
for W in ['W2','W3','W4','W5','W6b','W7']:
    R31n, R42n = NEW[W]
    b = mkband(W, R31n, R42n)
    tot, parts, _ = C.row(b, 561)
    okB = boot(f"{W} @ m=561", 561, tot, parts['main'], b[6]) and okB
R31n, R42n = NEW['W1']
main1 = R42n/2 + mp.mpf('0.3')*R31n**2 + (mp.mpf(5)/700)**2/2
okB = boot("W1 @ m=700 (R.2 tail row)", 700, R2bound(700, R31n, R42n), main1, '0.28') and okB
main1c = R42n/2 + mp.mpf('0.3')*R31n**2 + (mp.mpf(5)/561)**2/2
okB = boot("W1 @ m=561 (cell-rung row)", 561, cellrow(561, R31n, R42n), main1c, '0.28') and okB
print(f"  BOOTSTRAP closes from the (S4) seed 0.89 at every new worst row: {okB}")

print()
print("== [S2] (S2)-CONSISTENCY: C5* table and the single W7 adjustment ==")
print("  C5*(W): W1-W6b UNCHANGED = 0.05/0.06/0.08/0.10/0.15/0.25;  W7: 0.80 -> 0.50")
lam89 = mp.mpf('0.89')
s2c, k3c, k4c = cums(561, lam89)
k5c = 561*phi5(lam89)
for j in range(1, 562):
    jl = j*lam89
    if jl > 140 and j > 1: break
    k5c -= j**5*phi5(jl)
c5lead561 = abs(k5c)*lam89**3/(120*s2c)
c5geo = phi5(lam89)/phis(lam89)[0]*lam89**3/120
print(f"  kappa_5 leading-order C5 estimate at the W7 corner: m=561: {ns(c5lead561,5)};"
      f"  geometric limit: {ns(c5geo,5)}  [recorded measured truth max: 0.2104]")
print(f"  => C5*(W7) = 0.50 keeps a {ns(mp.mpf('0.50')/mp.mpf('0.2104'),4)}x margin over the recorded W7 truth"
      f" (was {ns(mp.mpf('0.80')/mp.mpf('0.2104'),4)}x); W1-W6b margins untouched.")
print("  ledger C5-acceptance with the NEW targets (largest C5 the row absorbs at row = 1):")
for W in ['W2','W3','W4','W5','W6b','W7']:
    R31n, R42n = NEW[W]
    c5t = mp.mpf(dict((f[0], f[6]) for f in FRAME)[W])
    lo, hi = c5t, mp.mpf('3.0')
    for _ in range(60):
        mid = (lo+hi)/2
        if C.row(mkband(W, R31n, R42n, C5=mid), 561)[0] <= 1: lo = mid
        else: hi = mid
    print(f"    {W:3s}: acceptance C5 = {ns(lo,4)} = {ns(lo/c5t,4)}x of target {ns(c5t,3)}")
R31n, R42n = NEW['W1']
lo, hi = mp.mpf('0.05'), mp.mpf('3.0')
for _ in range(60):
    mid = (lo+hi)/2
    if max(cellrow(561, R31n, R42n, C5=mid), R2bound(700, R31n, R42n, C5=mid)) <= 1: lo = mid
    else: hi = mid
print(f"    W1 : acceptance C5 = {ns(lo,4)} = {ns(lo/mp.mpf('0.05'),4)}x of target 0.05 (binding rung: R.2 @ 700)")

print()
print("== FINAL TABLE (old -> new; margin = min clause margin vs truth sup over m >= 561) ==")
for W in ['W1','W2','W3','W4','W5','W6b','W7']:
    T31, T42 = TSUP[W]; R31n, R42n = NEW[W]
    o31, o42 = OLD[W]
    m31 = (R31n/T31 - 1)*100; m42 = (R42n/T42 - 1)*100
    mo31 = (mp.mpf(o31)/T31 - 1)*100; mo42 = (mp.mpf(o42)/T42 - 1)*100
    print(f"  {W:3s}: R31* {o31} -> {ns(R31n,4)}  R42* {o42} -> {ns(R42n,4)}"
          f"   old margins {ns(mo31,4)}%/{ns(mo42,4)}%  ->  NEW {ns(m31,4)}%/{ns(m42,4)}%"
          f"   [min {ns(min(m31,m42),4)}%]")
wmarg = min(min((NEW[W][0]/TSUP[W][0]-1), (NEW[W][1]/TSUP[W][1]-1)) for W in NEW)*100
print(f"  WORST-BAND (S1) PROOF MARGIN: {ns(wmarg,4)}%  (was 2.94% -- W7 r42 vs its geometric limit)")
print(f"  C*(m >= 561) = {ns(cstar,6)} <= 20;  C*(m >= 1581) = {ns(c1581,6)} <= 136;  ALL CHECKS PASS: "
      f"{gok and ok561 and mono and allc and allE and okB and cstar <= 20 and c1581 <= 136}")
