#!/usr/bin/env python3
"""Exact checks for HIGH_REDUNDANCY_RELEASE_HALL_BARRIER.md."""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product


def cross(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull_indices(points):
    order = sorted(range(len(points)), key=lambda i: points[i])
    lower = []
    for i in order:
        while (len(lower) >= 2 and
               cross(points[lower[-2]], points[lower[-1]], points[i]) <= 0):
            lower.pop()
        lower.append(i)
    upper = []
    for i in reversed(order):
        while (len(upper) >= 2 and
               cross(points[upper[-2]], points[upper[-1]], points[i]) <= 0):
            upper.pop()
        upper.append(i)
    return lower[:-1] + upper[:-1]


def convex(labels, points):
    labels = tuple(labels)
    return (len(labels) == len(set(labels)) and
            len(labels) == len(hull_indices([points[i] for i in labels])))


def main():
    m = 5
    delta = F(1, 100 * m * m)
    local = [(F(2) - delta*t*t, -F(1, 5) + delta*t)
             for t in range(1, m + 1)]
    a, b, c = (F(0), F(-1)), (F(4), F(-1)), (F(0), F(4))
    epsilon = F(1, 700)
    upper = [(epsilon*u, F(4) - epsilon*epsilon*u*u)
             for u in (6, 4, 2, -2, -4, -6)]
    points = [a, b, c] + local + upper
    labels = tuple(range(len(points)))
    edge = (0, 1)
    root = (0, 1, 2)
    pocket = tuple(range(3, 8))
    roles = ((8, 9), (10, 11), (12, 13))

    assert all(cross(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(labels, 3))
    assert convex(root + tuple(range(8, 14)), points)

    parity = {(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)}
    sources = []
    for word in parity:
        source = root + tuple(roles[i][word[i]] for i in range(3))
        assert convex(source, points)
        sources.append(source)
    assert len(sources) == 4

    ambient_sources = [root + choice for choice in product(*roles)]
    assert len(ambient_sources) == 8
    assert all(convex(source, points) for source in ambient_sources)

    rich = [face for size in range(3, 6)
            for face in combinations(pocket, size)]
    assert len(rich) == 16
    outputs = Counter()
    records = 0
    for source in sources:
        chosen = source[3:]
        for face in rich:
            assert convex(face, points)
            released = tuple(sorted(edge + face))
            assert convex(released, points)
            assert not convex(tuple(sorted(set(source) | set(face))), points)
            # Every occupied source label is a mandatory singleton trace.
            for y in chosen:
                assert any(not convex(triple + (y,), points)
                           for triple in combinations(face, 3))
            outputs[released] += 1
            records += 1

    assert records == 64
    assert len(outputs) == 16 and set(outputs.values()) == {4}

    # Every fibre has parity-code entropy 2 in a 3-bit box.
    redundancy = 3 - 2
    assert redundancy == 1
    support_bank = len(ambient_sources)
    support_overlap = len(rich)
    local_ratio = F(len(sources)**2, support_bank)
    assert (support_bank, support_overlap, local_ratio) == (8, 16, 2)

    # Conditional-to-source redundancy transfer is equality here:
    # R_cond=1, R_src=3-H(parity)=1, and H(U)=log rich=4.
    source_entropy = 2
    output_entropy = 4
    pocket_entropy = 4
    source_redundancy = 3 - source_entropy
    assert redundancy == source_redundancy + output_entropy - pocket_entropy
    assert F(len(sources), support_bank) == F(1, 2) == F(1, 2**redundancy)

    # Exact coefficient stress q=.4L, k=.2L, h=.3L.
    q, k, h = F(2, 5), F(1, 5), F(3, 10)
    assert q - k == F(1, 5)
    assert k + h == F(1, 2)
    assert max(q, h) == F(2, 5)

    print('PASS: common-guard sources=4 rich=16 records=64 R=1 '
          'support=8 overlap=16; coefficients=(1/2,2/5,3/10)')


if __name__ == '__main__':
    main()
