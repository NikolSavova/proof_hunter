#!/usr/bin/env python3
"""Exact audit for PREVALENCE_COMMON_CAGE_REGRESSION.md."""

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


def powerset(labels):
    labels = tuple(sorted(labels))
    for size in range(len(labels) + 1):
        yield from combinations(labels, size)


def circle(t, scale=F(1), shift=(F(0), F(0))):
    den = 1 + t * t
    return (shift[0] + scale * (1 - t * t) / den,
            shift[1] + scale * 2 * t / den)


def canonical_triples(face, points):
    cyclic = [face[i] for i in hull_indices([points[j] for j in face])]
    h = len(cyclic)
    triples = set()
    for i in range(h):
        for j in range(h):
            if j not in (i, (i + 1) % h):
                triples.add(tuple(sorted(
                    (cyclic[i], cyclic[(i + 1) % h], cyclic[j]))))
    return triples


class DSU:
    def __init__(self, labels):
        self.parent = {x: x for x in labels}

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.parent[y] = x


def main():
    p, q, r, m = 5, 3, 2, 4
    u_parameters = [F(35 + 5 * i, 1000) for i in range(p)]
    v_parameters = [F(1690 + 10 * i, 1000) for i in range(p)]
    w_parameters = [F(-1770 + 10 * i, 1000) for i in range(p)]
    optional_parameters = [F(-1710 + 10 * i, 1000) for i in range(r)]

    points = []
    u = tuple(range(len(points), len(points) + p))
    points.extend(circle(t) for t in u_parameters)
    v = tuple(range(len(points), len(points) + p))
    points.extend(circle(t) for t in v_parameters)
    w = tuple(range(len(points), len(points) + p))
    points.extend(circle(t) for t in w_parameters)
    optional = tuple(range(len(points), len(points) + r))
    points.extend(circle(t) for t in optional_parameters)

    inner_parameters = (F(1, 7), F(3, 5), F(5, 3), F(-4))
    inner = tuple(range(len(points), len(points) + m))
    shift = (F(1, 1000), F(-1, 2000))
    points.extend(circle(t, F(1, 100), shift) for t in inner_parameters)

    n = len(points)
    outer = tuple(range(3 * p + r))
    core = tuple(sorted(u + v + w))
    root = tuple(sorted((u[-1], v[0], w[2])))
    shields = [tuple(sorted((u[i], v[i], w[i]))) for i in range(q)]

    assert all(cross(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(n), 3))
    assert convex(outer, points)
    assert len(set().union(*map(set, shields))) == 3 * q

    # Complete transversal circuit tensor.
    for ui in u:
        for vi in v:
            for wi in w:
                for x in inner:
                    four = tuple(sorted((ui, vi, wi, x)))
                    assert not convex(four, points)

    sources = []
    completion_histogram = Counter()
    for chosen in powerset(optional):
        source = tuple(sorted(core + chosen))
        assert convex(source, points)
        assert root in canonical_triples(source, points)
        sources.append(source)

        # The full root neighborhood is exactly X.
        neighbors = []
        for label in range(n):
            if label in root:
                continue
            if not convex(tuple(sorted(root + (label,))), points):
                neighbors.append(label)
        assert tuple(neighbors) == inner

        # After any root deletion, bad circuits meeting X connect all labels.
        for deleted in root:
            residual = tuple(sorted((set(source) - {deleted}) | set(inner)))
            dsu = DSU(residual)
            for four in combinations(residual, 4):
                if set(four) & set(inner) and not convex(four, points):
                    for label in four[1:]:
                        dsu.union(four[0], label)
            roots = {dsu.find(label) for label in residual}
            assert len(roots) == 1

        # Every matching toggle has size q<p and therefore fails.
        for word in product(range(3), repeat=q):
            guard = {shields[i][word[i]] for i in range(q)}
            for x in inner:
                released = tuple(sorted((set(source) - guard) | {x}))
                assert not convex(released, points)

        # Exhaust every guard below p, then classify every size-p completion.
        for x in inner:
            for size in range(p):
                for guard in combinations(source, size):
                    released = tuple(sorted((set(source) - set(guard)) | {x}))
                    assert not convex(released, points)

            good = []
            for guard in combinations(source, p):
                released = tuple(sorted((set(source) - set(guard)) | {x}))
                if convex(released, points):
                    good.append(tuple(sorted(guard)))

            expected = {tuple(sorted(u)), tuple(sorted(v))}
            if not chosen:
                expected.add(tuple(sorted(w)))
            assert set(good) == expected
            completion_histogram[len(good)] += 1

    assert len(sources) == 2 ** r
    assert completion_histogram == Counter({2: m * (2 ** r - 1), 3: m})

    print("PASS: prevalence common-cage regression")
    print(f"  parameters: p={p}, q={q}, r={r}, m={m}, n={n}")
    print(f"  weighted canonical sources: {len(sources)}")
    print("  every root-deleted external circuit graph is connected")
    print(f"  all {3**q} matched toggles fail for every source and label")
    print(f"  minimum singleton guards: {dict(completion_histogram)}")


if __name__ == "__main__":
    main()
