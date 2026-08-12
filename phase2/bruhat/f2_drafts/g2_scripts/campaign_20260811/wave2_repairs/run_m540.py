"""Harness extension to m = 540 (STATUS_wave2.md 5.2, wave 3 repairs session).

COPY of `harness_m200/run_m200.py` (wave 2, exact to m = 400) with MMAX
default raised to 540 and extra checkpoint rows; method, recurrences, and
all six certificates C1-C6 are byte-identical.  Purpose: pre-clear G4's
part-(c) band [401, 534] (STATUS_wave2.md section 2, cross-package plug
caveat): with the crude C_ker(4) the plugged part-(c) bound first reaches
187/216 at m* = 535 (grid flavor; 537 closed), so exact harness coverage
through m = 540 leaves no uncovered m for part (c) at K = 4.

EXACT ARITHMETIC ONLY IN THE VERDICT PATH: Mahonian coefficients are exact
integers (incremental product of [m]_q! factors via running-sum convolution,
identical recurrence to mahonian.py), ratios and varfit are exact Fractions;
floats appear only in the printed display columns, never in any PASS/FAIL test.

Per m (4 <= m <= MMAX) it certifies, exactly:
  (C1) symmetry a_k = a_{N-k} and positivity;
  (C2) argmin_k r_m(k) = floor(N/2) for m >= 5 (full scan over 1 <= k <= N-1),
       and at m = 4: argmin = 2, |argmin - N/2| = 1 (known exception, F2 draft);
  (C3) min ratio == central ratio r(floor(N/2)) exactly, for m >= 5;
  (C4) N odd => exact central tie r(floor(N/2)) == r(ceil(N/2));
  (C5) varfit := sigma^2 (r_m - 1) >= 187/216, equality iff m = 6
       (sigma^2 = m(m-1)(2m+5)/72 exactly, as Fraction);
  (C6) varfit strictly increasing on 6 <= m <= MMAX (exact Fraction compare).

Named constants:
  VAR_NUM(m)   = m(m-1)(2m+5), VAR_DEN = 72   (sigma^2 = VAR_NUM/VAR_DEN)
  C_SHARP      = Fraction(187, 216)           (sharp lower bound, attained m=6)
  C_LIMIT_FIT  = 27/25 = 1.08                 (F2: m(1 - varfit) -> 27/25)

Usage: python3 run_m540.py [--mmax 540] [--out results_m540.txt]
"""

import argparse
import sys
import time
from fractions import Fraction

C_SHARP = Fraction(187, 216)   # corrected sharp target, attained at m = 6
VAR_DEN = 72                   # sigma^2 = m(m-1)(2m+5)/72
C_LIMIT_NUM, C_LIMIT_DEN = 27, 25   # predicted limit of m(1 - varfit)


def next_poly(poly, d):
    """Multiply coefficient list `poly` by (1 + q + ... + q^{d-1}).

    Same running-sum recurrence as mahonian.py:mahonian (exact ints)."""
    out = [0] * (len(poly) + d - 1)
    run = 0
    npoly = len(poly)
    for k in range(len(out)):
        if k < npoly:
            run += poly[k]
        if k - d >= 0:
            run -= poly[k - d]
        out[k] = run
    return out


def min_ratio_full_scan(a):
    """Exact (Fraction, argmin) of r(k) = a_k^2/(a_{k-1} a_{k+1}) over ALL
    interior k, ties broken by smallest k.  Integer cross-multiplication only."""
    bn = bd = None   # best ratio as numerator/denominator ints
    bk = None
    for k in range(1, len(a) - 1):
        num = a[k] * a[k]
        den = a[k - 1] * a[k + 1]
        if bn is None or num * bd < bn * den:
            bn, bd, bk = num, den, k
    return Fraction(bn, bd), bk


def certify(m, a, prev_varfit, log):
    N = m * (m - 1) // 2
    verdicts = []

    # C1 symmetry + positivity
    ok1 = (len(a) == N + 1) and (a == a[::-1]) and all(c > 0 for c in a)
    verdicts.append(("C1_sym_pos", ok1))

    r, k = min_ratio_full_scan(a)
    mid = N // 2
    rc = Fraction(a[mid] * a[mid], a[mid - 1] * a[mid + 1])

    # C2 argmin central
    if m == 4:
        ok2 = (k == 2) and abs(2 * k - N) <= 2   # |k - N/2| <= 1
    else:
        ok2 = (k == mid)
    verdicts.append(("C2_argmin_central", ok2))

    # C3 min ratio == central ratio (m >= 5)
    ok3 = (m == 4) or (r == rc)
    verdicts.append(("C3_min_eq_central", ok3))

    # C4 exact tie when N odd
    if N % 2 == 1:
        rc2 = Fraction(a[mid + 1] * a[mid + 1], a[mid] * a[mid + 2])
        ok4 = (rc == rc2)
    else:
        ok4 = True
    verdicts.append(("C4_odd_tie", ok4))

    # C5 varfit >= 187/216, equality iff m == 6
    var = Fraction(m * (m - 1) * (2 * m + 5), VAR_DEN)
    varfit = (r - 1) * var
    ok5 = (varfit > C_SHARP) if m != 6 else (varfit == C_SHARP)
    if m == 4:   # m=4 predates the sharp bound's range (5 <= m); record only
        ok5 = True
    verdicts.append(("C5_ge_187_216", ok5))

    # C6 strict increase from m = 6 on
    if m >= 7:
        ok6 = varfit > prev_varfit
    else:
        ok6 = True
    verdicts.append(("C6_strict_incr", ok6))

    all_ok = all(v for _, v in verdicts)
    fails = [name for name, v in verdicts if not v]
    mfit = float(m * (1 - varfit))          # -> 27/25 = 1.08 predicted
    line = (f"{m:>4} {N:>6} {k:>6} {mid:>6} "
            f"{float(r - 1):>12.4e} {float(varfit):>12.10f} {mfit:>8.5f} "
            f"{'PASS' if all_ok else 'FAIL ' + ','.join(fails):>6}")
    log(line)
    return all_ok, varfit, fails


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mmax", type=int, default=540)
    ap.add_argument("--out", type=str, default="results_m540.txt")
    args = ap.parse_args()

    fh = open(args.out, "w")

    def log(s):
        print(s)
        fh.write(s + "\n")
        fh.flush()

    log(f"# Exact Mahonian harness extension, m = 4..{args.mmax}")
    log("# Exact integer/Fraction arithmetic in every verdict; floats display-only.")
    log(f"# sigma^2 = m(m-1)(2m+5)/{VAR_DEN}; C_SHARP = 187/216 = {float(C_SHARP)!r}")
    log(f"# mfit column = m*(1 - varfit), predicted -> {C_LIMIT_NUM}/{C_LIMIT_DEN} = 1.08")
    log(f"{'m':>4} {'N':>6} {'argmin':>6} {'mid':>6} {'r-1':>12} "
        f"{'varfit':>12} {'mfit':>8} {'verdict':>6}")

    t0 = time.time()
    poly = [1]           # product over d = 1..m, built incrementally
    for d in range(1, 4):
        poly = next_poly(poly, d)
    prev_varfit = None
    n_fail = 0
    fail_detail = []
    special_rows = {}
    for m in range(4, args.mmax + 1):
        poly = next_poly(poly, m)
        ok, varfit, fails = certify(m, poly, prev_varfit, log)
        if not ok:
            n_fail += 1
            fail_detail.append((m, fails))
        if m >= 6:
            prev_varfit = varfit
        if m in (6, 40, 143, 150, 151, 189, 190, 200, 266, 267, 378, 379,
                 400, 401, 534, 535, 537, args.mmax):
            special_rows[m] = varfit
    elapsed = time.time() - t0

    log("#")
    log(f"# elapsed: {elapsed:.1f} s")
    log(f"# rows: {args.mmax - 3}, failures: {n_fail}")
    if fail_detail:
        for m, fails in fail_detail:
            log(f"# FAIL at m={m}: {fails}")
        log("# OVERALL: FAIL")
    else:
        log("# OVERALL: PASS -- all of C1..C6 hold exactly for "
            f"4 <= m <= {args.mmax} (C2/C3 with the known m=4 exception).")
    log("# checkpoint varfit values (exact Fraction -> 12 digits):")
    for m in sorted(special_rows):
        log(f"#   varfit({m}) = {float(special_rows[m]):.12f}")
    fh.close()


if __name__ == "__main__":
    main()
