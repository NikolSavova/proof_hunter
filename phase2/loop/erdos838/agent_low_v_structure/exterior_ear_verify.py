#!/usr/bin/env python3
"""Exact checks for the exterior-ear pair injection and no-crossing family."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from random import Random


Point = tuple[Fraction, Fraction]


def orient(a: Point, b: Point, c: Point) -> int:
    z = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return (z > 0) - (z < 0)


def hull(points: list[Point], ids: tuple[int, ...]) -> tuple[int, ...]:
    order = sorted(ids, key=lambda i: points[i])
    if len(order) <= 1:
        return tuple(order)

    def half(seq):
        out = []
        for i in seq:
            while len(out) >= 2 and orient(points[out[-2]], points[out[-1]], points[i]) <= 0:
                out.pop()
            out.append(i)
        return out

    low, high = half(order), half(reversed(order))
    return tuple(low[:-1] + high[:-1])


def convex(points: list[Point], ids: tuple[int, ...]) -> bool:
    return len(ids) <= 2 or len(hull(points, ids)) == len(ids)


def deterministic_points(n: int, seed: int) -> list[Point]:
    rng = Random(seed)
    points: list[Point] = []
    while len(points) < n:
        candidate = (Fraction(rng.randrange(-100, 101)), Fraction(rng.randrange(-100, 101)))
        if candidate in points:
            continue
        if any(orient(points[i], points[j], candidate) == 0 for i, j in combinations(range(len(points)), 2)):
            continue
        points.append(candidate)
    return points


def check_pair_injection() -> None:
    points = deterministic_points(9, 20260814)
    images = set()
    incidences = 0
    for r in range(3, 9):
        for face in combinations(range(9), r):
            if not convex(points, face):
                continue
            for p in set(range(9)) - set(face):
                if p in hull(points, face + (p,)) and not convex(points, face + (p,)):
                    boundary = set(hull(points, face + (p,)))
                    hidden = tuple(sorted(set(face) - boundary))
                    outer = tuple(sorted(boundary))
                    assert hidden and p in outer
                    assert convex(points, hidden) and convex(points, outer)
                    assert len(hidden) + len(outer) == r + 1
                    image = (hidden, outer, p)
                    assert image not in images
                    images.add(image)
                    incidences += 1
    assert len(images) == incidences
    print(f"two-face exterior injection: {incidences} exact incidences PASS")


def check_common_interval_family() -> None:
    r, m = 5, 25
    last = m - 1
    chain: list[Point] = [(Fraction(i), Fraction(i * (last - i))) for i in range(m)]
    epsilon = Fraction(1, 10**6)
    apex_center = (Fraction(-1), Fraction(m * m))
    apex = [
        (apex_center[0] + epsilon * j, apex_center[1] + epsilon * j * j)
        for j in range(r * r)
    ]
    points = chain + apex
    assert all(orient(points[i], points[j], points[k]) != 0 for i, j, k in combinations(range(len(points)), 3))

    anchor = m // 2
    middle = tuple(i for i in range(1, last) if i != anchor)
    source_count = 0
    for selected in combinations(middle, r - 3):
        face = (0, anchor, last) + selected
        assert convex(points, face)
        addable = set(range(m)) - set(face)
        assert len(addable) == 4 * r
        assert all(convex(points, face + (q,)) for q in addable)
        expected_hidden = set(face) - {0, last}
        for x in range(m, m + r * r):
            boundary = set(hull(points, face + (x,)))
            assert boundary == {0, last, x}
            assert set(face) - boundary == expected_hidden
        source_count += 1

    assert source_count == 231
    print(f"common interval: {source_count} sources x {r*r} identical exterior labels PASS")


if __name__ == "__main__":
    check_pair_injection()
    check_common_interval_family()
