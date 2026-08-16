#!/usr/bin/env python3
"""Exact audit for DISJOINT_SHIELD_COMMON_POCKET_REGRESSION.md."""

import sys
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product

sys.dont_write_bytecode = True


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


def convex(labels, points):
    labels = tuple(labels)
    return len(set(labels)) == len(labels) == len(
        hull_indices([points[i] for i in labels]))


def powerset(labels, max_size=None):
    labels = tuple(sorted(labels))
    stop = len(labels) if max_size is None else min(max_size, len(labels))
    for size in range(stop + 1):
        yield from combinations(labels, size)


def circle(t, scale=F(1), shift=(F(0), F(0))):
    den = 1 + t * t
    return (shift[0] + scale * (1 - t * t) / den,
            shift[1] + scale * 2 * t / den)


def canonical_triples(face, points):
    if len(face) <= 2:
        return set()
    cyclic = [face[i] for i in hull_indices([points[j] for j in face])]
    h = len(cyclic)
    triples = set()
    for i in range(h):
        for j in range(h):
            if j not in (i, (i + 1) % h):
                triples.add(tuple(sorted(
                    (cyclic[i], cyclic[(i + 1) % h], cyclic[j]))))
    return triples


def interior_label(labels, points):
    labels = tuple(labels)
    hull = set(hull_indices([points[i] for i in labels]))
    assert len(labels) == 4 and len(hull) == 3
    return labels[next(i for i in range(4) if i not in hull)]


def main():
    q, r, m = 4, 3, 5

    u_parameters = [F(40 + 5 * i, 1000) for i in range(q)]
    v_parameters = [F(1700 + 10 * i, 1000) for i in range(q)]
    w_parameters = [F(-1750 + 10 * i, 1000) for i in range(q)]
    optional_parameters = [F(-1710 + 10 * i, 1000) for i in range(r)]

    points = []
    u = tuple(range(len(points), len(points) + q))
    points.extend(circle(t) for t in u_parameters)
    v = tuple(range(len(points), len(points) + q))
    points.extend(circle(t) for t in v_parameters)
    w = tuple(range(len(points), len(points) + q))
    points.extend(circle(t) for t in w_parameters)
    optional = tuple(range(len(points), len(points) + r))
    points.extend(circle(t) for t in optional_parameters)

    inner_parameters = (F(1, 7), F(3, 5), F(5, 3), F(-4), F(-1, 2))
    inner = tuple(range(len(points), len(points) + m))
    inner_shift = (F(1, 1000), F(-1, 2000))
    points.extend(circle(t, F(1, 100), inner_shift)
                  for t in inner_parameters)

    n = len(points)
    outer = tuple(range(3 * q + r))
    core = tuple(sorted(u + v + w))

    assert all(cross(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(n), 3))
    assert convex(outer, points)
    assert convex(inner, points)

    # u[-1] and v[0] face the empty U--V gap and are adjacent.
    root = tuple(sorted((u[-1], v[0], w[1])))
    shields = [tuple(sorted((u[i], v[i], w[i]))) for i in range(q)]
    assert len(set().union(*map(set, shields))) == 3 * q

    # Every transversal triangle contains every inner point.
    for ui in u:
        for vi in v:
            for wi in w:
                triangle = (ui, vi, wi)
                for x in inner:
                    four = tuple(sorted(triangle + (x,)))
                    assert not convex(four, points)
                    assert interior_label(four, points) == x

    sources = []
    for chosen in powerset(optional):
        source = tuple(sorted(core + chosen))
        assert convex(source, points)
        assert root in canonical_triples(source, points)
        sources.append(source)
    assert len(sources) == 2 ** r

    neighbors = []
    for x in range(n):
        if x in root:
            continue
        four = tuple(sorted(root + (x,)))
        if not convex(four, points):
            neighbors.append(x)
            assert interior_label(four, points) == x
    assert tuple(neighbors) == inner

    # The complete q by m shield--repair circuit rectangle.
    for shield in shields:
        for x in inner:
            four = tuple(sorted(shield + (x,)))
            assert not convex(four, points)
            assert interior_label(four, points) == x

    x_zero = inner[0]
    toggle_candidates = []
    for source in sources:
        for guard in powerset(source, q - 1):
            released = tuple(sorted((set(source) - set(guard)) | {x_zero}))
            assert not convex(released, points)

        for pocket_face in powerset(inner):
            if not pocket_face:
                continue
            retained = tuple(sorted(set(source) | set(pocket_face)))
            assert not convex(retained, points)

        convex_toggle_words = []
        for word in product(range(3), repeat=q):
            guard = {shields[i][word[i]] for i in range(q)}
            released = tuple(sorted((set(source) - guard) | {x_zero}))
            if convex(released, points):
                convex_toggle_words.append(word)
            if len(set(word)) > 1:
                assert not convex(released, points)
        assert len(convex_toggle_words) <= 3
        toggle_candidates.append(len(convex_toggle_words))

    # Exact two-copy union collision on the convex pocket bank.
    pocket_faces = list(powerset(inner))
    union_histogram = Counter(
        tuple(sorted(set(first) | set(second)))
        for first in pocket_faces for second in pocket_faces)
    assert len(pocket_faces) == 2 ** m
    assert len(union_histogram) == 2 ** m
    assert sum(union_histogram.values()) == 4 ** m
    assert all(count == 3 ** len(union)
               for union, count in union_histogram.items())
    assert max(union_histogram.values()) == 3 ** m

    print("PASS: disjoint-shield common-pocket regression")
    print(f"  parameters: q={q}, r={r}, m={m}, n={n}")
    print(f"  canonical source contexts: {len(sources)}")
    print(f"  shield-label circuits: {q*m}, all with one common pocket")
    print(f"  every guard of size < {q} fails against x_0")
    print(f"  surviving matched-toggle candidates by source: {toggle_candidates}")
    print(f"  two-bank union: {4**m} records -> {2**m} outputs, "
          f"max fibre {3**m}")


if __name__ == "__main__":
    main()
