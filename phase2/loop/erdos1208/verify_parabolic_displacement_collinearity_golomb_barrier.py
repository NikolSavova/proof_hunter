#!/usr/bin/env python3
"""Exact checks for PARABOLIC_DISPLACEMENT_COLLINEARITY_GOLOMB_BARRIER.md."""

from __future__ import annotations

from itertools import combinations, product


Point = tuple[int, int]
H_VALUE = 10
R_VALUE = 20


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def add(first: Point, second: Point) -> Point:
    return first[0] + second[0], first[1] + second[1]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def squared_norm(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def golomb_marks(prime: int, size: int) -> list[int]:
    assert size <= prime
    return [2 * prime * index + (index * index % prime) for index in range(size)]


def verify_golomb(marks: list[int]) -> None:
    differences = [second - first for first, second in combinations(marks, 2)]
    assert all(value > 0 for value in differences)
    assert len(differences) == len(set(differences))
    sums = [first + second for first, second in combinations(marks, 2)]
    diagonal_sums = [2 * value for value in marks]
    all_sums = sums + diagonal_sums
    assert len(all_sums) == len(set(all_sums))


def distance_sidon(points: list[Point]) -> bool:
    distances = [
        squared_norm(subtract(first, second))
        for first, second in combinations(points, 2)
    ]
    return len(distances) == len(set(distances))


def cyclic_edges(points: list[Point]):
    return [
        subtract(points[(index + 1) % 3], points[index])
        for index in range(3)
    ]


def cross_transverse(source: list[Point], target: list[Point]) -> bool:
    source_edges = cyclic_edges(source)
    target_edges = cyclic_edges(target)
    return all(
        determinant(first, second)
        for first in source_edges
        for second in target_edges
    )


def barrier_profile(sign: int):
    # p=31 and h=5 give six disjoint ruler classes.
    prime = 31
    block_size = 5
    marks = golomb_marks(prime, 6 * block_size)
    verify_golomb(marks)
    groups = [
        marks[index * block_size:(index + 1) * block_size]
        for index in range(6)
    ]

    sources = [
        [(R_VALUE * value, row) for value in groups[row]]
        for row in range(3)
    ]
    targets = [
        [
            (R_VALUE * value, H_VALUE + sign * row)
            for value in groups[3 + row]
        ]
        for row in range(3)
    ]
    all_points = [point for group in sources + targets for point in group]
    assert len(all_points) == len(set(all_points)) == 30
    assert distance_sidon(all_points)

    blocks = []
    for row in range(3):
        current = []
        for source in sources[row]:
            for target in targets[row]:
                scalar = subtract(target, source) if sign == 1 else add(target, source)
                assert scalar[1] == H_VALUE
                current.append((scalar, source, target))
        assert len(current) == block_size * block_size
        blocks.append(current)

    scalar_vectors = [record[0] for block in blocks for record in block]
    assert len(scalar_vectors) == len(set(scalar_vectors)) == 3 * block_size * block_size

    clean_count = 0
    equal_area_count = 0
    fully_transverse_count = 0
    lifted_collinearity_count = 0
    for records in product(*blocks):
        source = [record[1] for record in records]
        target = [record[2] for record in records]
        source_area = determinant(
            subtract(source[1], source[0]),
            subtract(source[2], source[0]),
        )
        target_area = determinant(
            subtract(target[1], target[0]),
            subtract(target[2], target[0]),
        )
        assert source_area and target_area
        clean_count += 1

        # For w=(1,0), r is the source y-coordinate and s is the
        # horizontal displacement (trace +2) or sum (trace -2).
        s_values = [record[0][0] for record in records]
        lifted_collinear = s_values[0] - 2 * s_values[1] + s_values[2] == 0
        assert lifted_collinear == (source_area == target_area)
        if lifted_collinear:
            lifted_collinearity_count += 1
            equal_area_count += 1
            if cross_transverse(source, target):
                fully_transverse_count += 1

    expected_raw = block_size ** 6
    assert clean_count == expected_raw
    assert lifted_collinearity_count == equal_area_count
    expected_filtered = (28, 27) if sign == 1 else (14, 14)
    assert (equal_area_count, fully_transverse_count) == expected_filtered
    return (
        len(all_points),
        expected_raw,
        equal_area_count,
        fully_transverse_count,
        max(point[0] for point in all_points),
    )


def main() -> None:
    plus = barrier_profile(1)
    minus = barrier_profile(-1)
    print("trace +2 raw barrier", plus)
    print("trace -2 raw barrier", minus)
    print("parabolic displacement-collinearity Golomb barrier: PASS")


if __name__ == "__main__":
    main()
