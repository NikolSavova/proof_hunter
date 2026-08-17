#!/usr/bin/env python3
"""Exact tower-data checks for the rank-22 placewise Erdos 1208 bound."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

from verify_placewise_rank20 import gf2_rank, is_prime_u64


ALPHA = Fraction(249, 500)  # 0.498
W0 = Fraction(68267, 10)  # 6826.7
RAMIFIED_PRIMES = [
    3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
]
RADICANDS = [
    5, 13, 17, 29, 37, 41, 53, 61, 73, 89,
    21, 33, 57, 69, 93, 129, 141, 177, 201, 213, 237, 249,
]
SPLIT_PRIMES = [
    int(line)
    for line in Path(__file__).with_name("rank22_split_primes.txt").read_text().split()
]


def square_class_vector(a: int) -> int:
    vector, remainder = 0, a
    for i, p in enumerate(RAMIFIED_PRIMES):
        while remainder % p == 0:
            vector ^= 1 << i
            remainder //= p
    assert remainder == 1
    return vector


def exact_checks() -> int:
    assert len(RAMIFIED_PRIMES) == 23
    assert len(RADICANDS) == 22
    assert all(is_prime_u64(p) for p in RAMIFIED_PRIMES)
    for a in RADICANDS:
        assert a > 0 and a % 4 == 1
        assert all(a % (p * p) for p in RAMIFIED_PRIMES)
    assert gf2_rank([square_class_vector(a) for a in RADICANDS]) == 22

    assert len(SPLIT_PRIMES) == len(set(SPLIT_PRIMES)) == 98
    for q in SPLIT_PRIMES:
        assert q < 2**64 and is_prime_u64(q) and q % 4 == 1
        for a in RADICANDS:
            assert pow(a, (q - 1) // 2, q) == 1

    generator_rank = 22
    relation_rank_bound = generator_rank + len(SPLIT_PRIMES)
    assert relation_rank_bound == 120
    assert 4 * relation_rank_bound < generator_rank**2

    discriminant_bound = 1
    for p in RAMIFIED_PRIMES:
        discriminant_bound *= p
    assert discriminant_bound == 11884370948172775385325268800679155
    return discriminant_bound


def main() -> None:
    discriminant_bound = exact_checks()
    print("split primes / residue checks:", len(SPLIT_PRIMES), 98 * 22)
    print("generator/relation bound:", 22, 120)
    print("D =", discriminant_bound)
    print("target alpha =", ALPHA.numerator / ALPHA.denominator)
    print("exact rank-22 tower checks: PASS")


if __name__ == "__main__":
    main()
