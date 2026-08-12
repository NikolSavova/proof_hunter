#!/usr/bin/env python3
# ref_rp_d_misc.py -- wave-5 numerics referee on wave4_sl4p_repaired:
# remaining audits -- F3/F4/F5/F6 spot re-verification at NEW points, the
# SS2 W2-W4 weakened-C5* remark, and an INDEPENDENT harness-coverage parse
# (different method from the repair's regex) for Corollary R.3's input.
#
# [D1] SL4'-E eta at NEW W1 points in Fact R.G / Cor R.3's load-bearing
#      range (m = 463/561/699): pricing must hold (<= 1); record vs the
#      draft's "never above 0.66" measured-evidence sentence.
# [D2] efac boundary: exact 4(1 - e^{-1/4}) at dps 40; efac at the rounded
#      display value 0.88480 (is it > e? -- display-rounding direction).
# [D3] e_midn(0.1317, .) peak location by fine scan (draft: A ~ 36.7) and
#      strict decrease on [45.5581, 200] step 0.01 (the "6/g sufficient"
#      claim); far-entry threshold 5.5/0.0741.
# [D4] SS2's C5*-acceptance remark at the OTHER bands (not re-checked by the
#      repair scripts): W2 at 0.2, W3 at 0.4, W4 at 0.4 must PASS at m=401;
#      also W3 at 0.8 / W4 at 0.8 (expect FAIL -- the remark's ceiling is
#      honest, not slack).
# [D5] INDEPENDENT harness parse (split-based, not regex): per-file row
#      counts, verdict column check, coverage of [4, 560] and [401, 560],
#      overlap between the two files, the m = 461/462/463 rows verbatim,
#      and the OVERALL line.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'wave5_sl4prepair'))
import mpmath as mp
from sl4pr_common import BANDS, row, e_midn

print("== [D1] SL4'-E eta pricing at NEW W1 points (m = 463/561/699) ==")
mp.mp.dps = 30
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
worst = -mp.inf; warg = None; allok = True; k4ok = True
for (m, wstr) in ((463, '4.0001'), (463, '4.5'), (463, '5.0'),
                  (561, '4.001'), (561, '5.0'), (699, '4.2'), (699, '5.0')):
    w = mp.mpf(wstr); lam = w/m
    mu, s2, k3, k4 = sum_cums(m, lam)
    A = lam*lam*s2; u = 1/A
    e = eta_of(s2, k3, k4)
    price = mp.mpf('0.8')/2 + mp.mpf('0.3')*mp.mpf('1.0')**2 + lam*lam/2   # W1
    ratio = abs(e)/u/price
    allok = allok and ratio <= 1; k4ok = k4ok and k4 > 0
    if ratio > worst: worst = ratio; warg = (m, wstr)
    print(f"  m={m} w={wstr}: ratio = {mp.nstr(ratio, 5)}  k4>0: {k4 > 0}")
print(f"  ALL <= 1 (SL4'-E): {allok};  k4 > 0 everywhere: {k4ok}")
print(f"  worst = {mp.nstr(worst, 5)} at {warg};  still <= 0.66 (draft F3 sentence): {worst <= mp.mpf('0.66')}")

print("\n== [D2] efac boundary display rounding ==")
mp.mp.dps = 40
bd = 4*(1 - mp.e**mp.mpf('-0.25'))
ef = lambda C5: (mp.mpf('0.5')/(mp.mpf('0.5')-mp.mpf(C5)/8))**4
print(f"  4(1-e^(-1/4)) = {mp.nstr(bd, 12)}  (draft displays 0.88480)")
print(f"  efac(0.88480) = {mp.nstr(ef('0.88480'), 12)} vs e = {mp.nstr(mp.e, 12)}"
      f"  -> efac(0.88480) > e: {ef('0.88480') > mp.e}  (display rounds UP past the boundary)")
print(f"  efac(0.8464) = {mp.nstr(ef('0.8464'), 8)} < e: {ef('0.8464') < mp.e}  (working cutoff safe)")

print("\n== [D3] e_midn tier-1 peak and decrease threshold ==")
g0 = mp.mpf('0.1317')
best = -mp.inf; bA = None
A = mp.mpf('30')
while A <= 50:
    v = e_midn(g0, A)
    if v > best: best = v; bA = A
    A += mp.mpf('0.01')
print(f"  peak of e_midn(0.1317, A) on [30, 50] step 0.01: A = {mp.nstr(bA, 6)}  (draft: ~36.7)")
dec_ok = True
A = mp.mpf('45.5581'); prev = e_midn(g0, A)
while A <= 200:
    A += mp.mpf('0.01'); v = e_midn(g0, A)
    if v > prev: dec_ok = False
    prev = v
print(f"  strictly nonincreasing on [45.5581, 200] step 0.01 (6/g sufficiency): {dec_ok}")
print(f"  6/g = {mp.nstr(6/g0, 8)};  far threshold 5.5/0.0741 = {mp.nstr(mp.mpf('5.5')/mp.mpf('0.0741'), 8)}")

print("\n== [D4] SS2 C5*-acceptance remark, other bands at m = 401 ==")
for (bi, c5, expect) in ((1, '0.2', 'PASS'), (2, '0.4', 'PASS'), (3, '0.4', 'PASS'),
                         (2, '0.8', '?'), (3, '0.8', '?')):
    t = row(BANDS[bi], 401, C5o=c5)[0]
    print(f"  {BANDS[bi][0]}, C5*={c5}: row = {mp.nstr(t, 6)} {'PASS' if t <= 1 else 'FAIL'}"
          f"  (remark claims {expect})")

print("\n== [D5] independent harness parse (split-based) ==")
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
files = [os.path.join(base, 'wave2_repairs', 'results_m540.txt'),
         os.path.join(base, 'harness_m560', 'results_m560.txt')]
cov = {}; per = {}; nonpass = []
for fn in files:
    rows = {}
    for line in open(fn):
        parts = line.split()
        if len(parts) == 8 and parts[0].isdigit() and parts[-1] in ('PASS', 'FAIL'):
            mval = int(parts[0]); rows[mval] = parts[-1]
            if parts[-1] != 'PASS': nonpass.append((os.path.basename(fn), mval))
    per[os.path.basename(fn)] = rows
    for k, v in rows.items(): cov.setdefault(k, v)
f1, f2 = (per[os.path.basename(f)] for f in files)
print(f"  results_m540: {len(f1)} data rows, m in [{min(f1)}, {max(f1)}]")
print(f"  results_m560: {len(f2)} data rows, m in [{min(f2)}, {max(f2)}]")
print(f"  overlap keys: {sorted(set(f1) & set(f2))};  non-PASS rows: {nonpass if nonpass else 0}")
print(f"  union rows: {len(cov)};  gaps in [4, 560]: {[m for m in range(4, 561) if m not in cov] or 'NONE'};"
      f"  gaps in [401, 560]: {[m for m in range(401, 561) if m not in cov] or 'NONE'}")
for target in (461, 462, 463):
    src = 'm540' if target in f1 else 'm560'
    for fn in files:
        for line in open(fn):
            parts = line.split()
            if len(parts) == 8 and parts[0].isdigit() and int(parts[0]) == target:
                print(f"  row m={target} ({src}): {line.rstrip()}")
                break
        else:
            continue
        break
for line in open(files[1]):
    if line.startswith('# OVERALL'):
        print(f"  OVERALL: {line.rstrip()}")
