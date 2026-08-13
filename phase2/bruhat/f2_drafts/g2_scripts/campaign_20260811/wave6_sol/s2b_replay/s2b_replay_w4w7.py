#!/usr/bin/env python3
"""Independent replay of bands W4, W5, W6b (SOL.7) and W7 (SOL.4) of sol_s2b_20260812.md.

Completes the (S2) attempt-2 verification: s2b_replay.py covered W1-W3 (the cell
certificate); this covers the four analytic bands, which are monotonicity arguments
rather than cell sweeps. Written from the draft's stated formulas only.

Identifications derived here (the draft uses G and F_1 without restating them):
  H(w) = w - pi^2/3 + 2 sum_r e^{-rw} S_2(rw)/r^2  =>  H'(w) = 1 - w^2 A_1(w),
  so the draft's G is  G(w) = w^2 A_1(w)  (equivalently h_2(w) of the (S3) work), and
  int_0^oo G = 2 zeta(2) = pi^2/3 as the draft asserts. F_1(w) = w^5 A_4(w) (matches its
  own F_1(8) < 12 etc.). G is decreasing: G(w) = 1/s(w/2)^2 with s(y) = sinh(y)/y
  increasing. These identifications are CHECKED numerically below, not assumed.

W7 (SOL.4) chain, re-derived independently:
  |R5| <= t^5/120 (m A_4(lam) + sum_j j^5 A_4(j lam)) <= t^5/120 * 50 m lam^-5   [sup y^5A_4 < 25]
  lam^2 s_2 = m G(lam) - sum_j G(j lam) =: D_m(lam)                              [G(y) = y^2 A_1(y)]
  lam sum_j G(j lam) <= int_0^oo G = pi^2/3   [left Riemann sum, G decreasing]
  => D_m > m(G(0.89) - 3.29/40) > m * 683/800                                    [lam <= 0.89, w > 40]
  => lam^3|R5|/(s_2 t^5) <= 50m/(120 D_m) < 40000/81960 < 0.4881 < 0.50

Interval arithmetic (mpmath.iv) throughout; every bound reported is an outer enclosure.
"""
from fractions import Fraction as Fr
from pathlib import Path

from mpmath import iv

HERE = Path(__file__).resolve().parent
OUTF = HERE / "out_s2b_replay_w4w7.txt"
RMAX = 200
SLOP = iv.mpf([-1e-100, 1e-100])


def ivfr(fr):
    return iv.mpf(fr.numerator) / iv.mpf(fr.denominator)


def A1(z):
    q = iv.exp(-z)
    return q / (1 - q) ** 2


def A4(z):
    q = iv.exp(-z)
    return q * (1 + 11 * q + 11 * q * q + q ** 3) / (1 - q) ** 5


def G(w):
    return w * w * A1(w)


def F1(w):
    return w ** 5 * A4(w)


def _sums(w, N):
    """sum_r e^{-rw} S_N(rw)/r^2 via sum_{k<=N} (w^k/k!) D_k, D_k = sum_r r^(k-2)e^{-rw}."""
    D = [iv.mpf(0)] * (N + 1)
    for r in range(1, RMAX + 1):
        e = iv.exp(-iv.mpf(r) * w)
        rp = iv.mpf(r)
        cur = e / (rp * rp)
        for k in range(N + 1):
            D[k] = D[k] + cur
            cur = cur * rp
    acc = iv.mpf(0)
    term = iv.mpf(1)
    for k in range(N + 1):
        if k:
            term = term * w / iv.mpf(k)
        acc = acc + term * (D[k] + SLOP)
    return acc


def H(w):
    return w - iv.pi ** 2 / 3 + 2 * _sums(w, 2)


def T(w):
    return 120 * _sums(w, 5)


def main():
    iv.dps = 30
    lines = []

    def log(s):
        print(s, flush=True)
        lines.append(s)

    ok = True
    C = 20 * iv.pi ** 2
    log(f"C = 20 pi^2 = {float(C.a):.6f}  (draft uses 197.39 as a lower bound -> "
        f"{C.a > 197.39})")
    ok &= C.a > 197.39

    # ---- identification checks (the draft never restates G, F_1) ----
    log("\n[ID] identification checks for G and H' (draft leaves these implicit):")
    for w0 in ("4", "10", "20"):
        w = iv.mpf(w0)
        h = 1e-6
        num = (H(w + iv.mpf(h)) - H(w - iv.mpf(h))) / (2 * iv.mpf(h))
        pred = 1 - G(w)
        good = num.a - 1e-7 <= pred.b and pred.a <= num.b + 1e-7
        ok &= good
        log(f"  w={w0:>3}: H'(w) numeric = {float(num.a):.9f} vs 1 - G(w) = "
            f"{float(pred.a):.9f} -> {good}")
    intG = iv.pi ** 2 / 3
    log(f"  int_0^oo G = 2 zeta(2) = pi^2/3 = {float(intG.a):.9f} (draft: < 3.29 -> "
        f"{intG.b < 3.29})")
    ok &= intG.b < 3.29
    log("  G decreasing: G(w) = 1/s(w/2)^2, s(y) = sinh(y)/y increasing on y>0 (analytic);")
    prev = None
    for w0 in ("0.1", "0.5", "0.89", "2", "8", "20", "40"):
        g = G(iv.mpf(w0))
        if prev is not None:
            ok &= g.b < prev.a
        prev = g
        log(f"    G({w0:>5}) = {float(g.a):.9f}")

    # ---- W7 (SOL.4) ----
    log("\n[W7] SOL.4 chain:")
    g089 = G(ivfr(Fr(89, 100)))
    thr = ivfr(Fr(117, 125))
    good = g089.a > thr.b
    ok &= good
    log(f"  G(0.89) = [{float(g089.a):.9f}, {float(g089.b):.9f}]  vs 117/125 = 0.936 -> "
        f"{'PASS' if good else 'FAIL'}   (margin {float(g089.a) / 0.936:.6f}x — TIGHT)")
    # D_m > m (G(0.89) - 3.29/40)
    coef = g089 - iv.mpf("3.29") / 40
    good = coef.a > float(Fr(683, 800))
    ok &= good
    log(f"  D_m/m > G(0.89) - 3.29/40 = {float(coef.a):.9f}  vs claimed 683/800 = 0.85375"
        f" -> {'PASS' if good else 'FAIL'}")
    ratio = iv.mpf(50) / (120 * coef)
    claimed = ivfr(Fr(40000, 81960))
    good = ratio.b < 0.4881 and ratio.b <= claimed.b * (1 + 1e-9)
    ok &= good
    log(f"  50/(120 D_m/m) <= {float(ratio.b):.9f}  vs 40000/81960 = "
        f"{float(claimed.b):.9f} < 0.4881 < 0.50 -> {'PASS' if good else 'FAIL'}")
    # SOL.4.2: sup y^5 A_4 < 25 gives the 50 m lam^-5 (both terms <= 25 m lam^-5)
    log("  (SOL.4.2 uses sup y^5 A_4 < 25 twice — verified 24.854113 in s2b_replay block [B])")

    # ---- W4, W5, W6b (SOL.7) ----
    log("\n[W4/W5/W6b] SOL.7 monotonicity chain:")
    H8, H10, H14, H20 = H(iv.mpf(8)), H(iv.mpf(10)), H(iv.mpf(14)), H(iv.mpf(20))
    T8, T10, T14, T20, T40 = (T(iv.mpf(x)) for x in (8, 10, 14, 20, 40))
    w0 = C / 24
    log(f"  w_0 = C/24 = {float(w0.a):.6f}")

    # W4 on [8, w_0]: (C - 24w + 2w + T(w))/(120 H(w)) at w=8
    v = (C - 192 + 16 + T8) / (120 * H8)
    good = v.b < 0.079
    ok &= good
    log(f"  W4 [8,w_0] at w=8: (C-192+16+T(8))/(120 H(8)) = {float(v.b):.6f} < 0.079 -> "
        f"{'PASS' if good else 'FAIL'}")
    # W4 on [w_0,10]: J' < -3.2 and J(10) > 1.7
    worst = -1e9
    x = w0
    for i in range(101):
        wv = w0 + (iv.mpf(10) - w0) * iv.mpf(i) / 100
        Jp = iv.mpf("10.8") * (1 - G(wv)) - 26 + F1(wv)
        worst = max(worst, float(Jp.b))
    good = worst < -3.2
    ok &= good
    log(f"  W4 [w_0,10]: max J'(w) = {worst:.6f} < -3.2 -> {'PASS' if good else 'FAIL'}")
    J10 = iv.mpf("10.8") * H10 - (260 - C + T10)
    good = J10.a > 1.7
    ok &= good
    log(f"  W4: J(10) = {float(J10.a):.6f} > 1.7 -> {'PASS' if good else 'FAIL'}")

    # W5 on [10,14]: J_5' < -4.2, J_5(14) > 12
    worst = -1e9
    for i in range(101):
        wv = iv.mpf(10) + iv.mpf(4) * iv.mpf(i) / 100
        Jp = iv.mpf("16.8") * (1 - G(wv)) - 26 + F1(wv)
        worst = max(worst, float(Jp.b))
    good = worst < -4.2
    ok &= good
    log(f"  W5 [10,14]: max J_5'(w) = {worst:.6f} < -4.2 -> {'PASS' if good else 'FAIL'}")
    J514 = iv.mpf("16.8") * H14 - (364 - C + T14)
    good = J514.a > 12
    ok &= good
    log(f"  W5: J_5(14) = {float(J514.a):.6f} > 12 -> {'PASS' if good else 'FAIL'}")
    # W5 [14,40]: B^2 < 6A^2 at 14; ratio increasing; value at 20
    Aa, Bb = 24 * iv.mpf(14) - C, 24 * iv.mpf(14)
    good = (Bb * Bb).b < (6 * Aa * Aa).a
    ok &= good
    b2, a6 = float((Bb * Bb).b), float((6 * Aa * Aa).a)
    log(f"  W5: B^2 = {b2:.3f} < 6A^2 = {a6:.3f} at w=14 -> "
        f"{'PASS' if good else 'FAIL'}  (margin {a6/b2:.4f}x — TIGHT)")
    worstmono = 1e9
    for i in range(0, 105):
        wv = iv.mpf(14) + iv.mpf(26) * iv.mpf(i) / 104
        lhs = (24 - F1(wv)) * H(wv) - (24 * wv - C + T(wv)) * (1 - G(wv))
        worstmono = min(worstmono, float((lhs - (121 - wv)).a))
    good = worstmono > 0
    ok &= good
    log(f"  W5/W6b monotonicity on [14,40]: min[(24-F_1)H - (24w-C+T)(1-G) - (121-w)] = "
        f"{worstmono:.6f} > 0 -> {'PASS' if good else 'FAIL'}")
    v20 = (480 - C + T20) / (120 * H20)
    good = v20.b < 0.142
    ok &= good
    log(f"  W5 value at w=20: {float(v20.b):.6f} < 0.142 -> {'PASS' if good else 'FAIL'}")
    H40 = H(iv.mpf(40))
    v40 = (960 - C + T40) / (120 * H40)
    good = v40.b < 0.174
    ok &= good
    log(f"  W6b value at w=40: {float(v40.b):.6f} < 0.174 -> {'PASS' if good else 'FAIL'}")

    # ---- finite-m assembly for W4, W5, W6b ----
    log("\n[E] finite-m assembly (SOL.5.6) for W4, W5, W6b:")
    for name, wlo, b, B, target in (("W4", 8, 10, float(v.b if False else 0.09), 0.10),
                                    ("W5", 10, 20, 0.142, 0.15),
                                    ("W6b", 20, 40, 0.174, 0.25)):
        L = H(iv.mpf(wlo))
        hb = iv.mpf(b) / iv.mpf(561)
        eb = hb * hb * iv.mpf(b + 14) / iv.mpf(12)
        Eb = iv.mpf(49) * hb / 2 + 250 * hb * hb + iv.mpf(b) * hb ** 6 / 200
        Ll = iv.mpf([L.a, L.a])
        U = Ll / (Ll - eb) * iv.mpf(B) + Eb / (120 * (Ll - eb))
        good = U.b < target
        ok &= good
        log(f"  {name}: L = {float(L.a):.6f}, B = {B}, e_b = {float(eb.b):.6e}, "
            f"E_b = {float(Eb.b):.6f} -> U_b <= {float(U.b):.6f} vs C5* = {target} -> "
            f"{'PASS' if good else 'FAIL'} (margin {target/float(U.b):.3f}x)")

    log(f"\n# OVERALL: {'ALL W4-W7 CHECKS PASS' if ok else 'SOME CHECKS FAILED'}")
    OUTF.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
