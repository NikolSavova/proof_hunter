#!/usr/bin/env python3
"""Exact checks for TWO_SCALE_DISTANCE_GAP_CORRELATION_NO_GO.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points
from verify_dilated_internal_pair_sum_charge import transformed_parabola_43
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Edge = tuple[int, Point]


def squared_distance(first: Point, second: Point) -> int:
    x_value = first[0] - second[0]
    y_value = first[1] - second[1]
    return x_value * x_value + y_value * y_value


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def edge_data(points: list[Point]) -> list[Edge]:
    edges = []
    for first, second in combinations(points, 2):
        vector = (first[0] - second[0], first[1] - second[1])
        edges.append((squared_distance(first, second), vector))
    assert len({distance for distance, _ in edges}) == len(edges)
    return edges


def gap_loads(distances: list[int]) -> Counter[int]:
    return Counter(
        first - second
        for first in distances
        for second in distances
    )


def correlation(loads: Counter[int]) -> int:
    return sum(load * loads[-18 * gap] for gap, load in loads.items())


def scalar_energy(distances: list[int]) -> tuple[int, int]:
    loads = Counter(
        first + 18 * second
        for first in distances
        for second in distances
    )
    return sum(load * load for load in loads.values()), len(loads)


def raw_profile(points: list[Point]) -> tuple[int, int, int, int, int, int]:
    edges = edge_data(points)
    distances = [distance for distance, _ in edges]
    loads = gap_loads(distances)
    energy = correlation(loads)
    off_diagonal = energy - len(edges) ** 2
    aligned = [
        (gap, load * loads[-18 * gap])
        for gap, load in loads.items()
        if gap and loads[-18 * gap]
    ]
    return (
        len(points),
        len(edges),
        energy,
        off_diagonal,
        len(aligned),
        max(product for _, product in aligned),
    )


def verify_charge_identity_and_range(points: list[Point]) -> None:
    edges = edge_data(points)
    distances = [distance for distance, _ in edges]
    loads = gap_loads(distances)
    charge_energy, support = scalar_energy(distances)
    assert charge_energy == correlation(loads)

    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    side = max(max(x_values) - min(x_values), max(y_values) - min(y_values))
    number = len(distances)
    assert max(distances) <= 2 * side * side
    assert support <= 38 * side * side + 1
    assert charge_energy * support >= number ** 4
    assert charge_energy * (38 * side * side + 1) >= number ** 4


def decorated_cells(edges: list[Edge]) -> Counter[tuple[int, int]]:
    output: Counter[tuple[int, int]] = Counter()
    for first_distance, first_vector in edges:
        for second_distance, second_vector in edges:
            gap = first_distance - second_distance
            area = 2 * determinant(first_vector, second_vector)

            alpha = (
                first_vector[0] - second_vector[0],
                first_vector[1] - second_vector[1],
            )
            beta = (
                first_vector[0] + second_vector[0],
                first_vector[1] + second_vector[1],
            )
            gaussian_real = alpha[0] * beta[0] + alpha[1] * beta[1]
            gaussian_imaginary = alpha[1] * beta[0] - alpha[0] * beta[1]
            assert (gaussian_real, gaussian_imaginary) == (gap, -area)
            output[gap, area] += 1
    return output


def verify_determinant_truncation(points: list[Point]) -> None:
    edges = edge_data(points)
    number = len(edges)
    raw = gap_loads([distance for distance, _ in edges])
    cells = decorated_cells(edges)
    maximum_cell = max(
        load for (gap, _), load in cells.items() if gap != 0
    )
    off_diagonal = correlation(raw) - number * number

    for cutoff in (0, number // len(points), number):
        high = Counter()
        for (gap, area), load in cells.items():
            if gap and abs(area) > cutoff:
                high[gap] += load

        low_bound = (2 * cutoff + 1) * maximum_cell
        for gap, load in raw.items():
            if gap:
                assert load <= high[gap] + low_bound

        weighted = sum(
            load * raw[-18 * gap]
            for gap, load in high.items()
        )
        assert weighted >= off_diagonal - low_bound * number * number

        for threshold in (1, len(points), number):
            rich_weighted = sum(
                load * raw[-18 * gap]
                for gap, load in high.items()
                if load >= threshold
            )
            assert rich_weighted >= (
                off_diagonal
                - (low_bound + threshold) * number * number
            )

            rich_unweighted = sum(
                raw[-18 * gap]
                for gap, load in high.items()
                if load >= threshold
            )
            assert number * rich_unweighted >= rich_weighted


def main() -> None:
    families = [
        (
            "closure-20",
            list(POINTS[:20]),
            (20, 190, 77_246, 41_146, 406, 726),
        ),
        (
            "closure-40",
            list(POINTS[:40]),
            (40, 780, 2_346_900, 1_738_500, 4_204, 6_177),
        ),
        (
            "Costas-22",
            transformed_costas(23),
            (22, 231, 73_247, 19_886, 1_390, 168),
        ),
        (
            "parabola-43",
            transformed_parabola_43(),
            (43, 903, 897_791, 82_382, 27_518, 54),
        ),
        (
            "ruler-40",
            ruler_points(),
            (40, 780, 624_164, 15_764, 7_328, 84),
        ),
    ]

    for name, points, expected in families:
        actual = raw_profile(points)
        assert actual == expected, (name, actual, expected)
        print(name, actual)

    verify_charge_identity_and_range(list(POINTS[:20]))
    verify_determinant_truncation(list(POINTS[:20]))
    verify_determinant_truncation(transformed_costas(23))
    print("two-scale distance-gap correlation no-go: PASS")


if __name__ == "__main__":
    main()
