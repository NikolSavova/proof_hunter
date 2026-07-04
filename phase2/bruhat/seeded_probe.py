"""Seeded equality-wall probe: perturb dihedral equality intervals in type B.

F3 (vetted 2026-07-04): equality a_k^2 = a_{k-1}a_{k+1} in Weyl Bruhat
intervals appears to arise ONLY from rank-2 dihedral parabolic patterns
(ranks (1,2,...,2,1), braid order >= 4). The live question for the
counterexample hunt: is that wall a hard floor, or does the log-concavity
ratio DIP BELOW 1 for intervals NEAR the equality family? (H3's failure is
exactly a small perturbed-dihedral-flavored interval, margin -1.)

Probe: in B_n, build v0 = u * s_a s_b s_a s_b (a,b = the m=4 braid pair,
letters n-1, n), requiring each step to be a length increase (so [u, v0] is
a genuine copy of the dihedral interval up to isomorphism-in-position);
then perturb: 0-3 extra random up-covers on v and/or down-covers on u.
Score every perturbed interval; report anything with ratio < 1 immediately,
and the distribution of ratios at each perturbation size.

Usage:
    python3 seeded_probe.py B7 --num 4000 --seed 3
    python3 seeded_probe.py B8 --num 2000 --seed 3 --procs 4
"""

import argparse
import multiprocessing as mp
import os
import random
import sys
import time
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scaled import min_ratio
from fast import FastWeyl, compose, length, interval_levels

_W = {}


def _init_worker(typ, n):
    _W["F"] = FastWeyl(typ, n)


def _probe(job):
    seed, pmax = job
    F = _W["F"]
    rng = random.Random(seed)
    n = F.n
    a_letter, b_letter = n - 1, n            # 1-indexed m=4 braid pair in B_n
    # random base u
    u = F.e
    for _ in range(rng.randrange(2 * F.L // 3 + 1)):
        g = F.gen_act[rng.randrange(n)]
        u = (compose(u[0], g), compose(g, u[1]))
    # ascend through the braid word; abort if any step is not an up-cover
    v = u
    lv = length(v[0])
    for letter in (a_letter, b_letter, a_letter, b_letter):
        g = F.gen_act[letter - 1]
        v2 = (compose(v[0], g), compose(g, v[1]))
        if length(v2[0]) != lv + 1:
            return None
        v, lv = v2, lv + 1
    # perturb: extra up-steps on v, down-steps on u; count APPLIED steps only
    eu, ed = rng.randrange(pmax + 1), rng.randrange(pmax + 1)
    applied = 0
    for _ in range(eu):
        ups = F.upcovers(v, lv)
        if not ups:
            return None
        v = rng.choice(ups)
        lv += 1
        applied += 1
    for _ in range(ed):
        downs = F.cocovers(u)
        if not downs:
            break
        u = rng.choice(downs)
        applied += 1
    a = interval_levels(F, u, v, cap=2_000_000)
    if a is None or len(a) < 3:
        return None
    r, k, margin = min_ratio(a)
    return (applied, r, k, margin, a, u, v)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("groups", nargs="*")
    ap.add_argument("--num", type=int, default=4000)
    ap.add_argument("--seed", type=int, default=3)
    ap.add_argument("--pertmax", type=int, default=3,
                    help="max extra up-steps and down-steps each")
    ap.add_argument("--procs", type=int, default=max(1, os.cpu_count() - 2))
    args = ap.parse_args()

    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(outdir, exist_ok=True)
    names = [g.upper() for g in args.groups]
    out = os.path.join(outdir,
                       f"seeded_{'-'.join(names)}_seed{args.seed}_{os.getpid()}.md")
    lines = [f"# Seeded equality-wall probe — {' '.join(names)} "
             f"(num={args.num}, seed={args.seed})\n",
             "Intervals CONTAINING the m=4 dihedral braid core, perturbed by "
             "0-6 extra cover steps. ratio < 1 = counterexample; "
             "ratio = 1 entries test the F3 equality characterization.\n"]
    any_ce = False
    for name in names:
        typ, n = name[0], int(name[1:])
        assert typ == "B", "B-type only (m=4 braid pair)"
        t0 = time.time()
        by_pert = defaultdict(lambda: [0, None])   # pert -> [count, min]
        equalities = []
        ces = []
        jobs = [(args.seed * 10_000_000 + i, args.pertmax)
                for i in range(args.num)]
        with mp.Pool(args.procs, initializer=_init_worker,
                     initargs=(typ, n)) as pool:
            F = FastWeyl(typ, n)   # local copy for word_of on results
            done = 0
            for res in pool.imap_unordered(_probe, jobs, chunksize=8):
                done += 1
                if done % 500 == 0:
                    print(f"  ... {done}/{args.num} [{time.time() - t0:.0f}s]",
                          flush=True)
                if res is None:
                    continue
                pert, r, k, margin, a, u, v = res
                slot = by_pert[pert]
                slot[0] += 1
                if slot[1] is None or r < slot[1][0]:
                    slot[1] = (r, k, margin, a, u, v)
                if r < 1:
                    ces.append(res)
                    print(f"*** RATIO < 1 in {name}: pert={pert} ranks={a} "
                          f"[{F.word_of(u) or 'e'}, {F.word_of(v)}] ***",
                          flush=True)
                elif r == 1 and pert > 0:
                    equalities.append(res)
        verdict = "**COUNTEREXAMPLE**" if ces else "all pass"
        print(f"{name}: {verdict} [{time.time() - t0:.0f}s]", flush=True)
        lines.append(f"## {name}  ({args.num} probes, {time.time() - t0:.0f}s) "
                     f"— **{verdict}**")
        for pert in sorted(by_pert):
            cnt, best = by_pert[pert]
            r, k, margin, a, u, v = best
            line = (f"- pert={pert}: {cnt} intervals, min ratio "
                    f"{float(r):.6f} (margin {margin}) ranks {a}")
            print(line, flush=True)
            lines.append(line)
        if equalities:
            lines.append(f"- NOTE: {len(equalities)} PERTURBED intervals with "
                         f"ratio exactly 1 — check against F3 (are these "
                         f"still pure dihedral patterns?):")
            for pert, r, k, margin, a, u, v in equalities[:10]:
                lines.append(f"    - pert={pert} ranks={a} "
                             f"[{F.word_of(u) or 'e'}, {F.word_of(v)}]")
        for res in ces:
            any_ce = True
            pert, r, k, margin, a, u, v = res
            lines.append(f"- **COUNTEREXAMPLE:** pert={pert} ranks={a} "
                         f"margin={margin} [{F.word_of(u) or 'e'}, "
                         f"{F.word_of(v)}]")
        lines.append("")
    with open(out, "w") as f:
        f.write("\n".join(lines))
    print(f"\nwrote {out}")
    if any_ce:
        print("\n*** COUNTEREXAMPLE — prior-art recheck + independent "
              "re-verification (scaled_general.py) first. ***")


if __name__ == "__main__":
    main()
