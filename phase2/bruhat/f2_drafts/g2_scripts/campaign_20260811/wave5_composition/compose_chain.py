#!/usr/bin/env python3
# compose_chain.py -- wave-5 COMPOSITION check: CL(79, 20, 0.89) at m >= 561,
# assembled from Theorem SL4'-R (repaired, two-referee) + Theorem SL3'
# (two-referee) + the SL-sliver closure (two-referee) + Theorem E (wave5_sl4pe,
# two-referee) + Theorem X.1 (wave5_sl4px, two-referee).
# End-to-end verification of the composed constant chain:
#   [A] exact harness coverage [4, 560]  (threshold shift to m >= 561)
#   [B] the seven ledger rows at m = 401 (reference) and at the operative
#       threshold m = 561; W2-W7 m-monotonicity spot checks
#   [C] the W1 closure ladder on m >= 561 (Fact R.G probes re-run at the
#       sentinels; Lemma R.2 tail bound recomputed from its closed form)
#   [D] the COMPOSED effective constant C* on m >= 561 vs the budget 20,
#       and at m >= 1581 vs the relaxed budget 136
#   [E] eta-pricing interface consistency (wave5_sl4pe J*/REM*/J0 vs the
#       ledger's main-row pricing)
#   [F] sliver far-entry headroom at 561 + the X.2 interval cap
# Row machinery: sl4pr_common.py (the twice-validated engine: referee-rebuilt
# from closed forms to < 5e-5 in wave 4; byte-audited in wave 5).
# mpmath dps-40 point-evaluation class (house-approved); harness parse is
# exact string arithmetic.
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'wave5_sl4prepair'))
import mpmath as mp
from sl4pr_common import (BANDS, row, far_ent, X_w6, INFL, QUADF, SQ2PI, C1T,
                          e_R5n, e_R5d, e_cube, e_cross, e_midn, e_midd, efac)
mp.mp.dps = 40

HERE = os.path.dirname(os.path.abspath(__file__))
SCR  = os.path.join(HERE, '..')

print("[A] exact harness coverage (threshold shift)")
rows = {}
overall = None
for fn, rng in ((os.path.join(SCR, 'wave2_repairs', 'results_m540.txt'), (4, 481)),
                (os.path.join(SCR, 'harness_m560',  'results_m560.txt'), (482, 560))):
    with open(fn) as f:
        for line in f:
            if line.startswith('# OVERALL'):
                overall = line.rstrip('\n')
            ls = line.strip()
            if not ls or ls.startswith('#'):
                continue
            parts = ls.split()
            if len(parts) >= 8 and parts[0].isdigit():
                m = int(parts[0])
                if rng[0] <= m <= rng[1]:
                    rows[m] = parts[-1]
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

print("\n[B] the seven ledger rows: m = 401 (SL4'-R certification) and m = 561 (operative)")
vals = {}
for mval in (401, 561, 601, 1581):
    vals[mval] = {}
    for b in BANDS:
        name = b[0]
        if name == 'W1':
            continue  # W1 handled by the ladder in [C]
        tot, parts, mono = row(b, mval)
        vals[mval][name] = tot
    line = "  m=%4d:  " % mval + "  ".join("%s=%s" % (n, mp.nstr(vals[mval][n], 5))
                                           for n in ('W2', 'W3', 'W4', 'W5', 'W6b', 'W7'))
    print(line)
ok_ref = (abs(vals[401]['W5'] - mp.mpf('0.9891')) < 5e-4 and
          abs(vals[401]['W7'] - mp.mpf('0.9808')) < 5e-4)
print("  reference reproduction at 401: W5 = %s (~0.9891), W7 = %s (~0.9808): %s"
      % (mp.nstr(vals[401]['W5'], 5), mp.nstr(vals[401]['W7'], 5), ok_ref))
mono_spot = all(vals[561][n] >= vals[601][n] >= vals[1581][n]
                for n in ('W2', 'W3', 'W4', 'W5', 'W6b', 'W7'))
ok_B = all(vals[561][n] <= 1 for n in vals[561]) and mono_spot
print("  all W2-W7 rows at m = 561 <= 1: %s;  m-monotone spot (561 >= 601 >= 1581): %s"
      % (all(vals[561][n] <= 1 for n in vals[561]), mono_spot))
w27max561 = max(vals[561].values())
w27arg    = max(vals[561], key=vals[561].get)
print("  worst W2-W7 row at m = 561: %s (%s)" % (mp.nstr(w27max561, 6), w27arg))

print("\n[C] W1 closure ladder on m >= 561")
b1 = BANDS[0]
wprobes = ['4.000000001', '4.001', '4.01', '4.05', '4.10', '4.25', '4.50', '4.75', '5.00']
worstRG = mp.mpf(0); worstat = None; monoall = True
for mval in (561, 650, 699):
    mx = mp.mpf(0); mxw = None
    for ws in wprobes:
        tot, parts, mono = row(b1, mval, wX=mp.mpf(ws))
        monoall = monoall and mono
        if tot > mx: mx, mxw = tot, ws
        if tot > worstRG: worstRG, worstat = tot, (mval, ws)
    print("  m=%d: worst probe row = %s at w = %s  (all <= 1: %s)"
          % (mval, mp.nstr(mx, 6), mxw, mx <= 1))
print("  Fact R.G sentinel reproduction: worst = %s at (m, w) = %s;"
      % (mp.nstr(worstRG, 6), worstat))
print("  X_w6 monotone-in-tau flag (Theorem X.1, now PROVED) at every probe: %s" % monoall)

def r2_bound(mval):
    # Lemma R.2 closed form (wave4_sl4p_repaired sec 5.4), inputs W.6 pointwise
    # + Lemma R.1 floor 0.0176 + C.1 + A2 + SL1'-w + SL4'-E + Theorem SL3'
    # (maths-referee M1: SL3' is load-bearing via gamma*(W1) = 0.42 in dec).
    m = mp.mpf(mval)
    B = (mp.mpf('0.19332')*m**mp.mpf('2.5') + mp.mpf('0.21863')*m**mp.mpf('1.5')) \
        * mp.e**(-mp.mpf('0.0176')*m)
    A0 = mp.mpf('0.28')*m
    lammax = mp.mpf(5)/m
    main = mp.mpf('0.8')/2 + mp.mpf('0.3')*mp.mpf('1.0')**2 + lammax**2/2
    dec = main + INFL*(e_R5n('0.05', A0) + e_cube('1.0', A0)
                       + e_cross('1.0', '0.8', A0) + e_midn(mp.mpf('0.42'), A0)
                       + e_R5d('0.05', A0) + e_midd(mp.mpf('0.42'), A0))
    Fn, Fd = far_ent(4, mval)
    return (1 + QUADF)*(dec/(20*mp.mpf('0.28')) + INFL*(B + Fn + Fd)/20), B, dec

rb700, B700, dec700 = r2_bound(700)
rb1000, _, _ = r2_bound(1000)
rb1581, _, _ = r2_bound(1581)
print("  Lemma R.2 recomputed: m=700: B = %s, dec_W1 = %s, W1 row bound = %s (<= 0.9115: %s)"
      % (mp.nstr(B700, 6), mp.nstr(dec700, 6), mp.nstr(rb700, 6), rb700 <= mp.mpf('0.9115')))
print("                        m=1000: %s   m=1581: %s   (B nonincreasing for m >= 142.05)"
      % (mp.nstr(rb1000, 6), mp.nstr(rb1581, 6)))
ok_C = (worstRG <= 1 and monoall and rb700 <= mp.mpf('0.9115')
        and abs(rb700 - mp.mpf('0.911407')) < 1e-5)

print("\n[D] the COMPOSED effective constant")
# certified worst row bound on m >= 561:
#   W2-W7: values at 561 (nonincreasing in m; [D3] scans + analytic thresholds)
#   W1 on [561, 699]: Fact R.G (grid class; worst probe above) -- and, entirely
#     independent of SL4'-X and of the w-grid, the maths referee's M3 per-cell
#     bound (worst 0.416537 at 561)
#   W1 on m >= 700: Lemma R.2 bound (nonincreasing; worst 0.911407 at 700)
w1_561_699 = worstRG
w1_700up   = rb700
comp_worst = max(w27max561, w1_561_699, w1_700up)
Cstar_561  = 20*comp_worst
print("  segment worsts: W2-W7@561 = %s | W1[561,699] = %s | W1[700,inf) = %s"
      % (mp.nstr(w27max561, 6), mp.nstr(w1_561_699, 6), mp.nstr(w1_700up, 6)))
print("  composed worst row bound on m >= 561 = %s  ->  C*(m >= 561) = %s <= 20: %s"
      % (mp.nstr(comp_worst, 6), mp.nstr(Cstar_561, 6), Cstar_561 <= 20))
# m >= 1581 vs the relaxed budget 136 (wp3-a2 sec 6.1 second clause):
w27max1581 = max(vals[1581].values())
comp1581   = max(w27max1581, rb1581)
Cstar_1581 = 20*comp1581
print("  m >= 1581: worst W2-W7 row = %s (%s), W1 tail bound = %s"
      % (mp.nstr(w27max1581, 6), max(vals[1581], key=vals[1581].get), mp.nstr(rb1581, 6)))
print("  C*(m >= 1581) = %s <= 136: %s   (headroom %sx)"
      % (mp.nstr(Cstar_1581, 6), Cstar_1581 <= 136, mp.nstr(136/Cstar_1581, 4)))
ok_D = (Cstar_561 <= 20 and Cstar_1581 <= 136)
# reference: the SL4'-R theorem-level constant at its certification point m = 401
print("  (reference: SL4'-R certification at m = 401: C*_eff = 20 x %s = %s <= 20)"
      % (mp.nstr(vals[401]['W5'], 5), mp.nstr(20*vals[401]['W5'], 5)))

print("\n[E] eta-pricing interface (wave5_sl4pe Theorem E vs the ledger main row)")
R31s = ['1.0', '1.2', '1.5', '1.7', '2.0', '2.1', '2.2']
R42s = ['0.8', '1.4', '2.6', '3.5', '5.2', '6.0', '6.6']
REMs = ['0.017058', '0.029319', '0.05938', '0.080548', '0.13207', '0.14494', '0.15603']
J0s  = ['0.682942', '1.10268', '1.91562', '2.53645', '3.66793', '4.17806', '4.59597']
ok_E = True
for i, name in enumerate(['W1', 'W2', 'W3', 'W4', 'W5', 'W6b', 'W7']):
    Jstar = mp.mpf(R42s[i])/2 + mp.mpf('0.3')*mp.mpf(R31s[i])**2
    slack = mp.mpf(REMs[i]) <= mp.mpf('0.3')*mp.mpf(R31s[i])**2
    match = abs((Jstar - mp.mpf(REMs[i])) - mp.mpf(J0s[i])) < 2e-5
    ok_E = ok_E and slack and match
    if name in ('W1', 'W7'):
        print("  %s: J* = %s;  J* - REM* = %s vs quoted J0 = %s (match: %s);  REM* <= 0.3 R31*^2: %s"
              % (name, mp.nstr(Jstar, 5), mp.nstr(Jstar - mp.mpf(REMs[i]), 6), J0s[i], match, slack))
print("  all 7 bands: J0 = J* - REM* consistent AND REM* <= 0.3 R31*^2: %s" % ok_E)
# the ledger main entry is exactly J* + lammax^2/2 = Theorem E's price bracket
# (exact-rational check; the ledger evaluates the same expression in mpmath):
from fractions import Fraction as Fr
main7F  = Fr(66, 10)/2 + Fr(3, 10)*Fr(22, 10)**2 + Fr(89, 100)**2/2
Jstar7F = Fr(66, 10)/2 + Fr(3, 10)*Fr(22, 10)**2
exact7  = (main7F == Jstar7F + Fr(89, 100)**2/2 == Fr(514805, 100000))
ok_E = ok_E and exact7
print("  ledger main(W7) = R42*/2 + 0.3 R31*^2 + lam_max^2/2 = J*(W7) + 0.89^2/2 = %s (exact Fraction)"
      % float(main7F))
print("  (exactly 4.752 + 0.39605 = 5.14805: %s; the sl4pe maths referee's '5.148' is 3-dp display)"
      % exact7)

print("\n[F] sliver far-entry headroom at the operative threshold + X.2 cap")
m = mp.mpf(561)
farp = SQ2PI*m**mp.mpf('5.5')*mp.e**(-mp.mpf('0.0741')*m)/mp.mpf(4)**3
print("  far'(561, 4) = %s  (slot 0.05; headroom %sx  [SLV note: 4.556e-05, 1097.6x])"
      % (mp.nstr(farp, 4), mp.nstr(mp.mpf('0.05')/farp, 5)))
tcap = 2*mp.asin(mp.sinh(mp.mpf('0.89')/2))/mp.mpf('0.89')
print("  tau_0(0.89)/0.89 = %s <= 1.074 (Cor X.2 edge): %s" % (mp.nstr(tcap, 9), tcap <= mp.mpf('1.074')))
ok_F = (farp <= mp.mpf('0.05') and tcap <= mp.mpf('1.074'))

print("\n== COMPOSED-CHAIN VERDICT ==")
allok = ok_A and ok_ref and ok_B and ok_C and ok_D and ok_E and ok_F
print("  [A] harness/threshold: %s  [B] rows@561: %s  [C] W1 ladder: %s  [D] C* budgets: %s  [E] eta interface: %s  [F] sliver/X.2: %s"
      % (ok_A, ok_B, ok_C, ok_D, ok_E, ok_F))
print("  ALL CHECKS PASS: %s" % allok)
print("  NOTE: this certifies the IMPLICATION chain and its constants only.")
print("  CL(79, 20, 0.89) at m >= 561 remains CONDITIONAL on the named open")
print("  hypotheses (S1)-(S4) of CL_composition_20260812.md sec 4 (SL1'-w(i),")
print("  SL1'-w(ii), SL4'-E-J = (E3), and the SL4'.6/.7 bootstrap seed).")
