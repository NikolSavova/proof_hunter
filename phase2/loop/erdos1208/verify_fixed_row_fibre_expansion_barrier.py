#!/usr/bin/env python3
"""Exact checks for FIXED_ROW_FIBRE_EXPANSION_BARRIER.md."""

from __future__ import annotations

import random

from search_rotated_support import is_distance_sidon


Point = tuple[int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def negate(point: Point) -> Point:
    return -point[0], -point[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def norm(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def radial_representatives(side: int) -> list[Point]:
    """One first-quadrant representative of each positive norm <= side^2."""
    representatives: dict[int, Point] = {}
    for x in range(side + 1):
        for y in range(side + 1):
            value = x * x + y * y
            if 0 < value <= side * side and value not in representatives:
                representatives[value] = (x, y)
    return [representatives[value] for value in sorted(representatives)]


def vector_model(side: int) -> tuple[list[Point], list[Point], Point]:
    intended = radial_representatives(side)
    base = 2 * side + 1
    scale = 2 * side * side + 1
    target = scale, base * scale
    partners = [rotate(subtract(point, target)) for point in intended]
    vectors = intended + partners
    assert len(set(vectors)) == len(vectors)
    assert len({norm(vector) for vector in vectors}) == len(vectors)
    return intended, vectors, target


def partner(vector: Point, target: Point) -> Point:
    """The unique g satisfying vector + Jg = target."""
    return negate(rotate(subtract(target, vector)))


def internal_fibre(vectors: list[Point], target: Point) -> set[Point]:
    oriented = set(vectors) | {negate(vector) for vector in vectors}
    return {vector for vector in oriented if partner(vector, target) in oriented}


def orthogonal_support(fibre: set[Point]) -> set[Point]:
    return {
        subtract(first, rotate(second))
        for first in fibre
        for second in fibre
    }


def verify_vector_profiles() -> None:
    expected = {
        6: (18, 18, 72),
        8: (29, 29, 123),
        10: (43, 43, 203),
        20: (145, 145, 818),
        40: (504, 504, 3_280),
        60: (1_063, 1_063, 7_381),
        80: (1_811, 1_811, 13_199),
        100: (2_749, 2_749, 20_633),
    }
    for side, target_profile in expected.items():
        intended, vectors, target = vector_model(side)
        fibre = internal_fibre(vectors, target)
        support = orthogonal_support(fibre)
        assert set(intended) <= fibre
        actual = len(intended), len(fibre), len(support)
        assert actual == target_profile
        print("vector profile", side, actual)


def generic_segment_instance(side: int, seed: int) -> tuple[list[Point], Point]:
    _, vectors, target = vector_model(side)
    generator = random.Random(seed)
    points: list[Point] = []
    occupied: set[Point] = set()
    for vector in vectors:
        while True:
            translation = (
                generator.randrange(-(1 << 100), 1 << 100),
                generator.randrange(-(1 << 100), 1 << 100),
            )
            other = subtract(translation, vector)
            if translation not in occupied and other not in occupied:
                break
        occupied.add(translation)
        occupied.add(other)
        points.extend((translation, other))
    return points, target


def verify_concrete_instance() -> None:
    points, target = generic_segment_instance(8, 1_208)
    assert len(points) == 116
    assert is_distance_sidon(points)
    differences = {
        subtract(first, second)
        for first in points
        for second in points
    }
    assert len(differences) == 13_341
    fibre = {vector for vector in differences if partner(vector, target) in differences}
    support = orthogonal_support(fibre)
    intended, vectors, _ = vector_model(8)
    assert fibre == internal_fibre(vectors, target) == set(intended)
    assert len(fibre) == 29
    assert len(support) == 123
    print(
        "concrete instance",
        "points", len(points),
        "differences", len(differences),
        "fibre", len(fibre),
        "support", len(support),
    )


def verify_coefficient_rule() -> None:
    identity = ((1, 0), (0, 1))
    quarter_turn = ((0, -1), (1, 0))
    for first in (-1, 0, 1):
        for second in (-1, 0, 1):
            matrix = tuple(
                tuple(
                    first * identity[row][column]
                    + second * quarter_turn[row][column]
                    for column in range(2)
                )
                for row in range(2)
            )
            assert (matrix == ((0, 0), (0, 0))) == (first == second == 0)
    print("row coefficient rule: PASS")


def main() -> None:
    verify_coefficient_rule()
    verify_vector_profiles()
    verify_concrete_instance()
    print("fixed-row fibre-expansion barrier: PASS")


if __name__ == "__main__":
    main()
