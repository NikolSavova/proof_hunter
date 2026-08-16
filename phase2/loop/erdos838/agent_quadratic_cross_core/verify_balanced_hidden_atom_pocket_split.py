#!/usr/bin/env python3
"""Exact finite audit for BALANCED_HIDDEN_ATOM_POCKET_SPLIT.md."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import ceil, log2


Point = tuple[Fraction, Fraction]


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def strict_ccw_convex(points: tuple[Point, ...]) -> bool:
    if len(points) < 3:
        return True
    signs = []
    for i in range(len(points)):
        value = orient(points[i - 1], points[i], points[(i + 1) % len(points)])
        if value == 0:
            return False
        signs.append(value > 0)
    return all(signs) or not any(signs)


def convex_hull(points: frozenset[Point]) -> tuple[Point, ...]:
    """Andrew monotone chain, retaining no collinear boundary points."""
    ordered = sorted(points)
    if len(ordered) <= 1:
        return tuple(ordered)

    def half(seq: list[Point]) -> list[Point]:
        out: list[Point] = []
        for p in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    lower = half(ordered)
    upper = half(list(reversed(ordered)))
    return tuple(lower[:-1] + upper[:-1])


def is_convex_position(points: frozenset[Point]) -> bool:
    return len(convex_hull(points)) == len(points)


def cyclic_audit() -> dict[str, int]:
    checked = 0
    alternatives = [0, 0]
    eta = Fraction(1, 2)
    for m in range(4, 9):
        for p in product(range(4), repeat=m):
            s = sum(p)
            if not s:
                continue
            windows = [p[(i - 1) % m] + p[i] + p[(i + 1) % m] for i in range(m)]
            big_m = max(windows)
            separated = sum(
                p[i] * p[j]
                for i in range(m)
                for j in range(m)
                if i != j and (i - j) % m not in (1, m - 1)
            )
            bad = sum(p[i] * windows[i] for i in range(m))
            assert separated == s * s - bad
            assert separated >= s * (s - big_m)
            if separated >= eta * s * s:
                alternatives[0] += 1
            else:
                assert big_m > (1 - eta) * s
                alternatives[1] += 1
            checked += 1
    return {
        "weight_vectors": checked,
        "dispersed": alternatives[0],
        "three_window": alternatives[1],
    }


def octagon_and_pockets() -> tuple[tuple[Point, ...], tuple[Point, ...]]:
    raw = (
        (0, 0),
        (4, -1),
        (8, 1),
        (10, 5),
        (8, 9),
        (4, 11),
        (0, 9),
        (-2, 5),
    )
    f = tuple((Fraction(x), Fraction(y)) for x, y in raw)
    assert strict_ccw_convex(f)

    # Move the midpoint of each directed edge a small distance to its right.
    # A CCW polygon lies to the left of every directed support line.
    eps = Fraction(1, 1000)
    qs: list[Point] = []
    for i, a in enumerate(f):
        b = f[(i + 1) % len(f)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        midpoint = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        q = (midpoint[0] + eps * dy, midpoint[1] - eps * dx)
        assert orient(a, b, q) < 0
        for j, c in enumerate(f):
            d = f[(j + 1) % len(f)]
            if j != i:
                assert orient(c, d, q) > 0
        assert is_convex_position(frozenset(f + (q,)))
        qs.append(q)
    return f, tuple(qs)


def geometric_and_load_audit() -> dict[str, int]:
    f, qs = octagon_and_pockets()
    m = len(f)
    faces: dict[frozenset[Point], list[tuple[int, int]]] = {}
    descriptions = 0
    for i in range(m):
        for j in range(m):
            if i == j or (i - j) % m in (1, m - 1):
                continue
            target = frozenset(f + (qs[i], qs[j]))
            assert is_convex_position(target)
            faces.setdefault(target, []).append((i, j))
            descriptions += 1

            # The directed support chords recover their own pocket atoms.
            beyond_i = {x for x in target if orient(f[i], f[(i + 1) % m], x) < 0}
            beyond_j = {x for x in target if orient(f[j], f[(j + 1) % m], x) < 0}
            assert beyond_i == {qs[i]}
            assert beyond_j == {qs[j]}

    # Reversing the ordered atom pair is the only collision in this model.
    max_description_fibre = max(map(len, faces.values()))
    assert max_description_fibre == 2
    output_rank = m + 2
    assert max_description_fibre < output_rank**4

    # Give each atom a distinct light integer completion weight <= T and
    # audit the weighted target load against s^4 T^2.
    threshold = 11
    weights = [1 + (7 * i) % threshold for i in range(m)]
    loads: dict[frozenset[Point], int] = {}
    for target, pairs in faces.items():
        loads[target] = sum(weights[i] * weights[j] for i, j in pairs)
    assert max(loads.values()) <= max_description_fibre * threshold**2
    assert max(loads.values()) < output_rank**4 * threshold**2
    return {
        "ordered_separated_descriptions": descriptions,
        "distinct_faces": len(faces),
        "max_description_fibre": max_description_fibre,
        "max_weighted_load": max(loads.values()),
    }


def heavy_and_telescope_audit() -> dict[str, int]:
    cases = 0
    eta = Fraction(1, 2)
    threshold = 7
    for m in range(4, 9):
        # Atom weights, including values above the light threshold.
        for betas in product((1, 3, 7, 8, 13), repeat=m):
            total = sum(betas)
            heavy = sum(x for x in betas if x > threshold)
            if 2 * heavy >= total:
                assert heavy * 2 >= total
            else:
                light = tuple(x if x <= threshold else 0 for x in betas)
                s = sum(light)
                assert 2 * s > total
                windows = [light[(i - 1) % m] + light[i] + light[(i + 1) % m] for i in range(m)]
                separated = sum(
                    light[i] * light[j]
                    for i in range(m)
                    for j in range(m)
                    if i != j and (i - j) % m not in (1, m - 1)
                )
                if separated < eta * s * s:
                    assert max(windows) > (1 - eta) * s
                    assert 4 * max(windows) > total
                else:
                    assert 4 * separated >= total * total // 2
            cases += 1

    telescope_rows = 0
    for r in range(2, 10001):
        depth = ceil(log2(r))
        loss = 4**depth
        assert loss <= 4 * r * r
        telescope_rows += 1
    return {"heavy_light_cases": cases, "telescope_rows": telescope_rows}


def main() -> None:
    print("CYCLIC", cyclic_audit())
    print("GEOMETRY_AND_LOAD", geometric_and_load_audit())
    print("HEAVY_AND_TELESCOPE", heavy_and_telescope_audit())
    print("ALL_EXACT_CHECKS_PASSED")


if __name__ == "__main__":
    main()
