#!/usr/bin/env python3
"""Exact checks for CHRONOLOGY_ONE_BIT_REPAIR_SPLICE_HELLY_GATE.md."""

from __future__ import annotations

import itertools
from fractions import Fraction


Point = tuple[Fraction, Fraction]
Inequality = tuple[Fraction, Fraction, Fraction]


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points: list[Point]) -> list[Point]:
    points = sorted(set(points))

    def half(seq: list[Point]) -> list[Point]:
        out: list[Point] = []
        for point in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], point) <= 0:
                out.pop()
            out.append(point)
        return out

    return half(points)[:-1] + half(list(reversed(points)))[:-1]


def convex(points: list[Point]) -> bool:
    return len(points) <= 3 or len(hull(points)) == len(points)


def line_value(a: Point, b: Point) -> Inequality:
    """Coefficients A,B,C for orient(a,b,(x,y))."""
    return (
        -(b[1] - a[1]),
        b[0] - a[0],
        (b[1] - a[1]) * a[0] - (b[0] - a[0]) * a[1],
    )


def ear_cell(poly: list[Point], index: int) -> list[Inequality]:
    """Strict inequalities for insertion between index and index+1."""
    k = len(poly)
    previous = poly[(index - 1) % k]
    left = poly[index]
    right = poly[(index + 1) % k]
    following = poly[(index + 2) % k]
    first = line_value(previous, left)
    middle = tuple(-value for value in line_value(left, right))
    last = line_value(right, following)
    return [first, middle, last]  # type: ignore[list-item]


def strict_halfplanes(conditions: list[Inequality]) -> Point | None:
    """Exact Fourier--Motzkin feasibility for A*x+B*y+C>0."""
    lowers: list[tuple[Fraction, Fraction]] = []
    uppers: list[tuple[Fraction, Fraction]] = []
    in_x: list[tuple[Fraction, Fraction]] = []
    for a, b, c in conditions:
        if b > 0:
            lowers.append((-a / b, -c / b))
        elif b < 0:
            uppers.append((-a / b, -c / b))
        else:
            in_x.append((a, c))
    for lower_m, lower_b in lowers:
        for upper_m, upper_b in uppers:
            in_x.append((upper_m - lower_m, upper_b - lower_b))

    lower_x: Fraction | None = None
    upper_x: Fraction | None = None
    for a, c in in_x:
        if a == 0:
            if c <= 0:
                return None
        elif a > 0:
            bound = -c / a
            lower_x = bound if lower_x is None else max(lower_x, bound)
        else:
            bound = -c / a
            upper_x = bound if upper_x is None else min(upper_x, bound)
    if lower_x is not None and upper_x is not None and lower_x >= upper_x:
        return None
    if lower_x is None and upper_x is None:
        x = Fraction(0)
    elif lower_x is None:
        x = upper_x - 1  # type: ignore[operator]
    elif upper_x is None:
        x = lower_x + 1
    else:
        x = (lower_x + upper_x) / 2

    lower_y = [m * x + b for m, b in lowers]
    upper_y = [m * x + b for m, b in uppers]
    if lower_y and upper_y:
        y = (max(lower_y) + min(upper_y)) / 2
    elif lower_y:
        y = max(lower_y) + 1
    elif upper_y:
        y = min(upper_y) - 1
    else:
        y = Fraction(0)
    point = (x, y)
    assert all(a * x + b * y + c > 0 for a, b, c in conditions)
    return point


def shear(point: Point) -> Point:
    return point[0] + point[1] / 997, point[1]


def audit_entropy_tradeoff() -> tuple[int, int]:
    # Check the integer core of s-log_2(s)>=1 and the second branch of (5).
    for d_over_k in range(2, 513):
        for selected in range(1, 2 * d_over_k + 1):
            if selected <= d_over_k:
                assert 2 ** (selected - 1) >= selected
            else:
                # selected >= log_2(D)+1, written without floating point.
                assert 2 ** (selected - 1) >= d_over_k

    # A live-scale exact calibration: d=2^12, K=2^4, q=16.
    d, kappa, roles = 2 ** 12, 2 ** 4, 16
    d_over_k = d // kappa
    per_role_bits = d_over_k.bit_length()  # log_2(D)+1 = 9
    assert per_role_bits == 9
    assert roles * per_role_bits == 144
    return per_role_bits, roles * per_role_bits


def audit_three_ear_obstruction(q: int = 12) -> tuple[int, int, int]:
    f = Fraction
    a, b, c = (f(0), f(0)), (f(6), f(0)), (f(0), f(6))
    d, e, ff = (f(3), f(-10)), (f(13), f(3)), (f(-10), f(13))
    outer = [a, b, c, d, e, ff]
    epsilon = f(1, 100000 * q * q)
    completion = [
        (f(1) + epsilon * t, f(2) + epsilon * t * t)
        for t in range(1, q + 1)
    ]
    points = outer + completion

    assert all(orient(points[i], points[j], points[k]) != 0
               for i, j, k in itertools.combinations(range(len(points)), 3))
    assert all(z[0] > 0 and z[1] > 0 and z[0] + z[1] < 6
               for z in completion)
    assert convex(completion)

    releases = [hull([a, b, c, point]) for point in (d, e, ff)]
    assert all(len(release) == 4 and convex(release) for release in releases)
    for z in completion:
        assert not convex([a, b, c, z])
        for release in releases:
            assert not convex(release + [z])
    for start in range(q):
        assert convex(completion[start:])
        for release in releases:
            assert not convex(release + completion[start:])

    # With labels a,b,c,z_1,...,z_q,d,e,f, the designated fixed circuit is
    # the canonical lexicographically first bad four-set at every level.
    ordered = [a, b, c] + completion + [d, e, ff]
    for start in range(q):
        completion_indices = list(range(3 + start, 3 + q))
        for extra in range(3):
            ground = [0, 1, 2, 3 + q + extra] + completion_indices
            bad_fours = [
                indices
                for indices in itertools.combinations(sorted(ground), 4)
                if not convex([ordered[index] for index in indices])
            ]
            assert min(bad_fours) == (0, 1, 2, 3 + start)

    # No triple of ear cells intersects; every pair of released faces has a
    # simultaneous repair point.  All calculations are exact rationals.
    triple_feasible = 0
    for indices in itertools.product(range(4), repeat=3):
        conditions = sum(
            (ear_cell(release, index)
             for release, index in zip(releases, indices)),
            [],
        )
        if strict_halfplanes(conditions) is not None:
            triple_feasible += 1
    assert triple_feasible == 0

    pair_witnesses = 0
    for left, right in itertools.combinations(releases, 2):
        witness: Point | None = None
        for i, j in itertools.product(range(4), repeat=2):
            witness = strict_halfplanes(ear_cell(left, i) + ear_cell(right, j))
            if witness is not None:
                break
        assert witness is not None
        assert convex(left + [witness]) and convex(right + [witness])
        pair_witnesses += 1
    assert pair_witnesses == 3

    # One explicit generic chart, preserving every orientation.
    chart_points = [shear(point) for point in points]
    assert len({point[0] for point in chart_points}) == len(chart_points)
    assert all(
        (orient(points[i], points[j], points[k]) > 0)
        == (orient(chart_points[i], chart_points[j], chart_points[k]) > 0)
        for i, j, k in itertools.combinations(range(len(points)), 3)
    )
    return len(points), pair_witnesses, triple_feasible


def main() -> None:
    per_role, total = audit_entropy_tradeoff()
    points, pair_witnesses, triple_feasible = audit_three_ear_obstruction()
    print(
        "PASS: repair tradeoff per-role/16-role=%d/%d bits; "
        "fixed-circuit gadget points=%d pair-repairs=%d triple-cells=%d"
        % (per_role, total, points, pair_witnesses, triple_feasible)
    )


if __name__ == "__main__":
    main()
