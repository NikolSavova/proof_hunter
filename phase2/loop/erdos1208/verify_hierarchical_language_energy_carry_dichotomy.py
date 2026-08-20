#!/usr/bin/env python3
"""Finite checks for HIERARCHICAL_LANGUAGE_ENERGY_CARRY_DICHOTOMY.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product


Gaussian = tuple[int, int]
Word = tuple[Gaussian, ...]


def gsub(a: Gaussian, b: Gaussian) -> Gaussian:
    return a[0] - b[0], a[1] - b[1]


def gmul_conj(a: Gaussian, b: Gaussian) -> Gaussian:
    # a * conjugate(b)
    return a[0] * b[0] + a[1] * b[1], a[1] * b[0] - a[0] * b[1]


def word_difference(a: Word, b: Word) -> Word:
    return tuple(gsub(x, y) for x, y in zip(a, b))


def norm_polynomial(d: Word) -> tuple[int, ...]:
    out = [(0, 0) for _ in range(2 * len(d) - 1)]
    for i, a in enumerate(d):
        for j, b in enumerate(d):
            value = gmul_conj(a, b)
            old = out[i + j]
            out[i + j] = old[0] + value[0], old[1] + value[1]
    assert all(imaginary == 0 for _, imaginary in out)
    return tuple(real for real, _ in out)


def evaluate(coefficients: tuple[int, ...], base: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = value * base + coefficient
    return value


def language_statistics(language: list[Word]):
    rho = Counter(
        word_difference(x, y)
        for x in language
        for y in language
    )
    energy = sum(value * value for value in rho.values())

    norm_fibres: dict[tuple[int, ...], set[Word]] = defaultdict(set)
    for difference in rho:
        if any(digit != (0, 0) for digit in difference):
            norm_fibres[norm_polynomial(difference)].add(difference)
    max_fibre = max(map(len, norm_fibres.values()), default=1)

    color_multiplicity = {
        color: sum(rho[difference] for difference in differences)
        for color, differences in norm_fibres.items()
    }
    lhs = sum(value * value for value in color_multiplicity.values())
    assert lhs <= max_fibre * energy

    maximum_color_degree = 0
    for x in language:
        degrees = Counter(
            norm_polynomial(word_difference(x, y))
            for y in language
            if y != x
        )
        maximum_color_degree = max(
            maximum_color_degree, max(degrees.values(), default=0)
        )
    assert maximum_color_degree <= max_fibre
    return energy, max_fibre, lhs, maximum_color_degree


def check_nonproduct_languages() -> None:
    triangle = [(0, 0), (1, 0), (0, 1)]
    full = list(product(triangle, repeat=4))
    languages = [
        [word for word in full if sum(x + y for x, y in word) % 2 == 0],
        [word for word in full if word[0] != word[-1]],
        [word for word in full if sum(x for x, _ in word) <= 2],
    ]
    for language in languages:
        energy, fibre, lhs, local = language_statistics(language)
        assert energy > 0 and fibre > 0 and lhs > 0 and local > 0


def check_coefficient_separation_and_carries() -> None:
    digits = [(0, 0), (1, 0), (0, 1)]
    words = list(product(digits, repeat=3))
    differences = {
        word_difference(x, y)
        for x in words
        for y in words
        if x != y
    }
    norm_polynomials = {d: norm_polynomial(d) for d in differences}

    # At a sufficiently large base, evaluation is injective on the finite
    # coefficient set, exactly as in the leading-coefficient proof.
    large_base = 100
    by_value: dict[int, set[tuple[int, ...]]] = defaultdict(set)
    for polynomial in norm_polynomials.values():
        by_value[evaluate(polynomial, large_base)].add(polynomial)
    assert max(map(len, by_value.values())) == 1

    # Small bases genuinely merge different norm polynomials.
    small_base = 2
    by_small_value: dict[int, set[tuple[int, ...]]] = defaultdict(set)
    for polynomial in norm_polynomials.values():
        by_small_value[evaluate(polynomial, small_base)].add(polynomial)
    carry_ambiguity = max(map(len, by_small_value.values()))
    assert carry_ambiguity > 1

    # Scalar fibres are unions of at most kappa polynomial fibres.
    polynomial_fibre = Counter(norm_polynomials.values())
    scalar_fibre = Counter(
        evaluate(polynomial, small_base)
        for polynomial in norm_polynomials.values()
    )
    assert max(scalar_fibre.values()) <= carry_ambiguity * max(
        polynomial_fibre.values()
    )

    # Verify the carry recurrence for every equality Q(2)=Q'(2).
    polynomials = sorted(set(norm_polynomials.values()))
    for left in polynomials:
        for right in polynomials:
            if evaluate(left, small_base) != evaluate(right, small_base):
                continue
            h = [a - b for a, b in zip(left, right)]
            carry = 0
            for coefficient in h:
                assert (coefficient + carry) % small_base == 0
                carry = (coefficient + carry) // small_base
            assert carry == 0


def check_complete_digit_grid() -> None:
    for base, depth in ((2, 3), (3, 2)):
        digits = [(a, b) for a in range(base) for b in range(base)]
        images = set()
        for word in product(digits, repeat=depth):
            real = sum((base**j) * digit[0] for j, digit in enumerate(word))
            imag = sum((base**j) * digit[1] for j, digit in enumerate(word))
            images.add((real, imag))
        side = base**depth
        expected = set(product(range(side), repeat=2))
        assert images == expected


def main() -> None:
    check_nonproduct_languages()
    check_coefficient_separation_and_carries()
    check_complete_digit_grid()
    print("PASS: language energy, norm fibres, carries, and grid identity")


if __name__ == "__main__":
    main()
