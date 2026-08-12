"""NC-A3: the refined (real-part-split) Delta_ker bound (Lemma D.1'/D.3'/D.4',
Theorem D.5).

 (1) TRUTH of the split majorants on (0, t1]: with
       DC + i DS := (phi_lam^c - phihat) e^{+s2 t^2/2}
     (true cumulants, mpmath dps 40), check
       |DC| <= e^{eps s2min t^2/2} WR(t),  |DS| <= e^{eps s2min t^2/2} WI(t),
       |Im e^{-z}| <= e^{eps s2min t^2/2} ZI(t),
     on m in {30, 60, 120} x K in {1, 2, 4} x w in {K/2, K}, 48-pt t-grids.
 (2) Per-piece table of the refined bound C_ker2(K, m) (m^2-scaled).
 (3) Monotone decrease of C_ker2 in m on [M(K), 3000].
 (4) Threshold scan: mker(K) := first m >= 30 with far_piece + tail_piece
     <= 0.2 (campaign 0.2-tolerance convention); headline constants at
     M(K) := max(180, mker(K)).
 (5) Comparison: crude (wp2a2_lib) vs refined (wp2a2_lib2) vs truth anchor
     (wp2-b NC-W4(6): 1.39 / 4.07 / 5.04).

Run: python3 wp2a2_nc3_refined.py
"""
import math
import os
import sys

import mpmath as mp

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import wp2a2_lib as L
import wp2a2_lib2 as L2
import wp2a2_nc1_model_err as NC1

mp.mp.dps = 40


def main():
    ok = True
    print("NC-A3: refined real-part-split Delta_ker bound")

    # ---------- (1) truth of the split majorants ----------
    print("(1) split-majorant truth ratios (PASS iff all <= 1):")
    print("      m  K    w     |DC|/WRdom   |DS|/WIdom   |Im e^-z|/ZIdom")
    wr_worst = wi_worst = zi_worst = 0.0
    for m in (30, 60, 120):
        for K in (1, 2, 4):
            S = L2.split_polys(K, m)
            B = S["B"]
            eps, t1, s2min = B["eps"], B["t1"], B["s2min"]
            for wfrac in (0.5, 1.0):
                w = K * wfrac
                lam = w / m
                s2, al, be, de, ga = NC1.true_model_coeffs(m, lam)
                rWR = rWI = rZI = 0.0
                for i in range(1, 49):
                    t = t1 * i / 48
                    ph = NC1.phi_c(m, lam, t)
                    gauss = mp.e ** (-s2 * t * t / 2)
                    err = (ph - gauss * NC1.hatQ(t, al, be, de, ga)) / gauss
                    dom = math.exp(eps * s2min * t * t / 2)
                    WRt = sum(c * t ** n for n, c in S["WR"].items())
                    WIt = sum(c * t ** n for n, c in S["WI"].items())
                    ZIt = sum(c * t ** n for n, c in S["ZI"].items())
                    rWR = max(rWR, float(abs(mp.re(err))) / (dom * WRt))
                    rWI = max(rWI, float(abs(mp.im(err))) / (dom * WIt))
                    imz = mp.im(ph / gauss)
                    rZI = max(rZI, float(abs(imz)) / (dom * ZIt))
                if wfrac == 1.0:
                    print("   %4d %2d %5.2f   %10.6f   %10.6f   %10.6f"
                          % (m, K, w, rWR, rWI, rZI))
                wr_worst = max(wr_worst, rWR)
                wi_worst = max(wi_worst, rWI)
                zi_worst = max(zi_worst, rZI)
    print("    GLOBAL max ratios: WR %.6f  WI %.6f  ZI %.6f"
          % (wr_worst, wi_worst, zi_worst))
    ok &= max(wr_worst, wi_worst, zi_worst) <= 1.0

    # ---------- (2) per-piece table ----------
    print("(2) refined per-piece table (m^2-scaled):")
    print("      m  K    m2*box    m2*tail     m2*far      dbar    m2*den"
          "     m2*Cker2")
    for m in (180, 190, 250, 300, 350, 379, 400, 500, 1000, 2000):
        for K in (1, 2, 4):
            r = L2.delta_ker_bound2(K, m)
            if r is None:
                print("   %4d %2d   -- not assembled --" % (m, K))
                continue
            print("   %4d %2d  %8.4f  %9.2e  %9.2e  %8.2e  %8.4f  %10.4f"
                  % (m, K, r["box_piece"], r["tail_piece"], r["far_piece"],
                     r["dbar"], r["den_piece"], r["Cker"]))

    # ---------- (4) thresholds ----------
    print("(4) threshold scan (unit step from m = 30): far+tail piece <= 0.2")
    mker = {}
    for K in (1, 2, 4):
        first = None
        for m in range(30, 2001):
            r = L2.delta_ker_bound2(K, m)
            if r is None:
                continue
            if r["far_piece"] + r["tail_piece"] <= 0.2:
                first = m
                break
        mker[K] = first
        print("    K=%d: mker = %s" % (K, first))

    # ---------- (3) monotone decrease ----------
    print("(3) monotone decrease of C_ker2 on [max(180, mker), 3000]:")
    for K in (1, 2, 4):
        lo = max(180, mker[K])
        ms = list(range(lo, 1001)) + list(range(1010, 3001, 10))
        prev, mono = None, True
        where = None
        for m in ms:
            r = L2.delta_ker_bound2(K, m)
            c = r["Cker"] if r else float("inf")
            if prev is not None and c > prev + 1e-12:
                mono, where = False, m
                break
            prev = c
        print("    K=%d: decreasing on [%d, 3000]: %s%s"
              % (K, lo, mono, "" if mono else " (fails at m=%d)" % where))
        ok &= mono

    # ---------- (5) headline + comparison ----------
    print("(5) headline constants and comparison:")
    print("      K   M(K)   C_ker2(M)   crude C_ker(M)   truth anchor")
    anchors = {1: 1.39, 2: 4.07, 4: 5.04}
    for K in (1, 2, 4):
        M = max(180, mker[K] or 10 ** 9)
        r2 = L2.delta_ker_bound2(K, M)
        r1 = L.delta_ker_bound(K, M)
        print("     %2d  %5d   %9.4f   %13.4f   %8.2f   (bound/truth = %.1fx)"
              % (K, M, r2["Cker"], r1["Cker"] if r1 else float("nan"),
                 anchors[K], r2["Cker"] / anchors[K]))
        ok &= r2["Cker"] > anchors[K]   # bound must sit above the truth

    print("\nNC-A3 VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
