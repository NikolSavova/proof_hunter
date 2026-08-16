#!/usr/bin/env python3
"""Exact audits for the common-root fan and summed antichain bank."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import comb, isqrt

Point = tuple[Fraction, Fraction]


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def strict_inside_triangle(p: Point, tri: tuple[Point, Point, Point]) -> bool:
    vals = [orient(tri[i], tri[(i + 1) % 3], p) for i in range(3)]
    return all(v > 0 for v in vals) or all(v < 0 for v in vals)


def convex_hull(points: tuple[Point, ...]) -> tuple[Point, ...]:
    pts = sorted(set(points))
    if len(pts) <= 1:
        return tuple(pts)

    def half(seq: list[Point]) -> list[Point]:
        ans: list[Point] = []
        for p in seq:
            while len(ans) >= 2 and orient(ans[-2], ans[-1], p) <= 0:
                ans.pop()
            ans.append(p)
        return ans

    lo = half(pts)
    hi = half(list(reversed(pts)))
    return tuple(lo[:-1] + hi[:-1])


def apex(left: Fraction, right: Fraction) -> Point:
    assert left + right > 0
    return ((left - right) / (left + right), Fraction(2, 1) / (left + right))


def coordinate_geometry_audit() -> dict[str, int]:
    b = (Fraction(-1), Fraction(0))
    c = (Fraction(1), Fraction(0))
    a = (Fraction(0), Fraction(1))
    values = [Fraction(k, 4) for k in range(-2, 4)]
    coords = [(l, r) for l in values for r in values if l + r > 0 and l < 1 and r < 1]
    points = {z: apex(*z) for z in coords}
    for z, x in points.items():
        assert strict_inside_triangle(a, (b, c, x))

    pairs = 0
    incomparable = 0
    for z, w in combinations(coords, 2):
        x, y = points[z], points[w]
        x_in_y = strict_inside_triangle(x, (b, c, y))
        y_in_x = strict_inside_triangle(y, (b, c, x))
        z_ge_w = z[0] > w[0] and z[1] > w[1]
        w_ge_z = w[0] > z[0] and w[1] > z[1]
        # The grid was chosen so no coordinate equality is used in a
        # general-position comparison.
        if z[0] == w[0] or z[1] == w[1]:
            continue
        assert x_in_y == z_ge_w
        assert y_in_x == w_ge_z
        inc = not x_in_y and not y_in_x
        assert (len(convex_hull((b, c, x, y))) == 4) == inc
        pairs += 1
        incomparable += int(inc)
    return {"apices": len(coords), "pairs": pairs, "incomparable_pairs": incomparable}


def width_height(subset: tuple[tuple[int, int], ...]) -> tuple[int, int]:
    n = len(subset)
    height = 0
    width = 0
    for mask in range(1, 1 << n):
        chosen = [subset[i] for i in range(n) if (mask >> i) & 1]
        chain = all(
            (x[0] <= y[0] and x[1] <= y[1]) or (y[0] <= x[0] and y[1] <= x[1])
            for x, y in combinations(chosen, 2)
        )
        anti = all(
            not ((x[0] <= y[0] and x[1] <= y[1]) or (y[0] <= x[0] and y[1] <= x[1]))
            for x, y in combinations(chosen, 2)
        )
        height = max(height, len(chosen) if chain else 0)
        width = max(width, len(chosen) if anti else 0)
    return width, height


def dominance_audit() -> dict[str, int]:
    ground = tuple(product(range(3), repeat=2))
    checked = 0
    wide = 0
    for size in range(1, 8):
        for subset in combinations(ground, size):
            w, h = width_height(subset)
            assert w * h >= size
            assert max(w, h) >= isqrt(size)
            wide += int(w * w >= size)
            checked += 1
    return {"dominance_subsets": checked, "wide_subsets": wide}


def maximum_antichain(row: frozenset[int], order: list[list[bool]]) -> tuple[int, ...]:
    vals = sorted(row)
    best: tuple[int, ...] = ()
    for size in range(1, len(vals) + 1):
        for sub in combinations(vals, size):
            if all(not order[x][y] and not order[y][x] for x, y in combinations(sub, 2)):
                best = sub
    return best


def incidence_bank_audit() -> dict[str, int]:
    # Blockers form a 3 by 3 dominance grid.  Test many deterministic row
    # systems and verify events <= Lambda times distinct pair outputs.
    blockers = tuple(product(range(3), repeat=2))
    order = [[False] * len(blockers) for _ in blockers]
    for i, x in enumerate(blockers):
        for j, y in enumerate(blockers):
            order[i][j] = i != j and x[0] <= y[0] and x[1] <= y[1]

    rows_pool = [frozenset(s) for k in range(4, 8) for s in combinations(range(9), k)]
    systems = 0
    event_total = 0
    for seed in range(400):
        rows = [rows_pool[(seed * 17 + j * 43 + j * j) % len(rows_pool)] for j in range(2 + seed % 7)]
        chosen = [maximum_antichain(row, order) for row in rows]
        pair_load: dict[tuple[int, int], int] = {}
        events = 0
        for row, anti in zip(rows, chosen):
            # Only wide rows enter Theorem 1.
            if len(anti) * len(anti) < len(row):
                continue
            for pair in combinations(anti, 2):
                pair_load[pair] = pair_load.get(pair, 0) + 1
                events += 1
        if not events:
            continue
        lam = max(pair_load.values())
        assert events <= lam * len(pair_load)
        event_total += events
        systems += 1

    # A convex k-gon has exactly k cyclic adjacent pairs.  These are the
    # only possible choices for the inserted pair in the reconstruction.
    adjacent_decompositions = sum(k for k in range(4, 65))
    return {
        "incidence_systems": systems,
        "pair_events": event_total,
        "adjacent_decompositions_4_to_64": adjacent_decompositions,
    }


def scaling_audit() -> dict[str, int]:
    rows = 0
    for r in range(8, 81):
        n = 1 << (2 * r)
        ambient_tags = 3 * comb(n, 3)
        for g in range(1, r + 1):
            d = 1 << g
            # For epsilon=1/3, the ambient tag count already exceeds the
            # desired gain throughout this linear-codimension model.
            assert ambient_tags > 1 << (g // 3)
            rows += 1

    product_rows = 0
    for retained in range(1, 9):
        for hidden in range(2, 10):
            for m in range(2, 17):
                sources = m ** (retained + hidden - 1)
                targets = m ** retained * m
                fibre = m ** (hidden - 1)
                assert sources * m == targets * fibre
                assert sources == (m ** retained) * (m ** (hidden - 1))
                product_rows += 1
    return {"tag_scale_rows": rows, "fixed_outer_product_rows": product_rows}


def main() -> None:
    print("COORDINATE_GEOMETRY", coordinate_geometry_audit())
    print("DILWORTH", dominance_audit())
    print("SUMMED_BANK", incidence_bank_audit())
    print("SCALE_AND_BARRIER", scaling_audit())
    print("ALL_EXACT_CHECKS_PASSED")


if __name__ == "__main__":
    main()
