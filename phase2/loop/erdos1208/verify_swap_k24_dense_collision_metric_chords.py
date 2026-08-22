#!/usr/bin/env python3
"""Verify the dense-collision metric/common-chord dichotomy."""

from __future__ import annotations

from fractions import Fraction


Point = tuple[int, int]


def add(first: Point, second: Point) -> Point:
    return first[0] + second[0], first[1] + second[1]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def rotate(value: Point) -> Point:
    return -value[1], value[0]


def linear(value: Point) -> Point:
    return subtract(value, rotate(value))


def dot(first: Point, second: Point) -> int:
    return first[0] * second[0] + first[1] * second[1]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def norm(value: Point) -> int:
    return dot(value, value)


def scale(multiplier: Fraction, value: Point) -> tuple[Fraction, Fraction]:
    return multiplier * value[0], multiplier * value[1]


def verify_transverse_metric_map() -> None:
    a_value = (10, 3)
    b_value = (2, -1)
    alpha = (1, 2)
    beta = (3, 1)
    assert dot(alpha, beta) == 5

    first_a = (20, 10)
    first_a_prime = subtract(first_a, a_value)
    second_a = subtract(first_a, alpha)
    second_a_prime = subtract(first_a_prime, alpha)
    first_b = (5, 30)
    first_b_prime = subtract(first_b, b_value)
    second_b = subtract(first_b, beta)
    second_b_prime = subtract(first_b_prime, beta)

    c_value = (7, 4)
    c_prime = (-2, 5)
    delta_c = subtract(c_value, c_prime)
    k_value = subtract(a_value, rotate(b_value))
    z_prime = (0, 0)
    z_value = subtract(k_value, linear(delta_c))
    delta_z = subtract(z_value, z_prime)
    assert add(delta_z, linear(delta_c)) == subtract(
        a_value, rotate(b_value)
    )

    x_first = subtract(c_value, first_a)
    x_second = subtract(c_value, second_a)
    x_first_prime = subtract(c_prime, first_a_prime)
    x_second_prime = subtract(c_prime, second_a_prime)
    u_value = subtract(delta_c, a_value)
    assert subtract(x_second, x_second_prime) == u_value
    gap_zero = (norm(x_first) - norm(x_second)) - (
        norm(x_first_prime) - norm(x_second_prime)
    )
    assert gap_zero == -2 * dot(u_value, alpha)

    t_first = subtract(z_value, rotate(subtract(c_value, first_b)))
    t_second = subtract(z_value, rotate(subtract(c_value, second_b)))
    t_first_prime = subtract(
        z_prime, rotate(subtract(c_prime, first_b_prime))
    )
    t_second_prime = subtract(
        z_prime, rotate(subtract(c_prime, second_b_prime))
    )
    assert subtract(t_first, t_second) == rotate(beta)
    assert subtract(t_second, t_second_prime) == (-u_value[0], -u_value[1])
    gap_one = (norm(t_first) - norm(t_second)) - (
        norm(t_first_prime) - norm(t_second_prime)
    )
    assert gap_one == -2 * dot(u_value, rotate(beta))

    jacobian = 4 * determinant(alpha, rotate(beta))
    assert jacobian == 4 * dot(alpha, beta) == 20

    # Solve the two scalar equations and recover u exactly.
    row_first = alpha
    row_second = rotate(beta)
    rhs_first = Fraction(-gap_zero, 2)
    rhs_second = Fraction(-gap_one, 2)
    det_value = determinant(row_first, row_second)
    recovered_x = Fraction(
        rhs_first * row_second[1] - row_first[1] * rhs_second,
        det_value,
    )
    recovered_y = Fraction(
        row_first[0] * rhs_second - rhs_first * row_second[0],
        det_value,
    )
    assert (recovered_x, recovered_y) == u_value


def verify_two_line_alternative() -> None:
    a_chords = ((1, 0), (2, 0), (-3, 0))
    b_chords = ((0, 1), (0, -2), (0, 5))
    assert all(dot(first, second) == 0 for first in a_chords for second in b_chords)
    first_a = a_chords[0]
    first_b = b_chords[0]
    assert all(determinant(first_a, chord) == 0 for chord in a_chords)
    assert all(determinant(first_b, chord) == 0 for chord in b_chords)
    assert dot(first_a, first_b) == 0

    # Conversely, a single nonorthogonal pair activates the transverse map.
    perturbed_b = b_chords + ((1, 1),)
    transverse_pairs = [
        (first, second)
        for first in a_chords
        for second in perturbed_b
        if dot(first, second) != 0
    ]
    assert transverse_pairs
    assert all(4 * abs(dot(first, second)) >= 4 for first, second in transverse_pairs)


def main() -> None:
    verify_transverse_metric_map()
    verify_two_line_alternative()
    print("K2,4 dense-collision metric chord dichotomy: PASS")


if __name__ == "__main__":
    main()
