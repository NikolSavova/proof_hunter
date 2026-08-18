#!/usr/bin/env python3
"""Exact finite checks for ORTHOGONAL_ENERGY_SUPPORT_GATE.md."""

from __future__ import annotations

from collections import Counter

from search_rotated_support import is_distance_sidon
from verify_orthogonal_two_support_gate import (
    add,
    dense_perpendicular_points,
    difference_set,
    rotate,
    translation_counts,
)
from verify_third_additive_energy_barrier import parabola, transform
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Matrix = tuple[tuple[int, int], tuple[int, int]]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def matrix_apply(matrix: Matrix, point: Point) -> Point:
    return (
        matrix[0][0] * point[0] + matrix[0][1] * point[1],
        matrix[1][0] * point[0] + matrix[1][1] * point[1],
    )


def common_energy(differences: set[Point]) -> int:
    counts = translation_counts(differences)
    return sum(
        count * counts.get(rotate(shift), 0)
        for shift, count in counts.items()
    )


def ordinary_support(differences: set[Point]) -> int:
    return len({
        add(first, second)
        for first in differences
        for second in differences
    })


def profile(points: list[Point]) -> tuple[int, int, int]:
    assert is_distance_sidon(points)
    differences = difference_set(points)
    return (
        len(differences),
        ordinary_support(differences),
        common_energy(differences),
    )


def verify_standard_profiles() -> None:
    expected = {
        20: (381, 16_097, 1_735_609),
        30: (871, 62_273, 16_135_769),
        40: (1_561, 156_057, 76_060_041),
    }
    for size, target in expected.items():
        actual = profile(POINTS[:size])
        assert actual == target
        number, support, energy = actual
        assert energy <= number * support
        print("closure", size, actual, "ratio", energy / (number * support))

    families = (
        (
            "parabola-31",
            transform(parabola(31)),
            (931, 9_779, 866_761),
        ),
        (
            "dense-perpendicular-40",
            dense_perpendicular_points(),
            (1_561, 431_225, 17_767_185),
        ),
    )
    for name, points, target in families:
        actual = profile(points)
        assert actual == target
        number, support, energy = actual
        assert energy <= number * support
        print(name, actual, "ratio", energy / (number * support))


def pair_sum_peak(points: list[Point]) -> tuple[Point, int]:
    pair_sums = {
        add(first, second)
        for index, first in enumerate(points)
        for second in points[index:]
    }
    counts = Counter(
        subtract(second, first)
        for first in pair_sums
        for second in pair_sums
    )
    value, shift = max(
        (count, shift)
        for shift, count in counts.items()
        if shift[0] == 0 and shift[1] != 0
    )
    return shift, value


def verify_two_parabola_peak() -> None:
    base = parabola(23)
    shift, peak = pair_sum_peak(base)
    assert (shift, peak) == ((0, 3), 67)

    first_matrix: Matrix = ((8, 33), (-17, 50))
    second_matrix: Matrix = ((19, -50), (-39, 33))
    translation = (-510_869_963_034_764_799_375_850,
                   -380_205_624_461_973_988_087_153)
    first = [matrix_apply(first_matrix, point) for point in base]
    second = [
        add(matrix_apply(second_matrix, point), translation)
        for point in base
    ]
    points = first + second
    assert len(points) == 46
    assert is_distance_sidon(points)

    differences = difference_set(points)
    assert len(differences) == 2_071
    counts = translation_counts(differences)
    image = matrix_apply(first_matrix, shift)
    assert image == (99, 150)
    assert rotate(image) == (-150, 99)
    assert counts[image] == counts[rotate(image)] == 252
    assert counts[image] * counts[rotate(image)] == 63_504

    support = ordinary_support(differences)
    energy = sum(
        count * counts.get(rotate(delta), 0)
        for delta, count in counts.items()
    )
    assert support == 608_903
    assert energy == 7_263_825
    assert energy <= len(differences) * support
    print(
        "two-parabola peak",
        "points", len(points),
        "N", len(differences),
        "peak", (counts[image], counts[rotate(image)]),
        "support", support,
        "energy", energy,
        "ratio", energy / (len(differences) * support),
    )


def main() -> None:
    verify_standard_profiles()
    verify_two_parabola_peak()
    print("orthogonal energy-support gate: PASS")


if __name__ == "__main__":
    main()
