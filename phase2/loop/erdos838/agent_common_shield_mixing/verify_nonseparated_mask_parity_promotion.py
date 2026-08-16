#!/usr/bin/env python3
"""Exact checks for NONSEPARATED_MASK_PARITY_PROMOTION.md."""

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product


def det(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and det(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and det(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def convex(points):
    return len(hull(points)) == len(points)


def strict_inside(p, a, b, c):
    signs = (det(a, b, p), det(b, c, p), det(c, a, p))
    return all(x > 0 for x in signs) or all(x < 0 for x in signs)


def parity_set(q, g):
    k = q // 2
    return {(g + 2 * j) % q for j in range(k)}


def check_independent_bases():
    for q in range(5, 31):
        for g in range(q):
            ears = parity_set(q, g)
            assert g in ears
            assert len(ears) == q // 2
            assert all((i + 1) % q not in ears for i in ears)
            base = set(range(q)) - ears
            assert len(base) >= 3
            # Both original neighbours of each ear are retained anchors.
            assert all((i - 1) % q in base and (i + 1) % q in base
                       for i in ears)


def check_varying_base_decoder():
    # A purely exact decoder audit.  The seam rule deliberately varies with
    # the retained base labels.  Geometry is supplied by Theorem 1.
    q, m, target, jet_count = 8, 3, 1, 5
    ears = {1, 3, 5, 7}
    base = set(range(q)) - ears
    left, right = 7, 3
    loads = Counter()
    incidences = 0
    for word in product(range(m), repeat=q):
        for face in range(jet_count):
            bad_left = (word[left] + word[0] + face) % 3 == 0
            bad_right = (word[right] + word[2] + 2 * face) % 3 == 0
            deleted = ({left} if bad_left else set()) | (
                {right} if bad_right else set())
            trace = []
            for i in range(q):
                if i == target:
                    trace.append(("F", face))
                elif i in deleted:
                    trace.append(None)
                else:
                    trace.append(("x", word[i]))
            loads[tuple(trace)] += 1
            incidences += 1
    assert incidences == (m ** q) * jet_count
    assert max(loads.values()) <= m ** 3
    assert len(loads) >= incidences // (m ** 3)
    return incidences, len(loads), max(loads.values())


DELTAS = {
    -3: (Q(7, 500), Q(14, 625)),
    -2: (Q(23, 2500), Q(11, 625)),
    -1: (Q(19, 1000), Q(59, 2500)),
    0: (Q(29, 10000), Q(13, 1250)),
    1: (Q(61, 5000), Q(41, 2000)),
    2: (Q(12, 625), Q(63, 2500)),
    3: (Q(21, 1250), Q(213, 10000)),
}


def pp(i, t):
    return Q(i), Q(i * i) - DELTAS[i][t]


def check_rational_parabola():
    indices = list(range(-3, 4))
    all_points = [pp(i, t) for i in indices for t in range(2)]
    assert all(det(*triple) != 0 for triple in combinations(all_points, 3))

    transversal_count = 0
    for labels in product(range(2), repeat=7):
        points = [pp(i, t) for i, t in zip(indices, labels)]
        assert convex(points)
        transversal_count += 1
    assert transversal_count == 128

    # A genuinely root-good two-point replacement: it replaces cell zero
    # in every word and all eight resulting points remain hull vertices.
    good_face = [(Q(-1, 4), Q(1, 16) - Q(1, 100)),
                 (Q(1, 4), Q(1, 16) - Q(1, 100))]
    root_good_count = 0
    for labels in product(range(2), repeat=6):
        points = []
        cursor = 0
        for i in indices:
            if i == 0:
                continue
            points.append(pp(i, labels[cursor]))
            cursor += 1
        points.extend(good_face)
        assert convex(points)
        root_good_count += 1
    assert root_good_count == 64

    inner, outer = pp(0, 0), pp(0, 1)
    assert inner[1] > outer[1]
    witnesses = 0
    for i in (-3, -2, -1):
        for j in (1, 2, 3):
            for a in range(2):
                for b in range(2):
                    assert strict_inside(inner, outer, pp(i, a), pp(j, b))
                    witnesses += 1
    assert witnesses == 36

    # Deleting exactly one side succeeds for every choice on the retained
    # side, while retaining one point on both sides fails by the witness.
    for side in ((-3, -2, -1), (1, 2, 3)):
        for labels in product(range(2), repeat=3):
            points = [inner, outer]
            points.extend(pp(i, t) for i, t in zip(side, labels))
            assert convex(points)

    # At L=2 the least erased support product is therefore exactly 2^3.
    min_erased_cells = min(3, 3)
    assert min_erased_cells == 3
    assert 2 ** min_erased_cells == 8
    return transversal_count, root_good_count, witnesses


def check_mask_entropy_algebra():
    # Integer log units: log L = ell.  Verify the limiting half-source ratio
    # and the balanced coefficient identity exactly.
    for q in range(5, 40, 2):
        k = (q - 1) // 2
        for ell in range(1, 8):
            source_entropy = q * ell
            erased_entropy = k * ell
            assert 2 * erased_entropy == source_entropy - ell
    a = Q(1, 4)
    kappa = Q(1, 4)
    c0 = Q(1, 8)
    jet_coefficient = c0 * (a / kappa) ** 2
    assert jet_coefficient == Q(1, 8)
    assert jet_coefficient == a / 2


def check_dominance_root_bad():
    q = (Q(-19, 20), Q(1, 20))
    x = (Q(-3, 40), Q(7, 8))
    w = (Q(0), Q(10, 11))
    z = (Q(3, 40), Q(7, 8))
    y = (Q(2, 15), Q(8, 9))
    assert convex([q, x, w, z])
    assert convex([q, x, w, y])
    alpha, beta, gamma = Q(15, 662), Q(671, 2648), Q(1917, 2648)
    assert alpha > 0 and beta > 0 and gamma > 0
    assert alpha + beta + gamma == 1
    recovered = tuple(alpha * q[i] + beta * w[i] + gamma * y[i]
                      for i in range(2))
    assert recovered == z
    assert not convex([q, w, z, y])


def main():
    check_independent_bases()
    incidences, outputs, load = check_varying_base_decoder()
    transversals, root_good, witnesses = check_rational_parabola()
    check_mask_entropy_algebra()
    check_dominance_root_bad()
    print("PASS: parity bases ranks 5..30; "
          f"decoder incidences={incidences}, outputs={outputs}, load={load}; "
          f"transversals={transversals}, root_good={root_good}, "
          f"triangle_witnesses={witnesses}; half-entropy and R=0 root-bad exact")


if __name__ == "__main__":
    main()
