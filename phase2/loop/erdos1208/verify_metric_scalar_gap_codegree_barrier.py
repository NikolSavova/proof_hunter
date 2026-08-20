#!/usr/bin/env python3
"""Exact gap-multiplicity barrier and weighted codegree profiles."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_metric_scalar_target_c4_barrier import Q_VALUE, ROWS
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Profile = tuple[int, ...]


def squared_distance(first: Point, second: Point) -> int:
    return (first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2


def labels(points: list[Point]) -> dict[Point, int]:
    output: dict[Point, int] = {}
    for first, second in combinations(points, 2):
        pair_sum = (first[0] + second[0], first[1] + second[1])
        assert pair_sum not in output
        output[pair_sum] = squared_distance(first, second)
    assert len(output) == len(set(output.values()))
    return output


def perpendicular_gap_family(length: int, base: int = 11) -> tuple[list[Point], int, int]:
    """An exact member of the infinite R_D(r)=Theta(k^2) family."""
    exponent = 2 * length + 1
    gap = base**exponent
    horizontal: list[int] = []
    for index in range(length):
        high = base ** (exponent - index)
        low = base**index
        horizontal.extend(((high + low) // 2, (high - low) // 2))

    horizontal_differences = {
        abs(first - second) for first, second in combinations(horizontal, 2)
    }
    assert len(horizontal_differences) == len(horizontal) * (len(horizontal) - 1) // 2
    assert all(
        horizontal[2 * index] ** 2 - horizontal[2 * index + 1] ** 2 == gap
        for index in range(length)
    )

    vertical_base = [2**index for index in range(2 * length)]
    vertical_base_differences = {
        abs(first - second) for first, second in combinations(vertical_base, 2)
    }
    assert len(vertical_base_differences) == len(vertical_base) * (len(vertical_base) - 1) // 2
    scale = 1
    while any(
        scale * difference in horizontal_differences
        for difference in vertical_base_differences
    ):
        scale += 1
    vertical = [scale * value for value in vertical_base]

    offset = 3 * max(horizontal)
    while True:
        points = (
            [(value, 0) for value in horizontal]
            + [(0, offset + value) for value in vertical]
        )
        distances = [
            squared_distance(first, second)
            for first, second in combinations(points, 2)
        ]
        if len(distances) == len(set(distances)):
            break
        offset += 1

    assert scale == 2
    assert not clean_start_fibres(points)
    distance_set = set(distances)
    gap_load = sum(value - gap in distance_set for value in distances)
    assert gap_load == 2 * length * length
    return points, gap, gap_load


def weighted_profile(points: list[Point]) -> Profile:
    edge_labels = labels(points)
    distance_values = list(edge_labels.values())
    gap_loads = Counter(
        first - second
        for first in distance_values
        for second in distance_values
    )
    fibres = clean_start_fibres(points)
    source_gap_loads: Counter[int] = Counter()
    for starts in fibres.values():
        values = [edge_labels[start] for start in starts]
        source_gap_loads.update(first - second for first in values for second in values)

    contributions = {
        gap: load * source_gap_loads[-18 * gap]
        for gap, load in gap_loads.items()
        if gap and source_gap_loads[-18 * gap]
    }
    maximum_gap_load = max(
        (load for gap, load in gap_loads.items() if gap),
        default=0,
    )
    maximum_contribution = max(contributions.values(), default=0)
    maximizing_gap = max(contributions, key=contributions.get, default=0)
    total_h = sum(map(len, fibres.values()))
    off_diagonal = sum(contributions.values())
    return (
        len(points),
        len(edge_labels),
        total_h,
        maximum_gap_load,
        len(contributions),
        off_diagonal,
        maximum_contribution,
        gap_loads[maximizing_gap],
        source_gap_loads[-18 * maximizing_gap],
    )


def main() -> None:
    gap_expected = {
        2: (8, 28, 8),
        4: (16, 120, 32),
        8: (32, 496, 128),
        16: (64, 2_016, 512),
    }
    for length, expected in gap_expected.items():
        points, gap, load = perpendicular_gap_family(length)
        actual = (len(points), len(points) * (len(points) - 1) // 2, load)
        assert actual == expected, (length, actual, expected)
        assert gap == 11 ** (2 * length + 1)
        print("gap family", length, actual, "gap", gap)

    scalar_barrier = [(0, 0), Q_VALUE] + [point for row in ROWS for point in row]
    expected_profiles = {
        "closure-40": (40, 780, 12_420, 100, 2_300,
                       347_362, 1_988, 71, 28),
        "Costas-22": (22, 231, 9_342, 19, 1_296,
                      72_622, 686, 14, 49),
        "parabola-43": (43, 903, 190_278, 11, 27_218,
                        2_143_322, 2_637, 9, 293),
        "ruler-40": (40, 780, 4_914, 24, 980,
                     2_188, 25, 5, 5),
        "scalar-barrier-74": (74, 2_701, 252, 2, 114,
                              172, 4, 2, 2),
    }
    families = [
        ("closure-40", POINTS[:40]),
        ("Costas-22", transformed_costas(23)),
        ("parabola-43", transformed_parabola_43()),
        ("ruler-40", ruler_points()),
        ("scalar-barrier-74", scalar_barrier),
    ]
    for name, points in families:
        actual = weighted_profile(points)
        assert actual == expected_profiles[name], (name, actual, expected_profiles[name])
        print(name, actual)

    print("metric scalar gap-codegree barrier: PASS")


if __name__ == "__main__":
    main()
