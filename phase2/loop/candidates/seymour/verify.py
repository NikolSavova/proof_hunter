#!/usr/bin/env python3
"""Verifier and small-case harness for Seymour's second neighbourhood conjecture.

Written BEFORE the CP-SAT model, per the project's standing rule: the harness defines what
"counterexample" means, so the model cannot later move the goalposts. Any CP-SAT solution MUST be
re-checked by `is_counterexample` here, independently of the solver, before it is believed.

Definitions (fixed). An ORIENTED GRAPH on vertex set {0..n-1} has, for each unordered pair, at
most one of the two arcs. N^+(v) is the out-neighbourhood. N^{++}(v) is the set of vertices at
EXACT directed distance 2: reachable by a path of length 2, minus N^+(v), minus {v}. A vertex v is
a SEYMOUR VERTEX if |N^{++}(v)| >= |N^+(v)|. A COUNTEREXAMPLE has no Seymour vertex.

Representation: out[v] is an int bitmask of N^+(v). This makes the second neighbourhood a few
OR/AND-NOT operations and the whole check O(n^2) word ops.

Blocks
  [A] verifier self-test   hand-checked tiny graphs, including the directed triangle
  [B] exhaustive n <= 6    every oriented graph; the conjecture must hold for all of them
  [C] tournaments n <= 7   Dean's conjecture (Fisher): every tournament has a Seymour vertex
  [D] random probe         how close do random oriented graphs get to having NO Seymour vertex?
                           reports the best (largest) number of non-Seymour vertices seen, which
                           is the quantity a counterexample must drive all the way to n

Usage: ./verify.py [A B C D]
"""
import itertools
import random
import sys


def second_out(out, n, v):
    """Bitmask of N^{++}(v): distance exactly 2."""
    reach = 0
    m = out[v]
    u = 0
    mm = m
    while mm:
        if mm & 1:
            reach |= out[u]
        mm >>= 1
        u += 1
    return reach & ~m & ~(1 << v)


def margins(out, n):
    """margin(v) = |N^{++}(v)| - |N^+(v)|. v is a Seymour vertex iff margin(v) >= 0."""
    return [bin(second_out(out, n, v)).count("1") - bin(out[v]).count("1") for v in range(n)]


def has_seymour_vertex(out, n):
    for v in range(n):
        if bin(second_out(out, n, v)).count("1") >= bin(out[v]).count("1"):
            return True
    return False


def is_counterexample(out, n):
    """The ONLY definition that counts. Every vertex must fail."""
    return all(m < 0 for m in margins(out, n))


def from_pairs(n, states):
    """states[i] in {0,1,2} for the i-th pair (u<v): 0 = no arc, 1 = u->v, 2 = v->u."""
    out = [0] * n
    for (u, v), s in zip(itertools.combinations(range(n), 2), states):
        if s == 1:
            out[u] |= 1 << v
        elif s == 2:
            out[v] |= 1 << u
    return out


def block_A(log_):
    ok = True
    # directed triangle 0->1->2->0 : N^+(0)={1}, N^{++}(0)={2}, margin 0 -> Seymour vertex
    out = from_pairs(3, [1, 2, 1])          # 0->1, 2->0, 1->2
    m = margins(out, 3)
    log_(f"  directed triangle margins {m} (expect all 0, every vertex Seymour)")
    ok &= m == [0, 0, 0] and has_seymour_vertex(out, 3)
    # single arc 0->1 on 2 vertices: N^+(0)={1}, N^{++}(0)={} -> margin -1; vertex 1 has margin 0
    out = from_pairs(2, [1])
    m = margins(out, 2)
    log_(f"  single arc margins {m} (expect [-1, 0]; vertex 1 is a Seymour vertex)")
    ok &= m == [-1, 0] and has_seymour_vertex(out, 2)
    # empty graph: every out-degree 0, margin 0 everywhere
    out = [0] * 4
    ok &= margins(out, 4) == [0, 0, 0, 0]
    # transitive triangle 0->1, 0->2, 1->2: N^+(0)={1,2}, N^{++}(0)= {} (2 already in N^+)
    out = from_pairs(3, [1, 1, 1])
    m = margins(out, 3)
    log_(f"  transitive triangle margins {m} (vertex 0 has margin -2, but 1 and 2 are Seymour)")
    ok &= m[0] == -2 and has_seymour_vertex(out, 3)
    log_(f"  verifier self-test -> {'PASS' if ok else 'FAIL'}")
    return ok


def block_B(log_):
    ok = True
    for n in range(2, 7):
        npairs = n * (n - 1) // 2
        total = 3 ** npairs
        worst = None
        cnt = 0
        for code in range(total):
            st, c = [], code
            for _ in range(npairs):
                st.append(c % 3)
                c //= 3
            out = from_pairs(n, st)
            m = margins(out, n)
            bad = sum(1 for x in m if x < 0)
            if worst is None or bad > worst[0]:
                worst = (bad, st[:])
            if bad == n:
                cnt += 1
        ok &= cnt == 0
        log_(f"  n={n}: {total:>9,} oriented graphs, counterexamples found = {cnt}; "
             f"max non-Seymour vertices = {worst[0]}/{n}")
    log_(f"  exhaustive n<=6 finds no counterexample -> {'PASS' if ok else 'FAIL'}")
    return ok


def block_C(log_):
    ok = True
    for n in range(3, 8):
        npairs = n * (n - 1) // 2
        cnt = 0
        for code in range(2 ** npairs):
            st = [1 + ((code >> i) & 1) for i in range(npairs)]   # every pair oriented: 1 or 2
            out = from_pairs(n, st)
            if is_counterexample(out, n):
                cnt += 1
        ok &= cnt == 0
        log_(f"  n={n}: {2**npairs:>9,} tournaments, counterexamples = {cnt}")
    log_(f"  Dean's conjecture holds on all tournaments n<=7 -> {'PASS' if ok else 'FAIL'}")
    return ok


def block_D(log_):
    """How hard is it to make MANY vertices fail at once? A counterexample needs ALL of them."""
    rng = random.Random(20260813)
    for n, delta in ((19, 8), (25, 8), (36, 8)):
        best = None
        trials = 20000
        for _ in range(trials):
            # random orientation biased to out-degree ~delta..delta+3
            out = [0] * n
            for u, v in itertools.combinations(range(n), 2):
                r = rng.random()
                p = min(0.95, (delta + 2) / (n - 1))
                if r < p:
                    if rng.random() < 0.5:
                        out[u] |= 1 << v
                    else:
                        out[v] |= 1 << u
            m = margins(out, n)
            degs = [bin(out[v]).count("1") for v in range(n)]
            if min(degs) < delta:
                continue
            bad = sum(1 for x in m if x < 0)
            if best is None or bad > best[0]:
                best = (bad, min(degs), max(m))
        if best:
            log_(f"  n={n}, min out-degree >= {delta}: best over {trials:,} random graphs = "
                 f"{best[0]}/{n} vertices non-Seymour (need {n}/{n}); "
                 f"largest margin still {best[2]:+d}")
        else:
            log_(f"  n={n}: no random sample met the min-degree floor")
    log_("  random probe is a difficulty gauge only; it proves nothing")
    return True


BLOCKS = {"A": ("verifier self-test", block_A), "B": ("exhaustive n<=6", block_B),
          "C": ("tournaments n<=7 (Dean)", block_C), "D": ("random difficulty probe", block_D)}

if __name__ == "__main__":
    which = [a.upper() for a in sys.argv[1:]] or list(BLOCKS)
    lines = []

    def log_(s):
        print(s, flush=True)
        lines.append(s)

    log_("Seymour second neighbourhood — verifier and small-case harness")
    allok = True
    for k in which:
        name, fn = BLOCKS[k]
        log_(f"[{k}] {name}:")
        allok &= fn(log_)
    log_(f"# OVERALL: {'ALL CHECKS PASS' if allok else 'SOME CHECKS FAILED'}")
    import pathlib
    (pathlib.Path(__file__).resolve().parent / "out_verify.txt").write_text("\n".join(lines) + "\n")
