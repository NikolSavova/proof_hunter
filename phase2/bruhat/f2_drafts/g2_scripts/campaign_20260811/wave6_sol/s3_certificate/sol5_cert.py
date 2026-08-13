#!/usr/bin/env python3
"""(SOL.5) certificate — |h_n^(8)(x)| <= H_8 := 10^12 on (0, 40], n = 2, 3, 4.

This is the second item of referee_numerics_sol_s3.md finding F1 (the draft asserts
(SOL.5) with an unrun "exact rational interval" certification). s3_cert.py CONSUMES
(SOL.5) in its remainder radius, so certifying it here removes that conditionality.

h_n(x) = x^n sum_{k>=1} k^(n-1) e^(-kx) is EVEN and analytic on C minus {2 pi i k, k != 0}
(nearest singularity to the real axis: distance 2 pi). Equivalent closed forms used here:

    s(y) = sinh(y)/y ;  h_2 = 1/s(x/2)^2 ,  h_3 = 2 cosh(x/2)/s(x/2)^3 ,
    h_4 = (2 cosh(x) + 4)/s(x/2)^4
  i.e.  h_2 = z^2/(4 sinh^2(z/2)),  h_3 = z^3 cosh(z/2)/(4 sinh^3(z/2)),
        h_4 = z^4 (2 cosh z + 4)/(16 sinh^4(z/2)).

TWO REGIMES (the direct series is useless near 0 — its Leibniz terms diverge like
x^-8 while h_n stays smooth, so the small-x range needs an analytic estimate):

  PART A, x in [0, 1] — Cauchy coefficient bound.
    h_n(x) = sum_{m>=0} c_{n,m} x^(2m) with |c_{n,m}| <= M_n(R)/R^(2m), R = 6 < 2 pi,
    M_n(R) = max_{|z|=R} |h_n(z)|. Differentiating 8 times and using |x| <= 1,
        |h_n^(8)(x)| <= M_n(6) * SUM8,   SUM8 := sum_{m>=4} [(2m)!/(2m-8)!] / 6^(2m).
    M_n(6) is enclosed by complex interval arithmetic over arcs of the circle
    (implemented below over mpmath.iv real intervals; the boxes outer-bound the arcs).

  PART B, x in [1, 40] — direct series.
    h_n^(8) = sum_{j=0}^{min(8,n)} C(8,j) (n!/(n-j)!) x^(n-j) phi_n^(8-j)(x),
    phi_n^(r)(x) = (-1)^r sum_k k^(n-1+r) e^(-kx); bound term-wise in absolute value
    (massively lossy — the true cancellation is ~8 orders — but 10^12 is loose enough).
    Tail k > K: for K >= 2p/x consecutive terms decay by <= e^(-x/2), so
        sum_{k>K} k^p e^(-kx) <= K^p e^(-Kx)/(1 - e^(-x/2)).

Both parts are outer bounds under directed rounding, so a PASS is rigorous.
"""
import math
from fractions import Fraction as Fr
from pathlib import Path

from mpmath import iv

HERE = Path(__file__).resolve().parent
OUTF = HERE / "out_sol5_certificate.txt"
H8 = iv.mpf(10) ** 12
FACT = [1, 1, 2, 6, 24]


def ivfr(fr):
    return iv.mpf(fr.numerator) / iv.mpf(fr.denominator)


def hull(x, y):
    x, y = iv.mpf(x), iv.mpf(y)
    return iv.mpf([min(x.a, y.a), max(x.b, y.b)])


# ---------- complex interval arithmetic over real intervals ----------
class C:
    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re, self.im = iv.mpf(re), iv.mpf(im)

    def __add__(s, o):
        return C(s.re + o.re, s.im + o.im)

    def __sub__(s, o):
        return C(s.re - o.re, s.im - o.im)

    def __mul__(s, o):
        return C(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)

    def __truediv__(s, o):
        d = o.re * o.re + o.im * o.im
        return C((s.re * o.re + s.im * o.im) / d, (s.im * o.re - s.re * o.im) / d)

    def abs2(s):
        return s.re * s.re + s.im * s.im

    def __repr__(s):
        return f"({s.re} + {s.im}i)"


def csinh(w):
    """sinh(u+iv) = sinh u cos v + i cosh u sin v."""
    eu, emu = iv.exp(w.re), iv.exp(-w.re)
    return C((eu - emu) / 2 * iv.cos(w.im), (eu + emu) / 2 * iv.sin(w.im))


def ccosh(w):
    """cosh(u+iv) = cosh u cos v + i sinh u sin v."""
    eu, emu = iv.exp(w.re), iv.exp(-w.re)
    return C((eu + emu) / 2 * iv.cos(w.im), (eu - emu) / 2 * iv.sin(w.im))


def h_complex(n, z):
    half = C(z.re / 2, z.im / 2)
    sh = csinh(half)
    if n == 2:
        return (z * z) / (C(4) * sh * sh)
    if n == 3:
        return (z * z * z) * ccosh(half) / (C(4) * sh * sh * sh)
    num = (z * z * z * z) * (C(2) * ccosh(z) + C(4))
    return num / (C(16) * sh * sh * sh * sh)


def M_on_circle(n, R, N, log):
    """Rigorous upper bound for max_{|z|=R} |h_n(z)| via N arc-boxes."""
    two_pi = 2 * iv.pi
    worst = iv.mpf(0)
    worst_at = None
    for i in range(N):
        th = hull(two_pi * iv.mpf(i) / iv.mpf(N), two_pi * iv.mpf(i + 1) / iv.mpf(N))
        z = C(iv.mpf(R) * iv.cos(th), iv.mpf(R) * iv.sin(th))
        a2 = h_complex(n, z).abs2()
        if a2.b > worst.b:
            worst = iv.mpf([a2.b, a2.b])
            worst_at = float(2 * math.pi * (i + 0.5) / N)
    M = iv.sqrt(worst)
    log(f"  M_{n}({R}) <= {float(M.b):.6g}   (worst arc near theta = {worst_at:.4f})")
    return iv.mpf([M.b, M.b])


def sum8(R=6, mmax=40):
    """SUM8 = sum_{m>=4} [(2m)!/(2m-8)!]/R^(2m), finite part + geometric tail."""
    tot = iv.mpf(0)
    for m in range(4, mmax + 1):
        c = 1
        for t in range(2 * m - 7, 2 * m + 1):
            c *= t
        tot += iv.mpf(c) / iv.mpf(R) ** (2 * m)
    # tail m > mmax: term ratio <= ((2m+2)/(2m-8))^... bounded crudely by 2/R^2 < 1/9
    last = iv.mpf(1)
    c = 1
    for t in range(2 * mmax - 7, 2 * mmax + 1):
        c *= t
    last = iv.mpf(c) / iv.mpf(R) ** (2 * mmax)
    tot += last * iv.mpf(2) / iv.mpf(R) ** 2 / (1 - iv.mpf(2) / iv.mpf(R) ** 2)
    return iv.mpf([tot.b, tot.b])


def part_A(log):
    """x in [0,1] via Cauchy coefficient bounds on |z| = 6."""
    S8 = sum8()
    log(f"  SUM8 = sum_(m>=4) (2m)!/((2m-8)! 6^(2m)) <= {float(S8.b):.6g}")
    ok = True
    for n in (2, 3, 4):
        M = M_on_circle(n, 6, 4000, log)
        bound = M * S8
        bd = float(bound.b)
        good = bd < 1e12
        ok &= good
        log(f"  n={n}: sup_[0,1] |h_n^(8)| <= {bd:.6g}  vs H_8 = 1e12  "
            f"-> {'PASS' if good else 'FAIL'}  (margin {1e12 / bd:.3g}x)")
    return ok


def phi_abs_bound(n, r, xlo, xhi, K=400):
    """Upper bound for sum_k k^(n-1+r) e^(-kx) over x in [xlo, xhi] (uses x = xlo)."""
    p = n - 1 + r
    x = iv.mpf(xlo)  # smallest x -> largest sum
    tot = iv.mpf(0)
    for k in range(1, K + 1):
        tot += iv.mpf(k) ** p * iv.exp(-iv.mpf(k) * x)
    assert K >= 2 * p / xlo, f"tail geometric hypothesis needs K >= {2 * p / xlo}"
    tail = iv.mpf(K) ** p * iv.exp(-iv.mpf(K) * x) / (1 - iv.exp(-x / 2))
    return iv.mpf([(tot + tail).b, (tot + tail).b])


def part_B(log):
    """x in [1,40] via the direct Leibniz series, bounded term-wise in absolute value."""
    edges = [Fr(1), Fr(2), Fr(4), Fr(8), Fr(16), Fr(40)]
    ok = True
    for n in (2, 3, 4):
        worst = 0.0
        for a, b in zip(edges, edges[1:]):
            acc = iv.mpf(0)
            for j in range(0, min(8, n) + 1):
                c = math.comb(8, j) * (FACT[n] // FACT[n - j])
                xpow = ivfr(b) ** (n - j)  # x^(n-j) increasing
                acc += iv.mpf(c) * xpow * phi_abs_bound(n, 8 - j, float(a), float(b))
            worst = max(worst, float(acc.b))
            good = float(acc.b) < 1e12
            ok &= good
            if not good:
                log(f"  n={n} x in [{a},{b}]: FAIL bound {float(acc.b):.6g}")
        log(f"  n={n}: sup_[1,40] |h_n^(8)| <= {worst:.6g}  vs H_8 = 1e12  "
            f"-> {'PASS' if worst < 1e12 else 'FAIL'}  (margin {1e12 / worst:.3g}x)")
    return ok


def main():
    lines = []

    def log(s):
        print(s, flush=True)
        lines.append(s)

    iv.dps = 30
    log("(SOL.5) certificate: |h_n^(8)(x)| <= 10^12 on (0,40], n = 2,3,4")
    log("PART A — x in [0,1], Cauchy coefficient bound on |z| = 6 (4000 arcs):")
    a = part_A(log)
    log("PART B — x in [1,40], direct Leibniz series, term-wise absolute bound:")
    b = part_B(log)
    verdict = "PASS — (SOL.5) CERTIFIED on (0,40]" if (a and b) else "FAIL"
    log(f"# OVERALL: {verdict}")
    OUTF.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
