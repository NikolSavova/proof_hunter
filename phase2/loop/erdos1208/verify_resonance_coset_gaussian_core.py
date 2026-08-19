#!/usr/bin/env python3
"""Exact finite checks for the resonance-coset/Gaussian-core dichotomy."""

from __future__ import annotations

from collections import Counter

from analyze_affine_costas_energy import welch


Point = tuple[int, int]
Matrix = tuple[tuple[int, int], tuple[int, int]]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def apply(matrix: Matrix, point: Point) -> Point:
    return (
        matrix[0][0] * point[0] + matrix[0][1] * point[1],
        matrix[1][0] * point[0] + matrix[1][1] * point[1],
    )


def determinant(matrix: Matrix) -> int:
    return (
        matrix[0][0] * matrix[1][1]
        - matrix[0][1] * matrix[1][0]
    )


def adjugate(matrix: Matrix) -> Matrix:
    return (
        (matrix[1][1], -matrix[0][1]),
        (-matrix[1][0], matrix[0][0]),
    )


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def resonance_numerator(matrix: Matrix) -> tuple[Matrix, int]:
    # R=T^{-1}JT=(adj(T)JT)/det(T).
    j_times_t: Matrix = (
        (-matrix[1][0], -matrix[1][1]),
        (matrix[0][0], matrix[0][1]),
    )
    return multiply(adjugate(matrix), j_times_t), determinant(matrix)


def divisible_point(point: Point, divisor: int) -> bool:
    divisor = abs(divisor)
    return point[0] % divisor == 0 and point[1] % divisor == 0


def in_gamma(matrix: Matrix, point: Point) -> bool:
    numerator, denominator = resonance_numerator(matrix)
    return divisible_point(apply(numerator, point), denominator)


def in_lambda(matrix: Matrix, vector: Point) -> bool:
    det = determinant(matrix)
    numerator = apply(adjugate(matrix), vector)
    if not divisible_point(numerator, det):
        return False
    divisor = abs(det)
    gamma = numerator[0] // det, numerator[1] // det
    # The signed division above is exact; abs(det) was only for divisibility.
    assert apply(matrix, gamma) == vector
    return in_gamma(matrix, gamma)


def difference_representations(points: list[Point]) -> Counter[Point]:
    return Counter(subtract(left, right) for left in points for right in points)


def gamma_cosets(points: list[Point], matrix: Matrix) -> list[list[Point]]:
    remaining = set(points)
    cosets: list[list[Point]] = []
    while remaining:
        representative = next(iter(remaining))
        cell = [
            point
            for point in list(remaining)
            if in_gamma(matrix, subtract(point, representative))
        ]
        for point in cell:
            remaining.remove(point)
        cosets.append(cell)
    return cosets


def linear_l(point: Point) -> Point:
    return point[0] - point[1], point[0] + point[1]


def quarter_turn(point: Point) -> Point:
    return -point[1], point[0]


def triple_support(points: list[Point]) -> set[Point]:
    return {
        subtract(add(first, second), linear_l(third))
        for first in points
        for second in points
        for third in points
    }


def quotient_classes(
    representatives: list[Point], matrix: Matrix
) -> list[list[int]]:
    remaining = set(range(len(representatives)))
    classes: list[list[int]] = []
    while remaining:
        first = next(iter(remaining))
        cell = [
            index
            for index in list(remaining)
            if in_lambda(
                matrix,
                subtract(representatives[index], representatives[first]),
            )
        ]
        for index in cell:
            remaining.remove(index)
        classes.append(cell)
    return classes


def verify_instance(prime: int, matrix: Matrix) -> tuple[int, int, int, int]:
    assert determinant(matrix) != 0
    base = welch(prime)
    k = len(base)
    representations = difference_representations(base)
    assert representations[(0, 0)] == k
    assert all(
        multiplicity == 1
        for difference, multiplicity in representations.items()
        if difference != (0, 0)
    )

    cosets = gamma_cosets(base, matrix)
    h_resonance = sum(
        1
        for difference in representations
        if difference != (0, 0) and in_gamma(matrix, difference)
    )
    occupancy_identity = sum(len(cell) * (len(cell) - 1) for cell in cosets)
    assert h_resonance == occupancy_identity

    physical_cells = [[apply(matrix, point) for point in cell] for cell in cosets]
    supports = [triple_support(cell) for cell in physical_cells]
    representatives = [next(iter(support)) for support in supports]

    # Every internal support lies in one Lambda-coset.
    for support, representative in zip(supports, representatives):
        assert all(
            in_lambda(matrix, subtract(point, representative))
            for point in support
        )

    output_cosets = quotient_classes(representatives, matrix)
    max_output_coset_multiplicity = max(map(len, output_cosets))
    assert max_output_coset_multiplicity == 1

    internal_union = set().union(*supports)
    assert len(internal_union) == sum(map(len, supports))

    physical = [apply(matrix, point) for point in base]
    full_support = triple_support(physical)
    assert internal_union <= full_support
    assert len(full_support) >= sum(map(len, supports))

    largest_cell = max(map(len, cosets))
    collision_denominator = (
        2 * k**3
        - k**2
        + h_resonance * (k**2 + k - 1)
    )
    assert collision_denominator <= 2 * largest_cell * k**3
    assert 2 * largest_cell * len(full_support) >= k**3

    # Brute finite R-stability check on the differences used by this row.
    r_numerator, r_denominator = resonance_numerator(matrix)
    for difference in representations:
        if not in_gamma(matrix, difference):
            continue
        rotated_numerator = apply(r_numerator, difference)
        rotated = (
            rotated_numerator[0] // r_denominator,
            rotated_numerator[1] // r_denominator,
        )
        assert in_gamma(matrix, rotated)
        assert apply(matrix, rotated) == quarter_turn(apply(matrix, difference))

    return (
        len(cosets),
        largest_cell,
        h_resonance,
        max_output_coset_multiplicity,
    )


def main() -> None:
    matrices: list[Matrix] = [
        ((1, 0), (0, 1)),
        ((2, 0), (0, 1)),
        ((2, 1), (1, 1)),
        ((3, 1), (1, 1)),
        ((4, 1), (1, 1)),
        ((3, 2), (1, 1)),
        ((5, 2), (1, 1)),
        ((5, 1), (2, 1)),
    ]
    profiles = []
    for prime in (7, 11, 13):
        for matrix in matrices:
            profile = verify_instance(prime, matrix)
            profiles.append((prime, determinant(matrix), profile))
    print("checked profiles (prime, det, cosets/largest/H/output multiplicity)")
    for profile in profiles:
        print(profile)
    print("resonance-coset Gaussian-core dichotomy: PASS")


if __name__ == "__main__":
    main()
