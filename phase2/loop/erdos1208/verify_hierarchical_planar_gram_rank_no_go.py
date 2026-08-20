#!/usr/bin/env python3
"""Exact checks for HIERARCHICAL_PLANAR_GRAM_RANK_NO_GO.md."""

from __future__ import annotations

from itertools import combinations, product

Point = tuple[int, int]
Word = tuple[int, ...]

Q = 5
NON_SQUARE = 2
DIRECTIONS: tuple[Point, ...] = ((1, 1), (1, 2), (1, 3), (1, 4))
EXPONENTS = (1, 3, 9, 27)
BASE = 2_003


def dot(first: Point, second: Point) -> int:
    return first[0] * second[0] + first[1] * second[1]


def add(first: Point, second: Point) -> Point:
    return first[0] + second[0], first[1] + second[1]


def sub(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def scale(multiplier: int, point: Point) -> Point:
    return multiplier * point[0], multiplier * point[1]


def embed(word: Word) -> Point:
    value = (0, 0)
    for digit, direction, exponent in zip(word, DIRECTIONS, EXPONENTS):
        value = add(value, scale(digit * BASE**exponent, direction))
    return value


def squared_norm(point: Point) -> int:
    return dot(point, point)


def coefficient_key(difference: Word) -> tuple[tuple[int, int], ...]:
    coefficients: dict[int, int] = {}
    for first in range(len(difference)):
        coefficients[2 * EXPONENTS[first]] = (
            difference[first] ** 2 * dot(DIRECTIONS[first], DIRECTIONS[first])
        )
        for second in range(first + 1, len(difference)):
            coefficients[EXPONENTS[first] + EXPONENTS[second]] = (
                2
                * difference[first]
                * difference[second]
                * dot(DIRECTIONS[first], DIRECTIONS[second])
            )
    return tuple(sorted(coefficients.items()))


def field_square(value: tuple[int, int]) -> tuple[int, int]:
    first, second = value
    return (
        (first * first + NON_SQUARE * second * second) % Q,
        (2 * first * second) % Q,
    )


def sidon_code() -> list[Word]:
    return [
        (first, second, *field_square((first, second)))
        for first in range(Q)
        for second in range(Q)
    ]


def canonical(difference: Word) -> Word:
    negative = tuple(-value for value in difference)
    return min(difference, negative)


def verify_pair_sum_separation() -> None:
    sums = [
        EXPONENTS[first] + EXPONENTS[second]
        for first in range(len(EXPONENTS))
        for second in range(first, len(EXPONENTS))
    ]
    assert len(sums) == len(set(sums))
    assert all(dot(first, second) != 0 for first in DIRECTIONS for second in DIRECTIONS)


def verify_expansion_and_sign_rigidity() -> None:
    keys: dict[tuple[tuple[int, int], ...], list[Word]] = {}
    norms_to_keys: dict[int, tuple[tuple[int, int], ...]] = {}
    for difference in product(range(-(Q - 1), Q), repeat=len(EXPONENTS)):
        direct = squared_norm(
            sub(embed(tuple(max(value, 0) for value in difference)),
                embed(tuple(max(-value, 0) for value in difference)))
        )
        key = coefficient_key(difference)
        expanded = sum(coefficient * BASE**exponent for exponent, coefficient in key)
        assert direct == expanded
        previous = norms_to_keys.setdefault(direct, key)
        assert previous == key
        keys.setdefault(key, []).append(difference)

    zero = (0,) * len(EXPONENTS)
    for fibre in keys.values():
        if fibre == [zero]:
            continue
        assert len(fibre) == 2
        assert fibre[1] == tuple(-value for value in fibre[0])
    assert len(keys) == (9**4 + 1) // 2
    assert len(norms_to_keys) == len(keys)


def verify_cross_term_split() -> None:
    first = ((1, 0), (1, 1))
    second = ((0, 1), (1, -1))
    assert [dot(value, value) for value in first] == [1, 2]
    assert [dot(value, value) for value in second] == [1, 2]
    assert dot(*first) == 1
    assert dot(*second) == -1


def verify_code() -> None:
    code = sidon_code()
    assert len(code) == Q**2

    differences: set[Word] = set()
    for source, target in combinations(code, 2):
        difference = canonical(tuple(a - b for a, b in zip(target, source)))
        assert difference not in differences
        differences.add(difference)

    points = [embed(word) for word in code]
    assert len(points) == len(set(points))
    distances: set[int] = set()
    for source, target in combinations(points, 2):
        distance = squared_norm(sub(target, source))
        assert distance not in distances
        distances.add(distance)
    assert len(distances) == len(code) * (len(code) - 1) // 2


def verify_zero_cylinder() -> None:
    first = (0, 0, 0, 0)
    second = (1, 0, 0, 0)
    third = (0, 1, 2, 3)
    fourth = (1, 1, 2, 3)
    assert sub(embed(second), embed(first)) == sub(embed(fourth), embed(third))
    assert {first, second} != {third, fourth}


def main() -> None:
    verify_pair_sum_separation()
    verify_expansion_and_sign_rigidity()
    verify_cross_term_split()
    verify_code()
    verify_zero_cylinder()
    print(
        "hierarchical planar Gram-rank no-go: PASS",
        f"ambient={Q ** len(EXPONENTS)}",
        f"distance-Sidon subcode={Q**2}",
        f"Gram colours={(9**4 + 1) // 2}",
    )


if __name__ == "__main__":
    main()
