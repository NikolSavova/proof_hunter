"""Wave-5 hygiene batch: verification script for wave4_hygiene_20260812.md.

Blocks (each independently labeled EXACT or FLOAT):
  [A] EXACT parse of both harness results files -> coverage [4, 560], zero
      FAIL, verbatim OVERALL + last-row quotes; W-F1 support (results_m540.txt
      ends at m = 481 with NO overall line).
  [B] Record-only: state of the referee's from-scratch fresh re-run
      (referee_fresh_results_m560.txt) + byte-identity of overlapping rows.
  [C] EXACT-rational re-derivation of the SL3' R1 crossover margins:
      ratio(W) = q(W) * (1/(1+tau_start^2) - 2 gamma*) / b(W) per band
      (constants verbatim from wave4_sl3p_20260812.md section 7.2 table).
  [D] Small numeric errata checks (SL3' R5/F3, R3/F1 arithmetic, eps_t).
  [E] EXACT independent spot-check of the m560 footer varfit values:
      rebuild the exact Mahonian polynomial (same running-sum recurrence,
      copied from the twice-refereed method) through m = 560 and recompute
      the central varfit at the checkpoint m's as exact Fractions.

Usage: python3 hygiene_checks.py [--skip-e]
"""

import argparse
import os
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
CAMP = os.path.join(HERE, os.pardir)
DRAFTS = os.path.join(CAMP, os.pardir, os.pardir, "g2_campaign_20260811")

F_M540 = os.path.join(CAMP, "wave2_repairs", "results_m540.txt")
F_M560 = os.path.join(CAMP, "harness_m560", "results_m560.txt")
F_FRESH = os.path.join(DRAFTS, "referee_numerics_wave4_sliver_scripts",
                       "referee_fresh_results_m560.txt")

ROW_RE = re.compile(r"^\s*(\d+)\s+\d+\s+\d+\s+\d+\s+\S+\s+\S+\s+\S+\s+(PASS|FAIL\S*)\s*$")


def parse(path):
    """Return (rows: {m: (verdict, raw_line)}, overall_lines, fail_rows)."""
    rows, overall, fails = {}, [], []
    with open(path) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("# OVERALL"):
                overall.append(line)
            mo = ROW_RE.match(line)
            if mo:
                m = int(mo.group(1))
                rows.setdefault(m, (mo.group(2), line))
                if mo.group(2) != "PASS":
                    fails.append((m, line))
    return rows, overall, fails


def block_a():
    print("[A] EXACT parse: harness coverage 4..560 (m540 honored + m560 fresh)")
    r540, o540, f540 = parse(F_M540)
    r560, o560, f560 = parse(F_M560)
    union = dict(r540)
    union.update({m: v for m, v in r560.items() if m not in union})
    ms = sorted(union)
    gaps = [m for m in range(4, 561) if m not in union]
    print(f"  results_m540.txt: {len(r540)} data rows, m in [{min(r540)}, {max(r540)}], "
          f"FAIL rows: {len(f540)}, '# OVERALL' lines: {len(o540)}")
    print(f"  results_m560.txt: {len(r560)} data rows, m in [{min(r560)}, {max(r560)}], "
          f"FAIL rows: {len(f560)}, '# OVERALL' lines: {len(o560)}")
    print(f"  union coverage: m in [{ms[0]}, {ms[-1]}]; gaps in [4, 560]: {gaps}")
    print(f"  FAIL rows anywhere: {len(f540) + len(f560)}")
    print(f"  W-F1 support: m540 last data row m = {max(r540)} (== 481: "
          f"{max(r540) == 481}), m540 has NO overall line: {len(o540) == 0}")
    print("  m560 OVERALL line (verbatim):")
    for line in o560:
        print(f"    {line}")
    print(f"  m560 last data row (verbatim): '{r560[max(r560)][1]}'")
    ok = (not gaps and not f540 and not f560 and max(r540) == 481
          and not o540 and len(o560) == 1 and "OVERALL: PASS" in o560[0]
          and ms[0] == 4 and ms[-1] == 560)
    print(f"  BLOCK A PASS: {ok}")
    return ok, r540, r560


def block_b(r540, r560):
    print("[B] RECORD-ONLY: referee from-scratch fresh re-run state + byte-identity")
    rf, of, ff = parse(F_FRESH)
    ms = sorted(rf)
    gaps = [m for m in range(ms[0], ms[-1] + 1) if m not in rf]
    mismatch = []
    for m in ms:
        prim = r540.get(m) or r560.get(m)
        if prim is not None and prim[1] != rf[m][1]:
            mismatch.append(m)
    print(f"  fresh file: {len(rf)} data rows, m in [{ms[0]}, {ms[-1]}], gaps: {gaps}, "
          f"FAIL rows: {len(ff)}, OVERALL lines: {len(of)} (0 => still incomplete)")
    print(f"  byte-identity vs primary rows on overlap [{ms[0]}, {ms[-1]}]: "
          f"mismatches: {mismatch}")
    print(f"  BLOCK B (record-only) clean: {not ff and not gaps and not mismatch}")
    return True


# section 7.2 table of wave4_sl3p_20260812.md, verbatim (decimal strings -> exact)
SL3P_BANDS = [
    # band, gamma*, b(W), q(W), tau_start
    ("W1", "0.42", "0.002730", "0.29825", "0.4150"),
    ("W2", "0.42", "0.002735", "0.39208", "0.4200"),
    ("W3", "0.40", "0.002648", "0.47231", "0.4850"),
    ("W4", "0.40", "0.002664", "0.59214", "0.4875"),
    ("W5", "0.38", "0.002706", "0.67152", "0.5500"),
    ("W6b", "0.34", "0.003131", "0.83548", "0.6750"),
    ("W7", "0.32", "0.009844", "0.91774", "0.7275"),
]

# referee_maths_wave4_sl3p.md R1 dps-30 figures, for comparison
R1_REFEREE = {"W1": "1.4286", "W2": "1.4409", "W3": "1.7065", "W4": "1.7732",
              "W5": "1.9241", "W6b": "1.8654", "W7": "1.2971"}


def block_c():
    print("[C] EXACT-rational SL3' R1 crossover margins: "
          "ratio = q*(1/(1+tau_start^2) - 2*gamma*)/b")
    worst_band, worst = None, None
    ok = True
    for band, g, b, q, ts in SL3P_BANDS:
        g, b, q, ts = (Fraction(x) for x in (g, b, q, ts))
        ana = q * (Fraction(1, 1) / (1 + ts * ts) - 2 * g)   # analytic floor at tau_start
        ratio = ana / b                                       # certified margin over b(W)
        rf = float(ratio)
        agree = abs(rf - float(R1_REFEREE[band])) < 5e-4
        ok &= agree
        if worst is None or ratio < worst:
            worst, worst_band = ratio, band
        print(f"  {band:>3}: ana(tau_start) = {float(ana):.6f}  ratio = {rf:.4f}x "
              f"(referee dps-30: {R1_REFEREE[band]}x, agree to 5e-4: {agree})")
    print(f"  worst certified crossover margin: {float(worst):.4f}x at {worst_band} "
          f"(claim: 1.30x-class at W7): {worst_band == 'W7' and 1.29 < float(worst) < 1.31}")
    ok &= (worst_band == "W7" and 1.29 < float(worst) < 1.31)
    print(f"  BLOCK C PASS: {ok}")
    return ok


def block_d():
    import math
    print("[D] Small numeric errata (SL3' R5/F3, R3/F1 arithmetic, eps_t)")
    v = Fraction("4.04") * (Fraction(1, 4) + Fraction(1, 401))   # EXACT
    print(f"  4.04*(1/4 + 1/401) = {float(v):.6f} exactly "
          f"(= 1.020075: {v == Fraction('1.02007481296758104738154613466334') or abs(float(v)-1.020075) < 5e-7}; "
          f"<= 1.0201: {v <= Fraction('1.0201')}; draft printed '= 1.0202' -> errata '<= 1.0201')")
    eps_t = 1.0 / math.sinh(3.925) ** 2                          # FLOAT, display
    print(f"  eps_t = 1/sinh^2(3.925) = {eps_t:.6e} (nearest 1.5602e-3; "
          f"<= 1.57e-3: {eps_t <= 1.57e-3}; draft printed '= 1.5603e-3' -> '<=')")
    conc = Fraction("0.002673") - Fraction("0.001448")           # EXACT arithmetic
    print(f"  E.6.B corner: true slack 0.002673 - cell bound 0.001448 = "
          f"{float(conc):.6f} concession (~0.0012, NOT ~0.0026: "
          f"{Fraction('0.001') < conc < Fraction('0.0014')})")
    ok = (v <= Fraction("1.0201") and eps_t <= 1.57e-3
          and Fraction("0.001") < conc < Fraction("0.0014"))
    print(f"  BLOCK D PASS: {ok}")
    return ok


def next_poly(poly, d):
    """Running-sum multiply by (1 + q + ... + q^{d-1}) -- verbatim method of
    run_m560.py / run_m540.py / run_m200.py (exact ints)."""
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


# footer of results_m560.txt, verbatim 12-digit floats
FOOTER = {534: "0.997978810615", 535: "0.997982586007", 536: "0.997986347205",
          537: "0.997990094521", 540: "0.998001253256", 560: "0.998072591511"}


def block_e():
    print("[E] EXACT independent recompute of the m560 footer varfit checkpoints")
    targets = sorted(FOOTER)
    poly = [1]
    for d in range(1, 4):
        poly = next_poly(poly, d)
    ok = True
    for m in range(4, 561):
        poly = next_poly(poly, m)
        if m in FOOTER:
            N = m * (m - 1) // 2
            mid = N // 2
            r = Fraction(poly[mid] * poly[mid], poly[mid - 1] * poly[mid + 1])
            varfit = (r - 1) * Fraction(m * (m - 1) * (2 * m + 5), 72)
            got = f"{float(varfit):.12f}"
            match = (got == FOOTER[m])
            ok &= match
            print(f"  varfit({m}) exact -> {got}  footer: {FOOTER[m]}  match: {match}")
    print(f"  BLOCK E PASS: {ok}")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-e", action="store_true")
    args = ap.parse_args()
    oka, r540, r560 = block_a()
    block_b(r540, r560)
    okc = block_c()
    okd = block_d()
    oke = True if args.skip_e else block_e()
    print(f"OVERALL (blocks A/C/D{'' if args.skip_e else '/E'}): "
          f"{'PASS' if (oka and okc and okd and oke) else 'FAIL'}")
    sys.exit(0 if (oka and okc and okd and oke) else 1)


if __name__ == "__main__":
    main()
