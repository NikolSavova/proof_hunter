#!/usr/bin/env python3
"""Exact verifier for NEARBY_ANCHOR_TANGENT_INTERVAL_ANTIALIGNMENT_GATE.md."""

from fractions import Fraction as F
from itertools import combinations


def det(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    ps = sorted(points)
    if len(ps) <= 1:
        return ps

    lo = []
    for p in ps:
        while len(lo) >= 2 and det(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    hi = []
    for p in reversed(ps):
        while len(hi) >= 2 and det(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    return lo[:-1] + hi[:-1]


def ordinary(points):
    return len(hull(points)) == len(points)


def audit_interval_charging():
    # Proper oriented discrete arcs on a four-cycle.  Every continuous
    # circular interval incidence type has such a finite endpoint model.
    n = 4
    arcs = []
    for start in range(n):
        for length in range(1, n):
            arcs.append((start, frozenset((start + j) % n
                                          for j in range(length))))
    assert len(arcs) == 12

    for first, I in arcs:
        for second, J in arcs:
            if I & J:
                assert first in J or second in I

    # Exhaust all binary weighted subfamilies (repetitions are immaterial:
    # the proof is linear in every nonnegative weight).
    for mask in range(1 << len(arcs)):
        chosen = [arcs[i] for i in range(len(arcs)) if mask >> i & 1]
        W = len(chosen)
        depth = max((sum(x in I for _, I in chosen) for x in range(n)),
                    default=0)
        meeting = sum(bool(I & J) for _, I in chosen for _, J in chosen)
        assert meeting <= 2 * W * depth
    return len(arcs), 1 << len(arcs)


def audit_rational_antialignment(m=14):
    eps = F(1, 100 * m)
    u = (F(0), F(0))
    R = [(F(i), F(i, 10) + eps * i * (m - i))
         for i in range(1, m + 1)]
    s1 = (F(0), F(m * m))
    s2 = (F(-1), F(1))
    S = [s1, s2]
    P = [u] + R + S

    assert all(det(P[i], P[j], P[k]) != 0
               for i, j, k in combinations(range(len(P)), 3))
    assert ordinary([u] + R)
    assert ordinary([u] + S)

    # All child ray slopes lie in [1/10,11/100); the shield interval runs
    # from the vertical direction to slope -1, so the projective intervals
    # are disjoint.  Check the stated rational bounds exactly.
    slopes = [y / x for x, y in R]
    assert min(slopes) == F(1, 10)
    assert max(slopes) < F(11, 100)

    compatible = 0
    child_faces = 0
    for mask in range(1, 1 << m):
        face = [R[i] for i in range(m) if mask >> i & 1]
        assert ordinary([u] + face)
        child_faces += 1
        good = ordinary([u] + face + S)
        assert good == (len(face) == 1)
        compatible += good

        if len(face) >= 2:
            inds = [i + 1 for i in range(m) if mask >> i & 1]
            i, k = inds[0], inds[-1]
            alpha = F(i, k)
            beta = eps * i * (k - i) / (m * m)
            gamma = 1 - alpha - beta
            assert alpha > 0 and beta > 0 and gamma > 0
            lhs = R[i - 1]
            rhs = (alpha * R[k - 1][0] + beta * s1[0] + gamma * u[0],
                   alpha * R[k - 1][1] + beta * s1[1] + gamma * u[1])
            assert lhs == rhs

    assert child_faces == (1 << m) - 1
    assert compatible == m
    return child_faces, compatible


def main():
    arcs, systems = audit_interval_charging()
    faces, compatible = audit_rational_antialignment()
    print("PASS: intervals=%d binary-systems=%d; "
          "rational child-faces=%d shield-compatible=%d"
          % (arcs, systems, faces, compatible))


if __name__ == "__main__":
    main()
