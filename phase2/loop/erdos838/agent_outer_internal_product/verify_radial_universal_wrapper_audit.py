#!/usr/bin/env python3
"""Exact audit for RADIAL_UNIVERSAL_WRAPPER_AUDIT.md."""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product


def cross(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def convex(points):
    return len(set(points)) == len(points) == len(hull(points))


def inside_triangle(p, a, b, c):
    signs = (cross(a, b, p), cross(b, c, p), cross(c, a, p))
    return all(x > 0 for x in signs) or all(x < 0 for x in signs)


def main():
    clusters = [
        [(F(-2), F(-2)), (F(-9, 5), F(-3, 2))],
        [(F(2), F(-2)), (F(17, 10), F(-9, 5))],
        [(F(2), F(2)), (F(9, 5), F(17, 10))],
        [(F(-2), F(2)), (F(-17, 10), F(9, 5))],
    ]
    points = sum(clusters, [])
    blocks = sum(([i, i] for i in range(4)), [])

    assert all(cross(*triple) != 0 for triple in combinations(points, 3))
    transversals = [tuple(clusters[i][bits[i]] for i in range(4))
                    for bits in product(range(2), repeat=4)]
    assert all(convex(t) for t in transversals)
    assert all(not convex(list(dict.fromkeys(t + u)))
               for t, u in combinations(transversals, 2))
    for i, (outer, inner) in enumerate(clusters):
        previous = clusters[(i - 1) % 4]
        following = clusters[(i + 1) % 4]
        assert all(inside_triangle(inner, outer, p, n)
                   for p in previous for n in following)
    assert convex([clusters[0][0], clusters[0][1],
                   clusters[1][0], clusters[2][0]])

    profile = Counter()
    masks = Counter()
    for size in range(len(points) + 1):
        for inds in combinations(range(len(points)), size):
            selected = [points[i] for i in inds]
            if convex(selected):
                profile[size] += 1
                mask = 0
                for i in inds:
                    mask |= 1 << blocks[i]
                masks[mask] += 1
    assert tuple(profile[i] for i in range(9)) == (
        1, 8, 28, 56, 38, 0, 0, 0, 0)
    assert sum(profile.values()) == 131
    expected_masks = (1, 3, 3, 9, 3, 9, 9, 12,
                      3, 9, 9, 12, 9, 12, 12, 16)
    assert tuple(masks[i] for i in range(16)) == expected_masks
    claimed = 1 + 4 * 3 + 6 * 9 + 4 * 2**3 + 2**4
    assert claimed == 115 and sum(profile.values()) - claimed == 16

    print("PASS: radial universal-wrapper classification audit")
    print("  16/16 transversals convex; 120/120 pair unions nonconvex")
    print("  full profile: (1,8,28,56,38,0,0,0,0); V=131")
    print("  scalar recurrence predicts 115, missing 16 faces")
    print("  each 3-block mask: 12 faces; full mask: 16")
    print("  exact counterface: {a,a',b,c} is convex")


if __name__ == "__main__":
    main()
