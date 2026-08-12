"""Post-run analysis of results_m200.txt (display-level; the exact verdicts
live in run_m200.py's output itself).

Reads the table produced by run_m200.py and prints, at checkpoint m values,
the F2-prediction comparison:
    varfit          = sigma^2 (r_m - 1)            (prediction: -> 1)
    mfit            = m (1 - varfit)               (prediction: -> 27/25 = 1.08)
    second-order    m (27/25 - mfit)               (prediction: bounded, O(1);
                                                    measures the O(m^{-2}) term
                                                    in varfit = 1 - 1.08/m + c2/m^2)
Also scans the whole table for: any FAIL, max |argmin - mid|, and the largest
m where mfit decreases (monotonicity of the approach, display-level).

Usage: python3 analyze_m200.py [results_m200.txt]
"""

import sys

C_LIMIT = 27 / 25   # 1.08, display-level only

CHECKPOINTS = [40, 100, 143, 150, 151, 189, 190, 200, 266, 267, 300, 378, 379, 400]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "results_m200.txt"
    rows = {}
    n_fail = 0
    max_off = 0
    for line in open(path):
        if line.startswith("#") or line.strip().startswith("m "):
            continue
        parts = line.split()
        if len(parts) < 8 or not parts[0].isdigit():
            continue
        m, N, argmin, mid = int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])
        varfit, mfit = float(parts[5]), float(parts[6])
        verdict = parts[7]
        if verdict != "PASS":
            n_fail += 1
        if m >= 5:
            max_off = max(max_off, abs(argmin - mid))
        rows[m] = (varfit, mfit)
    print(f"rows parsed: {len(rows)}, non-PASS: {n_fail}, "
          f"max |argmin - mid| (m>=5): {max_off}")
    print(f"{'m':>4} {'varfit':>14} {'mfit=m(1-vf)':>13} {'m(1.08-mfit)':>13}")
    for m in CHECKPOINTS:
        if m in rows:
            vf, mf = rows[m]
            print(f"{m:>4} {vf:>14.10f} {mf:>13.5f} {m * (C_LIMIT - mf):>13.4f}")
    # display-level monotonicity of mfit
    ms = sorted(rows)
    dec = [m for i, m in enumerate(ms[1:], 1)
           if rows[m][1] < rows[ms[i - 1]][1] and m >= 7]
    print(f"mfit decreases (m>=7, display precision) at: {dec if dec else 'never'}")


if __name__ == "__main__":
    main()
