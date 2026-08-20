#!/usr/bin/env python3
"""Exact checks for METRIC_SCALAR_SQUARECLASS_TRANSVERSE_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import gcd, isqrt

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import side_length
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_gaussian_edge_vector_charge import add, subtract
from verify_gaussian_edge_vector_two_arm_barrier import (
    choose_translation,
    dense_ruler,
)
from verify_metric_scalar_pair_sum_charge import pair_labels
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Edge = tuple[Point, Point]
Profile = tuple[int, ...]


EXPECTED: dict[str, Profile] = {
    # k, h, mass, energy, resonant energy, transverse energy,
    # four-edge resonant, four-edge transverse, parallel-parallel,
    # maximum cell load, global squareclasses, source squareclasses.
    "closure-30": (30, 14, 6_090, 6_342, 6_090, 252,
                   0, 252, 0, 1, 310, 14),
    "closure-40": (40, 23, 17_940, 20_592, 17_940, 2_652,
                   0, 2_648, 0, 1, 539, 22),
    "closure-80": (80, 63, 199_080, 221_584, 199_080, 22_504,
                   0, 22_474, 0, 1, 2_430, 62),
    "closure-120": (120, 127, 906_780, 1_023_788, 906_780, 117_008,
                    0, 116_938, 0, 1, 5_713, 123),
    "Costas-22": (22, 34, 7_854, 8_382, 7_854, 528,
                  0, 514, 0, 1, 156, 32),
    "parabola-image-43": (43, 171, 154_413, 157_133, 154_421, 2_712,
                          4, 2_704, 4, 2, 600, 154),
}


def norm(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def dot(left: Point, right: Point) -> int:
    return left[0] * right[0] + left[1] * right[1]


def squarefree_kernel(value: int) -> int:
    output = 1
    prime = 2
    while prime * prime <= value:
        odd_valuation = False
        while value % prime == 0:
            value //= prime
            odd_valuation = not odd_valuation
        if odd_valuation:
            output *= prime
        prime += 1 if prime == 2 else 2
    return output * value


def divisor_count(value: int) -> int:
    output = 1
    prime = 2
    while prime * prime <= value:
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        output *= exponent + 1
        prime += 1 if prime == 2 else 2
    if value > 1:
        output *= 2
    return output


def verify_binary_representation_bound() -> None:
    # A finite independent stress of Lemma 3.1, including coefficients with
    # large common factors and nonsquarefree products.
    for first_coefficient in range(1, 17):
        for second_coefficient in range(1, 17):
            for value in range(1, 161):
                representations = 0
                for first in range(-isqrt(value // first_coefficient),
                                   isqrt(value // first_coefficient) + 1):
                    remainder = value - first_coefficient * first * first
                    if remainder < 0 or remainder % second_coefficient:
                        continue
                    second_squared = remainder // second_coefficient
                    second = isqrt(second_squared)
                    if second * second == second_squared:
                        representations += 1 if second == 0 else 2
                assert representations <= 6 * divisor_count(
                    first_coefficient * value
                )


def endpoint_map(points: list[Point]) -> dict[Point, Edge]:
    output: dict[Point, Edge] = {}
    for first, second in combinations(points, 2):
        edge = tuple(sorted((first, second)))
        pair_sum = add(edge[0], edge[1])
        assert pair_sum not in output
        output[pair_sum] = edge
    return output


def primitive_direction(edge: Edge) -> Point:
    difference = subtract(edge[0], edge[1])
    divisor = gcd(abs(difference[0]), abs(difference[1]))
    first, second = difference[0] // divisor, difference[1] // divisor
    if first < 0 or (first == 0 and second < 0):
        first, second = -first, -second
    return first, second


def collision_profile(points: list[Point]) -> Profile:
    labels = pair_labels(points)
    kernels = {
        pair_sum: squarefree_kernel(label)
        for pair_sum, label in labels.items()
    }
    endpoints = endpoint_map(points)
    directions = {
        pair_sum: primitive_direction(edge)
        for pair_sum, edge in endpoints.items()
    }
    fibres = clean_start_fibres(points)
    q_value = max(fibres, key=lambda value: len(fibres[value]))
    starts = fibres[q_value]
    # Exact squared form of K >= N^2/(8m^2), equation (5.6).
    assert len(endpoints) ** 2 <= (
        8 * side_length(points) ** 2 * len(set(kernels.values()))
    )

    records_by_charge: dict[int, list[tuple[Point, Point]]] = defaultdict(list)
    cell_loads: Counter[tuple[int, int, int]] = Counter()
    for start in starts:
        for target in endpoints:
            charge = labels[start] + 18 * labels[target]
            records_by_charge[charge].append((start, target))
            cell_loads[charge, kernels[start], kernels[target]] += 1

    mass = len(starts) * len(endpoints)
    energy = sum(len(records) ** 2 for records in records_by_charge.values())
    resonant_energy = sum(load * load for load in cell_loads.values())
    four_edge_resonant = 0
    four_edge_transverse = 0
    parallel_parallel = 0
    complete_differences = {
        subtract(first, second)
        for first in points
        for second in points
    }

    for records in records_by_charge.values():
        for first_index, first_record in enumerate(records):
            for second_index, second_record in enumerate(records):
                if first_index == second_index:
                    continue
                start, target = first_record
                other_start, other_target = second_record
                if len({start, target, other_start, other_target}) < 4:
                    continue

                c_value, d_value = endpoints[start]
                e_value, f_value = endpoints[add(start, q_value)]
                other_c, other_d = endpoints[other_start]
                other_e, other_f = endpoints[add(other_start, q_value)]
                x_value, y_value = endpoints[target]
                other_x, other_y = endpoints[other_target]

                alpha = subtract(c_value, other_c)
                beta = subtract(d_value, other_d)
                eta = subtract(e_value, other_e)
                theta = subtract(f_value, other_f)
                gamma = subtract(x_value, other_x)
                zeta = subtract(y_value, other_y)
                assert add(alpha, beta) == add(eta, theta)
                assert all(
                    vector in complete_differences
                    for vector in (alpha, beta, eta, theta, gamma, zeta)
                )

                source_vector = subtract(c_value, d_value)
                other_source_vector = subtract(other_c, other_d)
                target_vector = subtract(x_value, y_value)
                other_target_vector = subtract(other_x, other_y)
                assert (
                    dot(
                        subtract(alpha, beta),
                        add(source_vector, other_source_vector),
                    )
                    + 18
                    * dot(
                        subtract(gamma, zeta),
                        add(target_vector, other_target_vector),
                    )
                    == 0
                )
                assert (
                    norm(source_vector) + 18 * norm(target_vector)
                    == norm(other_source_vector)
                    + 18 * norm(other_target_vector)
                )

                resonant = (
                    kernels[start] == kernels[other_start]
                    and kernels[target] == kernels[other_target]
                )
                if resonant:
                    four_edge_resonant += 1
                else:
                    four_edge_transverse += 1

                both_parallel = (
                    directions[start] == directions[other_start]
                    and directions[target] == directions[other_target]
                )
                if both_parallel:
                    parallel_parallel += 1
                    assert resonant

    return (
        len(points),
        len(starts),
        mass,
        energy,
        resonant_energy,
        energy - resonant_energy,
        four_edge_resonant,
        four_edge_transverse,
        parallel_parallel,
        max(cell_loads.values()),
        len(set(kernels.values())),
        len({kernels[start] for start in starts}),
    )


def resonant_two_arm_scalar(side_size: int) -> tuple[int, ...]:
    marks = dense_ruler(2 * side_size)
    first_marks, second_marks = marks[:side_size], marks[side_size:]
    translation = choose_translation(first_marks, second_marks)
    first_arm = [(mark, 0) for mark in first_marks]
    second_arm = [
        (translation[0] - mark, translation[1] - mark)
        for mark in second_marks
    ]
    points = first_arm + second_arm
    endpoints = endpoint_map(points)
    fibres = clean_start_fibres(points)
    first_points = set(first_arm)
    second_points = set(second_arm)

    internal_second: dict[Point, list[Point]] = defaultdict(list)
    for q_value, starts in fibres.items():
        for start in starts:
            if (
                set(endpoints[start]) <= second_points
                and set(endpoints[add(start, q_value)]) <= second_points
            ):
                internal_second[q_value].append(start)
    q_value = max(
        internal_second,
        key=lambda value: len(internal_second[value]),
    )
    starts = internal_second[q_value]
    first_targets = [
        pair_sum
        for pair_sum, edge in endpoints.items()
        if set(edge) <= first_points
    ]

    loads: Counter[int] = Counter()
    for start in starts:
        source_label = norm(subtract(*endpoints[start]))
        assert squarefree_kernel(source_label) == 2
        for target in first_targets:
            target_label = norm(subtract(*endpoints[target]))
            assert squarefree_kernel(target_label) == 1
            loads[source_label + 18 * target_label] += 1

    return (
        len(starts),
        len(first_targets),
        sum(loads.values()),
        len(loads),
        sum(load * load for load in loads.values()),
        max(loads.values()),
    )


def main() -> None:
    verify_binary_representation_bound()
    families = [
        ("closure-30", POINTS[:30]),
        ("closure-40", POINTS[:40]),
        ("closure-80", POINTS[:80]),
        ("closure-120", POINTS[:120]),
        ("Costas-22", transformed_costas(23)),
        ("parabola-image-43", transformed_parabola_43()),
    ]
    for name, points in families:
        actual = collision_profile(points)
        assert actual == EXPECTED[name], (name, actual, EXPECTED[name])
        print(name, actual)

    two_arm = resonant_two_arm_scalar(50)
    assert two_arm == (114, 1_225, 139_650, 139_345, 140_262, 3)
    print("resonant-two-arm-50 restricted", two_arm)
    print("metric scalar squareclass-transverse gate: PASS")


if __name__ == "__main__":
    main()
