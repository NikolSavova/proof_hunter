#!/usr/bin/env python3
"""Exact audit of the rational nested-cap counterexample to pointwise RMC."""

from __future__ import annotations

import json
import importlib.util
import math
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
Point = tuple[Q, Q]
ENDPOINT_SOURCE = (
    HERE.parent / "agent_unit_matrix_asymptotic" / "verify_endpoint_span_localization.py"
)


def orient(a: Point, b: Point, c: Point) -> Q:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def convex_hull(points: list[Point]) -> list[Point]:
    ordered = sorted(set(points))
    if len(ordered) <= 1:
        return ordered

    def half(sequence: list[Point]) -> list[Point]:
        result: list[Point] = []
        for point in sequence:
            while len(result) >= 2 and orient(result[-2], result[-1], point) <= 0:
                result.pop()
            result.append(point)
        return result

    lower = half(ordered)
    upper = half(list(reversed(ordered)))
    return lower[:-1] + upper[:-1]


def construction(m: int) -> tuple[list[Point], list[Point], list[Point]]:
    assert m >= 3
    high = [(Q(a), Q(-(a * a))) for a in (-6, -4, -2, 2, 4, 6)]
    low = []
    for i in range(1, m + 1):
        x = Q(-1) + Q(2 * i, m + 1)
        low.append((x, Q(-100) - x * x))
    return sorted(high + low), high, low


def trace_polynomial_cap(m: int) -> Q:
    return Q(1) + Q(m, 2) + Q(m * (m - 1), 8)


def quotient_lower_bound(m: int) -> Q:
    a_m = trace_polynomial_cap(m)
    return Q(1, 64) * Q(3, 2) ** (2 * m - 12) / a_m**3


def prefix_polynomial_cap(size: int) -> Q:
    return Q(1) + Q(size, 2)


def rank_four_quotient_lower_bound(m: int) -> Q:
    return (
        Q(1, 16)
        * Q(3, 2) ** (m - 10)
        / (prefix_polynomial_cap(m - 1) * prefix_polynomial_cap(m - 2))
    )


def is_convex_face(points: list[Point]) -> bool:
    return len(points) <= 2 or len(convex_hull(points)) == len(points)


def brute_normalization_audit(m: int = 8) -> dict[str, object]:
    """Reconstruct every probability and capture factor from definitions."""
    points, high, _ = construction(m)
    n = len(points)
    faces: list[int] = []
    total = Q()
    rank_six = 0
    for mask in range(1 << n):
        selected = [points[i] for i in range(n) if mask >> i & 1]
        if not is_convex_face(selected):
            continue
        faces.append(mask)
        rank = mask.bit_count()
        total += Q(1, 1 << rank)
        if rank == 6:
            rank_six += 1

    point_index = {point: i for i, point in enumerate(points)}
    high_by_x = {int(point[0]): point for point in high}
    selected_mask = sum(1 << point_index[point] for point in high)
    assert selected_mask in faces
    bucket_probability = Q(rank_six, 64) / total

    capture_product = Q(1)
    capture_rows = []
    for radius in (6, 4, 2):
        left_index = point_index[high_by_x[-radius]]
        right_index = point_index[high_by_x[radius]]
        interval = list(range(left_index + 1, right_index))
        denominator = Q()
        numerator = Q()
        for local_mask in range(1 << len(interval)):
            trace = [
                points[interval[j]]
                for j in range(len(interval))
                if local_mask >> j & 1
            ]
            weight = Q(1, 1 << len(trace))
            if is_convex_face(trace):
                denominator += weight
            if is_convex_face([points[left_index], points[right_index], *trace]):
                numerator += weight
        capture = numerator / denominator
        capture_product *= capture
        assert denominator >= Q(3, 2) ** m
        high_count = radius - 2
        assert numerator <= Q(3, 2) ** high_count * trace_polynomial_cap(m)
        capture_rows.append(
            {
                "radius": radius,
                "numerator": str(numerator),
                "denominator": str(denominator),
                "capture": str(capture),
            }
        )

    quotient = bucket_probability / capture_product
    assert quotient >= quotient_lower_bound(m)
    return {
        "m": m,
        "faces": len(faces),
        "half_partition_function": str(total),
        "rank_six_bucket_degree": rank_six,
        "rank_six_bucket_probability": str(bucket_probability),
        "capture_rows": capture_rows,
        "capture_product": str(capture_product),
        "bucket_to_capture_quotient": str(quotient),
    }


def exact_rank_four_audit(m: int) -> dict[str, object]:
    """Use exact reflection matrices and enumerate only rank-four subsets."""
    specification = importlib.util.spec_from_file_location(
        f"endpoint_matrix_audit_{m}", ENDPOINT_SOURCE
    )
    assert specification is not None and specification.loader is not None
    matrix = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(matrix)

    points, high, low = construction(m)
    n = len(points)
    roots = matrix.slope_roots(points)
    scale, forward = matrix.product_half_scaled(n, roots)
    _, backward = matrix.product_half_scaled(n, tuple(reversed(roots)))
    _, total = matrix.endpoint_masses(n, roots, Q(1, 2))

    capture: dict[tuple[int, int], Q] = {}
    for i, j in combinations(range(n), 2):
        cell = Q(forward[j][i] * backward[j][i], scale * scale)
        interval = matrix.interval_face_totals(roots, i, j)[0]
        capture[i, j] = 4 * cell / interval

    rank_four_degree = sum(
        is_convex_face([points[i] for i in indices])
        for indices in combinations(range(n), 4)
    )
    point_index = {point: i for i, point in enumerate(points)}
    high_by_x = {int(point[0]): point for point in high}
    face = tuple(
        sorted(
            (
                point_index[high_by_x[-4]],
                point_index[high_by_x[-2]],
                point_index[low[-2]],
                point_index[low[-1]],
            )
        )
    )
    assert is_convex_face([points[i] for i in face])
    product = capture[face[0], face[3]] * capture[face[1], face[2]]
    bucket_probability = Q(rank_four_degree, 16) / total
    quotient = bucket_probability / product
    return {
        "m": m,
        "n": n,
        "face_indices": list(face),
        "face_x_coordinates": [str(points[i][0]) for i in face],
        "rank_four_bucket_degree": rank_four_degree,
        "half_partition_function": str(total),
        "capture_product": str(product),
        "bucket_probability": str(bucket_probability),
        "bucket_to_capture_quotient": str(quotient),
        "log2_quotient": math.log2(float(quotient)),
        "per_vertex_constant": float(quotient) ** Q(1, 4),
    }


def audit(m: int = 54) -> dict[str, object]:
    points, high, low = construction(m)
    assert len(points) == m + 6
    assert len(set(points)) == m + 6
    assert [point[0] for point in points] == sorted(point[0] for point in points)

    # Exact general position.  This also independently checks the elementary
    # two-translated-parabolas argument in the report.
    for a, b, c in combinations(points, 3):
        assert orient(a, b, c) != 0

    # Every point of each strict cap is a hull vertex.
    assert len(convex_hull(high)) == 6
    assert len(convex_hull(low)) == m

    high_by_x = {int(point[0]): point for point in high}
    witness_count = 0
    for radius in (6, 4, 2):
        left = high_by_x[-radius]
        right = high_by_x[radius]
        assert left[1] == right[1]
        assert all(left[0] < w[0] < right[0] for w in low)
        assert all(w[1] < left[1] for w in low)

        # Any three selected low points make the middle one non-extreme in
        # the hull with the endpoint pair.  This proves the trace cap without
        # enumerating exponentially many traces.
        for i, j, k in combinations(range(m), 3):
            hull_without_middle = convex_hull([left, right, low[i], low[k]])
            assert len(hull_without_middle) == 4
            hull_with_middle = convex_hull([left, right, low[i], low[j], low[k]])
            assert len(hull_with_middle) == 4
            assert low[j] not in hull_with_middle
            witness_count += 1

    # For the asymmetric rank-four face, the selected low endpoint supplies
    # the third low point: two earlier prefix points already hide the latter.
    triangle_witness_count = 0
    for high_x, low_endpoint_index in ((-4, m - 1), (-2, m - 2)):
        left = high_by_x[high_x]
        right = low[low_endpoint_index]
        for i, j in combinations(range(low_endpoint_index), 2):
            without_middle = convex_hull([left, low[i], right])
            assert len(without_middle) == 3
            with_middle = convex_hull([left, low[i], low[j], right])
            assert len(with_middle) == 3
            assert low[j] not in with_middle
            triangle_witness_count += 1

    a_m = trace_polynomial_cap(m)
    trace_uppers = {
        radius: Q(3, 2) ** (radius - 2) * a_m for radius in (6, 4, 2)
    }
    interval_lower = Q(3, 2) ** m
    lambda_uppers = {
        radius: trace_upper / interval_lower
        for radius, trace_upper in trace_uppers.items()
    }
    product_upper = math.prod(lambda_uppers.values(), start=Q(1))
    bucket_probability_lower = Q(1, 64) / Q(3, 2) ** (m + 6)
    quotient = bucket_probability_lower / product_upper
    assert quotient == quotient_lower_bound(m)
    assert quotient > 8**6

    rank_four_quotient = rank_four_quotient_lower_bound(m)
    assert rank_four_quotient > 8**4

    # The base 9/4 beats every polynomial.  These finite checks are only
    # illustrations; the report's limit argument proves arbitrary fixed b.
    polynomial_stress: dict[str, int] = {}
    for b in (0, 4, 20, 100):
        threshold = None
        for size in range(3, 5000):
            if quotient_lower_bound(size) > Q(8**6) * (size + 6) ** b:
                threshold = size
                break
        assert threshold is not None
        polynomial_stress[str(b)] = threshold

    brute = brute_normalization_audit()
    exact_rank_four = [exact_rank_four_audit(size) for size in (21, 22)]
    assert exact_rank_four[0]["per_vertex_constant"] > 8
    assert exact_rank_four[1]["per_vertex_constant"] > 9
    certificate: dict[str, object] = {
        "description": "rational rank-four nested-cap counterexample to every pointwise RMC(C,b)",
        "m": m,
        "n": m + 6,
        "selected_face_rank": 4,
        "asymmetric_endpoint_pairs": [[-4, "w_m"], [-2, "w_(m-1)"]],
        "rank_four_triangle_witnesses_checked": triangle_witness_count,
        "rank_four_bucket_to_capture_quotient_lower": str(rank_four_quotient),
        "rank_four_bucket_to_capture_log2_lower": math.log2(float(rank_four_quotient)),
        "rank_four_RMC_8_0_analytic_threshold_m": next(
            size
            for size in range(3, m + 1)
            if rank_four_quotient_lower_bound(size) > 8**4
        ),
        "rank_four_exact_matrix_audits": exact_rank_four,
        "symmetric_selected_face_rank": 6,
        "endpoint_pairs": [[-6, 6], [-4, 4], [-2, 2]],
        "general_position_triples_checked": math.comb(m + 6, 3),
        "quadrilateral_witnesses_checked": witness_count,
        "A_m": str(a_m),
        "trace_halfweight_uppers": {
            str(radius): str(value) for radius, value in trace_uppers.items()
        },
        "interval_halfweight_lower": str(interval_lower),
        "capture_uppers": {
            str(radius): str(value) for radius, value in lambda_uppers.items()
        },
        "three_capture_product_upper": str(product_upper),
        "bucket_probability_lower": str(bucket_probability_lower),
        "bucket_to_capture_quotient_lower": str(quotient),
        "bucket_to_capture_log2_lower": math.log2(float(quotient)),
        "RMC_8_0_threshold_m": next(
            size for size in range(3, m + 1) if quotient_lower_bound(size) > 8**6
        ),
        "illustrative_m_thresholds_for_C_8": polynomial_stress,
        "exhaustive_small_normalization_audit": brute,
        "claims": [
            "all coordinates are rational and the configuration is in general position",
            "both the six-point high cap and the m-point low cap are convex faces",
            "every endpoint-compatible trace contains at most two low-cap points",
            "each asymmetric rank-four compatible trace contains at most one earlier low-prefix point",
            "the same Boolean low-cap reservoir occurs in all three interval denominators",
            "the rank-four exact matrix audit violates RMC(8,0) at m=21",
            "the rank-four analytic bound violates RMC(8,0) at m=54",
            "asymptotic quotient is Omega((9/4)^m/m^6), defeating every fixed C and b",
            "the stronger rank-four quotient is Omega((3/2)^m/m^2)",
        ],
    }
    output = HERE / "rmc_nested_cap_counterexample_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    return certificate


def main() -> None:
    certificate = audit()
    print("RMC nested-cap counterexample audit: PASS")
    print(
        "n=", certificate["n"],
        "rank=", certificate["selected_face_rank"],
        "log2 quotient lower=",
        f'{certificate["rank_four_bucket_to_capture_log2_lower"]:.6f}',
    )
    print(
        "RMC(8,0) rank-four analytic threshold m=",
        certificate["rank_four_RMC_8_0_analytic_threshold_m"],
        "exact threshold at most m=21",
    )


if __name__ == "__main__":
    main()
