#!/usr/bin/env python3
# ref_rp_b_gridgaps.py -- wave-5 numerics referee on wave4_sl4p_repaired:
# OFF-GRID probes on Fact R.G's range m in [463, 699] (the repair's script
# [B] used a fixed 106-point w-set; this script probes the GAPS of that set
# and random off-grid points; a single row > 1 refutes Fact R.G's claim).
#
# [B1] gap probes: for EVERY integer m in [463, 699], w = 4 + {3e-10, 3e-9,
#      3e-8, 3e-7, 3e-6, 3e-5, 5e-5, 3e-4, 5e-4, 7e-4, 3e-3, 7e-3} (all 12
#      strictly between the repair's probe points near the edge): expect 0
#      FAILs; track overall max (expect at m = 463 edge).
# [B2] 500 seeded random (m, w), m uniform in [463, 699], w = 4 + 10^u with
#      u uniform in [-9, 0] (log-scaled toward the binding open edge).
# [B3] dense edge scan at the thin point m = 463: w = 4 + k*2e-6,
#      k = 1..250 (covers (4, 4.0005]): 0 FAILs, monotone nonincreasing.
# [B4] SL4'-X flag (X_w6 monotone-in-tau) at every evaluation above.
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'wave5_sl4prepair'))
import mpmath as mp
from sl4pr_common import BANDS, row
mp.mp.dps = 40
W1 = BANDS[0]
monobad = 0

def rv(m, w):
    global monobad
    t, _, mono = row(W1, m, wX=mp.mpf(w))
    if not mono: monobad += 1
    return t

print("== [B1] gap probes, every integer m in [463, 699] x 12 off-grid w ==")
gaps = ['3e-10', '3e-9', '3e-8', '3e-7', '3e-6', '3e-5', '5e-5', '3e-4',
        '5e-4', '7e-4', '3e-3', '7e-3']
fails = 0; total = 0; worst = mp.mpf('-1'); warg = None
for m in range(463, 700):
    for e in gaps:
        t = rv(m, mp.mpf('4') + mp.mpf(e)); total += 1
        if t > 1: fails += 1
        if t > worst: worst = t; warg = (m, '4+' + e)
print(f"  probes: {total};  FAILs: {fails}")
print(f"  max over gap probes = {mp.nstr(worst, 6)} at (m, w) = {warg}")

print("\n== [B2] 500 seeded random off-grid (m, w) on [463, 699] x (4, 5] ==")
rng = random.Random(79)
fails2 = 0; worst2 = mp.mpf('-1'); warg2 = None
for _ in range(500):
    m = rng.randint(463, 699)
    u = -9 + 9 * rng.random()
    w = mp.mpf(4) + mp.power(10, mp.mpf(u))
    if w > 5: w = mp.mpf(5)
    t = rv(m, w)
    if t > 1: fails2 += 1
    if t > worst2: worst2 = t; warg2 = (m, mp.nstr(w, 10))
print(f"  FAILs: {fails2};  max = {mp.nstr(worst2, 6)} at (m, w) = {warg2}")

print("\n== [B3] dense edge scan m = 463, w = 4 + k*2e-6, k = 1..250 ==")
prevv = None; noninc = True; fails3 = 0; first = last = None
for k in range(1, 251):
    t = rv(463, mp.mpf('4') + k * mp.mpf('2e-6'))
    if k == 1: first = t
    last = t
    if t > 1: fails3 += 1
    if prevv is not None and t > prevv + mp.mpf('1e-25'): noninc = False
    prevv = t
print(f"  FAILs: {fails3};  row(4+2e-6) = {mp.nstr(first, 8)} -> row(4.0005) = {mp.nstr(last, 8)}")
print(f"  nonincreasing in w across the dense scan: {noninc}"
      f"  (edge is the max -- consistent with Fact R.G's worst point (463, 4+))")

print(f"\n== [B4] SL4'-X monotone-in-tau flag violations over ALL {total + 500 + 250} "
      f"evaluations above: {monobad} ==")
