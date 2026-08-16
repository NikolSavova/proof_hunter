#!/usr/bin/env python3
"""Exact audit for KL radial-bucket reduction and scalable barrier."""

from __future__ import annotations

import importlib.util
import json
import math
import random
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "agent_unit_matrix_asymptotic" / "verify_endpoint_span_localization.py"
SPEC = importlib.util.spec_from_file_location("endpoint_audit", SOURCE)
assert SPEC is not None and SPEC.loader is not None
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


def enumerate_faces(n: int, roots: tuple[tuple[int, int], ...]) -> list[tuple[int, ...]]:
    forward = V.temporal_paths(n, roots)
    backward = V.temporal_paths(n, tuple(reversed(roots)))
    faces: list[tuple[int, ...]] = [(), *((i,) for i in range(n))]
    for i, j in combinations(range(n), 2):
        seen: set[tuple[int, ...]] = set()
        for upper in forward[i, j]:
            for lower in backward[i, j]:
                face = tuple(sorted(set(upper + lower)))
                assert face not in seen
                seen.add(face)
                faces.append(face)
    assert len(faces) == len(set(faces))
    return faces


def capture_table(
    n: int, roots: tuple[tuple[int, int], ...]
) -> tuple[dict[tuple[int, int], Q], Q]:
    scale, forward = V.product_half_scaled(n, roots)
    _, backward = V.product_half_scaled(n, tuple(reversed(roots)))
    _, total = V.endpoint_masses(n, roots, Q(1, 2))
    capture: dict[tuple[int, int], Q] = {}
    for i, j in combinations(range(n), 2):
        cell = Q(forward[j][i] * backward[j][i], scale * scale)
        interior = V.interval_face_totals(roots, i, j)[0]
        capture[i, j] = 4 * cell / interior
        assert 0 < capture[i, j] <= 1
    return capture, total


def bucket_key(face: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    rank = len(face)
    radius = rank // 2
    return rank, face[radius : rank - radius]


def audit_instance(
    name: str,
    n: int,
    roots: tuple[tuple[int, int], ...],
    check_radial_all_depths: bool = False,
) -> dict[str, float | int | str]:
    faces = enumerate_faces(n, roots)
    capture, total = capture_table(n, roots)
    assert total == sum((Q(1, 1 << len(face)) for face in faces), Q())

    buckets = Counter(bucket_key(face) for face in faces)
    products: dict[tuple[int, ...], Q] = {}
    worst_ratio = Q()
    worst_face: tuple[int, ...] = ()
    entropy_bucket = 0.0
    entropy_face = 0.0
    mean_rank = 0.0
    expected_kl = 0.0
    distortion = 0.0

    bucket_probabilities: dict[tuple[int, tuple[int, ...]], Q] = {}
    for key, degree in buckets.items():
        rank = key[0]
        probability = Q(degree, 1 << rank) / total
        bucket_probabilities[key] = probability
        entropy_bucket -= float(probability) * math.log2(float(probability))

    expected_log_degree = 0.0
    for face in faces:
        rank = len(face)
        probability = Q(1, 1 << rank) / total
        product = Q(1)
        for depth in range(rank // 2):
            product *= capture[face[depth], face[-1 - depth]]
        products[face] = product
        key = bucket_key(face)
        bucket_probability = bucket_probabilities[key]
        degree = buckets[key]

        # Exact bucket factorization and the audited constant-distortion gate.
        assert bucket_probability == degree * probability
        assert bucket_probability <= (8**rank) * product

        ratio = bucket_probability / product
        if ratio > worst_ratio:
            worst_ratio = ratio
            worst_face = face

        p = float(probability)
        entropy_face -= p * math.log2(p)
        mean_rank += p * rank
        expected_log_degree += p * math.log2(degree)
        expected_kl -= p * math.log2(float(product))
        distortion += p * math.log2(float(ratio))

    assert abs(entropy_face - entropy_bucket - expected_log_degree) < 2e-10
    assert abs(expected_kl - entropy_bucket - distortion) < 2e-10

    # Exact d_j identities and the core-tilt/second-moment tail currency.
    max_depth = max(map(len, faces)) // 2
    depths = range(max_depth + 1) if check_radial_all_depths else range(min(3, max_depth) + 1)
    degree_tables: list[Counter[tuple[int, ...]]] = []
    for depth in depths:
        degrees: Counter[tuple[int, ...]] = Counter()
        tail = Q()
        for face in faces:
            if len(face) < 2 * depth:
                continue
            core = face[depth : len(face) - depth]
            degrees[core] += 1
            tail += Q(1, 1 << len(face)) / total
        degree_tables.append(degrees)
        first = sum(
            (Q(degree, 1 << len(core)) / total for core, degree in degrees.items()),
            Q(),
        )
        assert first == (4**depth) * tail

        if first:
            # rho(core)=pi(core)d_j(core)/E_pi d_j is a probability law.
            rho_total = sum(
                (Q(degree, 1 << len(core)) / total / first for core, degree in degrees.items()),
                Q(),
            )
            assert rho_total == 1
            kl_rho = 0.0
            mean_log_degree = 0.0
            for core, degree in degrees.items():
                pi_core = Q(1, 1 << len(core)) / total
                rho_core = pi_core * degree / first
                kl_rho += float(rho_core) * math.log2(float(rho_core / pi_core))
                mean_log_degree += float(rho_core) * math.log2(degree)
            assert abs(
                kl_rho
                - (mean_log_degree - 2 * depth - math.log2(float(tail)))
            ) < 2e-10
            second = sum(
                (Q(degree * degree, 1 << len(core)) / total for core, degree in degrees.items()),
                Q(),
            )
            for threshold in (1, 2, 8, 32):
                tail_rho = sum(
                    (
                        Q(degree, 1 << len(core)) / total / first
                        for core, degree in degrees.items()
                        if degree >= threshold
                    ),
                    Q(),
                )
                assert tail_rho <= second / (threshold * first)

    # d_(j+1)(S) is the sum of the d_j(T) over all immediate radial
    # parents T of S.  This is the exact weighted cross-child recurrence.
    for depth in range(len(degree_tables) - 1):
        current = degree_tables[depth]
        following = degree_tables[depth + 1]
        parent_sums: defaultdict[tuple[int, ...], int] = defaultdict(int)
        for parent, parent_degree in current.items():
            if len(parent) >= 2:
                parent_sums[parent[1:-1]] += parent_degree
        for core, degree in following.items():
            assert parent_sums[core] == degree

    radial_kl_expansion = 0.0
    maximum_parent_conditional_cost = 0.0
    if check_radial_all_depths:
        for depth in range(len(degree_tables) - 1):
            current = degree_tables[depth]
            following = degree_tables[depth + 1]
            weighted_costs: defaultdict[tuple[int, ...], float] = defaultdict(float)
            for parent, parent_degree in current.items():
                if len(parent) < 2:
                    continue
                core = parent[1:-1]
                cost = -math.log2(float(capture[parent[0], parent[-1]]))
                weighted_costs[core] += parent_degree * cost
                radial_kl_expansion += (
                    float(Q(1, 1 << len(core)) / total / (4 ** (depth + 1)))
                    * parent_degree
                    * cost
                )
            for core, weighted_cost in weighted_costs.items():
                # This is exactly E[-log lambda_T | S_(j+1)=core]
                # under parent probability d_j(T)/d_(j+1)(core).
                conditional_cost = weighted_cost / following[core]
                maximum_parent_conditional_cost = max(
                    maximum_parent_conditional_cost, conditional_cost
                )
        assert abs(radial_kl_expansion - expected_kl) < 2e-10

    # When RMC(C,0) fails, the first normalized radial-bucket crossing has
    # exactly the degree jump in (18).  C=2 exposes this in the saved hard
    # instances, while C=8 was checked above.
    first_crossing_checked = False
    any_constant_two_failure = False
    if check_radial_all_depths:
        constant = 2
        for face in faces:
            rank = len(face)
            radius = rank // 2
            if radius == 0:
                continue
            if bucket_probabilities[bucket_key(face)] <= constant**rank * products[face]:
                continue
            any_constant_two_failure = True
            prefix_capture = Q(1)
            previous_x = Q(1, 1 << rank) / total
            assert previous_x < 1
            for depth in range(radius):
                edge = face[depth], face[-1 - depth]
                prefix_capture *= capture[edge]
                core = face[depth + 1 : rank - depth - 1]
                next_x = (
                    Q(1, 1 << rank)
                    / total
                    * degree_tables[depth + 1][core]
                    / (constant ** (2 * (depth + 1)) * prefix_capture)
                )
                if previous_x <= 1 < next_x:
                    parent = face[depth : rank - depth]
                    assert (
                        degree_tables[depth + 1][core]
                        > constant**2
                        * capture[edge]
                        * degree_tables[depth][parent]
                    )
                    first_crossing_checked = True
                    break
                previous_x = next_x
            if first_crossing_checked:
                break
        assert first_crossing_checked == any_constant_two_failure

    return {
        "name": name,
        "n": n,
        "faces": len(faces),
        "mean_rank": mean_rank,
        "kl": expected_kl,
        "bucket_entropy": entropy_bucket,
        "radial_distortion": distortion,
        "worst_face": str(worst_face),
        "worst_log2_bucket_over_capture": math.log2(float(worst_ratio)),
        "worst_per_vertex_constant": float(worst_ratio) ** (1 / max(1, len(worst_face))),
        "maximum_parent_conditional_cost": maximum_parent_conditional_cost,
    }


def small_and_random_search() -> tuple[float, float]:
    worst_small = 0.0
    for n in range(3, 7):
        representatives = V.reflection_class_representatives(n)
        assert len(representatives) == {3: 2, 4: 8, 5: 62, 6: 908}[n]
        for roots in representatives.values():
            row = audit_instance("small", n, roots)
            worst_small = max(worst_small, float(row["worst_per_vertex_constant"]))

    generator = random.Random(20260814)
    worst_random = 0.0
    for _ in range(100):
        n = 14
        heights = generator.sample(range(-10**9, 10**9), n)
        points = [(Q(i), Q(height)) for i, height in enumerate(heights)]
        row = audit_instance("random", n, V.slope_roots(points))
        worst_random = max(worst_random, float(row["worst_per_vertex_constant"]))
    return worst_small, worst_random


def poly_add(left: list[int], right: list[int]) -> list[int]:
    result = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return result


def alternating_profile(n: int) -> list[int]:
    # R_d(t)=t+t^2 sum_s (1+t)^floor((s-1)/2), and
    # F_n(t)=1+nt+sum_d (n-d)tR_d(t).
    profile = [1, n]
    for distance in range(1, n):
        rich = [0, 1]
        for step in range(1, distance):
            exponent = (step - 1) // 2
            term = [0, 0] + [math.comb(exponent, rank) for rank in range(exponent + 1)]
            rich = poly_add(rich, term)
        cell = [0] + rich
        if len(profile) < len(cell):
            profile += [0] * (len(cell) - len(profile))
        for rank, value in enumerate(cell):
            profile[rank] += (n - distance) * value
    return profile


def value_and_mean(profile: list[int]) -> tuple[Q, Q]:
    value = sum((Q(count, 1 << rank) for rank, count in enumerate(profile)), Q())
    moment = sum((Q(rank * count, 1 << rank) for rank, count in enumerate(profile)), Q())
    return value, moment / value


def alternating_closed_form_audit() -> list[tuple[int, float, float]]:
    q = Q(3, 2)

    def rich(distance: int) -> Q:
        return Q(1, 2) + Q(1, 4) * sum(
            (q ** ((step - 1) // 2) for step in range(1, distance)), Q()
        )

    def partition(size: int) -> Q:
        return Q(1) + Q(size, 2) + sum(
            (Q(size - distance, 2) * rich(distance) for distance in range(1, size)),
            Q(),
        )

    for k in range(1, 60):
        assert rich(2 * k) == Q(5, 4) * q ** (k - 1) - Q(1, 2)
        assert rich(2 * k + 1) == q**k - Q(1, 2)
        assert partition(2 * k) == (
            10 * q**k - Q(k * k, 2) - Q(13 * k, 4) - 9
        )
        assert partition(2 * k + 1) == (
            Q(49, 4) * q**k - Q(k * k, 2) - Q(15 * k, 4) - Q(43, 4)
        )

    for distance in range(3, 120):
        capture = 2 * rich(distance) / partition(distance - 1)
        assert Q(1, 5) <= capture <= Q(8, 9)

    rows = []
    for n in (20, 40, 80, 160, 320):
        profile = alternating_profile(n)
        value, mean = value_and_mean(profile)
        assert value == partition(n)
        # The exact formula has mean n/6+O(1); this finite replay checks
        # convergence without using floating partition evaluations.
        assert abs(float(mean) / n - 1 / 6) < 0.08
        lower_kl_per_n = math.log2(9 / 8) * max(0.0, float(mean) / 2 - 1.5) / n
        rows.append((n, float(mean) / n, lower_kl_per_n))
    assert abs(rows[-1][1] - 1 / 6) < 0.01
    return rows


def outer_triangle_rare_tail_audit() -> tuple[float, Q, float]:
    """Replay the exact rare, high-cost tangent parent in the n=63 barrier."""
    source = HERE.parent / "agent_planar_tutte" / "verify_outer_triangle_barrier.py"
    spec = importlib.util.spec_from_file_location("outer_triangle", source)
    assert spec is not None and spec.loader is not None
    outer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(outer)
    hull, inner = outer.configuration()
    points = sorted(hull + inner)
    roots = V.slope_roots(points)
    capture, _ = capture_table(len(points), roots)
    left = points.index(hull[0])
    right = points.index(hull[1])
    left, right = sorted((left, right))
    cost = -math.log2(float(capture[left, right]))
    empty_core_parent_probability = Q(1, math.comb(len(points), 2))
    contribution = float(empty_core_parent_probability) * cost
    assert cost > 23
    assert contribution < Q(1, 50)
    return cost, empty_core_parent_probability, contribution


def main() -> None:
    saved = json.loads(V.N58_CERTIFICATE.read_text())["finite_braid_record"]
    n58 = audit_instance(
        "n58",
        saved["n"],
        V.root_sequence(saved["n"], tuple(saved["word_zero_based"])),
        check_radial_all_depths=True,
    )
    pascal = audit_instance(
        "Pascal36", 36, V.slope_roots(V.pascal_composition()), check_radial_all_depths=True
    )
    alternating = audit_instance(
        "alternating30", 30, V.slope_roots(V.alternating_points(30)), check_radial_all_depths=True
    )
    worst_small, worst_random = small_and_random_search()
    asymptotic_rows = alternating_closed_form_audit()
    outer_cost, outer_probability, outer_contribution = outer_triangle_rare_tail_audit()

    # The whole-radial-multiplicity C=1 strengthening really fails.
    assert float(n58["worst_log2_bucket_over_capture"]) > 14
    assert float(pascal["worst_log2_bucket_over_capture"]) > 10
    assert float(alternating["worst_log2_bucket_over_capture"]) > 4

    print("KL radial-bucket audit: PASS")
    for row in (n58, pascal, alternating):
        print(
            row["name"],
            "faces=", row["faces"],
            "mu=", f"{row['mean_rank']:.6f}",
            "D=", f"{row['kl']:.6f}",
            "H(B)=", f"{row['bucket_entropy']:.6f}",
            "J=", f"{row['radial_distortion']:.6f}",
            "max conditional parent cost=",
            f"{row['maximum_parent_conditional_cost']:.6f}",
            "worst log2 bucket/capture=",
            f"{row['worst_log2_bucket_over_capture']:.6f}",
            "worst face=", row["worst_face"],
        )
    print(
        "RMC(8,0) exhaustive/sample maxima per-vertex C:",
        f"small={worst_small:.6f}",
        f"random14={worst_random:.6f}",
        "PASS",
    )
    n, mean_ratio, kl_lower_ratio = asymptotic_rows[-1]
    print(
        "alternating scalable canonical-KL barrier:",
        f"n={n}",
        f"mu/n={mean_ratio:.6f}",
        f"certified D/n lower={kl_lower_ratio:.6f}",
        "PASS",
    )
    print(
        "outer-triangle rare tangent tail:",
        f"cost={outer_cost:.6f}",
        f"empty-core parent probability={outer_probability}",
        f"conditional contribution={outer_contribution:.6f}",
        "PASS",
    )


if __name__ == "__main__":
    main()
