"""NC-W4: assembly of the explicit C_R(K) table (K = 1, 2, 4) and truth comparison.

 (1) PW_grid(K): independent re-run of the pointwise bucket grid certificate
     max_{m in [30,2000], 0 < w <= K} |N(0)_resid / P(0)^2 * m^2|
     (same grid as g2_item4_bucket_notes / t2i4_nc1_model.py; must reproduce
     ~1.55 / 4.09 / 4.91).
 (2) PW_closed(K, m): closed-form bound from the NC-W1 monomial table with the
     NC-W2 boxes: sum |coeff| amax^ea bmax^eb dmax^ed gmax^eg * m^2 / P0min^2,
     evaluated at m in {180, 500, 2000, 10000} (valid for ALL m >= 180 by
     monotone decrease, checked).
 (3) c_w(K): the proved w^2-envelope coefficient at m >= 180 (audit of T.9's
     claim c_w = 1/2), assembled from
       B-part:  |B_lam/B_m - 1|, via kappa_4-ratio bounds x (lambda/s2)^2 bounds,
                taking the min of the recentred route (q_r w^2) and the direct
                route (T.9''a |kappa_4| <= (S_4+m)/120) on each side;
       bare-alpha^2 part: 36 a(w)^2 / (P0^2 B_m)  with |a(w)| <= w * a_unit.
 (4) Lin(K, m) = m^2 * (9/8) e^{1.5/s2min} / s2min  (linearization
     s2(r-1) vs s2 log r; conditional on |s2 log r - 1| <= 1/2).
 (5) Assembled C_R^{PT}(K) = PW + Taylor + Lin at threshold m >= 180, in a
     grid-certified flavor and an all-m closed-form flavor. Kernel-transfer +
     denominator bucket: PENDING (wp2-a); its TRUTH is measured in (6).
 (6) Exact-harness truth, m in {30, 60, 100, 140}: with lam(k) solved from the
     closed-form mean (bisection),
       needed0(K, m)    := max_{|w|<=K} |s2 (r(k)-1) - (1 - B_m)| m^2
       needed_env(K, m) := max_{|w|<=K} (|s2 (r(k)-1) - (1-B_m)| - B_m c_w(K) w^2)_+ m^2
       ker_truth(K, m)  := max_{|w|<=K} |s2 (log(1+u) - log(1+v))| m^2,
     u := r(k)-1 (exact rows), v := e^{1/s2} P(0)^2/(P(-h)P(h)) - 1 (model).
     Slack report vs NC-T8's measured "needed C_R <= 0.35".

Run: python3 wp2b_nc4_assembly.py
"""
import math
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wp2b_lib as lib
from wp2b_nc3_taylor import CK, boxes, taylor_bucket
from wp2b_n0_resid_table import RESID


def P0_min(K, m):
    a, b, d, g, h, s2min = boxes(K, m)
    return 1 - (3 * b + 15 * (g + a * a / 2) + 105 * (b * b / 2 + a * d) + 3 * a * h + 15 * d * h + 105 * a * b * h)


def pw_closed(K, m):
    a, b, d, g, h, s2min = boxes(K, m)
    tot = 0.0
    for (ea, eb, ed, eg), co in RESID:
        tot += abs(Fraction(co)) * a**ea * b**eb * d**ed * g**eg
    return float(tot) * m * m / P0_min(K, m) ** 2


def c_w(K, m):
    """(c_w, parts) proved envelope coefficient at this (K, m)."""
    S4 = float(lib.S(4, m))
    dir_ratio = (S4 + m) / (S4 - m)
    lamv = float(lib.lam_var(m))
    Bm = (S4 - m) / 240.0 / lamv**2
    a_unit = (1.0 / m) * (S4 + m) / 120 / (6 * (CK[K] * lamv) ** 1.5)  # |a| <= w*a_unit
    bare = 36 * a_unit**2 / (Bm * P0_min(K, m) ** 2)
    worstB = 0.0
    for wi in range(1, 401):
        w = K * wi / 400
        de = min(0.0330 * w * w, 0.40)
        devB = de * (2 - de) / (1 - de) ** 2
        q = ((600 / 2200) if w <= math.pi else (600 / 1500)) * w * w
        upper = min(q * (1 + devB) + devB + (dir_ratio - 1),
                    dir_ratio * (1 + devB) - 1)
        # lower: 1 - ratio*R with |ratio-1| <= q, R in [1, 1+devB];
        # worst ratio = 1-q: if q <= 1 the min over R is at R=1 (value q);
        # if q > 1, ratio may be negative and the max is at R = 1+devB.
        lower_q = q if q <= 1 else 1 + (q - 1) * (1 + devB)
        lower = min(lower_q, 1 + dir_ratio * (1 + devB))
        worstB = max(worstB, max(upper, lower) / (w * w))
    return worstB + bare, (worstB, bare)


def lin_bucket(K, m):
    s2min = CK[K] * float(lib.lam_var(m))
    return m * m * 1.125 * math.exp(1.5 / s2min) / s2min


def solve_lam(m, k, lam_hint):
    lo, hi = max(0.0, lam_hint - 0.02), lam_hint + 0.1
    while lib.cumulants(m, hi)[0] > k:
        hi += 0.1
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if lib.cumulants(m, mid)[0] > k:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    ok = True

    print("(1) PW_grid re-run (independent implementation):")
    pw_grid = {}
    for K in (1, 2, 4):
        worst, at = 0.0, None
        for m in (30, 50, 80, 120, 200, 350, 600, 1000, 2000):
            for wi in range(1, 21):
                w = K * wi / 20
                a, b, d, g, s2 = lib.scaled_coeffs(m, w / m)
                r, P0 = lib.N0_resid_and_P0(a, b, d, g)
                val = abs(r / P0**2 * m * m)
                if val > worst:
                    worst, at = val, (m, round(w, 2))
        pw_grid[K] = worst
        print(f"    K={K}: max |N0_resid/P0^2 m^2| = {worst:.4f} at (m,w)={at}")
    ref = {1: 1.5491, 2: 4.0889, 4: 4.9126}
    rep = all(abs(pw_grid[K] - ref[K]) < 0.02 for K in ref)
    print(f"    reproduces item-4 notes (1.5491/4.0889/4.9126 within 0.02): {rep}")
    ok &= rep

    print("(2) PW_closed(K, m) [all m >= row-m, closed-form boxes]:")
    print(f"    {'m':>6s} {'K=1':>10s} {'K=2':>10s} {'K=4':>10s}")
    for m in (180, 500, 2000, 10000):
        print(f"    {m:6d} " + " ".join(f"{pw_closed(K, m):10.3f}" for K in (1, 2, 4)))
    dec = all(pw_closed(K, m) >= pw_closed(K, m + 60) - 1e-12
              for K in (1, 2, 4) for m in range(180, 2000, 60))
    print(f"    decreasing in m (180..2000 step 60): {dec}")
    ok &= dec

    print("(3) proved w^2-envelope coefficient c_w(K), max over m in "
          "{180, 500, 2000, 10000} (T.9 claims c_w = 1/2):")
    cw = {}
    for K in (1, 2, 4):
        best = None
        for mm in (180, 500, 2000, 10000):
            val, parts = c_w(K, mm)
            if best is None or val > best[0]:
                best = (val, parts, mm)
        cw[K] = best[0]
        print(f"    K={K}: c_w = {cw[K]:.4f}   (B-part {best[1][0]:.4f} + "
              f"bare-alpha^2 {best[1][1]:.4f}, worst m = {best[2]})"
              f"   -> c_w <= 1/2: {cw[K] <= 0.5}")

    print("(4) linearization bucket Lin(K, 180):",
          " ".join(f"K={K}: {lin_bucket(K, 180):.4f}" for K in (1, 2, 4)))

    print("(5) ASSEMBLED C_R^{PT}(K) at m >= 180  [pointwise + Taylor + Lin; "
          "kernel bucket PENDING wp2-a]:")
    print(f"    {'K':>2s} {'PW_grid':>9s} {'PW_closed':>10s} {'Taylor':>9s} {'Lin':>7s}"
          f" {'C_R^PT grid':>12s} {'C_R^PT closed':>14s}")
    for K in (1, 2, 4):
        T = taylor_bucket(K, 180)["bucket"]
        L = lin_bucket(K, 180)
        Cg = pw_grid[K] + T + L
        Cc = pw_closed(K, 180) + T + L
        print(f"    {K:2d} {pw_grid[K]:9.4f} {pw_closed(K, 180):10.3f} {T:9.5f} {L:7.4f}"
              f" {Cg:12.4f} {Cc:14.3f}")

    print("(6) exact-harness truth (m in {30, 60, 100, 140}):")
    print(f"    {'m':>4s} {'K':>2s} {'needed0':>9s} {'needed_env':>10s} {'ker_truth':>10s}"
          f"  {'(max over k with |w|<=K)':>24s}")
    for m in (30, 60, 100, 140):
        rows = lib.mahonian(m)
        N = m * (m - 1) // 2
        lamv = float(lib.lam_var(m))
        S4 = float(lib.S(4, m))
        Bm = (S4 - m) / 240.0 / lamv**2
        data = []
        lam_hint = 0.0
        for k in range(N // 2, 0, -1):
            lam = solve_lam(m, k, lam_hint)
            lam_hint = lam
            w = lam * m
            if w > 4.05:
                break
            a, b, d, g, s2 = lib.scaled_coeffs(m, lam)
            u = rows[k] * rows[k] / (rows[k - 1] * rows[k + 1]) - 1.0
            h = 1 / math.sqrt(s2)
            F0 = (math.exp(1 / s2) * lib.P_eval(a, b, d, g, 0.0) ** 2
                  / (lib.P_eval(a, b, d, g, h) * lib.P_eval(a, b, d, g, -h)))
            v = F0 - 1.0
            data.append((w, s2 * u, s2 * (math.log1p(u) - math.log1p(v))))
        for K in (1, 2, 4):
            sel = [(w, su, dk) for (w, su, dk) in data if w <= K]
            n0 = max(abs(su - (1 - Bm)) for w, su, dk in sel) * m * m
            ne = max(max(0.0, abs(su - (1 - Bm)) - Bm * cw[K] * w * w)
                     for w, su, dk in sel) * m * m
            kt = max(abs(dk) for w, su, dk in sel) * m * m
            print(f"    {m:4d} {K:2d} {n0:9.3f} {ne:10.3f} {kt:10.3f}")

    print("\nNC-W4 VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
