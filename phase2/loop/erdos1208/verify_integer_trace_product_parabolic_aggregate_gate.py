#!/usr/bin/env python3
"""Exact checks for INTEGER_TRACE_PRODUCT_PARABOLIC_AGGREGATE_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import gcd, isqrt

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_special_affine_trace_denominator_lattice_gate import (
    cross_matrix,
    doubled_area,
    edge_vectors,
    fully_transverse,
    triangle_map,
)


Point = tuple[int, int]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def canonical_direction(vector: Point) -> Point:
    divisor = gcd(abs(vector[0]), abs(vector[1]))
    direction = (vector[0] // divisor, vector[1] // divisor)
    if direction[0] < 0 or (direction[0] == 0 and direction[1] < 0):
        direction = (-direction[0], -direction[1])
    return direction


def rational_square(value: Fraction) -> bool:
    if value < 0:
        return False
    numerator_root = isqrt(value.numerator)
    denominator_root = isqrt(value.denominator)
    return (
        numerator_root * numerator_root == value.numerator
        and denominator_root * denominator_root == value.denominator
    )


def invariant_value(matrix, vector: Point) -> int:
    image = (
        matrix[0] * vector[0] + matrix[1] * vector[1],
        matrix[2] * vector[0] + matrix[3] * vector[1],
    )
    value = vector[0] * image[1] - vector[1] * image[0]
    assert value.denominator == 1
    return value.numerator


def records(points: list[Point]):
    buckets = defaultdict(list)
    for triangle in permutations(range(len(points)), 3):
        area = doubled_area(points, triangle)
        if area:
            buckets[area].append(triangle)

    for triangles in buckets.values():
        for source in triangles:
            source_vertices = set(source)
            for target in triangles:
                if not source_vertices.isdisjoint(target):
                    continue
                cross = cross_matrix(points, source, target)
                if not fully_transverse(cross):
                    continue
                mapping = triangle_map(points, source, target)
                yield source, target, cross, mapping


def trace_and_product_profile(prime: int):
    points = transformed_costas(prime)
    trace_counts: Counter[int] = Counter()
    product_fibres: Counter[tuple[tuple[Fraction, ...], int]] = Counter()
    total = 0

    for source, _target, cross, mapping in records(points):
        total += 1
        matrix = mapping[0]
        trace = matrix[0] + matrix[3]
        if trace.denominator != 1:
            continue
        trace_value = trace.numerator
        trace_counts[trace_value] += 1

        edges = edge_vectors(points, source)
        q_values = [invariant_value(matrix, edge) for edge in edges]
        assert q_values == [cross[index][index] for index in range(3)]
        assert all(q_values)
        area = doubled_area(points, source)
        assert (
            (q_values[0] + q_values[2] - q_values[1]) ** 2
            + (4 - trace_value * trace_value) * area * area
            == 4 * q_values[0] * q_values[2]
        )

        if trace_value in (2, -2):
            # All nonzero values have one signed rational squareclass.
            for value in q_values[1:]:
                assert rational_square(Fraction(value, q_values[0]))

            sign = 1 if trace_value == 2 else -1
            assert cross[0][0] * cross[1][1] == (
                cross[0][1] - sign * area
            ) ** 2
        else:
            product = q_values[0] * q_values[2]
            product_fibres[matrix, product] += 1

    return (
        total,
        trace_counts[2],
        trace_counts[-2],
        max(product_fibres.values(), default=0),
        len(product_fibres),
    )


def direction_edge_counts(points: list[Point]) -> Counter[Point]:
    return Counter(
        canonical_direction(subtract(second, first))
        for first, second in combinations(points, 2)
    )


def line_counts(points: list[Point], vector: Point) -> Counter[int]:
    return Counter(determinant(vector, point) for point in points)


def shifted_correlation(
    first: Counter[int], second: Counter[int], shift: int
) -> int:
    return sum(load * second.get(level + shift, 0) for level, load in first.items())


def line_correlation_profile(points: list[Point]):
    edge_counts = direction_edge_counts(points)
    line_cache = {
        (first, second): line_counts(points, subtract(points[second], points[first]))
        for first in range(len(points))
        for second in range(len(points))
        if first != second
    }

    correlation_sum = 0
    maximum_correlation = 0
    for first in range(len(points)):
        for second in range(len(points)):
            if first == second:
                continue
            source_vector = subtract(points[second], points[first])
            source_direction = canonical_direction(source_vector)
            source_lines = line_cache[first, second]
            source_moment = len(points) + 2 * edge_counts[source_direction]
            assert sum(load * load for load in source_lines.values()) == source_moment

            for target_first in range(len(points)):
                for target_second in range(len(points)):
                    if target_first == target_second:
                        continue
                    target_vector = subtract(
                        points[target_second], points[target_first]
                    )
                    target_direction = canonical_direction(target_vector)
                    target_lines = line_cache[target_first, target_second]
                    target_moment = len(points) + 2 * edge_counts[target_direction]
                    shift = (
                        determinant(target_vector, points[target_first])
                        - determinant(source_vector, points[first])
                    )
                    correlation = shifted_correlation(
                        source_lines, target_lines, shift
                    )
                    assert correlation * correlation <= source_moment * target_moment
                    correlation_sum += correlation
                    maximum_correlation = max(maximum_correlation, correlation)

    fully_transverse_count = sum(1 for _ in records(points))
    assert fully_transverse_count <= correlation_sum

    # A rational upper bound for the radical envelope: sqrt(x)<=x for x>=1.
    # The verifier's substantive check is the exact per-edge Cauchy inequality
    # above; this final check merely confirms the combinatorial summation.
    coarse_envelope = sum(
        2 * load * (len(points) + 2 * load)
        for load in edge_counts.values()
    ) ** 2
    assert correlation_sum <= coarse_envelope
    return fully_transverse_count, correlation_sum, maximum_correlation


def main() -> None:
    expected = {
        11: (1_260, 0, 48),
        13: (6_876, 156, 108),
        17: (32_292, 444, 624),
    }
    for prime, prefix in expected.items():
        actual = trace_and_product_profile(prime)
        assert actual[:3] == prefix, (prime, actual, prefix)
        assert actual[3] > 0 and actual[4] > 0
        print(f"Costas-{prime}", actual)

    correlation = line_correlation_profile(transformed_costas(11))
    assert correlation[0] == 1_260
    print("line-correlation Costas-11", correlation)
    print("integer trace product/parabolic aggregate gate: PASS")


if __name__ == "__main__":
    main()
