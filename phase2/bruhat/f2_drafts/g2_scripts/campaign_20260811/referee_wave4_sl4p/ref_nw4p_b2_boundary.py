#!/usr/bin/env python3
# ref_nw4p_b2_boundary.py -- pin the m = 462 off-by-one found by ref_nw4p_b [B3]:
# row(462, w -> 4+) FAILS, so the residual trapezoid extends to m = 462 (not 461).
# [B2a] row(m, w = 4.0 exact) for m = 459..470  (continuity limit of w -> 4+);
# [B2b] fine threshold at m = 462: least w with PASS, step 1e-5;
# [B2c] first m with row(m, 4.0) <= 1  (true full-band closure point).
import mpmath as mp
mp.mp.dps = 40
exec(open('/Users/sihaohuang/Desktop/Coding/proof_hunter/phase2/bruhat/f2_drafts/'
          'g2_scripts/campaign_20260811/referee_wave4_sl4p/ref_nw4p_b_sliver.py')
     .read().split("print(\"== [B1]")[0])   # reuse row()/BANDS defs verbatim, no prints

print("== [B2a] row(m, w = 4.0 exact) = lim_{w->4+} row(m, w), m = 459..470 ==")
for m in range(459, 471):
    v = row(BANDS[0], m, wX=mp.mpf('4.0'))
    print(f"  m={m}: row(w->4+) = {float(v):.6f}  {'PASS' if v <= 1 else 'FAIL'}")

print("\n== [B2b] m = 462 threshold: least w with PASS (step 1e-5) ==")
lo = None
for i in range(0, 101):
    w = mp.mpf(4)+i*mp.mpf('1e-5')
    if row(BANDS[0], 462, wX=w) <= 1: lo = w; break
print(f"  w_dagger(462) = {float(lo) if lo is not None else '> 4.001'}")

print("\n== [B2c] first m with full closure at w -> 4+ ==")
first = None
for m in range(459, 476):
    if row(BANDS[0], m, wX=mp.mpf('4.0')) <= 1:
        first = m; break
print(f"  first m with row(m, 4.0) <= 1: {first}"
      f"  -> corrected trapezoid: m in [401, {first-1}] (draft SS5/SS8 say [401, 461])")
