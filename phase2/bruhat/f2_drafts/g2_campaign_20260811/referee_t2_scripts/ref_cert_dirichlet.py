"""Referee re-implementation (numerics referee, T2 draft, 2026-08-11).

Upgrades the two grid-only Dirichlet-kernel certificates of g2_draft_t2 to
proof-grade via an analytic reduction, then re-confirms the draft's grid minima
at 10x density.

Certificates under audit (draft SS3, grid-certified only, "Sturm-able on demand"):
  (T.7b-cert)  1 - |F_j(t)|^2 >= 1/80   for all j >= 2, jt >= 0.45, |t| <= pi
  (T.7c-cert)  1 - |F_j(t)|^2 >= 0.35   for all j >= 2, jt >= 2.8,  |t| <= pi
where F_j(t) = sin(jt/2)/(j sin(t/2)) (uniform-on-{0..j-1} cf modulus).

ANALYTIC REDUCTION (this script verifies every ingredient numerically at high
precision; each ingredient is also provable by hand):

 (A) Envelope: on 0 < t <= pi, sin(t/2) >= t/pi, so |F_j(t)| <= pi/(jt) and
     1 - F_j^2 >= 1 - pi^2/(jt)^2.  Hence:
       jt >= 3.5  =>  1 - F_j^2 >= 1 - pi^2/12.25 = 0.19435... >= 1/80   [T.7b]
       jt >= 3.9  =>  1 - F_j^2 >= 1 - pi^2/15.21 = 0.35108... >= 0.35   [T.7c]

 (B) j-monotonicity at fixed c := jt: |F_j(c/j)| = sin(c/2) / (j sin(c/(2j))),
     and j |-> j sin(c/(2j)) is INCREASING in j (derivative in the continuous
     variable x: sin(u) - u cos(u) with u = c/(2x) in (0, pi), and
     d/du[sin u - u cos u] = u sin u > 0 with value 0 at u = 0).  So for fixed
     c, 1 - F_j^2 is minimized over j >= 2 at j = 2, where
     1 - F_2(c/2)^2 = 1 - cos^2(c/4) = sin^2(c/4)  (valid: c/2 <= pi for c <= 2pi).

 (C) Endpoint values (sin^2 is increasing on the relevant ranges c/4 <= 0.975 < pi/2):
       c in [0.45, 3.5]: sin^2(c/4) >= sin^2(0.1125) = 0.0126028... >= 1/80   [T.7b]
       c in [2.8,  3.9]: sin^2(c/4) >= sin^2(0.7)    = 0.4150164... >= 0.35   [T.7c]

 (A)+(B)+(C) cover the full regions of both certificates.

stdlib + mpmath. Run: python3 ref_cert_dirichlet.py
"""
import math
import sys

import mpmath as mp

mp.mp.dps = 50


def Fj2(j, t):
    s = math.sin(t / 2)
    if s == 0:
        return 1.0
    return (math.sin(j * t / 2) / (j * s)) ** 2


def main():
    ok = True

    print("(C) endpoint values at 50 digits (mpmath):")
    v_b = mp.sin(mp.mpf("0.1125")) ** 2          # T.7b: c = 0.45, j = 2
    v_c = mp.sin(mp.mpf("0.7")) ** 2             # T.7c: c = 2.8,  j = 2
    print(f"  sin^2(0.1125) = {mp.nstr(v_b, 12)}  vs 1/80 = 0.0125 : "
          f"margin = {mp.nstr(v_b - mp.mpf(1)/80, 6)}")
    print(f"  sin^2(0.7)    = {mp.nstr(v_c, 12)}  vs 0.35        : "
          f"margin = {mp.nstr(v_c - mp.mpf('0.35'), 6)}")
    ok &= v_b > mp.mpf(1) / 80 and v_c > mp.mpf("0.35")

    print("(A) envelope thresholds at 50 digits:")
    e_b = 1 - mp.pi**2 / mp.mpf("3.5") ** 2
    e_c = 1 - mp.pi**2 / mp.mpf("3.9") ** 2
    print(f"  1 - pi^2/3.5^2 = {mp.nstr(e_b, 12)}  (>= 1/80: {e_b > mp.mpf(1)/80})")
    print(f"  1 - pi^2/3.9^2 = {mp.nstr(e_c, 12)}  (>= 0.35: {e_c > mp.mpf('0.35')})")
    ok &= e_b > mp.mpf(1) / 80 and e_c > mp.mpf("0.35")
    # the envelope's own ingredient sin(t/2) >= t/pi on (0, pi]: concavity of sin
    # on [0, pi/2]; numeric confirmation on a grid:
    worst = min(math.sin(t / 2) - t / math.pi
                for t in (math.pi * i / 20000 for i in range(1, 20001)))
    print(f"  min[ sin(t/2) - t/pi ] on (0, pi] grid = {worst:.3e}  (>= 0)")
    ok &= worst >= -1e-15

    print("(B) monotonicity kernel sin(u) - u cos(u) > 0 on (0, pi):")
    wm = min(math.sin(u) - u * math.cos(u)
             for u in (math.pi * i / 20000 for i in range(1, 20000)))
    print(f"  min on grid = {wm:.3e}  (> 0; analytic: derivative u sin u > 0)")
    ok &= wm > 0

    print("(B) reduction sanity: 1-F_j(c/j)^2 >= 1-F_2(c/2)^2 on the danger zones:")
    bad = 0
    for zone_lo, zone_hi in ((0.45, 3.5), (2.8, 3.9)):
        for ci in range(401):
            c = zone_lo + (zone_hi - zone_lo) * ci / 400
            base = 1 - Fj2(2, c / 2)
            for j in (3, 4, 5, 8, 16, 64, 512, 4096):
                if 1 - Fj2(j, c / j) < base - 1e-12:
                    bad += 1
    print(f"  violations: {bad} (expect 0)")
    ok &= bad == 0

    print("10x-density direct rescans of the draft's grids (belt and braces):")
    mn_b = 10.0
    arg_b = None
    for j in list(range(2, 513)) + [1000, 5000]:
        t0 = 0.45 / j
        t_hi = min(math.pi, 3.5 / j)  # envelope covers jt >= 3.5 analytically
        for i in range(40000):
            t = t0 + (t_hi - t0) * i / 39999
            v = 1 - Fj2(j, t)
            if v < mn_b:
                mn_b, arg_b = v, (j, t)
    print(f"  T.7b danger zone min = {mn_b:.6f} at j={arg_b[0]}, t={arg_b[1]:.4f}"
          f"  (draft: 0.012603 at j=2, t=0.225; >= 1/80: {mn_b >= 1/80})")
    ok &= mn_b >= 1 / 80

    mn_c = 10.0
    arg_c = None
    for j in list(range(2, 513)) + [1000, 5000]:
        t0 = 2.8 / j
        if t0 > math.pi:
            continue
        t_hi = min(math.pi, 3.9 / j)
        for i in range(40000):
            t = t0 + (t_hi - t0) * i / 39999
            v = 1 - Fj2(j, t)
            if v < mn_c:
                mn_c, arg_c = v, (j, t)
    print(f"  T.7c danger zone min = {mn_c:.6f} at j={arg_c[0]}, t={arg_c[1]:.4f}"
          f"  (draft: 0.4150 at j=2, t=1.4; >= 0.35: {mn_c >= 0.35})")
    ok &= mn_c >= 0.35

    print(f"REF-CERT VERDICT: {'PASS - both certificates hold, now with an '
          'analytic covering argument (no longer grid-only)' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
