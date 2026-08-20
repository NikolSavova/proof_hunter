#!/usr/bin/env python3
"""Verify reverse slope packing and the exact Heisenberg endpoint map."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
from random import Random


GroupElement = tuple[int, int, int]


def multiply(first: GroupElement, second: GroupElement) -> GroupElement:
    q, slope, intercept = first
    r, other_slope, other_intercept = second
    return (
        q + r,
        slope + other_slope,
        intercept + other_intercept + slope * r,
    )


def inverse(element: GroupElement) -> GroupElement:
    q, slope, intercept = element
    return -q, -slope, -intercept + slope * q


def right_quotient(first: GroupElement, second: GroupElement) -> GroupElement:
    return multiply(first, inverse(second))


def distance_sidon(f: dict[int, int]) -> bool:
    seen: dict[int, tuple[int, int]] = {}
    for first, second in combinations(sorted(f), 2):
        norm = (second - first) ** 2 + (f[second] - f[first]) ** 2
        if norm in seen:
            return False
        seen[norm] = (first, second)
    return True


def put(f: dict[int, int], level: int, value: int) -> None:
    if level in f:
        assert f[level] == value
    else:
        f[level] = value


def isolated_reverse_certificate() -> tuple[
    dict[int, int],
    frozenset[int],
    int,
    int,
    int,
    list[tuple[GroupElement, frozenset[int]]],
]:
    rng = Random(12080820)
    child_support = frozenset({1_000_000, 1_000_001, 1_000_003})
    child_shift = 7
    child_slope = 7919
    child_intercept = 1_000_000_000_000_003
    denominators = (10_000, 20_000, 30_000)

    f = {tail: rng.randrange(-(10**15), 10**15) for tail in child_support}
    for tail in child_support:
        put(
            f,
            tail + child_shift,
            f[tail] + child_intercept + child_slope * tail,
        )

    patches: list[tuple[GroupElement, frozenset[int]]] = []
    for index, denominator in enumerate(denominators, 1):
        intercept = rng.randrange(
            2 * index * 10**18, (2 * index + 1) * 10**18
        )
        slope = rng.randrange(10**6, 10**7)
        core = frozenset(tail - denominator for tail in child_support)
        left_support = core | frozenset(
            range(100_000 * index, 100_000 * index + 17)
        )
        right_support = core | frozenset(
            range(120_000 * index, 120_000 * index + 17)
        )

        for child_tail in child_support:
            source = child_tail - denominator
            put(
                f,
                source,
                f[child_tail] - intercept - slope * source,
            )
        for tail in left_support - core:
            put(f, tail, rng.randrange(-(10**15), 10**15))
            put(f, tail + denominator, f[tail] + intercept + slope * tail)

        next_intercept = (
            intercept
            + child_slope * denominator
            + child_intercept
        )
        next_slope = slope + child_slope
        for tail in right_support - core:
            put(f, tail, rng.randrange(-(10**15), 10**15))
            put(
                f,
                tail + denominator + child_shift,
                f[tail] + next_intercept + next_slope * tail,
            )

        left = (denominator, slope, intercept)
        right = (
            denominator + child_shift,
            next_slope,
            next_intercept,
        )
        patches.append((left, left_support))
        patches.append((right, right_support))
        assert right_quotient(right, left) == (
            child_shift,
            child_slope,
            child_intercept,
        )

    return (
        f,
        child_support,
        child_shift,
        child_slope,
        child_intercept,
        patches,
    )


def maximum_center_load(elements: list[GroupElement]) -> int:
    return max(Counter((q, slope) for q, slope, _ in elements).values())


def collinear(
    first: tuple[int, int],
    second: tuple[int, int],
    third: tuple[int, int],
) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (third[0] - first[0]) * (second[1] - first[1])
    )


def maximum_abelian_coset_load(elements: list[GroupElement]) -> int:
    projection_load = Counter((q, slope) for q, slope, _ in elements)
    points = list(projection_load)
    maximum = max(projection_load.values())
    for first, second in combinations(points, 2):
        maximum = max(
            maximum,
            sum(
                load
                for point, load in projection_load.items()
                if collinear(first, second, point)
            ),
        )
    return maximum


def child_line_support(
    f: dict[int, int], quotient: GroupElement
) -> frozenset[int]:
    shift, slope, intercept = quotient
    return frozenset(
        tail
        for tail in f
        if tail + shift in f
        and f[tail + shift] - f[tail] == intercept + slope * tail
    )


def verify_isolated_reverse_stress() -> tuple[int, ...]:
    (
        f,
        child_support,
        child_shift,
        child_slope,
        child_intercept,
        patches,
    ) = isolated_reverse_certificate()
    assert len(f) == 219
    assert 20**2 > len(f)
    assert distance_sidon(f)

    elements = [element for element, _ in patches]
    for (shift, slope, intercept), support in patches:
        assert len(support) == 20
        for tail in support:
            assert tail + shift in f
            assert f[tail + shift] - f[tail] == intercept + slope * tail

    denominators = elements[::2]
    numerators = elements[1::2]
    assert len({element[0] for element in elements}) == len(elements)
    assert all(
        right_quotient(right, left)
        == (child_shift, child_slope, child_intercept)
        for left, right in zip(denominators, numerators, strict=True)
    )
    assert all(
        len(patches[2 * index][1] & patches[2 * index + 1][1]) == 3
        for index in range(3)
    )
    assert all(
        (patches[2 * first][1] | patches[2 * first + 1][1]).isdisjoint(
            patches[2 * second][1] | patches[2 * second + 1][1]
        )
        for first, second in combinations(range(3), 2)
    )
    assert child_line_support(
        f, (child_shift, child_slope, child_intercept)
    ) == child_support

    quotient_counts = Counter(
        right_quotient(first, second)
        for first in elements
        for second in elements
    )
    energy = sum(count * count for count in quotient_counts.values())
    target_multiplicity = quotient_counts[
        (child_shift, child_slope, child_intercept)
    ]
    assert target_multiplicity == 3

    ordered_overlap_mass = 0
    weighted_child_mass = 0
    off_diagonal_counts = Counter()
    for first_index, (first, first_support) in enumerate(patches):
        for second_index, (second, second_support) in enumerate(patches):
            if first_index == second_index:
                continue
            quotient = right_quotient(first, second)
            off_diagonal_counts[quotient] += 1
            ordered_overlap_mass += comb(len(first_support & second_support), 3)
    for quotient, count in off_diagonal_counts.items():
        weighted_child_mass += count * comb(len(child_line_support(f, quotient)), 3)
    assert ordered_overlap_mass == 6
    assert ordered_overlap_mass <= weighted_child_mass

    shifts = [element[0] for element in denominators]
    assert all(abs(first - second) != child_shift for first, second in combinations(shifts, 2))
    center_load = maximum_center_load(elements)
    abelian_load = maximum_abelian_coset_load(elements)
    assert center_load == 1
    assert abelian_load == 2

    coordinate_diameter = max(
        max(f) - min(f), max(f.values()) - min(f.values())
    )
    richness = 20
    reverse_bound = Fraction(
        8 * coordinate_diameter**2 * len(f) * (len(f) - 1),
        richness * (richness - 1) ** 3,
    )
    assert target_multiplicity <= len(f)
    assert target_multiplicity <= reverse_bound
    return (
        len(f),
        richness,
        len(elements),
        target_multiplicity,
        energy,
        center_load,
        abelian_load,
        ordered_overlap_mass,
        weighted_child_mass,
        coordinate_diameter,
        comb(len(f), 2),
    )


def group_law_checks() -> None:
    samples = [
        (0, 0, 0),
        (3, 5, 7),
        (-11, 13, -17),
        (19, -23, 29),
    ]
    identity = (0, 0, 0)
    for element in samples:
        assert multiply(element, identity) == element
        assert multiply(identity, element) == element
        assert multiply(element, inverse(element)) == identity
        assert multiply(inverse(element), element) == identity
    for first in samples:
        for second in samples:
            for third in samples:
                assert multiply(multiply(first, second), third) == multiply(
                    first, multiply(second, third)
                )


def finite_reverse_bound_checks() -> None:
    for k in range(4, 80):
        for richness in range(3, k + 1):
            per_slope = Fraction(k * (k - 1), richness * (richness - 1))
            for side_diameter in range(1, 40):
                slope_count = Fraction(
                    8 * side_diameter**2, (richness - 1) ** 2
                )
                reverse_bound = slope_count * per_slope
                assert reverse_bound == Fraction(
                    8 * side_diameter**2 * k * (k - 1),
                    richness * (richness - 1) ** 3,
                )


def main() -> None:
    group_law_checks()
    finite_reverse_bound_checks()
    stress = verify_isolated_reverse_stress()
    print("PASS", {"isolated_reverse_stress": stress})


if __name__ == "__main__":
    main()
