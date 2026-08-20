#!/usr/bin/env python3
"""Exact checks for FULL_NINE_METRIC_ARRAY_PELL_GATE.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_third_energy_centroid_gate import unordered_triple_fibres
from verify_dilated_internal_pair_sum_charge import transformed_parabola_43
from verify_equal_centroid_nine_anchor_symmetry import planted_points
from verify_orthogonal_energy_product_ruler_barrier import squared_distance_sidon
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Triple = tuple[int, int, int]
Profile = tuple[int, int, int, int, int, int, int]


COLLISION_POINTS: list[Point] = [
    (-12, -3),
    (5, 5),
    (7, -2),
    (9, -12),
    (-11, 2),
    (2, 10),
    (-26, -29),
    (-13, -9),
    (-3, -22),
    (-4, -31),
    (-24, -20),
    (-14, -9),
]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def squared_norm(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def distance(points: list[Point], first: int, second: int) -> int:
    return squared_norm(subtract(points[first], points[second]))


def doubled_area(points: list[Point], triple: Triple) -> int:
    first, second, third = (points[index] for index in triple)
    u_value = subtract(second, first)
    v_value = subtract(third, first)
    return u_value[0] * v_value[1] - u_value[1] * v_value[0]


def canonical_sides(points: list[Point], triple: Triple) -> tuple[int, int, int]:
    values = tuple(
        sorted(distance(points, first, second) for first, second in combinations(triple, 2))
    )
    assert len(set(values)) == 3
    return values  # type: ignore[return-value]


def full_array(
    first_sides: tuple[int, int, int],
    second_sides: tuple[int, int, int],
) -> tuple[int, ...]:
    return tuple(
        first + 18 * second
        for first in first_sides
        for second in second_sides
    )


def check_pell(points: list[Point], triple: Triple) -> None:
    first, second, third = canonical_sides(points, triple)
    offset_one = second - first
    offset_two = third - first
    area = doubled_area(points, triple)
    x_value = 3 * first + offset_one + offset_two
    y_value = 2 * area
    norm_value = 4 * (
        offset_one * offset_one
        - offset_one * offset_two
        + offset_two * offset_two
    )
    assert x_value * x_value - 3 * y_value * y_value == norm_value
    assert norm_value > 0


def maximum_collinearity(points: list[Point]) -> int:
    maximum = 2
    for first, second in combinations(range(len(points)), 2):
        count = 0
        for third in range(len(points)):
            u_value = subtract(points[second], points[first])
            v_value = subtract(points[third], points[first])
            if u_value[0] * v_value[1] == u_value[1] * v_value[0]:
                count += 1
        maximum = max(maximum, count)
    return maximum


def side_length(points: list[Point]) -> int:
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    return max(
        max(x_values) - min(x_values),
        max(y_values) - min(y_values),
    )


def profile(points: list[Point]) -> Profile:
    assert squared_distance_sidon(points)
    loads: Counter[tuple[int, ...]] = Counter()
    unordered_records = 0
    for members in unordered_triple_fibres(points).values():
        for first, second in combinations(members, 2):
            assert set(first).isdisjoint(second)
            unordered_records += 1
            check_pell(points, first)
            check_pell(points, second)
            for source, target in ((first, second), (second, first)):
                loads[
                    full_array(
                        canonical_sides(points, source),
                        canonical_sides(points, target),
                    )
                ] += 1

    mass = sum(loads.values())
    assert mass == 2 * unordered_records
    return (
        len(points),
        side_length(points),
        unordered_records,
        mass,
        len(loads),
        sum(load * load for load in loads.values()),
        max(loads.values(), default=0),
    )


def collision_check() -> None:
    points = COLLISION_POINTS
    assert squared_distance_sidon(points)
    assert maximum_collinearity(points) == 2
    assert side_length(points) == 41

    first_source = (0, 1, 2)
    first_target = (3, 4, 5)
    second_source = (6, 7, 8)
    second_target = (9, 10, 11)
    assert tuple(
        sum(points[index][axis] for index in first_source) for axis in (0, 1)
    ) == tuple(
        sum(points[index][axis] for index in first_target) for axis in (0, 1)
    ) == (0, 0)
    assert tuple(
        sum(points[index][axis] for index in second_source) for axis in (0, 1)
    ) == tuple(
        sum(points[index][axis] for index in second_target) for axis in (0, 1)
    ) == (-42, -60)

    first_source_sides = canonical_sides(points, first_source)
    first_target_sides = canonical_sides(points, first_target)
    second_source_sides = canonical_sides(points, second_source)
    second_target_sides = canonical_sides(points, second_target)
    assert first_source_sides == (53, 353, 362)
    assert second_source_sides == (269, 569, 578)
    assert second_target_sides == (221, 521, 584)
    assert first_target_sides == (233, 533, 596)
    assert tuple(
        second - first
        for first, second in zip(first_source_sides, second_source_sides)
    ) == (216, 216, 216)
    assert tuple(
        first - second
        for first, second in zip(first_target_sides, second_target_sides)
    ) == (12, 12, 12)

    expected_array = (
        4_247,
        9_647,
        10_781,
        4_547,
        9_947,
        11_081,
        4_556,
        9_956,
        11_090,
    )
    assert full_array(first_source_sides, first_target_sides) == expected_array
    assert full_array(second_source_sides, second_target_sides) == expected_array


def main() -> None:
    collision_check()
    families: list[tuple[str, list[Point], Profile]] = [
        (
            "closure-40",
            POINTS[:40],
            (40, 223, 690, 1_380, 1_380, 1_380, 1),
        ),
        (
            "Costas-22",
            transformed_costas(23),
            (22, 131, 519, 1_038, 1_038, 1_038, 1),
        ),
        (
            "parabola-43",
            transformed_parabola_43(),
            (43, 2_586, 10_571, 21_142, 21_142, 21_142, 1),
        ),
        (
            "planted-14",
            planted_points(),
            (14, 87_631_682, 3, 6, 6, 6, 1),
        ),
        (
            "collision-12",
            COLLISION_POINTS,
            (12, 41, 3, 6, 5, 8, 2),
        ),
    ]
    for name, points, expected in families:
        actual = profile(points)
        assert actual == expected, (name, actual, expected)
        print(name, actual)
    print("full nine metric array Pell gate: PASS")


if __name__ == "__main__":
    main()
