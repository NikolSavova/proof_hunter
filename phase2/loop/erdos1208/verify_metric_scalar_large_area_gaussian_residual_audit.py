#!/usr/bin/env python3
"""Checks for METRIC_SCALAR_LARGE_AREA_GAUSSIAN_RESIDUAL_AUDIT.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import comb, isqrt
from random import Random

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points
from verify_dilated_internal_pair_sum_charge import transformed_parabola_43
from verify_gaussian_edge_vector_two_arm_barrier import distance_sidon
from verify_metric_scalar_cross_edge_determinant_branch import (
    cross_factor_checks,
    endpoint_map,
    largest_fibre,
    resonant_two_arm_data,
)
from verify_metric_scalar_pair_sum_charge import pair_labels
from verify_transverse_closure_witness import POINTS
from verify_transverse_row_source_c4 import SOURCE_POINTS


Point = tuple[int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def squarefree_kernel(number: int) -> int:
    output = 1
    prime = 2
    while prime * prime <= number:
        parity = 0
        while number % prime == 0:
            number //= prime
            parity ^= 1
        if parity:
            output *= prime
        prime += 1
    return output * number


def residual_profile(
    points: list[Point],
    q_value: Point,
    starts: list[Point],
    targets: list[Point],
) -> tuple[int, ...]:
    labels = pair_labels(points)
    endpoints = endpoint_map(points)
    records: dict[int, list[tuple[Point, Point]]] = defaultdict(list)
    for start in starts:
        for target in targets:
            records[labels[start] + 18 * labels[target]].append((start, target))

    cutoff = len(targets) // len(starts)
    four = low_target = low_residual = union = 0
    fixed_projection_targets: dict[
        tuple[Point, Point, int],
        set[tuple[Point, Point]],
    ] = defaultdict(set)

    for bucket in records.values():
        for first_index, (start, target) in enumerate(bucket):
            for second_index, (other_start, other_target) in enumerate(bucket):
                if first_index == second_index:
                    continue
                if len({start, target, other_start, other_target}) < 4:
                    continue

                source_radius, source_area, _, _ = cross_factor_checks(
                    endpoints[start], endpoints[other_start]
                )
                target_radius, target_area, _, _ = cross_factor_checks(
                    endpoints[target], endpoints[other_target]
                )
                assert source_radius + 18 * target_radius == 0
                residual = source_area + 18 * target_area
                four += 1
                first_low = abs(target_area) <= cutoff
                second_low = abs(residual) <= cutoff
                low_target += first_low
                low_residual += second_low
                union += first_low or second_low

                # For a fixed source pair and projected-area value, the
                # target (radius,area) pair is fixed, as in Theorem 2.1.
                fixed_projection_targets[
                    (start, other_start, residual)
                ].add((target, other_target))

    # Finite fixed-invariant multiplicities on every current stress.
    maximum = max(map(len, fixed_projection_targets.values()), default=0)
    assert low_residual <= (2 * cutoff + 1) * len(starts) ** 2 * max(1, maximum)
    return (
        len(starts),
        len(targets),
        cutoff,
        four,
        low_target,
        low_residual,
        union,
        four - union,
        maximum,
    )


def sums_of_two_squares(limit: int) -> tuple[list[int], list[Point]]:
    labels: list[int] = []
    vectors: list[Point] = []
    for number in range(1, limit + 1):
        for x in range(isqrt(number) + 1):
            y = isqrt(number - x * x)
            if x * x + y * y == number:
                labels.append(number)
                vectors.append((x, y))
                break
    return labels, vectors


def dressed_certificate() -> tuple[int, ...]:
    abstract_labels, representing_vectors = sums_of_two_squares(50)
    h = len(abstract_labels)
    assert h == 24
    scale = h
    random = Random(1208)
    anchor_a = (0, 0)
    anchor_b = (2, 0)
    q_value = subtract(anchor_a, anchor_b)
    half_q = (q_value[0] // 2, q_value[1] // 2)
    points = [anchor_a, anchor_b]
    starts: list[Point] = []

    # The first deterministic draw is already a valid generic specialization.
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
        starts.append(add(source_left, source_right))

    assert len(points) == 98
    assert len(set(points)) == len(points)
    assert distance_sidon(points)

    endpoints = endpoint_map(points)
    actual_q_starts = []
    for pair_sum, (first, second) in endpoints.items():
        translated = add(pair_sum, q_value)
        if translated not in endpoints:
            continue
        third, fourth = endpoints[translated]
        if len({anchor_a, anchor_b, first, second, third, fourth}) == 6:
            actual_q_starts.append(pair_sum)
    assert set(actual_q_starts) == set(starts)

    labels = pair_labels(points)
    assert [labels[start] for start in starts] == [
        4 * scale * scale * label for label in abstract_labels
    ]
    records: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for first, first_label in enumerate(abstract_labels):
        for second, second_label in enumerate(abstract_labels):
            records[first_label + 18 * second_label].append((first, second))

    energy = sum(len(bucket) ** 2 for bucket in records.values())
    full_edges = comb(len(points), 2)
    cutoff = full_edges // h
    off_diagonal = three = four = resonant = large = residual_large = 0
    edge_vectors = [
        (-2 * scale * x, -2 * scale * y) for x, y in representing_vectors
    ]
    for bucket in records.values():
        for first_index, (source, target) in enumerate(bucket):
            for second_index, (other_source, other_target) in enumerate(bucket):
                if first_index == second_index:
                    continue
                off_diagonal += 1
                if len({source, target, other_source, other_target}) < 4:
                    three += 1
                    continue
                four += 1
                if (
                    squarefree_kernel(abstract_labels[source])
                    == squarefree_kernel(abstract_labels[other_source])
                    and squarefree_kernel(abstract_labels[target])
                    == squarefree_kernel(abstract_labels[other_target])
                ):
                    resonant += 1

                source_vector = edge_vectors[source]
                other_source_vector = edge_vectors[other_source]
                target_vector = edge_vectors[target]
                other_target_vector = edge_vectors[other_target]
                source_area = 2 * (
                    source_vector[0] * other_source_vector[1]
                    - source_vector[1] * other_source_vector[0]
                )
                target_area = 2 * (
                    target_vector[0] * other_target_vector[1]
                    - target_vector[1] * other_target_vector[0]
                )
                large += abs(target_area) > cutoff
                residual_large += abs(source_area + 18 * target_area) > cutoff

    assert (energy, off_diagonal, three, four, resonant) == (736, 160, 16, 144, 0)
    assert large == four and residual_large == four
    return (
        len(points),
        h,
        full_edges,
        cutoff,
        h * h,
        energy,
        off_diagonal,
        three,
        four,
        large,
        residual_large,
    )


def main() -> None:
    ordinary = [
        ("closure-30", POINTS[:30], (14, 435, 31, 252, 4, 0, 4, 248, 1)),
        ("closure-40", POINTS[:40], (23, 780, 33, 2_648, 82, 4, 86, 2_562, 2)),
        ("closure-80", POINTS[:80], (63, 3_160, 50, 22_474, 190, 8, 198, 22_276, 2)),
        ("closure-120", POINTS[:120], (127, 7_140, 56, 116_938, 448, 10, 458, 116_480, 3)),
        ("source-45", SOURCE_POINTS, (22, 990, 45, 830, 22, 0, 22, 808, 1)),
        ("perpendicular-ruler-40", ruler_points(), (14, 780, 55, 18, 10, 10, 10, 8, 3)),
        ("Costas-22", transformed_costas(23), (34, 231, 6, 514, 0, 0, 0, 514, 3)),
        ("parabola-image-43", transformed_parabola_43(), (171, 903, 5, 2_708, 50, 44, 90, 2_618, 3)),
    ]
    for name, points, expected in ordinary:
        q_value, starts = largest_fibre(points)
        actual = residual_profile(points, q_value, starts, list(endpoint_map(points)))
        assert actual == expected, (name, actual, expected)
        print(name, actual)

    points, q_value, starts, targets = resonant_two_arm_data(50)
    expected_two_arm = (114, 1_225, 10, 612, 612, 612, 612, 0, 3)
    actual_two_arm = residual_profile(points, q_value, starts, targets)
    assert actual_two_arm == expected_two_arm
    print("two-arm-50-restricted", actual_two_arm)

    dressed = dressed_certificate()
    assert dressed == (98, 24, 4_753, 198, 576, 736, 160, 16, 144, 144, 144)
    print("dressed-sums-of-two-squares", dressed)
    print("metric scalar large-area Gaussian residual audit: PASS")


if __name__ == "__main__":
    main()
