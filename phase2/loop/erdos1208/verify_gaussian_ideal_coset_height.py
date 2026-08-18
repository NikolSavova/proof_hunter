#!/usr/bin/env python3
"""Exact certificates for GAUSSIAN_IDEAL_COSET_HEIGHT.md."""

from __future__ import annotations

from fractions import Fraction
from math import gcd


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for prime in small:
        if value % prime == 0:
            return value == prime
    exponent = value - 1
    power = 0
    while exponent % 2 == 0:
        exponent //= 2
        power += 1
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % value == 0:
            continue
        witness = pow(base, exponent, value)
        if witness in (1, value - 1):
            continue
        for _ in range(power - 1):
            witness = witness * witness % value
            if witness == value - 1:
                break
        else:
            return False
    return True


def first_prime_at_least(lower: int) -> int:
    candidate = max(3, lower | 1)
    while not is_prime(candidate):
        candidate += 2
    return candidate


def ceil_fraction(value: Fraction) -> int:
    return -(-value.numerator // value.denominator)


def distinct_prime_factors(value: int) -> list[int]:
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1 if divisor == 2 else 2
    if value > 1:
        factors.append(value)
    return factors


def crt_coprime(left: int, left_modulus: int, right: int, right_modulus: int) -> tuple[int, int]:
    assert gcd(left_modulus, right_modulus) == 1
    if left_modulus == 1:
        return right % right_modulus, right_modulus
    if right_modulus == 1:
        return left % left_modulus, left_modulus
    step = (right - left) * pow(left_modulus, -1, right_modulus)
    step %= right_modulus
    modulus = left_modulus * right_modulus
    return (left + left_modulus * step) % modulus, modulus


def crt_general(left: int, left_modulus: int, right: int, right_modulus: int) -> tuple[int, int]:
    common = gcd(left_modulus, right_modulus)
    assert (right - left) % common == 0
    reduced_left = left_modulus // common
    reduced_right = right_modulus // common
    step = ((right - left) // common) * pow(reduced_left, -1, reduced_right)
    step %= reduced_right
    period = left_modulus * reduced_right
    return (left + left_modulus * step) % period, period


def nearest_in_class(target: Fraction, residue: int, modulus: int) -> int:
    quotient = (target - residue) / modulus
    centre = quotient.numerator // quotient.denominator
    choices = [residue + modulus * (centre + shift) for shift in range(-3, 4)]
    return min(choices, key=lambda item: abs(Fraction(item) - target))


def reduced_certificate(h: int, p: int, s: int, side: int) -> dict[str, int]:
    assert h >= 2 and gcd(gcd(p, s), h) == 1
    assert 0 <= Fraction(p, h) <= Fraction(s, h)
    first_centre_scaled = Fraction(2 * p, h) + side - 1
    second_centre_scaled = Fraction(2 * s, h) + side - 1
    alpha = second_centre_scaled / first_centre_scaled
    assert Fraction(h) * second_centre_scaled / (side * side) <= Fraction(1, 100_000_000)

    factor_a = gcd(p, h)
    factor_b = h // factor_a
    x_lower = Fraction(side, 128) / (alpha * factor_a)
    prime_e = first_prime_at_least(ceil_fraction(x_lower))
    assert x_lower <= prime_e <= 4 * x_lower
    assert prime_e > factor_b
    primitive_e = factor_a * prime_e

    if factor_b == 1:
        base = 0
    else:
        base = s * prime_e * pow(p // factor_a, -1, factor_b) % factor_b
    exclusive = 1
    for prime in distinct_prime_factors(factor_a):
        if factor_b % prime != 0:
            exclusive *= prime
    residue, modulus = crt_coprime(base, factor_b, 1 % exclusive, exclusive)
    assert modulus == factor_b * exclusive <= h

    target = alpha * primitive_e
    primitive_d = nearest_in_class(target, residue, modulus)
    candidates = [primitive_d + shift * modulus for shift in range(-2, 3)]
    candidates = [
        value for value in candidates
        if value > 0 and gcd(value, primitive_e) == 1
    ]
    assert candidates
    primitive_d = min(candidates, key=lambda value: abs(Fraction(value) - target))
    assert abs(Fraction(primitive_d) - target) <= 2 * h
    assert (p * primitive_d - s * primitive_e) % h == 0
    assert gcd(primitive_d, primitive_e) == 1

    gap_d = 2 * primitive_d
    gap_e = 2 * primitive_e
    assert gap_d < side and gap_e < side

    first_centre = gap_d * (2 * p + h * (side - 1))
    first_halfwidth = h * gap_d * (side - 1 - gap_d)
    second_centre = gap_e * (2 * s + h * (side - 1))
    second_halfwidth = h * gap_e * (side - 1 - gap_e)
    overlap_left = max(first_centre - first_halfwidth, second_centre - second_halfwidth)
    overlap_right = min(first_centre + first_halfwidth, second_centre + second_halfwidth)

    first_modulus = 2 * h * gap_d
    second_modulus = 2 * h * gap_e
    first_residue = gap_d * (2 * p + h * gap_d)
    second_residue = gap_e * (2 * s + h * gap_e)
    common_residue, period = crt_general(
        first_residue,
        first_modulus,
        second_residue,
        second_modulus,
    )
    assert gcd(first_modulus, second_modulus) == 4 * h
    assert period == h * gap_d * gap_e
    assert overlap_right - overlap_left > period
    common_value = common_residue
    if common_value < overlap_left:
        common_value += ceil_fraction(Fraction(overlap_left - common_value, period)) * period
    assert overlap_left <= common_value <= overlap_right

    first_numerator = common_value - gap_d * (2 * p + h * gap_d)
    second_numerator = common_value - gap_e * (2 * s + h * gap_e)
    assert first_numerator % first_modulus == 0
    assert second_numerator % second_modulus == 0
    index_i = first_numerator // first_modulus
    index_j = second_numerator // second_modulus
    assert 0 <= index_i <= side - 1 - gap_d
    assert 0 <= index_j <= side - 1 - gap_e

    left_norm = (p + h * (index_i + gap_d)) ** 2 + (s + h * index_j) ** 2
    right_norm = (p + h * index_i) ** 2 + (s + h * (index_j + gap_e)) ** 2
    assert left_norm == right_norm
    return {"i": index_i, "j": index_j, "d": gap_d, "e": gap_e}


def physical_certificate(z: tuple[int, int], remainder: tuple[int, int], aspect: int) -> tuple[int, int]:
    x, y = z
    q = x * x + y * y
    rem_x, rem_y = remainder
    assert q >= 2
    shift_first = 1000
    side = 200_000_000 * q
    shift_second = shift_first + aspect * side // (1000 * q)

    # t=z(shift_first+i shift_second)+remainder.
    tx = x * shift_first - y * shift_second + rem_x
    ty = y * shift_first + x * shift_second + rem_y
    numerator_p = tx * x + ty * y
    numerator_s = -tx * y + ty * x
    common = gcd(gcd(abs(numerator_p), abs(numerator_s)), q)
    h = q // common
    p = numerator_p // common
    s = numerator_s // common
    assert h >= 2
    assert 0 <= Fraction(p, h) <= Fraction(s, h)
    data = reduced_certificate(h, p, s, side)

    def point(i: int, j: int) -> tuple[int, int]:
        return tx + x * i - y * j, ty + y * i + x * j

    left = point(data["i"] + data["d"], data["j"])
    right = point(data["i"], data["j"] + data["e"])
    assert left != right and left != (-right[0], -right[1])
    assert left[0] * left[0] + left[1] * left[1] == right[0] * right[0] + right[1] * right[1]
    return q, h


def main() -> None:
    cases = [
        ((3, 0), (1, 1)),       # inert step; neither raw numerator is a unit mod q=9
        ((5, 0), (1, 2)),       # odd prime power, q=25
        ((4, 7), (1, 1)),       # split composite norm q=65
        ((2, 2), (1, 0)),       # power of 1+i, q=8
        ((1, 3), (1, 0)),       # mixed even norm q=10
        ((1, 7), (1, 1)),       # even composite norm q=50
        ((6, 3), (1, 2)),       # nonprimitive Gaussian step, q=45
        ((5, 5), (2, 1)),       # mixed 2-adic/rational content, q=50
        ((6, 7), (3, 7)),       # split composite norm q=85
    ]
    reductions: set[tuple[int, int]] = set()
    checks = 0
    for z, remainder in cases:
        for aspect in (1, 3, 9):
            reductions.add(physical_certificate(z, remainder, aspect))
            checks += 1
    # Kernel cases in which the two numerator gcds are supported on
    # different prime factors of the reduced denominator.
    reduced_cases = [
        (21, 3, 7),
        (30, 6, 25),
        (72, 8, 27),
        (105, 15, 49),
    ]
    for h, p, s in reduced_cases:
        assert gcd(p, h) > 1 and gcd(s, h) > 1
        reduced_certificate(h, p, s, 200_000_000 * h)
        checks += 1
    print("arbitrary Gaussian-ideal CRT certificates", checks, "PASS")
    print("norm/reduced-denominator pairs", sorted(reductions))
    print("Gaussian-ideal critical height: PASS")


if __name__ == "__main__":
    main()
