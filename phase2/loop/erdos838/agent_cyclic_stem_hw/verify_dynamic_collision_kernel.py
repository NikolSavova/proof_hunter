#!/usr/bin/env python3
"""Exact checks for the Boolean collision kernel in dynamic pair descent."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
import json
from pathlib import Path


def collision_energy(family: list[int]) -> Fraction:
    total = Fraction(0)
    for a in family:
        for b in family:
            total += Fraction(1, 1 << ((a | b).bit_count()))
    return total


def comparable_energy(family: list[int]) -> Fraction:
    total = Fraction(0)
    for a in family:
        for b in family:
            if (a & b) == a or (a & b) == b:
                total += Fraction(1, 1 << ((a | b).bit_count()))
    return total


def exhaustive_comparable_bound(max_ground: int = 4) -> dict[str, int]:
    checked = 0
    for m in range(max_ground + 1):
        subsets = list(range(1 << m))
        for family_mask in range(1 << len(subsets)):
            family = [subsets[i] for i in range(len(subsets)) if (family_mask >> i) & 1]
            comp = comparable_energy(family)
            assert comp <= 2 * len(family)
            checked += 1
    return {"maximum_ground_size": max_ground, "families_checked": checked}


def chain_rows(max_depth: int = 128) -> list[dict[str, str | int]]:
    selected = {0, 1, 2, 4, 8, 16, 32, 64, max_depth}
    rows = []
    for s in range(max_depth + 1):
        family = [(1 << t) - 1 for t in range(s + 1)]
        exact = collision_energy(family)
        formula = sum((Fraction(2 * k + 1, 1 << k) for k in range(s + 1)), Fraction(0))
        assert exact == formula < 6
        if s in selected:
            rows.append({"depth": s, "energy": str(exact), "strict_upper_bound": "6"})
    return rows


def transversal_mask(word: tuple[int, ...], alphabet: int) -> int:
    mask = 0
    for coordinate, letter in enumerate(word):
        mask |= 1 << (coordinate * alphabet + letter)
    return mask


def product_rows() -> list[dict[str, str | int]]:
    rows = []
    for alphabet, blocks in ((2, 2), (3, 3), (4, 3), (8, 6), (256, 16)):
        formula = Fraction((alphabet * (alphabet + 1)) ** blocks, 4**blocks)
        diagonal = Fraction(alphabet**blocks, 2**blocks)
        if alphabet <= 4 and blocks <= 3:
            family = [transversal_mask(word, alphabet) for word in product(range(alphabet), repeat=blocks)]
            assert collision_energy(family) == formula
            assert comparable_energy(family) == diagonal
        assert formula >= diagonal
        rows.append(
            {
                "alphabet": alphabet,
                "blocks": blocks,
                "carrier_count": alphabet**blocks,
                "collision_energy": str(formula),
                "comparable_diagonal_energy": str(diagonal),
                "incomparable_to_comparable_ratio": str(formula / diagonal - 1),
            }
        )
    return rows


def tag_rows() -> list[dict[str, int | str]]:
    rows = []
    for tags, alphabet, blocks in ((16, 16, 8), (256, 256, 16), (65536, 65536, 32)):
        child = Fraction((alphabet * (alphabet + 1)) ** blocks, 4**blocks)
        untagged = tags * tags * child
        tagged = tags * child
        assert untagged / tagged == tags
        rows.append(
            {
                "tags": tags,
                "alphabet": alphabet,
                "blocks": blocks,
                "untagged_to_tagged_collision_ratio": str(untagged / tagged),
            }
        )
    return rows


def ramp_exponents(h: int) -> list[int]:
    L = 1 << h
    left = [1 << q for q in range(h)]
    plateau = [L] * (L // 2)
    return left + plateau + list(reversed(left))


def ramp_rows() -> list[dict[str, int | str]]:
    rows = []
    for h in range(3, 8):
        exponents = ramp_exponents(h)
        prefix_product = 1
        kraft = Fraction(1)
        reciprocal_letters = Fraction(0)
        for exponent in exponents:
            alphabet = 1 << exponent
            reciprocal_letters += Fraction(1, alphabet)
            prefix_product *= alphabet
            kraft += Fraction(1, prefix_product)
        assert kraft < 2
        assert reciprocal_letters < 2
        rows.append(
            {
                "h": h,
                "L": 1 << h,
                "blocks": len(exponents),
                "prefix_collision_kraft_1e12_floor": (kraft.numerator * 10**12) // kraft.denominator,
                "sum_reciprocal_alphabets_1e12_floor": (reciprocal_letters.numerator * 10**12) // reciprocal_letters.denominator,
                "exact_checks": "1 < each quantity < 2",
            }
        )
    return rows


def main() -> None:
    certificate = {
        "comparable_kernel_exhaustion": exhaustive_comparable_bound(),
        "parabolic_prefix_chains": chain_rows(),
        "product_transversals": product_rows(),
        "outer_tag_factor": tag_rows(),
        "ramp_plateau": ramp_rows(),
    }
    saved = Path(__file__).with_name("dynamic_collision_kernel_certificate.json")
    if saved.exists():
        with saved.open(encoding="utf-8") as handle:
            assert certificate == json.load(handle)
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
