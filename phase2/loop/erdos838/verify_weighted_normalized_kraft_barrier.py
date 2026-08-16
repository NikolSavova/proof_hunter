#!/usr/bin/env python3
"""Exact certificate for the stretchable weighted normalized-Kraft failure."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations


POINTS = ((0, 0), (1, 10), (2, 15), (3, 21), (4, 50))
ROOTS = (
    (1, 2), (1, 3), (2, 3), (0, 3), (0, 2),
    (0, 1), (0, 4), (1, 4), (2, 4), (3, 4),
)
WORD = (1, 2, 1, 0, 1, 2, 3, 2, 1, 0)
SIZES = (256, 16, 16, 16, 256)


def determinant(i: int, j: int, k: int) -> int:
    xi, yi = POINTS[i]
    xj, yj = POINTS[j]
    xk, yk = POINTS[k]
    return (xj - xi) * (yk - yi) - (yj - yi) * (xk - xi)


def coordinate_roots():
    return tuple(sorted(
        combinations(range(5), 2),
        key=lambda edge: Q(
            POINTS[edge[1]][1] - POINTS[edge[0]][1],
            POINTS[edge[1]][0] - POINTS[edge[0]][0],
        ),
    ))


def verify_geometry() -> int:
    assert coordinate_roots() == ROOTS
    order = list(range(5))
    word = []
    for left, right in ROOTS:
        a, b = order.index(left), order.index(right)
        assert abs(a - b) == 1
        position = min(a, b)
        word.append(position)
        order[position], order[position + 1] = (
            order[position + 1], order[position]
        )
    assert tuple(word) == WORD
    assert order == [4, 3, 2, 1, 0]
    determinants = [
        abs(determinant(i, j, k))
        for i, j, k in combinations(range(5), 3)
    ]
    assert min(determinants) > 0
    return min(determinants)


def monomial_less(left: tuple[int, int], right: tuple[int, int]) -> bool:
    """Compare 257^a 17^b exactly for the small nonnegative exponents used."""
    return 257 ** left[0] * 17 ** left[1] < 257 ** right[0] * 17 ** right[1]


def monomial_max(left: tuple[int, int], right: tuple[int, int]):
    if monomial_less(left, right):
        return right
    return left


def monomial_add(left: tuple[int, int], right: tuple[int, int]):
    return left[0] + right[0], left[1] + right[1]


def symbolic_profiles():
    # A pair (a,b) means a*log2(257)+b*log2(17).
    weights = ((1, 0), (0, 1), (0, 1), (0, 1), (1, 0))
    cap = [(0, 0)] * 5
    cup = [(0, 0)] * 5
    for i, j in ROOTS:
        cap[i] = monomial_max(cap[i], monomial_add(cap[j], weights[j]))
        cup[j] = monomial_max(cup[j], monomial_add(cup[i], weights[i]))
    rewards = tuple(monomial_add(cap[i], cup[i]) for i in range(5))
    assert rewards == ((0, 2), (2, 0), (2, 0), (1, 2), (0, 3))
    return tuple(cap), tuple(cup), rewards


def verify_integer_root_bounds() -> Q:
    # 17^(-1/4) > 4924/10000.
    assert 4924 ** 4 * 17 < 10000 ** 4
    # 2/sqrt(257) > 1247/10000.
    assert 1247 ** 2 * 257 < 4 * 10000 ** 2
    # 74273^(-1/4) > 605/10000.
    assert 605 ** 4 * 74273 < 10000 ** 4
    # 17^(-3/8) > 3456/10000.
    assert 3456 ** 8 * 17 ** 3 < 10000 ** 8
    lower = Q(4924 + 1247 + 605 + 3456, 10000)
    assert lower == Q(1279, 1250)  # 1.0232
    assert lower > 1
    return lower


def ln_interval(value: Q, terms: int = 100) -> tuple[Q, Q]:
    """Rigorous rational interval for the natural logarithm."""
    if value < 1:
        lower, upper = ln_interval(1 / value, terms)
        return -upper, -lower
    exponent = 0
    while value >= 2:
        value /= 2
        exponent += 1
    z = (value - 1) / (value + 1)

    def atanh_bounds(argument: Q) -> tuple[Q, Q]:
        total = Q(0)
        power = argument
        for index in range(terms):
            total += power / (2 * index + 1)
            power *= argument * argument
        lower = 2 * total
        tail = 2 * power / ((2 * terms + 1) * (1 - argument * argument))
        return lower, lower + tail

    ln2_lower, ln2_upper = atanh_bounds(Q(1, 3))
    value_lower, value_upper = atanh_bounds(z)
    return (
        exponent * ln2_lower + value_lower,
        exponent * ln2_upper + value_upper,
    )


def log2_interval(value: Q) -> tuple[Q, Q]:
    numerator_lower, numerator_upper = ln_interval(value)
    denominator_lower, denominator_upper = ln_interval(Q(2))
    return (
        numerator_lower / denominator_upper,
        numerator_upper / denominator_lower,
    )


def verify_square_margin() -> tuple[Q, Q]:
    # The maximizing displayed bank is position 4: 8^2/2 + 3 log2(17).
    log17 = log2_interval(Q(17))
    log560 = log2_interval(Q(560))
    log5 = log2_interval(Q(5))
    bank = (Q(32) + 3 * log17[0], Q(32) + 3 * log17[1])
    target = (
        Q(1, 2) * log560[0] ** 2 - Q(1, 2) * log5[1] ** 2,
        Q(1, 2) * log560[1] ** 2 - Q(1, 2) * log5[0] ** 2,
    )
    margin = bank[0] - target[1], bank[1] - target[0]
    assert margin[0] > 5
    return margin


def main() -> None:
    determinant_margin = verify_geometry()
    cap, cup, rewards = symbolic_profiles()
    kraft_lower = verify_integer_root_bounds()
    square_margin = verify_square_margin()
    print(
        "PASS: stretchable normalized-Kraft barrier; "
        f"determinant_margin={determinant_margin}; word={WORD}; "
        f"cap={cap}; cup={cup}; rewards={rewards}; "
        f"kraft_lower={kraft_lower}; square_margin_lower={float(square_margin[0]):.9f}"
    )


if __name__ == "__main__":
    main()
