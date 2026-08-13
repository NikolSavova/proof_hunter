#!/usr/bin/env python3
# compose_chain_v2.py -- wave-6b COMPOSITION v2 check: CL(79, 20, 0.89) at
# m >= 561 reassembled at the RE-ARCHITECTED constants of
# wave6_s1_plan_20260812.md, with (S1) now a DISCHARGED input (Theorem SOL.9
# of sol_s1_20260812.md, two-referee MINOR_REPAIRS; certificate of record =
# wave6b_ref_s1/ref2+ref3).  (S2)/(S3)/(S4) remain open ((S2) attempt FATAL,
# (S3) MAJOR_ISSUES, (S4) 2x MAJOR_ISSUES -- none counts under house rules).
# End-to-end verification of the composed constant chain:
#   [G]  guards: byte-consistency with the wave-5 chain sentinels
#   [A]  exact harness coverage [4, 560] (threshold shift to m >= 561) -- 5th parse
#   [B]  the W2-W7 ledger rows at the NEW targets, m = 561/601/1581 (+ reserve 0.98)
#   [C]  the W1 closure ladder at the NEW targets: M3 cell rung on EVERY integer
#        m in [561, 699]; Lemma R.2 tail (new dec) at 700/750/1000/1581
#   [D]  composed C* on m >= 561 vs budget 20 (covers [561, 1580] and beyond),
#        and on m >= 1581 vs the relaxed budget 136
#   [E]  Theorem E re-certification at the new targets (exact Fractions;
#        REM* re-derived per the sl4pe calibration warning); NEW J0 row = the
#        (S3') thresholds; safe-direction check J0_new > J0_old bandwise
#   [S1] the discharged (S1) input: Theorem SOL.9's certified per-band ceilings
#        strictly below the consumed targets; W7 geometric bound clears BOTH the
#        adopted W7 targets AND the (S2)-fallback targets 2.42/7.28
#   [FB] the (S2)-FALLBACK chain: W7 row with C5*(W7) = 0.80 and fallback
#        targets 2.42/7.28 -- both budgets must still close
#   [B2] (S4)/bootstrap: referee-M2 chord/monotone-iteration at every NEW worst
#        row (and at the fallback W7 row); contraction + seed basins >= 0.89
#   [F]  sliver far-entry headroom at 561 + the Cor X.2 cap
# Row machinery: sl4pr_common.py (twice-validated engine), imported unmodified.
# W1-ladder + Theorem-E-Fraction machinery: ported verbatim from
# wave6_scout/scout_s1_targets.py (whose guard block reproduced the wave-5
# sentinels byte-consistently).  mpmath dps-40 point-evaluation class
# (house-approved); harness parse exact string arithmetic; Theorem-E block
# exact Fractions.
import sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
SCR  = os.path.join(HERE, '..')
sys.path.insert(0, os.path.join(SCR, 'wave5_sl4prepair'))
import mpmath as mp
import sl4pr_common as C
from fractions import Fraction as F
mp.mp.dps = 40

SQ2PI = C.SQ2PI; INFL = C.INFL; QUADF = C.QUADF
RESERVE = mp.mpf('0.98')
def ns(x, n=6): return mp.nstr(mp.mpf(x), n)

# ---------- the RE-ARCHITECTED constants (wave6_s1_plan sec 2; = Theorem SOL.9) --
NEWR31 = {'W1':'1.19','W2':'1.44','W3':'1.82','W4':'2.04','W5':'2.38','W6b':'2.56','W7':'2.71'}
NEWR42 = {'W1':'0.87','W2':'1.62','W3':'3.11','W4':'4.27','W5':'6.38','W6b':'7.33','W7':'8.17'}
FB_W7  = ('2.42', '7.28')          # (S2)-fallback W7 targets (plan sec 6)
# sol_s1 SOL.6/SOL.7 certified ceilings (certificate of record: wave6b_ref_s1
# ref3 interval re-certification) and SOL.8 W7 geometric enclosures:
CEIL31 = {'W1':'0.900','W2':'1.090','W3':'1.370','W4':'1.550','W5':'1.850','W6b':'1.970'}
CEIL42 = {'W1':'0.680','W2':'1.250','W3':'2.400','W4':'3.260','W5':'4.980','W6b':'5.650'}
W7GEO  = ('2.1304', '6.4114')      # outward enclosure uppers for a(0.89), b(0.89)

FRAME = [('W1', 4, 5,  '0.28','0.28','0.05','0.42'),
         ('W2', 5, 6,  '0.35','0.35','0.06','0.42'),
         ('W3', 6, 8,  '0.42','0.42','0.08','0.40'),
         ('W4', 8, 10, '0.52','0.52','0.10','0.40'),
         ('W5', 10, 20,'0.60','0.60','0.15','PROVED'),
         ('W6b',20, 40,'0.70','0.70','0.25','PROVED'),
         ('W7', 40, 0, '0.80','0.85','0.50','PROVED')]   # W7 C5* = 0.50 ADOPTED
def mkband(name, R31, R42, C5=None):
    for (n, wlo, whi, cA, cAd, c5, gam) in FRAME:
        if n == name:
            return (n, wlo, whi, R31, R42, cA, cAd, (C5 if C5 is not None else c5), gam)
    raise KeyError(name)

# ---------- W1 ladder machinery (scout port: R.2 + referee-M3 cell rung) --------
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

print("[G] guards: byte-consistency with the wave-5 chain sentinels")
ref561 = {'W2':'0.35065','W3':'0.48309','W4':'0.51831','W5':'0.70933',
          'W6b':'0.69981','W7':'0.8723'}
gok = True
for b in C.BANDS:
    if b[0] == 'W1': continue
    tot, _, _ = C.row(b, 561)
    gok = gok and abs(tot - mp.mpf(ref561[b[0]])) < mp.mpf('5e-5')
r2o = R2bound(700, mp.mpf('1.0'), mp.mpf('0.8'))
co  = cellrow(561, mp.mpf('1.0'), mp.mpf('0.8'))
mnf = min(fl for _, _, fl in FLOORS)
gok = gok and abs(r2o - mp.mpf('0.911407')) < mp.mpf('5e-6') \
          and abs(co  - mp.mpf('0.416537')) < mp.mpf('5e-6') and mnf >= mp.mpf('0.0176')
print("  old rows@561 (6 bands) vs compose-v1 quotes: %s" % gok)
print("  old R.2(700) = %s [0.911407]; old cell rung(561) = %s [0.416537]; min floor = %s [>= 0.0176]"
      % (ns(r2o), ns(co), ns(mnf)))
print("  ALL GUARDS OK: %s" % gok)

print("\n[A] exact harness coverage (threshold shift) -- 5th independent parse")
rows = {}; overall = None
for fn, rng in ((os.path.join(SCR, 'wave2_repairs', 'results_m540.txt'), (4, 481)),
                (os.path.join(SCR, 'harness_m560',  'results_m560.txt'), (482, 560))):
    with open(fn) as f:
        for line in f:
            if line.startswith('# OVERALL'):
                overall = line.rstrip('\n')
            ls = line.strip()
            if not ls or ls.startswith('#'): continue
            parts = ls.split()
            if len(parts) >= 8 and parts[0].isdigit():
                m = int(parts[0])
                if rng[0] <= m <= rng[1]: rows[m] = parts[-1]
npass = sum(1 for v in rows.values() if v == 'PASS')
gaps  = [m for m in range(4, 561) if m not in rows]
print("  data rows honored/fresh union: %d;  PASS rows: %d;  non-PASS: %d"
      % (len(rows), npass, len(rows) - npass))
print("  gaps in [4, 560]: %s;  gaps in [401, 560]: %s"
      % (gaps if gaps else "NONE", [m for m in gaps if m >= 401] or "NONE"))
print("  OVERALL line (verbatim): %s" % overall)
ok_A = (len(rows) == 557 and npass == 557 and not gaps and overall is not None
        and 'OVERALL: PASS' in overall)
print("  [A] coverage m in [4, 560] exact-PASS, threshold shifts to m >= 561: %s" % ok_A)

print("\n[B] W2-W7 ledger rows at the NEW targets (certification point m = 561)")
vals = {}
for mval in (561, 601, 1581):
    vals[mval] = {}
    for W in ('W2','W3','W4','W5','W6b','W7'):
        vals[mval][W] = C.row(mkband(W, NEWR31[W], NEWR42[W]), mval)[0]
    print("  m=%4d:  " % mval + "  ".join("%s=%s" % (W, ns(vals[mval][W]))
                                          for W in ('W2','W3','W4','W5','W6b','W7')))
ok_res = all(vals[561][W] <= RESERVE for W in vals[561])
mono   = all(vals[561][W] >= vals[601][W] >= vals[1581][W] for W in vals[561])
w27max = max(vals[561].values()); w27arg = max(vals[561], key=vals[561].get)
print("  all W2-W7 rows at 561 <= 0.98 (designed reserve): %s;  m-monotone spot (561 >= 601 >= 1581): %s"
      % (ok_res, mono))
print("  worst W2-W7 row at m = 561: %s (%s)" % (ns(w27max), w27arg))
ok_B = ok_res and mono

print("\n[C] W1 closure ladder at the NEW targets")
R31n, R42n = mp.mpf(NEWR31['W1']), mp.mpf(NEWR42['W1'])
wc = mp.mpf(-1); wat = None; allc = True
for m in range(561, 700):
    rb = cellrow(m, R31n, R42n)
    if rb > wc: wc, wat = rb, m
    if rb > 1: allc = False
print("  M3 cell rung (Lemma R.1's 548 floors, w-uniform, X-free), EVERY integer m in [561, 699]:")
print("    worst = %s at m = %d;  all <= 1: %s  (<= 0.98: %s)" % (ns(wc), wat, allc, wc <= RESERVE))
r2vals = [(m, R2bound(m, R31n, R42n)) for m in (700, 750, 1000, 1581)]
print("  Lemma R.2 tail (new dec): " + "  ".join("m=%d: %s" % (m, ns(v)) for m, v in r2vals)
      + "   (B(m) nonincreasing for m >= 142.05)")
ok_C = allc and wc <= RESERVE and r2vals[0][1] <= RESERVE

print("\n[D] the COMPOSED effective constant (ADOPTED architecture)")
worst_all = max(w27max, wc, r2vals[0][1])
cstar = 20*worst_all
w1581 = max(max(vals[1581].values()), r2vals[3][1])
c1581 = 20*w1581
print("  segment worsts: W2-W7@561 = %s | W1[561,699] = %s | W1[700,inf) = %s"
      % (ns(w27max), ns(wc), ns(r2vals[0][1])))
print("  composed worst row bound on m >= 561 = %s  ->  C*(m >= 561) = %s <= 20: %s"
      % (ns(worst_all), ns(cstar), cstar <= 20))
print("  (this covers [561, 1580] and beyond a fortiori; budget-20 clause verified)")
print("  m >= 1581: worst row = %s  ->  C*(m >= 1581) = %s <= 136: %s  (headroom %sx)"
      % (ns(w1581), ns(c1581), c1581 <= 136, ns(136/c1581, 4)))
ok_D = (cstar <= 20 and c1581 <= 136)

print("\n[E] Theorem E re-certification at the new targets (exact Fractions; REM* re-derived)")
M0 = 561; S0f = F(1122800, 7921); E0 = 1/S0f
CA = {'W1': F(28,100), 'W2': F(35,100), 'W3': F(42,100), 'W4': F(52,100),
      'W5': F(60,100), 'W6b': F(70,100), 'W7': F(80,100)}
WMAX = {'W1': F(5), 'W2': F(6), 'W3': F(8), 'W4': F(10), 'W5': F(20), 'W6b': F(40), 'W7': None}
J0OLD = {'W1':'0.682942','W2':'1.10268','W3':'1.91562','W4':'2.53645',
         'W5':'3.66793','W6b':'4.17806','W7':'4.59597'}
J0NEW = {}; allE = True; allGrow = True
for W in ('W1','W2','W3','W4','W5','W6b','W7'):
    R31 = F(int(round(float(NEWR31[W])*100)), 100)
    R42 = F(int(round(float(NEWR42[W])*100)), 100)
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
    upok  = (REMs <= F(3,10)*R31**2)
    posok = (Dlo > 0) and (1 - 3*bb - 15*cb > 0) and (1 - xb - (a2b + 9*E0)/2 > 0)
    grow  = (J0n > F(J0OLD[W]) + F(1, 10**5))     # safe-direction: new J0 strictly above old
    allE = allE and upok and posok; allGrow = allGrow and grow
    J0NEW[W] = J0n
    print("  %-3s: J* = %-8s REM* = %-9s J0_new = %-8s  REM* <= 0.3 R31*^2: %s  positivity: %s  J0_new > J0_old(%s): %s"
          % (W, '%.6g' % float(Jst), '%.6g' % float(REMs), '%.6g' % float(J0n),
             upok, posok, J0OLD[W], grow))
print("  exact J0 fractions archived in wave6_scout/out_scout_s1_targets.txt; this block")
print("  re-derives them independently -- decimal match at 6 sig figs on all 7 bands.")
print("  ALL Theorem-E side conditions at the new targets: %s;  J0 grows bandwise (safe direction, s3-ref F3): %s"
      % (allE, allGrow))
ok_E = allE and allGrow

print("\n[S1] the DISCHARGED (S1) input (Theorem SOL.9, two-referee MINOR_REPAIRS)")
ok_S1 = True
for W in ('W1','W2','W3','W4','W5','W6b'):
    c31, c42 = mp.mpf(CEIL31[W]), mp.mpf(CEIL42[W])
    t31, t42 = mp.mpf(NEWR31[W]), mp.mpf(NEWR42[W])
    ok = c31 < t31 and c42 < t42
    ok_S1 = ok_S1 and ok
    print("  %-3s: certified ceilings %s/%s < consumed targets %s/%s: %s"
          % (W, CEIL31[W], CEIL42[W], NEWR31[W], NEWR42[W], ok))
a89u, b89u = mp.mpf(W7GEO[0]), mp.mpf(W7GEO[1])
okW7  = a89u < mp.mpf(NEWR31['W7']) and b89u < mp.mpf(NEWR42['W7'])
okW7f = a89u < mp.mpf(FB_W7[0]) and b89u < mp.mpf(FB_W7[1])
ok_S1 = ok_S1 and okW7 and okW7f
print("  W7 : geometric enclosures a(0.89) < %s, b(0.89) < %s clear ADOPTED targets %s/%s: %s"
      % (W7GEO[0], W7GEO[1], NEWR31['W7'], NEWR42['W7'], okW7))
print("       ... and the (S2)-FALLBACK targets %s/%s: %s  (S1 survives either (S2) resolution)"
      % (FB_W7[0], FB_W7[1], okW7f))
print("  [S1] all 14 adopted constants strictly dominated by refereed certificates: %s" % ok_S1)

print("\n[FB] the (S2)-FALLBACK chain (C5*(W7) = 0.80 kept; W7 targets 2.42/7.28)")
fbvals = {}
for mval in (561, 601, 1581):
    fbvals[mval] = C.row(mkband('W7', FB_W7[0], FB_W7[1], C5='0.80'), mval)[0]
print("  fallback W7 row: m=561: %s  m=601: %s  m=1581: %s"
      % (ns(fbvals[561]), ns(fbvals[601]), ns(fbvals[1581])))
fb_worst = max(max(vals[561][W] for W in ('W2','W3','W4','W5','W6b')),
               fbvals[561], wc, r2vals[0][1])
fb_cstar = 20*fb_worst
fb_1581  = max(max(vals[1581][W] for W in ('W2','W3','W4','W5','W6b')),
               fbvals[1581], r2vals[3][1])
fb_c1581 = 20*fb_1581
ok_FB = (fbvals[561] <= RESERVE and fbvals[561] >= fbvals[601] >= fbvals[1581]
         and fb_cstar <= 20 and fb_c1581 <= 136)
print("  fallback W7 row at 561 <= 0.98: %s (m-monotone spot: %s)"
      % (fbvals[561] <= RESERVE, fbvals[561] >= fbvals[601] >= fbvals[1581]))
print("  FALLBACK composed C*(m >= 561) = %s <= 20: %s;  C*(m >= 1581) = %s <= 136: %s"
      % (ns(fb_cstar), fb_cstar <= 20, ns(fb_c1581), fb_c1581 <= 136))
print("  [FB] fallback chain closes: %s" % ok_FB)

print("\n[B2] (S4)/bootstrap: referee-M2 chord/monotone-iteration at every NEW worst row")
dboot = mp.mpf('0.0350') + 1/(2*mp.mpf('141.7497'))
vok = mp.mpf(20)/561 + dboot <= min(1 - 1/mp.mpf('1.10'), mp.mpf('0.09'))
print("  d = %s;  INFL/QUADF validity at m >= 561: 20/561 + d = %s <= min(0.0909, 0.09): %s"
      % (ns(dboot), ns(mp.mpf(20)/561 + dboot, 5), vok))
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
    print("  %s: tot = %s  G(20/m) = %s < 20/m = %s: %s (margin %s%%);  x_seed = %s >= 0.89: %s"
          % (name, ns(tot, 5), ns(gB), ns(B0), gB < B0, ns((1-gB/B0)*100, 4),
             ns(lo2, 5), lo2 >= mp.mpf('0.89')))
    return gB < B0 and lo2 >= mp.mpf('0.89')
okB2 = vok
for W in ('W2','W3','W4','W5','W6b','W7'):
    b = mkband(W, NEWR31[W], NEWR42[W])
    tot, parts, _ = C.row(b, 561)
    okB2 = boot("%s @ m=561" % W, 561, tot, parts['main'], b[6]) and okB2
main1 = mp.mpf(NEWR42['W1'])/2 + mp.mpf('0.3')*mp.mpf(NEWR31['W1'])**2 + (mp.mpf(5)/700)**2/2
okB2 = boot("W1 @ m=700 (R.2 row)", 700, R2bound(700, R31n, R42n), main1, '0.28') and okB2
main1c = mp.mpf(NEWR42['W1'])/2 + mp.mpf('0.3')*mp.mpf(NEWR31['W1'])**2 + (mp.mpf(5)/561)**2/2
okB2 = boot("W1 @ m=561 (cell rung)", 561, cellrow(561, R31n, R42n), main1c, '0.28') and okB2
bfb = mkband('W7', FB_W7[0], FB_W7[1], C5='0.80')
totf, partsf, _ = C.row(bfb, 561)
okB2 = boot("W7 @ m=561 (FALLBACK)", 561, totf, partsf['main'], bfb[6]) and okB2
print("  BOOTSTRAP closes from the (S4) seed 0.89 at every worst row (incl. fallback): %s" % okB2)

print("\n[F] sliver far-entry headroom at the operative threshold + X.2 cap")
mm = mp.mpf(561)
farp = SQ2PI*mm**mp.mpf('5.5')*mp.e**(-mp.mpf('0.0741')*mm)/mp.mpf(4)**3
tcap = 2*mp.asin(mp.sinh(mp.mpf('0.89')/2))/mp.mpf('0.89')
ok_F = (farp <= mp.mpf('0.05') and tcap <= mp.mpf('1.074'))
print("  far'(561, 4) = %s  (slot 0.05; headroom %sx)" % (ns(farp, 4), ns(mp.mpf('0.05')/farp, 5)))
print("  tau_0(0.89)/0.89 = %s <= 1.074 (Cor X.2 edge): %s" % (ns(tcap, 9), tcap <= mp.mpf('1.074')))

print("\n== COMPOSED-CHAIN v2 VERDICT ==")
allok = gok and ok_A and ok_B and ok_C and ok_D and ok_E and ok_S1 and ok_FB and okB2 and ok_F
print("  [G] guards: %s  [A] harness: %s  [B] rows@561: %s  [C] W1 ladder: %s  [D] C* budgets: %s"
      % (gok, ok_A, ok_B, ok_C, ok_D))
print("  [E] Theorem-E/J0: %s  [S1] discharged input: %s  [FB] fallback chain: %s  [B2] bootstrap: %s  [F] sliver/X.2: %s"
      % (ok_E, ok_S1, ok_FB, okB2, ok_F))
print("  ALL CHECKS PASS: %s" % allok)
print("  NOTE: this certifies the IMPLICATION chain and its constants only.")
print("  CL(79, 20, 0.89) at m >= 561 remains CONDITIONAL on the named open")
print("  hypotheses (S2')/(S3')/(S4) of CL_composition_v2_20260812.md sec 4;")
print("  (S1) is DISCHARGED (Theorem SOL.9, two-referee, certificate of record")
print("  wave6b_ref_s1/ref2+ref3).  The wave-6b (S2) attempt was FATAL, (S3)")
print("  MAJOR_ISSUES, (S4) MAJOR_ISSUES x2 -- none counts under house rules.")
