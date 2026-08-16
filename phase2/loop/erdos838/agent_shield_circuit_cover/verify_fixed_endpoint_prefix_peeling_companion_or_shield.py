#!/usr/bin/env python3
"""Exact checks for FIXED_ENDPOINT_PREFIX_PEELING_COMPANION_OR_SHIELD."""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb


Point = tuple[F, F]


def lower_hull(values: list[F]) -> list[tuple[int, F]]:
    hull: list[tuple[int, F]] = []
    for x, y in enumerate(values):
        while len(hull) >= 2:
            x1, y1 = hull[-2]
            x2, y2 = hull[-1]
            if ((y2 - y1) * (x - x2)
                    >= (y - y2) * (x2 - x1)):
                hull.pop()
            else:
                break
        hull.append((x, y))
    return hull


def envelope(hull: list[tuple[int, F]], x: F) -> F:
    for (x1, y1), (x2, y2) in zip(hull, hull[1:]):
        if F(x1) <= x <= F(x2):
            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    if x == hull[-1][0]:
        return hull[-1][1]
    raise AssertionError((hull, x))


def floor_from_weights(weights: tuple[int, ...], columns: int) -> F:
    total = sum(weights)
    tails = [F(0)] * (len(weights) + 1)
    running = 0
    for q in range(len(weights) - 1, -1, -1):
        running += weights[q]
        tails[q] = F(running, total)
    hull = lower_hull(tails)
    # The profile is concave on each affine hull segment.
    return min((1 + x) * (1 + columns * y) for x, y in hull)


def maximum_child_path(
    family: tuple[tuple[int, ...], ...]
) -> list[tuple[tuple[int, ...], int, int, F]]:
    rank = len(family[0])
    node = family
    prefix: tuple[int, ...] = ()
    out = []
    for depth in range(rank):
        children: dict[int, list[tuple[int, ...]]] = {}
        for member in node:
            assert member[:depth] == prefix
            children.setdefault(member[depth], []).append(member)
        label, child = min(children.items(), key=lambda z: (-len(z[1]), z[0]))
        ratio = F(len(node), len(child))
        out.append((prefix, len(node), len(child), ratio))
        prefix += (label,)
        node = tuple(child)
    assert len(node) == 1
    return out


def exhaustive_trie_audit() -> tuple[int, int]:
    ground, rank, columns = 5, 2, 7
    universe = tuple(combinations(range(ground), rank))
    family_count = 0
    order_tests = 0
    for mask in range(1, 1 << len(universe)):
        family = tuple(universe[i] for i in range(len(universe))
                       if mask >> i & 1)
        path = maximum_child_path(family)
        product_ratio = F(1)
        lam = F(1)
        node = family
        prefix: tuple[int, ...] = ()
        for depth, (want_prefix, parent_size, child_size, ratio) in enumerate(path):
            assert prefix == want_prefix
            assert len(node) == parent_size
            product_ratio *= ratio
            lam = max(lam, ratio, F(2 ** depth))

            children: dict[int, list[tuple[int, ...]]] = {}
            for member in node:
                children.setdefault(member[depth], []).append(member)
            weights = tuple(len(children[z]) for z in sorted(children))
            assert max(weights) == child_size
            h = F(sum(weights), max(weights))
            assert h == ratio
            for order in set(permutations(weights)):
                order_tests += 1
                total = sum(order)
                crossed = 0
                for q in range(len(order) + 1):
                    tail = F(total - crossed, total)
                    wedge = max(F(0), 1 - F(q, 1) / h)
                    assert tail >= wedge
                    if q < len(order):
                        crossed += order[q]
                floor = floor_from_weights(order, columns)
                assert floor >= 1 + min(F(columns), h)

            label, child = min(children.items(), key=lambda z: (-len(z[1]), z[0]))
            prefix += (label,)
            node = tuple(child)
        assert product_ratio == len(family)
        s = rank
        assert F(2 ** (s - 1)) <= lam
        assert F(len(family)) <= lam ** s
        family_count += 1
    assert family_count == 1023
    return family_count, order_tests


def det(a: Point, b: Point, c: Point) -> F:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def is_cap(points: list[Point]) -> bool:
    ordered = sorted(points)
    return (len(ordered) <= 2 or
            all(det(ordered[i], ordered[j], ordered[k]) < 0
                for i, j, k in combinations(range(len(ordered)), 3)))


def is_cup(points: list[Point]) -> bool:
    ordered = sorted(points)
    return (len(ordered) <= 2 or
            all(det(ordered[i], ordered[j], ordered[k]) > 0
                for i, j, k in combinations(range(len(ordered)), 3)))


def hull_size(points: list[Point]) -> int:
    if len(points) <= 2:
        return len(points)
    ordered = sorted(set(points))
    lower: list[Point] = []
    for p in ordered:
        while len(lower) >= 2 and det(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper: list[Point] = []
    for p in reversed(ordered):
        while len(upper) >= 2 and det(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return len(lower[:-1] + upper[:-1])


def circle_point(t: int) -> Point:
    tt = F(t)
    return (F(1 - tt * tt, 1 + tt * tt), F(2 * tt, 1 + tt * tt))


def circle_peeling_audit(m: int = 6, rank: int = 3) -> tuple[int, int, int, int]:
    u, v = (F(-1), F(0)), (F(1), F(0))
    upper_points = sorted(circle_point(i) for i in range(1, m + 1))
    lower_points = sorted(circle_point(-(m + i)) for i in range(1, m + 1))
    points = [u, v] + upper_points + lower_points
    assert len({p[0] for p in points}) == len(points)
    assert all(det(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))

    family = tuple(combinations(range(m), rank))
    fixed_cup = [u, v] + lower_points
    assert is_cup(fixed_cup)
    for member in family:
        cap = [u, v] + [upper_points[i] for i in member]
        assert is_cap(cap)
        assert hull_size(cap + lower_points) == len(cap + lower_points)

    path = maximum_child_path(family)
    node = family
    prefix: tuple[int, ...] = ()
    max_shield = 1
    for depth, (_, _, _, _) in enumerate(path):
        children: dict[int, list[tuple[int, ...]]] = {}
        for member in node:
            children.setdefault(member[depth], []).append(member)

        # Omitting u and the common prefix exposes the next label as the
        # literal left endpoint of every suffix cap.
        for label, child in children.items():
            for member in child:
                remaining = [upper_points[i] for i in member[depth:]] + [v]
                assert is_cap(remaining)
                assert min(remaining)[0] == upper_points[label][0]

        # Every subset of the common cap prefix is a rooted ordinary shield.
        for mask in range(1 << len(prefix)):
            subset = [upper_points[prefix[i]] for i in range(len(prefix))
                      if mask >> i & 1]
            rooted = fixed_cup + subset
            assert hull_size(rooted) == len(rooted)
        max_shield = max(max_shield, 1 << len(prefix))

        label, child = min(children.items(), key=lambda z: (-len(z[1]), z[0]))
        prefix += (label,)
        node = tuple(child)
    assert len(family) == comb(m, rank)
    assert max_shield == 1 << (rank - 1)
    return m, rank, len(family), max_shield


def middle_layer_barrier(m: int = 32) -> tuple[int, int, F, int]:
    assert m % 2 == 0
    s = m // 2
    total = comb(m, s)
    gains = []
    ratios = []
    for j in range(s):
        node = comb(m - j, s - j)
        h = F(m - j, s - j)
        gains.append(F(node, total) * h)
        if j + 1 < s:
            next_gain = (F(comb(m - j - 1, s - j - 1), total)
                         * F(m - j - 1, s - j - 1))
            ratios.append(next_gain / gains[-1])
    assert gains[0] == 2
    assert all(g <= 2 for g in gains)
    assert all(q <= 1 for q in ratios)
    shield = 1 << (s - 1)
    assert shield * shield <= total * s
    assert 4 * shield * shield >= total
    return m, total, max(gains), shield


def main() -> None:
    families, orders = exhaustive_trie_audit()
    circle = circle_peeling_audit()
    middle = middle_layer_barrier()
    middle_out = (middle[0], middle[1], int(middle[2]), middle[3])
    print(
        "PASS: fixed-endpoint prefix peeling; "
        f"families={families}, order_tests={orders}, "
        f"circle={circle}, middle={middle_out}"
    )


if __name__ == "__main__":
    main()
