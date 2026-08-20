#!/usr/bin/env python3
"""Checks for THREE_SIDE_INVARIANT_COUPLING_PARABOLIC_SHARPNESS_GATE.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations


Point = tuple[int, int]


X_VALUES = [
    29_731,
    70_499,
    683_831,
    407_793,
    867_066,
    508_031,
    408_985,
    292_518,
    990_968,
    660_358,
]
C_VALUE = 100
H_VALUE = 200


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def matrix_apply(vector: Point) -> Point:
    return vector[0] + vector[1], vector[1]


def affine_apply(point: Point) -> Point:
    return point[0] + point[1] + C_VALUE, point[1] + H_VALUE


def squared_norm(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def cyclic_edges(points: list[Point], indices: tuple[int, int, int]):
    return [
        subtract(points[indices[(slot + 1) % 3]], points[indices[slot]])
        for slot in range(3)
    ]


def invariant_value(vector: Point) -> int:
    return determinant(vector, matrix_apply(vector))


def verify_cross_matrix_reconstruction() -> int:
    # A synthetic integer example.  Start from two determinant-equal frames.
    source = [(2, 1), (1, 3)]
    target = [(-4, -3), (-1, -2)]
    area = determinant(source[0], source[1])
    assert area == determinant(target[0], target[1]) == 5
    source.append((-3, -4))
    target.append((5, 5))
    cross = [
        [determinant(first, second) for second in target]
        for first in source
    ]
    q_one, q_two, q_three = (cross[index][index] for index in range(3))
    trace_area = cross[0][1] - cross[1][0]
    discriminant = (
        q_one * q_one + q_two * q_two + q_three * q_three
        - 2 * q_one * q_two - 2 * q_two * q_three - 2 * q_three * q_one
    )
    assert discriminant == trace_area * trace_area - 4 * area * area

    reconstructed = [
        [q_one, (trace_area - q_one - q_two + q_three) // 2, 0],
        [(-trace_area - q_one - q_two + q_three) // 2, q_two, 0],
        [0, 0, q_three],
    ]
    reconstructed[0][2] = (-trace_area - q_one + q_two - q_three) // 2
    reconstructed[2][0] = (trace_area - q_one + q_two - q_three) // 2
    reconstructed[1][2] = (trace_area + q_one - q_two - q_three) // 2
    reconstructed[2][1] = (-trace_area + q_one - q_two - q_three) // 2
    assert reconstructed == cross
    assert all(sum(row) == 0 for row in cross)
    assert all(sum(cross[row][column] for row in range(3)) == 0 for column in range(3))
    return discriminant


def verify_sharpness_certificate():
    source = [(value, index + 1) for index, value in enumerate(X_VALUES)]
    target = [affine_apply(point) for point in source]
    points = source + target

    distances = [
        squared_norm(subtract(first, second))
        for first, second in combinations(points, 2)
    ]
    assert len(distances) == len(set(distances))
    assert set(source).isdisjoint(target)

    # Distance-Sidon implies unordered additive Sidon, as used for trace -2.
    sums = [
        (first[0] + second[0], first[1] + second[1])
        for first, second in combinations_with_replacement(points, 2)
    ]
    assert len(sums) == len(set(sums))

    # Trace +2 is exactly collinearity of the point displacements.
    displacements = [subtract(target[index], source[index]) for index in range(10)]
    base_difference = subtract(displacements[1], displacements[0])
    assert all(
        determinant(base_difference, subtract(value, displacements[0])) == 0
        for value in displacements[2:]
    )

    value_triples: Counter[tuple[int, int, int]] = Counter()
    record_count = 0
    for indices in permutations(range(len(source)), 3):
        source_edges = cyclic_edges(source, indices)
        target_edges = cyclic_edges(target, indices)
        assert target_edges == [matrix_apply(edge) for edge in source_edges]
        area = determinant(source_edges[0], source_edges[1])
        assert area and determinant(target_edges[0], target_edges[1]) == area
        cross = [
            [determinant(first, second) for second in target_edges]
            for first in source_edges
        ]
        assert all(value for row in cross for value in row)
        q_values = tuple(invariant_value(edge) for edge in source_edges)
        assert q_values == tuple(cross[index][index] for index in range(3))
        vertical_gaps = tuple(edge[1] for edge in source_edges)
        assert sum(vertical_gaps) == 0
        assert q_values == tuple(-gap * gap for gap in vertical_gaps)
        value_triples[q_values] += 1
        record_count += 1

    assert record_count == 10 * 9 * 8
    # The eight increasing consecutive triples have vertical gaps (1,1,-2).
    assert value_triples[-1, -1, -4] >= 8
    return record_count, value_triples[-1, -1, -4], len(value_triples)


def main() -> None:
    discriminant = verify_cross_matrix_reconstruction()
    assert discriminant == 44
    sharpness = verify_sharpness_certificate()
    print("nonparabolic discriminant", discriminant)
    print("trace-2 sharpness certificate", sharpness)
    print("three-side invariant/parabolic sharpness gate: PASS")


if __name__ == "__main__":
    main()
