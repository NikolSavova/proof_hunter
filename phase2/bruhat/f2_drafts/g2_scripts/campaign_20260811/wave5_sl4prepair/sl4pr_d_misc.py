#!/usr/bin/env python3
# sl4pr_d_misc.py -- wave-5 SL4' repair, script [D]: the remaining referee
# findings F3/F4/F5/F6/F7 of referee_numerics_wave4_sl4p.md, plus the exact
# harness-coverage parse that the mootness corollary consumes.
#
# [D1] (F3) SL4'-E eta pricing at the band RIGHT edges the prover's 17-point
#      set missed: worst ratio (expect 0.6579 at w = 5.0), all <= 1, k4 > 0.
#      Machinery = sl4p_nc2_eta.py verbatim (orphan Part A Hermite forms).
# [D2] (F5) the efac "iff" boundary: true value 4(1 - e^{-1/4}) = 0.88480;
#      0.8464 remains a SAFE sufficient cutoff.
# [D3] (F6) per-entry A-monotonicity: thresholds and a scan on the USED range
#      A >= 112.28 (= 0.28*401); the tier-1 mid entry is NOT decreasing on
#      [32, 45.6) (referee's point) but is on A >= 46.
# [D4] (F7) the (4.05, 401) share decomposition with an EXPLICIT convention
#      (replaces the unreproducible "share 0.68").
# [D5] (F4) C5*-slack scoping: W1's "accepts 0.4" holds at w = 4.30, FAILS at
#      the sliver edge w = 4.10; W6b slack is 1.6x (0.4 vs 0.25); W5 range.
# [D6] exact parse of the harness results files (mootness input): zero
#      non-PASS rows, contiguous coverage of [401, 560] (and [4, 560]).
import mpmath as mp
from sl4pr_common import BANDS, row, X_w6, far_ent, e_midn, e_Xn_tier2, e_Xd_tier2, INFL, QUADF
mp.mp.dps = 30

# ---------- [D1] eta machinery (sl4p_nc2_eta.py verbatim) ----------
def factor_cums(j, lam):
    ws = [mp.e**(-lam*i) for i in range(j)]
    Z = mp.fsum(ws)
    m1 = mp.fsum(i*w for i, w in enumerate(ws))/Z
    c2 = mp.fsum((i-m1)**2*w for i, w in enumerate(ws))/Z
    c3 = mp.fsum((i-m1)**3*w for i, w in enumerate(ws))/Z
    c4 = mp.fsum((i-m1)**4*w for i, w in enumerate(ws))/Z - 3*c2**2
    return m1, c2, c3, c4
def sum_cums(m, lam):
    mu = k2 = k3 = k4 = mp.mpf(0)
    for j in range(1, m+1):
        a, b, c, d = factor_cums(j, lam)
        mu += a; k2 += b; k3 += c; k4 += d
    return mu, k2, k3, k4
def He(n, x):
    if n == 3: return x**3 - 3*x
    if n == 4: return x**4 - 6*x**2 + 3
    if n == 6: return x**6 - 15*x**4 + 45*x**2 - 15
def qhat(d, s2, k3, k4):
    g = mp.e**(-d*d/(2*s2))/mp.sqrt(2*mp.pi*s2)
    z = d/mp.sqrt(s2)
    a = k3/(6*s2**mp.mpf('1.5')); b4 = k4/(24*s2**2); c6 = k3**2/(72*s2**3)
    return g*(1 + a*He(3, z) + b4*He(4, z) + c6*He(6, z))
def eta_of(s2, k3, k4):
    q0 = qhat(0, s2, k3, k4); qm = qhat(-1, s2, k3, k4); qp = qhat(1, s2, k3, k4)
    return s2*((q0*q0 - qm*qp)/(qm*qp)) - 1
BAND = lambda w: ('W1' if w<=5 else 'W2' if w<=6 else 'W3' if w<=8 else
                  'W4' if w<=10 else 'W5' if w<=20 else 'W6b' if w<=40 else 'W7')
R31S = {'W1':1.0,'W2':1.2,'W3':1.5,'W4':1.7,'W5':2.0,'W6b':2.1,'W7':2.2}
R42S = {'W1':0.8,'W2':1.4,'W3':2.6,'W4':3.5,'W5':5.2,'W6b':6.0,'W7':6.6}

print("== [D1] (F3) SL4'-E eta pricing at the band right edges / missed corners ==")
worst = -mp.inf; warg = None; ok = True; k4pos = True
pts = [(401, '4.001'), (401, '4.9'), (401, '5.0'), (401, '6.0'), (401, '8.0'),
       (401, '10.0'), (401, '20.0'), (401, '40.0'), (401, '356.89'),
       (402, '5.0'), (1000, '5.0')]
for m, wstr in pts:
    w = mp.mpf(wstr); lam = w/m
    mu, s2, k3, k4 = sum_cums(m, lam)
    A = lam*lam*s2; u = 1/A
    e = eta_of(s2, k3, k4)
    b = BAND(float(w))
    price = R42S[b]/2 + mp.mpf('0.3')*R31S[b]**2 + lam*lam/2
    ratio = abs(e)/u/price
    if ratio > worst: worst = ratio; warg = (m, wstr)
    ok = ok and (ratio <= 1); k4pos = k4pos and (k4 > 0)
    print(f"  m={m} w={wstr} [{b}]: |eta|/u = {mp.nstr(abs(e)/u, 5)}  ratio = {mp.nstr(ratio, 5)}"
          f"  k4>0: {k4 > 0}")
print(f"  ALL |eta| <= price*u: {ok};  kappa_4 > 0 everywhere: {k4pos}")
print(f"  worst ratio = {mp.nstr(worst, 5)} at (m, w) = {warg}  [referee C2: 0.6579 at the W1 right edge]")
print(f"  corrected F3 sentence: 'never above 0.66 of its budget; worst 0.6579 at w = 5':"
      f" {worst <= mp.mpf('0.66')}")

print("\n== [D2] (F5) efac boundary ==")
bd = 4*(1 - mp.e**mp.mpf('-0.25'))
ef = lambda C5: (mp.mpf('0.5')/(mp.mpf('0.5')-mp.mpf(C5)/8))**4
print(f"  true 'iff' boundary: efac(C5*) <= e  iff  C5* <= 4(1-e^(-1/4)) = {mp.nstr(bd, 8)}")
print(f"  efac(0.8464) = {mp.nstr(ef('0.8464'), 6)} < e = {mp.nstr(mp.e, 6)}: {ef('0.8464') < mp.e}"
      f"   (0.8464 stays a SAFE sufficient cutoff; W7's C5* = 0.80 < 0.8464)")
print(f"  efac({mp.nstr(bd, 8)}) = {mp.nstr(ef(str(bd)), 8)}  (= e to print precision)")

print("\n== [D3] (F6) A-monotonicity: thresholds and the used range ==")
print(f"  tier-1 mid (g = 0.1317): pure-form A^(3/2)e^(-gA/4) decreasing iff A > 6/g = "
      f"{mp.nstr(6/mp.mpf('0.1317'), 6)} (referee's threshold; SUFFICIENT for the full entry,")
print(f"  whose Mills factor (1+2/(gA)) is decreasing); the full entry's actual peak is at")
g0 = mp.mpf('0.1317'); prev = None; peak = None; A = mp.mpf(20)
while A < 60:
    v = e_midn(g0, A)
    if prev is not None and v < prev and peak is None: peak = A - mp.mpf('0.1')
    prev = v; A += mp.mpf('0.1')
inc_check = e_midn(g0, mp.mpf(32)) < e_midn(g0, mp.mpf(36))
print(f"  A ~ {mp.nstr(peak, 4)}; witness that 'A >= 32' was FALSE: e_midn(32) = "
      f"{mp.nstr(e_midn(g0, mp.mpf(32)), 6)} < e_midn(36) = {mp.nstr(e_midn(g0, mp.mpf(36)), 6)}: {inc_check}")
A0min = mp.mpf('0.28')*401
print(f"  used range: A0 >= 0.28*401 = {mp.nstr(A0min, 6)} (W1) up to 0.85*401 (W7)")
ents = [('mid g=0.42', lambda A: e_midn(mp.mpf('0.42'), A)),
        ('mid g=0.40', lambda A: e_midn(mp.mpf('0.40'), A)),
        ('mid g=0.1317', lambda A: e_midn(mp.mpf('0.1317'), A)),
        ('X tier-2 (Xn+Xd)', lambda A: e_Xn_tier2(A)+e_Xd_tier2(A))]
for name, f in ents:
    prev = None; monotone = True
    A = mp.mpf(112)
    while A <= 3000:
        v = f(A)
        if prev is not None and v > prev: monotone = False
        prev = v; A += 1
    print(f"  {name}: nonincreasing on the used range A in [112, 3000] (step 1): {monotone}")
print(f"  tier-2 X pure-form A^(3/2)e^(-0.64 c2 A) threshold: 1.5/(0.64*0.0871) = "
      f"{mp.nstr(mp.mpf('1.5')/(mp.mpf('0.64')*mp.mpf('0.0871')), 6)} (Mills factor decreasing; sufficient)")
print(f"  far entry: m^5.5 e^(-0.0741 m) decreasing iff m > 5.5/0.0741 = "
      f"{mp.nstr(mp.mpf('5.5')/mp.mpf('0.0741'), 6)} ('m >= 75' safe)")
print("  increasing entries (share rule needs e(A)/A nondecreasing): far is EXACTLY")
print("  linear in A (e/A constant); W1's X is ~A^(5/2) (e/A ~ A^(3/2)): both satisfy it.")

print("\n== [D4] (F7) share decomposition at (w, m) = (4.05, 401), explicit convention ==")
mp.mp.dps = 40
W1 = BANDS[0]
tot, p, _ = row(W1, 401, wX=mp.mpf('4.05'))
Xn, Xd, _ = X_w6(mp.mpf('4.05'), 401, mp.mpf(401))
Fn, Fd = far_ent(4, 401)
decpart = tot - (1+QUADF)*INFL*((Xn+Xd)+(Fn+Fd))/20
Xsh = (1+QUADF)*INFL*(Xn+Xd)/20
Fsh = (1+QUADF)*INFL*(Fn+Fd)/20
print(f"  convention: contribution of each slot to the row value share*(1+q), i.e.")
print(f"  slot*(1+QUADF)*INFL/20 for the A-increasing slots, dec-part/(20*0.28)*(1+QUADF).")
print(f"  row total = {mp.nstr(tot, 6)} (FAIL, inside the trapezoid);")
print(f"  X-share = {mp.nstr(Xsh, 5)};  far-share = {mp.nstr(Fsh, 5)};  dec-share = {mp.nstr(decpart, 5)}"
      f"   [referee D1: 0.9954 / 0.1214 / 0.2743, total 1.3911]")
from sl4pr_common import w6_x
print(f"  m*x(4.05, 0.8) = {mp.nstr(401*w6_x(mp.mpf('4.05'), mp.mpf('0.8'), 401), 6)}"
      f"   [the crossover-limited diagnosis stands; 'share 0.68' is RETIRED]")

print("\n== [D5] (F4) C5*-slack scoping ==")
for wtag, c5 in (('4.10', '0.4'), ('4.30', '0.4'), ('4.10', '0.05')):
    t = row(W1, 401, wX=mp.mpf(wtag), C5o=c5)[0]
    print(f"  W1, m=401, w={wtag}, C5*={c5}: row = {mp.nstr(t, 5)} {'PASS' if t <= 1 else 'FAIL'}")
t6 = row(BANDS[5], 401, C5o='0.4')[0]
print(f"  W6b, m=401, C5*=0.4: row = {mp.nstr(t6, 5)} {'PASS' if t6 <= 1 else 'FAIL'}"
      f"  -> W6b slack = 0.4/0.25 = 1.6x (NOT '2x-8x')")
t5a = row(BANDS[4], 401, C5o='0.15')[0]; t5b = row(BANDS[4], 401, C5o='0.2')[0]
print(f"  W5, m=401: C5*=0.15 row = {mp.nstr(t5a, 5)} {'PASS' if t5a <= 1 else 'FAIL'};"
      f"  C5*=0.20 row = {mp.nstr(t5b, 5)} {'PASS' if t5b <= 1 else 'FAIL'}"
      f"  -> W5 acceptance is 0.15 (the ledger value; the block-[4] grid prints 0.10, its next grid point)")

print("\n== [D6] exact harness-coverage parse (mootness input) ==")
import re
base = '/Users/sihaohuang/Desktop/Coding/proof_hunter/phase2/bruhat/f2_drafts/g2_scripts/campaign_20260811'
cov = {}; bad = []
for fn in (base+'/wave2_repairs/results_m540.txt', base+'/harness_m560/results_m560.txt'):
    for line in open(fn):
        mm = re.match(r'\s*(\d+)\s+\d+\s+\d+\s+\d+\s+\S+\s+\S+\s+\S+\s+(\S+)\s*$', line)
        if mm:
            mval, verdict = int(mm.group(1)), mm.group(2)
            if verdict != 'PASS': bad.append((fn, mval, verdict))
            cov.setdefault(mval, verdict)
print(f"  parsed data rows: {len(cov)};  non-PASS rows: {len(bad)} {bad if bad else ''}")
gaps = [m for m in range(4, 561) if m not in cov]
gaps401 = [m for m in range(401, 561) if m not in cov]
print(f"  coverage [4, 560]: gaps = {gaps if gaps else 'NONE'};  [401, 560]: gaps = {gaps401 if gaps401 else 'NONE'}")
for line in open(base+'/harness_m560/results_m560.txt'):
    if line.startswith('# OVERALL'):
        print(f"  OVERALL line (verbatim): {line.rstrip()}")
print(f"  => M_H = 560; trapezoid m-ranges [401, 462] (route a) and [401, 469] (route b)")
print(f"     are covered: {not gaps401}")
