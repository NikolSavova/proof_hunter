#!/usr/bin/env python3
"""Verify the common-core special-affine energy dichotomy."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, gcd


NONCOHERENT_F = [
    3894026, 7834044, 2503735, 292095, 4723279, 2530952,
    30792235, 34732290, 29402018, 27190415, 31621636, 29429346,
    48518509, 52458628, 47128420, 44916881, 49348166, 47155940,
    67404464, 71344732, 66014673, 63803283, 68234717, 66042640,
]

RATIONAL_LEVELS = [0, 2, 4, 6, 10, 12, 14, 16]
RATIONAL_F = [
    827497, 968559, 595483, 295371,
    3183660, 3324725, 2951652, 2651543,
]


def distance_sidon(levels: set[int], f: dict[int, int]) -> bool:
    seen: dict[int, tuple[int, int]] = {}
    for first, second in combinations(sorted(levels), 2):
        norm = (second - first) ** 2 + (f[second] - f[first]) ** 2
        if norm in seen:
            return False
        seen[norm] = (first, second)
    return True


def line_key(
    first: tuple[int, Fraction], second: tuple[int, Fraction]
) -> tuple[Fraction, Fraction]:
    q, value = first
    r, other = second
    theta = (other - value) / (r - q)
    return theta, value - theta * q


def parameter_blocks(
    parameters: dict[int, tuple[Fraction, Fraction]]
) -> tuple[int, dict[tuple[Fraction, Fraction], frozenset[int]]]:
    points = [(q, parameters[q][1]) for q in parameters]
    if len(points) == 1:
        return 1, {}
    keys = {line_key(first, second) for first, second in combinations(points, 2)}
    blocks = {
        key: frozenset(
            q for q, slope in points if slope == key[0] * q + key[1]
        )
        for key in keys
    }
    return max(map(len, blocks.values())), {
        key: block for key, block in blocks.items() if len(block) >= 3
    }


def rich_lines(
    derivative: dict[int, int], minimum: int = 3
) -> dict[tuple[Fraction, Fraction], frozenset[int]]:
    points = list(derivative.items())
    keys = {
        line_key(
            (first_tail, Fraction(first_value)),
            (second_tail, Fraction(second_value)),
        )
        for (first_tail, first_value), (second_tail, second_value)
        in combinations(points, 2)
        if first_value != second_value
    }
    output = {}
    for slope, intercept in keys:
        tails = frozenset(
            tail
            for tail, value in points
            if value == slope * tail + intercept
        )
        if len(tails) >= minimum:
            output[(slope, intercept)] = tails
    return output


def quotient(
    c: int,
    d: int,
    parameters: dict[int, tuple[Fraction, Fraction]],
) -> tuple[int, Fraction, Fraction]:
    alpha_c, slope_c = parameters[c]
    alpha_d, slope_d = parameters[d]
    child_slope = slope_c - slope_d
    child_intercept = alpha_c - alpha_d - child_slope * d
    return c - d, child_slope, child_intercept


def verify_instance(
    f: dict[int, int],
    support: frozenset[int],
    parameters: dict[int, tuple[Fraction, Fraction]],
) -> tuple[int, ...]:
    levels = set(f)
    k = len(levels)
    L = len(support)
    shifts = frozenset(parameters)
    M = len(shifts)
    assert parameters[0] == (0, 0)
    assert distance_sidon(levels, f)

    for q, (alpha, slope) in parameters.items():
        for tail in support:
            assert tail + q in levels
            assert f[tail + q] - f[tail] == alpha + slope * tail

    B, rich_parameter_blocks = parameter_blocks(parameters)
    sum_representations = Counter(
        tail + q for tail in support for q in shifts
    )
    additive_energy = sum(value * value for value in sum_representations.values())
    assert additive_energy * len(sum_representations) >= (L * M) ** 2

    neighborhood_mass = 0
    maximum_neighborhood = 0
    for tail in support:
        for anchor in shifts:
            neighborhood = frozenset(
                c for c in shifts if tail + c - anchor in support
            )
            assert anchor in neighborhood
            for c, d in combinations(neighborhood, 2):
                slope_anchor = parameters[anchor][1]
                slope_c = parameters[c][1]
                slope_d = parameters[d][1]
                assert (c - anchor) * (slope_d - slope_anchor) == (
                    (d - anchor) * (slope_c - slope_anchor)
                )
            assert len(neighborhood) <= B
            neighborhood_mass += len(neighborhood)
            maximum_neighborhood = max(maximum_neighborhood, len(neighborhood))
    assert neighborhood_mass == additive_energy
    assert additive_energy <= L * M * B
    assert L * M <= k * B

    quotient_checks = 0
    for c in shifts:
        for d in shifts:
            child_shift, child_slope, child_intercept = quotient(c, d, parameters)
            for tail in support:
                child_tail = tail + d
                assert f[child_tail + child_shift] - f[child_tail] == (
                    child_intercept + child_slope * child_tail
                )
                quotient_checks += 1

    intercept_cells = 0
    for (theta, _), block in rich_parameter_blocks.items():
        differences = {c - d for c in block for d in block if c != d}
        for h in differences:
            beta_supports: dict[Fraction, list[frozenset[int]]] = defaultdict(list)
            for d in block:
                if d + h not in block:
                    continue
                alpha_next = parameters[d + h][0]
                alpha_d = parameters[d][0]
                beta = alpha_next - alpha_d - theta * h * d
                translated_support = frozenset(tail + d for tail in support)
                beta_supports[beta].append(translated_support)
                child = quotient(d + h, d, parameters)
                assert child == (h, theta * h, beta)
            representatives = [sets[0] for sets in beta_supports.values()]
            assert all(
                first.isdisjoint(second)
                for first, second in combinations(representatives, 2)
            )
            assert len(beta_supports) * L <= k
            intercept_cells += len(beta_supports)

    core_records = (M - 1) * comb(L, 3)
    assert 6 * core_records <= B * k**3
    return (
        k,
        L,
        M,
        B,
        len(sum_representations),
        additive_energy,
        maximum_neighborhood,
        quotient_checks,
        len(rich_parameter_blocks),
        intercept_cells,
        core_records,
    )


def coherent_quadratic_profile() -> tuple[int, ...]:
    levels = set(range(11))
    f = {r: r * r for r in levels}
    support = frozenset(range(8))
    parameters = {
        q: (Fraction(q * q), Fraction(2 * q)) for q in range(4)
    }
    profile = verify_instance(f, support, parameters)
    assert profile[3] == 4

    theta = Fraction(2)
    for h in range(1, 4):
        beta_values = {
            parameters[d + h][0] - parameters[d][0] - theta * h * d
            for d in parameters if d + h in parameters
        }
        assert beta_values == {Fraction(h * h)}
    return profile


def noncoherent_disjoint_profile() -> tuple[int, ...]:
    levels = set(range(24))
    f = dict(enumerate(NONCOHERENT_F))
    support = frozenset(range(6))
    parameters = {
        0: (Fraction(0), Fraction(0)),
        6: (Fraction(26898209), Fraction(37)),
        12: (Fraction(44624483), Fraction(101)),
        18: (Fraction(63510438), Fraction(250)),
    }
    profile = verify_instance(f, support, parameters)
    assert support and len(support) ** 2 > len(levels)
    assert profile[3] == 2
    assert profile[4] == len(support) * len(parameters)
    assert profile[5] == len(support) * len(parameters)
    return profile


def quadratic_recurrence_check() -> None:
    theta = Fraction(7, 3)
    beta = Fraction(11, 5)
    start = 4
    step = 6
    alpha = {start: Fraction(13, 7)}
    for index in range(7):
        d = start + index * step
        alpha[d + step] = alpha[d] + theta * step * d + beta
    for index in range(8):
        d = start + index * step
        expected = (
            alpha[start]
            + index * beta
            + theta * step * (
                index * start + Fraction(step * index * (index - 1), 2)
            )
        )
        assert alpha[d] == expected


def rational_slope_profile() -> tuple[int, ...]:
    levels = set(RATIONAL_LEVELS)
    f = dict(zip(RATIONAL_LEVELS, RATIONAL_F, strict=True))
    assert distance_sidon(levels, f)
    support = frozenset({0, 2, 4, 6})
    shift = 10
    slope = Fraction(3, 2)
    intercept = Fraction(2356163)
    for tail in support:
        assert f[tail + shift] - f[tail] == intercept + slope * tail

    numerator = abs(slope.numerator)
    denominator = slope.denominator
    ordered = sorted(support)
    assert all((tail - ordered[0]) % denominator == 0 for tail in ordered)
    coordinate_diameter = max(
        max(levels) - min(levels), max(f.values()) - min(f.values())
    )
    assert numerator * (len(support) - 1) <= 2 * coordinate_diameter
    assert denominator * (len(support) - 1) <= 2 * coordinate_diameter
    return (
        len(levels),
        len(support),
        shift,
        numerator,
        denominator,
        coordinate_diameter,
        comb(len(levels), 2),
    )


def global_reverse_profile() -> tuple[int, ...]:
    n = 11
    f = {r: r * r for r in range(n)}
    derivatives = {
        shift: {
            tail: f[tail + shift] - f[tail]
            for tail in range(n - shift)
        }
        for shift in range(1, n)
    }
    patches = [
        (shift, slope, intercept, tails)
        for shift, derivative in derivatives.items()
        for (slope, intercept), tails in rich_lines(derivative).items()
    ]
    records = {
        (shift, slope, intercept, triple)
        for shift, slope, intercept, tails in patches
        for triple in combinations(sorted(tails), 3)
    }
    by_tail_triple: dict[tuple[int, int, int], list[tuple]] = defaultdict(list)
    for record in records:
        by_tail_triple[record[3]].append(record)
    T = len(records)
    support_size = comb(n, 3)
    ordered_overlap = sum(
        len(block) * (len(block) - 1) for block in by_tail_triple.values()
    )
    assert (ordered_overlap + T) * support_size >= T * T

    reverse: dict[tuple, set[int]] = defaultdict(set)
    parent_pairs = 0
    for triple, block in by_tail_triple.items():
        for left, right in combinations(block, 2):
            c, slope_c, intercept_c, _ = left
            d, slope_d, intercept_d, _ = right
            assert c != d
            if c < d:
                c, d = d, c
                slope_c, slope_d = slope_d, slope_c
                intercept_c, intercept_d = intercept_d, intercept_c
            child_shift = c - d
            child_slope = slope_c - slope_d
            child_intercept = intercept_c - intercept_d - child_slope * d
            child_triple = tuple(tail + d for tail in triple)
            child_record = (
                child_shift,
                child_slope,
                child_intercept,
                child_triple,
            )
            assert child_record in records
            assert d not in reverse[child_record]
            reverse[child_record].add(d)
            parent_pairs += 1
    assert 2 * parent_pairs == ordered_overlap
    maximum_reverse = max(map(len, reverse.values()), default=0)
    assert maximum_reverse <= n
    assert parent_pairs <= n * T
    assert T <= (2 * n + 1) * support_size
    return T, ordered_overlap, parent_pairs, len(reverse), maximum_reverse


def slope_count_inequalities() -> None:
    for side_diameter in range(1, 31):
        for direction_height in range(1, 11):
            for richness in range(2, 16):
                max_numerator = (2 * side_diameter) // (
                    direction_height * (richness - 1)
                )
                max_denominator = (2 * direction_height * side_diameter) // (
                    richness - 1
                )
                count = sum(
                    1
                    for numerator in range(1, max_numerator + 1)
                    for denominator in range(1, max_denominator + 1)
                    if gcd(numerator, denominator) == 1
                ) * 2
                assert count * (richness - 1) ** 2 <= 8 * side_diameter**2


def main() -> None:
    quadratic_recurrence_check()
    slope_count_inequalities()
    coherent = coherent_quadratic_profile()
    noncoherent = noncoherent_disjoint_profile()
    rational = rational_slope_profile()
    global_reverse = global_reverse_profile()
    print(
        "PASS",
        {
            "coherent_quadratic": coherent,
            "noncoherent_disjoint": noncoherent,
            "rational_slope": rational,
            "global_reverse": global_reverse,
        },
    )


if __name__ == "__main__":
    main()
