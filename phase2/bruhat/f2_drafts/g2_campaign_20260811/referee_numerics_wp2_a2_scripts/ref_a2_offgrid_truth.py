"""Referee check R3 (wp2-a2 numerics): OFF-GRID truth of the Lemma D.1/D.1'
majorants.  The draft's NC-A1(b,c)/NC-A3(1) used m in {30,60,120},
w in {K/4, K/2, K} (resp {K/2, K}), and 48-point t-grids t = t1*i/48.
Here: m in {45, 240}, w in {0.15K, 0.7K, 0.95K, K}, OFFSET 64-point grids
t = t1*(i - 0.37)/64 (never hitting the draft's grid points, and probing
closer to t = 0), all at mpmath dps 40.

Bounds checked (must all be <= 1):
  (A.1a)  |phi_lam^c(t)| / e^{-(1-eps) s2min t^2/2}
  (D.1')  |DC| / (EE*WR),  |DS| / (EE*WI),  |Im e^{-z}| / (EE*ZI),
          |Re e^{-z}| / EE
  (Q-side) |Re Q - 1| / VE,  |Im Q| / VO    (true cumulants vs box majorants)

Run: python3 ref_a2_offgrid_truth.py
"""
import os
import sys

import mpmath as mp

_HERE = os.path.dirname(os.path.abspath(__file__))
_WP = os.path.normpath(os.path.join(_HERE, "..", "..", "g2_scripts",
                                    "campaign_20260811", "wp2_a2"))
sys.path.insert(0, _WP)
import wp2a2_lib as L            # noqa: E402
import wp2a2_lib2 as L2          # noqa: E402
import wp2a2_nc1_model_err as NC1  # noqa: E402

mp.mp.dps = 40


def peval(p, t):
    return sum(c * t ** n for n, c in p.items())


def main():
    ok = True
    print("R3: off-grid truth of the D.1/D.1' majorants (dps 40)")
    print("      m  K     w     A.1a      DC/WR     DS/WI     Im/ZI"
          "     Re/EE     ReQ/VE    ImQ/VO")
    gmax = dict(a=0.0, wr=0.0, wi=0.0, zi=0.0, re=0.0, ve=0.0, vo=0.0)
    for m in (45, 240):
        for K in (1, 2, 4):
            S = L2.split_polys(K, m)
            B = S["B"]
            eps, t1, s2min = B["eps"], B["t1"], B["s2min"]
            for wfrac in (0.15, 0.7, 0.95, 1.0):
                w = K * wfrac
                lam = w / m
                s2, al, be, de, ga = NC1.true_model_coeffs(m, lam)
                r = dict(a=0.0, wr=0.0, wi=0.0, zi=0.0, re=0.0, ve=0.0,
                         vo=0.0)
                for i in range(1, 65):
                    t = t1 * (i - 0.37) / 64
                    ph = NC1.phi_c(m, lam, t)
                    gauss = mp.e ** (-s2 * t * t / 2)
                    dom_a = mp.e ** (-(1 - eps) * s2min * t * t / 2)
                    EE = mp.e ** (eps * s2min * t * t / 2)
                    err = (ph - gauss * NC1.hatQ(t, al, be, de, ga)) / gauss
                    ez = ph / gauss                  # e^{-z}
                    Q = NC1.hatQ(t, al, be, de, ga)
                    r["a"] = max(r["a"], float(abs(ph) / dom_a))
                    r["wr"] = max(r["wr"], float(abs(mp.re(err))
                                                 / (EE * peval(S["WR"], t))))
                    r["wi"] = max(r["wi"], float(abs(mp.im(err))
                                                 / (EE * peval(S["WI"], t))))
                    r["zi"] = max(r["zi"], float(abs(mp.im(ez))
                                                 / (EE * peval(S["ZI"], t))))
                    r["re"] = max(r["re"], float(abs(mp.re(ez)) / EE))
                    r["ve"] = max(r["ve"], float(abs(mp.re(Q) - 1)
                                                 / peval(S["VE"], t)))
                    r["vo"] = max(r["vo"], float(abs(mp.im(Q))
                                                 / peval(S["VO"], t)))
                if wfrac in (0.95, 1.0):
                    print("   %4d %2d %5.2f  %8.6f  %8.6f  %8.6f  %8.6f"
                          "  %8.6f  %8.6f  %8.6f"
                          % (m, K, w, r["a"], r["wr"], r["wi"], r["zi"],
                             r["re"], r["ve"], r["vo"]))
                for k in gmax:
                    gmax[k] = max(gmax[k], r[k])
    print("  GLOBAL maxima:", "  ".join("%s %.6f" % (k, v)
                                        for k, v in gmax.items()))
    ok &= all(v <= 1.0 for v in gmax.values())
    print("R3 VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
