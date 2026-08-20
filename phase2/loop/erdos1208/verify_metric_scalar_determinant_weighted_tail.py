#!/usr/bin/env python3
"""Gaussian determinant cells and an aligned clean-codegree obstruction."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def norm(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def determinant(left: Point, right: Point) -> int:
    return left[0] * right[1] - left[1] * right[0]


def edge_data(points: list[Point]) -> tuple[dict[Point, int], dict[Point, Point]]:
    labels: dict[Point, int] = {}
    vectors: dict[Point, Point] = {}
    for first, second in combinations(points, 2):
        pair_sum = add(first, second)
        vector = subtract(first, second)
        assert pair_sum not in labels
        labels[pair_sum] = norm(vector)
        vectors[pair_sum] = vector
    assert len(labels) == len(set(labels.values()))
    return labels, vectors


def decorated_target_cells(points: list[Point]) -> Counter[tuple[int, int]]:
    labels, vectors = edge_data(points)
    cells: Counter[tuple[int, int]] = Counter()
    for first, first_vector in vectors.items():
        for second, second_vector in vectors.items():
            radius_gap = labels[first] - labels[second]
            doubled_area = 2 * determinant(first_vector, second_vector)

            alpha = subtract(first_vector, second_vector)
            beta = add(first_vector, second_vector)
            # (alpha_x+i alpha_y)(beta_x-i beta_y)=r-i d.
            gaussian_real = alpha[0] * beta[0] + alpha[1] * beta[1]
            gaussian_imaginary = alpha[1] * beta[0] - alpha[0] * beta[1]
            assert (gaussian_real, gaussian_imaginary) == (
                radius_gap,
                -doubled_area,
            )
            cells[radius_gap, doubled_area] += 1
    return cells


def maximum_nonzero_cell(points: list[Point]) -> tuple[int, Counter[int]]:
    cells = decorated_target_cells(points)
    nonzero = [
        multiplicity
        for cell, multiplicity in cells.items()
        if cell != (0, 0)
    ]
    return max(nonzero), Counter(nonzero)


def aligned_parabola_profile() -> tuple[object, ...]:
    points = transformed_parabola_43()
    labels, vectors = edge_data(points)
    codegrees: Counter[tuple[Point, Point]] = Counter()
    for starts in clean_start_fibres(points).values():
        codegrees.update(
            (first, second)
            for first in starts
            for second in starts
            if first != second
        )

    target_cells = decorated_target_cells(points)
    target_gaps: Counter[int] = Counter()
    for (radius_gap, _), multiplicity in target_cells.items():
        target_gaps[radius_gap] += multiplicity

    source_cells: Counter[tuple[int, int]] = Counter()
    source_pair_counts: Counter[tuple[int, int]] = Counter()
    source_codegrees: dict[tuple[int, int], list[int]] = {}
    temporary: dict[tuple[int, int], list[int]] = {}
    for (first, second), multiplicity in codegrees.items():
        radius_gap = labels[first] - labels[second]
        if radius_gap % 18:
            continue
        target_gap = -radius_gap // 18
        if target_gaps[target_gap] == 0:
            continue
        doubled_area = 2 * determinant(vectors[first], vectors[second])
        cell = (radius_gap, doubled_area)
        source_cells[cell] += multiplicity
        source_pair_counts[cell] += 1
        temporary.setdefault(cell, []).append(multiplicity)

    champion = max(source_cells, key=source_cells.get)
    source_codegrees = {
        cell: sorted(values, reverse=True)
        for cell, values in temporary.items()
    }
    radius_gap, doubled_area = champion
    target_gap = -radius_gap // 18
    target_area_cells = {
        area: multiplicity
        for (gap, area), multiplicity in target_cells.items()
        if gap == target_gap
    }
    return (
        champion,
        source_cells[champion],
        source_pair_counts[champion],
        tuple(source_codegrees[champion]),
        target_gap,
        target_gaps[target_gap],
        tuple(sorted(target_area_cells.items())),
        source_cells[champion] * target_gaps[target_gap],
    )


def main() -> None:
    expected_cells = {
        "closure-20": (3, Counter({1: 35_552, 2: 176, 3: 2})),
        "closure-40": (3, Counter({1: 604_356, 2: 1_620, 3: 8})),
        "Costas-22": (5, Counter({1: 51_672, 2: 666, 3: 28, 4: 8, 5: 2})),
        "parabola-43": (
            8,
            Counter({1: 798_956, 2: 7_120, 3: 328, 4: 58,
                     5: 8, 6: 4, 7: 2, 8: 2}),
        ),
        "ruler-40": (
            6,
            Counter({1: 598_818, 2: 3_706, 3: 382, 4: 48, 5: 8, 6: 2}),
        ),
    }
    families = [
        ("closure-20", POINTS[:20]),
        ("closure-40", POINTS[:40]),
        ("Costas-22", transformed_costas(23)),
        ("parabola-43", transformed_parabola_43()),
        ("ruler-40", ruler_points()),
    ]
    for name, points in families:
        actual = maximum_nonzero_cell(points)
        assert actual == expected_cells[name], (name, actual, expected_cells[name])
        print(name, actual)

    aligned = aligned_parabola_profile()
    assert aligned == (
        (189_216, -288),
        219,
        7,
        (60, 38, 37, 29, 25, 20, 10),
        -10_512,
        4,
        ((-716, 1), (16, 2), (1_020, 1)),
        876,
    ), aligned
    print("aligned parabola cell", aligned)
    print("metric scalar determinant weighted tail: PASS")


if __name__ == "__main__":
    main()
