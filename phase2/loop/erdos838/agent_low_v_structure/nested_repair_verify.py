#!/usr/bin/env python3
"""Exact census for the singleton/ear repair dichotomy."""

from __future__ import annotations

from itertools import combinations
from random import Random


Point = tuple[int, int]


def orient(a: Point, b: Point, c: Point) -> int:
    z = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return (z > 0) - (z < 0)


def hull(points: list[Point], ids: tuple[int, ...]) -> tuple[int, ...]:
    ordered = sorted(ids, key=lambda i: (points[i][0], points[i][1]))
    if len(ordered) <= 1:
        return tuple(ordered)

    def build(sequence):
        out = []
        for i in sequence:
            while len(out) >= 2 and orient(points[out[-2]], points[out[-1]], points[i]) <= 0:
                out.pop()
            out.append(i)
        return out

    lower = build(ordered)
    upper = build(reversed(ordered))
    return tuple(lower[:-1] + upper[:-1])


def convex(points: list[Point], ids: tuple[int, ...]) -> bool:
    return len(ids) <= 2 or len(hull(points, ids)) == len(ids)


def strictly_in_triangle(p: Point, a: Point, b: Point, c: Point) -> bool:
    signs = (orient(a, b, p), orient(b, c, p), orient(c, a, p))
    return all(s > 0 for s in signs) or all(s < 0 for s in signs)


def cyclic_interval(positions: set[int], length: int) -> bool:
    if not positions or len(positions) == length:
        return True
    transitions = sum(((i in positions) != (((i + 1) % length) in positions)) for i in range(length))
    return transitions == 2


def deterministic_points(n: int, seed: int) -> list[Point]:
    rng = Random(seed)
    points: list[Point] = []
    while len(points) < n:
        candidate = (rng.randrange(-200, 201), rng.randrange(-200, 201))
        if candidate in points:
            continue
        if any(orient(points[i], points[j], candidate) == 0 for i, j in combinations(range(len(points)), 2)):
            continue
        points.append(candidate)
    return points


def audit(points: list[Point]) -> None:
    n = len(points)
    v = [0] * (n + 1)
    repair = [0] * (n + 1)
    interior_repair = [0] * (n + 1)
    ear_repair = [0] * (n + 1)
    ear_factorized = [0] * (n + 1)

    convex_sets: dict[int, list[tuple[int, ...]]] = {k: [] for k in range(n + 1)}
    for size in range(n + 1):
        for ids in combinations(range(n), size):
            if convex(points, ids):
                v[size] += 1
                convex_sets[size].append(ids)

    for size in range(4, n + 1):
        for ids in combinations(range(n), size):
            if convex(points, ids):
                continue
            boundary = hull(points, ids)
            boundary_set = set(boundary)
            inside = set(ids) - boundary_set
            for x in ids:
                target = tuple(i for i in ids if i != x)
                if not convex(points, target):
                    continue
                repair[size] += 1
                if x in inside:
                    interior_repair[size] += 1
                    assert inside == {x}
                    continue

                ear_repair[size] += 1
                pos = boundary.index(x)
                u, w = boundary[(pos - 1) % len(boundary)], boundary[(pos + 1) % len(boundary)]
                reduced_boundary = tuple(i for i in boundary if i != x)
                reduced_hull = set(hull(points, reduced_boundary))
                assert reduced_hull == set(reduced_boundary)
                for y in inside:
                    assert strictly_in_triangle(points[y], points[u], points[x], points[w])
                    assert y in set(hull(points, reduced_boundary + (y,)))

                target_hull = hull(points, target)
                hidden_positions = {j for j, y in enumerate(target_hull) if y in inside}
                assert cyclic_interval(hidden_positions, len(target_hull))

    # Direct factorization of the ear sum (6).
    for h in range(3, n + 1):
        for boundary in convex_sets[h]:
            cyclic_boundary = hull(points, boundary)
            for x in boundary:
                pos = cyclic_boundary.index(x)
                u, w = cyclic_boundary[(pos - 1) % h], cyclic_boundary[(pos + 1) % h]
                pocket = tuple(
                    y for y in range(n)
                    if y not in boundary and strictly_in_triangle(points[y], points[u], points[x], points[w])
                )
                for d in range(1, len(pocket) + 1):
                    size = h + d
                    if size > n:
                        break
                    for hidden in combinations(pocket, d):
                        target = tuple(y for y in boundary if y != x) + hidden
                        if convex(points, target):
                            ear_factorized[size] += 1

    for k in range(3, n):
        boundary_count = (n - k) * v[k] - (k + 1) * v[k + 1]
        assert repair[k + 1] == boundary_count
        assert repair[k + 1] == interior_repair[k + 1] + ear_repair[k + 1]
        assert ear_repair[k + 1] == ear_factorized[k + 1]

    print(
        f"n={n} v={v[3:]} repairs={repair[4:]} "
        f"interior={interior_repair[4:]} ears={ear_repair[4:]} PASS"
    )


def audit_arbitrary_fibre() -> None:
    triangle = [(-1000, 0), (0, 1000), (1000, 0)]
    fibre = [(-10, 2987), (-6, 3005), (-2, 2987), (1, 2990), (14, 2990), (18, 3002)]
    points = triangle + fibre
    assert all(orient(points[i], points[j], points[k]) != 0 for i, j, k in combinations(range(9), 3))
    assert not convex(points, tuple(range(3, 9)))
    for x in range(3, 9):
        ids = (0, 1, 2, x)
        assert set(hull(points, ids)) == {0, 2, x}
    print("arbitrary six-point replacement-cone fibre: PASS")


if __name__ == "__main__":
    for n, seed in ((8, 838), (9, 839), (10, 840)):
        audit(deterministic_points(n, seed))
    audit_arbitrary_fibre()
