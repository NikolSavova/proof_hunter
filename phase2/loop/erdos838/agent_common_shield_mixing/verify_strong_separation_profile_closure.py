#!/usr/bin/env python3
"""Exact checks for STRONG_SEPARATION_PROFILE_CLOSURE.md."""

from fractions import Fraction as Q
from itertools import combinations
from math import prod


def det(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
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
    return len(set(points)) == len(hull(points))


def point(m, t):
    delta = Q(1, 100 * m * m)
    return Q(2) - delta * t * t, -Q(1, 5) + delta * t


A = (Q(0), Q(0))
B = (Q(4), Q(0))
C = (Q(0), Q(4))


def check_same_type_and_local_faces(m):
    delta = Q(1, 100 * m * m)
    cluster = [point(m, t) for t in range(1, m + 1)]
    for p in cluster:
        signs = tuple(det(*triple) > 0 for triple in (
            (p, B, C), (p, B, A), (p, C, A), (B, C, A)))
        assert signs == (True,) * 4
        assert convex([p, B, C, A])

    assert convex(cluster)
    assert all(det(*triple) != 0 for triple in combinations(cluster, 3))
    assert max(p[0] for p in cluster) - min(p[0] for p in cluster) < Q(1, 100)
    assert max(p[1] for p in cluster) - min(p[1] for p in cluster) < Q(1, 100 * m)

    for t, p in enumerate(cluster, 1):
        assert det(p, B, C) == Q(44, 5) + 4 * delta * (t * t - t)
        assert det(p, B, A) == Q(4, 5) - 4 * delta * t
        assert det(p, C, A) == 8 - 4 * delta * t * t
        assert det(B, C, A) == 16
    return cluster


def check_barycentric_blocking(m, cluster):
    delta = Q(1, 100 * m * m)
    triples = 0
    for i, j, k in combinations(range(1, m + 1), 3):
        pi, pj, pk = cluster[i - 1], cluster[j - 1], cluster[k - 1]
        denominator = det(pi, pk, C)
        n_i = det(pj, pk, C)
        n_k = det(pi, pj, C)
        n_c = det(pi, pk, pj)
        assert denominator == delta * (k - i) * (
            2 - Q(21, 5) * (i + k) + delta * i * k)
        assert n_i == delta * (k - j) * (
            2 - Q(21, 5) * (j + k) + delta * j * k)
        assert n_k == delta * (j - i) * (
            2 - Q(21, 5) * (i + j) + delta * i * j)
        assert n_c == delta * delta * (k - i) * (j - i) * (j - k)
        assert denominator < 0 and n_i < 0 and n_k < 0 and n_c < 0
        assert n_i + n_k + n_c == denominator
        weights = (n_i / denominator, n_k / denominator, n_c / denominator)
        assert all(w > 0 for w in weights) and sum(weights) == 1
        assert pj == tuple(weights[0] * pi[z] + weights[1] * pk[z]
                           + weights[2] * C[z] for z in range(2))
        assert not convex([pi, pj, pk, C])
        assert not convex([pi, pj, pk, C, A])
        assert not convex([pi, pj, pk, B, C])
        triples += 1
    assert triples == m * (m - 1) * (m - 2) // 6
    return triples


def check_capacity_failure():
    first = None
    for m in range(1, 81):
        endpoint = m + m * (m - 1) // 2
        local_faces = 2 ** m - 1
        if endpoint * endpoint < local_faces and first is None:
            first = m
        if m >= 14:
            assert endpoint * endpoint < local_faces
    assert first == 14
    assert (14 + 14 * 13 // 2) ** 2 == 11025
    assert 2 ** 14 - 1 == 16383


def check_conditional_identities():
    lengths = [3, 5, 7, 11, 13]
    left = [2, 4, 3, 5, 6]
    right = [7, 3, 8, 2, 9]
    q = len(lengths)
    p0 = prod(lengths)
    banks = []
    for j in range(q):
        value = right[(j - 1) % q] * left[(j + 1) % q]
        for i in range(q):
            if i not in ((j - 1) % q, j, (j + 1) % q):
                value *= lengths[i]
        banks.append(value)
    assert Q(prod(banks), p0 ** q) == Q(
        prod(left[i] * right[i] for i in range(q)),
        prod(lengths[i] ** 3 for i in range(q)))

    a = kappa = local = Q(1, 4)
    assert a + local * (a / kappa) ** 2 == Q(1, 2)


def main():
    m = 14
    cluster = check_same_type_and_local_faces(m)
    triples = check_barycentric_blocking(m, cluster)
    check_capacity_failure()
    check_conditional_identities()
    endpoint = m + m * (m - 1) // 2
    print("PASS: "
          f"m={m}, transversals={m}, blocked triples={triples}; "
          f"endpoint cap={endpoint}, square={endpoint ** 2} "
          f"< local faces={2 ** m - 1}; first failure m=14; "
          "conditional cyclic coefficient=1/2")


if __name__ == "__main__":
    main()
