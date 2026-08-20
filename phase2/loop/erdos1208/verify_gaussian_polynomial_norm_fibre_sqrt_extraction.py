#!/usr/bin/env python3
"""Finite audit for GAUSSIAN_POLYNOMIAL_NORM_FIBRE_SQRT_EXTRACTION.md.

The asymptotic fibre estimate uses Dobrowolski's theorem and is proved in
the note.  This script exhaustively checks the exact algebra, carry
separation, tensor-energy identity, finite fibre inequality, and the F_27
square-root certificate.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, product

Point = tuple[int, int]
Word = tuple[int, ...]
DifferenceWord = tuple[Point, ...]

P: tuple[Point, ...] = ((0, 0), (1, 0), (0, 1))


def add(x: Point, y: Point) -> Point:
    return x[0] + y[0], x[1] + y[1]


def sub(x: Point, y: Point) -> Point:
    return x[0] - y[0], x[1] - y[1]


def mul(x: Point, y: Point) -> Point:
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def conjugate(x: Point) -> Point:
    return x[0], -x[1]


def dot(x: Point, y: Point) -> int:
    return x[0] * y[0] + x[1] * y[1]


def norm(x: Point) -> int:
    return dot(x, x)


def difference_data() -> Counter[Point]:
    return Counter(sub(x, y) for x in P for y in P)


DIFFERENCE_COUNTS = difference_data()
DIFFERENCES = tuple(DIFFERENCE_COUNTS)
MAX_DIFFERENCE_NORM = max(norm(value) for value in DIFFERENCES)


def norm_key(difference: DifferenceWord) -> tuple[int, ...]:
    """Coefficients of F(z) conjugate(F)(z), low degree first."""
    r = len(difference)
    coefficients = [0] * (2 * r - 1)
    for first in range(r):
        for second in range(r):
            coefficients[first + second] += dot(difference[first], difference[second])
    return tuple(coefficients)


def embed(word: Word, base: int) -> Point:
    result = (0, 0)
    power = 1
    for digit in word:
        result = add(result, (P[digit][0] * power, P[digit][1] * power))
        power *= base
    return result


def evaluate_key(key: tuple[int, ...], base: int) -> int:
    return sum(coefficient * base**degree for degree, coefficient in enumerate(key))


def polynomial_product(first: tuple[Point, ...], second: tuple[Point, ...]) -> tuple[Point, ...]:
    result = [(0, 0)] * (len(first) + len(second) - 1)
    for i, x in enumerate(first):
        for j, y in enumerate(second):
            result[i + j] = add(result[i + j], mul(x, y))
    return tuple(result)


def polynomial_conjugate(value: tuple[Point, ...]) -> tuple[Point, ...]:
    return tuple(conjugate(coefficient) for coefficient in value)


def verify_triangle_energy() -> None:
    assert DIFFERENCE_COUNTS[(0, 0)] == 3
    assert len(DIFFERENCE_COUNTS) == 7
    assert all(count == 1 for value, count in DIFFERENCE_COUNTS.items() if value != (0, 0))
    energy = sum(count * count for count in DIFFERENCE_COUNTS.values())
    assert energy == 15
    assert energy * energy < 3**5  # exact form of 15 < 3^(5/2)


def verify_carry_and_finite_fibres(r: int = 6) -> tuple[int, int]:
    # The note's bound B > 4 r max |d|^2 + 2 is deliberately conservative.
    base = 4 * r * MAX_DIFFERENCE_NORM + 3
    evaluation_to_key: dict[int, tuple[int, ...]] = {}
    fibre_sizes: Counter[tuple[int, ...]] = Counter()
    weighted_colour_sizes: Counter[tuple[int, ...]] = Counter()
    sum_rho_squared = 0

    for difference in product(DIFFERENCES, repeat=r):
        key = norm_key(difference)
        value = evaluate_key(key, base)
        old_key = evaluation_to_key.setdefault(value, key)
        assert old_key == key
        fibre_sizes[key] += 1
        rho = 1
        for digit in difference:
            rho *= DIFFERENCE_COUNTS[digit]
        weighted_colour_sizes[key] += rho
        sum_rho_squared += rho * rho

    finite_R = max(size for key, size in fibre_sizes.items() if any(key))
    energy = 15
    assert sum_rho_squared == energy**r
    # Includes the zero colour on both sides; this only makes the audit stronger.
    assert sum(size * size for size in weighted_colour_sizes.values()) <= finite_R * energy**r

    # Direct squared-distance evaluation agrees with the polynomial key.
    sample_words = list(product(range(3), repeat=3))
    for first in sample_words:
        for second in sample_words:
            difference = tuple(sub(P[x], P[y]) for x, y in zip(first, second))
            embedded_difference = sub(embed(first, base), embed(second, base))
            assert norm(embedded_difference) == evaluate_key(norm_key(difference), base)

    return finite_R, len(fibre_sizes)


def verify_factor_swapping_identity() -> None:
    # pi=z-(1+i), rho=z-(2+i); replacing pi by conjugate(pi) preserves F bar(F).
    pi = ((-1, -1), (1, 0))
    rho = ((-2, -1), (1, 0))
    first = polynomial_product(pi, rho)
    second = polynomial_product(polynomial_conjugate(pi), rho)
    first_norm = polynomial_product(first, polynomial_conjugate(first))
    second_norm = polynomial_product(second, polynomial_conjugate(second))
    assert first != second
    assert first_norm == second_norm


def field_multiply(first: tuple[int, int, int], second: tuple[int, int, int]) -> tuple[int, int, int]:
    """Multiply in F_3[t]/(t^3+2t+1), where t^3=t+2."""
    raw = [0] * 5
    for i, x in enumerate(first):
        for j, y in enumerate(second):
            raw[i + j] = (raw[i + j] + x * y) % 3
    for degree in (4, 3):
        coefficient = raw[degree] % 3
        raw[degree] = 0
        raw[degree - 2] = (raw[degree - 2] + coefficient) % 3
        raw[degree - 3] = (raw[degree - 3] + 2 * coefficient) % 3
    return tuple(raw[:3])  # type: ignore[return-value]


def field27_code() -> list[Word]:
    code: list[Word] = []
    for value in product(range(3), repeat=3):
        square = field_multiply(value, value)
        code.append(tuple(value + square))
    return code


def verify_f27_square_root_certificate() -> int:
    code = field27_code()
    assert len(code) == 27
    assert len(set(code)) == 27
    colours: set[tuple[int, ...]] = set()
    for first, second in combinations(code, 2):
        difference = tuple(sub(P[x], P[y]) for x, y in zip(first, second))
        key = norm_key(difference)
        assert key not in colours
        colours.add(key)
    assert len(colours) == 27 * 26 // 2

    base = 4 * 6 * MAX_DIFFERENCE_NORM + 3
    integer_distances: set[int] = set()
    for first, second in combinations(code, 2):
        distance = norm(sub(embed(first, base), embed(second, base)))
        assert distance not in integer_distances
        integer_distances.add(distance)
    assert len(integer_distances) == len(colours)
    return len(colours)


def verify_local_colour_degree(r: int = 4) -> int:
    words = list(product(range(3), repeat=r))
    fibres: Counter[tuple[int, ...]] = Counter()
    for difference in product(DIFFERENCES, repeat=r):
        fibres[norm_key(difference)] += 1
    finite_R = max(size for key, size in fibres.items() if any(key))

    maximum_degree = 0
    for source in words:
        degrees: Counter[tuple[int, ...]] = Counter()
        for target in words:
            if source == target:
                continue
            difference = tuple(sub(P[x], P[y]) for x, y in zip(source, target))
            degrees[norm_key(difference)] += 1
        maximum_degree = max(maximum_degree, max(degrees.values()))
        assert max(degrees.values()) <= finite_R
    return maximum_degree


def main() -> None:
    verify_triangle_energy()
    verify_factor_swapping_identity()
    finite_R, colour_count = verify_carry_and_finite_fibres()
    certificate_colours = verify_f27_square_root_certificate()
    maximum_degree = verify_local_colour_degree()
    print(
        "Gaussian polynomial norm-fibre square-root extraction: PASS",
        f"r=6 finite_R={finite_R}",
        f"norm_colours={colour_count}",
        f"F27_certificate_colours={certificate_colours}",
        f"r=4_max_colour_degree={maximum_degree}",
    )


if __name__ == "__main__":
    main()
