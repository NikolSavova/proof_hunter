#!/usr/bin/env python3
"""Exact checks for CORRECTED_EQUAL_AREA_AMBIENT_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import gcd, isqrt, log

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points
from verify_dilated_internal_pair_sum_charge import transformed_parabola_43
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Direction = tuple[int, int]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def squared_norm(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def canonical_direction(vector: Point) -> tuple[Direction, int]:
    x_value, y_value = vector
    divisor = gcd(abs(x_value), abs(y_value))
    assert divisor
    direction = (x_value // divisor, y_value // divisor)
    coefficient = divisor
    if direction[0] < 0 or (direction[0] == 0 and direction[1] < 0):
        direction = (-direction[0], -direction[1])
        coefficient = -coefficient
    return direction, coefficient


def doubled_area(first: Point, second: Point, third: Point) -> int:
    return determinant(subtract(second, first), subtract(third, first))


def distance_sidon(points: list[Point]) -> bool:
    distances = [
        squared_norm(subtract(first, second))
        for first, second in combinations(points, 2)
    ]
    return len(distances) == len(set(distances))


def divisor_count(value: int) -> int:
    value = abs(value)
    assert value
    output = 0
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor == 0:
            output += 1 + (divisor * divisor != value)
    return output


def direction_structure(
    points: list[Point],
) -> tuple[
    Counter[Direction],
    dict[Direction, dict[int, int]],
    dict[Direction, Counter[int]],
]:
    edge_counts: Counter[Direction] = Counter()
    bases: dict[Direction, dict[int, int]] = defaultdict(dict)

    for first_index, second_index in combinations(range(len(points)), 2):
        first = points[first_index]
        second = points[second_index]
        direction, coefficient = canonical_direction(subtract(second, first))
        edge_counts[direction] += 1

        sigma = determinant(direction, first)
        assert determinant(direction, second) == sigma
        assert coefficient not in bases[direction]
        assert -coefficient not in bases[direction]
        bases[direction][coefficient] = sigma
        bases[direction][-coefficient] = sigma

    lines: dict[Direction, Counter[int]] = {}
    for direction in edge_counts:
        lines[direction] = Counter(
            determinant(direction, point) for point in points
        )

    return edge_counts, bases, lines


def enumerated_direction_area_loads(
    points: list[Point],
) -> Counter[tuple[Direction, int]]:
    output: Counter[tuple[Direction, int]] = Counter()
    for first_index, first in enumerate(points):
        for second_index, second in enumerate(points):
            if second_index == first_index:
                continue
            direction, _ = canonical_direction(subtract(second, first))
            for third_index, third in enumerate(points):
                if third_index in (first_index, second_index):
                    continue
                area = doubled_area(first, second, third)
                if area:
                    output[direction, area] += 1
    return output


def formula_direction_area_loads(
    bases: dict[Direction, dict[int, int]],
    lines: dict[Direction, Counter[int]],
) -> Counter[tuple[Direction, int]]:
    output: Counter[tuple[Direction, int]] = Counter()
    for direction, signed_bases in bases.items():
        line_loads = lines[direction]
        for coefficient, sigma in signed_bases.items():
            for line, load in line_loads.items():
                height = line - sigma
                if height:
                    output[direction, coefficient * height] += load
    return output


def profile(points: list[Point]) -> tuple[int, ...]:
    assert distance_sidon(points)
    k_value = len(points)
    number_edges = k_value * (k_value - 1) // 2
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    side = max(max(x_values) - min(x_values), max(y_values) - min(y_values))

    edge_counts, bases, lines = direction_structure(points)
    assert sum(edge_counts.values()) == number_edges
    for direction, count in edge_counts.items():
        assert len(bases[direction]) == 2 * count
        assert sum(load * load for load in lines[direction].values()) == (
            k_value + 2 * count
        )

        direction_height = max(abs(direction[0]), abs(direction[1]))
        assert count <= side // direction_height

    square_sum = sum(count * count for count in edge_counts.values())
    harmonic_bound = 4 * side * side * (1 + log(max(side, 1)))
    assert square_sum <= harmonic_bound

    enumerated = enumerated_direction_area_loads(points)
    formula = formula_direction_area_loads(bases, lines)
    assert enumerated == formula

    support_areas = {area for _, area in formula}
    maximum_tau = max((divisor_count(area) for area in support_areas), default=1)
    for (direction, area), load in formula.items():
        active = sum(
            area % coefficient == 0
            and lines[direction][
                bases[direction][coefficient] + area // coefficient
            ]
            > 0
            for coefficient in bases[direction]
        )
        assert active <= 2 * divisor_count(area)
        cauchy_right = 2 * maximum_tau * sum(
            lines[direction][
                bases[direction][coefficient] + area // coefficient
            ] ** 2
            for coefficient in bases[direction]
            if area % coefficient == 0
        )
        assert load * load <= cauchy_right

    parallel_energy = sum(load * load for load in formula.values())
    theorem_bound = 4 * maximum_tau * (
        k_value * number_edges + 2 * square_sum
    )
    assert parallel_energy <= theorem_bound

    return (
        k_value,
        side,
        number_edges,
        len(edge_counts),
        max(edge_counts.values(), default=0),
        square_sum,
        len(formula),
        parallel_energy,
        maximum_tau,
        theorem_bound,
    )


def main() -> None:
    families = [
        (
            "closure-20",
            list(POINTS[:20]),
            (20, 75, 190, 175, 3, 226, 6_708, 7_120, 30, 510_240),
        ),
        (
            "closure-40",
            list(POINTS[:40]),
            (40, 223, 780, 708, 5, 988, 58_516, 60_884, 72, 9_554_688),
        ),
        (
            "Costas-22",
            transformed_costas(23),
            (22, 131, 231, 168, 6, 457, 8_186, 12_350, 36, 863_424),
        ),
        (
            "parabola-43",
            transformed_parabola_43(),
            (
                43, 2_586, 903, 605, 21, 2_673, 64_944, 106_378,
                48, 8_481_600,
            ),
        ),
        (
            "ruler-40",
            ruler_points(),
            (
                40, 3_202, 780, 382, 210, 80_580, 44_412, 44_556,
                240, 184_665_600,
            ),
        ),
    ]

    for name, points, expected in families:
        actual = profile(points)
        assert actual == expected, (name, actual, expected)
        print(name, actual)

    print("corrected equal-area ambient gate: PASS")


if __name__ == "__main__":
    main()
