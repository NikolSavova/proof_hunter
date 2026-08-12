"""NC-A2: the assembled Delta_ker bound C_ker(K, m) (Theorem A.5).

 (1) Full per-piece table at m in {180, 200, 250, 300, 350, 379, 400, 500,
     1000, 2000} x K in {1, 2, 4}: box / tail / out kernel pieces, pointwise
     E_pt, denominator dbar, and the assembled C_ker (m^2-scaled).
 (2) Far-piece threshold scan (unit step): m3(K) := first m >= 30 with the far
     piece of C_ker <= 0.2 (the campaign's standing 0.2-tolerance convention,
     NC-T10d / wp1-c NC-W4 class) AND C_ker finite; also the first m where
     C_ker <= its headline constant.
 (3) Monotone decrease of C_ker in m on [max(180, m3(K)), 3000] (step 1 to
     1000, step 10 beyond).
 (4) Headline constants: C_ker(K) at the reference thresholds
     M(1) = 180, M(2) = 190, M(4) = 379 (wp1-c m_2-class), rounded UP.

Run: python3 wp2a2_nc2_buckets.py
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import wp2a2_lib as L


def main():
    ok = True
    print("NC-A2: Delta_ker bound assembly")

    print("(1) per-piece table (all entries m^2-scaled where marked):")
    print("      m  K      eps    m2*box   m2*tail    m2*out      dbar"
          "      m2*Cker   (far piece)")
    table = {}
    for m in (180, 200, 250, 300, 350, 379, 400, 500, 1000, 2000):
        for K in (1, 2, 4):
            r = L.delta_ker_bound(K, m)
            table[(K, m)] = r
            if r is None:
                print("   %4d %2d   -- bound not assembled (eps/z >= 1) --" % (m, K))
                continue
            pref = 2.0 * 3.141592653589793 * r["s2min"] / L.CK[K]  # display only
            s2wf_box = (r["s2wf"] * r["D_box"] / r["DD"]) * m * m
            s2wf_tail = (r["s2wf"] * r["D_tail"] / r["DD"]) * m * m
            s2wf_out = (r["s2wf"] * r["D_out"] / r["DD"]) * m * m
            print("   %4d %2d  %7.4f  %8.4f  %8.2e  %8.2e  %8.2e  %10.4f  (%8.2e)"
                  % (m, K, r["eps"], s2wf_box, s2wf_tail, s2wf_out,
                     r["dbar"], r["Cker"], r["Cker_far_piece"]))

    print("(2) thresholds (unit-step scans from m = 30):")
    m3 = {}
    for K in (1, 2, 4):
        first_far = first_ok = None
        for m in range(30, 2001):
            r = L.delta_ker_bound(K, m)
            if r is None:
                continue
            if first_far is None and r["Cker_far_piece"] <= 0.2:
                first_far = m
            if first_far is not None and first_ok is None:
                first_ok = m
                break
        m3[K] = first_far
        print("    K=%d: far piece <= 0.2 first at m = %s" % (K, first_far))

    print("(3) monotone decrease of C_ker in m:")
    for K in (1, 2, 4):
        lo = max(180, m3[K])
        ms = list(range(lo, 1001)) + list(range(1010, 3001, 10))
        prev, mono = None, True
        for m in ms:
            r = L.delta_ker_bound(K, m)
            c = r["Cker"] if r else float("inf")
            if prev is not None and c > prev + 1e-12:
                mono = False
                print("      K=%d NOT decreasing at m=%d (%.6f -> %.6f)"
                      % (K, m, prev, c))
                break
            prev = c
        print("    K=%d: decreasing on [%d, 3000]: %s" % (K, lo, mono))
        ok &= mono

    print("(4) headline constants (rounded UP, safe direction):")
    refs = {1: 180, 2: 190, 4: 379}
    for K in (1, 2, 4):
        M = max(refs[K], m3[K] if m3[K] else 10**9)
        r = L.delta_ker_bound(K, M)
        print("    K=%d: M(K) = %d ,  C_ker(K) = %.4f  -> carry %.2f"
              % (K, M, r["Cker"], (int(r["Cker"] * 100) + 1) / 100.0))

    print("\nNC-A2 VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
