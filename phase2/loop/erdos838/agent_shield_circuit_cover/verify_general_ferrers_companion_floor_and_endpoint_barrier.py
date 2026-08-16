#!/usr/bin/env python3
"""Exact checks for GENERAL_FERRERS_COMPANION_FLOOR_AND_ENDPOINT_BARRIER."""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations, product
from math import comb


Point = tuple[F, F]


def lower_hull(values: list[F]) -> list[tuple[int, F]]:
    """Vertices of the greatest convex minorant of integer data."""
    hull: list[tuple[int, F]] = []
    for x, y in enumerate(values):
        p = (x, y)
        while len(hull) >= 2:
            x1, y1 = hull[-2]
            x2, y2 = hull[-1]
            x3, y3 = p
            # Convex slopes must be nondecreasing.
            if (y2 - y1) * (x3 - x2) >= (y3 - y2) * (x2 - x1):
                hull.pop()
            else:
                break
        hull.append(p)
    return hull


def envelope(hull: list[tuple[int, F]], x: F) -> F:
    for (x1, y1), (x2, y2) in zip(hull, hull[1:]):
        if F(x1) <= x <= F(x2):
            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    if x == hull[-1][0]:
        return hull[-1][1]
    raise AssertionError((hull, x))


def normalized_tails(weights: list[int]) -> list[F]:
    total = sum(weights)
    tails = [F(0)] * (len(weights) + 1)
    running = 0
    for q in range(len(weights) - 1, -1, -1):
        running += weights[q]
        tails[q] = F(running, total)
    return tails


def profile_value(hull: list[tuple[int, F]], m: int, x: F) -> F:
    return (1 + x) * (1 + m * envelope(hull, x))


def floor_value(weights: list[int], m: int) -> F:
    hull = lower_hull(normalized_tails(weights))
    # On each hull segment the profile is concave, hence its minimum is
    # attained at a segment endpoint.
    return min(profile_value(hull, m, F(x)) for x, _ in hull)


def ferrers_audit() -> int:
    weights = [8, 4, 2, 1]
    tails = normalized_tails(weights)
    hull = lower_hull(tails)
    m = 4
    floor = floor_value(weights, m)
    states = 0
    by_area: dict[int, list[F]] = {}
    # Nondecreasing heights are precisely the Ferrers ideals in this
    # convention.
    for hs in product(range(len(weights) + 1), repeat=m):
        if any(hs[i] > hs[i + 1] for i in range(m - 1)):
            continue
        states += 1
        mean_h = F(sum(hs), m)
        mean_tail = sum((tails[h] for h in hs), F(0)) / m
        actual = (1 + mean_h) * (1 + m * mean_tail)
        jensen = profile_value(hull, m, mean_h)
        assert actual >= jensen >= floor
        by_area.setdefault(sum(hs), []).append(actual)
    assert states == comb(2 * m, m) == 70
    assert set(by_area) == set(range(m * len(weights) + 1))
    grid_peak = max(profile_value(hull, m, F(a, m))
                    for a in range(m * len(weights) + 1))
    for area, values in by_area.items():
        assert min(values) >= profile_value(hull, m, F(area, m))
    assert max(profile_value(hull, m, F(a, m))
               for a in by_area) == grid_peak

    # A non-geometric endpoint distribution.
    weights2 = [5, 1, 7]
    tails2 = normalized_tails(weights2)
    hull2 = lower_hull(tails2)
    for hs in product(range(4), repeat=3):
        if hs[0] <= hs[1] <= hs[2]:
            mean_h = F(sum(hs), 3)
            mean_tail = sum((tails2[h] for h in hs), F(0)) / 3
            assert mean_tail >= envelope(hull2, mean_h)
            states += 1
    assert states == 70 + comb(6, 3) == 90

    # Harmonic convex-minorant criterion, in exact arithmetic.
    mm, ll, rr = 12, 3, 14
    phi = [max(F(0), F(1, ll * (1 + q)) - F(1, mm))
           for q in range(rr + 1)]
    # A nonnegative perturbation above the barrier; retain a zero endpoint.
    data = [phi[q] + F((7 * q + 3) % 5, 100) for q in range(rr + 1)]
    data[-1] = F(0)
    hh = lower_hull(data)
    for den in range(1, 9):
        for num in range(rr * den + 1):
            x = F(num, den)
            phix = max(F(0), F(1, ll) / (1 + x) - F(1, mm))
            assert envelope(hh, x) >= phix
            assert profile_value(hh, mm, x) >= F(mm, ll)
    return states


def endpoint_weight_barriers() -> tuple[F, F]:
    m = 8
    delta = [1] + [0] * 7
    assert lower_hull(normalized_tails(delta)) == [
        (0, F(1)), (1, F(0)), (8, F(0))]
    delta_floor = floor_value(delta, m)
    assert delta_floor == 2

    geometric = [2 ** (m - 1 - i) for i in range(m)]
    assert all(geometric[i] ** 2 == geometric[i - 1] * geometric[i + 1]
               for i in range(1, m - 1))
    tails = normalized_tails(geometric)
    # Geometric tails are convex and equal their lower convex envelope.
    assert lower_hull(tails) == list(enumerate(tails))
    geometric_floor = floor_value(geometric, m)
    assert geometric_floor == F(622, 85)  # 7.317647058823529...
    q = 3
    assert geometric_floor <= (1 + q) * (1 + m * tails[q])
    return delta_floor, geometric_floor


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


def circle_module_audit(m: int = 4) -> tuple[int, int, int, int, int]:
    u, v = (F(-1), F(0)), (F(1), F(0))
    upper = [circle_point(i) for i in range(1, m + 1)]
    lower = [circle_point(-(m + i)) for i in range(1, m + 1)]
    points = [u, v] + upper + lower
    n = len(points)
    assert len({p[0] for p in points}) == n
    assert all(det(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(n), 3))

    caps: list[tuple[int, ...]] = []
    cups: list[tuple[int, ...]] = []
    faces = 0
    for mask in range(1, 1 << n):
        ids = tuple(i for i in range(n) if mask >> i & 1)
        subset = [points[i] for i in ids]
        assert hull_size(subset) == len(subset)
        faces += 1
        if is_cap(subset):
            caps.append(ids)
        if is_cup(subset):
            cups.append(ids)
    assert faces == (1 << n) - 1

    module_caps = []
    module_cups = []
    for mask in range(1 << m):
        cap_ids = (0, 1) + tuple(2 + i for i in range(m) if mask >> i & 1)
        cup_ids = (0, 1) + tuple(2 + m + i for i in range(m)
                                 if mask >> i & 1)
        assert is_cap([points[i] for i in cap_ids])
        assert is_cup([points[i] for i in cup_ids])
        module_caps.append(cap_ids)
        module_cups.append(cup_ids)
    unions = {tuple(sorted(set(a) | set(b)))
              for a in module_caps for b in module_cups}
    assert len(module_caps) == len(module_cups) == 1 << m
    assert len(unions) == 1 << (2 * m)
    assert len(unions) * 4 > faces

    rm = 1 + m + comb(m, 2)
    assert len(caps) <= (1 << (m + 2)) * rm
    assert len(cups) <= (1 << (m + 2)) * rm
    assert F(len(caps) * len(cups), faces) <= 8 * rm * rm
    return n, len(caps), len(cups), faces, len(unions)


def wall(a: Point, b: Point) -> F:
    assert a[1] != b[1]
    return -(a[0] - b[0]) / (a[1] - b[1])


def row_major_audit(n: int = 8, m: int = 8) -> tuple[int, int, int]:
    xx = 1000
    eps = F(1, xx ** 6)
    # n variable left endpoints and one fixed right root.
    aa = [(F(i), F(-i * i)) for i in range(n + 1)]
    bb = [(F(xx) + eps * j, F(xx * xx) + eps * eps * j * j)
          for j in range(m)]
    points = aa + bb
    assert all(det(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(n + 1 + m), 3))

    cross_all = [[wall(aa[i], bb[j]) for j in range(m)]
                 for i in range(n + 1)]
    cross = cross_all[:n]
    # The fixed-root row is strictly later and can remain uncrossed.
    assert max(cross[-1]) < min(cross_all[n])
    for i in range(n - 1):
        assert max(cross[i]) < min(cross[i + 1])

    internal_a = [wall(aa[i], aa[j])
                  for i, j in combinations(range(n + 1), 2)
                  if aa[i][1] != aa[j][1]]
    internal_b = [wall(bb[i], bb[j]) for i, j in combinations(range(m), 2)]
    flat_cross = [x for row in cross for x in row]
    assert min(internal_a) > max(flat_cross)
    assert max(internal_b) < min(flat_cross)

    assert all(det(aa[i], aa[j], aa[k]) < 0
               for i, j, k in combinations(range(n + 1), 3))
    degree = [0] * n
    for mask in range(1, 1 << n):
        ids = [i for i in range(n) if mask >> i & 1] + [n]
        assert is_cap([aa[i] for i in ids])
        degree[min(i for i in ids if i < n)] += 1
    assert degree == [2 ** (n - 1 - i) for i in range(n)]
    return n, m, len(flat_cross)


def main() -> None:
    states = ferrers_audit()
    delta, geometric = endpoint_weight_barriers()
    circle = circle_module_audit()
    rows = row_major_audit()
    print(
        "PASS: Ferrers floor/peak theorem and endpoint barriers; "
        f"states={states}, delta_floor={delta}, "
        f"geometric_floor={float(geometric):.12f}, circle={circle}, "
        f"row_major={rows}"
    )


if __name__ == "__main__":
    main()
