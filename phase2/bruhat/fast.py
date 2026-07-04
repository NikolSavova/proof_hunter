"""Root-action fast engine — same algorithms as scaled_general.py, ~30-50x faster.

An element w is stored as its SIGNED ACTION ON POSITIVE ROOTS: a tuple act of
length P where act[i] = j means w(alpha_i) = +alpha_j and act[i] = ~j means
w(alpha_i) = -alpha_j (bitwise-complement encoding, an involution). Then:

    compose(a, b)[i] = a[b[i]] if b[i]>=0 else ~a[~b[i]]     O(P)
    length(w)        = #{i : act[i] < 0}                      O(P)
    left descent i   = inv_act[simple_idx[i]] < 0             O(1)
    cocovers         loop only over inversions of w           O(#inv * P)

vs O(n^3) matmuls + O(P n^2) length in scaled_general — the hot loop drops
from ~1e5 to ~2e3 ops. Construction converts scaled_general.GWeyl's validated
matrices, but AFTER construction no matrix code is used, so scaled_general is
an independent oracle for the selftest.

Selftest: FastWeyl vs GWeyl on B3/D4 (lengths, all lower + sampled general
intervals), vs scaled.py's permutation engine on A5, known minima (D5, D6,
B4 equality). Heartbeat logging + --procs multiprocessing for sweeps.

Usage:
    python3 fast.py --selftest
    python3 fast.py --scan D7 D8 --cogap 3 --procs 6
    python3 fast.py --sample B7 E7 --num 20000 --dmin 4 --dmax 12 --procs 6
"""

import argparse
import multiprocessing as mp
import os
import random
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from weyl import apply
from scaled import min_ratio
import scaled_general as sg


def compose(a, b):
    return tuple(a[x] if x >= 0 else ~a[~x] for x in b)


def length(act):
    return sum(1 for x in act if x < 0)


class FastWeyl:
    def __init__(self, typ, n):
        G = sg.GWeyl(typ, n)
        self.typ, self.n, self.name = typ, n, G.name
        self.P, self.L = G.P, G.L
        self.poincare = G.poincare
        pos_idx = {r: i for i, r in enumerate(G.pos)}
        self.simple_idx = [pos_idx[s] for s in G.simple]

        def act_of(mat):
            out = []
            for r in G.pos:
                v = apply(mat, r)
                out.append(pos_idx[v] if sum(v) > 0
                           else ~pos_idx[tuple(-c for c in v)])
            return tuple(out)

        self.gen_act = [act_of(g) for g in G.gens]
        ident = tuple(range(self.P))
        self.e = (ident, ident)
        self.w0 = (act_of(G.w0[0]), act_of(G.w0[1]))
        # reflections with their root index (t_alpha inverts alpha)
        self.refl = []
        for t in G.reflections:
            a = act_of(t)
            roots = [i for i in range(self.P) if a[i] == ~i]
            assert len(roots) >= 1 and compose(a, a) == ident
            self.refl.append((a, min(roots)))
        assert len(self.refl) == self.P
        assert length(self.w0[0]) == self.L
        self._G = G  # kept only for word_of / debugging

    # element = (act, inv_act)
    def rmul_refl(self, w, t_act):
        return (compose(w[0], t_act), compose(t_act, w[1]))

    def lmul_gen(self, i, w):
        g = self.gen_act[i]
        return (compose(g, w[0]), compose(w[1], g))

    def left_descent(self, w, i):
        return w[1][self.simple_idx[i]] < 0

    def rmul_w0(self, w):
        return (compose(w[0], self.w0[0]), compose(self.w0[1], w[1]))

    def cocovers(self, w, lw=None):
        if lw is None:
            lw = length(w[0])
        act = w[0]
        out = []
        for t_act, r in self.refl:
            if act[r] >= 0:      # alpha_r not an inversion -> length goes up
                continue
            u = compose(act, t_act)
            if length(u) == lw - 1:
                out.append((u, compose(t_act, w[1])))
        return out

    def upcovers(self, w, lw=None):
        if lw is None:
            lw = length(w[0])
        act = w[0]
        out = []
        for t_act, r in self.refl:
            if act[r] < 0:
                continue
            u = compose(act, t_act)
            if length(u) == lw + 1:
                out.append((u, compose(t_act, w[1])))
        return out

    def word_of(self, w):
        # stripping left descents s_a, s_b, ... gives w = s_a s_b ... s_z,
        # i.e. the word IS the strip order (right-multiplication convention)
        out = []
        cur = w
        l = length(w[0])
        while l > 0:
            for i in range(self.n):
                if self.left_descent(cur, i):
                    cur = self.lmul_gen(i, cur)
                    out.append(i + 1)
                    l -= 1
                    break
        chk = self.e
        for letter in out:
            chk = (compose(chk[0], self.gen_act[letter - 1]),
                   compose(self.gen_act[letter - 1], chk[1]))
        assert chk[0] == w[0], "word roundtrip"
        return "".join(str(x) for x in out)


class LeqTop:
    """z <= v via the lifting property along v's left-descent chain (same
    algorithm as scaled_general.LeqTop, root-action ops)."""

    def __init__(self, F, v):
        self.F = F
        self.desc = []
        cur, l = v, length(v[0])
        while l > 0:
            for i in range(F.n):
                if F.left_descent(cur, i):
                    cur = F.lmul_gen(i, cur)
                    self.desc.append(i)
                    l -= 1
                    break
            else:
                raise AssertionError("no descent")
        self.desc.reverse()  # desc[k-1]: strip to go from length k to k-1
        self.lv = len(self.desc)
        self.memo = {}

    def leq(self, z, lz=None):
        if lz is None:
            lz = length(z[0])
        return self._leq(z, lz, self.lv)

    def _leq(self, z, lz, k):
        if lz > k:
            return False
        if lz == 0:
            return True
        key = (z[0], k)
        hit = self.memo.get(key)
        if hit is not None:
            return hit
        s = self.desc[k - 1]
        if self.F.left_descent(z, s):
            res = self._leq(self.F.lmul_gen(s, z), lz - 1, k - 1)
        else:
            res = self._leq(z, lz, k - 1)
        self.memo[key] = res
        return res


def complement_levels(F, v, cap=None):
    lv = length(v[0])
    if lv == F.L:
        return {}
    top = LeqTop(F, v)
    seen = {F.w0[0]}
    levels = {F.L: 1}
    frontier = [F.w0]
    l = F.L
    while frontier:
        l -= 1
        nxt = []
        for z in frontier:
            for u in F.cocovers(z, l + 1):
                if u[0] in seen:
                    continue
                if top.leq(u, l):
                    continue
                seen.add(u[0])
                nxt.append(u)
        if nxt:
            levels[l] = len(nxt)
        if cap is not None and len(seen) > cap:
            return None
        frontier = nxt
    return levels


def rank_seq_lower(F, v, cap=None):
    lv = length(v[0])
    comp = complement_levels(F, v, cap=cap)
    if comp is None:
        return None
    for l in range(lv + 1, F.L + 1):
        assert comp.get(l, 0) == F.poincare[l], "complement above ell(v)"
    a = [F.poincare[l] - comp.get(l, 0) for l in range(lv + 1)]
    assert a[0] == 1 and a[lv] == 1 and all(x > 0 for x in a), a
    return a


def interval_levels(F, u, v, cap=None):
    lu, lv = length(u[0]), length(v[0])
    top = LeqTop(F, F.rmul_w0(u))       # z >= u  <=>  z*w0 <= u*w0
    if not top.leq(F.rmul_w0(v), F.L - lv):
        return None
    seen = {v[0]}
    levels = {lv: 1}
    frontier = [v]
    l = lv
    while frontier and l > lu:
        l -= 1
        nxt = []
        for z in frontier:
            for w in F.cocovers(z, l + 1):
                if w[0] in seen:
                    continue
                if not top.leq(F.rmul_w0(w), F.L - l):
                    continue
                seen.add(w[0])
                nxt.append(w)
        if nxt:
            levels[l] = len(nxt)
        if cap is not None and len(seen) > cap:
            return None
        frontier = nxt
    a = [levels.get(x, 0) for x in range(lu, lv + 1)]
    assert a[0] == 1 and a[-1] == 1 and all(x > 0 for x in a), (a, lu, lv)
    return a


def slab(F, cogap):
    seen = {F.w0[0]: F.w0}
    frontier = [F.w0]
    l = F.L
    for _ in range(cogap):
        nxt = []
        for z in frontier:
            for u in F.cocovers(z, l):
                if u[0] not in seen:
                    seen[u[0]] = u
                    nxt.append(u)
        frontier = nxt
        l -= 1
    return list(seen.values())


# ------------------------------------------------------------ worker plumbing

_W = {}


def _init_worker(typ, n):
    _W["F"] = FastWeyl(typ, n)


def _eval_candidate(v):
    F = _W["F"]
    a = rank_seq_lower(F, v, cap=5_000_000)
    if a is None or len(a) < 3:
        return None
    r, k, margin = min_ratio(a)
    return (r, k, margin, a, v)


def _eval_sample(job):
    seed, dmin, dmax, max_word = job
    F = _W["F"]
    rng = random.Random(seed)
    w = F.e
    for _ in range(rng.randrange(max_word + 1)):
        i = rng.randrange(F.n)
        g = F.gen_act[i]
        w = (compose(w[0], g), compose(g, w[1]))
    v = w
    for _ in range(rng.randrange(dmin, dmax + 1)):
        ups = F.upcovers(v)
        if not ups:
            return None
        v = rng.choice(ups)
    a = interval_levels(F, w, v, cap=2_000_000)
    if a is None or len(a) < 3:
        return None
    r, k, margin = min_ratio(a)
    return (r, k, margin, a, w, v)


def run_pool(procs, typ, n, fn, jobs, progress_every, log, on_result):
    t0 = time.time()
    if procs <= 1:
        _init_worker(typ, n)
        for i, job in enumerate(jobs):
            on_result(fn(job))
            if (i + 1) % progress_every == 0:
                log(f"  ... {i + 1}/{len(jobs)} [{time.time() - t0:.0f}s]")
    else:
        with mp.Pool(procs, initializer=_init_worker,
                     initargs=(typ, n)) as pool:
            for i, res in enumerate(pool.imap_unordered(fn, jobs, chunksize=1)):
                on_result(res)
                if (i + 1) % progress_every == 0:
                    log(f"  ... {i + 1}/{len(jobs)} [{time.time() - t0:.0f}s]")


# ------------------------------------------------------------------ selftest

def selftest():
    from weyl import WeylGroup, matmul
    import scaled as typeA

    for typ, n in (("B", 3), ("D", 4)):
        W = WeylGroup(typ, n)
        F = FastWeyl(typ, n)
        G = F._G
        pairs = []
        for i in range(W.N):
            w = F.e
            for letter in W.word[i]:
                g = F.gen_act[letter - 1]
                w = (compose(w[0], g), compose(g, w[1]))
            assert length(w[0]) == W.length[i]
            pairs.append(w)
        for i in range(W.N):
            ref = W.rank_sequence(0, i)
            assert rank_seq_lower(F, pairs[i]) == ref, f"{typ}{n} lower {i}"
            wd = F.word_of(pairs[i])   # self-asserting roundtrip
            assert len(wd) >= W.length[i]  # >=: letters can be multi-digit
        rng = random.Random(0)
        checked = 0
        for _ in range(400):
            i, j = rng.randrange(W.N), rng.randrange(W.N)
            ref = W.rank_sequence(j, i)
            got = interval_levels(F, pairs[j], pairs[i])
            assert got == ref, f"{typ}{n} [{j},{i}]"
            checked += 1
        print(f"{typ}{n}: all {W.N} lower + {checked} random general "
              f"intervals match weyl.py")

    F = FastWeyl("A", 5)
    W = __import__("weyl").WeylGroup("A", 5)
    pA = typeA.poincare_A(5)
    for i in range(W.N):
        w = F.e
        for letter in W.word[i]:
            g = F.gen_act[letter - 1]
            w = (compose(w[0], g), compose(g, w[1]))
        vperm = typeA.perm_from_word(W.word[i], 6)
        assert rank_seq_lower(F, w) == typeA.rank_seq_lower(vperm, pA), i
    print("A5: all 720 lower intervals: fast engine == permutation engine")

    for typ, n, want, cg in (("D", 5, 1.069459, 3), ("D", 6, 1.040703, 2)):
        F = FastWeyl(typ, n)
        best = None
        for v in slab(F, cg):
            a = rank_seq_lower(F, v)
            if a is None or len(a) < 3:
                continue
            r = min_ratio(a)[0]
            best = r if best is None or r < best else best
        assert abs(float(best) - want) < 1e-6, (typ, n, best)
        print(f"{typ}{n}: known global min {want} reproduced")
    F = FastWeyl("B", 4)
    v = F.e
    for letter in (3, 4, 3, 4):
        g = F.gen_act[letter - 1]
        v = (compose(v[0], g), compose(g, v[1]))
    assert rank_seq_lower(F, v) == [1, 2, 2, 2, 1]
    print("B4: known equality interval [e,3434] = (1,2,2,2,1) reproduced")
    print("ALL SELFTESTS PASS")


# ---------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("groups", nargs="*")
    ap.add_argument("--scan", action="store_true")
    ap.add_argument("--sample", action="store_true")
    ap.add_argument("--cogap", type=int, default=3)
    ap.add_argument("--num", type=int, default=10000)
    ap.add_argument("--dmin", type=int, default=4)
    ap.add_argument("--dmax", type=int, default=12)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--procs", type=int, default=max(1, os.cpu_count() - 2))
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return
    assert args.scan != args.sample, "pick exactly one of --scan/--sample"

    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(outdir, exist_ok=True)
    mode = "scan" if args.scan else "sample"
    names = [g.upper() for g in args.groups]
    out = os.path.join(outdir,
                       f"fast{mode}_{'-'.join(names)}_{os.getpid()}.md")
    lines = [f"# fast.py --{mode} — {' '.join(names)} "
             f"({'cogap<=' + str(args.cogap) if args.scan else f'num={args.num}, d in [{args.dmin},{args.dmax}], seed={args.seed}'}"
             f", procs={args.procs})\n",
             "Engine: root-action (fast.py), selftested against weyl.py + "
             "scaled.py + scaled_general.py.",
             "A ratio < 1 would be a COUNTEREXAMPLE to Brenti Conj 2.11.\n"]
    any_ce = False
    for name in names:
        typ, n = name[0], int(name[1:])
        F = FastWeyl(typ, n)
        best = {"r": None}
        ces = []

        def on_result(res, F=F, best=best, ces=ces):
            if res is None:
                return
            r = res[0]
            if best["r"] is None or r < best["r"][0]:
                best["r"] = res
                print(f"  new best: ratio={float(r):.6f} k={res[1]} "
                      f"ranks={res[3] if len(res[3]) < 25 else '(long)'}",
                      flush=True)
            if r < 1:
                ces.append(res)
                print(f"*** RATIO < 1 in {name}: {res} ***", flush=True)

        t0 = time.time()
        if args.scan:
            cands = slab(F, args.cogap)
            print(f"{name}: |W|={sum(F.poincare)}, ell(w0)={F.L}, "
                  f"slab cogap<={args.cogap}: {len(cands)} candidates, "
                  f"procs={args.procs}", flush=True)
            run_pool(args.procs, typ, n, _eval_candidate,
                     sorted(cands, key=lambda w: -length(w[0])),
                     progress_every=25, log=lambda m: print(m, flush=True),
                     on_result=on_result)
        else:
            jobs = [(args.seed * 10_000_000 + i, args.dmin, args.dmax,
                     2 * F.L // 3) for i in range(args.num)]
            print(f"{name}: |W|={sum(F.poincare)}, sampling {args.num} "
                  f"short intervals, procs={args.procs}", flush=True)
            run_pool(args.procs, typ, n, _eval_sample, jobs,
                     progress_every=500, log=lambda m: print(m, flush=True),
                     on_result=on_result)
        r, k, margin, a = best["r"][:4]
        elems = best["r"][4:]
        words = [F.word_of(w) or "e" for w in elems]
        verdict = "**COUNTEREXAMPLE**" if ces else "all pass"
        print(f"{name}: min ratio {float(r):.6f} (margin {margin}) at "
              f"[{', '.join(words) if len(words) > 1 else 'e, ' + words[0]}] "
              f"k={k} — {verdict}  [{time.time() - t0:.0f}s]", flush=True)
        lines += [f"## {name}  ({mode}, {time.time() - t0:.0f}s)",
                  f"- verdict: **{verdict}**",
                  f"- min ratio: {float(r):.6f} = {r} (margin {margin}) k={k}",
                  f"- witness: [{', '.join(words) if len(words) > 1 else 'e, ' + words[0]}]",
                  f"- ranks: {a}", ""]
        any_ce = any_ce or bool(ces)
    with open(out, "w") as f:
        f.write("\n".join(lines))
    print(f"\nwrote {out}")
    if any_ce:
        print("\n*** COUNTEREXAMPLE — prior-art recheck + independent "
              "re-verification (scaled_general.py + weyl.py) first. ***")


if __name__ == "__main__":
    main()
