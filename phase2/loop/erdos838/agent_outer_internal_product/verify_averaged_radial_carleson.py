#!/usr/bin/env python3
"""Exact verifier for the averaged radial Carleson decomposition."""

from __future__ import annotations

import importlib.util
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


R = load_module("nested_cap_rmc", HERE / "verify_rmc_nested_cap_counterexample.py")
M = load_module(
    "endpoint_matrix_carleson",
    HERE.parent / "agent_unit_matrix_asymptotic" / "verify_endpoint_span_localization.py",
)


def all_faces(points: list[R.Point]) -> list[tuple[int, ...]]:
    faces = []
    n = len(points)
    for mask in range(1 << n):
        face = tuple(i for i in range(n) if mask >> i & 1)
        if R.is_convex_face([points[i] for i in face]):
            faces.append(face)
    return faces


def safe_term(weight: Q, ratio: Q) -> float:
    if weight == 0:
        return 0.0
    assert ratio > 0
    return float(weight) * math.log2(float(ratio))


def small_complete_audit(m: int = 8) -> dict[str, object]:
    points, _, _ = R.construction(m)
    n = len(points)
    faces = all_faces(points)
    total = sum((Q(1, 1 << len(face)) for face in faces), Q())

    cells: defaultdict[tuple[int, int], Q] = defaultdict(Q)
    for face in faces:
        if len(face) >= 2:
            cells[face[0], face[-1]] += Q(1, 1 << len(face))

    interval_totals: dict[tuple[int, int], Q] = {}
    captures: dict[tuple[int, int], Q] = {}
    for i, j in combinations(range(n), 2):
        interval_total = sum(
            (
                Q(1, 1 << len(face))
                for face in faces
                if all(i < vertex < j for vertex in face)
            ),
            Q(),
        )
        interval_totals[i, j] = interval_total
        captures[i, j] = 4 * cells[i, j] / interval_total
        assert 0 < captures[i, j] <= 1

    face_set = set(faces)
    # Every actual parent supplies a Boolean core and disjoint one-label
    # compatible cubes, as in (7a).
    boolean_core_checks = 0
    for parent in faces:
        if len(parent) < 2:
            continue
        edge = parent[0], parent[-1]
        core = parent[1:-1]
        addable = sum(
            tuple(sorted((*parent, z))) in face_set
            for z in range(edge[0] + 1, edge[1])
            if z not in parent
        )
        compatible_trace_weight = 4 * cells[edge]
        lower = Q(3, 2) ** len(core) * (1 + Q(addable, 2))
        assert compatible_trace_weight >= lower
        boolean_core_checks += 1

    p = {edge: mass / total for edge, mass in cells.items()}
    probability_rank_two = sum(p.values(), Q())
    carleson_mass = sum(interval_totals.values(), Q()) / (4 * total)

    # Exact interval-container incidence identity.
    incidence_expectation = Q()
    for face in faces:
        if not face:
            containers = math.comb(n, 2)
        else:
            containers = face[0] * (n - 1 - face[-1])
        incidence_expectation += Q(1, 1 << len(face)) * containers / total
    assert incidence_expectation == 4 * carleson_mass
    assert carleson_mass <= Q(math.comb(n, 2), 4)

    max_radius = max(map(len, faces)) // 2
    depth_rows = []
    tail_sum = Q()
    total_kl = 0.0
    crowding_sum = 0.0
    omitted_depth_expectation = 0.0
    for depth in range(max_radius):
        degrees: Counter[tuple[int, ...]] = Counter(
            face[depth : len(face) - depth]
            for face in faces
            if len(face) >= 2 * depth
        )
        q: defaultdict[tuple[int, int], Q] = defaultdict(Q)
        crowding = 0.0
        for face in faces:
            if len(face) < 2 * depth + 2:
                continue
            probability = Q(1, 1 << len(face)) / total
            parent = face[depth : len(face) - depth]
            edge = parent[0], parent[-1]
            q[edge] += probability
            crowding += safe_term(probability, Q(degrees[parent], 4**depth))

        tau = sum(q.values(), Q())
        if not tau:
            continue
        tail_sum += tau
        direct = sum(
            safe_term(weight, 1 / captures[edge]) for edge, weight in q.items()
        )
        tilt = sum(safe_term(weight, weight / p[edge]) for edge, weight in q.items())
        first_exact = sum(
            safe_term(weight, interval_totals[edge] / (4 * total * weight))
            for edge, weight in q.items()
        )
        assert abs(direct - first_exact - tilt) < 2e-10
        carleson_bound = safe_term(tau, carleson_mass / tau)
        assert first_exact <= carleson_bound + 2e-10

        endpoint_divergence = sum(
            safe_term(weight / tau, (weight / tau) / (p[edge] / probability_rank_two))
            for edge, weight in q.items()
        )
        tilt_identity = float(tau) * (
            endpoint_divergence + math.log2(float(tau / probability_rank_two))
        )
        assert abs(tilt - tilt_identity) < 2e-10
        reservoir_law = {
            edge: interval_totals[edge] / (4 * total * carleson_mass)
            for edge in interval_totals
        }
        reservoir_divergence = sum(
            safe_term(weight / tau, (weight / tau) / reservoir_law[edge])
            for edge, weight in q.items()
        )
        two_reference = float(tau) * (
            math.log2(float(carleson_mass / probability_rank_two))
            + endpoint_divergence
            - reservoir_divergence
        )
        assert abs(direct - two_reference) < 2e-10
        assert tilt <= crowding + 2e-10
        assert direct <= carleson_bound + crowding + 2e-10
        total_kl += direct
        crowding_sum += crowding
        depth_rows.append(
            {
                "depth": depth,
                "tail_probability": str(tau),
                "capture_cost_bits": direct,
                "carleson_bound_bits": carleson_bound,
                "endpoint_tilt_bits": tilt,
                "endpoint_divergence_bits": endpoint_divergence,
                "reservoir_divergence_bits": reservoir_divergence,
                "radial_crowding_bits": crowding,
            }
        )

    # Pointwise omitted-depth capture bound (7c).
    for face in faces:
        probability = Q(1, 1 << len(face)) / total
        gap_area = 0
        product_cost = 0.0
        for depth in range(len(face) // 2):
            left, right = face[depth], face[-1 - depth]
            core_size = len(face) - 2 * depth - 2
            gap_area += right - left - 1 - core_size
            product_cost += math.log2(1 / float(captures[left, right]))
        assert product_cost <= math.log2(1.5) * gap_area + 2e-10
        omitted_depth_expectation += float(probability) * gap_area

    # Exact addable-depth second-moment identity (7e).
    addable_depth = 0.0
    addable_count = 0.0
    rank_second_moment = 0.0
    mean_rank = 0.0
    for face in faces:
        probability = Q(1, 1 << len(face)) / total
        selected = set(face)
        for z in range(n):
            if z in selected or tuple(sorted((*face, z))) not in face_set:
                continue
            left = sum(vertex < z for vertex in face)
            right = len(face) - left
            addable_count += float(probability)
            addable_depth += float(probability) * min(left, right)
        rank_second_moment += float(probability) * 2 * ((len(face) - 1) ** 2 // 4)
        mean_rank += float(probability) * len(face)
    assert abs(addable_depth - rank_second_moment) < 2e-10
    assert abs(addable_count - 2 * mean_rank) < 2e-10

    # Concavity bound (20), applied to all live depths.
    summed_carleson = sum(row["carleson_bound_bits"] for row in depth_rows)
    global_carleson_bound = float(tail_sum) * math.log2(
        float(carleson_mass * len(depth_rows) / tail_sum)
    )
    assert summed_carleson <= global_carleson_bound + 2e-10

    return {
        "m": m,
        "n": n,
        "faces": len(faces),
        "half_partition_function": str(total),
        "rank_at_least_two_probability": str(probability_rank_two),
        "carleson_mass": str(carleson_mass),
        "interval_container_expectation": str(incidence_expectation),
        "mean_radial_depth": str(tail_sum),
        "depth_rows": depth_rows,
        "total_canonical_KL_bits": total_kl,
        "aggregate_radial_crowding_bits": crowding_sum,
        "boolean_core_parent_checks": boolean_core_checks,
        "expected_omitted_label_depth": omitted_depth_expectation,
        "expected_addable_label_depth": addable_depth,
        "expected_addable_label_count": addable_count,
        "twice_mean_rank": 2 * mean_rank,
        "twice_rank_radial_second_moment": rank_second_moment,
        "summed_carleson_bound_bits": summed_carleson,
        "global_tail_carleson_bound_bits": global_carleson_bound,
    }


def nested_cap_activity_audit(m: int = 21) -> dict[str, object]:
    points, high, low = R.construction(m)
    n = len(points)
    roots = M.slope_roots(points)
    scale, forward = M.product_half_scaled(n, roots)
    _, backward = M.product_half_scaled(n, tuple(reversed(roots)))
    _, total = M.endpoint_masses(n, roots, Q(1, 2))

    point_index = {point: i for i, point in enumerate(points)}
    high_by_x = {int(point[0]): point for point in high}
    outer_face = tuple(
        sorted(
            (
                point_index[high_by_x[-4]],
                point_index[high_by_x[-2]],
                point_index[low[-2]],
                point_index[low[-1]],
            )
        )
    )
    inner_parent = outer_face[1:3]
    assert R.is_convex_face([points[i] for i in outer_face])

    left_choices = range(inner_parent[0])
    right_choices = range(inner_parent[-1] + 1, n)
    histories = [
        (left, right)
        for left in left_choices
        for right in right_choices
        if R.is_convex_face(
            [points[left], points[inner_parent[0]], points[inner_parent[1]], points[right]]
        )
    ]
    assert len(histories) == 8

    rows = []
    costs = []
    for edge in ((outer_face[0], outer_face[3]), tuple(inner_parent)):
        cell = Q(forward[edge[1]][edge[0]] * backward[edge[1]][edge[0]], scale * scale)
        interval = M.interval_face_totals(roots, *edge)[0]
        capture = 4 * cell / interval
        costs.append(math.log2(1 / float(capture)))
        rows.append(
            {
                "edge": list(edge),
                "interval_halfweight": str(interval),
                "capture": str(capture),
                "capture_cost_bits": costs[-1],
            }
        )

    exact_contribution = (costs[0] + 8 * costs[1]) / (16 * float(total))
    alpha = math.log2(1.5)
    cage_bound = 9 * alpha * (m - 2) / (16 * float(total))
    boolean_cage_bound = 9 * alpha * (m - 2) / (16 * (1.5**m))
    assert costs[0] <= (m - 2) * alpha + 2e-10
    assert costs[1] <= (m - 2) * alpha + 2e-10
    assert exact_contribution <= cage_bound + 2e-10
    assert cage_bound <= boolean_cage_bound + 2e-10

    return {
        "m": m,
        "n": n,
        "outer_parent_degree": 1,
        "inner_parent_degree": len(histories),
        "outer_parent_activity": str(Q(1, 16) / total),
        "inner_parent_activity": str(Q(8, 16) / total),
        "rows": rows,
        "exact_two_depth_contribution_bits": exact_contribution,
        "ambient_partition_cage_bound_bits": cage_bound,
        "boolean_cage_only_bound_bits": boolean_cage_bound,
    }


def main() -> None:
    complete = small_complete_audit()
    nested = nested_cap_activity_audit()
    certificate = {
        "description": "averaged radial endpoint Carleson and common-cage activity audit",
        "complete_small_instance": complete,
        "nested_cap_activity": nested,
        "claims": [
            "one-depth capture cost is bounded by interval Carleson mass plus endpoint activity tilt",
            "one-depth capture cost exactly equals a difference of endpoint and reservoir KL divergences",
            "endpoint activity tilt is data-processed radial log-degree crowding",
            "interval Carleson mass equals one quarter of the expected open-container count",
            "the rank-four nested-cap parents have exact radial degrees 1 and 8",
            "their complete two-depth activity is exponentially discounted by the common Boolean cage",
        ],
    }
    output = HERE / "averaged_radial_carleson_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print("averaged radial Carleson audit: PASS")
    print(
        "small n=", complete["n"],
        "KL bits=", f'{complete["total_canonical_KL_bits"]:.6f}',
        "depths=", len(complete["depth_rows"]),
    )
    print(
        "nested m=", nested["m"],
        "degrees=", (nested["outer_parent_degree"], nested["inner_parent_degree"]),
        "activity bits=", f'{nested["exact_two_depth_contribution_bits"]:.9f}',
    )


if __name__ == "__main__":
    main()
