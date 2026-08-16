#!/usr/bin/env python3
"""Exact verifier for COLORFUL_PAIR_ENDPOINT_TRANSVERSAL_BARRIER.md."""

from itertools import combinations, product


POINTS = [
    (-11000, -11), (-7797, 629),
    (-9971, 1975), (-10004, 505),
    (-1006, 9987), (999, 10011),
    (-30, 12020), (-254, 13159),
    (9005, -24), (15883, -1249),
    (9980, 2008), (9984, 500),
]
PAIRS = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]
CLASSES = [(0, 1, 10, 11), (2, 3, 4, 5), (6, 7, 8, 9)]
CIRCUITS = [PAIRS[0] + PAIRS[1],
            PAIRS[2] + PAIRS[3],
            PAIRS[4] + PAIRS[5]]


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - \
           (b[1] - a[1]) * (c[0] - a[0])


def hull(indices):
    points = sorted((POINTS[i], i) for i in indices)
    if len(points) <= 1:
        return tuple(i for _, i in points)

    def half(seq):
        out = []
        for item in seq:
            while len(out) >= 2 and orient(out[-2][0], out[-1][0],
                                            item[0]) <= 0:
                out.pop()
            out.append(item)
        return out

    return tuple(i for _, i in half(points)[:-1] + half(reversed(points))[:-1])


def convex(indices):
    return len(indices) <= 2 or len(hull(indices)) == len(indices)


def main():
    assert all(orient(POINTS[i], POINTS[j], POINTS[k]) != 0
               for i, j, k in combinations(range(12), 3))
    assert all(convex(c) for c in CLASSES)

    hidden = []
    for circuit in CIRCUITS:
        assert not convex(circuit)
        missing = set(circuit) - set(hull(circuit))
        assert len(missing) == 1
        hidden.append(next(iter(missing)))
    assert hidden == [3, 6, 11]

    hull_rank = {3: 0, 4: 0, 5: 0, 6: 0}
    colorful = []
    for bits in product((0, 1), repeat=6):
        trace = tuple(PAIRS[i][bits[i]] for i in range(6))
        hull_rank[len(hull(trace))] += 1
        if convex(trace):
            colorful.append((bits, trace))
    assert not colorful
    assert hull_rank == {3: 16, 4: 32, 5: 16, 6: 0}

    one_gap = []
    for omitted in range(6):
        retained = [pair for i, pair in enumerate(PAIRS) if i != omitted]
        good = 0
        for bits in product((0, 1), repeat=5):
            trace = tuple(retained[i][bits[i]] for i in range(5))
            good += convex(trace)
        one_gap.append(good)
    assert one_gap == [0, 0, 8, 8, 0, 0]

    face_vector = [0] * 13
    for mask in range(1, 1 << 12):
        trace = tuple(i for i in range(12) if mask >> i & 1)
        if convex(trace):
            face_vector[len(trace)] += 1
    assert face_vector == [0, 12, 66, 220, 253, 125, 30, 3,
                           0, 0, 0, 0, 0]
    assert sum(face_vector) == 709

    print(
        "PASS: GP 12-point pair reset; hidden=(3,6,11); "
        "colorful6=0/64; one_gap=(0,0,8,8,0,0); V=709"
    )


if __name__ == "__main__":
    main()
