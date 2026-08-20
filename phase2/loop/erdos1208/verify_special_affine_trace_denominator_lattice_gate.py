#!/usr/bin/env python3
"""Exact checks for SPECIAL_AFFINE_TRACE_DENOMINATOR_LATTICE_GATE.md."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import gcd

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Matrix = tuple[Fraction, Fraction, Fraction, Fraction]
AffineMap = tuple[Matrix, tuple[Fraction, Fraction]]
Triangle = tuple[int, int, int]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def doubled_area(points: list[Point], triangle: Triangle) -> int:
    first, second, third = (points[index] for index in triangle)
    return determinant(subtract(second, first), subtract(third, first))


def edge_vectors(points: list[Point], triangle: Triangle) -> list[Point]:
    return [
        subtract(points[triangle[(index + 1) % 3]], points[triangle[index]])
        for index in range(3)
    ]


def matrix_apply(matrix: Matrix, point: Point) -> tuple[Fraction, Fraction]:
    first, second, third, fourth = matrix
    return (
        first * point[0] + second * point[1],
        third * point[0] + fourth * point[1],
    )


def affine_apply(mapping: AffineMap, point: Point) -> tuple[Fraction, Fraction]:
    image = matrix_apply(mapping[0], point)
    return image[0] + mapping[1][0], image[1] + mapping[1][1]


def triangle_map(
    points: list[Point], source: Triangle, target: Triangle
) -> AffineMap:
    source_first, source_second, source_third = (
        points[index] for index in source
    )
    target_first, target_second, target_third = (
        points[index] for index in target
    )
    u_value = subtract(source_second, source_first)
    v_value = subtract(source_third, source_first)
    u_prime = subtract(target_second, target_first)
    v_prime = subtract(target_third, target_first)
    area = determinant(u_value, v_value)
    assert area and determinant(u_prime, v_prime) == area

    # [u' v'] [u v]^{-1}
    matrix = (
        Fraction(u_prime[0] * v_value[1] - v_prime[0] * u_value[1], area),
        Fraction(-u_prime[0] * v_value[0] + v_prime[0] * u_value[0], area),
        Fraction(u_prime[1] * v_value[1] - v_prime[1] * u_value[1], area),
        Fraction(-u_prime[1] * v_value[0] + v_prime[1] * u_value[0], area),
    )
    linear_first = matrix_apply(matrix, source_first)
    translation = (
        Fraction(target_first[0]) - linear_first[0],
        Fraction(target_first[1]) - linear_first[1],
    )
    assert affine_apply((matrix, translation), source_second) == target_second
    assert affine_apply((matrix, translation), source_third) == target_third
    return matrix, translation


def lattice_index(points: list[Point]) -> int:
    base = points[0]
    differences = [subtract(point, base) for point in points[1:]]
    output = 0
    for first, second in combinations(differences, 2):
        output = gcd(output, abs(determinant(first, second)))
    return output


def overlap(points: list[Point], mapping: AffineMap) -> list[Point]:
    point_set = set(points)
    return [point for point in points if affine_apply(mapping, point) in point_set]


def cross_matrix(
    points: list[Point], source: Triangle, target: Triangle
) -> list[list[int]]:
    source_edges = edge_vectors(points, source)
    target_edges = edge_vectors(points, target)
    return [
        [determinant(first, second) for second in target_edges]
        for first in source_edges
    ]


def fully_transverse(matrix: list[list[int]]) -> bool:
    return all(value for row in matrix for value in row)


def verify_pair(
    points: list[Point], source: Triangle, target: Triangle
) -> tuple[int, int, int]:
    area = doubled_area(points, source)
    assert area and doubled_area(points, target) == area
    cross = cross_matrix(points, source, target)
    assert fully_transverse(cross)
    mapping = triangle_map(points, source, target)
    matrix = mapping[0]
    trace = matrix[0] + matrix[3]

    first = cross[0][0]
    second = cross[0][1]
    third = cross[1][0]
    fourth = cross[1][1]
    trace_numerator = second - third
    assert trace == Fraction(trace_numerator, area)
    assert first * fourth - second * third == area * area
    assert (
        4 * first * fourth - (second + third) ** 2
        == 4 * area * area - trace_numerator * trace_numerator
    )

    subset = overlap(points, mapping)
    index = lattice_index(subset)
    assert index
    assert index % trace.denominator == 0

    # Directly test det(u,Mv)-det(v,Mu)=tr(M)det(u,v).
    for first_point, second_point, third_point in permutations(subset, 3):
        u_value = subtract(second_point, first_point)
        v_value = subtract(third_point, first_point)
        if determinant(u_value, v_value) == 0:
            continue
        mu = matrix_apply(matrix, u_value)
        mv = matrix_apply(matrix, v_value)
        left = (
            u_value[0] * mv[1] - u_value[1] * mv[0]
            - v_value[0] * mu[1] + v_value[1] * mu[0]
        )
        assert left == trace * determinant(u_value, v_value)
        break

    return len(subset), trace.denominator, index


def sample_profiles(points: list[Point], limit: int) -> tuple[int, Counter[int], int]:
    triangles = [
        triangle
        for triangle in permutations(range(len(points)), 3)
        if doubled_area(points, triangle) != 0
    ]
    checked = 0
    denominators: Counter[int] = Counter()
    maximum_overlap = 0
    for source in triangles:
        source_vertices = set(source)
        area = doubled_area(points, source)
        for target in triangles:
            if not source_vertices.isdisjoint(target):
                continue
            if doubled_area(points, target) != area:
                continue
            cross = cross_matrix(points, source, target)
            if not fully_transverse(cross):
                continue
            overlap_size, denominator, _ = verify_pair(points, source, target)
            denominators[denominator] += 1
            maximum_overlap = max(maximum_overlap, overlap_size)
            checked += 1
            if checked == limit:
                return checked, denominators, maximum_overlap
    return checked, denominators, maximum_overlap


def main() -> None:
    closure = sample_profiles(list(POINTS[:10]), 180)
    costas = sample_profiles(transformed_costas(11), 180)
    print("closure-10", closure)
    print("Costas-10", costas)
    assert closure == (
        180,
        Counter({
            429: 36, 52: 24, 143: 24, 1: 24, 51: 24,
            13: 12, 153: 12, 34: 12, 306: 12,
        }),
        3,
    ), closure
    assert costas == (
        180,
        Counter({
            1: 51, 2: 35, 4: 26, 8: 20, 3: 8, 16: 8,
            7: 8, 5: 6, 17: 6, 9: 6, 20: 4, 14: 2,
        }),
        5,
    ), costas
    print("special-affine trace denominator lattice gate: PASS")


if __name__ == "__main__":
    main()
