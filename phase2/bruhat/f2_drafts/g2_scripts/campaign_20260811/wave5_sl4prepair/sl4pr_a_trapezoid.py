#!/usr/bin/env python3
# sl4pr_a_trapezoid.py -- wave-5 SL4' repair, script [A]: the corrected W1
# trapezoid (referee findings F1 + F2 of referee_numerics_wave4_sl4p.md).
#
# [A1] w_dagger(m) at the ledger's gamma*(W1) = 0.42 (route (a)) for EVERY
#      integer m in [401, 462], scan step 0.001 from w = 4.000; nonincreasing
#      check; w_dagger(462) refined to step 1e-5.
# [A2] the w -> 4+ closure edge: row(m, w) at w = 4.0 (continuity limit),
#      4 + 1e-7, 4 + 1e-9 for m = 455..475 -> first full-closure m.
# [A3] route (b) numbers for the record: w_dagger(401; gamma* = 0.25) and the
#      first full-closure m under gamma* = 0.25 (referee E2/E3 cross-check).
# [A4] mootness arithmetic: trapezoid max-m vs harness coverage M_H = 560.
import mpmath as mp
from sl4pr_common import BANDS, row
mp.mp.dps = 40
W1 = BANDS[0]

def wdag(m, go=None, step=mp.mpf('0.001'), wmax=mp.mpf('4.6')):
    """least w on the step-grid with W1 row PASS (<= 1); None if none <= wmax."""
    w = mp.mpf(4)
    while w <= wmax:
        if row(W1, m, wX=(w if w > 4 else mp.mpf('4.000000001')), go=go)[0] <= 1:
            return w
        w += step
    return None

print("== [A1] w_dagger(m), gamma*(W1) = 0.42 (table value; route (a)), step 0.001, m = 401..462 ==")
prev = None; noninc = True; table = {}
for m in range(401, 463):
    wd = wdag(m)
    table[m] = wd
    if prev is not None and wd > prev: noninc = False
    prev = wd
    if m in (401, 402, 405, 410, 420, 430, 440, 450, 455, 460, 461, 462):
        print(f"  m={m}: w_dagger = {mp.nstr(wd, 6)}   (row at w_dagger = {mp.nstr(row(W1, m, wX=wd)[0], 6)})")
print(f"  w_dagger nonincreasing over the FULL integer grid m = 401..462: {noninc}")
print(f"  w_dagger(401) = {mp.nstr(table[401], 6)}  [referee B2: 4.095; draft's 4.10 was the 0.01-grid value, safe direction]")

# refine w_dagger(462) to 1e-5
w = mp.mpf('4.0')
while row(W1, 462, wX=w+mp.mpf('0.00001'))[0] > 1:
    w += mp.mpf('0.00001')
print(f"  w_dagger(462) refined (step 1e-5) = {mp.nstr(w+mp.mpf('0.00001'), 7)}  [referee B2b: 4.00021]")

print("\n== [A2] w -> 4+ closure edge: first m with W1 PASS at the open edge ==")
first = {}
for tag, weps in (('4.0 (limit)', mp.mpf('4') + mp.mpf('1e-30')),
                  ('4+1e-9', mp.mpf('4') + mp.mpf('1e-9')),
                  ('4+1e-7', mp.mpf('4') + mp.mpf('1e-7'))):
    fm = None; vals = {}
    for m in range(455, 476):
        t = row(W1, m, wX=weps)[0]
        vals[m] = t
        if t <= 1 and fm is None: fm = m
    first[tag] = fm
    line = "  ".join(f"{m}:{mp.nstr(vals[m],6)}{'P' if vals[m]<=1 else 'F'}" for m in (461, 462, 463, 464))
    print(f"  w = {tag}: first PASS m = {fm}   [{line}]")
print(f"  => corrected trapezoid m-range at gamma* = 0.42:  [401, {first['4+1e-9']-1}]"
      f"   (F2 repair: 461 -> 462; referee B2c confirmed)")

print("\n== [A3] route (b) record: the trapezoid under the ORIGINAL stated gamma*(W1) = 0.25 ==")
wd25 = wdag(401, go='0.25', step=mp.mpf('0.005'))
print(f"  w_dagger(401; gamma* = 0.25), step 0.005 = {mp.nstr(wd25, 6)}   [referee E2: 4.135]")
fm25 = None
for m in range(455, 500):
    if row(W1, m, wX=mp.mpf('4')+mp.mpf('1e-9'), go='0.25')[0] <= 1:
        fm25 = m; break
print(f"  first full-closure m at w -> 4+ under gamma* = 0.25: {fm25}"
      f"  -> route-(b) trapezoid m-range [401, {fm25-1}]   [referee E3: 470]")

print("\n== [A4] mootness arithmetic (both routes) vs harness coverage ==")
MH = 560
for tag, mmax in (("route (a): gamma*(W1)=0.42", first['4+1e-9']-1),
                  (f"route (b): gamma*(W1)=0.25", fm25-1)):
    print(f"  {tag}: trapezoid m-range [401, {mmax}];  max m = {mmax} <= M_H = {MH}: {mmax <= MH}"
          f";  first sliver-free m = {mmax+1} <= 561: {mmax+1 <= 561}")
print("  => under EITHER route the corrected trapezoid lies entirely inside the")
print("     harness-verified range [401, 560]; at the shifted CL threshold m >= 561")
print("     the W1 sliver exception is EMPTY (see scripts [B] and [C] for the")
print("     m >= 463 / m >= 700 W1 closure that makes the m >= 561 statement total).")
