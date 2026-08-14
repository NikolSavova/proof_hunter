#!/usr/bin/env python3
"""Exact affine-convex-lattice and deletion/variance verifier.

The input is a JSON certificate containing integral coordinates under
``macros[str(n)]["points"]`` (the growing-state search format).  For selected
sizes this script enumerates every convex subset, reconstructs its closure,
and verifies the Boolean-interval and deletion identities with integers.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


Point = tuple[int, int]


def orient(a: Point, b: Point, c: Point) -> int:
    value = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return (value > 0) - (value < 0)


def convex_hull(points: Sequence[Point], indices: Sequence[int]) -> list[int]:
    selected = sorted(indices, key=lambda i: (points[i], i))
    if len(selected) <= 1:
        return selected

    def half(items: Iterable[int]) -> list[int]:
        out: list[int] = []
        for item in items:
            while len(out) >= 2 and orient(points[out[-2]], points[out[-1]], points[item]) <= 0:
                out.pop()
            out.append(item)
        return out

    lower = half(selected)
    upper = half(reversed(selected))
    return lower[:-1] + upper[:-1]


def is_convex(points: Sequence[Point], indices: Sequence[int]) -> bool:
    return len(indices) <= 2 or len(convex_hull(points, indices)) == len(indices)


def inside_hull(points: Sequence[Point], hull: Sequence[int], p: int) -> bool:
    if len(hull) < 3:
        return p in hull
    signs = [orient(points[hull[i]], points[hull[(i + 1) % len(hull)]], points[p]) for i in range(len(hull))]
    return all(value > 0 for value in signs) or all(value < 0 for value in signs)


def closure_mask(points: Sequence[Point], face: Sequence[int]) -> int:
    hull = convex_hull(points, face)
    if len(hull) < 3:
        return sum(1 << value for value in face)
    return sum(1 << p for p in range(len(points)) if p in face or inside_hull(points, hull, p))


def frac(numerator: int, denominator: int) -> str:
    return str(Fraction(numerator, denominator))


def analyze(points: Sequence[Point], expected_profile: Sequence[int] | None = None) -> dict[str, object]:
    n = len(points)
    max_degree = n if expected_profile is None else max(i for i, value in enumerate(expected_profile) if value)
    profile = [0] * (n + 1)
    joint: dict[tuple[int, int], int] = {}
    faces: list[tuple[int, int, int]] = []  # mask, h, i
    for h in range(max_degree + 1):
        for face in itertools.combinations(range(n), h):
            if not is_convex(points, face):
                continue
            mask = sum(1 << value for value in face)
            closed = closure_mask(points, face)
            interior = closed.bit_count() - h
            profile[h] += 1
            joint[(h, interior)] = joint.get((h, interior), 0) + 1
            faces.append((mask, h, interior))
    if expected_profile is not None:
        padded = list(expected_profile) + [0] * (n + 1 - len(expected_profile))
        padded[0] = 1
        if profile != padded:
            raise AssertionError((profile, padded))

    v = len(faces)
    m1 = sum(h for _, h, _ in faces)
    m2 = sum(h * h for _, h, _ in faces)
    interior_sum = sum(interior for _, _, interior in faces)
    omitted_sum = sum(n - h - interior for _, h, interior in faces)

    # Boolean intervals [ext(K),K] partition the Boolean lattice, coefficient
    # by coefficient and at t=1.
    boolean_coefficients = [0] * (n + 1)
    weighted_y = weighted_y2_plus_i = 0
    for _, h, interior in faces:
        weight = 1 << interior
        y = 2 * h + interior
        weighted_y += weight * y
        weighted_y2_plus_i += weight * (y * y + interior)
        for extra in range(interior + 1):
            boolean_coefficients[h + extra] += math.comb(interior, extra)
    target = [math.comb(n, degree) for degree in range(n + 1)]
    if boolean_coefficients != target:
        raise AssertionError("Boolean-interval polynomial identity failed")
    if weighted_y != n * (1 << n):
        raise AssertionError("first differentiated Boolean identity failed")
    if weighted_y2_plus_i != (n * n + n) * (1 << n):
        raise AssertionError("second differentiated Boolean identity failed")

    # Direct deletion arrays.  Empty face is retained in every deletion.
    deletion_v = [0] * n
    deletion_m = [0] * n
    for mask, h, _ in faces:
        for p in range(n):
            if not (mask >> p) & 1:
                deletion_v[p] += 1
                deletion_m[p] += h
    total_deletion_v = sum(deletion_v)
    total_deletion_m = sum(deletion_m)
    if total_deletion_v != n * v - m1:
        raise AssertionError("deletion count identity failed")
    if total_deletion_m != n * m1 - m2:
        raise AssertionError("weighted deletion first moment identity failed")

    # E up-degree equals E down-degree for every finite face poset.  Since an
    # addable point is necessarily outside the current hull, the residual is
    # the average number of blocked exterior points, witnessed by rooted
    # planar circuits.
    blocked_sum = omitted_sum - m1
    if blocked_sum < 0:
        raise AssertionError("more addable than exterior points")

    variance_num = m2 * v - m1 * m1
    deletion_gap_num = m1 * total_deletion_v - v * total_deletion_m
    if deletion_gap_num != variance_num:  # same denominator v*total_deletion_v
        raise AssertionError("variance/deletion gap identity failed")

    # From 2^n=V E[2^i] and Jensen: log V <= mu+E[omitted].  The display uses
    # floating point only after the exact identities have passed.
    mu = m1 / v
    variance = variance_num / (v * v)
    mean_interior = interior_sum / v
    mean_omitted = omitted_sum / v
    mean_blocked = blocked_sum / v
    return {
        "n": n,
        "profile_including_empty": profile,
        "V": v,
        "M1": m1,
        "M2": m2,
        "mu": frac(m1, v),
        "mu_decimal": mu,
        "mu_minus_log2_n": mu - math.log2(n),
        "variance": frac(variance_num, v * v),
        "variance_decimal": variance,
        "mean_interior": frac(interior_sum, v),
        "mean_omitted": frac(omitted_sum, v),
        "mean_blocked_exterior": frac(blocked_sum, v),
        "boolean_weight_sum": 1 << n,
        "boolean_coefficients": boolean_coefficients,
        "deletion_V": deletion_v,
        "deletion_M1": deletion_m,
        "weighted_deletion_mean": frac(total_deletion_m, total_deletion_v),
        "mean_minus_weighted_deletion_mean": frac(deletion_gap_num, v * total_deletion_v),
        "variance_over_n_minus_mu": frac(variance_num, v * total_deletion_v),
        "log2_V": math.log2(v),
        "jensen_coverage_upper": mu + mean_omitted,
        "jensen_slack": mu + mean_omitted - math.log2(v),
        "qms_rhs": 0.5 * mu * mu,
        "qms_gap": math.log2(v) - 0.5 * mu * mu,
        "low_mean_coverage_target": 0.5 * mu * mu - mu,
        "joint_h_i": {f"{h},{i}": count for (h, i), count in sorted(joint.items())},
    }


def verify_projection_decomposition(
    points: Sequence[Point],
    clusters: Sequence[Sequence[int]],
    directions: Sequence[Sequence[int]],
) -> dict[str, object]:
    """Verify an equal-size 3-decomposition by exact projection orders."""
    if len(clusters) != 3 or len({len(cluster) for cluster in clusters}) != 1:
        raise ValueError("standard 3-decomposition needs three equal clusters")
    label = {point: block for block, cluster in enumerate(clusters) for point in cluster}
    if set(label) != set(range(len(points))):
        raise ValueError("clusters do not partition the points")
    rows = []
    middle_seen = set()
    for direction in directions:
        dx, dy = direction
        values = [points[i][0] * dx + points[i][1] * dy for i in range(len(points))]
        if len(set(values)) != len(values):
            raise AssertionError("projection direction has a tie")
        order = sorted(range(len(points)), key=values.__getitem__)
        labels = [label[index] for index in order]
        compressed = [value for i, value in enumerate(labels) if i == 0 or labels[i - 1] != value]
        if len(compressed) != 3 or set(compressed) != {0, 1, 2}:
            raise AssertionError((direction, order, labels))
        middle_seen.add(compressed[1])
        rows.append({"direction": list(direction), "point_order": order, "block_order": compressed})
    if middle_seen != {0, 1, 2}:
        raise AssertionError("the three directions do not expose all middle clusters")
    return {"clusters": [list(cluster) for cluster in clusters], "projections": rows, "status": "PASS"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--sizes", default="9,17,20")
    parser.add_argument("--direct-n9", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    source = json.loads(args.input.read_text())
    sizes = [int(value) for value in args.sizes.split(",") if value]
    results = []
    for n in sizes:
        macro = source["macros"][str(n)]
        points = tuple(tuple(value) for value in macro["points"])
        profile = [1] + list(macro["convex_profile"])[1:]
        result = analyze(points, profile)
        results.append(result)
        print(json.dumps({key: result[key] for key in (
            "n", "V", "mu", "variance", "mean_omitted", "mean_blocked_exterior",
            "mu_minus_log2_n", "jensen_slack", "qms_gap")}, sort_keys=True))
    direct = None
    if args.direct_n9 is not None:
        record = json.loads(args.direct_n9.read_text())
        sorted_points = sorted(tuple(point) for point in record["coordinates_as_stored"])
        direct_stats = analyze(sorted_points, [1] + list(record["profile"])[1:])
        clusters = ((0, 1, 5), (2, 3, 4), (6, 7, 8))
        directions = (
            (867574037, -497308043),
            (910323393, 413897717),
            (505573743, 862783397),
        )
        direct = {
            "source_mode": record["mode"],
            "coordinates_sorted": [list(point) for point in sorted_points],
            "lattice": direct_stats,
            "three_decomposition": verify_projection_decomposition(
                sorted_points, clusters, directions
            ),
        }
        print(json.dumps({
            "direct_n9_V": direct_stats["V"],
            "direct_n9_mu": direct_stats["mu"],
            "direct_n9_variance": direct_stats["variance"],
            "direct_n9_three_decomposition": direct["three_decomposition"]["status"],
        }, sort_keys=True))
    certificate = {
        "schema": "exact integer/rational affine closure-lattice audit",
        "results": results,
        "direct_n9_lex_minimizer": direct,
    }
    if args.output is not None:
        args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
