#!/usr/bin/env python3
"""w2r_rep3: wave-3 repair session — wp2-a2 repairs R-F2 (genuine full
per-piece table rows at m = 181 and m = 367) and R-F6 (LFlow provenance).

Imports wp2-a2's shipped library wp2a2_lib2 (UNMODIFIED, from its original
directory) and:

(R-F2) prints genuine full per-piece rows of the refined Delta_ker bound at
  exactly the theorem thresholds (K, m) = (1, 180), (2, 181), (4, 367) —
  the rows Theorem D.5's table borrowed from m = 180/379 in the tail/den
  columns.  Every column is the true value at that (K, m); the C_ker column
  must reproduce the headline constants 30.89 / 209.03 / 37811 (NC-A3(5):
  30.8863 / 209.0224 / 37810.0442, displayed rounded UP).

(R-F6) prints LFlow at the theorem-used pairs (K, M(K)) = (1, 180),
  (2, 181), (4, 367) plus the non-theorem point (4, 180) whose value 0.92237
  the draft's section 5 quoted rounded UP as "0.9224".  Certifies:
  min over theorem-used pairs = 0.96388-level (>= 0.9638), every printed
  LFlow > 0.9223 (the safe restatement), and LFlow(4, 180) < 0.9224 (the
  unsafe rounding, confirmed).

Library floats are the draft's own certified-display convention (the
underlying certificates are wp2-b's; statuses unchanged).  Verdict
comparisons here use explicit safe-direction constants.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_WP2A2 = os.path.join(_HERE, "..", "wp2_a2")
sys.path.insert(0, _WP2A2)
import wp2a2_lib2 as L2   # noqa: E402  (shipped library, unmodified)

HEADLINE = {1: 30.89, 2: 209.03, 4: 37811.0}   # displayed rounded-up constants

def main():
    ok = True
    print("(R-F2) genuine full per-piece rows at the theorem thresholds:")
    print("      m  K    m2*box    m2*tail     m2*far      dbar    m2*den"
          "     m2*Cker2")
    for K, m in ((1, 180), (2, 181), (4, 367)):
        r = L2.delta_ker_bound2(K, m)
        if r is None:
            print("   %4d %2d   -- not assembled --" % (m, K))
            ok = False
            continue
        print("   %4d %2d  %8.4f  %9.2e  %9.2e  %8.2e  %8.4f  %10.4f"
              % (m, K, r["box_piece"], r["tail_piece"], r["far_piece"],
                 r["dbar"], r["den_piece"], r["Cker"]))
        # headline constants (rounded-up displays) must dominate the true row
        ok &= r["Cker"] <= HEADLINE[K]
    print("    Cker(row) <= displayed headline 30.89/209.03/37811: %s" % ok)

    print("(R-F6) LFlow provenance:")
    vals = {}
    for K, m in ((1, 180), (2, 181), (4, 367), (4, 180)):
        r = L2.delta_ker_bound2(K, m)
        vals[(K, m)] = r["LFlow"]
        print("    LFlow(K=%d, m=%3d) = %.5f" % (K, m, r["LFlow"]))
    theorem_min = min(vals[(1, 180)], vals[(2, 181)], vals[(4, 367)])
    c1 = theorem_min >= 0.9638
    c2 = all(v > 0.9223 for v in vals.values())
    c3 = vals[(4, 180)] < 0.9224
    print("    min over theorem-used pairs = %.5f >= 0.9638: %s" %
          (theorem_min, c1))
    print("    every value > 0.9223 (safe restatement): %s" % c2)
    print("    LFlow(4, 180) < 0.9224 (the draft's rounding was UP/unsafe):"
          " %s" % c3)
    ok = ok and c1 and c2 and c3
    print("VERDICT:", "PASS" if ok else "FAIL")

if __name__ == "__main__":
    main()
