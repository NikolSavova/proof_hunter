#!/usr/bin/env python3
"""Exact checks for INTEGER_TRACE_INVARIANT_FORM_PELL_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import permutations
from math import isqrt

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_special_affine_trace_denominator_lattice_gate import (
    cross_matrix,
    doubled_area,
    edge_vectors,
    fully_transverse,
    triangle_map,
)


Point = tuple[int, int]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def matrix_apply(matrix, vector: Point):
    return (
        matrix[0] * vector[0] + matrix[1] * vector[1],
        matrix[2] * vector[0] + matrix[3] * vector[1],
    )


def invariant_value(matrix, vector: Point) -> int:
    image = matrix_apply(matrix, vector)
    value = determinant(vector, image)
    assert value.denominator == 1
    return value.numerator


def trace_denominator_profile(prime: int) -> tuple[int, int, int, int]:
    points = transformed_costas(prime)
    buckets = defaultdict(list)
    for triangle in permutations(range(len(points)), 3):
        area = doubled_area(points, triangle)
        if area:
            buckets[area].append(triangle)

    denominators: Counter[int] = Counter()
    identity_checks = 0
    for triangles in buckets.values():
        for source in triangles:
            source_vertices = set(source)
            for target in triangles:
                if not source_vertices.isdisjoint(target):
                    continue
                cross = cross_matrix(points, source, target)
                if not fully_transverse(cross):
                    continue
                matrix, _ = triangle_map(points, source, target)
                trace = matrix[0] + matrix[3]
                denominators[trace.denominator] += 1

                if trace.denominator == 1 and trace not in (2, -2):
                    edges = edge_vectors(points, source)
                    q_one, q_two, q_three = (
                        invariant_value(matrix, edge) for edge in edges
                    )
                    area = doubled_area(points, source)
                    assert all((q_one, q_two, q_three))
                    assert (
                        (q_one + q_three - q_two) ** 2
                        + (4 - trace.numerator ** 2) * area * area
                        == 4 * q_one * q_three
                    )
                    assert invariant_value(
                        matrix, matrix_apply(matrix, edges[0])
                    ) == q_one
                    identity_checks += 1

    total = sum(denominators.values())
    small = sum(load for denominator, load in denominators.items() if denominator <= 4)
    assert identity_checks
    return total, denominators[1], small, identity_checks


def verify_planted_integer_trace() -> tuple[tuple[int, int, int, int], int]:
    first = (339, -652, 13, -25)
    second = (-17, 312, -3, 55)
    inverse_first = (first[3], -first[1], -first[2], first[0])
    matrix = (
        second[0] * inverse_first[0] + second[1] * inverse_first[2],
        second[0] * inverse_first[1] + second[1] * inverse_first[3],
        second[2] * inverse_first[0] + second[3] * inverse_first[2],
        second[2] * inverse_first[1] + second[3] * inverse_first[3],
    )
    determinant_value = matrix[0] * matrix[3] - matrix[1] * matrix[2]
    trace = matrix[0] + matrix[3]
    assert determinant_value == 1
    assert matrix == (-3_631, 94_684, -640, 16_689)
    assert trace == 13_058
    discriminant = trace * trace - 4
    root = isqrt(discriminant)
    assert root * root != discriminant
    return matrix, trace


def main() -> None:
    expected = {
        11: (1_260, 360, 804),
        13: (6_876, 1_308, 2_508),
        17: (32_292, 6_108, 10_956),
    }
    for prime, prefix in expected.items():
        actual = trace_denominator_profile(prime)
        assert actual[:3] == prefix, (prime, actual, prefix)
        print(f"Costas-{prime}", actual)

    planted = verify_planted_integer_trace()
    print("planted", planted)
    print("integer trace invariant form Pell gate: PASS")


if __name__ == "__main__":
    main()
