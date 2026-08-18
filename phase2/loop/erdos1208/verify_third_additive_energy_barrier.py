#!/usr/bin/env python3
"""Exact certificate for THIRD_ADDITIVE_ENERGY_BARRIER.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations


P = 127
MATRIX = (-93, -83, 66, -1)
EXPECTED_TRIPLE_SUPPORT = 81_221
EXPECTED_THIRD_ENERGY = 86_658_955
EXPECTED_MAX_REPRESENTATION = 168


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def parabola(prime: int) -> list[tuple[int, int]]:
    return [(x, x * x % prime) for x in range(prime)]


def transform(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    a, b, c, d = MATRIX
    return [(a * x + b * y, c * x + d * y) for x, y in points]


def squared_distance(first: tuple[int, int], second: tuple[int, int]) -> int:
    dx = first[0] - second[0]
    dy = first[1] - second[1]
    return dx * dx + dy * dy


def verify_vector_sidon(points: list[tuple[int, int]]) -> None:
    differences: dict[tuple[int, int], tuple[int, int]] = {}
    for first in range(len(points)):
        for second in range(len(points)):
            if first == second:
                continue
            difference = (
                points[first][0] - points[second][0],
                points[first][1] - points[second][1],
            )
            assert difference not in differences
            differences[difference] = (first, second)
    assert len(differences) == P * (P - 1)


def verify_distance_sidon(points: list[tuple[int, int]]) -> None:
    distances: dict[int, tuple[int, int]] = {}
    for first, second in combinations(range(len(points)), 2):
        distance = squared_distance(points[first], points[second])
        assert distance > 0
        assert distance not in distances
        distances[distance] = (first, second)
    assert len(distances) == P * (P - 1) // 2
    print("unordered distances", len(distances))


def verify_general_position(points: list[tuple[int, int]]) -> None:
    for first, second, third in combinations(points, 3):
        area_twice = (
            (second[0] - first[0]) * (third[1] - first[1])
            - (second[1] - first[1]) * (third[0] - first[0])
        )
        assert area_twice != 0
    print("maximum collinearity", 2)


def verify_third_energy(points: list[tuple[int, int]]) -> None:
    representations: Counter[tuple[int, int]] = Counter()
    for first in points:
        for second in points:
            for third in points:
                representations[
                    (
                        first[0] + second[0] + third[0],
                        first[1] + second[1] + third[1],
                    )
                ] += 1
    support = len(representations)
    energy = sum(value * value for value in representations.values())
    maximum = max(representations.values())
    assert support == EXPECTED_TRIPLE_SUPPORT
    assert support <= 9 * P * P
    assert energy == EXPECTED_THIRD_ENERGY
    assert energy * 9 >= P**4
    assert maximum == EXPECTED_MAX_REPRESENTATION
    print("triple support", support)
    print("third energy", energy)
    print("third energy / k^4", energy / P**4)
    print("maximum triple-sum representation", maximum)


def main() -> None:
    assert is_prime(P)
    a, b, c, d = MATRIX
    assert a * d - b * c == 5_571
    base = parabola(P)
    verify_vector_sidon(base)
    points = transform(base)
    assert len(set(points)) == P
    verify_distance_sidon(points)
    verify_general_position(points)
    verify_third_energy(points)
    print("all exact third-additive-energy barrier checks passed")


if __name__ == "__main__":
    main()
