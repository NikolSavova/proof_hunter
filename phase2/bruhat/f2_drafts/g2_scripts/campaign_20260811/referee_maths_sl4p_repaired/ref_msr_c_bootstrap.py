#!/usr/bin/env python3
# ref_msr_c_bootstrap.py -- maths referee, wave4_sl4p_repaired: the INFL/QUADF
# self-consistency bootstrap (Lemmas SL4'.6/.7, inherited unchanged).
#
# The lemmas price the ledger with INFL(Theta) = 1/(1 - Theta - d) and
# QUADF(Theta) = Theta + d (d = dHe + dq = 0.03853) evaluated AT the
# conclusion Theta = 20/m.  That is a fixed-point ansatz, not yet a proof.
# This script quantifies the missing closure: with G(x) := the ledger's bound
# on |s2(r-1)-1| when the true perturbation is x (entries re-inflated
# honestly), the monotone-iteration argument
#     Theta <= G(Theta),  G increasing,  G(x) < x on [20/m, x_seed]
# closes the bootstrap FROM ANY a-priori seed Theta <= x_seed.  We compute
# G(x) exactly for the two thinnest rows (W5 at m = 401; W1 at (463, 4+))
# and locate x_seed = sup{x : G(x) <= x}.  The residual obligation is the
# SEED LEMMA (a crude a-priori |s2(r-1)-1| <= x_seed), which no cited input
# currently supplies.
import mpmath as mp
mp.mp.dps = 40
d = mp.mpf('0.0350') + 1/(2*mp.mpf('141.7497'))   # dHe + dq, block [5] values
print(f"  d = dHe + dq = {mp.nstr(d, 6)}  (block [5]: 0.0885 - 20/401 = "
      f"{mp.nstr(mp.mpf('0.0884') - mp.mpf(20)/401, 4)}-class: consistent)")
# rows: (label, m, tot_ref at INFL=1.10/QUADF=0.09, main-part uninflated)
# tot = (1+q)*share; share = (main + I*restdec)/(20cA) + I*(inc)/20.
# We reconstruct the split from the archived parts (original block [1] and
# this wave's scripts): for the G(x) scaling only the INFL-scaled fraction
# matters; main/(20cA)(1+q) is x-free except the (1+q) factor.
ROWS = [
  # (name, m, tot_ref, main_contrib_ref)  main_contrib_ref = main/(20 cA)*(1.09)
  ('W5 (m=401, worst ledger row)', 401, mp.mpf('0.9891'),
   mp.mpf('3.801')/(20*mp.mpf('0.60'))*mp.mpf('1.09')),
  ('W1 (m=463, w->4+, thinnest assembly row)', 463, mp.mpf('0.991128'),
   (mp.mpf('0.4') + mp.mpf('0.3') + (mp.mpf(5)/463)**2/2)/(20*mp.mpf('0.28'))*mp.mpf('1.09')),
]
for name, m, tot, mainc in ROWS:
    B0 = mp.mpf(20)/m
    infc = tot - mainc          # the INFL-scaled part of tot at reference
    def G(x, infc=infc, mainc=mainc, B0=B0):
        I = 1/(1 - x - d)
        return B0*(mainc*(1 + x + d)/mp.mpf('1.09')
                   + infc*(I/mp.mpf('1.10'))*((1 + x + d)/mp.mpf('1.09')))
    print(f"\n  {name}: tot_ref = {mp.nstr(tot, 6)}, main-part = {mp.nstr(mainc, 4)}, "
          f"INFL-part = {mp.nstr(infc, 4)}, budget 20/m = {mp.nstr(B0, 4)}")
    print(f"    G(20/m) = {mp.nstr(G(B0), 6)} < 20/m = {mp.nstr(B0, 6)}: {G(B0) < B0}"
          f"   (strict contraction at the target)")
    for x in ('0.10', '0.25', '0.5', '0.7', '0.8', '0.85', '0.9'):
        xx = mp.mpf(x)
        print(f"    G({x}) = {mp.nstr(G(xx), 5)}  {'<' if G(xx) < xx else '>='} {x}")
    # sup{x: G(x) <= x} by bisection on [B0, 0.96-d)
    lo2, hi2 = B0, mp.mpf('0.96') - d
    for _ in range(80):
        mid = (lo2 + hi2)/2
        if G(mid) <= mid: lo2 = mid
        else: hi2 = mid
    print(f"    x_seed = sup{{x : G(x) <= x}} = {mp.nstr(lo2, 5)}  -> ANY a-priori bound"
          f" |s2(r-1)-1| <= {mp.nstr(lo2, 3)} closes the bootstrap by monotone iteration")
print("\n  NOTE: G is convex increasing on [0, 1-d) (it is a*(1+u) + b*(1+u)/(1-u),")
print("  u = x + d), so G < id on [20/m, x_seed] follows from the two endpoint")
print("  checks alone (chord argument); the iteration x_{n+1} = G(x_n) then")
print("  descends from the seed to a fixed point < 20/m.  The MISSING ingredient")
print("  is only the seed lemma; nothing in [A2]/[A3]/[C.1]/[W.6]/[SL3']/[SLV]")
print("  currently provides an unconditional crude bound on the deep-tilt band.")
