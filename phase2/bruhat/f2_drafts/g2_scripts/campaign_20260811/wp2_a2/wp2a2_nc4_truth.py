"""NC-A4: ground truth of Delta_ker vs the refined bound; ports; v > 0.

 (1) Port cross-check: wp2a2_lib's re-implementations of wp2-b's buckets
     reproduce the wp2-b certified values at m = 180:
     Taylor T(K,180) = 0.00035/0.00100/0.01402; PW_closed = 10.278/21.063/
     187.414; Lin = 0.2308/0.2571/0.3719 (all from wp2_draft_b.md section 7,
     with the FIXED library per repairs B1 -- no printed digit moved).
 (2) TRUTH: measured m^2 |Delta_ker(k)| = m^2 |s2 (log(1+u) - log(1+v))|
     with u = r(k)-1 EXACT (integer Mahonian rows, Fractions) and
     v = F(0)-1 at the true cumulants of lam(k) (Newton, fixed float lib):
       m = 60: FULL scan of every interior k with 0 < w(k) <= K
               (reproduces wp2-b NC-W4(6) row: 1.386/4.070/5.022);
       m = 140: every 8th k (anchor row: 1.386/4.059/5.038).
     Verify measured <= refined bound C_ker2(K, m) at the same m.
 (3) v > 0: minimum measured v across all scanned k (both m); plus the
     PROVED clause: LFlow(K, m) = 1 - 12b - 36a^2/P0min^2 - PW/m^2 - T/m^2
     > 0 at the theorem's thresholds (Lemma D.4'(iii)), table on
     m in {180, 181, 367, 400, 1000}.

Run: python3 wp2a2_nc4_truth.py
"""
import math
import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import wp2a2_lib as L
import wp2a2_lib2 as L2
lib = L.lib


def lam_solve(m, k):
    """Newton for mu(lam) = k, lam >= 0 (k <= N/2), float lib cumulants."""
    lam = 1e-6
    for _ in range(80):
        mu, s2 = lib.cumulants(m, lam)[:2]
        step = (mu - k) / s2          # mu' = -s2
        lam = lam + step
        if lam < 0:
            lam = 1e-12
        if abs(step) < 1e-13:
            break
    mu, s2 = lib.cumulants(m, lam)[:2]
    return lam, abs(mu - k)


def v_model(m, lam):
    """v = F(0) - 1 at the true cumulants; F(0) = e^{h^2} P(0)^2/(P(h)P(-h))."""
    mu, s2, k3, k4, k5, k6 = lib.cumulants(m, lam)
    a = (k3 / 6.0) / s2 ** 1.5
    b = (-k4 / 24.0) / s2 ** 2
    d = (k5 / 120.0) / s2 ** 2.5
    g = (k6 / 720.0) / s2 ** 3

    def P(y):
        He = {}
        He[0], He[1] = 1.0, y
        for n in range(1, 8):
            He[n + 1] = y * He[n] - n * He[n - 1]
        return (1.0 + a * He[3] - b * He[4] + d * He[5]
                + (g + a * a / 2.0) * He[6] - a * b * He[7]
                + (b * b / 2.0 + a * d) * He[8])
    h = 1.0 / math.sqrt(s2)
    logF = 1.0 / s2 + 2.0 * math.log(P(0.0)) - math.log(P(h)) - math.log(P(-h))
    return math.expm1(logF), s2, logF


def scan(m, K, step):
    rows = lib.mahonian(m)
    N = m * (m - 1) // 2
    kc = N // 2
    worst, minv, count = 0.0, float("inf"), 0
    k = kc - 1 if N % 2 == 0 else kc      # start just left of center
    ks = list(range(k, 0, -step))
    for k in ks:
        lam, res = lam_solve(m, k)
        w = lam * m
        if w > K:
            break
        if w <= 0:
            continue
        u = float(Fraction(rows[k] * rows[k] - rows[k - 1] * rows[k + 1],
                           rows[k - 1] * rows[k + 1]))
        v, s2, _ = v_model(m, lam)
        dker = s2 * (math.log1p(u) - math.log1p(v))
        worst = max(worst, m * m * abs(dker))
        minv = min(minv, v)
        count += 1
    return worst, minv, count


def main():
    ok = True
    print("NC-A4: ground truth, ports, v > 0")

    print("(1) port cross-check at m = 180 (wp2-b certified values):")
    tgt_T = {1: 0.00035, 2: 0.00100, 4: 0.01402}
    tgt_PW = {1: 10.278, 2: 21.063, 4: 187.414}
    tgt_Lin = {1: 0.2308, 2: 0.2571, 4: 0.3719}
    for K in (1, 2, 4):
        T = L.taylor_bucket(K, 180)
        PW = L.pw_closed(K, 180)
        Lin = L.lin_bucket(K, 180)
        # PW tolerance 0.1% relative: the port is used only inside LFlow's
        # slack estimate; the MERGE table carries wp2-b's certified values
        # verbatim (which sit 0.001-0.149 ABOVE this port -- safe direction).
        okK = (abs(T - tgt_T[K]) < 6e-6 and abs(PW - tgt_PW[K]) < 1e-3 * tgt_PW[K]
               and abs(Lin - tgt_Lin[K]) < 6e-5 and PW <= tgt_PW[K] + 1e-9)
        print("    K=%d: T = %.5f (%.5f)  PW = %.3f (%.3f)  Lin = %.4f (%.4f)"
              "  match: %s" % (K, T, tgt_T[K], PW, tgt_PW[K], Lin, tgt_Lin[K],
                               okK))
        ok &= okK

    print("(2) measured m^2 |Delta_ker| vs refined bound:")
    anchors = {(60, 1): 1.386, (60, 2): 4.070, (60, 4): 5.022,
               (140, 1): 1.386, (140, 2): 4.059, (140, 4): 5.038}
    minv_all = float("inf")
    for m, step in ((60, 1), (140, 8)):
        for K in (1, 2, 4):
            worst, minv, count = scan(m, K, step)
            minv_all = min(minv_all, minv)
            r = L2.delta_ker_bound2(K, m)
            bound = r["Cker"] if r else float("inf")
            anchor = anchors[(m, K)]
            below = worst <= bound
            print("    m=%3d K=%d (step %d, %3d pts): measured = %.3f "
                  "(wp2-b anchor %.3f)  bound = %10.1f  measured<=bound: %s"
                  % (m, K, step, count, worst, anchor, bound, below))
            ok &= below
            if step == 1:
                ok &= abs(worst - anchor) < 0.02   # full scan must reproduce
    print("    min measured v over all scans: %.3e  (> 0: %s)"
          % (minv_all, minv_all > 0))
    ok &= minv_all > 0

    print("(3) v > 0 PROVED clause: LFlow(K, m) > 0 (Lemma D.4'(iii)):")
    for m in (180, 181, 367, 400, 1000):
        row = []
        for K in (1, 2, 4):
            r = L2.delta_ker_bound2(K, m)
            row.append(r["LFlow"] if r else float("nan"))
        good = all(x > 0 for x in row)
        print("    m=%4d:  K=1: %.5f  K=2: %.5f  K=4: %.5f   all > 0: %s"
              % (m, *row, good))
        ok &= good

    print("\nNC-A4 VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
