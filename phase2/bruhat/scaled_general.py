"""Generic-type per-interval Bruhat engine — Sihao's lane beyond type A.

weyl.py enumerates the WHOLE group with |W|-bit bitsets: impossible for D7+
(|W|=322k, bitsets ~13GB) let alone E7 (2.9M). This module computes rank
sequences of single intervals with NO global enumeration, for ANY type in
weyl.py's tables (A/B/D/E/F/G). Elements are (matrix, inverse-matrix) pairs
on the simple-root basis, reusing weyl.py's Cartan data verbatim.

Primitives (each standard, and none trusts the others — see selftest):
  length(w)        #positive roots sent negative           [inversion formula]
  cocovers(w)      {w t_a : a inversion of w, length drops exactly 1}
  leq via LeqTop   lifting-property recursion on a fixed top element
                   (Bjorner-Brenti Prop 2.2.7), memoized along the fixed
                   left-descent chain of the top
  rank_seq_lower(v)     = Poincare(degrees) - complement-BFS-from-w0(v)
                          (complement {z !<= v} is an up-set: tiny for v near w0)
  interval_levels(u, v)  down-BFS from v pruning z !>= u, where z >= u is
                          tested as z*w0 <= u*w0 (Bruhat anti-automorphism
                          w -> w*w0, BB Prop 2.3.4) -> general intervals [u,v]

Self-checks (--selftest):
  1. B3 + D4 vs weyl.WeylGroup: length, ALL pairwise <=, ALL lower-interval
     rank sequences, and general-interval rank sequences (all comparable pairs
     in B3, sampled in D4).
  2. A5 vs scaled.py's independent permutation engine: all 720 lower intervals.
  3. Known exhaustive minima reproduced: D5 1.069459, B4 (1,2,2,2,1) ratio-1.0
     equality interval, D6 1.040703.

Usage:
    python3 scaled_general.py --selftest
    python3 scaled_general.py D7 D8 --cogap 3 --deepen
"""

import argparse
import os
import sys
import time
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from weyl import cartan, gen_matrix, matmul, apply, ORDER, NPOS, DEGREES
from scaled import min_ratio  # exact-Fraction scorer, already selftested


def poincare_poly(typ, n):
    poly = [1]
    for d in DEGREES[typ](n):
        poly = [sum(poly[k - j] for j in range(min(d, k + 1))
                    if 0 <= k - j < len(poly))
                for k in range(len(poly) + d - 1)]
    return poly


class GWeyl:
    """Root-system scaffolding only — never enumerates the group."""

    def __init__(self, typ, n):
        self.typ, self.n, self.name = typ, n, f"{typ}{n}"
        A = cartan(typ, n)
        self.gens = [gen_matrix(A, i, n) for i in range(n)]
        self.ident = tuple(tuple(1 if r == c else 0 for c in range(n))
                           for r in range(n))
        self.e = (self.ident, self.ident)

        # roots = orbit of the simple roots under the generators
        simple = [tuple(1 if k == i else 0 for k in range(n)) for i in range(n)]
        self.simple = simple
        roots = set(simple)
        frontier = list(simple)
        while frontier:
            nxt = []
            for r in frontier:
                for g in self.gens:
                    gr = apply(g, r)
                    if gr not in roots:
                        roots.add(gr)
                        nxt.append(gr)
            frontier = nxt
        self.pos = [r for r in roots if sum(r) > 0]
        assert all((sum(r) > 0) != (sum(r) < 0) for r in roots)
        assert len(self.pos) == NPOS[typ](n), f"#pos roots({self.name})"
        self.P = len(self.pos)

        # one reflection per positive root, built as U s_{i0} U^-1 by a BFS on
        # roots carrying (U, U^-1) pairs from the originating simple root
        refl = {}
        carrier = {r: (self.ident, self.ident, i) for i, r in enumerate(simple)}
        frontier = list(simple)
        while frontier:
            nxt = []
            for r in frontier:
                for gi, g in enumerate(self.gens):
                    gr = apply(g, r)
                    if gr not in carrier:
                        U, Uinv, i0 = carrier[r]
                        carrier[gr] = (matmul(g, U), matmul(Uinv, g), i0)
                        nxt.append(gr)
            frontier = nxt
        for r, (U, Uinv, i0) in carrier.items():
            assert matmul(U, Uinv) == self.ident
            pr = r if sum(r) > 0 else tuple(-c for c in r)
            if pr not in refl:
                refl[pr] = matmul(matmul(U, self.gens[i0]), Uinv)
        assert len(refl) == self.P, f"#reflections({self.name})"
        self.reflections = list(refl.values())
        for t in self.reflections:
            assert matmul(t, t) == self.ident

        self.poincare = poincare_poly(typ, n)
        assert sum(self.poincare) == ORDER[typ](n)
        self.L = len(self.poincare) - 1
        assert self.L == self.P

        # longest element by greedy ascent
        w = self.e
        l = 0
        while True:
            for i, g in enumerate(self.gens):
                if self.length_drop_right_simple(w, i) is False:
                    w = (matmul(w[0], g), matmul(g, w[1]))
                    l += 1
                    break
            else:
                break
        assert l == self.P and self.length(w[0]) == self.P, "w0 construction"
        self.w0 = w
        assert matmul(w[0], w[0]) == self.ident or True  # w0^2=e only if -1 in W

    # --- length & descents
    def length(self, mat):
        return sum(1 for r in self.pos if sum(apply(mat, r)) < 0)

    def length_drop_right_simple(self, w, i):
        """True iff l(w s_i) < l(w)  (iff w(alpha_i) < 0)."""
        return sum(apply(w[0], self.simple[i])) < 0

    def left_descent(self, w, i):
        """True iff l(s_i w) < l(w)  (iff w^-1(alpha_i) < 0)."""
        return sum(apply(w[1], self.simple[i])) < 0

    # --- covers
    def cocovers(self, w, lw=None):
        """All u with u <| w (covered by w): u = w t, l drops exactly 1."""
        if lw is None:
            lw = self.length(w[0])
        out = []
        for t in self.reflections:
            wt = matmul(w[0], t)
            if self.length(wt) == lw - 1:
                out.append((wt, matmul(t, w[1])))
        return out

    def rmul_w0(self, w):
        return (matmul(w[0], self.w0[0]), matmul(self.w0[1], w[1]))


class LeqTop:
    """Memoized test  z <= v  for a FIXED v, via the lifting property along
    v's canonical left-descent chain: with s a left descent of v,
       z <= v  <=>  (s z <= s v  if s z < z   else   z <= s v)."""

    def __init__(self, G, v):
        self.G = G
        chain, desc = [v], []
        cur, l = v, G.length(v[0])
        while l > 0:
            for i in range(G.n):
                if G.left_descent(cur, i):
                    g = G.gens[i]
                    cur = (matmul(g, cur[0]), matmul(cur[1], g))
                    chain.append(cur)
                    desc.append(i)
                    l -= 1
                    break
            else:
                raise AssertionError("no descent on nonidentity element")
        self.chain = chain[::-1]   # chain[k] has length k
        self.desc = desc[::-1]     # desc[k]: chain[k] = s_{desc[k]} * chain[k+1]...
        # note: chain[k+1] has left descent desc[k] and s*chain[k+1] = chain[k]
        self.lv = len(self.chain) - 1
        self.memo = {}

    def leq(self, z, lz=None):
        if lz is None:
            lz = self.G.length(z[0])
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
        g = self.G.gens[s]
        if self.G.left_descent(z, s):
            sz = (matmul(g, z[0]), matmul(z[1], g))
            res = self._leq(sz, lz - 1, k - 1)
        else:
            res = self._leq(z, lz, k - 1)
        self.memo[key] = res
        return res


# ------------------------------------------------------- interval enumeration

def complement_levels(G, v, cap=None):
    """Level counts of {z !<= v} (an up-set) by down-BFS from w0, pruning at
    z <= v. Exact and complete by the chain property."""
    lv = G.length(v[0])
    if lv == G.L:
        return {}
    top = LeqTop(G, v)
    seen = {G.w0[0]}
    levels = {G.L: 1}
    frontier = [G.w0]
    l = G.L
    while frontier:
        l -= 1
        nxt = []
        for z in frontier:
            for u in G.cocovers(z, l + 1):
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


def rank_seq_lower(G, v, cap=None):
    lv = G.length(v[0])
    comp = complement_levels(G, v, cap=cap)
    if comp is None:
        return None
    for l in range(lv + 1, G.L + 1):
        assert comp.get(l, 0) == G.poincare[l], "complement above ell(v)"
    a = [G.poincare[l] - comp.get(l, 0) for l in range(lv + 1)]
    assert a[0] == 1 and a[lv] == 1 and all(x > 0 for x in a), a
    return a


def interval_levels(G, u, v, cap=None):
    """Rank sequence of a GENERAL interval [u,v]: down-BFS from v keeping
    z >= u, tested as z*w0 <= u*w0 (anti-automorphism). None if u !<= v."""
    lu, lv = G.length(u[0]), G.length(v[0])
    top = LeqTop(G, G.rmul_w0(u))     # z >= u  <=>  z*w0 <= u*w0
    if not top.leq(G.rmul_w0(v), G.L - lv):
        return None
    seen = {v[0]}
    levels = {lv: 1}
    frontier = [v]
    l = lv
    while frontier and l > lu:
        l -= 1
        nxt = []
        for z in frontier:
            for w in G.cocovers(z, l + 1):
                if w[0] in seen:
                    continue
                if not top.leq(G.rmul_w0(w), G.L - l):
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


# -------------------------------------------------------------------- search

def slab(G, cogap):
    seen = {G.w0[0]: G.w0}
    frontier = [G.w0]
    l = G.L
    for _ in range(cogap):
        nxt = []
        for z in frontier:
            for u in G.cocovers(z, l):
                if u[0] not in seen:
                    seen[u[0]] = u
                    nxt.append(u)
        frontier = nxt
        l -= 1
    return list(seen.values())


def scan_group(G, cogap, deepen=False, cap=5_000_000, log=print):
    cands = slab(G, cogap)
    log(f"{G.name}: |W|={sum(G.poincare)}, ell(w0)={G.L}, "
        f"slab cogap<={cogap}: {len(cands)} candidates")
    best = None
    t0 = time.time()
    for i, v in enumerate(sorted(cands, key=lambda w: -G.length(w[0]))):
        a = rank_seq_lower(G, v, cap=cap)
        if a is None or len(a) < 3:
            continue
        r, k, margin = min_ratio(a)
        if best is None or r < best["ratio"]:
            best = {"v": v, "ratio": r, "k": k, "margin": margin, "ranks": a}
            log(f"  new best: ratio={float(r):.6f} "
                f"cogap={G.L - G.length(v[0])} k={k} "
                f"[{i + 1}/{len(cands)}, {time.time() - t0:.0f}s]")
    if deepen and best is not None:
        log(f"{G.name}: greedy deepen...")
        cur, visited = best, {best["v"][0]}
        while True:
            improved = None
            for u in G.cocovers(cur["v"]):
                if u[0] in visited:
                    continue
                visited.add(u[0])
                a = rank_seq_lower(G, u, cap=cap)
                if a is None or len(a) < 3:
                    continue
                r, k, margin = min_ratio(a)
                if r < cur["ratio"] and (improved is None or r < improved["ratio"]):
                    improved = {"v": u, "ratio": r, "k": k,
                                "margin": margin, "ranks": a}
            if improved is None:
                break
            cur = improved
            log(f"  deepen: ratio={float(cur['ratio']):.6f}")
        if cur["ratio"] < best["ratio"]:
            best = cur
    best["time"] = time.time() - t0
    best["cogap_scanned"] = cogap
    return best


def word_of(G, v):
    """Reduced word by left-descent stripping; roundtrip-verified.
    Stripping s_a, s_b, ... gives v = s_a s_b ... s_z: the word IS the
    strip order (right-multiplication convention, same as weyl.py)."""
    out = []
    cur = v
    l = G.length(v[0])
    while l > 0:
        for i in range(G.n):
            if G.left_descent(cur, i):
                g = G.gens[i]
                cur = (matmul(g, cur[0]), matmul(cur[1], g))
                out.append(i + 1)
                l -= 1
                break
    m = G.ident
    for letter in out:
        m = matmul(m, G.gens[letter - 1])
    assert m == v[0], "reduced-word roundtrip failed"
    return "".join(str(x) for x in out)


# ------------------------------------------------------------------ selftest

def selftest():
    from weyl import WeylGroup
    import scaled as typeA

    # 1. B3 + D4 exhaustive cross-check against weyl.py
    for typ, n in (("B", 3), ("D", 4)):
        W = WeylGroup(typ, n)
        G = GWeyl(typ, n)
        pairs = []
        for i in range(W.N):
            m = G.ident
            for letter in W.word[i]:
                m = matmul(m, G.gens[letter - 1])
            minv = G.ident
            for letter in reversed(W.word[i]):
                minv = matmul(minv, G.gens[letter - 1])
            e = (m, minv)
            assert matmul(m, minv) == G.ident
            assert G.length(m) == W.length[i], "length mismatch"
            pairs.append(e)
        # pairwise <= vs weyl bitsets (all pairs)
        for i in range(W.N):
            top = LeqTop(G, pairs[i])
            for j in range(W.N):
                ref = bool((W.up[j] >> i) & 1)  # j <= i in weyl's indexing
                assert top.leq(pairs[j]) == ref, f"{typ}{n} leq({j},{i})"
        print(f"{typ}{n}: all {W.N}x{W.N} Bruhat comparisons match weyl.py")
        # all lower intervals + general intervals
        import random
        random.seed(0)
        checked = 0
        for i in range(W.N):
            ref = W.rank_sequence(0, i)
            assert rank_seq_lower(G, pairs[i]) == ref, f"{typ}{n} lower {i}"
            assert interval_levels(G, G.e, pairs[i]) == ref
        js = range(W.N) if W.N <= 60 else random.sample(range(W.N), 40)
        for j in js:
            for i in range(W.N):
                ref = W.rank_sequence(j, i)
                got = interval_levels(G, pairs[j], pairs[i])
                assert got == ref, f"{typ}{n} interval [{j},{i}]"
                checked += 1
        print(f"{typ}{n}: all {W.N} lower + {checked} general intervals "
              f"match weyl.py")

    # 2. A5 against the independent permutation engine
    G = GWeyl("A", 5)
    W = WeylGroup("A", 5)
    pA = typeA.poincare_A(5)
    for i in range(W.N):
        m = G.ident
        for letter in W.word[i]:
            m = matmul(m, G.gens[letter - 1])
        minv = G.ident
        for letter in reversed(W.word[i]):
            minv = matmul(minv, G.gens[letter - 1])
        vperm = typeA.perm_from_word(W.word[i], 6)
        assert rank_seq_lower(G, (m, minv)) == \
            typeA.rank_seq_lower(vperm, pA), f"A5 engine mismatch at {i}"
    print("A5: all 720 lower intervals: generic engine == permutation engine")

    # 3. known exhaustive minima
    G = GWeyl("D", 5)
    best = scan_group(G, cogap=3, log=lambda *a: None)
    assert abs(float(best["ratio"]) - 1.069459) < 1e-6, best["ratio"]
    print(f"D5: known global min 1.069459 reproduced (cogap "
          f"{G.L - G.length(best['v'][0])})")
    G = GWeyl("B", 4)
    v = G.e
    for letter in (3, 4, 3, 4):
        g = G.gens[letter - 1]
        v = (matmul(v[0], g), matmul(g, v[1]))
    a = rank_seq_lower(G, v)
    assert a == [1, 2, 2, 2, 1], a
    r, k, margin = min_ratio(a)
    assert r == 1 and margin == 0
    print("B4: known equality interval [e,3434] = (1,2,2,2,1), ratio exactly 1")
    G = GWeyl("D", 6)
    best = scan_group(G, cogap=2, log=lambda *a: None)
    assert abs(float(best["ratio"]) - 1.040703) < 1e-6, best["ratio"]
    print("D6: known global min 1.040703 reproduced")
    print("ALL SELFTESTS PASS")


# ---------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("groups", nargs="*", help="e.g. D7 D8 B6 E7")
    ap.add_argument("--cogap", type=int, default=3)
    ap.add_argument("--deepen", action="store_true")
    ap.add_argument("--cap", type=int, default=5_000_000)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return

    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(outdir, exist_ok=True)
    names = [g.upper() for g in args.groups]
    out = os.path.join(outdir, f"scaled_{'-'.join(names)}_{os.getpid()}.md")
    lines = [f"# Scaled lower-interval near-miss scan — {' '.join(names)} "
             f"(cogap<={args.cogap}{', deepen' if args.deepen else ''})\n",
             "Method: generic-type complement-BFS (scaled_general.py); "
             "exact ints.",
             "A ratio < 1 would be a COUNTEREXAMPLE to Brenti Conj 2.11.\n"]
    violation = False
    for name in names:
        typ, n = name[0], int(name[1:])
        G = GWeyl(typ, n)
        best = scan_group(G, args.cogap, deepen=args.deepen, cap=args.cap)
        v = best["v"]
        r = float(best["ratio"])
        word = word_of(G, v)
        verdict = "**COUNTEREXAMPLE (ratio < 1)**" if r < 1 else "all pass"
        print(f"{name}: min ratio {r:.6f} (margin {best['margin']}) at "
              f"[e, {word}] cogap={G.L - G.length(v[0])} k={best['k']} "
              f"— {verdict}")
        lines += [f"## {name}  (slab cogap<={best['cogap_scanned']}, "
                  f"{best['time']:.0f}s)",
                  f"- verdict: **{verdict}**",
                  f"- min ratio: {r:.6f} = {best['ratio']} "
                  f"(margin {best['margin']}) at k={best['k']}",
                  f"- witness: [e, {word}], ell(v)={G.length(v[0])}",
                  f"- ranks: {best['ranks']}", ""]
        if r < 1:
            violation = True
    with open(out, "w") as f:
        f.write("\n".join(lines))
    print(f"\nwrote {out}")
    if violation:
        print("\n*** RATIO < 1 — prior-art recheck + independent verification "
              "before celebrating. ***")


if __name__ == "__main__":
    main()
