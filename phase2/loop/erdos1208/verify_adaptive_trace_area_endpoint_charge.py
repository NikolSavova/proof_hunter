#!/usr/bin/env python3
"""Checks for ADAPTIVE_TRACE_AREA_ENDPOINT_CHARGE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from random import Random

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_gaussian_edge_vector_charge import oriented_edge_vectors
from verify_metric_scalar_adversarial_stress import transform_champion
from verify_metric_scalar_fourier_endpoint_no_go import two_arm_instance
from verify_metric_scalar_large_area_gaussian_residual_audit import (
    add,
    subtract,
    sums_of_two_squares,
)
from verify_metric_trace_area_hybrid_audit import determinant, norm2
from verify_radial_orthogonal_product_barrier import canonical_transversal
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Profile = tuple[int, ...]


def adaptive_profile(first: list[Point], second: list[Point]) -> Profile:
    trace_loads: Counter[int] = Counter()
    area_loads: Counter[int] = Counter()
    joint_loads: Counter[tuple[int, int]] = Counter()

    first_data = [(vector, norm2(vector)) for vector in first]
    second_data = [(vector, norm2(vector)) for vector in second]
    for left, left_norm in first_data:
        for right, right_norm in second_data:
            trace = left_norm + 18 * right_norm
            area = determinant(left, right)
            trace_loads[trace] += 1
            area_loads[area] += 1
            joint_loads[(trace, area)] += 1

    selected: Counter[tuple[int, int]] = Counter()
    envelope = 0
    for left, left_norm in first_data:
        for right, right_norm in second_data:
            trace = left_norm + 18 * right_norm
            area = determinant(left, right)
            trace_load = trace_loads[trace]
            area_load = area_loads[area]
            envelope += min(trace_load, area_load)
            if trace_load <= area_load:
                selected[(0, trace)] += 1
            else:
                selected[(1, area)] += 1

    selected_energy = sum(load * load for load in selected.values())
    assert selected_energy <= envelope

    trace_support_degree = Counter(trace for trace, area in joint_loads)
    area_support_degree = Counter(area for trace, area in joint_loads)
    support_weighted = sum(
        multiplicity
        * min(trace_support_degree[trace], area_support_degree[area])
        for (trace, area), multiplicity in joint_loads.items()
    )
    support_unweighted = sum(
        min(trace_support_degree[trace], area_support_degree[area])
        for trace, area in joint_loads
    )
    maximum_joint = max(joint_loads.values(), default=0)
    assert envelope <= maximum_joint * support_weighted
    assert support_weighted <= maximum_joint * support_unweighted

    records = len(first) * len(second)
    assert sum(trace_loads.values()) == records
    assert sum(area_loads.values()) == records
    assert sum(joint_loads.values()) == records
    maximum_support_minimum = max(
        (
            min(trace_support_degree[trace], area_support_degree[area])
            for trace, area in joint_loads
        ),
        default=0,
    )
    return (
        len(first),
        len(second),
        records,
        sum(load * load for load in trace_loads.values()),
        sum(load * load for load in area_loads.values()),
        sum(load * load for load in joint_loads.values()),
        envelope,
        selected_energy,
        maximum_joint,
        len(joint_loads),
        support_weighted,
        support_unweighted,
        maximum_support_minimum,
    )


def endpoint_profile(points: list[Point]) -> Profile:
    vectors = oriented_edge_vectors(points)
    fibres = clean_start_fibres(points)
    q_value = max(fibres, key=lambda value: len(fibres[value]))
    return adaptive_profile(
        [vectors[start] for start in fibres[q_value]],
        list(vectors.values()),
    )


def support_four_cycle_profile(points: list[Point]) -> tuple[int, int, int]:
    vectors = oriented_edge_vectors(points)
    fibres = clean_start_fibres(points)
    q_value = max(fibres, key=lambda value: len(fibres[value]))

    endpoints = {
        (points[first][0] + points[second][0],
         points[first][1] + points[second][1]): frozenset((first, second))
        for first, second in combinations(range(len(points)), 2)
    }
    records: dict[tuple[int, int], list[tuple[Point, Point]]] = defaultdict(list)
    neighbors: dict[int, set[int]] = defaultdict(set)
    for start in fibres[q_value]:
        for target in vectors:
            key = (
                norm2(vectors[start]) + 18 * norm2(vectors[target]),
                determinant(vectors[start], vectors[target]),
            )
            records[key].append((start, target))
            neighbors[key[0]].add(key[1])

    trace_pairs: dict[tuple[int, int], list[int]] = defaultdict(list)
    for trace, areas in neighbors.items():
        for area_pair in combinations(sorted(areas), 2):
            trace_pairs[area_pair].append(trace)

    cycles = eight_edges = fourteen_endpoints = 0
    for area_pair, traces in trace_pairs.items():
        for first_trace, second_trace in combinations(traces, 2):
            cycles += 1
            chosen_records = [
                records[key][0]
                for key in (
                    (first_trace, area_pair[0]),
                    (first_trace, area_pair[1]),
                    (second_trace, area_pair[0]),
                    (second_trace, area_pair[1]),
                )
            ]
            edge_labels = [edge for record in chosen_records for edge in record]
            distinct_edges = set(edge_labels)
            if len(distinct_edges) == 8:
                eight_edges += 1
                point_labels = set().union(*(endpoints[edge] for edge in distinct_edges))
                if len(point_labels) == 14:
                    fourteen_endpoints += 1
    return cycles, eight_edges, fourteen_endpoints


def planted_points() -> tuple[list[Point], Point]:
    abstract_labels, representing_vectors = sums_of_two_squares(50)
    assert len(abstract_labels) == 24
    scale = len(abstract_labels)
    random = Random(1208)
    anchor_a = (0, 0)
    anchor_b = (2, 0)
    q_value = subtract(anchor_a, anchor_b)
    half_q = q_value[0] // 2, q_value[1] // 2
    points = [anchor_a, anchor_b]

    for vector in representing_vectors:
        center = (
            random.randrange(10_000_000, 2_000_000_000),
            random.randrange(10_000_000, 2_000_000_000),
        )
        source_half = scale * vector[0], scale * vector[1]
        partner_half = (
            random.randrange(1_000_000, 100_000_000),
            random.randrange(1_000_000, 100_000_000),
        )
        source_left = add(center, source_half)
        source_right = subtract(center, source_half)
        translated_center = add(center, half_q)
        target_left = add(translated_center, partner_half)
        target_right = subtract(translated_center, partner_half)
        points.extend((source_left, source_right, target_left, target_right))
    return points, q_value


def planted_profile() -> Profile:
    points, q_value = planted_points()
    vectors = oriented_edge_vectors(points)
    fibres = clean_start_fibres(points)
    assert len(fibres[q_value]) == 24
    return adaptive_profile(
        [vectors[start] for start in fibres[q_value]],
        list(vectors.values()),
    )


def main() -> None:
    genuine: list[tuple[str, Profile]] = [
        (
            "closure-30",
            endpoint_profile(POINTS[:30]),
        ),
        (
            "closure-120",
            endpoint_profile(POINTS[:120]),
        ),
        (
            "Costas-22",
            endpoint_profile(transformed_costas(23)),
        ),
        (
            "parabola-image-43",
            endpoint_profile(transformed_parabola_43()),
        ),
        (
            "parabola-champion-43",
            endpoint_profile(transform_champion(transformed_parabola_43())),
        ),
    ]
    expected = {
        "closure-30": (14, 435, 6_090, 6_342, 14_406, 6_090, 6_243,
                       6_182, 1, 6_090, 6_243, 6_243, 2),
        "closure-120": (127, 7_140, 906_780, 1_023_788, 3_986_674,
                        906_782, 1_004_179, 988_136, 2, 906_779,
                        1_004_177, 1_004_176, 6),
        "Costas-22": (34, 231, 7_854, 8_382, 186_714, 7_856, 8_379,
                      8_376, 2, 7_853, 8_377, 8_376, 3),
        "parabola-image-43": (171, 903, 154_413, 157_133, 17_585_719,
                              154_469, 157_132, 157_131, 2, 154_385,
                              157_076, 157_048, 3),
        "parabola-champion-43": (171, 903, 154_413, 158_371, 17_585_719,
                                 154_455, 158_369, 158_367, 2, 154_392,
                                 158_326, 158_304, 3),
    }
    for name, actual in genuine:
        assert actual == expected[name], (name, actual, expected[name])
        k_value = int((1 + (1 + 8 * actual[1]) ** 0.5) / 2)
        weak_budget = actual[1] * (actual[0] + k_value)
        print(name, actual, "envelope/weak", actual[6] / weak_budget)

    four_cycles = support_four_cycle_profile(transformed_parabola_43())
    assert four_cycles == (8, 4, 2)
    print("parabola-support-four-cycles", four_cycles)

    points, starts, edges = two_arm_instance(50)
    two_arm = adaptive_profile(
        [edges[start] for start in starts],
        list(edges.values()),
    )
    expected_two_arm = (
        114, 4_950, 564_300, 565_444, 19_511_800_228, 564_626,
        564_793, 564_698, 2, 564_137, 564_467, 564_304, 2,
    )
    assert two_arm == expected_two_arm
    print(
        "two-arm-50",
        two_arm,
        "envelope/weak",
        two_arm[6] / (two_arm[1] * (two_arm[0] + len(points))),
    )

    planted = planted_profile()
    expected_planted = (
        24, 4_753, 114_072, 114_232, 148_812, 114_076, 114_231,
        114_230, 2, 114_070, 114_227, 114_225, 2,
    )
    assert planted == expected_planted
    print(
        "sums-of-two-squares-98",
        planted,
        "envelope/weak",
        planted[6] / (planted[1] * (planted[0] + 98)),
    )

    radial_vectors = canonical_transversal(40)[::2]
    radial = adaptive_profile(radial_vectors, radial_vectors)
    expected_radial = (
        686, 686, 470_596, 6_833_852, 269_680_866, 487_266,
        6_821_254, 6_783_870, 5, 462_633, 6_681_159, 6_559_917, 33,
    )
    assert radial == expected_radial
    print("radial-transversal-40", radial, "envelope/records", radial[6] / radial[2])
    print("adaptive trace-area endpoint charge: PASS")


if __name__ == "__main__":
    main()
