"""Random SHORT-interval sampler for Brenti Conj 2.11 in big Weyl groups.

Rationale (from the H3 near-counterexample, ranks 1,3,5,7,10,10,5,1, margin -1):
hairline log-concavity failures live in SHORT intervals with small rank numbers
— not in the huge near-top intervals scaled.py / scaled_general.py scan (whose
ranks are smooth and safely log-concave). In groups too big to exhaust
(A8+, B7+, D7+, E7), the short intervals are terra incognita: |W|^2-many pairs,
reachable only by sampling. This is the cheap baseline that must run BEFORE
any evolutionary search (META_GUIDE house rule 2.5).

Sample: random u (random word of random length), then a random upward cover
walk of d steps to v; score = min log-concavity ratio of rank_seq([u,v])
(exact ints). Any ratio < 1 is a counterexample and is printed immediately
with reduced words + independently re-checked.

Self-check: --selftest samples intervals in B3/D4 and compares every rank
sequence against weyl.WeylGroup (global-bitset method).

Usage:
    python3 sampler.py --selftest
    python3 sampler.py D7 --num 2000 --dmin 5 --dmax 12 --seed 1
    python3 sampler.py B6 E7 --num 500 --seed 2
"""

import argparse
import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from weyl import matmul
from scaled import min_ratio
from scaled_general import GWeyl, LeqTop, interval_levels, word_of


def random_element(G, rng, max_word):
    """Random element as a (mat, inv) pair via a random word (not uniform on W
    — fine for a baseline; spread beats uniformity here)."""
    w = G.e
    for _ in range(rng.randrange(max_word + 1)):
        g = G.gens[rng.randrange(G.n)]
        w = (matmul(w[0], g), matmul(g, w[1]))
    return w


def random_up_walk(G, u, d, rng):
    """Walk d cover-steps up from u through random covers; None if stuck at w0."""
    v = u
    lv = G.length(v[0])
    for _ in range(d):
        ups = []
        for t in G.reflections:
            vt = matmul(v[0], t)
            if G.length(vt) == lv + 1:
                ups.append((vt, matmul(t, v[1])))
        if not ups:
            return None
        v = rng.choice(ups)
        lv += 1
    return v


def sample_group(G, num, dmin, dmax, rng, log=print):
    best = None
    t0 = time.time()
    counterexamples = []
    for i in range(num):
        u = random_element(G, rng, max_word=2 * G.L // 3)
        d = rng.randrange(dmin, dmax + 1)
        v = random_up_walk(G, u, d, rng)
        if v is None:
            continue
        a = interval_levels(G, u, v, cap=2_000_000)
        if a is None or len(a) < 3:
            continue
        r, k, margin = min_ratio(a)
        if best is None or r < best["ratio"]:
            best = {"u": u, "v": v, "ratio": r, "k": k, "margin": margin,
                    "ranks": a}
            log(f"  new best: ratio={float(r):.6f} d={d} k={k} ranks={a} "
                f"[{i + 1}/{num}, {time.time() - t0:.0f}s]")
        if r < 1:
            counterexamples.append(best)
            log(f"*** RATIO < 1 in {G.name}: [u,v]=[{word_of(G, u)}, "
                f"{word_of(G, v)}] ranks={a} ***")
    if best is not None:
        best["time"] = time.time() - t0
    return best, counterexamples


def selftest():
    from weyl import WeylGroup
    rng = random.Random(0)
    for typ, n in (("B", 3), ("D", 4)):
        W = WeylGroup(typ, n)
        G = GWeyl(typ, n)
        pairs = []
        for i in range(W.N):
            m = G.ident
            minv = G.ident
            for letter in W.word[i]:
                m = matmul(m, G.gens[letter - 1])
            for letter in reversed(W.word[i]):
                minv = matmul(minv, G.gens[letter - 1])
            pairs.append((m, minv))
        idx = {p[0]: i for i, p in enumerate(pairs)}
        checked = 0
        for _ in range(300):
            u = random_element(G, rng, max_word=G.L)
            v = random_up_walk(G, u, rng.randrange(2, 7), rng)
            if v is None:
                continue
            got = interval_levels(G, u, v)
            ref = W.rank_sequence(idx[u[0]], idx[v[0]])
            assert got == ref, f"{typ}{n}: [{idx[u[0]]},{idx[v[0]]}] {got}!={ref}"
            checked += 1
        print(f"{typ}{n}: {checked} random sampled intervals match weyl.py")
    print("ALL SELFTESTS PASS")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("groups", nargs="*", help="e.g. D7 B6 E7 A9")
    ap.add_argument("--num", type=int, default=1000)
    ap.add_argument("--dmin", type=int, default=4)
    ap.add_argument("--dmax", type=int, default=12)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return

    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(outdir, exist_ok=True)
    names = [g.upper() for g in args.groups]
    out = os.path.join(outdir,
                       f"sampler_{'-'.join(names)}_seed{args.seed}_{os.getpid()}.md")
    lines = [f"# Short-interval random sampling — {' '.join(names)} "
             f"(num={args.num}, d in [{args.dmin},{args.dmax}], "
             f"seed={args.seed})\n",
             "Rationale: H3's failure has tiny ranks -> hunt short intervals "
             "exhaustion can't reach. A ratio < 1 = counterexample.\n"]
    any_ce = False
    for name in names:
        typ, n = name[0], int(name[1:])
        G = GWeyl(typ, n)
        print(f"{name}: |W|={sum(G.poincare)}, sampling {args.num} intervals...")
        best, ces = sample_group(G, args.num, args.dmin, args.dmax,
                                 random.Random(args.seed))
        if best is None:
            lines += [f"## {name}: no scorable intervals sampled", ""]
            continue
        r = float(best["ratio"])
        verdict = "**COUNTEREXAMPLE**" if ces else "all pass"
        uw, vw = word_of(G, best["u"]), word_of(G, best["v"])
        print(f"{name}: sampled min ratio {r:.6f} (margin {best['margin']}) "
              f"at [{uw or 'e'}, {vw}] — {verdict}")
        lines += [f"## {name}  ({args.num} samples, {best['time']:.0f}s)",
                  f"- verdict: **{verdict}**",
                  f"- sampled min ratio: {r:.6f} = {best['ratio']} "
                  f"(margin {best['margin']}) at k={best['k']}",
                  f"- witness: [u,v] = [{uw or 'e'}, {vw}], ranks {best['ranks']}",
                  ""]
        for ce in ces:
            any_ce = True
            lines.append(f"- **COUNTEREXAMPLE:** "
                         f"[{word_of(G, ce['u']) or 'e'}, {word_of(G, ce['v'])}] "
                         f"ranks={ce['ranks']} margin={ce['margin']}")
    with open(out, "w") as f:
        f.write("\n".join(lines))
    print(f"\nwrote {out}")
    if any_ce:
        print("\n*** COUNTEREXAMPLE FOUND — prior-art recheck (Erdosgate) + "
              "independent re-verification before celebrating. ***")


if __name__ == "__main__":
    main()
