#!/usr/bin/env python3
"""Independent re-derivation of the Erdős-838 paper's composition claim.

Written WITHOUT consulting the paper's own verify.py / lexicographic_blowup.py, so that agreement
is evidence rather than a shared bug. Everything is exact rational arithmetic.

The paper (paper/main.tex, Lemma 2.2 and section "Verification artifact") asserts:

  * orientation rules for the blow-up S[Q] with q_j displaced by (eps^2 x_j, eps y_j);
  * exact composition identities
        C(S[Q]) = C(Q) * sum_j c_j(S) n^{j-1}
        U(S[Q]) = U(Q) * sum_j u_j(S) n^{j-1}
        W(S[Q]) = r W(Q) + C(Q) U(Q) * sum_{j>=2} v_j(S) n^{j-2}
  * and the concrete value (C,U,W) = (14136, 14136, 441399) for S = Q = T_{4,2}, a 36-point set.

We rebuild T_{4,2} from the strong-separation operation, build the 36-point composition with
explicit rational coordinates, and count caps / cups / convex subsets from the ORIENTATION
DETERMINANTS ALONE -- no substitution formula is used in the counting path. Then we compare
against the formulas.

Convex-subset count uses the standard decomposition: a set of size >= 2 in convex position is
exactly an upper cap and a lower cup sharing their leftmost and rightmost points, so
        W = n + sum_{p<q} c(p,q) u(p,q),
with c(p,q), u(p,q) the numbers of caps / cups having first point p and last point q.

Usage: ./independent_check.py
"""
from fractions import Fraction as F
from itertools import combinations


def orient(p, q, r):
    """Sign of the determinant; points given left to right."""
    d = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    return (d > 0) - (d < 0)


def prec(A, B, eps):
    """A <- B  (strong separation, Lemma 4.1): A near (0,0), B near (1,1), both squashed."""
    out = [(eps * eps * x, eps * y) for (x, y) in A]
    out += [(1 + eps * eps * x, 1 + eps * y) for (x, y) in B]
    return out


def T(m, i, eps):
    """Pascal cell T_{m,i}: singleton at the boundary, else T_{m-1,i-1} <- T_{m-1,i}."""
    if i == 0 or i == m:
        return [(F(0), F(0))]
    return prec(T(m - 1, i - 1, eps), T(m - 1, i, eps), eps)


def strong_rule_report(A, B, eps):
    """Check coordinate order, general position, and mixed signs in A <- B."""
    P = prec(A, B, eps)
    cut = len(A)
    coordinate_order = all(
        P[t][0] < P[t + 1][0] and P[t][1] < P[t + 1][1]
        for t in range(len(P) - 1)
    )
    zeros = 0
    mixed_mismatches = 0
    for a, b, c in combinations(range(len(P)), 3):
        got = orient(P[a], P[b], P[c])
        if got == 0:
            zeros += 1
        sides = (a < cut, b < cut, c < cut)
        if sides[0] == sides[1] == sides[2]:
            continue
        expected = -1 if sides[0] == sides[1] else 1
        if got != expected:
            mixed_mismatches += 1
    return coordinate_order, zeros, mixed_mismatches


def T_audited(m, i, eps, reports):
    """Build a Pascal cell while auditing every nontrivial recursive glue."""
    if i == 0 or i == m:
        return [(F(0), F(0))]
    A = T_audited(m - 1, i - 1, eps, reports)
    B = T_audited(m - 1, i, eps, reports)
    reports.append(((m, i), len(A), len(B), strong_rule_report(A, B, eps)))
    return prec(A, B, eps)


def blowup(S, Q, eps):
    """S[Q] of (2.1): replace s_i = (X_i, Y_i) by the block (X_i + eps^2 x_j, Y_i + eps y_j)."""
    return [(X + eps * eps * x, Y + eps * y) for (X, Y) in S for (x, y) in Q]


def composition_rule_report(S, Q, eps):
    """Audit the labelled composition against all four orientation rules.

    General position is not enough: a moderately small epsilon may give no
    zero determinant while blocks still overlap or mixed signs have not yet
    reached their limiting values.
    """
    labelled = []
    for i, (X, Y) in enumerate(S):
        for j, (x, y) in enumerate(Q):
            labelled.append(((X + eps * eps * x, Y + eps * y), i, j))

    coordinate_order = all(
        labelled[t][0][0] < labelled[t + 1][0][0]
        and labelled[t][0][1] < labelled[t + 1][0][1]
        for t in range(len(labelled) - 1)
    )
    zeros = 0
    mismatches = 0
    by_kind = {}
    for a, b, c in combinations(range(len(labelled)), 3):
        pa, ia, ja = labelled[a]
        pb, ib, jb = labelled[b]
        pc, ic, jc = labelled[c]
        got = orient(pa, pb, pc)
        if ia == ic:
            expected = orient(Q[ja], Q[jb], Q[jc])
            kind = "one block"
        elif ia < ib < ic:
            expected = orient(S[ia], S[ib], S[ic])
            kind = "three blocks"
        elif ia == ib:
            expected = -1
            kind = "first two in one block"
        elif ib == ic:
            expected = 1
            kind = "last two in one block"
        else:
            raise AssertionError((ia, ib, ic))
        if got == 0:
            zeros += 1
        if got != expected:
            mismatches += 1
            by_kind[kind] = by_kind.get(kind, 0) + 1
    return coordinate_order, zeros, mismatches, by_kind


def sorted_pts(P):
    return sorted(P)


def general_position(P):
    n = len(P)
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                if orient(P[a], P[b], P[c]) == 0:
                    return False
    return True


def chain_counts(P, sign):
    """c[(p,q)] = number of chains (caps if sign=-1, cups if sign=+1) with first point p,
    last point q, counting the 2-point chain. DP over the last edge."""
    n = len(P)
    # f[(i,j)] = number of chains ending with edge i->j, i<j, first point unconstrained ->
    # we need first point too, so index by (first, i, j) is too big; instead run a DP per start.
    res = {}
    for s in range(n):
        f = {}
        for j in range(s + 1, n):
            f[(s, j)] = 1                       # the 2-point chain s->j
        for i in range(s + 1, n):
            for j in range(i + 1, n):
                tot = f.get((i, j), 0)
                for h in range(s, i):
                    if (h, i) in f and orient(P[h], P[i], P[j]) == sign:
                        tot += f[(h, i)]
                if tot:
                    f[(i, j)] = tot
        for j in range(s + 1, n):
            v = sum(f.get((i, j), 0) for i in range(s, j))
            # chains with first s and last j: sum over the penultimate point i
            if v:
                res[(s, j)] = v
    return res


def stats(P):
    """Return (C, U, W) and the size-graded vectors, computed only from orientations."""
    P = sorted_pts(P)
    n = len(P)
    caps = chain_counts(P, -1)
    cups = chain_counts(P, +1)
    C = n + sum(caps.values())          # singletons plus all chains of size >= 2
    U = n + sum(cups.values())
    W = n + sum(caps.get(k, 0) * cups.get(k, 0) for k in set(caps) | set(cups))
    return C, U, W


def graded(P, sign):
    """Number of chains of each size, for the substitution formulas."""
    P = sorted_pts(P)
    n = len(P)
    out = {1: n}
    # DP tracking length
    for s in range(n):
        f = {}
        for j in range(s + 1, n):
            f[(s, j)] = {2: 1}
        for i in range(s + 1, n):
            for j in range(i + 1, n):
                acc = dict(f.get((i, j), {}))
                for h in range(s, i):
                    if (h, i) in f and orient(P[h], P[i], P[j]) == sign:
                        for L, cnt in f[(h, i)].items():
                            acc[L + 1] = acc.get(L + 1, 0) + cnt
                if acc:
                    f[(i, j)] = acc
        for (i, j), d in f.items():
            for L, cnt in d.items():
                out[L] = out.get(L, 0) + cnt
    return out


def graded_convex(P):
    P = sorted_pts(P)
    n = len(P)
    caps, cups = {}, {}
    for sign, store in ((-1, caps), (1, cups)):
        for s in range(n):
            f = {}
            for j in range(s + 1, n):
                f[(s, j)] = {2: 1}
            for i in range(s + 1, n):
                for j in range(i + 1, n):
                    acc = dict(f.get((i, j), {}))
                    for h in range(s, i):
                        if (h, i) in f and orient(P[h], P[i], P[j]) == sign:
                            for L, cnt in f[(h, i)].items():
                                acc[L + 1] = acc.get(L + 1, 0) + cnt
                    if acc:
                        f[(i, j)] = acc
            for (i, j), d in f.items():
                key = (s, j)
                tgt = store.setdefault(key, {})
                for L, cnt in d.items():
                    tgt[L] = tgt.get(L, 0) + cnt
    out = {1: n}
    for k in set(caps) | set(cups):
        for L1, a in caps.get(k, {}).items():
            for L2, b in cups.get(k, {}).items():
                L = L1 + L2 - 2
                out[L] = out.get(L, 0) + a * b
    return out


def main():
    # The strict determinant threshold depends on the input coordinates.
    # In particular, the already nested Pascal cell has a much smaller
    # feature scale than the one-point inputs used to build it.  The proof
    # chooses epsilon afresh at every finite composition, so use separate
    # exact rational parameters here as well.
    template_eps = F(1, 97)
    template_reports = []
    S = sorted_pts(T_audited(4, 2, template_eps, template_reports))
    print(f"Template glues at eps={template_eps}:")
    for cell, a, b, report in template_reports:
        ordered, zeros, bad = report
        print(f"  T_{cell}: child sizes {a}+{b}, coordinate_order={ordered}, "
              f"zeros={zeros}, mixed_mismatches={bad}")
        assert ordered and zeros == 0 and bad == 0
    print(f"T_(4,2): {len(S)} points, general position: {general_position(S)}")
    cS, uS, wS = stats(S)
    print(f"  (C,U,W) of the 6-point template = ({cS}, {uS}, {wS})")
    gc, gu, gv = graded(S, -1), graded(S, 1), graded_convex(S)
    print(f"  caps by size {gc}\n  cups by size {gu}\n  convex by size {gv}")
    print(f"  largest cap = {max(gc)}, largest cup = {max(gu)}   (paper: a=b=3 for T_(4,2))")

    print("\nSearching outer scales and auditing every orientation rule:")
    composition_eps = None
    for candidate in (
        F(1, 97), F(1, 1000), F(1, 5000), F(1, 9000),
        F(1, 9500), F(1, 9750), F(1, 10000), F(1, 16384),
    ):
        ordered, zeros, bad, kinds = composition_rule_report(S, S, candidate)
        print(
            f"  eps={candidate}: coordinate_order={ordered}, zeros={zeros}, "
            f"rule_mismatches={bad}{' ' + str(kinds) if kinds else ''}"
        )
        if composition_eps is None and ordered and zeros == 0 and bad == 0:
            composition_eps = candidate
    if composition_eps is None:
        raise AssertionError("no tested outer epsilon realizes the composition rules")

    B = blowup(S, S, composition_eps)
    print(f"\nUsing the first successful tested outer scale eps={composition_eps}")
    print(f"\nS[Q] with S=Q=T_(4,2): {len(B)} points, general position: {general_position(B)}")
    C, U, W = stats(B)
    print(f"  DIRECT count from orientations only: (C,U,W) = ({C}, {U}, {W})")

    n, r = len(S), len(S)
    Cf = cS * sum(gc.get(j, 0) * n ** (j - 1) for j in range(1, max(gc) + 1))
    Uf = uS * sum(gu.get(j, 0) * n ** (j - 1) for j in range(1, max(gu) + 1))
    Wf = r * wS + cS * uS * sum(gv.get(j, 0) * n ** (j - 2) for j in range(2, max(gv) + 1))
    print(f"  substitution FORMULAS (2.3)-(2.5): (C,U,W) = ({Cf}, {Uf}, {Wf})")
    print(f"  formulas agree with direct count: {(C, U, W) == (Cf, Uf, Wf)}")
    print(f"\n  paper's claimed value (14136, 14136, 441399): "
          f"{(C, U, W) == (14136, 14136, 441399)}")


if __name__ == "__main__":
    main()
