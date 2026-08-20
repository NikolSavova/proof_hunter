#!/usr/bin/env python3
"""Verify the support-weighted Heisenberg parabola barrier."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
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


def difference_counts(
    points: list[tuple[int, Fraction]],
) -> dict[tuple[int, Fraction], int]:
    counts: dict[tuple[int, Fraction], int] = {}
    for first in points:
        for second in points:
            difference = (first[0] - second[0], first[1] - second[1])
            counts[difference] = counts.get(difference, 0) + 1
    return counts


def coherent_block_height_checks() -> None:
    # Exhaust all four-point integer graphs in a 5-by-5 box, for several
    # rational nonzero curvatures.  Here w=(0,1), z_w=(1,0), so q_w=1.
    size = 4
    side_length = 5
    for values in product(range(side_length), repeat=size):
        for theta in (Fraction(1, 2), Fraction(2), Fraction(-3, 2)):
            transformed = [
                (index, Fraction(value) - theta * index * index / 2)
                for index, value in enumerate(values)
            ]
            counts = difference_counts(transformed)
            energy = sum(multiplicity**2 for multiplicity in counts.values())

            curvature_budget = int(
                Fraction(2 * (side_length - 1), 1) / abs(theta)
            )
            divisor_sum = sum(
                curvature_budget // value
                for value in range(1, curvature_budget + 1)
            )
            assert energy <= 2 * size**2 + 4 * size * divisor_sum
            factorial_energy = sum(
                multiplicity * (multiplicity - 1)
                for difference, multiplicity in counts.items()
                if difference != (0, 0)
            )
            assert energy == 2 * size**2 - size + factorial_energy
            assert factorial_energy <= 4 * size * divisor_sum
            child_triples = sum(
                comb(multiplicity, 3)
                for difference, multiplicity in counts.items()
                if difference != (0, 0)
            )
            assert 6 * child_triples <= size * factorial_energy

            # In a through-origin parameter block, every parent parameter
            # is an L-popular difference of B.  Test the exact
            # autocorrelation and resulting weighted estimate.
            for richness in (2, 3):
                popular = sorted(
                    difference
                    for difference, multiplicity in counts.items()
                    if difference[0] > 0 and multiplicity >= richness
                )
                parameter_differences: dict[tuple[int, Fraction], int] = {}
                popular_weight = 0
                for first in popular:
                    for second in popular:
                        difference = (
                            first[0] - second[0],
                            first[1] - second[1],
                        )
                        parameter_differences[difference] = (
                            parameter_differences.get(difference, 0) + 1
                        )
                for first_index, second_index in combinations(
                    range(len(popular)), 2
                ):
                    first = popular[first_index]
                    second = popular[second_index]
                    difference = (
                        first[0] - second[0],
                        first[1] - second[1],
                    )
                    popular_weight += comb(counts.get(difference, 0), 3)
                for difference, multiplicity in parameter_differences.items():
                    correlation = sum(
                        count * counts.get(
                            (
                                point[0] - difference[0],
                                point[1] - difference[1],
                            ),
                            0,
                        )
                        for point, count in counts.items()
                    )
                    assert richness**2 * multiplicity <= correlation
                    assert correlation <= energy
                assert popular_weight * richness**2 <= energy * child_triples
                assert (
                    3 * popular_weight * richness**2
                    <= 4
                    * size**3
                    * divisor_sum
                    * (size + 2 * divisor_sum)
                )

            # Check the exact four-index factorization behind the height
            # bound, including signs and the ambient coordinate identity.
            for a, d, b, c in product(range(size), repeat=4):
                if transformed[a][0] + transformed[d][0] != (
                    transformed[b][0] + transformed[c][0]
                ):
                    continue
                if transformed[a][1] + transformed[d][1] != (
                    transformed[b][1] + transformed[c][1]
                ):
                    continue
                u = a - b
                v = a - c
                assert d == a - u - v
                value_combo = values[a] + values[d] - values[b] - values[c]
                assert value_combo == theta * u * v
                assert abs(theta * u * v) <= 2 * (side_length - 1)

    # The weighted step is purely additive: any oriented parameter-pair
    # multiset is bounded by its largest difference multiplicity times the
    # full child-triple mass.
    theta = Fraction(3, 2)
    values = (0, 4, 1, 3, 2)
    transformed = [
        (index, Fraction(value) - theta * index * index / 2)
        for index, value in enumerate(values)
    ]
    child_counts = difference_counts(transformed)
    parameters = [
        (1, Fraction(0)),
        (2, Fraction(1)),
        (4, Fraction(-1)),
        (5, Fraction(3)),
        (7, Fraction(0)),
    ]
    oriented_counts: dict[tuple[int, Fraction], int] = {}
    weighted_mass = 0
    for second_index, first_index in combinations(range(len(parameters)), 2):
        first = parameters[first_index]
        second = parameters[second_index]
        difference = (first[0] - second[0], first[1] - second[1])
        oriented_counts[difference] = oriented_counts.get(difference, 0) + 1
        weighted_mass += comb(child_counts.get(difference, 0), 3)
    reverse_multiplicity = max(oriented_counts.values())
    child_triples = sum(comb(value, 3) for value in child_counts.values())
    assert weighted_mass <= reverse_multiplicity * child_triples


def main() -> None:
    pell_gap_identity_checks()
    coherent_block_height_checks()
    profiles = []
    for half_size in (4, 8, 16, 32, 64, 100):
        assert distance_sidon_parabola(2 * half_size)
        profiles.append(explicit_weighted_mass(half_size))
    print("PASS", {"profiles": profiles})


if __name__ == "__main__":
    main()
