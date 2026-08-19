#!/usr/bin/env python3
"""Exact checks for DETERMINANT_PRIME_COSTAS_RESONANCE.md."""

from __future__ import annotations

from math import gcd

from analyze_affine_costas_energy import is_distance_sidon, welch
from verify_orthogonal_two_support_gate import difference_set
from verify_seven_incidence_opposite_endpoint_charge import (
    charge_profile,
    overlap_table,
)


Point = tuple[int, int]
Matrix = tuple[int, int, int, int]


ROWS: dict[int, tuple[Matrix, tuple[int, int, int, int, int]]] = {
    11: ((-3, 2, 2, -5), (91, 707, 37, 20, 8_200)),
    13: ((-3, 7, -1, -2), (133, 969, 25, 12, 13_824)),
    17: ((-7, 5, -2, -1), (241, 2_299, 53, 24, 56_184)),
    19: ((-5, -3, 3, -2), (307, 2_927, 81, 52, 194_752)),
    23: ((-5, -2, -1, -5), (463, 4_513, 105, 72, 565_568)),
    29: ((-11, 9, -2, -1), (757, 7_205, 77, 56, 1_431_624)),
    31: ((-9, -13, 1, -2), (871, 9_495, 49, 36, 1_148_936)),
    37: ((-4, -13, 1, -6), (1_261, 13_917, 69, 56, 3_413_488)),
    41: ((-16, -7, -1, -3), (1_561, 17_875, 81, 56, 5_161_456)),
    43: ((-5, 13, -1, -6), (1_723, 19_819, 105, 88, 8_135_424)),
}


CHARGE_ROWS = {
    11: (2_264, 1_880, 4, 3_192),
    13: (3_450, 2_954, 4, 4_642),
    17: (20_014, 15_842, 7, 31_370),
    19: (127_002, 87_224, 10, 242_278),
    23: (498_674, 287_262, 14, 1_258_518),
}


def apply(matrix: Matrix, point: Point) -> Point:
    a, b, c, d = matrix
    x, y = point
    return a * x + b * y, c * x + d * y


def gram(matrix: Matrix) -> tuple[int, int, int]:
    a, b, c, d = matrix
    return a * a + c * c, a * b + c * d, b * b + d * d


def resonance_image(
    prime: int, quadratic: tuple[int, int, int], point: Point
) -> Point | None:
    """Return T^{-1}JT(point) when it is integral."""

    w, u, v = quadratic
    x, y = point
    first = -u * x - v * y
    second = w * x + u * y
    if first % prime or second % prime:
        return None
    return first // prime, second // prime


def verify_general_resonance_index() -> None:
    """Enumerate small matrices and check the exact Smith-index formula."""

    for a in range(-4, 5):
        for b in range(-4, 5):
            for c in range(-4, 5):
                for d in range(-4, 5):
                    determinant = a * d - b * c
                    modulus = abs(determinant)
                    if modulus < 2 or modulus > 20:
                        continue
                    w, u, v = gram((a, b, c, d))
                    common = gcd(gcd(w, abs(u)), v)
                    assert modulus % common == 0
                    predicted = modulus // common
                    kernel = {
                        (x, y)
                        for x in range(modulus)
                        for y in range(modulus)
                        if (-u * x - v * y) % modulus == 0
                        and (w * x + u * y) % modulus == 0
                    }
                    actual_index = modulus * modulus // len(kernel)
                    assert actual_index == predicted, (
                        (a, b, c, d),
                        predicted,
                        actual_index,
                    )


def verify_row(prime: int, matrix: Matrix) -> tuple[int, int, int, int, int]:
    a, b, c, d = matrix
    assert a * d - b * c == prime
    quadratic = gram(matrix)
    w, u, v = quadratic
    assert w * v - u * u == prime * prime
    assert any(value % prime for value in quadratic)

    # B mod p is nonzero singular, so its kernel has exactly p points.
    kernel = {
        (x, y)
        for x in range(prime)
        for y in range(prime)
        if (-u * x - v * y) % prime == 0
        and (w * x + u * y) % prime == 0
    }
    assert len(kernel) == prime

    base = welch(prime)
    transformed = [apply(matrix, point) for point in base]
    assert is_distance_sidon(transformed)

    base_differences = difference_set(base)
    overlaps = overlap_table(base_differences)
    number = len(base_differences)
    support = len(overlaps)
    joint = 0
    adaptive = 0
    tail = 0

    for shift, starts in overlaps.items():
        rotated_pullback = resonance_image(prime, quadratic, shift)
        if rotated_pullback is None:
            continue
        rotated_count = len(overlaps.get(rotated_pullback, ()))
        if not rotated_count:
            continue
        joint += 1
        assert (shift[0] % prime, shift[1] % prime) in kernel
        if (
            shift != (0, 0)
            and len(starts) * number > support
            and rotated_count * number > support
        ):
            adaptive += 1
            tail += len(starts) * rotated_count

    # The box in Proposition 2.1 has at most sixteen lifts per residue.
    assert joint <= 16 * prime
    return number, support, joint, adaptive, tail


def main() -> None:
    verify_general_resonance_index()
    print("general resonance-index formula: PASS")
    for prime, (matrix, expected) in ROWS.items():
        actual = verify_row(prime, matrix)
        assert actual == expected, (prime, actual, expected)
        print(prime, "support profile", actual)

        if prime in CHARGE_ROWS:
            transformed = [apply(matrix, point) for point in welch(prime)]
            profile = charge_profile(difference_set(transformed), adaptive=True)
            assert profile == CHARGE_ROWS[prime]
            print(prime, "charge profile", profile)

    print("DETERMINANT-PRIME COSTAS RESONANCE: PASS")


if __name__ == "__main__":
    main()
