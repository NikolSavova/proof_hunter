#!/usr/bin/env python3
# ref_rp_a_offgrid_trap.py -- wave-5 numerics referee on wave4_sl4p_repaired:
# OFF-GRID adversarial probes on the previously-broken W1 trapezoid region
# (referee findings F1/F2 of referee_numerics_wave4_sl4p.md; repaired draft
# SS5.1).  Machinery: imports the repair's sl4pr_common (itself diffed against
# the prover's sl4p_nc1_ledger.py lines 12-103 and referee-rebuilt to < 5e-5
# in the wave-4 pass).
#
# [A1] TRUE crossing wc(m) by bisection (tol 1e-8) for EVERY m in [401, 462];
#      checks: wc(m) <= w_dagger_grid(m) (grid value is safe-direction),
#      w_dagger_grid(m) - wc(m) < 0.001 (grid step), wc nonincreasing,
#      row FAILs at wc - 1e-6 and PASSes at wc + 1e-6 (crossing genuine).
# [A2] ONE-CROSSING attack, off-grid: for every m in [401, 462], probe the
#      row at 40 seeded pseudo-random w in (wc(m), 5] plus the adversarial
#      offsets wc + {1e-6, 3.7e-4, 6.3e-4, 1.7e-3, 0.0505}: EVERY probe must
#      PASS (a single FAIL above wc refutes the theorem's exception clause).
# [A3] m = 462 micro-window: bisect the true crossing; verify it lies in
#      (4.0002, 4.00021] (draft: w_dagger(462) = 4.00021, PASS at the grid
#      value); row(462, 4.00019) must FAIL, row(462, 4.00021) must PASS.
# [A4] m = 463 edge ladder w = 4 + {1e-15 .. 1e-3}: all PASS (first
#      sliver-free m), values <= edge value 0.991128; and m = 461/462 at
#      w = 4 + 1e-15 must FAIL (F2's corrected off-by-one, sharpest probe).
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'wave5_sl4prepair'))
import mpmath as mp
from sl4pr_common import BANDS, row
mp.mp.dps = 40
W1 = BANDS[0]

def rv(m, w):
    return row(W1, m, wX=mp.mpf(w))[0]

print("== [A1] true crossing wc(m) by bisection, m = 401..462 ==")
wc = {}; wd_grid = {}
bad_bracket = 0
for m in range(401, 463):
    lo, hi = mp.mpf('4') + mp.mpf('1e-12'), mp.mpf('4.6')
    assert rv(m, lo) > 1 and rv(m, hi) <= 1
    for _ in range(46):                       # 0.6 * 2^-46 < 1e-13
        mid = (lo + hi) / 2
        if rv(m, mid) <= 1: hi = mid
        else: lo = mid
    wc[m] = hi
    # grid w_dagger exactly as repair script [A1] (step 0.001 from 4.000)
    w = mp.mpf(4)
    while True:
        if row(W1, m, wX=(w if w > 4 else mp.mpf('4.000000001')))[0] <= 1:
            wd_grid[m] = w; break
        w += mp.mpf('0.001')
    if not (rv(m, wc[m] - mp.mpf('1e-6')) > 1 and rv(m, wc[m] + mp.mpf('1e-6')) <= 1):
        bad_bracket += 1
prev = None; noninc = True; safe = True; step_ok = True
for m in range(401, 463):
    if prev is not None and wc[m] > prev + mp.mpf('1e-12'): noninc = False
    prev = wc[m]
    if wc[m] > wd_grid[m]: safe = False
    if wd_grid[m] - wc[m] >= mp.mpf('0.001'): step_ok = False
for m in (401, 430, 461, 462):
    print(f"  m={m}: wc = {mp.nstr(wc[m], 8)}   w_dagger_grid = {mp.nstr(wd_grid[m], 6)}"
          f"   (grid - true = {mp.nstr(wd_grid[m]-wc[m], 3)})")
print(f"  crossing genuine (FAIL at wc-1e-6, PASS at wc+1e-6) failures: {bad_bracket}")
print(f"  wc nonincreasing over m = 401..462: {noninc}")
print(f"  SAFE DIRECTION wc(m) <= w_dagger_grid(m) for ALL m: {safe};"
      f"  grid gap < 0.001 for ALL m: {step_ok}")

print("\n== [A2] one-crossing attack: off-grid probes ABOVE wc(m), m = 401..462 ==")
rng = random.Random(20260812)
fails = 0; total = 0; worst = mp.mpf('-1'); warg = None
offsets = [mp.mpf('1e-6'), mp.mpf('3.7e-4'), mp.mpf('6.3e-4'), mp.mpf('1.7e-3'), mp.mpf('0.0505')]
for m in range(401, 463):
    ws = [wc[m] + o for o in offsets]
    ws += [wc[m] + (mp.mpf(5) - wc[m]) * mp.mpf(rng.random()) for _ in range(40)]
    for w in ws:
        if w > 5: w = mp.mpf(5)
        t = rv(m, w); total += 1
        if t > 1: fails += 1
        if t > worst: worst = t; warg = (m, mp.nstr(w, 8))
print(f"  probes above the true crossing: {total};  FAILs (row > 1): {fails}")
print(f"  worst (largest) row above crossing = {mp.nstr(worst, 6)} at (m, w) = {warg}")

print("\n== [A3] m = 462 micro-window ==")
print(f"  true crossing wc(462) = {mp.nstr(wc[462], 9)}")
print(f"  in (4.0002, 4.00021]: {mp.mpf('4.0002') < wc[462] <= mp.mpf('4.00021')}")
for w in ('4.00019', '4.0002', '4.00021'):
    t = rv(462, w)
    print(f"  row(462, {w}) = {mp.nstr(t, 8)}  {'PASS' if t <= 1 else 'FAIL'}")

print("\n== [A4] edge ladders at m = 461/462/463 ==")
lad = ['1e-15', '1e-12', '1e-10', '1e-9', '1e-8', '1e-7', '1e-6', '1e-5', '1e-4', '1e-3']
for m in (461, 462, 463):
    vals = [rv(m, mp.mpf('4') + mp.mpf(e)) for e in lad]
    verd = ''.join('P' if v <= 1 else 'F' for v in vals)
    print(f"  m={m}: row(4+eps), eps=1e-15..1e-3: [{verd}]  row(4+1e-15) = {mp.nstr(vals[0], 6)}")
mono463 = all(vals[i+1] <= vals[i] + mp.mpf('1e-20') for i in range(len(vals)-1))
print(f"  m=463 ladder nonincreasing in w: {mono463}"
      f"  (max at the open edge; draft Fact R.G's edge claim)")
first = None
for m in range(455, 476):
    if rv(m, mp.mpf('4') + mp.mpf('1e-15')) <= 1: first = m; break
print(f"  first m with PASS at w = 4+1e-15: {first}   [draft/F2: 463]")
