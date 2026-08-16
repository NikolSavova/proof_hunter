#!/usr/bin/env python3
"""Exact algebraic audit for the dynamic two-record Kraft theorem."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import ceil, log2, prod


def nested_pair_audit(limit: int = 512) -> dict[str, int]:
    maximum = Fraction(0, 1)
    argmax = -1
    for m in range(limit + 1):
        ratio = Fraction((m + 1) ** 2, 1 << m)
        if ratio > maximum:
            maximum, argmax = ratio, m
        assert 4 * (m + 1) ** 2 <= 9 * (1 << m)
    assert maximum == Fraction(9, 4) and argmax == 2
    return {
        "ranks_checked": limit + 1,
        "sharp_numerator": maximum.numerator,
        "sharp_denominator": maximum.denominator,
        "sharp_rank": argmax,
    }


def is_forward(x: tuple[int, ...], y: tuple[int, ...]) -> bool:
    if x == y:
        return False
    if y < x:
        x, y = y, x
    first = next(i for i in range(len(x)) if x[i] != y[i])
    assert x[first] < y[first]
    return any(x[j] > y[j] for j in range(first + 1, len(x)))


def word_counts(sizes: tuple[int, ...], brute: bool = False) -> tuple[int, int, int]:
    n = prod(sizes)
    prefix = 1
    first_difference = []
    for m in sizes:
        suffix = n // (prefix * m)
        count = prefix * m * (m - 1) * suffix * suffix
        first_difference.append(count)
        prefix *= m
    assert sum(first_difference) + n == n * n

    increasing = prod(m * (m + 1) // 2 for m in sizes)
    nonforward = 2 * increasing - n
    forward = n * n - nonforward
    assert nonforward * (4 ** len(sizes)) <= 2 * n * n * (3 ** len(sizes))

    if brute:
        words = list(product(*(range(m) for m in sizes)))
        brute_forward = sum(is_forward(x, y) for x in words for y in words)
        assert brute_forward == forward
        brute_first = [0] * len(sizes)
        diagonal = 0
        for x in words:
            for y in words:
                if x == y:
                    diagonal += 1
                    continue
                j = next(i for i in range(len(x)) if x[i] != y[i])
                brute_first[j] += 1
        assert brute_first == first_difference and diagonal == n
    return n, forward, nonforward


def heterogeneous_word_audit() -> dict[str, int]:
    cases = 0
    brute_cases = 0
    for q in range(1, 7):
        for base in range(2, 7):
            for tilt in range(6):
                sizes = tuple(2 + ((base + tilt * i + i * i) % 5) for i in range(q))
                brute = prod(sizes) <= 250
                word_counts(sizes, brute=brute)
                cases += 1
                brute_cases += int(brute)
    assert cases == 180
    return {"product_cells": cases, "brute_force_cells": brute_cases}


def fixed_outer_audit() -> dict[str, int]:
    checks = 0
    large_branch_checks = 0
    worst_ratio = Fraction(0, 1)
    for q in range(2, 81):
        s = q + 1
        threshold = ceil(2 * s * log2(2 * s))
        for m in range(2, 4097):
            records = m ** s
            source_faces = m ** q
            blocker_faces = 1 << m
            face_lower_bound = max(source_faces, blocker_faces)
            ratio = Fraction(records, face_lower_bound)
            worst_ratio = max(worst_ratio, ratio)
            assert records <= threshold * face_lower_bound
            if m > threshold:
                large_branch_checks += 1
                assert records <= blocker_faces
            else:
                assert records <= m * source_faces
                assert m <= threshold
            checks += 1
    return {
        "parameter_checks": checks,
        "large_blocker_branch_checks": large_branch_checks,
        "worst_ratio_floor": worst_ratio.numerator // worst_ratio.denominator,
    }


def ramp_exponents(h: int) -> tuple[int, ...]:
    ell = 1 << h
    left = tuple(1 << j for j in range(h))
    plateau = (ell,) * (ell // 2)
    return left + plateau + tuple(reversed(left))


def ramp_audit() -> dict[str, int]:
    profiles = 0
    largest_coordinates = 0
    largest_source_bits = 0
    for h in range(3, 8):
        exponents = ramp_exponents(h)
        sizes = tuple(1 << a for a in exponents)
        n, forward, nonforward = word_counts(sizes)
        assert forward + nonforward == n * n
        assert nonforward < n * n
        # Verify the exact first-divergence telescoping identity again in its
        # probability form, without constructing any floating quantities.
        survival = Fraction(1, 1)
        mass = Fraction(0, 1)
        for m in sizes:
            mass += survival * Fraction(m - 1, m)
            survival *= Fraction(1, m)
        assert mass + survival == 1
        profiles += 1
        largest_coordinates = max(largest_coordinates, len(sizes))
        largest_source_bits = max(largest_source_bits, sum(exponents))
    return {
        "profiles": profiles,
        "largest_coordinate_count": largest_coordinates,
        "largest_log2_source_count": largest_source_bits,
    }


def main() -> None:
    nested = nested_pair_audit()
    words = heterogeneous_word_audit()
    fixed_outer = fixed_outer_audit()
    ramps = ramp_audit()
    print("NESTED_PAIR_RELEASE", nested)
    print("VARIABLE_ALPHABET_KRAFT", words)
    print("FIXED_OUTER_LONG_EAR", fixed_outer)
    print("RAMP_PLATEAU", ramps)
    print("ALL_EXACT_CHECKS_PASSED")


if __name__ == "__main__":
    main()
