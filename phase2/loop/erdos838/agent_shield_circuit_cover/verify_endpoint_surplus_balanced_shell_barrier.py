#!/usr/bin/env python3
"""Exact checks for ENDPOINT_SURPLUS_BALANCED_SHELL_BARRIER.md.

The finite geometry is deliberately small enough to exhaust every subset in
every projection chamber.  The scalable part is an integer audit of the
rank/downset and shell-size inequalities used in the proof.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations
from math import comb


Point = tuple[F, F]


def det(a: Point, b: Point, c: Point) -> F:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def finite_points() -> tuple[Point, ...]:
    # Rational centrally symmetric octagon on the unit circle, in cyclic
    # order, followed by a generic three-point child in a tiny central box.
    shell = (
        (F(1), F(0)), (F(3, 5), F(4, 5)), (F(0), F(1)),
        (F(-3, 5), F(4, 5)), (F(-1), F(0)),
        (F(-3, 5), F(-4, 5)), (F(0), F(-1)),
        (F(3, 5), F(-4, 5)),
    )
    child = (
        (F(-1, 100), F(-1, 300)),
        (F(1, 200), F(1, 100)),
        (F(1, 150), F(-1, 120)),
    )
    return shell + child


def projection_orders(points: tuple[Point, ...]) -> list[tuple[int, ...]]:
    # Directions (1,t).  Reversing a direction swaps cap and cup, so one
    # half-turn suffices for their product.  Every wall and probe is rational.
    walls: set[F] = set()
    for a, b in combinations(points, 2):
        dx, dy = a[0] - b[0], a[1] - b[1]
        if dy:
            walls.add(-dx / dy)
    ordered_walls = sorted(walls)
    probes = [ordered_walls[0] - 1]
    probes += [(a + b) / 2 for a, b in zip(ordered_walls,
                                           ordered_walls[1:])]
    probes += [ordered_walls[-1] + 1]
    orders: list[tuple[int, ...]] = []
    for t in probes:
        order = tuple(sorted(range(len(points)),
                             key=lambda i: points[i][0] + t * points[i][1]))
        assert all(points[order[i]][0] + t * points[order[i]][1]
                   < points[order[i + 1]][0] + t * points[order[i + 1]][1]
                   for i in range(len(points) - 1))
        if order not in orders:
            orders.append(order)
    return orders


def is_convex(mask: int, points: tuple[Point, ...]) -> bool:
    inds = [i for i in range(len(points)) if mask >> i & 1]
    if len(inds) <= 3:
        return True
    # In general position a selected point is non-extreme iff it lies in a
    # triangle of three other selected points (planar Caratheodory).
    for x in inds:
        others = [i for i in inds if i != x]
        for a, b, c in combinations(others, 3):
            signs = (det(points[a], points[b], points[x]),
                     det(points[b], points[c], points[x]),
                     det(points[c], points[a], points[x]))
            if all(s > 0 for s in signs) or all(s < 0 for s in signs):
                return False
    return True


def endpoint_counts(order: tuple[int, ...], points: tuple[Point, ...]) -> tuple[int, int]:
    caps = cups = 0
    for mask in range(1, 1 << len(points)):
        inds = [i for i in order if mask >> i & 1]
        cap = cup = True
        for a, b, c in combinations(inds, 3):
            s = det(points[a], points[b], points[c])
            cap = cap and s < 0
            cup = cup and s > 0
            if not cap and not cup:
                break
        caps += cap
        cups += cup
    return caps, cups


def finite_geometry_audit() -> dict[str, object]:
    points = finite_points()
    assert all(det(points[i], points[j], points[k])
               for i, j, k in combinations(range(len(points)), 3))
    # The shell is strictly convex and its antipodal pairing is exact.
    for i in range(4):
        assert points[i + 4] == (-points[i][0], -points[i][1])
    assert all(is_convex(mask, points)
               for mask in range(1, 1 << 8))

    faces = sum(is_convex(mask, points)
                for mask in range(1, 1 << len(points)))
    orders = projection_orders(points)
    profiles = [(*endpoint_counts(order, points), faces) for order in orders]
    assert faces == 653
    assert len(orders) == 41
    assert min(c for c, _, _ in profiles) == 175
    assert max(c for c, _, _ in profiles) == 205
    # Exact cross-multiplied uniform bound: sigma < 61 in every chamber.
    assert all(c * u < 61 * faces for c, u, _ in profiles)
    return {
        "points": len(points),
        "projection_chambers": len(orders),
        "faces": faces,
        "cap_range": (min(c for c, _, _ in profiles),
                      max(c for c, _, _ in profiles)),
        "max_sigma_numerator": max(c * u for c, u, _ in profiles),
        "sigma_denominator": faces,
    }


def ceil_log2(x: int) -> int:
    assert x > 0
    return (x - 1).bit_length()


def scalable_integer_audit() -> list[tuple[int, int, int, int, int]]:
    rows = []
    for d in (8, 12, 16, 24, 32, 48, 64):
        m = comb(d, d // 2)
        rank = d
        # Exact rank/downset envelope for the Pascal core.
        envelope = sum(comb(m, j) for j in range(1, rank + 1))
        ell = ceil_log2(envelope)
        # A deliberately generous explicit shell.  K is divisible by four
        # and K/4 has enough entropy to absorb the core and every K^3 tag.
        quarter = ell + 3 * ceil_log2(4 * (ell + 16)) + 16
        k = 4 * quarter
        while k // 4 < ell + 3 * ceil_log2(k) + 8:
            k += 4
        if d >= 16:
            assert k < m
        assert envelope * k ** 3 * (1 << (k // 4)) <= (1 << (k // 2))
        n = m + k
        # Shell faces give the lower quasipolynomial scale; restriction to
        # shell/core faces gives the upper scale.
        lower_log = k - 1
        upper_log = k + ceil_log2(envelope)
        assert lower_log > 0 and upper_log < 8 * d * d
        if d >= 16:
            assert n < 2 * m
        rows.append((d, m, k, lower_log, upper_log))
    return rows


def main() -> None:
    geometry = finite_geometry_audit()
    rows = scalable_integer_audit()
    print("PASS: balanced-shell endpoint-surplus barrier")
    print("geometry:", geometry)
    print("scales:", rows)


if __name__ == "__main__":
    main()
