#!/usr/bin/env python3
"""Exact audit for the two-reference Hall demand and planar transport kill."""

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


R = load_module("nested_cap_geometry_for_transport", HERE / "verify_rmc_nested_cap_counterexample.py")


POINTS: list[R.Point] = [
    (Q(152732), Q(588305)),
    (Q(198972), Q(629398)),
    (Q(253646), Q(338142)),
    (Q(271535), Q(312524)),
    (Q(627261), Q(872520)),
    (Q(773158), Q(636702)),
    (Q(848731), Q(579029)),
    (Q(886929), Q(449046)),
    (Q(913864), Q(133077)),
]


def safe_term(weight: Q, ratio: Q) -> float:
    if weight == 0:
        return 0.0
    assert ratio > 0
    return float(weight) * math.log2(float(ratio))


def enumerate_faces(points: list[R.Point]) -> list[tuple[int, ...]]:
    result = []
    for mask in range(1 << len(points)):
        face = tuple(i for i in range(len(points)) if mask >> i & 1)
        if R.is_convex_face([points[i] for i in face]):
            result.append(face)
    return result


def audit() -> dict[str, object]:
    n = len(POINTS)
    assert [point[0] for point in POINTS] == sorted(point[0] for point in POINTS)
    for i, j, k in combinations(range(n), 3):
        assert R.orient(POINTS[i], POINTS[j], POINTS[k]) != 0

    faces = enumerate_faces(POINTS)
    face_set = set(faces)
    total = sum((Q(1, 1 << len(face)) for face in faces), Q())
    assert len(faces) == 449
    assert total == Q(9509, 256)

    cells: defaultdict[tuple[int, int], Q] = defaultdict(Q)
    for face in faces:
        if len(face) >= 2:
            cells[face[0], face[-1]] += Q(1, 1 << len(face))

    interval_totals: dict[tuple[int, int], Q] = {}
    for edge in combinations(range(n), 2):
        i, j = edge
        interval_totals[edge] = sum(
            (
                Q(1, 1 << len(face))
                for face in faces
                if all(i < vertex < j for vertex in face)
            ),
            Q(),
        )

    p = {edge: mass / total for edge, mass in cells.items()}
    probability_two = sum(p.values(), Q())
    carleson_mass = sum(interval_totals.values(), Q()) / (4 * total)
    assert carleson_mass == Q(8335, 9509)
    reservoir_normalizer = sum(interval_totals.values(), Q())
    reservoir = {
        edge: interval_totals[edge] / reservoir_normalizer for edge in interval_totals
    }
    capture = {
        edge: 4 * cells[edge] / interval_totals[edge] for edge in interval_totals
    }

    # Joint lift: the parent Gibbs law is the container-incidence law
    # conditioned on compatibility, with constant density A/P2.
    container_total = Q()
    compatible_container_total = Q()
    joint_density_checks = 0
    for edge in combinations(range(n), 2):
        i, j = edge
        for core in faces:
            if not all(i < vertex < j for vertex in core):
                continue
            container_probability = Q(1, 1 << len(core)) / (4 * total * carleson_mass)
            container_total += container_probability
            parent = tuple((i, *core, j))
            if parent not in face_set:
                continue
            compatible_container_total += container_probability
            parent_probability = Q(1, 1 << (len(core) + 2)) / (total * probability_two)
            assert parent_probability / container_probability == carleson_mass / probability_two
            joint_density_checks += 1
    assert container_total == 1
    assert compatible_container_total == probability_two / carleson_mass

    max_radius = max(map(len, faces)) // 2
    depth_rows = []
    total_kl = 0.0
    mean_radius = Q()
    sum_demands = Q()
    for depth in range(max_radius):
        degrees: Counter[tuple[int, ...]] = Counter(
            face[depth : len(face) - depth]
            for face in faces
            if len(face) >= 2 * depth
        )
        q: defaultdict[tuple[int, int], Q] = defaultdict(Q)
        for face in faces:
            if len(face) >= 2 * depth + 2:
                q[face[depth], face[-1 - depth]] += Q(1, 1 << len(face)) / total
        tau = sum(q.values(), Q())
        if not tau:
            continue
        mean_radius += tau

        direct_cost = sum(
            safe_term(weight, 1 / capture[edge]) for edge, weight in q.items()
        )
        endpoint_divergence = sum(
            safe_term(weight / tau, (weight / tau) / (p[edge] / probability_two))
            for edge, weight in q.items()
        )
        reservoir_divergence = sum(
            safe_term(weight / tau, (weight / tau) / reservoir[edge])
            for edge, weight in q.items()
        )
        two_reference = float(tau) * (
            math.log2(float(carleson_mass / probability_two))
            + endpoint_divergence
            - reservoir_divergence
        )
        assert abs(direct_cost - two_reference) < 2e-12

        demand = sum((weight / capture[edge] for edge, weight in q.items()), Q())
        demand_cross = carleson_mass * sum(
            (reservoir[edge] * (weight / p[edge]) for edge, weight in q.items()),
            Q(),
        )
        assert demand == demand_cross

        # Degree-side expression in (10).
        degree_demand = Q()
        for edge in combinations(range(n), 2):
            weighted_degree = Q()
            for parent in faces:
                if len(parent) >= 2 and (parent[0], parent[-1]) == edge:
                    weighted_degree += degrees[parent] * Q(1, 1 << len(parent))
            mean_degree = weighted_degree / cells[edge]
            degree_demand += interval_totals[edge] * mean_degree
        degree_demand /= (4 ** (depth + 1)) * total
        assert demand == degree_demand

        jensen_bound = safe_term(tau, demand / tau)
        assert direct_cost <= jensen_bound + 2e-12
        total_kl += direct_cost
        sum_demands += demand
        depth_rows.append(
            {
                "depth": depth,
                "tail_probability": str(tau),
                "capture_cost_bits": direct_cost,
                "endpoint_divergence_bits": endpoint_divergence,
                "reservoir_divergence_bits": reservoir_divergence,
                "divergence_difference_bits": endpoint_divergence - reservoir_divergence,
                "inverse_capture_demand": str(demand),
                "conditional_inverse_capture_moment": str(demand / tau),
                "jensen_bound_bits": jensen_bound,
            }
        )

    global_jensen_bound = safe_term(mean_radius, sum_demands / mean_radius)
    assert total_kl <= global_jensen_bound + 2e-12
    assert sum_demands >= mean_radius * Q.from_float(2 ** (total_kl / float(mean_radius)))

    depth_one = depth_rows[1]
    assert Q(depth_one["conditional_inverse_capture_moment"]) > carleson_mass / probability_two
    assert depth_one["divergence_difference_bits"] > 0

    # The positive KL difference is certified without floating-point logs.
    # At depth one every normalized endpoint weight has denominator 3109, so
    # exponentiating 3109 times the divergence reduces its sign to one exact
    # integer product comparison.
    q_one: defaultdict[tuple[int, int], Q] = defaultdict(Q)
    for face in faces:
        if len(face) >= 4:
            q_one[face[1], face[-2]] += Q(1, 1 << len(face)) / total
    tau_one = sum(q_one.values(), Q())
    exponent_denominator = math.lcm(
        *((weight / tau_one).denominator for weight in q_one.values())
    )
    assert exponent_denominator == 3109
    product_numerator = 1
    product_denominator = 1
    for edge, weight in q_one.items():
        exponent = int((weight / tau_one) * exponent_denominator)
        ratio = reservoir[edge] / (p[edge] / probability_two)
        product_numerator *= ratio.numerator**exponent
        product_denominator *= ratio.denominator**exponent
    assert product_numerator > product_denominator

    certificate: dict[str, object] = {
        "description": "two-reference joint lift, Hall demand bridge, and planar monotonicity kill",
        "n": n,
        "points": [[int(x), int(y)] for x, y in POINTS],
        "faces": len(faces),
        "half_partition_function": str(total),
        "rank_at_least_two_probability": str(probability_two),
        "carleson_mass": str(carleson_mass),
        "baseline_inverse_capture_moment": str(carleson_mass / probability_two),
        "joint_density_checks": joint_density_checks,
        "mean_radial_depth": str(mean_radius),
        "sum_inverse_capture_demands": str(sum_demands),
        "total_canonical_KL_bits": total_kl,
        "global_jensen_bound_bits": global_jensen_bound,
        "depth_rows": depth_rows,
        "exact_depth_one_KL_sign_certificate": {
            "common_exponent_denominator": exponent_denominator,
            "product_numerator_bit_length": product_numerator.bit_length(),
            "product_denominator_bit_length": product_denominator.bit_length(),
            "numerator_exceeds_denominator": product_numerator > product_denominator,
        },
        "claims": [
            "parent Gibbs incidences are interval-container incidences conditioned on compatibility",
            "all three inverse-capture demand formulas agree exactly",
            "one-depth and global Jensen/log-sum bridges hold",
            "depth one strictly violates inverse-moment monotonicity",
            "depth one strictly violates exact two-reference KL domination",
        ],
    }
    output = HERE / "two_reference_hall_demand_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    return certificate


def main() -> None:
    certificate = audit()
    row = certificate["depth_rows"][1]
    print("two-reference Hall demand audit: PASS")
    print(
        "n=", certificate["n"],
        "faces=", certificate["faces"],
        "depth-one divergence difference=",
        f'{row["divergence_difference_bits"]:.12f}',
    )
    print(
        "inverse moments depth one/baseline=",
        row["conditional_inverse_capture_moment"],
        certificate["baseline_inverse_capture_moment"],
    )


if __name__ == "__main__":
    main()
