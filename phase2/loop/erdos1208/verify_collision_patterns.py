#!/usr/bin/env python3
"""Exact Gaussian-rational checks for COLLISION_PATTERN_AUDIT.md."""

from __future__ import annotations

from fractions import Fraction


Gaussian = tuple[Fraction, Fraction]
ZERO: Gaussian = (Fraction(0), Fraction(0))
ONE: Gaussian = (Fraction(1), Fraction(0))
I: Gaussian = (Fraction(0), Fraction(1))


def add(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def negate(value: Gaussian) -> Gaussian:
    return -value[0], -value[1]


def multiply(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def row(left: tuple[int, int, int], right: tuple[int, int, int]) -> list[Gaussian]:
    coefficients = [ZERO for _ in range(5)]
    for triple, sign in ((left, 1), (right, -1)):
        for index, coefficient in zip(triple, (ONE, I, negate(I))):
            term = coefficient if sign == 1 else negate(coefficient)
            coefficients[index] = add(coefficients[index], term)
    return coefficients


def main() -> None:
    old_rows = [
        row((0, 0, 0), (2, 4, 3)),
        row((0, 0, 0), (3, 2, 1)),
        row((0, 0, 1), (4, 2, 4)),
        row((0, 0, 2), (2, 3, 4)),
    ]
    weights = [
        (Fraction(-1, 5), Fraction(3, 5)),
        (Fraction(-1, 5), Fraction(-3, 5)),
        (Fraction(-1, 5), Fraction(2, 5)),
        (Fraction(2, 5), Fraction(2, 5)),
    ]
    combination = [ZERO for _ in range(5)]
    for weight, current_row in zip(weights, old_rows):
        combination = [
            add(total, multiply(weight, coefficient))
            for total, coefficient in zip(combination, current_row)
        ]
    assert combination == [negate(add(ONE, negate(I))), ONE, negate(I), ZERO, ZERO]
    assert old_rows[0] and old_rows[1]  # Both use a diagonal left triple.

    # The two equations of the genuine off-diagonal three-cycle have this
    # coefficient matrix in x=a1-a0 and y=a2-a0.
    matrix = [
        (add(negate(ONE), negate(I)), negate(I)),
        (multiply((Fraction(-2), Fraction(0)), I), add(negate(ONE), I)),
    ]
    determinant = add(
        multiply(matrix[0][0], matrix[1][1]),
        negate(multiply(matrix[0][1], matrix[1][0])),
    )
    assert determinant == (Fraction(4), Fraction(0))

    triples = [(0, 0, 1), (1, 2, 0), (2, 1, 2)]
    assert all(middle != right for _, middle, right in triples)
    assert all(len({triple[position] for triple in triples}) == 3 for position in range(3))

    print("old weighted target", combination)
    print("off-diagonal determinant", determinant)
    print("PASS")


if __name__ == "__main__":
    main()
