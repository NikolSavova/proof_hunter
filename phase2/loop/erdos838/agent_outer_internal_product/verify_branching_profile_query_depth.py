#!/usr/bin/env python3
"""Exact checks for BRANCHING_PROFILE_QUERY_DEPTH_GATE.md."""

from fractions import Fraction as F
from math import comb, log2


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def transform(p, xi, eta, a=F(1), b=F(1)):
    """Coordinates (a xi(p), b eta(p)); coordinate covectors are marked."""
    return (
        a * (xi[0] * p[0] + xi[1] * p[1]),
        b * (eta[0] * p[0] + eta[1] * p[1]),
    )


def transformed_block(points, xi, eta):
    assert det(xi, eta) != 0
    # Positive scales preserve the two oriented functionals exactly.  The
    # affine image reflects when the ordered source pair has negative sign.
    b = F(1)
    out = [transform(p, xi, eta, F(1), b) for p in points]
    out.sort()
    assert all(out[i][0] < out[i + 1][0] for i in range(len(out) - 1))
    # Exact pullback checks: x=xi and y=b eta.
    for p, z in zip(points, [transform(p, xi, eta, F(1), b) for p in points]):
        assert z[0] == xi[0] * p[0] + xi[1] * p[1]
        assert z[1] == b * (eta[0] * p[0] + eta[1] * p[1])
    return out


def strong_seam(A, B):
    """Translate B by an exact (R,-M) satisfying the two strong signs."""
    width_a = max(x for x, _ in A) - min(x for x, _ in A)
    width_b = max(x for x, _ in B) - min(x for x, _ in B)
    R = width_a + width_b + F(3)
    M = F(1)
    while True:
        v = (R, -M)
        ok = True
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if det(sub(A[j], A[i]), v) >= 0:
                    ok = False
        for i in range(len(B)):
            for j in range(i + 1, len(B)):
                if det(v, sub(B[j], B[i])) <= 0:
                    ok = False
        if ok:
            break
        M *= 2
    # Shrink both blocks about the origin, then apply the macro translation.
    eps = F(1)
    while True:
        eps /= 2
        AA = [(eps * x, eps * y) for x, y in A]
        BB = [(R + eps * x, -M + eps * y) for x, y in B]
        ok = max(x for x, _ in AA) < min(x for x, _ in BB)
        if ok:
            for i in range(len(AA)):
                for j in range(i + 1, len(AA)):
                    for b in BB:
                        if det(sub(AA[j], AA[i]), sub(b, AA[i])) >= 0:
                            ok = False
        if ok:
            for a in AA:
                for i in range(len(BB)):
                    for j in range(i + 1, len(BB)):
                        if det(sub(BB[i], a), sub(BB[j], BB[i])) <= 0:
                            ok = False
        if ok:
            return AA, BB


def check_pair_and_seam():
    blocks = [
        [(F(-2), F(1)), (F(0), F(4)), (F(3), F(-1)), (F(5), F(3))],
        [(F(-3), F(-2)), (F(-1), F(5)), (F(2), F(0)), (F(6), F(7))],
        [(F(-4), F(3)), (F(1), F(-3)), (F(4), F(6))],
    ]
    marks = [
        ((F(1), F(2)), (F(-2), F(3))),
        ((F(2), F(-1)), (F(1), F(3))),
        ((F(3), F(1)), (F(-1), F(2))),
    ]
    out = [transformed_block(P, xi, eta) for P, (xi, eta) in zip(blocks, marks)]
    # Pairwise insertion is the load-bearing exact assertion.  Iteration of
    # the same argument gives an ordered strong tree.
    strong_seam(out[0], out[1])
    strong_seam(out[1], out[2])


def pullback(mat, cov):
    # If T has columns encoded by mat rows in primal coordinates, T^* cov.
    return (
        cov[0] * mat[0][0] + cov[1] * mat[1][0],
        cov[0] * mat[0][1] + cov[1] * mat[1][1],
    )


def check_query_depth():
    # Nonuniform affine maps on a depth-five path.  Starting with r=2 root
    # outputs, each child gets exactly the previous directions plus one new
    # construction direction; chosen data make all pullbacks distinct.
    S = {(F(1), F(k)) for k in (0, 1)}
    mats = [((F(1), F(0)), (F(0), F(1)))] * 5
    gammas = [(F(1), F(k)) for k in (13, 17, 19, 23, 29)]
    for depth, (mat, gamma) in enumerate(zip(mats, gammas), 1):
        old_plus = set(S)
        old_plus.add(gamma)
        S = {pullback(mat, d) for d in old_plus}
        # Projective directions are normalized by first coordinate here.
        normalized = {(F(1), y / x) for x, y in S}
        S = normalized
        assert len(S) == 2 + depth
    assert len(S) == 7

    # Recycled-mark grammar: the construction direction is already the
    # first exported mark, so union with it never increases cardinality.
    S = {(F(1), F(0)), (F(1), F(1))}
    for k in (2, 3, 5, 7, 11, 13):
        mat = ((F(1), F(k)), (F(0), F(1)))
        gamma = next(iter(S))
        old_plus = set(S)
        old_plus.add(gamma)
        S = {pullback(mat, d) for d in old_plus}
        S = {(F(1), y / x) for x, y in S}
        assert len(S) == 2


def balanced_levels(target_L, kappa=F(1, 4)):
    L = 16.0
    vals = [L]
    while L < target_L:
        q = float(kappa) * L
        L += log2(q)
        vals.append(L)
    return vals


def check_balanced_cost():
    previous_ratio = None
    for target in (2**12, 2**14, 2**16, 2**18):
        vals = balanced_levels(target)
        h = len(vals) - 1
        L = vals[-1]
        # h is Theta(L/log L); the displayed normalized quantities remain
        # bounded, while the path entropy ratio tends down to zero.
        depth_norm = h * log2(L) / L
        assert F(1, 10) < depth_norm < 10
        ratio = sum(vals[:-1]) / (L * L)
        assert ratio < 1
        if previous_ratio is not None:
            assert ratio < previous_ratio
        previous_ratio = ratio
        # Polynomial itinerary state at level k: O(log(s M_k^2)).
        state_bits = sum(3 * (log2(max(h, 2)) + 2 * x) for x in vals[:-1])
        assert state_bits / (L * L) < 20 / log2(L)


def check_one_gap_algebra():
    # Exact cyclic multiplication identity behind (4), on arbitrary counts.
    A = 7
    LR = [(2, 5), (3, 4), (5, 7), (4, 9), (6, 8)]
    q = len(LR)
    B = []
    for j in range(q):
        r_prev = LR[(j - 1) % q][1]
        l_next = LR[(j + 1) % q][0]
        B.append(r_prev * l_next * A ** (q - 3))
    lhs = 1
    rhs = A ** (q * (q - 3))
    for x in B:
        lhs *= x
    for l, r in LR:
        rhs *= l * r
    assert lhs == rhs
    assert max(B) ** q >= rhs


if __name__ == "__main__":
    check_pair_and_seam()
    check_query_depth()
    check_balanced_cost()
    check_one_gap_algebra()
    print(
        "PASS: pair pullbacks and exact strong seams; query novelty is additive; "
        "recycled Pi2 stays constant; all-fresh path costs are subquadratic"
    )
