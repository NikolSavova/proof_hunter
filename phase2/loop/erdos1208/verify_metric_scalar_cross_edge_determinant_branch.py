#!/usr/bin/env python3
"""Exact checks for METRIC_SCALAR_CROSS_EDGE_DETERMINANT_BRANCH.md."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points
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
from verify_transverse_row_source_c4 import SOURCE_POINTS


Point = tuple[int, int]
Edge = tuple[Point, Point]
Profile = tuple[int, ...]


EXPECTED: dict[str, Profile] = {
    # k, h, target edges, four-edge collisions, L=floor(target/h),
    # low-area collisions, parallel-target collisions,
    # maximum relevant fixed-(r,d) target multiplicity, occupied (r,d).
    "closure-30": (30, 14, 435, 252, 31, 4, 0, 1, 252),
    "closure-40": (40, 23, 780, 2_648, 33, 82, 2, 2, 2_480),
    "closure-80": (80, 63, 3_160, 22_474, 50, 190, 6, 2, 22_378),
    "closure-120": (
        120, 127, 7_140, 116_938, 56, 448, 14, 3, 114_960
    ),
    "source-45": (45, 22, 990, 830, 45, 22, 2, 1, 830),
    "perpendicular-ruler-40": (40, 14, 780, 18, 55, 10, 10, 3, 14),
    "Costas-22": (22, 34, 231, 514, 6, 0, 0, 3, 462),
    "parabola-image-43": (43, 171, 903, 2_708, 5, 50, 28, 3, 2_546),
    "resonant-two-arm-50-restricted": (
        100, 114, 1_225, 612, 10, 612, 612, 3, 520
    ),
}


def dot(left: Point, right: Point) -> int:
    return left[0] * right[0] + left[1] * right[1]


def determinant(left: Point, right: Point) -> int:
    return left[0] * right[1] - left[1] * right[0]


def norm(vector: Point) -> int:
    return dot(vector, vector)


def gaussian_product(left: Point, right: Point) -> Point:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def conjugate(vector: Point) -> Point:
    return vector[0], -vector[1]


def endpoint_map(points: list[Point]) -> dict[Point, Edge]:
    output: dict[Point, Edge] = {}
    for first, second in combinations(points, 2):
        edge = tuple(sorted((first, second)))
        pair_sum = add(edge[0], edge[1])
        assert pair_sum not in output
        output[pair_sum] = edge
    return output


def cross_factor_checks(
    first_edge: Edge,
    second_edge: Edge,
) -> tuple[int, int, Point, Point]:
    first_left, first_right = first_edge
    second_left, second_right = second_edge
    first_vector = subtract(first_left, first_right)
    second_vector = subtract(second_left, second_right)

    alpha = subtract(first_left, second_left)
    beta = subtract(first_right, second_right)
    rho = subtract(first_left, second_right)
    sigma = subtract(first_right, second_left)
    difference_factor = subtract(alpha, beta)
    sum_factor = subtract(rho, sigma)

    assert add(alpha, beta) == add(rho, sigma)
    assert difference_factor == subtract(first_vector, second_vector)
    assert sum_factor == add(first_vector, second_vector)

    radius_difference = norm(first_vector) - norm(second_vector)
    doubled_area = 2 * determinant(first_vector, second_vector)
    assert dot(difference_factor, sum_factor) == radius_difference
    assert determinant(difference_factor, sum_factor) == doubled_area

    # With vectors represented by x+iy, P*conj(R)=r-id.
    assert gaussian_product(
        difference_factor,
        conjugate(sum_factor),
    ) == (radius_difference, -doubled_area)
    return radius_difference, doubled_area, difference_factor, sum_factor


def profile(
    points: list[Point],
    q_value: Point,
    starts: list[Point],
    targets: list[Point],
) -> Profile:
    labels = pair_labels(points)
    endpoints = endpoint_map(points)
    records_by_charge: dict[int, list[tuple[Point, Point]]] = defaultdict(list)
    for start in starts:
        for target in targets:
            records_by_charge[
                labels[start] + 18 * labels[target]
            ].append((start, target))

    four_edge_collisions = 0
    low_area_collisions = 0
    parallel_target_collisions = 0
    cutoff = len(targets) // len(starts)
    target_pairs_by_radius_area: dict[
        tuple[int, int],
        set[tuple[Point, Point]],
    ] = defaultdict(set)
    factors_by_radius_area: dict[
        tuple[int, int],
        dict[tuple[Point, Point], tuple[Point, Point]],
    ] = defaultdict(dict)

    for records in records_by_charge.values():
        for first_index, first_record in enumerate(records):
            for second_index, second_record in enumerate(records):
                if first_index == second_index:
                    continue
                start, target = first_record
                other_start, other_target = second_record
                if len({start, target, other_start, other_target}) < 4:
                    continue

                source_radius, _, _, _ = cross_factor_checks(
                    endpoints[start], endpoints[other_start]
                )
                target_radius, target_area, difference_factor, sum_factor = (
                    cross_factor_checks(
                        endpoints[target], endpoints[other_target]
                    )
                )
                assert source_radius + 18 * target_radius == 0
                assert source_radius != 0 and target_radius != 0

                # Retain and check the clean-start translate equation.
                c_value, d_value = endpoints[start]
                other_c, other_d = endpoints[other_start]
                e_value, f_value = endpoints[add(start, q_value)]
                other_e, other_f = endpoints[add(other_start, q_value)]
                assert add(
                    subtract(c_value, other_c),
                    subtract(d_value, other_d),
                ) == add(
                    subtract(e_value, other_e),
                    subtract(f_value, other_f),
                )

                four_edge_collisions += 1
                if abs(target_area) <= cutoff:
                    low_area_collisions += 1
                if target_area == 0:
                    parallel_target_collisions += 1

                key = target_radius, target_area
                target_pair = target, other_target
                target_pairs_by_radius_area[key].add(target_pair)
                factors = difference_factor, sum_factor
                old_pair = factors_by_radius_area[key].setdefault(
                    factors,
                    target_pair,
                )
                # A fixed Gaussian factor pair determines the two canonical
                # edge vectors and hence, by distance-Sidonicity, the edges.
                assert old_pair == target_pair

    maximum_multiplicity = max(
        (len(pairs) for pairs in target_pairs_by_radius_area.values()),
        default=0,
    )
    finite_completion_bound = (
        (2 * cutoff + 1)
        * len(starts)
        * (len(starts) - 1)
        * max(1, maximum_multiplicity)
    )
    assert low_area_collisions <= finite_completion_bound
    # All current stresses satisfy the desired scale before any divisor
    # factor; this is evidence, while the displayed bound checks the proof.
    assert low_area_collisions <= len(starts) * len(targets)

    return (
        len(points),
        len(starts),
        len(targets),
        four_edge_collisions,
        cutoff,
        low_area_collisions,
        parallel_target_collisions,
        maximum_multiplicity,
        len(target_pairs_by_radius_area),
    )


def largest_fibre(points: list[Point]) -> tuple[Point, list[Point]]:
    fibres = clean_start_fibres(points)
    q_value = max(fibres, key=lambda value: len(fibres[value]))
    return q_value, fibres[q_value]


def resonant_two_arm_data(
    side_size: int,
) -> tuple[list[Point], Point, list[Point], list[Point]]:
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
    targets = [
        pair_sum
        for pair_sum, edge in endpoints.items()
        if set(edge) <= first_points
    ]
    return points, q_value, internal_second[q_value], targets


def main() -> None:
    ordinary_families = [
        ("closure-30", POINTS[:30]),
        ("closure-40", POINTS[:40]),
        ("closure-80", POINTS[:80]),
        ("closure-120", POINTS[:120]),
        ("source-45", SOURCE_POINTS),
        ("perpendicular-ruler-40", ruler_points()),
        ("Costas-22", transformed_costas(23)),
        ("parabola-image-43", transformed_parabola_43()),
    ]
    for name, points in ordinary_families:
        q_value, starts = largest_fibre(points)
        actual = profile(
            points,
            q_value,
            starts,
            list(endpoint_map(points)),
        )
        assert actual == EXPECTED[name], (name, actual, EXPECTED[name])
        print(name, actual)

    name = "resonant-two-arm-50-restricted"
    points, q_value, starts, targets = resonant_two_arm_data(50)
    actual = profile(points, q_value, starts, targets)
    assert actual == EXPECTED[name], (name, actual, EXPECTED[name])
    print(name, actual)

    print("metric scalar cross-edge determinant branch: PASS")


if __name__ == "__main__":
    main()
