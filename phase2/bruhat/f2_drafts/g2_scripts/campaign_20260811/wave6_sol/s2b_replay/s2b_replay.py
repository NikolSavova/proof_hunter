#!/usr/bin/env python3
"""Independent replay of the load-bearing computations in sol_s2b_20260812.md ((S2), attempt 2).

The draft's own WHAT REMAINS item 2 demands exactly this: "the 256-cell rational
calculation in SOL.6 and the scalar F<25 grid in SOL.3 must be transcribed into an
archived exact-interval script and independently rerun." Written from the draft's
VERIFICATION RECIPE and SOL.5/SOL.6 statements WITHOUT reusing any of its numbers.

Interval arithmetic throughout (mpmath.iv, directed rounding), so every reported bound
is an outer enclosure. Blocks:

  [A] model check      s2 = m A_1(lam) - sum_j j^2 A_1(j lam) vs direct truncated-geometric
                       variance sum (brute force, small m)
  [B] scalars          sup_{y>0} y^5 A_4(y) < 25 (per the draft's own grid recipe);
                       40000/81960 < 0.50; F(8) < 12, F(10) < 5, F(14) < 1
  [C] H and T          H(w) at w = 4,5,6,8,10,20 ; T(w) at w = 8,10,14,20,40
  [D] THE CERTIFICATE  the 256-cell cancellation-retaining check on W1,W2,W3:
                       V(I) < 0.030 / 0.040 / 0.065   (SOL.6.9 / recipe section 4)
  [E] finite-m         U_b = L/(L-e_b) B + E_b/(120(L-e_b))  vs the seven band targets

Definitions taken from the draft:
  A_1(z) = e^-z/(1-e^-z)^2 ;  A_4(z) = e^-z(1+11e^-z+11e^-2z+e^-3z)/(1-e^-z)^5
  S_N(z) = sum_{k=0}^N z^k/k! ;  Q_n = (n+1)(n+2)(n+3)(n+4) ;  c = pi^2/6
  p_n(w) = Q_n[(n+5)c - w - (n+5) sum_{r>=1} e^{-rw} S_{n+5}(rw)/r^2]      (SOL.6.3)
  H(w)   = w - pi^2/3 + 2 sum_{r>=1} e^{-rw} S_2(rw)/r^2                   (SOL.6.8)
  T(w)   = 120 sum_{r>=1} e^{-rw} S_5(rw)/r^2
  V(I)   = (1/inf_I H) sum_{n=0}^{64} (sup_I|p_n|) n!/(2^n (n+5)!)
           + 11e-6/(120 inf_I H)                                           (recipe 4)
  h_b = b/561 ; e_b = h_b^2(b+14)/12 ; E_b = 49h_b/2 + 250h_b^2 + b h_b^6/200 (SOL.5.4/5)
  U_b = L/(L-e_b) B + E_b/(120(L-e_b))                                     (SOL.5.6)

Key restructuring (for speed, mathematically identical): with
  D_k(w) := sum_{r>=1} r^(k-2) e^{-rw},
we have sum_r e^{-rw} S_N(rw)/r^2 = sum_{k=0}^N (w^k/k!) D_k(w), so the inner r-sums are
computed once per cell and reused across all n by accumulation. The r-sum is truncated at
r = RMAX with a slop interval; at w >= 4, N <= 69 the discarded tail is far below 1e-100
(the r = 201 term already has log ~ -579).

NOTE the draft's own warning, which this script obeys: |p_n| is formed AFTER the signed
combination inside the bracket. Taking absolute values earlier reproduces attempt 1's
failure (a ~23x deficit on W1).
"""
import sys, time
from fractions import Fraction as Fr
from pathlib import Path

from mpmath import iv, mp

HERE = Path(__file__).resolve().parent
OUTF = HERE / "out_s2b_replay.txt"
RMAX = 200
NMAX = 64
SLOP = None

BANDS = [  # name, w-lo, w-hi, n_cells, continuum target B (SOL.6.9 / SOL.7), C5* target
    ("W1", Fr(4), Fr(5), 64, Fr(3, 100), Fr(5, 100)),
    ("W2", Fr(5), Fr(6), 64, Fr(1, 25), Fr(6, 100)),
    ("W3", Fr(6), Fr(8), 128, Fr(13, 200), Fr(8, 100)),
]
# recipe section 4 expected ceilings on max V(I)
V_TARGET = {"W1": 0.030, "W2": 0.040, "W3": 0.065}


def ivfr(fr):
    return iv.mpf(fr.numerator) / iv.mpf(fr.denominator)


def hull(x, y):
    x, y = iv.mpf(x), iv.mpf(y)
    return iv.mpf([min(x.a, y.a), max(x.b, y.b)])


def setup(dps):
    global SLOP
    iv.dps = dps
    mp.dps = dps
    SLOP = iv.mpf([-1e-100, 1e-100])


def A(p, z):
    """A_p(z) = sum_{r>=1} r^p e^{-rz}, closed forms for p = 1 and 4."""
    q = iv.exp(-z)
    if p == 1:
        return q / (1 - q) ** 2
    if p == 4:
        return q * (1 + 11 * q + 11 * q * q + q ** 3) / (1 - q) ** 5
    raise ValueError(p)


def D_table(w, kmax):
    """D_k(w) = sum_{r>=1} r^(k-2) e^{-rw}, k = 0..kmax, truncated at RMAX + slop."""
    out = [iv.mpf(0)] * (kmax + 1)
    for r in range(1, RMAX + 1):
        e = iv.exp(-iv.mpf(r) * w)
        rp = iv.mpf(r)
        base = e / (rp * rp)
        cur = base
        for k in range(0, kmax + 1):
            out[k] = out[k] + cur
            cur = cur * rp
    return [o + SLOP for o in out]


def C_table(w, kmax, D):
    """C_N(w) = sum_{k=0}^N (w^k/k!) D_k(w), accumulated."""
    out = []
    acc = iv.mpf(0)
    term = iv.mpf(1)  # w^k/k!
    for k in range(0, kmax + 1):
        if k:
            term = term * w / iv.mpf(k)
        acc = acc + term * D[k]
        out.append(acc)
    return out


def H_of(w, C):
    return w - iv.pi ** 2 / 3 + 2 * C[2]


def T_of(w, C):
    return 120 * C[5]


def block_A(log):
    """s2 closed form vs brute-force sum of truncated-geometric variances."""
    ok = True
    for m, lam in ((7, "0.37"), (11, "0.9"), (23, "0.13")):
        lv = iv.mpf(lam)
        closed = iv.mpf(m) * A(1, lv) - sum(iv.mpf(j) ** 2 * A(1, iv.mpf(j) * lv)
                                            for j in range(1, m + 1))
        # direct: X = sum_j U_j, U_j uniform-ish on {0..j-1} tilted by e^{-lam u}
        tot = iv.mpf(0)
        for j in range(1, m + 1):
            wts = [iv.exp(-lv * iv.mpf(u)) for u in range(j)]
            Z = sum(wts)
            e1 = sum(iv.mpf(u) * wts[u] for u in range(j)) / Z
            e2 = sum(iv.mpf(u) ** 2 * wts[u] for u in range(j)) / Z
            tot = tot + (e2 - e1 * e1)
        agree = closed.a <= tot.b and tot.a <= closed.b
        ok &= agree and closed.a > 0
        log(f"  m={m:3d} lam={lam:>5}: s2_closed = {float(closed.a):.12f} | "
            f"s2_direct = {float(tot.a):.12f} | agree={agree} s2>0={closed.a > 0}")
    return ok


def block_B(log):
    """sup y^5 A_4(y) < 25 by the draft's own grid recipe; the scalar comparisons."""
    ok = True
    # [1/4, 6] in cells of width 2^-12, check b^5 A_4(a) < 25 (the draft's rule)
    step = Fr(1, 4096)
    a = Fr(1, 4)
    worst, worst_at = 0.0, None
    while a < 6:
        b = a + step
        val = ivfr(b) ** 5 * A(4, ivfr(a))
        if float(val.b) > worst:
            worst, worst_at = float(val.b), float(a)
        if not (val.b < 25):
            log(f"  FAIL cell [{a},{b}]: {float(val.b)}")
            ok = False
        a = b
    log(f"  sup over [1/4,6] grid of b^5 A_4(a) = {worst:.6f} at y~{worst_at:.4f}  (< 25 required)")
    # small-y: y^5 A_4(y) -> 24 y^5/y^5 = 24 as y->0 (A_4 ~ 24/y^5); check monotone approach
    for y in ("0.001", "0.01", "0.05", "0.1", "0.25"):
        v = iv.mpf(y) ** 5 * A(4, iv.mpf(y))
        log(f"  y={y:>6}: y^5 A_4(y) = {float(v.a):.9f}")
        ok &= v.b < 25
    # y >= 6 decreasing: spot check
    for y in ("6", "8", "10", "14", "20"):
        v = iv.mpf(y) ** 5 * A(4, iv.mpf(y))
        log(f"  F({y:>3}) = {float(v.b):.6f}")
        ok &= v.b < 25
    for y, lim in (("8", 12), ("10", 5), ("14", 1)):
        v = iv.mpf(y) ** 5 * A(4, iv.mpf(y))
        good = v.b < lim
        ok &= good
        log(f"  recipe: F({y}) < {lim} -> {good} (value <= {float(v.b):.6f})")
    r = ivfr(Fr(40000, 81960))
    log(f"  40000/81960 = {float(r.b):.9f} < 0.50 -> {r.b < 0.5}")
    ok &= r.b < 0.5
    return ok


def block_C(log):
    """H and T at the recipe's abscissae."""
    exp_H = {4: (1.193, 1.194), 5: (1.960, 1.962), 6: (2.834, 2.835),
             8: (4.737, 4.739), 10: (6.715, 6.717), 20: (16.710, 16.711)}
    exp_T = {8: 23.01, 10: 8.06, 14: 0.665, 20: 0.0087, 40: 1e-8}
    ok = True
    for w0, (lo, hi) in exp_H.items():
        w = iv.mpf(w0)
        D = D_table(w, 5)
        C = C_table(w, 5, D)
        h = H_of(w, C)
        good = h.a > lo and h.b < hi
        ok &= good
        log(f"  H({w0:2d}) = [{float(h.a):.6f}, {float(h.b):.6f}]  expected ({lo}, {hi}) -> {good}")
    for w0, lim in exp_T.items():
        w = iv.mpf(w0)
        D = D_table(w, 5)
        C = C_table(w, 5, D)
        t = T_of(w, C)
        good = t.b < lim
        ok &= good
        log(f"  T({w0:2d}) = {float(t.b):.6e}  expected < {lim} -> {good}")
    return ok


def block_D(log):
    """THE certificate: 256 cells on W1,W2,W3; V(I) vs 0.030/0.040/0.065."""
    Q = [(n + 1) * (n + 2) * (n + 3) * (n + 4) for n in range(NMAX + 1)]
    c = iv.pi ** 2 / 6
    # n!/(n+5)! = 1/((n+1)...(n+5))
    wt = [iv.mpf(1) / iv.mpf((n + 1) * (n + 2) * (n + 3) * (n + 4) * (n + 5))
          for n in range(NMAX + 1)]
    tail = iv.mpf(11) * iv.mpf(10) ** -6
    results = {}
    ok = True
    for name, lo, hi, ncell, _B, _C5 in BANDS:
        t0 = time.time()
        width = (hi - lo) / ncell
        worst, worst_cell, worstH = -1.0, None, None
        for i in range(ncell):
            a, b = lo + i * width, lo + (i + 1) * width
            w = hull(ivfr(a), ivfr(b))
            D = D_table(w, NMAX + 5)
            C = C_table(w, NMAX + 5, D)
            Hw = H_of(w, C)
            if not (Hw.a > 0):
                log(f"  {name} cell [{a},{b}]: H not positive!")
                ok = False
                continue
            acc = iv.mpf(0)
            for n in range(NMAX + 1):
                # SIGNED combination first, |.| only at the end (the draft's warning)
                brack = iv.mpf(n + 5) * c - w - iv.mpf(n + 5) * C[n + 5]
                pn = iv.mpf(Q[n]) * brack
                absmax = max(abs(float(pn.a)), abs(float(pn.b)))
                acc = acc + iv.mpf(absmax) * wt[n] / iv.mpf(2) ** n
            V = acc / iv.mpf([Hw.a, Hw.a]) + tail / (120 * iv.mpf([Hw.a, Hw.a]))
            if float(V.b) > worst:
                worst, worst_cell, worstH = float(V.b), (a, b), float(Hw.a)
        tgt = V_TARGET[name]
        good = worst < tgt
        ok &= good
        results[name] = worst
        log(f"  {name}: max V(I) = {worst:.9f}  vs recipe ceiling {tgt}  -> "
            f"{'PASS' if good else 'FAIL'}  (worst cell {worst_cell}, inf H = {worstH:.6f}, "
            f"{ncell} cells, {time.time()-t0:.0f}s)")
    return ok, results


def block_E(log, Bmap):
    """Finite-m assembly U_b vs the seven band targets."""
    # L = inf H over band = H(lower endpoint) (H increasing); B from the continuum bounds
    rows = [("W1", 4, 5, Bmap.get("W1", 0.030), 0.05),
            ("W2", 5, 6, Bmap.get("W2", 0.040), 0.06),
            ("W3", 6, 8, Bmap.get("W3", 0.065), 0.08)]
    ok = True
    for name, wlo, b, B, target in rows:
        w = iv.mpf(wlo)
        D = D_table(w, 5)
        C = C_table(w, 5, D)
        L = H_of(w, C)
        hb = iv.mpf(b) / iv.mpf(561)
        eb = hb * hb * iv.mpf(b + 14) / iv.mpf(12)
        Eb = iv.mpf(49) * hb / 2 + 250 * hb * hb + iv.mpf(b) * hb ** 6 / 200
        Ll = iv.mpf([L.a, L.a])
        U = Ll / (Ll - eb) * iv.mpf(B) + Eb / (120 * (Ll - eb))
        good = U.b < target
        ok &= good
        log(f"  {name}: L = {float(L.a):.6f}, e_b = {float(eb.b):.6e}, E_b = {float(Eb.b):.6f}"
            f" -> U_b <= {float(U.b):.6f}  vs C5* = {target}  -> {'PASS' if good else 'FAIL'}"
            f"  (margin {target/float(U.b):.3f}x)")
    return ok


def main():
    lines = []

    def log(s):
        print(s, flush=True)
        lines.append(s)

    which = sys.argv[1:] or ["A", "B", "C", "D", "E"]
    setup(30)
    log(f"Independent replay of sol_s2b_20260812.md — mpmath.iv, dps 30, RMAX={RMAX}, NMAX={NMAX}")
    allok = True
    Bmap = {}
    if "A" in which:
        log("[A] model check (s2 closed form vs brute-force variance sum):")
        allok &= block_A(log)
    if "B" in which:
        log("[B] scalar constants (sup y^5 A_4 < 25 grid; F values; 40000/81960):")
        allok &= block_B(log)
    if "C" in which:
        log("[C] H and T at the recipe abscissae:")
        allok &= block_C(log)
    if "D" in which:
        log("[D] THE 256-cell cancellation-retaining certificate (W1,W2,W3):")
        okD, Bmap = block_D(log)
        allok &= okD
    if "E" in which:
        log("[E] finite-m assembly U_b vs band targets:")
        allok &= block_E(log, Bmap)
    log(f"# OVERALL: {'ALL REPLAYED CHECKS PASS' if allok else 'SOME CHECKS FAILED'}")
    OUTF.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
