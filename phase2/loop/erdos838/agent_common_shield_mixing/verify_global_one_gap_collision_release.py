#!/usr/bin/env python3
"""Exact finite checks for GLOBAL_ONE_GAP_COLLISION_RELEASE.md.

Only integer/Fraction predicates are used.  The script checks:
  * the same-pocket dominance test on a rational general-position model;
  * source recovery for tagged two-extension faces;
  * circuit-transversal release exhaustively on the wrapper configuration;
  * the cross-symmetric-difference circuit lemma;
  * the unit and weighted collision quadratics by finite enumeration; and
  * every assertion and face count in the outer-triangle barrier.
"""

from fractions import Fraction as F
from itertools import combinations, product
from math import ceil, comb


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def strict_inside_triangle(p, a, b, c):
    signs = (orient(a, b, p), orient(b, c, p), orient(c, a, p))
    return all(x > 0 for x in signs) or all(x < 0 for x in signs)


def is_face(indices, points):
    """Convex position, via planar Caratheodory (ambient set is GP)."""
    indices = tuple(indices)
    if len(indices) < 4:
        return True
    for p in indices:
        others = [x for x in indices if x != p]
        for a, b, c in combinations(others, 3):
            if strict_inside_triangle(points[p], points[a], points[b], points[c]):
                return False
    return True


def all_faces(points):
    ans = []
    for r in range(len(points) + 1):
        ans.extend(S for S in combinations(range(len(points)), r) if is_face(S, points))
    return ans


def general_position(points):
    return all(orient(points[a], points[b], points[c]) != 0
               for a, b, c in combinations(range(len(points)), 3))


def check_same_pocket():
    # u=(-1,0), v=(1,0); (L,R) maps to ((L-R)/(L+R),-2/(L+R)).
    triangle = [(F(-1), F(0)), (F(1), F(0)), (F(0), F(5))]
    lr = [(2, 3), (4, 7), (8, 9), (9, 2),
          (3, 10), (7, 5), (11, 6), (5, 13)]
    labels = [(F(L - R, L + R), F(-2, L + R)) for L, R in lr]
    points = triangle + labels
    assert general_position(points)

    Q = (0, 1, 2)
    for i in range(len(labels)):
        assert is_face(Q + (3 + i,), points)

    comparable = {}
    for i, j in combinations(range(len(labels)), 2):
        comp = (lr[i][0] - lr[j][0]) * (lr[i][1] - lr[j][1]) > 0
        comparable[i, j] = comp
        assert is_face(Q + (3 + i, 3 + j), points) == (not comp)

    def pair_comp(i, j):
        if i > j:
            i, j = j, i
        return comparable[i, j]

    height = width = 1
    best_antichain = None
    for mask in range(1, 1 << len(labels)):
        S = [i for i in range(len(labels)) if mask >> i & 1]
        if all(pair_comp(i, j) for i, j in combinations(S, 2)):
            height = max(height, len(S))
        if all(not pair_comp(i, j) for i, j in combinations(S, 2)):
            if len(S) > width:
                width, best_antichain = len(S), tuple(S)
    assert height * width >= len(labels)
    assert best_antichain is not None
    antichain_faces = {
        tuple(sorted(Q + (3 + i, 3 + j)))
        for i, j in combinations(best_antichain, 2)
    }
    assert len(antichain_faces) == comb(width, 2)
    assert all(is_face(S, points) for S in antichain_faces)
    return len(labels), height, width, len(antichain_faces)


def check_tagged_decoder():
    # Pure labelled-set check: an output of rank q+2 has at most C(q+2,2)
    # possible q-source traces, obtained by deleting a pair.
    universe = range(8)
    q = 3
    fibres = {}
    for Q in combinations(universe, q):
        outside = [x for x in universe if x not in Q]
        for y, z in combinations(outside, 2):
            W = tuple(sorted(Q + (y, z)))
            fibres.setdefault(W, set()).add(Q)
    max_load = max(map(len, fibres.values()))
    assert max_load <= comb(q + 2, 2)
    return len(fibres), max_load


def trace_clutter(U, B, points):
    support = tuple(sorted(set(U) | set(B)))
    traces = set()
    for C in combinations(support, 4):
        if not is_face(C, points):
            trace = frozenset(set(C) & set(B))
            if trace:
                traces.add(trace)
    return traces


def check_release_exhaustively(points):
    faces = all_faces(points)
    checked = 0
    for U in faces:
        if len(U) > 3:
            continue
        for B in faces:
            if len(B) > 4 or set(U) & set(B):
                continue
            traces = trace_clutter(U, B, points)
            for r in range(len(B) + 1):
                for G in combinations(B, r):
                    if all(set(G) & set(T) for T in traces):
                        released = tuple(sorted(set(U) | (set(B) - set(G))))
                        assert is_face(released, points)
                        checked += 1
    return checked


def check_cross_circuit():
    # y is strictly inside triangle u,v,z.
    points = [(F(-1), F(0)), (F(1), F(0)),
              (F(0), F(-2)), (F(0), F(-1))]
    U, R1, R2 = (0, 1), (2,), (3,)
    assert general_position(points)
    assert is_face(U + R1, points) and is_face(U + R2, points)
    whole = tuple(sorted(U + R1 + R2))
    assert not is_face(whole, points)
    bad = [C for C in combinations(whole, 4) if not is_face(C, points)]
    assert bad
    for C in bad:
        assert set(C) & (set(R1) - set(R2))
        assert set(C) & (set(R2) - set(R1))
    return len(bad)


def check_collision_quadratics():
    unit_tests = 0
    weighted_tests = 0
    thetas = (F(1), F(1, 2), F(1, 3))

    # Unit occurrences.  K is the full same-U collision count.  Enumerate
    # arbitrary retained good mass G satisfying the theorem's hypotheses.
    for V in range(1, 8):
        for m in range(1, min(V, 5) + 1):
            for degrees in product(range(5), repeat=m):
                N = sum(degrees)
                if N == 0:
                    continue
                K = sum(comb(d, 2) for d in degrees)
                for G in range(K + 1):
                    L = ceil(F(G, V))
                    for theta in thetas:
                        for beta in range(3):
                            if F(G) < theta * K - beta * N:
                                continue
                            assert G <= L * V
                            x = F(N, V)
                            a = F(1) + F(2 * beta, 1) / theta
                            assert x * x - a * x - F(2 * L, 1) / theta <= 0
                            unit_tests += 1

    # Genuine weighted all-good instances.  Delta <= alpha W with
    # alpha=max_i w_i, and the same quadratic follows exactly.
    for V in range(1, 7):
        for m in range(1, min(V, 4) + 1):
            for weights in product((F(0), F(1), F(2), F(3, 2)), repeat=m):
                W = sum(weights, F(0))
                if W == 0:
                    continue
                delta = sum((w * w for w in weights), F(0))
                K = (sum((w * w for w in weights), F(0)) - delta) / 2
                # One occurrence per U gives K=0; instead make each listed
                # weight a two-occurrence fibre split equally.
                fibre_sums = weights
                individual = [w / 2 for w in weights for _ in range(2)]
                delta = sum((w * w for w in individual), F(0))
                K = (sum((s * s for s in fibre_sums), F(0)) - delta) / 2
                alpha = max(individual)
                assert delta <= alpha * W
                L = ceil(K / V)
                x = W / V
                assert x * x - alpha * x - 2 * L <= 0
                weighted_tests += 1
    return unit_tests, weighted_tests


def check_outer_triangle():
    X = [(F(-4), F(-4)), (F(4), F(-4)), (F(4), F(4)),
         (F(-4), F(4)), (F(0), F(1))]
    U = [(F(-23), F(-19)), (F(21), F(-17)), (F(2), F(31))]
    P = X + U
    assert general_position(P)

    # Strict containment in the consistently oriented triangle U.
    assert orient(U[0], U[1], U[2]) > 0
    assert all(all(orient(U[j], U[(j + 1) % 3], x) > 0 for j in range(3))
               for x in X)

    faces_X = all_faces(X)
    faces_P = all_faces(P)
    counts_X = [sum(len(S) == r for S in faces_X) for r in range(6)]
    counts_P = [sum(len(S) == r for S in faces_P) for r in range(9)]
    assert counts_X == [1, 5, 10, 10, 3, 0]
    assert counts_P == [1, 8, 28, 56, 32, 1, 0, 0, 0]
    assert len(faces_X) == 29 and len(faces_P) == 126
    assert len(faces_P) <= 8 * len(faces_X)

    q = max(map(len, faces_X))
    bases = [B for B in faces_X if len(B) == q]
    assert q == 4 and len(bases) == 3
    outer = (5, 6, 7)
    assert is_face(outer, P)
    for B in bases:
        assert not is_face(tuple(sorted(outer + B)), P)
        traces = trace_clutter(outer, B, P)
        assert all(frozenset((x,)) in traces for x in B)
        # Hence the only hitting set is the whole base.
        hitting = []
        for r in range(len(B) + 1):
            for G in combinations(B, r):
                if all(set(G) & set(T) for T in traces):
                    hitting.append(G)
        assert hitting == [B]

    for B, C in combinations(bases, 2):
        assert not is_face(tuple(sorted(set(B) | set(C))), X)

    # Restriction is injective and every X trace is an X-face.
    codes = [(tuple(x for x in S if x < 5), tuple(x for x in S if x >= 5))
             for S in faces_P]
    assert len(codes) == len(set(codes))
    face_X_set = set(faces_X)
    assert all(code[0] in face_X_set for code in codes)

    # Each x gives a 3+1 circuit crossing the two containers, so their
    # two-vertex circuit graph is connected.
    assert all(not is_face(tuple(sorted(outer + (x,))), P) for x in range(5))
    return counts_X, counts_P, len(bases)


def main():
    pocket = check_same_pocket()
    decoder = check_tagged_decoder()
    cross = check_cross_circuit()
    unit, weighted = check_collision_quadratics()
    counts_X, counts_P, bases = check_outer_triangle()
    wrapper = [(F(-4), F(-4)), (F(4), F(-4)), (F(4), F(4)),
               (F(-4), F(4)), (F(0), F(1)),
               (F(-23), F(-19)), (F(21), F(-17)), (F(2), F(31))]
    releases = check_release_exhaustively(wrapper)
    print(
        "global one-gap collision: PASS; "
        f"pocket(m,height,width,pairs)={pocket}; "
        f"decoder(outputs,maxload)={decoder}; cross={cross}; "
        f"quadratics(unit,weighted)=({unit},{weighted}); "
        f"release_checks={releases}; X={counts_X} P={counts_P} bases={bases}"
    )


if __name__ == "__main__":
    main()

