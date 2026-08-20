#!/usr/bin/env python3
"""Checks for GLOBAL_DIRECTIONAL_SHORT_COMPENSATOR_NO_GO.md."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import gcd
import sys

sys.path.insert(0, "phase2/loop/erdos1208")

from verify_ambient_centroid_endpoint_difference_hypergraph_gate import (  # noqa: E402
    direction_occupancies,
    is_distance_sidon,
    norm2,
    residue_parabola,
    sub,
    triple_loads,
)

Point = tuple[int, int]


def balanced_transform(points: list[Point], parameter: int) -> list[Point]:
    return [
        (
            parameter * x - y,
            x + (parameter + 1) * y,
        )
        for x, y in points
    ]


def coordinate_height(points: list[Point]) -> int:
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    return max(max(xs) - min(xs), max(ys) - min(ys))


def collision_signature(vector: Point) -> tuple[int, int, int]:
    x, y = vector
    return (
        x * x + y * y,
        y * y,
        x * x + 2 * x * y + 2 * y * y,
    )


def assert_symbolic_separation(points: list[Point]) -> None:
    signatures: dict[tuple[int, int, int], Point] = {}
    for first, second in combinations(range(len(points)), 2):
        vector = sub(points[second], points[first])
        signature = collision_signature(vector)
        assert signature not in signatures
        signatures[signature] = vector


def global_profile(prime: int, parameter: int) -> tuple[int, int, int, Fraction, int]:
    base = residue_parabola(prime)
    points = balanced_transform(base, parameter)
    assert_symbolic_separation(base)
    assert is_distance_sidon(points)

    base_occupancies = direction_occupancies(base)
    transformed_occupancies = direction_occupancies(points)
    assert sorted(base_occupancies.values()) == sorted(
        transformed_occupancies.values()
    )

    determinant = parameter * parameter + parameter + 1
    maximum_content = 0
    for direction in base_occupancies:
        a, b = direction
        image = (
            parameter * a - b,
            a + (parameter + 1) * b,
        )
        content = gcd(abs(image[0]), abs(image[1]))
        eisenstein_norm = a * a + a * b + b * b
        assert determinant % content == 0
        assert eisenstein_norm % content == 0
        maximum_content = max(maximum_content, content)

    height = coordinate_height(points)
    k = len(points)
    directional_budget = sum(
        Fraction(k * occupancy)
        + Fraction(
            height * height,
            max(abs(direction[0]), abs(direction[1])) ** 2,
        )
        for direction, occupancy in transformed_occupancies.items()
    )

    ordered_triple_pairs = sum(
        load * (load - 1) for load in triple_loads(points).values()
    )
    hyperedges = 6 * ordered_triple_pairs
    directional_mass = 3 * hyperedges
    return (
        height,
        hyperedges,
        directional_mass,
        directional_budget,
        maximum_content,
    )


def main() -> None:
    expected = {
        23: (20, 439, 8_652, 25_956, 2.8328285402696567),
        43: (69, 2_897, 126_852, 380_556, 7.04597190565827),
        59: (99, 5_741, 496_968, 1_490_904, 11.241571817342443),
    }

    for prime, (
        parameter,
        expected_height,
        expected_hyperedges,
        expected_mass,
        expected_ratio,
    ) in expected.items():
        height, hyperedges, mass, budget, maximum_content = global_profile(
            prime, parameter
        )
        assert height == expected_height
        assert hyperedges == expected_hyperedges
        assert mass == expected_mass
        assert maximum_content == 1
        assert abs(float(Fraction(mass, 1) / budget) - expected_ratio) < 1e-12

    _, _, mass, budget, _ = global_profile(43, 69)
    assert mass > 7 * budget

    print("global directional short compensator no-go: PASS")
    print(
        "balanced lifts:",
        {
            prime: round(expected[prime][4], 6)
            for prime in expected
        },
    )


if __name__ == "__main__":
    main()
