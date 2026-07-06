"""Exact ground-truth harness for F2 (Mahonian log-concavity ratio).

I_m(k) = #{sigma in S_m : inv(sigma) = k} = [q^k] prod_{i=1}^m (1+q+...+q^{i-1}).
For each m: the exact min log-concavity ratio r_m = min_k I(k)^2/(I(k-1)I(k+1)),
its argmin, the central ratio, and the fit constants m^3 (r_m - 1) / 36 and
sigma^2 (r_m - 1) (sigma^2 = m(m-1)(2m+5)/72). Every claim in an F2 proof
draft must be checked against this table (exact integer arithmetic).

Usage:  python3 mahonian.py [--mmax 40] [--json]
"""

import argparse
import json
from fractions import Fraction


def mahonian(m):
    poly = [1]
    for d in range(1, m + 1):
        out = [0] * (len(poly) + d - 1)
        run = 0
        for k in range(len(out)):
            if k < len(poly):
                run += poly[k]
            if k - d >= 0:
                run -= poly[k - d]
            out[k] = run
        poly = out
    return poly


def min_ratio(a):
    best = None
    for k in range(1, len(a) - 1):
        num, den = a[k] * a[k], a[k - 1] * a[k + 1]
        if best is None or num * best[0].denominator < best[0].numerator * den:
            best = (Fraction(num, den), k)
    return best


def row(m):
    a = mahonian(m)
    N = m * (m - 1) // 2
    assert len(a) == N + 1 and a == a[::-1] and sum(a) > 0
    r, k = min_ratio(a)
    mid = N // 2
    rc = Fraction(a[mid] * a[mid], a[mid - 1] * a[mid + 1])
    var = Fraction(m * (m - 1) * (2 * m + 5), 72)
    return {
        "m": m, "N": N, "argmin_k": k, "central_k": mid,
        "min_ratio_minus_1": float(r - 1),
        "central_ratio_minus_1": float(rc - 1),
        "argmin_is_central": abs(k - Fraction(N, 2)) <= 1,
        "m3_fit": float((r - 1) * m ** 3 / 36),   # -> 1 iff r-1 ~ 36/m^3
        "var_fit": float((r - 1) * var),          # -> 1 iff r-1 ~ 1/sigma^2
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mmax", type=int, default=40)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    rows = [row(m) for m in range(4, args.mmax + 1)]
    if args.json:
        print(json.dumps(rows, indent=1))
        return
    print(f"{'m':>3} {'N':>5} {'argmin':>7} {'mid':>5} {'r-1':>12} "
          f"{'rc-1':>12} {'m3fit':>8} {'varfit':>8} {'central?':>8}")
    for r in rows:
        print(f"{r['m']:>3} {r['N']:>5} {r['argmin_k']:>7} {r['central_k']:>5} "
              f"{r['min_ratio_minus_1']:>12.3e} {r['central_ratio_minus_1']:>12.3e} "
              f"{r['m3_fit']:>8.4f} {r['var_fit']:>8.4f} "
              f"{'YES' if r['argmin_is_central'] else 'NO':>8}")


if __name__ == "__main__":
    main()
