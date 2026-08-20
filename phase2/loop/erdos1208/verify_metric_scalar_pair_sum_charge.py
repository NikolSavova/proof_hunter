#!/usr/bin/env python3
"""Exact checks for the metric scalar clean-pair-sum charge."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points, side_length
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_orthogonal_energy_product_ruler_barrier import squared_distance_sidon
from verify_transverse_closure_witness import POINTS
from verify_transverse_row_source_c4 import SOURCE_POINTS


Point = tuple[int, int]
Profile = tuple[int, int, Point, int, int, int, int, int, int]

PATTERN_EXPECTED: dict[tuple[int, int], tuple[int, int]] = {
    # (three distinct edge labels, eight distinct endpoint labels)
    (30, 150): (0, 70),
    (40, 223): (4, 1_276),
    (80, 719): (30, 15_930),
    (120, 1_514): (70, 91_308),
    (45, 324): (2, 394),
    (40, 3_202): (0, 4),
    (22, 131): (14, 148),
    (43, 2_586): (12, 1_420),
}


def pair_labels(points: list[Point]) -> dict[Point, int]:
    output: dict[Point, int] = {}
    for first, second in combinations(range(len(points)), 2):
        left, right = points[first], points[second]
        pair_sum = left[0] + right[0], left[1] + right[1]
        dx, dy = left[0] - right[0], left[1] - right[1]
        output[pair_sum] = dx * dx + dy * dy
    assert len(output) == len(points) * (len(points) - 1) // 2
    assert len(output) == len(set(output.values()))
    return output


def profile(points: list[Point], coefficient: int = 18) -> Profile:
    assert squared_distance_sidon(points)
    labels = pair_labels(points)
    fibres = clean_start_fibres(points)
    difference = max(fibres, key=lambda value: len(fibres[value]))
    first_labels = [labels[start] for start in fibres[difference]]
    all_labels = list(labels.values())

    loads = Counter(
        first + coefficient * second
        for first in first_labels
        for second in all_labels
    )
    mass = len(first_labels) * len(all_labels)
    energy = sum(load * load for load in loads.values())

    # Every off-diagonal collision with only three distinct unordered edge
    # labels is one of the four repetitions in Proposition 2.1.
    records_by_value: dict[int, list[tuple[Point, Point]]] = {}
    endpoint_pair = {
        pair_sum: endpoints
        for pair_sum, endpoints in (
            (
                (points[first][0] + points[second][0],
                 points[first][1] + points[second][1]),
                (first, second),
            )
            for first, second in combinations(range(len(points)), 2)
        )
    }
    for start in fibres[difference]:
        first_edge = endpoint_pair[start]
        for pair_sum, second_edge in endpoint_pair.items():
            value = labels[start] + coefficient * labels[pair_sum]
            records_by_value.setdefault(value, []).append((first_edge, second_edge))
    three_edge_collisions = 0
    eight_endpoint_collisions = 0
    for records in records_by_value.values():
        for first_index, first_record in enumerate(records):
            for second_index, second_record in enumerate(records):
                if first_index == second_index:
                    continue
                edge_labels = {
                    frozenset(first_record[0]),
                    frozenset(first_record[1]),
                    frozenset(second_record[0]),
                    frozenset(second_record[1]),
                }
                assert len(edge_labels) >= 3
                if len(edge_labels) == 3:
                    three_edge_collisions += 1
                endpoints = {
                    *first_record[0],
                    *first_record[1],
                    *second_record[0],
                    *second_record[1],
                }
                if len(endpoints) == 8:
                    eight_endpoint_collisions += 1
    assert three_edge_collisions <= 4 * len(first_labels) ** 2
    pattern_key = len(points), side_length(points)
    if pattern_key in PATTERN_EXPECTED:
        assert (
            three_edge_collisions,
            eight_endpoint_collisions,
        ) == PATTERN_EXPECTED[pattern_key]

    # Direct check of the exact difference-correlation formula (1.3).
    if len(points) <= 50:
        first_differences = Counter(
            left - right for left in first_labels for right in first_labels
        )
        all_differences = Counter(
            left - right for left in all_labels for right in all_labels
        )
        predicted = sum(
            multiplicity * all_differences.get(-difference // coefficient, 0)
            for difference, multiplicity in first_differences.items()
            if difference % coefficient == 0
        )
        assert predicted == energy

    assert len(loads) * energy >= mass * mass
    assert len(loads) <= 2 * (coefficient + 1) * side_length(points) ** 2 + 1
    return (
        len(points),
        side_length(points),
        difference,
        len(first_labels),
        len(all_labels),
        mass,
        len(loads),
        energy,
        max(loads.values()),
    )


def integer_parabola(size: int) -> list[Point]:
    points = [(value, value * value) for value in range(size)]

    # Independent recovery proof: floor(sqrt(d)) is the product uv.
    recovered: dict[int, tuple[int, int]] = {}
    for first, second in combinations(range(size), 2):
        u, v = second - first, second + first
        distance = u * u * (1 + v * v)
        product = int(distance**0.5)
        while (product + 1) * (product + 1) <= distance:
            product += 1
        while product * product > distance:
            product -= 1
        assert product == u * v
        recovered_u_squared = distance - product * product
        assert recovered_u_squared == u * u
        assert distance not in recovered
        recovered[distance] = first, second
    return points


def main() -> None:
    families: list[tuple[str, list[Point], Profile]] = [
        ("closure-30", POINTS[:30],
         (30, 150, (-15, -19), 14, 435, 6_090, 5_964, 6_342, 2)),
        ("closure-40", POINTS[:40],
         (40, 223, (-12, -18), 23, 780, 17_940, 16_732, 20_592, 4)),
        ("closure-80", POINTS[:80],
         (80, 719, (-2, 0), 63, 3_160, 199_080, 188_394, 221_584, 4)),
        ("closure-120", POINTS[:120],
         (120, 1_514, (66, 14), 127, 7_140, 906_780,
          851_608, 1_023_788, 6)),
        ("source-45", SOURCE_POINTS,
         (45, 324, (-45, -21), 22, 990, 21_780, 21_364, 22_612, 2)),
        ("perpendicular-ruler-40", ruler_points(),
         (40, 3_202, (0, -314), 14, 780, 10_920, 10_911, 10_938, 2)),
        ("Costas-22", transformed_costas(23),
         (22, 131, (13, 21), 34, 231, 7_854, 7_601, 8_382, 3)),
        ("parabola-image-43", transformed_parabola_43(),
         (43, 2_586, (396, -38), 171, 903, 154_413,
          153_065, 157_133, 3)),
    ]

    for name, points, expected in families:
        actual = profile(points)
        assert actual == expected, (name, actual, expected)
        print(
            name,
            actual,
            "normalized",
            actual[7] / actual[5],
            "patterns",
            PATTERN_EXPECTED[(actual[0], actual[1])],
        )

    parabola_expected: dict[int, Profile] = {
        10: (10, 81, (-2, -20), 3, 45, 135, 135, 135, 1),
        15: (15, 196, (-4, -64), 7, 105, 735, 732, 741, 2),
        20: (20, 361, (-6, -108), 14, 190, 2_660, 2_649, 2_682, 2),
        25: (25, 576, (-6, -132), 22, 300, 6_600, 6_554, 6_692, 2),
        30: (30, 841, (-6, -180), 31, 435, 13_485, 13_400, 13_657, 3),
        40: (40, 1_521, (-6, -216), 54, 780, 42_120, 41_880, 42_602, 3),
        50: (50, 2_401, (-12, -528), 75, 1_225, 91_875,
             91_331, 92_977, 3),
    }
    for size, expected in parabola_expected.items():
        actual = profile(integer_parabola(size))
        assert actual == expected, (size, actual, expected)
        print("integer-parabola", size, actual, "normalized", actual[7] / actual[5])

    print("metric scalar pair-sum charge: PASS")


if __name__ == "__main__":
    main()
