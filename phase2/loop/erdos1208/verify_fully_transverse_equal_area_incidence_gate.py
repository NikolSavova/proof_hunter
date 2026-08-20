#!/usr/bin/env python3
"""Exact checks for FULLY_TRANSVERSE_EQUAL_AREA_INCIDENCE_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import gcd, isqrt

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Direction = tuple[int, int]
Triangle = tuple[int, int, int]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def squared_norm(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def canonical_direction(vector: Point) -> tuple[Direction, int]:
    divisor = gcd(abs(vector[0]), abs(vector[1]))
    assert divisor
    direction = (vector[0] // divisor, vector[1] // divisor)
    coefficient = divisor
    if direction[0] < 0 or (direction[0] == 0 and direction[1] < 0):
        direction = (-direction[0], -direction[1])
        coefficient = -coefficient
    return direction, coefficient


def doubled_area(points: list[Point], triangle: Triangle) -> int:
    first, second, third = (points[index] for index in triangle)
    return determinant(subtract(second, first), subtract(third, first))


def edge_vector(points: list[Point], first: int, second: int) -> Point:
    return subtract(points[second], points[first])


def side_directions(points: list[Point], triangle: Triangle) -> frozenset[Direction]:
    output = frozenset(
        canonical_direction(edge_vector(points, triangle[index], triangle[(index + 1) % 3]))[0]
        for index in range(3)
    )
    assert len(output) == 3
    return output


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


def signed_area_loads(points: list[Point]) -> Counter[int]:
    return Counter(
        area
        for triangle in permutations(range(len(points)), 3)
        if (area := doubled_area(points, triangle)) != 0
    )


def top_line_profile(points: list[Point], area: int) -> tuple[int, int, int]:
    """Return weighted incidences, distinct incident lines, max multiplicity."""

    lines: Counter[tuple[Direction, Fraction]] = Counter()
    for first_index, first in enumerate(points):
        for second_index, second in enumerate(points):
            if first_index == second_index:
                continue
            direction, coefficient = canonical_direction(subtract(second, first))
            sigma = determinant(direction, first)
            coordinate = Fraction(area, coefficient) + sigma
            if any(determinant(direction, point) == coordinate for point in points):
                lines[direction, coordinate] += 1

    maximum = max(lines.values(), default=0)
    assert maximum <= 2 * divisor_count(area)
    weighted_incidences = sum(
        multiplicity
        * sum(determinant(direction, point) == coordinate for point in points)
        for (direction, coordinate), multiplicity in lines.items()
    )
    return weighted_incidences, len(lines), maximum


def fixed_area_profile(points: list[Point]) -> tuple[int, int, int, int]:
    assert distance_sidon(points)
    loads = signed_area_loads(points)
    champion_area = max(loads, key=loads.get)
    incidence_load, distinct_lines, maximum = top_line_profile(
        points, champion_area
    )
    assert incidence_load == loads[champion_area]
    return champion_area, incidence_load, distinct_lines, maximum


def geometric_energy_profile(points: list[Point]) -> tuple[int, int, int]:
    buckets: dict[int, list[tuple[frozenset[int], frozenset[Direction]]]] = defaultdict(list)
    for triangle in combinations(range(len(points)), 3):
        area = abs(doubled_area(points, triangle))
        if area:
            buckets[area].append((
                frozenset(triangle),
                side_directions(points, triangle),
            ))

    disjoint_pairs = 0
    fully_transverse_pairs = 0
    cross_parallel_pairs = 0
    for triangles in buckets.values():
        for first_vertices, first_directions in triangles:
            for second_vertices, second_directions in triangles:
                if not first_vertices.isdisjoint(second_vertices):
                    continue
                disjoint_pairs += 1
                if first_directions.isdisjoint(second_directions):
                    fully_transverse_pairs += 1
                else:
                    cross_parallel_pairs += 1

    assert disjoint_pairs == fully_transverse_pairs + cross_parallel_pairs
    return (
        18 * disjoint_pairs,
        18 * fully_transverse_pairs,
        18 * cross_parallel_pairs,
    )


def corresponding_parallel_count(points: list[Point]) -> int:
    """Six-distinct equal-signed ordered pairs with a parallel side slot."""

    buckets: dict[int, list[Triangle]] = defaultdict(list)
    for triangle in permutations(range(len(points)), 3):
        area = doubled_area(points, triangle)
        if area:
            buckets[area].append(triangle)

    output = 0
    for triangles in buckets.values():
        for first in triangles:
            first_vertices = set(first)
            first_edges = [
                edge_vector(points, first[index], first[(index + 1) % 3])
                for index in range(3)
            ]
            for second in triangles:
                if not first_vertices.isdisjoint(second):
                    continue
                second_edges = [
                    edge_vector(points, second[index], second[(index + 1) % 3])
                    for index in range(3)
                ]
                if any(
                    determinant(first_edge, second_edge) == 0
                    for first_edge, second_edge in zip(first_edges, second_edges)
                ):
                    output += 1
    return output


def verify_cross_determinants(points: list[Point]) -> None:
    triangles = [
        triangle
        for triangle in permutations(range(len(points)), 3)
        if doubled_area(points, triangle) != 0
    ]
    witness = None
    for first in triangles:
        first_vertices = set(first)
        area = doubled_area(points, first)
        for second in triangles:
            if doubled_area(points, second) != area:
                continue
            if not first_vertices.isdisjoint(second):
                continue
            first_edges = [
                edge_vector(points, first[index], first[(index + 1) % 3])
                for index in range(3)
            ]
            second_edges = [
                edge_vector(points, second[index], second[(index + 1) % 3])
                for index in range(3)
            ]
            matrix = [
                [determinant(left, right) for right in second_edges]
                for left in first_edges
            ]
            if all(value for row in matrix for value in row):
                witness = area, first_edges, second_edges, matrix
                break
        if witness:
            break

    assert witness is not None
    area, first_edges, second_edges, matrix = witness
    assert tuple(map(sum, matrix)) == (0, 0, 0)
    assert tuple(sum(matrix[row][column] for row in range(3)) for column in range(3)) == (0, 0, 0)
    assert matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] == area * area
    assert tuple(sum(edge[index] for edge in first_edges) for index in range(2)) == (0, 0)
    assert tuple(sum(edge[index] for edge in second_edges) for index in range(2)) == (0, 0)


def main() -> None:
    expected_energy = {
        20: (15_516, 15_372, 144),
        40: (258_624, 256_824, 1_800),
        80: (2_588_364, 2_582_208, 6_156),
        120: (9_058_968, 9_048_816, 10_152),
    }
    for size, expected in expected_energy.items():
        actual = geometric_energy_profile(list(POINTS[:size]))
        assert actual == expected, (size, actual, expected)
        print(f"closure-{size}", actual)

    # The exact cyclic factor-three inequality is checked where direct
    # ordered enumeration is inexpensive.
    for size in (20, 40):
        points = list(POINTS[:size])
        _, _, cross_parallel = geometric_energy_profile(points)
        corresponding = corresponding_parallel_count(points)
        assert cross_parallel <= 3 * corresponding
        print(f"cyclic-{size}", cross_parallel, corresponding)

    fixed_profiles = [
        (
            "closure-20",
            list(POINTS[:20]),
            (18, 24, 23, 1),
        ),
        (
            "Costas-22",
            transformed_costas(23),
            (-1_012, 72, 65, 2),
        ),
    ]
    for name, points, expected in fixed_profiles:
        actual = fixed_area_profile(points)
        assert actual == expected, (name, actual, expected)
        print(name, actual)

    verify_cross_determinants(list(POINTS[:20]))
    print("fully transverse equal-area incidence gate: PASS")


if __name__ == "__main__":
    main()
