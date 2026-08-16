#!/usr/bin/env python3
"""Exact audit for REPAIR_STAR_CLIQUE_BARRIER.md."""

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


def main():
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
    points = sum(active, []) + repairs
    blocks = sum(([i, i] for i in range(4)), []) + [4, 4, 4]

    assert all(cross(*triple) != 0 for triple in combinations(points, 3))
    completions = [tuple(active[i][bits[i]] for i in range(4))
                   for bits in product(range(2), repeat=4)]
    assert len(completions) == 16
    assert all(convex(q) for q in completions)
    assert all(not convex(list(dict.fromkeys(q + r)))
               for q, r in combinations(completions, 2))

    stars = [q + (y,) for q in completions for y in repairs]
    assert len(stars) == len(set(stars)) == 48
    assert all(convex(s) for s in stars)
    assert all(not convex(list(dict.fromkeys(s + t)))
               for s, t in combinations(stars, 2))
    assert all(all(p in s or not convex(list(s) + [p]) for p in points)
               for s in stars)

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

    expected_profile = (1, 11, 55, 165, 220, 112, 0, 0, 0, 0, 0, 0)
    assert tuple(profile[i] for i in range(12)) == expected_profile
    assert sum(profile.values()) == 564
    assert masks[0b11111] == 48
    assert convex(repairs)

    print("PASS: repair-star clique barrier")
    print("  completions: 16 pairwise detached-incompatible")
    print("  repaired stars: 48 convex, maximal, pairwise incompatible")
    print("  full-support capacity: exactly 48 = D*M")
    print("  profile: (1,11,55,165,220,112,0,0,0,0,0,0); V=564")
    print("  unrestricted repair shield: 2^3 faces")


if __name__ == "__main__":
    main()
