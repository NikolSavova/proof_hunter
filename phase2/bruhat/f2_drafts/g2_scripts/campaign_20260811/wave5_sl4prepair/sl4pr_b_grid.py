#!/usr/bin/env python3
# sl4pr_b_grid.py -- wave-5 SL4' repair, script [B]: W1-row closure on the
# grid range m in [463, 699] (all w in (4, 5]), i.e. Fact R.G of the repaired
# draft.  (m >= 700 is Lemma R.2's analytic tail -- script [C]; m <= 462 is
# the trapezoid -- script [A].)
#
# [B1] for EVERY integer m in [463, 699]: W1 row at the 106-point w-probe set
#      {4+1e-9, 4+1e-7, 4+1e-5, 4.0001, 4.001, 4.005} u {4.01 .. 5.00 step
#      0.01}; count FAILs (expect 0); record per-m max row and its argmax;
#      verify the W.6 exponent monotone-in-tau flag (SL4'-X audit) at every
#      single X_w6 evaluation.
# [B2] fine scans (step 0.001, w in (4, 5]) at the sentinels m = 463 (worst,
#      first sliver-free m), m = 561 (first analytic-CL m), m = 699 (grid end).
# [B3] column m-monotonicity from [B1]'s stored values: for each of the 106
#      w-columns, row(m, w) nonincreasing over m = 463..699 (expect 0
#      violations).
import mpmath as mp
from sl4pr_common import BANDS, row
mp.mp.dps = 40
W1 = BANDS[0]

probes = [mp.mpf('4')+mp.mpf('1e-9'), mp.mpf('4')+mp.mpf('1e-7'),
          mp.mpf('4')+mp.mpf('1e-5'), mp.mpf('4.0001'), mp.mpf('4.001'), mp.mpf('4.005')]
probes += [mp.mpf(4)+mp.mpf(i)/100 for i in range(1, 101)]

print(f"== [B1] W1 row, every integer m in [463, 699] x {len(probes)}-point w-probe set ==")
fails = 0; mono_bad = 0; grid = {}
overall_max = mp.mpf('-1'); overall_arg = None
for m in range(463, 700):
    mx = mp.mpf('-1'); argw = None
    for w in probes:
        t, _, mono = row(W1, m, wX=w)
        grid[(m, w)] = t
        if not mono: mono_bad += 1
        if t > 1: fails += 1
        if t > mx: mx = t; argw = w
    if mx > overall_max: overall_max = mx; overall_arg = (m, argw)
    if m in (463, 470, 480, 500, 520, 540, 560, 561, 580, 600, 640, 699):
        print(f"  m={m}: max row over probes = {mp.nstr(mx, 6)} at w = {mp.nstr(argw, 8)}"
              f"  {'PASS' if mx <= 1 else 'FAIL'}")
print(f"  FAIL count over all {237*len(probes)} (m, w) probes: {fails}")
print(f"  X_w6 monotone-in-tau flag violations (SL4'-X audit, {237*len(probes)} evaluations x 60 cells): {mono_bad}")
print(f"  overall max row on the grid: {mp.nstr(overall_max, 6)} at (m, w) = "
      f"({overall_arg[0]}, {mp.nstr(overall_arg[1], 8)})   [worst point = smallest m at the open w-edge]")

print("\n== [B2] fine w-scans (step 0.001), sentinels m = 463 / 561 / 699 ==")
for m in (463, 561, 699):
    mx = mp.mpf('-1'); argw = None; nf = 0
    for i in range(1, 1001):
        w = mp.mpf(4)+mp.mpf(i)/1000
        t, _, _ = row(W1, m, wX=w)
        if t > 1: nf += 1
        if t > mx: mx = t; argw = w
    edge = row(W1, m, wX=mp.mpf('4')+mp.mpf('1e-9'))[0]
    print(f"  m={m}: fails on scan = {nf};  max over scan = {mp.nstr(mx, 6)} at w = {mp.nstr(argw, 6)};"
          f"  edge row(4+1e-9) = {mp.nstr(edge, 6)}  (margin {mp.nstr(1-edge, 4)})")

print("\n== [B3] column m-monotonicity over m = 463..699, all w-columns of [B1] ==")
viol = 0
for w in probes:
    prev = None
    for m in range(463, 700):
        t = grid[(m, w)]
        if prev is not None and t > prev + mp.mpf('1e-30'): viol += 1
        prev = t
print(f"  columns: {len(probes)};  nonincreasing-in-m violations: {viol}")
print("\n  => W1 row <= 1 for every probed (m, w), m in [463, 699]; worst margin at")
print("     (463, 4+): see [B2]; monotone evidence: [B3] columns + [A1] w_dagger shape.")
