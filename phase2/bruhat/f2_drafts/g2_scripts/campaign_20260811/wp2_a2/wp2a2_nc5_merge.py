"""NC-A5: the merged closed-form T.9 (Theorem T.9-final) and its thresholds.

 (1) Merged C_R(K) table at M(K) := max(180, mker(K)):
       C_R(K) := PW + T + C_ker2(K, M(K))    [theorem bucket, log-form]
     in both flavors -- PW grid-certified (wp2-b, m <= 2000; K = 4 row
     carries repair B3's caveat) and PW closed-form (all m >= 180) -- with
     wp2-b's CERTIFIED values carried verbatim (my ports sit 0.001-0.149
     below them; safe direction).
 (2) Lin-hypothesis discharge (wp2-b Lemma W.5 conditionality):
       H(K, m) := (1.080/m)(1 + c_w(K) K^2) + C_R_closed(K)/m^2 <= 1/2
     at m = M(K), and H decreasing in m (every piece is).  c_w per the
     repaired statement (repairs B2): c_w(1) = 0.407, c_w(2) = 0.466,
     c_w(4) = 1.
 (3) Large-m safety: C_ker2(K, 10000) < C_ker2(K, 3000) (the nc3 monotone
     scan stops at 3000; every row is a negative power of m asymptotically).
 (4) Coverage: M(K) <= 400 for all K -- against harness_m200_20260811's
     exact range 4 <= m <= 400: no uncovered m for any K <= 4 (K = 3 via
     the K = 4 row).
 (5) Honesty line: provided C_R vs the measured needed constant
     (NC-T8 / wp2-b needed_env <= 0.35).

Run: python3 wp2a2_nc5_merge.py
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import wp2a2_lib as L
import wp2a2_lib2 as L2

# wp2-b certified bucket values (wp2_draft_b.md section 7 / repairs B1: no
# printed digit moved with the fixed library), carried verbatim:
PW_GRID = {1: 1.5491, 2: 4.0889, 4: 4.9126}   # m <= 2000; K=4: repair B3 note
PW_CLOSED = {1: 10.278, 2: 21.063, 4: 187.414}  # all m >= 180
TAYLOR = {1: 0.00035, 2: 0.00100, 4: 0.01402}   # m >= 180
LIN = {1: 0.2308, 2: 0.2571, 4: 0.3719}         # m >= 180
CW = {1: 0.407, 2: 0.466, 4: 1.0}               # repairs B2 (c_w(4) = 1)
MK = {1: 180, 2: 181, 4: 367}                   # NC-A3(4) thresholds


def main():
    ok = True
    print("NC-A5: merged closed-form T.9")

    print("(1) merged C_R(K) table at M(K):")
    print("      K  M(K)   C_ker2(M)   C_R grid(m<=2000)   C_R closed(all m>=M)")
    CRC = {}
    for K in (1, 2, 4):
        M = MK[K]
        r = L2.delta_ker_bound2(K, M)
        ck = r["Cker"]
        crg = PW_GRID[K] + TAYLOR[K] + ck
        crc = PW_CLOSED[K] + TAYLOR[K] + ck
        CRC[K] = crc
        print("     %2d  %4d   %9.4f   %16.4f   %19.4f" % (K, M, ck, crg, crc))

    print("(2) Lin discharge: H(K, m) = (1.080/m)(1 + c_w K^2)"
          " + C_R_closed/m^2 <= 1/2:")
    for K in (1, 2, 4):
        M = MK[K]
        H = (1.080 / M) * (1.0 + CW[K] * K * K) + CRC[K] / M ** 2
        good = H <= 0.5
        print("    K=%d: H(%d) = %.4f  <= 1/2: %s   (decreasing in m: both"
              " pieces are)" % (K, M, H, good))
        ok &= good

    print("(3) large-m safety (beyond the nc3 scan):")
    for K in (1, 2, 4):
        c3 = L2.delta_ker_bound2(K, 3000)["Cker"]
        c10 = L2.delta_ker_bound2(K, 10000)["Cker"]
        good = c10 < c3
        print("    K=%d: C_ker2(3000) = %.4f  >  C_ker2(10000) = %.4f : %s"
              % (K, c3, c10, good))
        ok &= good

    print("(4) coverage vs the exact harness (4 <= m <= 400, "
          "harness_m200_20260811):")
    allcov = all(MK[K] <= 400 for K in (1, 2, 4))
    print("    M(K) = 180 / 181 / 367, all <= 400:", allcov,
          "\n    -> for every K <= 4 (K = 3 via the K = 4 row), every m >= 4"
          "\n       is covered: exact harness on [4, 400], Theorem T.9-final"
          "\n       on [M(K), infinity); the two ranges overlap.")
    ok &= allcov

    print("(5) honesty: provided C_R_closed vs measured need (NC-T8 <= 0.35):")
    for K in (1, 2, 4):
        print("    K=%d: provided %.1f = %.0fx the worst measured need 0.35"
              % (K, CRC[K], CRC[K] / 0.35))

    print("\nNC-A5 VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
