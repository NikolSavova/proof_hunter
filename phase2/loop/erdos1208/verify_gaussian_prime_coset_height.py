#!/usr/bin/env python3
"""Exact certificates for GAUSSIAN_PRIME_COSET_HEIGHT.md."""

from __future__ import annotations

from fractions import Fraction
from math import gcd, isqrt


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, isqrt(value) + 1))


def first_prime_at_least(lower: int, forbidden: int) -> int:
    candidate = max(3, lower | 1)
    while True:
        if candidate != forbidden and is_prime(candidate):
            return candidate
        candidate += 2


def ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def nearest_in_class(target: Fraction, residue: int, modulus: int) -> int:
    quotient = (target - residue) / modulus
    centre = quotient.numerator // quotient.denominator
    candidates = [residue + modulus * (centre + shift) for shift in range(-2, 4)]
    return min(candidates, key=lambda item: abs(Fraction(item) - target))


def crt(left: int, left_modulus: int, right: int, right_modulus: int) -> tuple[int, int]:
    common = gcd(left_modulus, right_modulus)
    assert (right - left) % common == 0
    reduced_left = left_modulus // common
    reduced_right = right_modulus // common
    step = ((right - left) // common) * pow(reduced_left, -1, reduced_right)
    step %= reduced_right
    period = left_modulus * reduced_right
    return (left + left_modulus * step) % period, period


def certificate(q: int, p: int, s: int, side: int) -> dict[str, int]:
    assert is_prime(q) and q % 2 == 1
    assert p % q and (p * p + s * s) % q == 0
    assert 0 <= Fraction(p, q) <= Fraction(s, q)

    centre_first = Fraction(2 * p, q) + side - 1
    centre_second = Fraction(2 * s, q) + side - 1
    alpha = centre_second / centre_first
    eta = Fraction(q) * centre_second / (side * side)
    assert eta <= Fraction(1, 1_000_000)

    lower = ceil_fraction(Fraction(side, 64) / alpha)
    e = first_prime_at_least(lower, q)
    assert e <= Fraction(side, 16) / alpha

    slope = (s * pow(p, -1, q)) % q
    base = nearest_in_class(alpha * e, (slope * e) % q, q)
    candidates = [
        base + shift * q
        for shift in range(-4, 5)
        if base + shift * q > 0
        and (base + shift * q) % 2 == 1
        and gcd(base + shift * q, e) == 1
    ]
    assert candidates
    d = min(candidates, key=lambda item: abs(Fraction(item) - alpha * e))
    assert abs(Fraction(d) - alpha * e) <= 5 * q
    assert d < side and e < side

    first_centre = d * (2 * p + q * (side - 1))
    first_halfwidth = q * d * (side - 1 - d)
    second_centre = e * (2 * s + q * (side - 1))
    second_halfwidth = q * e * (side - 1 - e)
    lower_overlap = max(
        first_centre - first_halfwidth,
        second_centre - second_halfwidth,
    )
    upper_overlap = min(
        first_centre + first_halfwidth,
        second_centre + second_halfwidth,
    )

    first_modulus = 2 * q * d
    second_modulus = 2 * q * e
    first_residue = d * (2 * p + q * d)
    second_residue = e * (2 * s + q * e)
    residue, period = crt(
        first_residue,
        first_modulus,
        second_residue,
        second_modulus,
    )
    assert period == 2 * q * d * e
    assert upper_overlap - lower_overlap > period
    common_value = residue
    if common_value < lower_overlap:
        common_value += ceil_fraction(Fraction(lower_overlap - common_value, period)) * period
    assert lower_overlap <= common_value <= upper_overlap

    first_numerator = common_value - d * (2 * p + q * d)
    second_numerator = common_value - e * (2 * s + q * e)
    assert first_numerator % first_modulus == 0
    assert second_numerator % second_modulus == 0
    i = first_numerator // first_modulus
    j = second_numerator // second_modulus
    assert 0 <= i <= side - 1 - d
    assert 0 <= j <= side - 1 - e

    left_scaled_norm = (p + q * (i + d)) ** 2 + (s + q * j) ** 2
    right_scaled_norm = (p + q * i) ** 2 + (s + q * (j + e)) ** 2
    assert left_scaled_norm == right_scaled_norm
    return {"d": d, "e": e, "i": i, "j": j}


def physical_check(z: tuple[int, int], lattice_shift: tuple[int, int], side: int) -> None:
    a, b = z
    q = a * a + b * b
    assert is_prime(q)
    shift_i, shift_j = lattice_shift
    # t/z = shift_i + i shift_j + 1/z.
    p = q * shift_i + a
    s = q * shift_j - b
    assert 0 <= Fraction(p, q) <= Fraction(s, q)
    data = certificate(q, p, s, side)

    # Recover the integral translate t=(p z+s iz)/q.
    tx_numerator = a * p - b * s
    ty_numerator = b * p + a * s
    assert tx_numerator % q == 0 and ty_numerator % q == 0
    tx = tx_numerator // q
    ty = ty_numerator // q

    def point(i: int, j: int) -> tuple[int, int]:
        return tx + a * i - b * j, ty + b * i + a * j

    left = point(data["i"] + data["d"], data["j"])
    right = point(data["i"], data["j"] + data["e"])
    assert left != right and left != (-right[0], -right[1])
    assert left[0] ** 2 + left[1] ** 2 == right[0] ** 2 + right[1] ** 2


def main() -> None:
    gaussian_primes = [
        (1, 2),   # norm 5
        (2, 3),   # norm 13
        (1, 4),   # norm 17
        (2, 5),   # norm 29
        (1, 6),   # norm 37
        (4, 5),   # norm 41
        (2, 7),   # norm 53
        (1, 8),   # norm 65 is not prime and is intentionally omitted
    ]
    gaussian_primes = [z for z in gaussian_primes if is_prime(z[0] ** 2 + z[1] ** 2)]
    assert len(gaussian_primes) == 7

    checks = 0
    for z in gaussian_primes:
        q = z[0] ** 2 + z[1] ** 2
        for aspect in (1, 3, 9):
            side = 200_000_000 * q
            first_shift = 1000
            second_shift = first_shift + aspect * side // (1000 * q)
            physical_check(z, (first_shift, second_shift), side)
            checks += 1
    print("prime Gaussian coset CRT certificates", checks, "PASS")
    print("Gaussian-prime critical height: PASS")


if __name__ == "__main__":
    main()
