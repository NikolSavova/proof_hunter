#!/usr/bin/env python3
"""Exact verifier for FIXED_CARRIER_THREE_EAR_COLLAPSE_AND_NESTED_CAGE."""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations


def det(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull_indices(points):
    order = sorted(range(len(points)), key=lambda i: points[i])
    if len(order) <= 1:
        return order

    lo = []
    for i in order:
        while len(lo) >= 2 and det(points[lo[-2]], points[lo[-1]],
                                   points[i]) <= 0:
            lo.pop()
        lo.append(i)
    hi = []
    for i in reversed(order):
        while len(hi) >= 2 and det(points[hi[-2]], points[hi[-1]],
                                   points[i]) <= 0:
            hi.pop()
        hi.append(i)
    return lo[:-1] + hi[:-1]


def ordinary(points):
    return len(hull_indices(points)) == len(points)


def boundary_edge(points, a, b):
    h = hull_indices(points)
    ia, ib = points.index(a), points.index(b)
    return any({h[j], h[(j + 1) % len(h)]} == {ia, ib}
               for j in range(len(h)))


def inserted_through(points, p, u, v):
    h = hull_indices(points + [p])
    ip = len(points)
    j = h.index(ip)
    return {h[(j - 1) % len(h)], h[(j + 1) % len(h)]} == {
        points.index(u), points.index(v)
    }


def general_position(points):
    return all(det(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))


def audit_nine_point_scope():
    sources = [{0, 1, 6}, {0, 1, 7}, {1, 3, 8}]
    repair_edges = [{6, 1}, {7, 1}, {3, 8}]
    common = set.intersection(*sources)
    assert common == {1}
    assert not any(edge <= common for edge in repair_edges)
    return len(common)


def audit_nested_cage(q=14):
    delta = F(1, 100 * q * q)
    u, v, w = (F(-2), F(0)), (F(2), F(0)), (F(0), F(6))
    B = [u, v, w]
    z = (F(0), F(1))
    p = (F(0), -F(1, 100 * q))
    m, n, d = (F(1), F(3)), (F(3), F(1)), (F(-2), F(6))
    A = [(m[0] + t * n[0] + delta * t * t * d[0],
          m[1] + t * n[1] + delta * t * t * d[1])
         for t in range(1, q + 1)]

    old, new = B + [z] + A, B + [p] + A
    assert general_position(old)
    assert general_position(new)
    assert ordinary(B)
    assert not ordinary(B + [z])

    for a in A:
        R = B + [a]
        assert ordinary(R)
        assert boundary_edge(R, u, v)
        assert not ordinary(R + [z])
        assert ordinary(R + [p])
        assert inserted_through(R, p, u, v)

    bad_pairs = 0
    for s, t in combinations(range(q), 2):
        assert not ordinary(B + [A[s], A[t]])
        bad_pairs += 1

        # Equation (10), with mathematical indices s+1,t+1.
        si, ti = s + 1, t + 1
        lam = F(si, ti)
        bst = (m[0] - delta * si * ti * d[0],
               m[1] - delta * si * ti * d[1])
        assert F(-1, 2) < -delta * si * ti < F(1, 2)
        rhs = (lam * A[t][0] + (1 - lam) * bst[0],
               lam * A[t][1] + (1 - lam) * bst[1])
        assert rhs == A[s]

    def carrier_ledger(anchor):
        faces = []
        extras = [anchor] + A
        for mask in range(1 << len(extras)):
            face = B + [extras[i] for i in range(len(extras))
                        if mask >> i & 1]
            if ordinary(face):
                faces.append(frozenset(face))
        return faces

    old_faces = carrier_ledger(z)
    new_faces = carrier_ledger(p)
    assert len(old_faces) == q + 1
    assert len(new_faces) == 2 * q + 2

    common_load = q  # Every history routed to the same B+p.
    full_outputs = Counter(frozenset(B + [p, A[t]]) for t in range(q))
    assert max(full_outputs.values()) == 1
    two_face = Counter(
        (frozenset(B + [A[s]]), frozenset(B + [A[t]]))
        for s in range(q) for t in range(q) if s != t
    )
    assert max(two_face.values()) == 1
    assert len(two_face) == q * (q - 1)

    # The variable labels form their own convex-position bank, so even
    # perfect common-edge localization has exponentially small dilution.
    assert ordinary(A)
    ambient_lower = (1 << q) - 1
    p_support = q + len(B)
    assert q * p_support < ambient_lower  # q/(2^q-1) < 1/p.

    return (len(old_faces), len(new_faces), bad_pairs,
            common_load, max(full_outputs.values()), max(two_face.values()),
            ambient_lower)


def main():
    common = audit_nine_point_scope()
    (old, new, pairs, common_load, full_load, two_load,
     ambient_lower) = audit_nested_cage()
    print(
        "PASS: n9-common=%d; q14 carrier-ledgers=%d/%d bad-pairs=%d "
        "loads(common/full/two-face)=%d/%d/%d ambient-bank>=%d"
        % (common, old, new, pairs, common_load, full_load, two_load,
           ambient_lower)
    )


if __name__ == "__main__":
    main()
