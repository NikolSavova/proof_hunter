"""Checkpointed harness extension to m = 560 (STATUS_wave3.md rec 1, wave 4).

RESUMABLE COPY of `wave2_repairs/run_m540.py` (which DIED at m = 481: all rows
PASS through 481, no OVERALL line).  Method, recurrences, and all six
certificates C1-C6 are byte-identical to run_m540.py / harness_m200's
run_m200.py; the only changes are (i) MMAX default 560, (ii) CHECKPOINTING:
each completed m is appended to the results file immediately (one line per m),
and on (re)start any prior partial results -- including wave2_repairs'
`results_m540.txt` -- are read and already-certified m are SKIPPED in the
verdict path (the exact polynomial is still rebuilt through them, since the
recurrence needs it), (iii) an exact-symmetry 2x speedup in the argmin scan
(scan k <= N/2 only, justified BY the exact C1 symmetry check a == a[::-1]
performed first each m; on C1 failure the full scan is used).

Purpose (STATUS_wave3.md):
  * closes G4's part-(c) band: [401, 536] pre-cleared exactly (crude C_A puts
    the analytic 187/216 crossover at m* = 535/537);
  * m = 560 also finitely closes the SL-sliver's harness option (b): the W1
    far sliver w in (4, ~4.51], m in [401, ~450] (~560 under the orphan's
    cruder floor) is covered by exact verification through 560.

EXACT ARITHMETIC ONLY IN THE VERDICT PATH: Mahonian coefficients are exact
integers (incremental product of [m]_q! factors via running-sum convolution),
ratios and varfit are exact Fractions; floats appear only in printed display
columns, never in any PASS/FAIL test.

Per m (4 <= m <= MMAX) it certifies, exactly:
  (C1) symmetry a_k = a_{N-k} and positivity;
  (C2) argmin_k r_m(k) = floor(N/2) for m >= 5 (scan over 1 <= k <= N-1,
       halved by exact symmetry), and at m = 4: argmin = 2 (known exception);
  (C3) min ratio == central ratio r(floor(N/2)) exactly, for m >= 5;
  (C4) N odd => exact central tie r(floor(N/2)) == r(ceil(N/2));
  (C5) varfit := sigma^2 (r_m - 1) >= 187/216, equality iff m = 6
       (sigma^2 = m(m-1)(2m+5)/72 exactly, as Fraction; m = 4 record-only);
  (C6) varfit strictly increasing on 6 <= m <= MMAX (exact Fraction compare;
       across a resume boundary, prev varfit is recomputed exactly from the
       rebuilt polynomial at the last skipped m -- never parsed from floats).

Named constants:
  VAR_NUM(m)   = m(m-1)(2m+5), VAR_DEN = 72   (sigma^2 = VAR_NUM/VAR_DEN)
  C_SHARP      = Fraction(187, 216)           (sharp lower bound, attained m=6)
  C_LIMIT_FIT  = 27/25 = 1.08                 (F2: m(1 - varfit) -> 27/25)

Usage: python3 run_m560.py [--mmax 560] [--out results_m560.txt]
                           [--prior results_m540.txt ...]
"""

import argparse
import os
import re
import time
from fractions import Fraction

C_SHARP = Fraction(187, 216)   # corrected sharp target, attained at m = 6
VAR_DEN = 72                   # sigma^2 = m(m-1)(2m+5)/72
C_LIMIT_NUM, C_LIMIT_DEN = 27, 25   # predicted limit of m(1 - varfit)

HERE = os.path.dirname(os.path.abspath(__file__))
PRIOR_DEFAULT = os.path.join(HERE, os.pardir, "wave2_repairs", "results_m540.txt")

ROW_RE = re.compile(r"^\s*(\d+)\s+\d+\s+\d+\s+\d+\s+\S+\s+\S+\s+\S+\s+PASS\s*$")


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


def min_ratio_scan(a, kmax):
    """Exact (Fraction, argmin) of r(k) = a_k^2/(a_{k-1} a_{k+1}) over
    1 <= k <= kmax, ties broken by smallest k.  Integer cross-mult only."""
    bn = bd = None
    bk = None
    for k in range(1, kmax + 1):
        num = a[k] * a[k]
        den = a[k - 1] * a[k + 1]
        if bn is None or num * bd < bn * den:
            bn, bd, bk = num, den, k
    return Fraction(bn, bd), bk


def certify(m, a, prev_varfit, log):
    N = m * (m - 1) // 2
    verdicts = []

    # C1 symmetry + positivity (exact)
    ok1 = (len(a) == N + 1) and (a == a[::-1]) and all(c > 0 for c in a)
    verdicts.append(("C1_sym_pos", ok1))

    # Argmin scan.  If C1's exact symmetry holds, r(k) = r(N-k) exactly, so
    # scanning 1 <= k <= floor(N/2) suffices and the smallest-k tie-break is
    # preserved; on (never observed) C1 failure fall back to the full scan.
    mid = N // 2
    kmax = mid if ok1 else N - 1
    r, k = min_ratio_scan(a, kmax)
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
        ok6 = (prev_varfit is not None) and varfit > prev_varfit
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


def exact_central_varfit(m, a):
    """Exact varfit at m from the CENTRAL ratio (valid as the min-ratio value
    whenever C3 held at m, which every skipped PASS row certifies)."""
    N = m * (m - 1) // 2
    mid = N // 2
    r = Fraction(a[mid] * a[mid], a[mid - 1] * a[mid + 1])
    return (r - 1) * Fraction(m * (m - 1) * (2 * m + 5), VAR_DEN)


def read_done(paths):
    """Return the set of m with a PASS row in any existing results file."""
    done = set()
    for p in paths:
        if not p or not os.path.exists(p):
            continue
        with open(p) as fh:
            for line in fh:
                mo = ROW_RE.match(line)
                if mo:
                    done.add(int(mo.group(1)))
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mmax", type=int, default=560)
    ap.add_argument("--out", type=str,
                    default=os.path.join(HERE, "results_m560.txt"))
    ap.add_argument("--prior", type=str, nargs="*", default=[PRIOR_DEFAULT])
    args = ap.parse_args()

    done = read_done(list(args.prior) + [args.out])
    resuming = os.path.exists(args.out)
    fh = open(args.out, "a")

    def log(s):
        print(s, flush=True)
        fh.write(s + "\n")
        fh.flush()

    if not resuming:
        log(f"# Exact Mahonian harness extension (checkpointed), m = 4..{args.mmax}")
        log("# Exact integer/Fraction arithmetic in every verdict; floats display-only.")
        log(f"# sigma^2 = m(m-1)(2m+5)/{VAR_DEN}; C_SHARP = 187/216 = {float(C_SHARP)!r}")
        log(f"# mfit column = m*(1 - varfit), predicted -> {C_LIMIT_NUM}/{C_LIMIT_DEN} = 1.08")
        log(f"# prior PASS rows honored (skipped here): {len(done)} "
            f"from {[os.path.relpath(p, HERE) for p in args.prior if os.path.exists(p)]}")
        log(f"{'m':>4} {'N':>6} {'argmin':>6} {'mid':>6} {'r-1':>12} "
            f"{'varfit':>12} {'mfit':>8} {'verdict':>6}")
    else:
        log(f"# --- resume {time.strftime('%Y-%m-%d %H:%M:%S')}: "
            f"{len(done)} m already certified, continuing to {args.mmax} ---")

    t0 = time.time()
    poly = [1]
    for d in range(1, 4):
        poly = next_poly(poly, d)
    prev_varfit = None
    n_fail = 0
    n_new = 0
    fail_detail = []
    special_rows = {}
    for m in range(4, args.mmax + 1):
        poly = next_poly(poly, m)
        if m in done:
            # Already certified PASS in a prior/partial run: skip the verdict
            # path, but keep prev_varfit exact for the C6 chain (recompute
            # from the rebuilt polynomial via the central ratio, valid by the
            # skipped row's own C3 PASS).
            if m >= 6 and (m + 1 not in done):
                prev_varfit = exact_central_varfit(m, poly)
            continue
        ok, varfit, fails = certify(m, poly, prev_varfit, log)
        n_new += 1
        if not ok:
            n_fail += 1
            fail_detail.append((m, fails))
        if m >= 6:
            prev_varfit = varfit
        if m in (401, 481, 482, 534, 535, 536, 537, 540, 560, args.mmax):
            special_rows[m] = varfit
    elapsed = time.time() - t0

    log("#")
    log(f"# elapsed this run: {elapsed:.1f} s; new rows: {n_new}; "
        f"prior rows honored: {len(done)}; failures (new rows): {n_fail}")
    if fail_detail:
        for m, fails in fail_detail:
            log(f"# FAIL at m={m}: {fails}")
        log("# OVERALL: FAIL")
    else:
        log("# OVERALL: PASS -- all of C1..C6 hold exactly for "
            f"4 <= m <= {args.mmax} (C2/C3 with the known m=4 exception; "
            "rows split across this file and the honored prior file(s)).")
    log("# checkpoint varfit values (exact Fraction -> 12 digits):")
    for m in sorted(special_rows):
        log(f"#   varfit({m}) = {float(special_rows[m]):.12f}")
    fh.close()


if __name__ == "__main__":
    main()
