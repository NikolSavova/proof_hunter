#!/usr/bin/env python3
"""Exact checks for BALANCED_COSTAS_SEPARATOR_EXACT_CUTOFF.md."""

from __future__ import annotations

from itertools import combinations
from math import gcd
import sys

sys.path.insert(0, "phase2/loop/erdos1208")

from analyze_affine_costas_energy import welch  # noqa: E402

Point = tuple[int, int]
Matrix = tuple[int, int, int, int]
Gram = tuple[int, int, int]

PRIME = 263
EMPTY_RADIUS = 66
WITNESS: Matrix = (-67, -45, 52, 31)
EXPECTED_GRAMS = 9_840


def extended_gcd(first: int, second: int) -> tuple[int, int, int]:
    """Return positive gcd and Bezout coefficients."""
    if second == 0:
        if first > 0:
            return first, 1, 0
        if first < 0:
            return -first, -1, 0
        return 0, 0, 0
    common, x, y = extended_gcd(second, first % second)
    return common, y, x - (first // second) * y


def matrix_determinant(matrix: Matrix) -> int:
    a, b, c, d = matrix
    return a * d - b * c


def gram(matrix: Matrix) -> Gram:
    a, b, c, d = matrix
    return a * a + c * c, a * b + c * d, b * b + d * d


def ceiling_divide(numerator: int, denominator: int) -> int:
    assert denominator > 0
    return -((-numerator) // denominator)


def parameter_interval(
    coefficient: int, offset: int, radius: int
) -> tuple[int, int] | None:
    """Integers t for which |offset+coefficient*t|<=radius."""
    if coefficient == 0:
        return (-10**30, 10**30) if abs(offset) <= radius else None
    if coefficient < 0:
        coefficient = -coefficient
        offset = -offset
    lower = ceiling_divide(-radius - offset, coefficient)
    upper = (radius - offset) // coefficient
    return (lower, upper) if lower <= upper else None


def determinant_prime_grams(prime: int, radius: int) -> set[Gram]:
    """Enumerate every T^T T with det(T)=prime and entry height <=radius."""
    assert radius < prime
    forms: set[Gram] = set()
    for a in range(-radius, radius + 1):
        for c in range(-radius, radius + 1):
            if gcd(a, c) != 1:
                continue
            common, x, y = extended_gcd(a, c)
            assert common == 1 and a * x + c * y == 1

            # a*d-c*b=prime, hence one solution is b=-prime*y,d=prime*x.
            b_zero = -prime * y
            d_zero = prime * x
            b_interval = parameter_interval(a, b_zero, radius)
            d_interval = parameter_interval(c, d_zero, radius)
            if b_interval is None or d_interval is None:
                continue
            lower = max(b_interval[0], d_interval[0])
            upper = min(b_interval[1], d_interval[1])
            for parameter in range(lower, upper + 1):
                b = b_zero + a * parameter
                d = d_zero + c * parameter
                if max(abs(b), abs(d)) > radius:
                    continue
                matrix = (a, b, c, d)
                assert matrix_determinant(matrix) == prime
                forms.add(gram(matrix))
    return forms


def canonical_edges(points: list[Point]) -> list[Point]:
    edges: list[Point] = []
    seen: set[Point] = set()
    for first, second in combinations(points, 2):
        vector = (second[0] - first[0], second[1] - first[1])
        canonical = min(vector, (-vector[0], -vector[1]))
        assert canonical not in seen
        seen.add(canonical)
        edges.append(canonical)
    return edges


def is_separating(form: Gram, edges: list[Point]) -> bool:
    first, mixed, second = form
    norms: set[int] = set()
    for x, y in edges:
        norm = first * x * x + 2 * mixed * x * y + second * y * y
        if norm in norms:
            return False
        norms.add(norm)
    return True


def main() -> None:
    points = welch(PRIME)
    edges = canonical_edges(points)
    assert len(points) == 262
    assert len(edges) == 34_191

    forms = determinant_prime_grams(PRIME, EMPTY_RADIUS)
    assert len(forms) == EXPECTED_GRAMS
    assert not any(is_separating(form, edges) for form in forms)

    assert matrix_determinant(WITNESS) == PRIME
    assert max(map(abs, WITNESS)) == EMPTY_RADIUS + 1
    assert is_separating(gram(WITNESS), edges)

    print(
        "balanced Costas exact cutoff: PASS",
        f"p={PRIME}",
        f"nonseparating Gram forms through {EMPTY_RADIUS}={len(forms)}",
        f"minimum separating radius={EMPTY_RADIUS + 1}",
    )


if __name__ == "__main__":
    main()
