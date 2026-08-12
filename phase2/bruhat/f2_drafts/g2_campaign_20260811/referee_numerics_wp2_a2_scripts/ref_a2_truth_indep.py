"""Referee check R4 (wp2-a2 numerics): INDEPENDENT ground-truth measurement of
m^2 |Delta_ker(k)| at m = 60 (full interior scan, K in {1,2,4}), avoiding the
package's float library entirely:

  * Mahonian rows: own implementation, exact Python ints (Gaussian-binomial
    product, plain polynomial multiplication -- different algorithm from the
    lib's running-sum version).
  * u = r(k) - 1: exact Fraction.
  * lam(k): mpmath (dps 30) Newton on mu(lam) = k, mu from the closed form
    mu = sum_j [ j g0(lam j) - g0(lam) ], g0(u) = 1/u - 1/(e^u - 1),
    residual |mu - k| checked < 1e-20.
  * v = F(0) - 1: mpmath cumulants via mp.diff of f(u) = 1/u - 1/expm1(u)
    (same route as the draft's NC-A1, but recomputed here), model polynomial
    P(y) evaluated in mpmath.

Targets (draft NC-A4 / wp2-b NC-W4(6) anchors): 1.386 / 4.070 / 5.022;
min v > 0 (draft: 1.288e-05 over its scans); measured <= C_ker2 bound at
m = 60 where the bound assembles.

Run: python3 ref_a2_truth_indep.py
"""
import os
import sys
from fractions import Fraction

import mpmath as mp

_HERE = os.path.dirname(os.path.abspath(__file__))
_WP = os.path.normpath(os.path.join(_HERE, "..", "..", "g2_scripts",
                                    "campaign_20260811", "wp2_a2"))
sys.path.insert(0, _WP)
import wp2a2_lib2 as L2      # noqa: E402

mp.mp.dps = 30


def mahonian_rows(m):
    """prod_{j=1..m} (1 + q + ... + q^{j-1}), exact ints, direct convolution."""
    poly = [1]
    for j in range(2, m + 1):
        block = [1] * j
        out = [0] * (len(poly) + j - 1)
        for i, c in enumerate(poly):
            if c:
                for l in range(j):
                    out[i + l] += c
        poly = out
    return poly


def g0(u):
    return 1 / u - 1 / mp.expm1(u)


def mu_of(m, lam):
    return mp.fsum([j * g0(lam * j) for j in range(1, m + 1)]) - m * g0(lam)


def s2_of(m, lam):
    g1 = lambda x: mp.diff(g0, x, 1)
    return -(mp.fsum([j * j * g1(lam * j) for j in range(1, m + 1)])
             - m * g1(lam))


def cumulants_mp(m, lam):
    out = []
    for r in range(2, 7):
        gr = lambda x: mp.diff(g0, x, r - 1)
        s = mp.fsum([j ** r * gr(lam * j) for j in range(1, m + 1)]) \
            - m * gr(lam)
        out.append(s * ((-1) ** (r + 1)))
    return out    # kappa_2 .. kappa_6


def He_eval(n, y):
    a, b = mp.mpf(1), y
    if n == 0:
        return a
    for k in range(1, n):
        a, b = b, y * b - k * a
    return b


def v_of(m, lam):
    k2, k3, k4, k5, k6 = cumulants_mp(m, lam)
    s2 = k2
    a = (k3 / 6) / s2 ** mp.mpf("1.5")
    b = (-k4 / 24) / s2 ** 2
    d = (k5 / 120) / s2 ** mp.mpf("2.5")
    g = (k6 / 720) / s2 ** 3

    def P(y):
        return (1 + a * He_eval(3, y) - b * He_eval(4, y) + d * He_eval(5, y)
                + (g + a * a / 2) * He_eval(6, y) - a * b * He_eval(7, y)
                + (b * b / 2 + a * d) * He_eval(8, y))
    h = 1 / mp.sqrt(s2)
    logF = 1 / s2 + 2 * mp.log(P(0)) - mp.log(P(h)) - mp.log(P(-h))
    return mp.expm1(logF), s2


def main():
    ok = True
    m = 60
    rows = mahonian_rows(m)
    # cross-check the row set: total count = m!, symmetry
    tot = sum(rows)
    fact = 1
    for j in range(2, m + 1):
        fact *= j
    sym = rows == rows[::-1]
    print("R4: independent ground truth at m = %d" % m)
    print("  rows: sum == m!: %s ; palindromic: %s ; N+1 = %d terms"
          % (tot == fact, sym, len(rows)))
    ok &= tot == fact and sym

    N = m * (m - 1) // 2
    kc = N // 2
    anchors = {1: 1.386, 2: 4.070, 4: 5.022}
    worst = {1: 0.0, 2: 0.0, 4: 0.0}
    minv = mp.mpf("inf")
    k = kc - 1 if N % 2 == 0 else kc
    while k > 0:
        # Newton in mpmath
        lam = mp.mpf("1e-6")
        for _ in range(200):
            step = (mu_of(m, lam) - k) / s2_of(m, lam)
            lam += step
            if lam <= 0:
                lam = mp.mpf("1e-15")
            if abs(step) < mp.mpf("1e-24"):
                break
        res = abs(mu_of(m, lam) - k)
        w = lam * m
        if w > 4:
            break
        if w > 0:
            assert res < mp.mpf("1e-20"), (k, float(res))
            u = Fraction(rows[k] * rows[k] - rows[k - 1] * rows[k + 1],
                         rows[k - 1] * rows[k + 1])
            v, s2 = v_of(m, lam)
            umv = mp.mpf(u.numerator) / u.denominator
            dker = s2 * (mp.log1p(umv) - mp.log1p(v))
            val = float(m * m * abs(dker))
            minv = min(minv, v)
            for K in (1, 2, 4):
                if w <= K:
                    worst[K] = max(worst[K], val)
        k -= 1

    for K in (1, 2, 4):
        r = L2.delta_ker_bound2(K, m)
        bound = r["Cker"] if r else float("inf")
        match = abs(worst[K] - anchors[K]) < 0.005
        below = worst[K] <= bound
        print("  K=%d: measured m^2|Delta_ker| = %.4f  (anchor %.3f, "
              "|diff| < 0.005: %s)  <= bound %.1f: %s"
              % (K, worst[K], anchors[K], match, bound, below))
        ok &= match and below
    print("  min v over the scan: %.4e  (> 0: %s)"
          % (float(minv), minv > 0))
    ok &= minv > 0
    print("R4 VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
