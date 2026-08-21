#!/usr/bin/env python3
"""Verify the rank-five anchored repeated-track normal form."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from random import Random

Point = tuple[int, int]


class Gaussian:
    """A minimal exact Q(i) scalar for the matrix audit."""

    def __init__(self, real: int | Fraction = 0, imag: int | Fraction = 0):
        self.real = Fraction(real)
        self.imag = Fraction(imag)

    def __add__(self, other: object) -> Gaussian:
        value = coerce(other)
        return Gaussian(self.real + value.real, self.imag + value.imag)

    __radd__ = __add__

    def __neg__(self) -> Gaussian:
        return Gaussian(-self.real, -self.imag)

    def __sub__(self, other: object) -> Gaussian:
        return self + (-coerce(other))

    def __rsub__(self, other: object) -> Gaussian:
        return coerce(other) - self

    def __mul__(self, other: object) -> Gaussian:
        value = coerce(other)
        return Gaussian(
            self.real * value.real - self.imag * value.imag,
            self.real * value.imag + self.imag * value.real,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> Gaussian:
        value = coerce(other)
        norm = value.real * value.real + value.imag * value.imag
        assert norm
        return Gaussian(
            (self.real * value.real + self.imag * value.imag) / norm,
            (self.imag * value.real - self.real * value.imag) / norm,
        )

    def __bool__(self) -> bool:
        return bool(self.real or self.imag)

    def __eq__(self, other: object) -> bool:
        value = coerce(other)
        return self.real == value.real and self.imag == value.imag


def coerce(value: object) -> Gaussian:
    if isinstance(value, Gaussian):
        return value
    assert isinstance(value, (int, Fraction))
    return Gaussian(value)


ZERO = Gaussian()
ONE = Gaussian(1)
I = Gaussian(0, 1)
L = ONE + I


MATRIX = (
    (ONE, ZERO, -ONE, ZERO, ZERO, -ONE),
    (ZERO, ONE, I, -L, ZERO, I),
    (ZERO, ONE, L, -L, ZERO, I),
    (ONE, ZERO, -ONE, ZERO, ONE, -ONE),
    (ZERO, ONE, ZERO, -ONE, -I, I),
    (ZERO, ONE, ZERO, ZERO, -I, I),
)


def rank(matrix: tuple[tuple[Gaussian, ...], ...]) -> int:
    rows = [list(row) for row in matrix]
    if not rows:
        return 0
    row = 0
    for column in range(len(rows[0])):
        pivot = next(
            (candidate for candidate in range(row, len(rows)) if rows[candidate][column]),
            None,
        )
        if pivot is None:
            continue
        rows[row], rows[pivot] = rows[pivot], rows[row]
        value = rows[row][column]
        rows[row] = [entry / value for entry in rows[row]]
        for candidate in range(len(rows)):
            if candidate == row:
                continue
            factor = rows[candidate][column]
            if factor:
                rows[candidate] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(rows[candidate], rows[row])
                ]
        row += 1
        if row == len(rows):
            break
    return row


def matrix_vector(
    matrix: tuple[tuple[Gaussian, ...], ...],
    vector: tuple[Gaussian, ...],
) -> tuple[Gaussian, ...]:
    return tuple(
        sum((coefficient * value for coefficient, value in zip(row, vector)), ZERO)
        for row in matrix
    )


def audit_matrix() -> None:
    assert rank(MATRIX) == 5
    right_kernel = (ONE, -I, ZERO, ZERO, ZERO, ONE)
    assert matrix_vector(MATRIX, right_kernel) == (ZERO,) * 6

    left_kernel = (ONE, ONE - I, -ONE, -ONE, -ONE + I, ONE)
    transpose = tuple(tuple(row[column] for row in MATRIX) for column in range(6))
    assert matrix_vector(transpose, left_kernel) == (ZERO,) * 6

    for omitted in range(6):
        five_rows = tuple(row for index, row in enumerate(MATRIX) if index != omitted)
        assert rank(five_rows) == 5
    for repeated_role in range(6):
        remaining = [index for index in range(6) if index != repeated_role]
        for four_roles in combinations(remaining, 4):
            selected = (repeated_role, *four_roles)
            assert rank(tuple(MATRIX[index] for index in selected)) == 5


def add(*values: Point) -> Point:
    return sum(value[0] for value in values), sum(value[1] for value in values)


def neg(value: Point) -> Point:
    return -value[0], -value[1]


def sub(left: Point, right: Point) -> Point:
    return add(left, neg(right))


def rotate(value: Point) -> Point:
    return -value[1], value[0]


def linear(value: Point) -> Point:
    return add(value, rotate(value))


def track_differences(
    u_value: Point,
    c_value: Point,
    a_value: Point,
    b_value: Point,
    e_value: Point,
    q_value: Point,
) -> tuple[Point, ...]:
    return (
        sub(sub(u_value, a_value), q_value),
        add(sub(c_value, linear(b_value)), rotate(add(q_value, a_value))),
        add(
            sub(c_value, linear(b_value)),
            rotate(q_value),
            linear(a_value),
        ),
        add(sub(sub(u_value, a_value), q_value), e_value),
        add(sub(c_value, b_value), rotate(sub(q_value, e_value))),
        add(c_value, rotate(sub(q_value, e_value))),
    )


def audit_integer_identities() -> None:
    rng = Random(1208202604)
    for _ in range(2000):
        values = tuple(
            (rng.randrange(-50, 51), rng.randrange(-50, 51))
            for _ in range(6)
        )
        u_value, c_value, a_value, b_value, e_value, q_value = values
        differences = track_differences(*values)
        relation = add(
            differences[0],
            sub(differences[1], rotate(differences[1])),
            neg(differences[2]),
            neg(differences[3]),
            sub(rotate(differences[4]), differences[4]),
            differences[5],
        )
        assert relation == (0, 0)
        assert add(rotate(u_value), c_value) == add(
            rotate(sub(u_value, q_value)),
            sub(c_value, neg(rotate(q_value))),
        )

        gauge = (
            q_value,
            neg(rotate(q_value)),
            (0, 0),
            (0, 0),
            (0, 0),
            q_value,
        )
        assert track_differences(*gauge) == ((0, 0),) * 6


def main() -> None:
    audit_matrix()
    audit_integer_identities()
    print("SWAP ANCHORED TRACK REUSE RANK FIVE: PASS")


if __name__ == "__main__":
    main()
