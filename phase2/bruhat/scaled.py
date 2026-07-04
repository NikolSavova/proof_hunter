"""Scaled near-miss search for Brenti Conj. 2.11 in big type-A Weyl groups (A7-A12).

Sihao's lane (HANDOFF §7): where exhaustive verification can't go, hunt the min
log-concavity ratio over LOWER Bruhat intervals [e,v]. Motivation from the
exhaustive runs (results/run_A2-...-F4_64112.md): every simply-laced global
min-ratio witness is a lower interval with v NEAR THE TOP element w0
(co-length ell(w0)-ell(v) = 0..3), and ratio-1 decays geometrically in rank —
a counterexample would show up as a NEW witness family overtaking that decay.

Method (exact integer arithmetic, no global bitsets — those need ~16GB at A8):

    rank_seq([e,v])_l  =  PoincareCoeff(W)_l  -  #{z : ell(z)=l, z NOT<= v}

The complement C(v) = {z !<= v} is an up-set in Bruhat order, so it is
enumerated completely by a downward cover-BFS from w0 that prunes at any
z <= v (tableau criterion). For v near w0, |C(v)| is tiny even when |W| is
astronomically large (A6 witness: |C|=144 of 5040), so this scales to A12
(|W| = 13! = 6.2e9) — the regime the exhaustive tier can never reach.

Elements are one-line permutations (tuples). Type A only for now; the same
complement trick works verbatim for B/D with signed permutations (TODO).

Self-checks (same ethos as weyl.py — nothing is trusted alone):
  1. --selftest cross-validates rank_seq_lower against weyl.WeylGroup
     .rank_sequence on ALL lower intervals of A3, A4, A5 (three independent
     disagreement points: group model, order criterion, enumeration).
  2. An independent second enumeration (direct ideal BFS from v) is compared
     on all of A3-A5 as well — complement method and ideal method share no code
     path except cocovers().
  3. Known global minima are reproduced: A3 25/18, A4 121/100 (at w0 itself),
     A5 1.122222 (co-length 1), A6 1.079096 (co-length 1).
  4. Structural asserts on every candidate: a_0 = a_{ell(v)} = 1, all a_l > 0,
     and complement level counts equal the FULL Poincare coefficients above
     ell(v) (everything longer than v must lie in the complement).

Usage:
    python3 scaled.py --selftest
    python3 scaled.py A7 --cogap 6          # scan all v with ell(w0)-ell(v)<=6
    python3 scaled.py A8 A9 --cogap 4 --deepen
Results append-only to results/scaled_<groups>_<pid>.md (house rule).
"""

import argparse
import os
import sys
import time
from fractions import Fraction


# ------------------------------------------------------------- permutations

def inversions(p):
    m = len(p)
    return sum(1 for i in range(m) for j in range(i + 1, m) if p[i] > p[j])


def w0_perm(m):
    return tuple(range(m - 1, -1, -1))


def rankmat(p):
    """R[i][j] = #{k <= i : p[k] <= j}  (0-indexed, inclusive)."""
    m = len(p)
    R = [[0] * m for _ in range(m)]
    row = [0] * m
    for i in range(m):
        for j in range(p[i], m):
            row[j] += 1
        R[i] = row[:]
    return R


def bruhat_leq(zR, vR, m):
    """z <= v  iff  R_z >= R_v pointwise (tableau/rank-matrix criterion)."""
    for i in range(m):
        zRi, vRi = zR[i], vR[i]
        for j in range(m):
            if zRi[j] < vRi[j]:
                return False
    return True


def cocovers(p):
    """All u covered by p in Bruhat order: swap p[i]>p[j] (i<j) with no
    intermediate value p[j] < p[k] < p[i] at position i<k<j."""
    m = len(p)
    out = []
    for i in range(m):
        pi = p[i]
        for j in range(i + 1, m):
            pj = p[j]
            if pi > pj and not any(pj < p[k] < pi for k in range(i + 1, j)):
                q = list(p)
                q[i], q[j] = pj, pi
                out.append(tuple(q))
    return out


def word_from_perm(p):
    """A reduced word (1-indexed letters, right-multiplication convention —
    same as weyl.py) for p; verified by roundtrip in perm_from_word."""
    p = list(p)
    rev = []
    while True:
        for i in range(len(p) - 1):
            if p[i] > p[i + 1]:
                p[i], p[i + 1] = p[i + 1], p[i]
                rev.append(i + 1)
                break
        else:
            break
    return tuple(reversed(rev))


def perm_from_word(word, m):
    p = list(range(m))
    for letter in word:
        j = letter - 1
        p[j], p[j + 1] = p[j + 1], p[j]
    return tuple(p)


# ------------------------------------------------------ Poincare coefficients

def poincare_A(n):
    """Coefficients of prod_{d=2}^{n+1} (q^d-1)/(q-1) — level sizes of A_n."""
    poly = [1]
    for d in range(2, n + 2):
        poly = [sum(poly[k - j] for j in range(min(d, k + 1))
                    if 0 <= k - j < len(poly))
                for k in range(len(poly) + d - 1)]
    return poly


# ------------------------------------------------------- the two enumerations

def complement_levels(v, cap=None):
    """Level counts of C(v) = {z !<= v}: downward cover-BFS from w0, pruning
    at z <= v. Returns dict length->count, or None if cap exceeded."""
    m = len(v)
    L = m * (m - 1) // 2
    w0 = w0_perm(m)
    if v == w0:
        return {}
    vR = rankmat(v)
    seen = {w0}
    levels = {L: 1}
    frontier = [w0]
    l = L
    while frontier:
        l -= 1
        nxt = []
        for z in frontier:
            for u in cocovers(z):
                if u in seen:
                    continue
                if bruhat_leq(rankmat(u), vR, m):
                    continue
                seen.add(u)
                nxt.append(u)
        if nxt:
            levels[l] = len(nxt)
        if cap is not None and len(seen) > cap:
            return None
        frontier = nxt
    return levels


def ideal_levels_direct(v):
    """INDEPENDENT check: level counts of {z <= v} by downward BFS from v.
    Only feasible for moderate ideals; used in --selftest."""
    seen = {v}
    frontier = [v]
    levels = {inversions(v): 1}
    l = inversions(v)
    while frontier:
        l -= 1
        nxt = []
        for z in frontier:
            for u in cocovers(z):
                if u not in seen:
                    seen.add(u)
                    nxt.append(u)
        if nxt:
            levels[l] = len(nxt)
        frontier = nxt
    return levels


def rank_seq_lower(v, poincare, cap=None):
    """Rank sequence of [e,v] = full Poincare levels minus complement levels."""
    L = inversions(v)
    comp = complement_levels(v, cap=cap)
    if comp is None:
        return None
    # structural checks: above ell(v) the complement must be EVERYTHING
    for l in range(L + 1, len(poincare)):
        assert comp.get(l, 0) == poincare[l], \
            f"complement mismatch above ell(v) at level {l}"
    a = [poincare[l] - comp.get(l, 0) for l in range(L + 1)]
    assert a[0] == 1 and a[L] == 1, f"bad rank seq ends: {a}"
    assert all(x > 0 for x in a), f"empty level in graded interval: {a}"
    return a


# ------------------------------------------------------------------ the score

def min_ratio(a):
    """Min over k of a_k^2 / (a_{k-1} a_{k+1}), exact. Returns
    (Fraction ratio, k, int margin) or None if len < 3. Ratio < 1 = THE RESULT."""
    best = None
    for k in range(1, len(a) - 1):
        num, den = a[k] * a[k], a[k - 1] * a[k + 1]
        if best is None or num * best[0].denominator < best[0].numerator * den:
            best = (Fraction(num, den), k, num - den)
    return best


# -------------------------------------------------------------------- search

def slab(m, cogap):
    """All v with ell(w0)-ell(v) <= cogap, by downward cover-BFS from w0."""
    w0 = w0_perm(m)
    seen = {w0}
    frontier = [w0]
    for _ in range(cogap):
        nxt = []
        for z in frontier:
            for u in cocovers(z):
                if u not in seen:
                    seen.add(u)
                    nxt.append(u)
        frontier = nxt
    return seen


def evaluate(v, poincare, cap=None):
    a = rank_seq_lower(v, poincare, cap=cap)
    if a is None or len(a) < 3:
        return None
    r, k, margin = min_ratio(a)
    return {"v": v, "ratio": r, "k": k, "margin": margin, "ranks": a}


def scan_group(n, cogap, deepen=False, cap=5_000_000, log=print):
    m = n + 1
    poincare = poincare_A(n)
    L = m * (m - 1) // 2
    cands = slab(m, cogap)
    log(f"A{n}: |W|={sum(poincare)}, ell(w0)={L}, "
        f"slab cogap<={cogap}: {len(cands)} candidates")
    best = None
    t0 = time.time()
    for i, v in enumerate(sorted(cands, key=inversions, reverse=True)):
        res = evaluate(v, poincare, cap=cap)
        if res is None:
            continue
        if best is None or res["ratio"] < best["ratio"]:
            best = res
            log(f"  new best: ratio={float(res['ratio']):.6f} "
                f"cogap={L - inversions(v)} k={res['k']} "
                f"[{i + 1}/{len(cands)}, {time.time() - t0:.0f}s]")
    if deepen and best is not None:
        log(f"A{n}: greedy deepen from best witness...")
        cur, visited = best, {best["v"]}
        while True:
            improved = None
            for u in cocovers(cur["v"]):
                if u in visited:
                    continue
                visited.add(u)
                res = evaluate(u, poincare, cap=cap)
                if res and res["ratio"] < cur["ratio"] and \
                        (improved is None or res["ratio"] < improved["ratio"]):
                    improved = res
            if improved is None:
                break
            cur = improved
            log(f"  deepen: ratio={float(cur['ratio']):.6f} "
                f"cogap={L - inversions(cur['v'])}")
        if cur["ratio"] < best["ratio"]:
            best = cur
    best["time"] = time.time() - t0
    best["cogap_scanned"] = cogap
    best["n"] = n
    return best


# ------------------------------------------------------------------ selftest

def selftest():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from weyl import WeylGroup

    # 1+2: cross-validate BOTH enumerations against weyl.py on all lower
    # intervals of A3, A4, A5 (identity has index 0: elems sorted by length).
    for n in (3, 4, 5):
        W = WeylGroup("A", n)
        poincare = poincare_A(n)
        m = n + 1
        for i in range(W.N):
            v = perm_from_word(W.word[i], m)
            assert inversions(v) == W.length[i]
            ref = W.rank_sequence(0, i)
            got = rank_seq_lower(v, poincare)
            assert got == ref, f"A{n} v={v}: {got} != weyl {ref}"
            lv = inversions(v)
            direct = ideal_levels_direct(v)
            assert [direct.get(l, 0) for l in range(lv + 1)] == ref, \
                f"A{n} v={v}: direct ideal BFS != weyl"
        print(f"A{n}: all {W.N} lower intervals match weyl.py "
              f"(complement method AND direct ideal BFS)")

    # word roundtrip
    v = (3, 5, 0, 4, 1, 2)
    assert perm_from_word(word_from_perm(v), 6) == v
    assert len(word_from_perm(v)) == inversions(v)

    # 3: reproduce the known exhaustive-run global minima (lower intervals)
    known = {  # n: (ratio, cogap of the witness)
        3: (Fraction(25, 18), 1),
        4: (Fraction(121, 100), 0),
        5: (Fraction(101, 90), 1),  # 1.122222 (ranks ...90,101,101...)
    }
    for n in (3, 4, 5):
        best = scan_group(n, cogap=known[n][1] + 2, log=lambda *a: None)
        assert best["ratio"] == known[n][0], \
            f"A{n} known min-ratio mismatch: {best['ratio']}"
        print(f"A{n}: known global min ratio {float(best['ratio']):.6f} "
              f"reproduced by slab scan")
    best6 = scan_group(6, cogap=2, log=lambda *a: None)
    assert abs(float(best6["ratio"]) - 1.079096) < 1e-6, best6["ratio"]
    print(f"A6: known global min ratio 1.079096 reproduced "
          f"(witness ranks {best6['ranks']})")
    print("ALL SELFTESTS PASS")


# ---------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("groups", nargs="*", help="e.g. A7 A8")
    ap.add_argument("--cogap", type=int, default=4)
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
             "Method: rank_seq([e,v]) = Poincare - complement-BFS; exact ints.",
             "A ratio < 1 would be a COUNTEREXAMPLE to Brenti Conj 2.11.\n"]
    found_violation = False
    for name in names:
        assert name[0] == "A", "type A only for now"
        n = int(name[1:])
        best = scan_group(n, args.cogap, deepen=args.deepen, cap=args.cap)
        v = best["v"]
        word = "".join(str(x) for x in word_from_perm(v))
        r = float(best["ratio"])
        verdict = "**COUNTEREXAMPLE (ratio < 1)**" if r < 1 else "all pass"
        print(f"A{n}: min ratio {r:.6f} (margin {best['margin']}) at "
              f"[e, {word}] cogap={best['n'] * (best['n'] + 1) // 2 - inversions(v)} "
              f"k={best['k']} — {verdict}")
        lines += [f"## A{n}  (slab cogap<={best['cogap_scanned']}, "
                  f"{best['time']:.0f}s)",
                  f"- verdict: **{verdict}**",
                  f"- min ratio: {r:.6f} = {best['ratio']} "
                  f"(margin {best['margin']}) at k={best['k']}",
                  f"- witness: v = {list(v)} (one-line), reduced word {word}, "
                  f"ell(v)={inversions(v)}",
                  f"- ranks: {best['ranks']}", ""]
        if r < 1:
            found_violation = True
    with open(out, "w") as f:
        f.write("\n".join(lines))
    print(f"\nwrote {out}")
    if found_violation:
        print("\n*** RATIO < 1 FOUND — prior-art recheck + independent "
              "re-verification (ideal_levels_direct + weyl.py if feasible) "
              "before celebrating. ***")


if __name__ == "__main__":
    main()
