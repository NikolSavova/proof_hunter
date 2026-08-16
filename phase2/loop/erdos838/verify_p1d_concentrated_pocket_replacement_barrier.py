#!/usr/bin/env python3
"""Exact verifier for the concentrated-pocket replacement barrier."""

from fractions import Fraction
from itertools import combinations


POINTS = (
    (0, 2926687),
    (1, 4112040),
    (2, -8641570),
    (3, -1312196),
    (4, 7155532),
    (5, 6305027),
    (6, 3587334),
    (7, 177486),
    (8, 5991940),
    (9, 2014143),
    (10, 9575052),
    (11, -2670279),
)

SOURCE = (0, 1, 2, 4)
POCKET = (8, 9, 10, 11)


def cross(i, j, k):
    xi, yi = POINTS[i]
    xj, yj = POINTS[j]
    xk, yk = POINTS[k]
    return (xj - xi) * (yk - yi) - (yj - yi) * (xk - xi)


def hull(indices):
    ordered = sorted(indices, key=lambda i: POINTS[i])

    def half(sequence):
        out = []
        for i in sequence:
            while len(out) >= 2 and cross(out[-2], out[-1], i) <= 0:
                out.pop()
            out.append(i)
        return out

    return tuple(half(ordered)[:-1] + half(reversed(ordered))[:-1])


def convex(indices):
    indices = tuple(indices)
    return len(indices) <= 2 or len(hull(indices)) == len(indices)


def cyclic_edge(h, u, v):
    return any(h[i] == u and h[(i + 1) % len(h)] == v for i in range(len(h)))


def exponent(alpha, delta):
    gamma = 1 - alpha + delta
    direct = (2 * alpha - alpha * alpha) + (2 * gamma - gamma * gamma) - 2 * delta
    simplified = (
        1
        + 2 * alpha
        - 2 * alpha * alpha
        - 2 * (1 - alpha) * delta
        - delta * delta
    )
    assert direct == simplified
    return direct


def main():
    assert all(cross(*triple) != 0 for triple in combinations(range(len(POINTS)), 3))

    source_hull = hull(SOURCE)
    assert source_hull == (0, 2, 4, 1)
    assert convex(SOURCE)
    assert convex(POCKET)

    insertion_hulls = {}
    for q in POCKET:
        h = hull((*SOURCE, q))
        assert len(h) == len(SOURCE) + 1
        assert cyclic_edge(h, 2, q) and cyclic_edge(h, q, 4)
        insertion_hulls[q] = h

    failed = []
    for size in range(1, len(SOURCE) + 1):
        for trace in combinations(SOURCE, size):
            assert not convex((*trace, *POCKET))
            failed.append(trace)
    assert len(failed) == 2 ** len(SOURCE) - 1

    half = Fraction(1, 2)
    quarter = Fraction(1, 4)
    assert exponent(half, quarter) == Fraction(19, 16)
    assert exponent(half, half) == Fraction(3, 4)
    for numerator in range(1, 100):
        alpha = Fraction(numerator, 100)
        assert exponent(alpha, alpha) == 1 - alpha * alpha

    print(
        "PASS: concentrated-pocket replacement barrier; "
        f"source_hull={source_hull}; pocket_hull={hull(POCKET)}; "
        f"common_edge=(2,4); insertion_hulls={insertion_hulls}; "
        f"nonempty_traces_killed={len(failed)}; "
        f"E(1/2,1/4)={exponent(half, quarter)}; "
        f"E(1/2,1/2)={exponent(half, half)}"
    )


if __name__ == "__main__":
    main()
