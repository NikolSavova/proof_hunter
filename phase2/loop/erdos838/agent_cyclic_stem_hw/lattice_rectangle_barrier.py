#!/usr/bin/env python3
"""Exact audit for the nested planar closure-rectangle barrier.

The construction and every predicate below use integers.  No floating-point
geometry is used.  The large profile verifies the claimed complete repair
rectangle and closure chain.  A smaller profile also exhausts every subset in
the relevant lattice intervals.
"""

from __future__ import annotations

from itertools import combinations
import json
from pathlib import Path


Point = tuple[int, int]


def cross(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def convex_hull(points: list[Point], indices: list[int]) -> list[int]:
    ids = sorted(set(indices), key=lambda i: (points[i][0], points[i][1]))
    if len(ids) <= 1:
        return ids
    lower: list[int] = []
    for i in ids:
        while len(lower) >= 2 and cross(points[lower[-2]], points[lower[-1]], points[i]) <= 0:
            lower.pop()
        lower.append(i)
    upper: list[int] = []
    for i in reversed(ids):
        while len(upper) >= 2 and cross(points[upper[-2]], points[upper[-1]], points[i]) <= 0:
            upper.pop()
        upper.append(i)
    return lower[:-1] + upper[:-1]


def in_hull(points: list[Point], q: int, hull: list[int]) -> bool:
    if len(hull) == 0:
        return False
    if len(hull) == 1:
        return points[q] == points[hull[0]]
    if len(hull) == 2:
        a, b = points[hull[0]], points[hull[1]]
        return cross(a, b, points[q]) == 0 and min(a[0], b[0]) <= points[q][0] <= max(a[0], b[0]) and min(a[1], b[1]) <= points[q][1] <= max(a[1], b[1])
    return all(cross(points[hull[k]], points[hull[(k + 1) % len(hull)]], points[q]) >= 0 for k in range(len(hull)))


def closure(points: list[Point], indices: list[int], universe: list[int] | None = None) -> set[int]:
    hull = convex_hull(points, indices)
    if universe is None:
        universe = list(range(len(points)))
    return {q for q in universe if in_hull(points, q, hull)}


def construction(common_size: int, alternatives: int):
    """Return R and a totally nested sequence y_1,...,y_(2M).

    R has ``common_size`` points.  A source and a repaired target both have
    rank common_size+1.
    """
    assert common_size >= 2 and alternatives >= 1
    B = 10 * (common_size + alternatives) ** 3
    z_values = [-B] + list(range(1, common_size - 1)) + [B]
    common = [(z, z * z - B * B) for z in z_values]
    nested = [(t * t, t) for t in range(1, 2 * alternatives + 1)]
    points = common + nested
    R = list(range(common_size))
    Y = list(range(common_size, common_size + 2 * alternatives))
    X = Y[:alternatives]
    P = Y[alternatives:]
    return points, R, Y, X, P, B


def assert_general_position(points: list[Point]) -> None:
    for a, b, c in combinations(range(len(points)), 3):
        assert cross(points[a], points[b], points[c]) != 0, (a, b, c)


def direct_chain_audit(common_size: int, alternatives: int) -> dict[str, int]:
    points, R, Y, X, P, B = construction(common_size, alternatives)
    assert_general_position(points)
    all_ids = list(range(len(points)))

    # K_t = cl(R+y_t) is exactly R plus the first t nested alternatives,
    # and ext(K_t)=R+y_t.
    for t, y in enumerate(Y, start=1):
        h = convex_hull(points, R + [y])
        assert set(h) == set(R + [y])
        assert closure(points, R + [y], all_ids) == set(R + Y[:t])

    # Every lower/upper pair is a singleton-ear exterior repair.  The later
    # point hides the earlier one, leaving R plus that later point extreme.
    for x in X:
        for p in P:
            h = convex_hull(points, R + [x, p])
            assert set(h) == set(R + [p])

    # No common-frame convex face can contain two nested alternatives.
    for a, b in combinations(Y, 2):
        assert set(convex_hull(points, R + [a, b])) == set(R + [b])

    rank = common_size + 1
    return {
        "common_size": common_size,
        "rank": rank,
        "alternatives_each_side": alternatives,
        "ground_size": len(points),
        "coordinate_scale_B": B,
        "repair_records": alternatives * alternatives,
        "common_frame_faces": 2 * alternatives + 1,
        "weighted_C4_numerator": alternatives**4,
        "weighted_C4_denominator": alternatives**4,
    }


def exhaustive_interval_audit(common_size: int, alternatives: int) -> dict[str, list[int] | int]:
    points, R, Y, _, P, _ = construction(common_size, alternatives)
    assert_general_position(points)
    counts: list[int] = []
    expected: list[int] = []
    for j, p in enumerate(P, start=1):
        allowed = Y[: alternatives + j]
        closed_masks: list[int] = []
        for mask in range(1 << len(allowed)):
            candidate = R + [allowed[k] for k in range(len(allowed)) if (mask >> k) & 1]
            if closure(points, candidate, R + allowed) == set(candidate):
                closed_masks.append(mask)
        # Precisely the prefix masks 0,1,3,7,... occur.
        prefix_masks = [0] + [(1 << k) - 1 for k in range(1, len(allowed) + 1)]
        assert closed_masks == prefix_masks
        counts.append(len(closed_masks))
        expected.append(alternatives + j + 1)
    assert counts == expected
    return {
        "common_size": common_size,
        "alternatives_each_side": alternatives,
        "interval_closed_set_counts": counts,
        "expected_counts": expected,
    }


def capped_profile(rank: int) -> dict[str, int | str]:
    # This is the asymptotic specialization in the report.  It is an exact
    # arithmetic certificate; materializing M=2^(3r) points is unnecessary.
    assert rank >= 2
    M = 1 << (3 * rank)
    n = rank - 1 + 2 * M
    d = n // (1 << rank)
    assert d == 1 << (2 * rank + 1)
    assert d <= M
    records = M * d
    targets = M + d + 1
    fibre_floor = (records + targets - 1) // targets
    assert fibre_floor >= 1 << (2 * rank)
    weighted_numerator = fibre_floor
    weighted_denominator = 1 << rank
    assert weighted_numerator >= (1 << rank) * weighted_denominator
    return {
        "rank": rank,
        "M": M,
        "ground_size": n,
        "cap_d=floor(n/2^r)": d,
        "selected_records": records,
        "selected_interval_faces": targets,
        "minimum_maximum_fibre": fibre_floor,
        "minimum_weighted_load_as_fraction": f"{weighted_numerator}/{weighted_denominator}",
    }


def main() -> None:
    certificate = {
        "construction": "R_z=(z,z^2-B^2), y_t=(t^2,t)",
        "small_exhaustive": exhaustive_interval_audit(common_size=5, alternatives=6),
        "large_exact_geometry": direct_chain_audit(common_size=8, alternatives=64),
        "capped_arithmetic": capped_profile(rank=8),
    }
    saved_path = Path(__file__).with_name("lattice_rectangle_barrier_certificate.json")
    if saved_path.exists():
        with saved_path.open(encoding="utf-8") as handle:
            assert certificate == json.load(handle)
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
