#!/usr/bin/env python3
"""Exact checks for CONTINUUM_PROFILE_COHERENCE_GATE.md."""

from fractions import Fraction as Q
from itertools import combinations, permutations, product


def scalar_checks():
    # Perfect exponent ramp: every forward term has exponent q-1.
    for q in range(3, 25):
        a = list(range(q))
        b = [q - x for x in a]
        for i in range(q):
            for j in range(i + 1, q):
                assert a[i] + b[j] + (j - i - 1) == q - 1

    # Reset pinning in the integer error model.  If
    # a<=s+e, b<=q-s+e, and a+b>=q-e, then
    # a>=s-2e and b>=q-s-2e.
    for q in range(3, 25):
        for e in range(4):
            for s in range(q + 1):
                for a in range(2 * q + 1):
                    for b in range(2 * q + 1):
                        if (a <= s + e and b <= q - s + e
                                and a + b >= q - e):
                            assert a >= s - 2 * e
                            assert b >= q - s - 2 * e

    # If every child has a+b>=q-e and the assembly cap width is at most r,
    # the endpoint term is at least 2q-e-r-2 in the D+1 >= D model.
    for q in range(3, 25):
        for e in range(4):
            for r in range(q + 1):
                for a_first in range(2 * q + 1):
                    for a_last in range(max(0, a_first - r),
                                        min(2 * q, a_first + r) + 1):
                        b_last = max(0, q - e - a_last)
                        endpoint = a_first + b_last + q - 2
                        assert endpoint >= 2 * q - e - r - 2


RAW_SEEDS = (
    ((0, -4), (1, -3), (2, -3), (7, -4)),
    ((0, -4), (1, -3), (2, -3), (7, -2)),
    ((0, -4), (1, -3), (2, -4), (7, -3)),
    ((0, -4), (1, -3), (2, -4), (7, 4)),
    ((0, -4), (1, -3), (2, -1), (7, -4)),
    ((0, -4), (1, -4), (2, -3), (7, -3)),
    ((0, -4), (1, -4), (2, -3), (7, 0)),
    ((0, -4), (1, -4), (2, -3), (7, 3)),
)


def det(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def chain_counts(points, order):
    """Cap/cup counts including the empty chain."""
    n = len(points)
    cap = [[0] * n for _ in range(n)]
    cup = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            cap[i][j] = cup[i][j] = 1
            for h in range(i):
                if det(points[order[h]], points[order[i]], points[order[j]]) < 0:
                    cap[i][j] += cap[h][i]
                else:
                    cup[i][j] += cup[h][i]
    return 1 + n + sum(map(sum, cap)), 1 + n + sum(map(sum, cup))


def adjacent_swap_checks():
    # The theorem is general; the complete rooted four-point menu is a
    # compact independent exact stress test of every order and swap.
    for raw in RAW_SEEDS:
        points = tuple((Q(x), Q(y)) for x, y in raw)
        assert all(det(*triple) for triple in combinations(points, 3))
        for order in permutations(range(4)):
            c0, u0 = chain_counts(points, order)
            for k in range(3):
                swapped = list(order)
                swapped[k], swapped[k + 1] = swapped[k + 1], swapped[k]
                c1, u1 = chain_counts(points, tuple(swapped))
                assert c0 <= 2 * c1 and c1 <= 2 * c0
                assert u0 <= 2 * u1 and u1 <= 2 * u0


def cross_ratio(values):
    a, b, c, d = values
    return (c - a) * (d - b) / ((d - a) * (c - b))


def cross_ratio_checks():
    source = (Q(0), Q(1), Q(2), Q(3))
    assert cross_ratio(source) == Q(4, 3)

    epsilon = Q(1, 100)
    intervals = ((-epsilon, epsilon),
                 (1 - epsilon, 1 + epsilon),
                 (2 - epsilon, 2 + epsilon),
                 (4 - epsilon, 4 + epsilon))
    corners = [cross_ratio(values) for values in product(*intervals)]
    assert min(corners) == Q(5000, 3383)
    assert max(corners) == Q(5000, 3283)
    assert not (min(corners) <= Q(4, 3) <= max(corners))

    # Every target-center triple has the same cyclic order as the
    # corresponding source triple.  PGL_2 is sharply triply transitive on
    # ordered triples of RP^1, so every three-coordinate request is feasible.
    centers = (Q(0), Q(1), Q(2), Q(4))
    for indices in combinations(range(4), 3):
        source_triple = tuple(source[i] for i in indices)
        target_triple = tuple(centers[i] for i in indices)
        assert source_triple[0] < source_triple[1] < source_triple[2]
        assert target_triple[0] < target_triple[1] < target_triple[2]


def main():
    scalar_checks()
    adjacent_swap_checks()
    cross_ratio_checks()
    print("PASS: scalar ramp width, reset pinning, adjacent-swap factor two, "
          "and four-direction cross-ratio obstruction verified")


if __name__ == "__main__":
    main()
