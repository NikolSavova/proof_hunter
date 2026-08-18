#!/usr/bin/env python3
"""Exact checks for ORTHOGONAL_TWO_SUPPORT_GATE.md."""

from __future__ import annotations

from collections import Counter

from search_rotated_support import is_distance_sidon
from verify_third_additive_energy_barrier import parabola, transform
from verify_transverse_closure_witness import POINTS as CLOSURE_POINTS


Point = tuple[int, int]


def difference_set(points: list[Point]) -> set[Point]:
    return {
        (first[0] - second[0], first[1] - second[1])
        for first in points
        for second in points
    }


def add(first: Point, second: Point) -> Point:
    return first[0] + second[0], first[1] + second[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def translation_counts(differences: set[Point]) -> Counter[Point]:
    return Counter(
        (second[0] - first[0], second[1] - first[1])
        for first in differences
        for second in differences
    )


def profile(points: list[Point]) -> tuple[int, int, int, int]:
    assert is_distance_sidon(points)
    differences = difference_set(points)
    ordinary = {add(first, second) for first in differences for second in differences}
    rotated = {
        add(first, rotate(second))
        for first in differences
        for second in differences
    }
    counts = translation_counts(differences)
    mixed_third = sum(
        count * count * counts[rotate(shift)]
        for shift, count in counts.items()
    )
    return len(differences), len(ordinary), len(rotated), mixed_third


def maximum_fibre_profile(points: list[Point]) -> tuple[int, int]:
    """Return max r_t and |E_t-JE_t| for one maximizing fixed-row fibre."""
    differences = difference_set(points)
    rotated_differences = {rotate(point) for point in differences}
    representations = Counter(
        add(first, second)
        for first in differences
        for second in rotated_differences
    )
    target, maximum = representations.most_common(1)[0]
    fibre = {
        point
        for point in differences
        if (target[0] - point[0], target[1] - point[1]) in rotated_differences
    }
    assert len(fibre) == maximum
    internal_support = {
        (first[0] - rotate(second)[0], first[1] - rotate(second)[1])
        for first in fibre
        for second in fibre
    }
    return maximum, len(internal_support)


def verify_fibre_identity() -> None:
    points = CLOSURE_POINTS[:8]
    differences = difference_set(points)
    fibres: Counter[tuple[Point, Point]] = Counter()
    for first in differences:
        for second in differences:
            ordinary = add(first, second)
            for third in differences:
                mixed = add(first, rotate(third))
                fibres[ordinary, mixed] += 1

    counts = translation_counts(differences)
    mixed_third = sum(
        count * count * counts[rotate(shift)]
        for shift, count in counts.items()
    )
    assert len(differences) == 57
    assert sum(fibres.values()) == 57**3 == 185_193
    assert sum(value * value for value in fibres.values()) == mixed_third
    assert mixed_third == 201_297
    assert len(fibres) == 177_873
    assert max(fibres.values()) == 6
    print("fibre identity", len(differences), mixed_third, len(fibres), 6)


def erdos_turan(prime: int) -> list[int]:
    return [2 * prime * index + (index * index % prime) for index in range(prime)]


def dense_perpendicular_points() -> list[Point]:
    marks = erdos_turan(41)[:40]
    first, second = marks[:20], marks[20:]
    points = [(mark, 0) for mark in first] + [(0, mark) for mark in second]
    assert len(points) == 40
    return points


def main() -> None:
    verify_fibre_identity()

    families = [
        (
            "closure-20",
            CLOSURE_POINTS[:20],
            (381, 16_097, 24_305, 90_168_653),
            (56, 2_303),
        ),
        (
            "parabola-31",
            transform(parabola(31)),
            (931, 9_779, 866_761, 806_954_491),
            (1, 1),
        ),
        (
            "dense-perpendicular-40",
            dense_perpendicular_points(),
            (1_561, 431_225, 1_413_381, 4_794_246_337),
            (97, 9_409),
        ),
    ]

    for name, points, expected, expected_fibre in families:
        actual = profile(points)
        assert actual == expected
        actual_fibre = maximum_fibre_profile(points)
        assert actual_fibre == expected_fibre
        size, ordinary, rotated, mixed_third = actual
        product = ordinary * rotated
        assert product >= size**3
        print(
            name,
            "N", size,
            "ordinary", ordinary,
            "rotated", rotated,
            "mixed-third", mixed_third,
            "product", product,
            "max-fibre", actual_fibre[0],
            "internal-support", actual_fibre[1],
        )

    print("orthogonal two-support gate: PASS")


if __name__ == "__main__":
    main()
