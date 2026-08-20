#!/usr/bin/env python3
"""Verify the support-weighted Heisenberg parabola barrier."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb


def distance_sidon_parabola(size: int) -> bool:
    seen: dict[int, tuple[int, int]] = {}
    for first, second in combinations(range(size), 2):
        norm = (second - first) ** 2 + (second * second - first * first) ** 2
        if norm in seen:
            return False
        seen[norm] = (first, second)
    return True


def derivative(size: int, shift: int, tail: int) -> int:
    assert 0 <= tail < tail + shift < size
    return (tail + shift) ** 2 - tail**2


def group_quotient(c: int, d: int) -> tuple[int, int, int]:
    # g_q=(q,2q,q^2), and g_c g_d^{-1}.
    shift = c - d
    slope = 2 * c - 2 * d
    intercept = c * c - d * d - slope * d
    return shift, slope, intercept


def explicit_weighted_mass(half_size: int) -> tuple[int, ...]:
    L = half_size
    k = 2 * L
    shifts = range(1, L + 1)
    weighted_mass = 0
    representation_mass: dict[tuple[int, int, int], int] = {}
    for d, c in combinations(shifts, 2):
        quotient = group_quotient(c, d)
        h = c - d
        assert quotient == (h, 2 * h, h * h)
        representation_mass[quotient] = representation_mass.get(quotient, 0) + 1
        child_support = frozenset(
            tail
            for tail in range(k - h)
            if derivative(k, h, tail) == h * h + 2 * h * tail
        )
        assert len(child_support) == k - h
        weighted_mass += comb(len(child_support), 3)

    closed_form = sum(
        (L - h) * comb(2 * L - h, 3)
        for h in range(1, L)
    )
    assert weighted_mass == closed_form
    assert representation_mass == {
        (h, 2 * h, h * h): L - h for h in range(1, L)
    }

    record_mass = sum(comb(k - shift, 3) for shift in shifts)
    assert record_mass == comb(2 * L, 4) - comb(L, 4)
    side_length = (k - 1) ** 2 + 1
    target = k**3 + side_length**2
    reverse_multiplicity = max(representation_mass.values(), default=0)

    # The transformed graph F(r)=f(r)-r^2 is horizontal.  Its difference
    # multiplicity at (h,0) is exactly k-h, which is the child occupancy.
    transformed = {tail: tail * tail - tail * tail for tail in range(k)}
    transformed_differences: dict[tuple[int, int], int] = {}
    for first in transformed:
        for second in transformed:
            difference = (
                first - second,
                transformed[first] - transformed[second],
            )
            transformed_differences[difference] = (
                transformed_differences.get(difference, 0) + 1
            )
    additive_energy = sum(
        multiplicity * multiplicity
        for multiplicity in transformed_differences.values()
    )
    transformed_triples = sum(
        comb(multiplicity, 3)
        for (shift, _), multiplicity in transformed_differences.items()
        if shift > 0
    )
    for h in range(1, L):
        difference_multiplicity = sum(
            1
            for tail in range(k - h)
            if transformed[tail + h] - transformed[tail] == 0
        )
        assert difference_multiplicity == k - h

    curvature_budget = side_length - 1  # floor(2(m-1)/|theta|), theta=2.
    divisor_sum = sum(curvature_budget // value for value in range(1, curvature_budget + 1))
    energy_bound = 2 * k * k + 4 * k * divisor_sum
    assert additive_energy <= energy_bound
    assert transformed_triples * 6 <= k * additive_energy
    assert weighted_mass <= reverse_multiplicity * transformed_triples
    assert weighted_mass * 6 <= reverse_multiplicity * k * additive_energy

    if L >= 4:
        assert weighted_mass >= Fraction(L**5, 100)
        assert weighted_mass <= 2 * L**5
        assert record_mass >= Fraction(L**4, 10)
        assert record_mass <= 2 * L**4
        assert target >= L**4
        assert target <= 20 * L**4
        assert weighted_mass * k**3 <= target**2
        if L >= 64:
            assert weighted_mass > target
    return (
        k,
        side_length,
        record_mass,
        weighted_mass,
        reverse_multiplicity,
        target,
        int(Fraction(weighted_mass * k**3, target**2) * 10**9),
        additive_energy,
        transformed_triples,
        comb(k, 2),
    )


def pell_gap_identity_checks(limit: int = 200) -> None:
    # If a^2(1+s^2)=b^2(1+t^2), reduce a/b=A/B.  Then
    # s^2+1=B^2 n and t^2+1=A^2 n.  For s>t, B>A and
    # 0 < sA-tB = (B^2-A^2)/(sA+tB).  The edge constraint
    # b<=t would force B<=t, making the final quotient <1.
    for t in range(1, limit):
        for s in range(t + 1, limit):
            for A in range(1, t + 1):
                numerator = t * t + 1
                if numerator % (A * A):
                    continue
                n = numerator // (A * A)
                square = s * s + 1
                for B in range(A + 1, t + 1):
                    if square != B * B * n:
                        continue
                    left = s * A - t * B
                    assert left > 0
                    assert Fraction(B * B - A * A, s * A + t * B) == left
                    assert left < 1  # This branch is mathematically impossible.


def main() -> None:
    pell_gap_identity_checks()
    profiles = []
    for half_size in (4, 8, 16, 32, 64, 100):
        assert distance_sidon_parabola(2 * half_size)
        profiles.append(explicit_weighted_mass(half_size))
    print("PASS", {"profiles": profiles})


if __name__ == "__main__":
    main()
