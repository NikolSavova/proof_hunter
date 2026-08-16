#!/usr/bin/env python3
"""Exact audit for RECOVERABLE_COMPONENT_TOGGLE_BRANCH.md."""

import sys
from collections import Counter
from fractions import Fraction as F
from itertools import combinations

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


def circle(t):
    den = 1 + t * t
    return ((1 - t * t) / den, 2 * t / den)


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


def bad_circuits(labels, points):
    return [q for q in combinations(sorted(labels), 4) if not convex(q, points)]


def main():
    # a,b bound the left arc; z lies to the right.  X is on the right circle
    # arc inside triangle abz, and Y is the optional left source arc.
    a_point = circle(F(-2))
    b_point = circle(F(2))
    x_parameters = (F(-3, 25), F(-1, 25), F(3, 100), F(11, 100))
    y_parameters = (F(3), F(5), F(-5), F(-3))

    points = [a_point, b_point]
    pocket = tuple(range(len(points), len(points) + len(x_parameters)))
    points.extend(circle(t) for t in x_parameters)
    optional = tuple(range(len(points), len(points) + len(y_parameters)))
    points.extend(circle(t) for t in y_parameters)
    z = len(points)
    points.append((F(4), F(1, 7)))

    a, b = 0, 1
    root = tuple(sorted((a, b, z)))
    block_1 = pocket[:2]
    block_2 = pocket[2:]
    n = len(points)

    assert all(cross(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(n), 3))
    assert convex((a, b) + pocket + optional, points)
    assert convex(pocket, points)

    sources = []
    output_records = Counter()
    for chosen_optional in powerset(optional):
        source = tuple(sorted(root + chosen_optional))
        assert convex(source, points)
        assert root in canonical_triples(source, points)

        # The root circuit neighborhood is exactly the pocket.
        for label in pocket:
            assert not convex(tuple(sorted(root + (label,))), points)
        for label in optional:
            assert convex(tuple(sorted(root + (label,))), points)

        base = tuple(sorted((set(source) - {z})))
        universe = set(base) | set(block_1) | set(block_2)
        # Pure internal cells: after deleting z there is no bad circuit at all.
        assert not bad_circuits(universe, points)

        local_count = 0
        for face_1 in powerset(block_1):
            for face_2 in powerset(block_2):
                output = tuple(sorted(
                    set(base) | set(face_1) | set(face_2)))
                assert convex(output, points)
                output_records[output] += 1
                local_count += 1

                # Exact decoder once root/description is fixed.
                decoded_1 = tuple(sorted(set(output) & set(block_1)))
                decoded_2 = tuple(sorted(set(output) & set(block_2)))
                decoded_source = tuple(sorted(
                    (set(output) - set(pocket)) | {z}))
                assert decoded_1 == face_1
                assert decoded_2 == face_2
                assert decoded_source == source
        assert local_count == (2 ** len(block_1)) * (2 ** len(block_2))
        sources.append(source)

    assert len(sources) == 2 ** len(optional)
    assert sum(output_records.values()) == 2 ** (len(optional) + len(pocket))
    assert len(output_records) == sum(output_records.values())
    assert max(output_records.values()) == 1

    print("PASS: recoverable component-toggle branch")
    print(f"  n={n}, weighted source contexts={len(sources)}")
    print(f"  two pure pocket banks: 2^{len(block_1)} x 2^{len(block_2)}")
    print(f"  decoded output records: {sum(output_records.values())}, collision free")


if __name__ == "__main__":
    main()
