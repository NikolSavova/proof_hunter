#!/usr/bin/env python3
"""Exact certificates for the sharp oblique modular-midpoint theorem."""

from __future__ import annotations


Point = tuple[int, int]
Matrix = tuple[tuple[int, int], tuple[int, int]]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def scale(factor: int, point: Point) -> Point:
    return factor * point[0], factor * point[1]


def dot(left: Point, right: Point) -> int:
    return left[0] * right[0] + left[1] * right[1]


def mat_vec(matrix: Matrix, vector: Point) -> Point:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )


def transpose(matrix: Matrix) -> Matrix:
    return (
        (matrix[0][0], matrix[1][0]),
        (matrix[0][1], matrix[1][1]),
    )


def multiply(left: Matrix, right: Matrix) -> Matrix:
    transposed = transpose(right)
    return tuple(
        tuple(dot(row, column) for column in transposed)
        for row in left
    )  # type: ignore[return-value]


def determinant(matrix: Matrix) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def norm_square(point: Point) -> int:
    return dot(point, point)


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def prime_in_interval(lower: int, upper: int) -> int:
    candidate = lower + 1
    if candidate % 2 == 0:
        candidate += 1
    while candidate < upper:
        if is_prime(candidate):
            return candidate
        candidate += 2
    raise AssertionError("no prime in requested interval")


def inverse_gram_solution(gram: Matrix, target: Point, prime: int) -> Point:
    gram_det = determinant(gram) % prime
    inverse_det = pow(gram_det, -1, prime)
    inverse = (
        (
            gram[1][1] * inverse_det % prime,
            -gram[0][1] * inverse_det % prime,
        ),
        (
            -gram[1][0] * inverse_det % prime,
            gram[0][0] * inverse_det % prime,
        ),
    )
    solution = mat_vec(inverse, target)
    return solution[0] % prime, solution[1] % prime


def central_representatives(residue: int, prime: int, side: int) -> list[int]:
    lower = side // 3 + 1
    upper = 2 * side // 3 - 1
    first = residue
    if first < lower:
        first += ((lower - first + prime - 1) // prime) * prime
    return list(range(first, upper + 1, prime))


def verify_certificate(matrix: Matrix, translate: Point, side: int) -> None:
    matrix_det = determinant(matrix)
    assert matrix_det != 0
    prime = prime_in_interval(side // 100, side // 40)
    assert abs(matrix_det) < prime

    corners = [
        add(translate, mat_vec(matrix, (first, second)))
        for first in (0, side - 1)
        for second in (0, side - 1)
    ]
    height = max(abs(coordinate) for point in corners for coordinate in point)
    # Exact form of height < side^(3/2)/100.
    assert 10_000 * height * height < side * side * side

    matrix_t = transpose(matrix)
    gram = multiply(matrix_t, matrix)
    linear = mat_vec(matrix_t, translate)
    residue = inverse_gram_solution(
        gram,
        (-linear[0] % prime, -linear[1] % prime),
        prime,
    )
    representatives = [
        central_representatives(residue[index], prime, side)
        for index in range(2)
    ]
    assert min(map(len, representatives)) >= 10

    midpoint: Point | None = None
    physical_midpoint: Point | None = None
    for first in representatives[0]:
        for second in representatives[1]:
            trial = (first, second)
            physical = add(translate, mat_vec(matrix, trial))
            if physical != (0, 0):
                midpoint = trial
                physical_midpoint = physical
                break
        if midpoint is not None:
            break
    assert midpoint is not None and physical_midpoint is not None

    covector = mat_vec(matrix_t, physical_midpoint)
    assert covector[0] % prime == 0
    assert covector[1] % prime == 0
    quotient = covector[0] // prime, covector[1] // prime
    direction = -quotient[1], quotient[0]
    assert direction != (0, 0)
    assert dot(covector, direction) == 0
    assert max(map(abs, direction)) < side // 10

    plus_coefficient = add(midpoint, direction)
    minus_coefficient = subtract(midpoint, direction)
    for coefficient in (plus_coefficient, minus_coefficient):
        assert 0 <= coefficient[0] < side
        assert 0 <= coefficient[1] < side

    plus_point = add(translate, mat_vec(matrix, plus_coefficient))
    minus_point = add(translate, mat_vec(matrix, minus_coefficient))
    assert plus_point != minus_point
    assert plus_point != scale(-1, minus_point)
    assert norm_square(plus_point) == norm_square(minus_point)


def main() -> None:
    matrices: list[Matrix] = [
        ((1, 0), (0, 1)),
        ((3, 0), (0, 7)),
        ((1, 11), (0, 1)),
        ((7, -13), (5, 9)),
        ((12, 18), (6, 15)),
        ((2, 101), (1, 50)),
        ((37, 4), (-19, 11)),
    ]
    translations: list[Point] = [
        (12345, -6789),
        (-31007, 22003),
        (0, 0),
    ]
    side = 400_000_000
    certificates = 0
    for matrix in matrices:
        for translate in translations:
            verify_certificate(matrix, translate, side)
            certificates += 1
    print("sharp modular-midpoint certificates", certificates, "PASS")
    print("all congruences, box bounds, and equal-norm identities: PASS")


if __name__ == "__main__":
    main()
