"""Brute-force verifier for Brenti's Conjecture 2.11 (arXiv 2410.09897, Problem #13):

    For every Weyl group W and every Bruhat interval [u,v], the rank sequence
    a_k = #{z in [u,v] : l(z)-l(u) = k}  is log-concave:  a_k^2 >= a_{k-1} a_{k+1}.

A single FAIL is a counterexample to the conjecture (and is printed with reduced
words for u, v so anyone can recheck it independently).

Usage:  python3 verify.py A2 A3 A4 B2 B3 D4 G2
        python3 verify.py A5 B4 D5 F4          # bigger, minutes each

Results are appended to results/run_<groups>_<pid>.md  (new file per run —
house rule: never overwrite previous outputs).
"""

import os
import sys
import time

from weyl import WeylGroup


def check_group(W: WeylGroup):
    """Check every Bruhat interval of W. Returns (stats dict, violations list)."""
    violations = []
    n_intervals = 0
    # two near-miss trackers, each (margin, ratio, u, v, k, ranks):
    #   tight  = min absolute margin a_k^2 - a_{k-1}a_{k+1}  (equality cases)
    #   tightr = min ratio a_k^2/(a_{k-1}a_{k+1})            (true near-misses)
    tight = None
    tightr = None
    for u in range(W.N):
        upset = W.up[u]
        lu = W.length[u]
        while upset:
            lsb = upset & -upset
            v = lsb.bit_length() - 1
            upset ^= lsb
            n_intervals += 1
            if W.length[v] - lu < 2:
                continue  # d < 2: log-concavity is vacuous
            a = W.rank_sequence(u, v)
            for k in range(1, len(a) - 1):
                margin = a[k] * a[k] - a[k - 1] * a[k + 1]
                if margin < 0:
                    violations.append((u, v, k, a))
                ratio = a[k] * a[k] / (a[k - 1] * a[k + 1])
                if tight is None or margin < tight[0]:
                    tight = (margin, ratio, u, v, k, list(a))
                if tightr is None or ratio < tightr[1]:
                    tightr = (margin, ratio, u, v, k, list(a))
    return {"intervals": n_intervals, "tight": tight, "tightr": tightr}, violations


def word_str(W, i):
    return "".join(str(x) for x in W.word[i]) or "e"


def main(names):
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, f"run_{'-'.join(names)}_{os.getpid()}.md")
    lines = [f"# Bruhat log-concavity brute-force run — groups: {' '.join(names)}\n"]
    any_violation = False

    for name in names:
        typ, n = name[0].upper(), int(name[1:])
        t0 = time.time()
        W = WeylGroup(typ, n)
        t_build = time.time() - t0
        print(f"{W.name}: |W|={W.N}, maxlen={W.maxlen}, built+validated in "
              f"{t_build:.1f}s; checking all intervals...", flush=True)
        t0 = time.time()
        stats, violations = check_group(W)
        t_check = time.time() - t0
        m, r, u, v, k, a = stats["tight"]
        mr, rr, ur, vr, kr, ar = stats["tightr"]
        verdict = "VIOLATION FOUND" if violations else "all pass"
        print(f"{W.name}: {stats['intervals']} intervals checked in {t_check:.1f}s "
              f"-> {verdict}; min margin {m} (ratio {r:.4f}) at "
              f"[{word_str(W, u)}, {word_str(W, v)}] k={k} ranks={a}; "
              f"min ratio {rr:.6f} (margin {mr}) at "
              f"[{word_str(W, ur)}, {word_str(W, vr)}] k={kr} ranks={ar}", flush=True)

        lines.append(f"## {W.name}  (|W|={W.N}, {stats['intervals']} intervals, "
                     f"build {t_build:.1f}s + check {t_check:.1f}s)")
        lines.append(f"- verdict: **{verdict}**")
        lines.append(f"- min margin: {m} (ratio {r:.4f}) at interval "
                     f"[u,v]=[{word_str(W, u)}, {word_str(W, v)}], k={k}, ranks {a}")
        lines.append(f"- min ratio: {rr:.6f} (margin {mr}) at interval "
                     f"[u,v]=[{word_str(W, ur)}, {word_str(W, vr)}], k={kr}, ranks {ar}")
        for (u, v, k, a) in violations:
            any_violation = True
            lines.append(f"- **COUNTEREXAMPLE:** u={word_str(W, u)} v={word_str(W, v)} "
                         f"k={k} ranks={a}  (a_k^2={a[k]**2} < "
                         f"a_(k-1)*a_(k+1)={a[k-1]*a[k+1]})")
        lines.append("")

    with open(out, "w") as f:
        f.write("\n".join(lines))
    print(f"\nwrote {out}")
    if any_violation:
        print("\n*** COUNTEREXAMPLE FOUND — do the prior-art recheck, then "
              "independently re-verify this interval before celebrating. ***")


if __name__ == "__main__":
    main(sys.argv[1:] or ["A2", "A3", "B2", "B3", "G2"])
