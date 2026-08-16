#!/usr/bin/env python3
"""Exact audit for MINIMIZER_CIRCUIT_CODEGREE_DICHOTOMY.md."""

from fractions import Fraction as F
from itertools import combinations


def cross(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull_indices(points):
    order = sorted(range(len(points)), key=lambda i: points[i])
    if len(order) <= 1:
        return order
    lower = []
    for i in order:
        while (len(lower) >= 2
               and cross(points[lower[-2]], points[lower[-1]], points[i]) <= 0):
            lower.pop()
        lower.append(i)
    upper = []
    for i in reversed(order):
        while (len(upper) >= 2
               and cross(points[upper[-2]], points[upper[-1]], points[i]) <= 0):
            upper.pop()
        upper.append(i)
    return lower[:-1] + upper[:-1]


def convex(points):
    return len(set(points)) == len(points) == len(hull_indices(points))


def canonical_triples(face, points):
    if len(face) <= 2:
        return set()
    local_points = [points[i] for i in face]
    cyclic = [face[i] for i in hull_indices(local_points)]
    h = len(cyclic)
    assert h == len(face)
    triples = set()
    for i in range(h):
        for j in range(h):
            if j not in (i, (i + 1) % h):
                triples.add(tuple(sorted((cyclic[i], cyclic[(i + 1) % h],
                                          cyclic[j]))))
    assert len(triples) <= h * (h - 2)
    return triples


def audit(points, expected_v, expected_moment, expected_rank):
    n = len(points)
    assert all(cross(*triple) != 0 for triple in combinations(points, 3))
    degree = {}
    for triple in combinations(range(n), 3):
        degree[triple] = sum(
            not convex([points[i] for i in triple + (p,)])
            for p in range(n) if p not in triple)
    delta = max(degree.values())

    faces = []
    bad_total = 0
    cover_total = 0
    for size in range(n + 1):
        for face in combinations(range(n), size):
            selected = [points[i] for i in face]
            if not convex(selected):
                continue
            faces.append(face)
            bad_labels = [
                p for p in range(n) if p not in face
                and not convex(selected + [points[p]])
            ]
            triples = canonical_triples(face, points)
            assert all(any(not convex([points[i] for i in triple]
                                      + [points[p]])
                           for triple in triples)
                       for p in bad_labels)
            bad_total += len(bad_labels)
            cover_total += sum(degree[triple] for triple in triples)

    v = len(faces)
    moment = sum(map(len, faces))
    rank = max(map(len, faces))
    assert (v, moment, rank) == (expected_v, expected_moment, expected_rank)
    assert bad_total == n * v - 2 * moment
    assert bad_total <= cover_total
    assert bad_total <= delta * (rank - 2) * moment
    return delta, bad_total, cover_total


def audit_triangle_parabola(max_m=40):
    for m in range(2, max_m + 1):
        big = (m + 1) ** 3
        outer = [(0, 0), (big, 0), (0, big)]
        inner = [(j, j * j) for j in range(1, m + 1)]
        points = outer + inner
        assert all(cross(*triple) != 0
                   for triple in combinations(points, 3))
        assert all(j + j * j < big for j in range(1, m + 1))
        assert hull_indices(points) == [0, 1, 2]
        # The closed hull of the outer triangle has h=3 and i=m.
        assert len(points) - len(hull_indices(points)) == m


def main():
    minimizer9 = [
        (62614, 7322), (2922, 4014), (10209, 14386),
        (20660, 24299), (33336, 29017), (30137, 33324),
        (15334, 45211), (14934, 55621), (10934, 61521),
    ]
    active = [
        [(F(-2), F(-2)), (F(-9, 5), F(-3, 2))],
        [(F(2), F(-2)), (F(17, 10), F(-9, 5))],
        [(F(2), F(2)), (F(9, 5), F(17, 10))],
        [(F(-2), F(2)), (F(-17, 10), F(9, 5))],
    ]
    repairs = [
        (F(2, 23), F(-1282, 575)),
        (F(2, 13), F(-734, 325)),
        (F(6, 29), F(-1658, 725)),
    ]
    repair11 = sum(active, []) + repairs

    row9 = audit(minimizer9, 169, 492, 5)
    row11 = audit(repair11, 564, 2056, 5)
    audit_triangle_parabola()

    assert row9 == (6, 537, 1002)
    assert row11 == (7, 2092, 4768)
    print("PASS: minimizer circuit-codegree dichotomy")
    print("  n=9:  Delta=6, bad incidences=537, canonical cover=1002")
    print("  n=11: Delta=7, bad incidences=2092, canonical cover=4768")
    print("  exact balance: sum_A b(A)=nV-2*sum_A |A|")
    print("  triangle/parabola hull-partition barriers: m=2,...,40")


if __name__ == "__main__":
    main()
