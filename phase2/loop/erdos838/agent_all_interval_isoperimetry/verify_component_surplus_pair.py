#!/usr/bin/env python3
"""Exact arithmetic checks for COMPONENT_SURPLUS_PAIR.md."""

from fractions import Fraction
from math import comb


def audit(length: int) -> None:
    assert length % 4 == 0
    a = b = length // 4
    u = 3 * length // 4
    rank = a + b + 1
    target_rank = a + 1

    record_entropy = (a + b) * u + length
    target_entropy = a * u + length
    ear_entropy = b * u

    rho = Fraction(record_entropy, rank)
    target_density = Fraction(target_entropy, target_rank)
    baseline = Fraction(u)
    assert rho - baseline == Fraction(length, 2 * length + 4)
    assert target_density - baseline == Fraction(length, length + 4)
    surplus = target_density - rho
    assert surplus == Fraction(length * length, (length + 4) * (2 * length + 4))
    assert surplus > 0

    conditional_deficit = ear_entropy + length
    assert conditional_deficit == 3 * length * length // 16 + length

    q = 1 << u
    y = 1 << length
    s_q = sum(comb(q, size) for size in range(3))
    numerator = q * q * y * y
    fibre = (numerator + s_q * s_q - 1) // (s_q * s_q)
    lower = 1 << (2 * (length - u))
    assert fibre >= lower
    assert fibre <= 4 * lower + 1

    print(
        f"L={length} rank={rank} surplus={float(surplus):.8f} "
        f"deficit={conditional_deficit} log2-lower-K={2*(length-u)} PASS"
    )


if __name__ == "__main__":
    for value in (8, 12, 16, 20, 24, 32):
        audit(value)
    print("ALL COMPONENT-SURPLUS PAIR CHECKS PASS")
