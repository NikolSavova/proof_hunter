#!/usr/bin/env python3
"""(S3) Lemma SOL.3 certificate — the 18.9M-box computation Sol asserted but never ran
(referee_numerics_sol_s3.md F1), executed as an ADAPTIVE certified interval computation
(explicitly permitted by that report: "an equivalent coarser certified computation — §6
suggests the resolution budget is generous"). Refines only where bounds are tight; a box
that still fails at the draft's own floor resolution (w-width 1/2048, z-width 1/256) is
recorded as a hard FAILURE.

Method: mpmath.iv interval arithmetic (directed rounding — every printed enclosure is a
true outer bound), dps set below; deviation from the draft's "exact rational" wording is
documented in the accompanying note. The Euler-Maclaurin remainder radius uses the
CORRECTED constant 2 * 10^12 * w * lam^8 / 1209600 (referee finding F2: the draft's
1/1209600 kernel constant misses the B_8 boundary term, true factor (2 - 2^-7) = 1.992;
we apply the referee's prescribed repair, a clean factor 2).

Structure per referee/draft spec (SOL.1-SOL.9):
  J(w, lam) = F3^2/F2^2 - F4/(2 F2),  lam = w z / 561,  z in [0,1]
  F_n = G_n(w) + w(h_n(lam) - h_n(0)) - (lam/2)(h_n(w) - h_n(0))
        - (lam^2/12) h_n'(w) + (lam^4/720) h_n'''(w) - (lam^6/30240) h_n^(5)(w) + E_n8
  (h_n is EVEN — h_2 = 1/s(x/2)^2, h_3 = 2 cosh(x/2)/s^3, h_4 = (2 cosh x + 4)/s^4 with
   s(y) = sinh(y)/y — so h_n'(0) = h_n'''(0) = h_n^(5)(0) = 0, and the s-series form is
   smooth through lam = 0, no case split.)
  G_n(w) = (n-1)! w - n! zeta2 + sum_{k=1..64} e^{-kw}/k^2 P_n(kw)  (+ tail slop; for
   w >= 4 the k > 64 tail is < 1e-95: terms <= 5 (kw)^4 e^{-kw} <= 65^8 e^{-260}).
  h_n^(p)(w) via Leibniz with phi_n^(r)(w) = sum_k (-k)^r k^{n-1} e^{-kw} (same K=64).
  zeta(2) via the draft's rational enclosure 1644934066848226..7 / 10^15.

Certification per box: F2.lower > 1/10  AND  J.upper <= band target.
Bands/targets (SOL.7): W1 [4,5] 1/2 | W2 [5,6] 13/20 | W3 [6,8] 9/10 | W4 [8,10] 11/10
| W5 [10,20] 3/2 | W6b [20,40] 17/10.

Selftest gauntlet (referee-measured anchors) runs first at two precisions; the sweep
aborts if any anchor falls outside its enclosure.
"""
import json, math, sys, time
from fractions import Fraction as Fr
from pathlib import Path

from mpmath import iv

HERE = Path(__file__).resolve().parent
OUTF = HERE / "out_s3_certificate.txt"
CKPT = HERE / "ckpt.json"

BANDS = {  # name: (w_lo, w_hi, target numerator, denominator)
    "W1": (Fr(4), Fr(5), 1, 2),
    "W2": (Fr(5), Fr(6), 13, 20),
    "W3": (Fr(6), Fr(8), 9, 10),
    "W4": (Fr(8), Fr(10), 11, 10),
    "W5": (Fr(10), Fr(20), 3, 2),
    "W6b": (Fr(20), Fr(40), 17, 10),
}
WFLOOR, ZFLOOR = Fr(1, 2048), Fr(1, 256)
K = 64
TINY = None  # set after dps


def hull(x, y):
    x, y = iv.mpf(x), iv.mpf(y)
    return iv.mpf([min(x.a, y.a), max(x.b, y.b)])


def ivfr(fr):
    return iv.mpf(fr.numerator) / iv.mpf(fr.denominator)


def setup(dps):
    global TINY, Z2
    iv.dps = dps
    TINY = iv.mpf([-1e-90, 1e-90])
    Z2 = (iv.mpf(1644934066848226) + iv.mpf([0, 1])) / iv.mpf(10) ** 15


FACT = [1, 1, 2, 6, 24]


def P(n, y):
    acc = iv.mpf(0)
    term = iv.mpf(1)
    for r in range(n + 1):
        if r:
            term = term * y / iv.mpf(r)
        acc += term
    return iv.mpf(FACT[n]) * acc


_wcache = {}


def wside(wlo, whi):
    key = (wlo, whi)
    if key in _wcache:
        return _wcache[key]
    w = hull(ivfr(wlo), ivfr(whi))
    q = iv.exp(-w)
    qp = [None, q]
    for k in range(2, K + 1):
        qp.append(qp[-1] * q)
    G = {}
    for n in (2, 3, 4):
        acc = iv.mpf(FACT[n - 1]) * w - iv.mpf(FACT[n]) * Z2
        for k in range(1, K + 1):
            acc += qp[k] / iv.mpf(k * k) * P(n, iv.mpf(k) * w)
        G[n] = acc + TINY
    # phi_n^{(r)}(w) = sum_k (-1)^r k^{n-1+r} e^{-kw}
    phi = {}
    for n in (2, 3, 4):
        for r in range(0, 6):
            acc = iv.mpf(0)
            for k in range(1, K + 1):
                acc += iv.mpf(k ** (n - 1 + r)) * qp[k]
            phi[(n, r)] = (acc if r % 2 == 0 else -acc) + TINY
    # h_n^{(p)}(w), p in {0,1,3,5}, Leibniz on x^n * phi_n(x)
    hd = {}
    for n in (2, 3, 4):
        for p in (0, 1, 3, 5):
            acc = iv.mpf(0)
            for j in range(0, min(p, n) + 1):
                c = math.comb(p, j) * (FACT[n] // FACT[n - j])
                acc += iv.mpf(c) * w ** (n - j) * phi[(n, p - j)]
            hd[(n, p)] = acc
    res = (G, hd)
    _wcache[key] = res
    return res


def s_series(y):
    """sinh(y)/y enclosure for 0 <= y <= 0.04: 4 terms + tail (ratio <= y^2/72)."""
    y2 = y * y
    acc = iv.mpf(1) + y2 / iv.mpf(6) + y2 * y2 / iv.mpf(120) + y2 * y2 * y2 / iv.mpf(5040)
    t8 = y2 * y2 * y2 * y2 / iv.mpf(362880)
    return acc + hull(iv.mpf(0), t8 * iv.mpf("1.01"))


def ivcosh(x):
    return (iv.exp(x) + iv.exp(-x)) / 2


def h_small(n, lam):
    """h_n(lam) for lam in [0, 0.0713] via the smooth even forms."""
    s = s_series(lam / 2)
    if n == 2:
        return 1 / (s * s)
    if n == 3:
        return 2 * ivcosh(lam / 2) / (s * s * s)
    return (2 * ivcosh(lam) + 4) / (s * s * s * s)


H0 = {2: 1, 3: 2, 4: 6}


def Fn(n, w, lam, G, hd):
    lam2 = lam * lam
    lam4 = lam2 * lam2
    lam6 = lam4 * lam2
    return (G[n] + w * (h_small(n, lam) - iv.mpf(H0[n]))
            - lam / 2 * (hd[(n, 0)] - iv.mpf(H0[n]))
            - lam2 / iv.mpf(12) * hd[(n, 1)]
            + lam4 / iv.mpf(720) * hd[(n, 3)]
            - lam6 / iv.mpf(30240) * hd[(n, 5)])


def Erad(w, lam):
    """CORRECTED EM remainder radius (F2 repair): 2 * 10^12 * w * lam^8 / 1209600."""
    lamu = iv.mpf([lam.b, lam.b])
    wu = iv.mpf([w.b, w.b])
    r = 2 * iv.mpf(10) ** 12 * wu * lamu ** 8 / iv.mpf(1209600)
    return hull(-r, r)


def box_ok(wlo, whi, zlo, zhi, target_iv):
    G, hd = wside(wlo, whi)
    w = hull(ivfr(wlo), ivfr(whi))
    z = hull(ivfr(zlo), ivfr(zhi))
    lam = w * z / iv.mpf(561)
    F = {n: Fn(n, w, lam, G, hd) + Erad(w, lam) for n in (2, 3, 4)}
    if not (F[2].a > 0.1):
        return False, None
    J = (F[3] / F[2]) ** 2 - F[4] / (2 * F[2])
    return (J.b <= target_iv.a), J


def certify_band(name, log):
    wlo, whi, tn, td = BANDS[name]
    target = ivfr(Fr(tn, td))
    stack = [(wlo, whi, Fr(0), Fr(1), 0)]
    leaves = fails = 0
    supJ = -1e9
    t0 = time.time()
    while stack:
        bw0, bw1, bz0, bz1, d = stack.pop()
        ok, J = box_ok(bw0, bw1, bz0, bz1, target)
        if ok:
            leaves += 1
            if J is not None:
                supJ = max(supJ, float(J.b))
            if leaves % 5000 == 0:
                log(f"  {name}: {leaves} leaves, {len(stack)} pending, depth~{d}, {time.time()-t0:.0f}s")
            continue
        ww, zw = bw1 - bw0, bz1 - bz0
        at_floor_w, at_floor_z = ww <= WFLOOR, zw <= ZFLOOR
        if at_floor_w and at_floor_z:
            fails += 1
            log(f"  {name}: HARD FAIL box w=[{bw0},{bw1}] z=[{bz0},{bz1}] "
                f"J_upper={float(J.b) if J else 'F2<=1/10'}")
            continue
        # split the dimension farther (relatively) from its floor
        if (not at_floor_w) and (at_floor_z or ww / WFLOOR >= zw / ZFLOOR):
            mid = (bw0 + bw1) / 2
            stack += [(bw0, mid, bz0, bz1, d + 1), (mid, bw1, bz0, bz1, d + 1)]
        else:
            mid = (bz0 + bz1) / 2
            stack += [(bw0, bw1, bz0, mid, d + 1), (bw0, bw1, mid, bz1, d + 1)]
    return leaves, fails, supJ, time.time() - t0


def selftest(log):
    """Anchors from referee_numerics_sol_s3.md (independent measurements)."""
    # G_4(4) = 0.2323482989 (also the scout guard value 0.2323483)
    G, _ = wside(Fr(4), Fr(4))
    assert G[4].a < 0.2323482989 < G[4].b + 1e-9, f"G_4(4) anchor: {G[4]}"
    # J(w=5, m=561) = 0.46031849 (referee ref2, 8 digits); z=1 exactly
    G5, hd5 = wside(Fr(5), Fr(5))
    w = ivfr(Fr(5)); lam = w / iv.mpf(561)
    F = {n: Fn(n, w, lam, G5, hd5) + Erad(w, lam) for n in (2, 3, 4)}
    J = (F[3] / F[2]) ** 2 - F[4] / (2 * F[2])
    assert J.a < 0.460318495 and J.b > 0.460318485, f"J(5,561) anchor (referee gave 8 digits): {J}"
    assert float(J.b) - float(J.a) < 1e-6, f"J(5,561) enclosure too wide: {J}"
    # h consistency: smooth form vs direct series at lam = 0.05 (inside range)
    lam = iv.mpf(1) / iv.mpf(20)
    for n in (2, 3, 4):
        direct = lam ** n * sum(iv.mpf(k ** (n - 1)) * iv.exp(-iv.mpf(k) * lam)
                                for k in range(1, 2500)) + TINY
        hs = h_small(n, lam)
        assert not (hs.b < direct.a or direct.b - 1e-40 > hs.b + 1e-6), \
            f"h_{n}(0.05) mismatch: {hs} vs {direct}"
    log("SELFTEST: all anchors pass")


def main():
    log_lines = []

    def log(s):
        print(s, flush=True)
        log_lines.append(s)

    bands = sys.argv[1:] or list(BANDS)
    done = json.loads(CKPT.read_text()) if CKPT.exists() else {}
    for dps in (30, 50):  # dual-precision selftest, house precedent
        _wcache.clear()
        setup(dps)
        selftest(log)
        log(f"selftest OK at dps={dps}")
    setup(40)
    _wcache.clear()
    total_fails = 0
    for name in bands:
        if name in done:
            log(f"{name}: already certified (checkpoint) — {done[name]}")
            continue
        log(f"== {name}: target {BANDS[name][2]}/{BANDS[name][3]}, "
            f"w in [{BANDS[name][0]},{BANDS[name][1]}] ==")
        leaves, fails, supJ, dt = certify_band(name, log)
        verdict = "CERTIFIED" if fails == 0 else f"FAILED ({fails} hard-fail boxes)"
        log(f"{name}: {verdict} | {leaves} certified leaves | sup J_upper <= {supJ:.6f} "
            f"| {dt:.0f}s")
        total_fails += fails
        if fails == 0:
            done[name] = {"leaves": leaves, "supJ_upper": supJ, "secs": round(dt)}
            CKPT.write_text(json.dumps(done, indent=1))
        _wcache.clear()  # bound memory between bands
    log(f"# OVERALL: {'PASS — all bands certified' if total_fails == 0 else 'FAIL'} "
        f"(EM constant: corrected 2x per referee F2; method: mpmath.iv directed rounding, "
        f"dps 40, selftests dual dps 30/50)")
    OUTF.write_text("\n".join(log_lines) + "\n")


if __name__ == "__main__":
    main()
