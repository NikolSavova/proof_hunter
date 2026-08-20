#!/usr/bin/env python3
"""Exact adversarial stress for the surviving metric scalar charge."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import gcd
from random import Random

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_gaussian_edge_vector_charge import add, subtract
from verify_gaussian_edge_vector_two_arm_barrier import (
    dense_ruler,
    distance_sidon,
)
from verify_metric_scalar_squareclass_transverse import squarefree_kernel
from verify_transverse_closure_witness import POINTS
from verify_transverse_row_source_c4 import SOURCE_POINTS


Point = tuple[int, int]
Form = tuple[int, int, int]
Aggregate = tuple[object, ...]


AGGREGATE_EXPECTED: dict[str, Aggregate] = {
    # k, N, active q, S=sum h, sum M, off-diagonal sum,
    # worst h, worst M, worst q, N(S+k^3), N(S+k*#q).
    "closure-40": (
        40, 780, 1_518, 12_420, 10_034_962, 347_362,
        23, 20_592, (-12, -18), 59_607_600, 57_049_200,
    ),
    "Costas-22": (
        22, 231, 462, 9_342, 2_230_624, 72_622,
        34, 8_382, (13, 21), 4_617_690, 4_505_886,
    ),
    "parabola-43-identity": (
        43, 903, 1_806, 190_278, 173_964_356, 2_143_322,
        171, 157_399, (-396, 38), 243_615_855, 241_946_208,
    ),
    "parabola-43-champion": (
        43, 903, 1_806, 190_278, 174_794_072, 2_973_038,
        171, 158_851, (-396, 38), 243_615_855, 241_946_208,
    ),
    "source-45": (
        45, 990, 1_920, 12_834, 12_922_594, 216_934,
        22, 22_612, (-45, -21), 102_919_410, 98_241_660,
    ),
    "perpendicular-ruler-40": (
        40, 780, 774, 4_914, 3_835_108, 2_188,
        14, 10_938, (0, -314), 53_752_920, 27_981_720,
    ),
}


MULTIARM_EXPECTED: dict[tuple[int, int], Aggregate] = {
    # side size, arms -> k,N,#q,S,sumM,off,worst h,worst M,worst q,N(S+k^3)
    (12, 2): (24, 276, 252, 756, 208_840, 184,
              6, 1_666, (86, 86), 4_024_080),
    (12, 3): (36, 630, 474, 1_278, 805_480, 340,
              6, 3_792, (86, 86), 30_198_420),
    (12, 4): (48, 1_128, 756, 1_908, 2_152_970, 746,
              6, 6_786, (86, 258), 126_900_000),
    (16, 2): (32, 496, 480, 3_276, 1_627_564, 2_668,
              12, 5_982, (138, 138), 17_877_824),
    (16, 3): (48, 1_128, 924, 5_220, 5_893_816, 5_656,
              13, 14_710, (138, 138), 130_635_936),
    (16, 4): (64, 2_016, 1_380, 7_200, 14_526_520, 11_320,
              13, 26_262, (138, 138), 542_997_504),
    (20, 2): (40, 780, 760, 11_520, 9_014_842, 29_242,
              27, 21_234, (-47, -47), 58_905_600),
    (20, 3): (60, 1_770, 1_524, 17_856, 31_664_630, 59_510,
              28, 49_692, (-47, -94), 413_925_120),
}


def edge_vectors(points: list[Point]) -> dict[Point, Point]:
    output: dict[Point, Point] = {}
    for first, second in combinations(points, 2):
        pair_sum = add(first, second)
        assert pair_sum not in output
        output[pair_sum] = subtract(first, second)
    return output


def metric_labels(vectors: dict[Point, Point], form: Form) -> dict[Point, int]:
    first, cross, second = form
    output = {
        pair_sum: (
            first * vector[0] * vector[0]
            + 2 * cross * vector[0] * vector[1]
            + second * vector[1] * vector[1]
        )
        for pair_sum, vector in vectors.items()
    }
    assert len(output) == len(set(output.values()))
    return output


def aggregate_profile(points: list[Point], form: Form = (1, 0, 1)) -> Aggregate:
    k = len(points)
    labels = metric_labels(edge_vectors(points), form)
    n_edges = len(labels)
    target_labels = list(labels.values())
    target_differences = Counter(
        first - second
        for first in target_labels
        for second in target_labels
    )
    fibres = clean_start_fibres(points)

    total_h = 0
    total_energy = 0
    total_off_diagonal = 0
    best_h = 0
    best_energy = 0
    best_q = (0, 0)
    for q_value, starts in fibres.items():
        source_labels = [labels[start] for start in starts]
        energy = sum(
            target_differences[(second - first) // 18]
            for first in source_labels
            for second in source_labels
            if (second - first) % 18 == 0
        )
        h_value = len(starts)
        assert energy >= h_value * n_edges
        total_h += h_value
        total_energy += energy
        total_off_diagonal += energy - h_value * n_edges
        if (
            best_h == 0
            or energy * (best_h + k) > best_energy * (h_value + k)
        ):
            best_h = h_value
            best_energy = energy
            best_q = q_value

    return (
        k,
        n_edges,
        len(fibres),
        total_h,
        total_energy,
        total_off_diagonal,
        best_h,
        best_energy,
        best_q,
        n_edges * (total_h + k**3),
        n_edges * (total_h + k * len(fibres)),
    )


def normalized_form(matrix: tuple[int, int, int, int]) -> Form:
    first, second, third, fourth = matrix
    form = (
        first * first + third * third,
        first * second + third * fourth,
        second * second + fourth * fourth,
    )
    divisor = gcd(gcd(form[0], abs(form[1])), form[2])
    return tuple(value // divisor for value in form)


def affine_scan() -> tuple[int, int, Form, int, int]:
    points = transformed_parabola_43()
    vectors = edge_vectors(points)
    fibres = clean_start_fibres(points)
    q_value = max(fibres, key=lambda value: len(fibres[value]))
    starts = fibres[q_value]
    n_edges = len(vectors)
    random = Random(2018)
    matrices = [(1, 0, 0, 1)]
    for _ in range(300):
        matrix = tuple(random.randint(-15, 15) for _ in range(4))
        if matrix[0] * matrix[3] - matrix[1] * matrix[2] != 0:
            matrices.append(matrix)

    forms_seen: set[Form] = set()
    accepted = 0
    best_form = (0, 0, 0)
    best_energy = 0
    best_load = 0
    for matrix in matrices:
        form = normalized_form(matrix)
        if form in forms_seen:
            continue
        forms_seen.add(form)
        labels = {
            pair_sum: (
                form[0] * vector[0] * vector[0]
                + 2 * form[1] * vector[0] * vector[1]
                + form[2] * vector[1] * vector[1]
            )
            for pair_sum, vector in vectors.items()
        }
        if len(set(labels.values())) != n_edges:
            continue
        accepted += 1
        target_labels = list(labels.values())
        loads = Counter(
            labels[start] + 18 * target
            for start in starts
            for target in target_labels
        )
        energy = sum(load * load for load in loads.values())
        if energy > best_energy:
            best_form = form
            best_energy = energy
            best_load = max(loads.values())

    return len(forms_seen), accepted, best_form, best_energy, best_load


def transform_champion(points: list[Point]) -> list[Point]:
    # M^T M=10*(1,-1; -1,17), so this is a genuine integral realization
    # of the champion normalized form.
    return [(-3 * x - y, -x + 13 * y) for x, y in points]


def champion_large_area_core() -> tuple[int, ...]:
    points = transform_champion(transformed_parabola_43())
    assert distance_sidon(points)
    k = len(points)
    vectors = edge_vectors(points)
    labels = metric_labels(vectors, (1, 0, 1))
    n_edges = len(labels)
    target_labels = list(labels.values())
    target_differences = Counter(
        first - second
        for first in target_labels
        for second in target_labels
    )
    fibres = clean_start_fibres(points)
    best_q = (0, 0)
    best_starts: list[Point] = []
    best_energy = 0
    for q_value, starts in fibres.items():
        source = [labels[start] for start in starts]
        energy = sum(
            target_differences[(second - first) // 18]
            for first in source
            for second in source
            if (second - first) % 18 == 0
        )
        if (
            not best_starts
            or energy * (len(best_starts) + k)
            > best_energy * (len(starts) + k)
        ):
            best_q = q_value
            best_starts = starts
            best_energy = energy

    endpoints: dict[Point, tuple[Point, Point]] = {}
    for first, second in combinations(points, 2):
        edge = tuple(sorted((first, second)))
        endpoints[add(edge[0], edge[1])] = edge
    kernels = {
        pair_sum: squarefree_kernel(label)
        for pair_sum, label in labels.items()
    }
    records: dict[int, list[tuple[Point, Point]]] = defaultdict(list)
    for start in best_starts:
        for target in endpoints:
            records[labels[start] + 18 * labels[target]].append((start, target))

    four_edge = 0
    transverse = 0
    large_area = 0
    low_area = 0
    parallel = 0
    source_overlap = 0
    target_overlap = 0
    both_overlap = 0
    neither_overlap = 0
    fully_endpoint_disjoint = 0
    cutoff = n_edges // len(best_starts)
    for charge_records in records.values():
        for first_index, (start, target) in enumerate(charge_records):
            for second_index, (other_start, other_target) in enumerate(
                charge_records
            ):
                if first_index == second_index:
                    continue
                if len({start, target, other_start, other_target}) < 4:
                    continue
                four_edge += 1
                is_transverse = (
                    kernels[start] != kernels[other_start]
                    or kernels[target] != kernels[other_target]
                )
                if not is_transverse:
                    continue
                transverse += 1
                first_vector = vectors[target]
                second_vector = vectors[other_target]
                doubled_area = abs(
                    2
                    * (
                        first_vector[0] * second_vector[1]
                        - first_vector[1] * second_vector[0]
                    )
                )
                if doubled_area <= cutoff:
                    low_area += 1
                else:
                    large_area += 1
                if doubled_area == 0:
                    parallel += 1
                if doubled_area > cutoff:
                    source_meets = not set(endpoints[start]).isdisjoint(
                        endpoints[other_start]
                    )
                    target_meets = not set(endpoints[target]).isdisjoint(
                        endpoints[other_target]
                    )
                    source_overlap += int(source_meets)
                    target_overlap += int(target_meets)
                    both_overlap += int(source_meets and target_meets)
                    neither_overlap += int(not source_meets and not target_meets)
                    four_endpoint_sets = (
                        endpoints[start],
                        endpoints[target],
                        endpoints[other_start],
                        endpoints[other_target],
                    )
                    fully_endpoint_disjoint += int(
                        len(set().union(*map(set, four_endpoint_sets))) == 8
                    )

    mass = len(best_starts) * n_edges
    maximum_load = max(map(len, records.values()))
    return (
        len(best_starts),
        best_energy,
        mass,
        best_energy - mass,
        four_edge,
        transverse,
        large_area,
        low_area,
        parallel,
        cutoff,
        best_q,
        source_overlap,
        target_overlap,
        both_overlap,
        neither_overlap,
        fully_endpoint_disjoint,
        maximum_load,
    )


def build_multiarm(arm_count: int, side_size: int) -> list[Point]:
    directions = [
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 3),
        (1, 4),
    ][:arm_count]
    marks = dense_ruler(side_size)
    points: list[Point] = []
    translation_parameter = 10 * max(marks) + 1
    for index, direction in enumerate(directions):
        if index == 0:
            translation = (0, 0)
        else:
            while True:
                translation = (
                    translation_parameter,
                    translation_parameter**2 + index,
                )
                arm = [
                    (
                        translation[0] + mark * direction[0],
                        translation[1] + mark * direction[1],
                    )
                    for mark in marks
                ]
                if distance_sidon(points + arm):
                    break
                translation_parameter += 1
            translation_parameter += max(marks) + 1
        points.extend(
            (
                translation[0] + mark * direction[0],
                translation[1] + mark * direction[1],
            )
            for mark in marks
        )
    assert distance_sidon(points)
    return points


def shortened(profile: Aggregate) -> Aggregate:
    return profile[:10]


def main() -> None:
    ordinary = [
        ("closure-40", POINTS[:40], (1, 0, 1)),
        ("Costas-22", transformed_costas(23), (1, 0, 1)),
        ("parabola-43-identity", transformed_parabola_43(), (1, 0, 1)),
        ("parabola-43-champion", transformed_parabola_43(), (1, -1, 17)),
        ("source-45", SOURCE_POINTS, (1, 0, 1)),
        ("perpendicular-ruler-40", ruler_points(), (1, 0, 1)),
    ]
    for name, points, form in ordinary:
        actual = aggregate_profile(points, form)
        assert actual == AGGREGATE_EXPECTED[name], (
            name,
            actual,
            AGGREGATE_EXPECTED[name],
        )
        print(name, actual)

    scan = affine_scan()
    assert scan == (295, 291, (1, -1, 17), 158_371, 3), scan
    print("affine scan", scan)

    core = champion_large_area_core()
    assert core == (
        171, 158_851, 154_413, 4_438, 4_416, 4_416,
        4_370, 46, 46, 5, (1_150, 890), 428, 394, 30, 3_578,
        2_232, 3,
    ), core
    print("champion large-area core", core)

    for (side_size, arm_count), expected in MULTIARM_EXPECTED.items():
        points = build_multiarm(arm_count, side_size)
        actual = shortened(aggregate_profile(points))
        assert actual == expected, ((side_size, arm_count), actual, expected)
        print("multiarm", side_size, arm_count, actual)

    print("metric scalar adversarial stress: PASS")


if __name__ == "__main__":
    main()
