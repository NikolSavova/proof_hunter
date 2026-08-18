#!/usr/bin/env python3
"""Exact certificates for UNIT_LATTICE_RICH_FIBRE_HEIGHT.md."""

from __future__ import annotations

from math import gcd
from random import Random


def radii_are_distinct(r: int, u: int, v: int) -> bool:
    values = {
        (u + i) ** 2 + (v + j) ** 2
        for i in range(r)
        for j in range(r)
    }
    return len(values) == r * r


def exhaustive_minimum(r: int) -> tuple[int, int, int]:
    for height in range(r**2 + 1):
        for u in range(height + 1):
            v = height
            if radii_are_distinct(r, u, v):
                return height, u, v
    raise AssertionError("the separated construction at height r^2 was missed")


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    divisor, x1, y1 = extended_gcd(b, a % b)
    return divisor, y1, x1 - (a // b) * y1


def crt_pair(a: int, m: int, b: int, n: int) -> tuple[int, int]:
    divisor, inverse, _ = extended_gcd(m, n)
    assert (b - a) % divisor == 0
    reduced = n // divisor
    multiplier = ((b - a) // divisor * inverse) % reduced
    modulus = m * reduced
    return (a + m * multiplier) % modulus, modulus


def nearest_positive_odd(numerator: int, denominator: int) -> int:
    centre = numerator // denominator
    candidates = {
        value
        for value in range(max(1, centre - 3), centre + 5)
        if value % 2 == 1
    }
    return min(
        candidates,
        key=lambda value: abs(value * denominator - numerator),
    )


def proof_collision(r: int, u: int, v: int) -> tuple[tuple[int, int], tuple[int, int]]:
    assert 0 <= u <= v
    a_centre = 2 * u + r - 1
    b_centre = 2 * v + r - 1

    e_bound = r * a_centre // (16 * b_centre)
    e = e_bound if e_bound % 2 == 1 else e_bound - 1
    assert e > 0
    d = nearest_positive_odd(e * b_centre, a_centre)
    assert 0 < d < r and 0 < e < r

    left_u = d * (2 * u + d)
    right_u = d * (2 * u + 2 * r - 2 - d)
    left_v = e * (2 * v + e)
    right_v = e * (2 * v + 2 * r - 2 - e)
    lower = max(left_u, left_v)
    upper = min(right_u, right_v)
    assert lower <= upper

    residue, modulus = crt_pair(d * d, 2 * d, e * e, 2 * e)
    value = residue
    if value < lower:
        value += ((lower - value + modulus - 1) // modulus) * modulus
    assert value <= upper

    i_numerator = value // d - 2 * u - d
    j_numerator = value // e - 2 * v - e
    assert value % d == 0 and value % e == 0
    assert i_numerator % 2 == 0 and j_numerator % 2 == 0
    i = i_numerator // 2
    j = j_numerator // 2
    assert 0 <= i < i + d < r
    assert 0 <= j < j + e < r

    first = (u + i + d, v + j)
    second = (u + i, v + j + e)
    assert first != second and first != (-second[0], -second[1])
    assert first[0] ** 2 + first[1] ** 2 == second[0] ** 2 + second[1] ** 2
    return first, second


def main() -> None:
    expected = {
        2: (1, 0, 1),
        3: (2, 0, 2),
        4: (4, 1, 4),
        5: (8, 0, 8),
        6: (11, 6, 11),
        7: (16, 10, 16),
        8: (23, 16, 23),
        9: (29, 21, 29),
        10: (37, 28, 37),
        11: (40, 30, 40),
        12: (47, 36, 47),
        13: (68, 56, 68),
        14: (69, 56, 69),
        15: (86, 72, 86),
    }
    for r, target in expected.items():
        assert exhaustive_minimum(r) == target
    print("small translated patches: PASS")

    exhaustive_certificates = 0
    for r in (10_000, 30_000):
        maximum = r * r // 1_000_000
        for u in range(maximum + 1):
            for v in range(u, maximum + 1):
                proof_collision(r, u, v)
                exhaustive_certificates += 1
    assert exhaustive_certificates == 411_502
    print("medium exhaustive CRT collisions", exhaustive_certificates, "PASS")

    generator = Random(1208)
    certificates = 0
    for r in (100_000, 300_000, 1_000_000):
        maximum = r * r // 1_000_000
        for _ in range(40):
            u = generator.randrange(maximum + 1)
            v = generator.randrange(u, maximum + 1)
            proof_collision(r, u, v)
            certificates += 1
    assert certificates == 120
    print("large CRT collisions", certificates, "PASS")
    print("unit-lattice rich-fibre height: PASS")


if __name__ == "__main__":
    main()
