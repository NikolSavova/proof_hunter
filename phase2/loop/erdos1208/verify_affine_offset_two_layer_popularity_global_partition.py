#!/usr/bin/env python3
"""Verify affine-offset two-layer popularity and the global pair partition."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import comb


Point = tuple[int, Fraction]


@dataclass(frozen=True)
class Patch:
    shift: int
    slope: int
    intercept: int
    support: frozenset[int]


def difference_counts(first: list[Point], second: list[Point]) -> Counter[Point]:
    return Counter(
        (a[0] - b[0], a[1] - b[1])
        for a in first
        for b in second
    )


def additive_energy(points: list[Point]) -> int:
    counts = difference_counts(points, points)
    return sum(value * value for value in counts.values())


def put_edge(
    values: dict[int, int],
    shift: int,
    slope: int,
    intercept: int,
    support: frozenset[int],
    salt: int,
) -> None:
    for tail in support:
        if tail not in values:
            values[tail] = 100_000 * salt + 97 * tail + tail * tail
        head = tail + shift
        target = values[tail] + intercept + slope * tail
        if head in values:
            assert values[head] == target
        else:
            values[head] = target


def synthetic_offset_family() -> tuple[dict[int, int], list[Patch], int, int]:
    # Two affine-offset blocks with the same theta=2 and the same child
    # quotient (h,mu,beta)=(3,6,-16), but eta=3 and eta=9.
    values: dict[int, int] = {}
    specifications = (
        (4, 11, 5, frozenset({0, 20, 40}), 1),
        (7, 17, 13, frozenset({1, 21, 41}), 2),
        (14, 37, 100, frozenset({100, 120, 140}), 3),
        (17, 43, 168, frozenset({101, 121, 141}), 4),
    )
    for shift, slope, intercept, support, salt in specifications:
        put_edge(values, shift, slope, intercept, support, salt)

    # Plant the common child line independently.
    child_support = frozenset({200, 220, 240})
    put_edge(values, 3, 6, -16, child_support, 5)

    patches: list[Patch] = []
    for shift, slope, intercept, intended, _ in specifications:
        full_support = frozenset(
            tail
            for tail in values
            if tail + shift in values
            and values[tail + shift] - values[tail] == intercept + slope * tail
        )
        assert full_support == intended
        patches.append(Patch(shift, slope, intercept, full_support))
    return values, patches, 2, 3


def normalized_graph(
    values: dict[int, int], theta: Fraction, eta: Fraction = Fraction(0)
) -> list[Point]:
    return [
        (
            level,
            Fraction(value) - theta * level * level / 2 + eta * level,
        )
        for level, value in sorted(values.items())
    ]


def normalized_parameter(patch: Patch, theta: Fraction) -> Point:
    return (
        patch.shift,
        Fraction(patch.intercept) - theta * patch.shift * patch.shift / 2,
    )


def quotient(
    first: Patch, second: Patch
) -> tuple[int, int, int]:
    return (
        first.shift - second.shift,
        first.slope - second.slope,
        first.intercept
        - second.intercept
        - (first.slope - second.slope) * second.shift,
    )


def derivative_support(
    values: dict[int, int], shift: int, slope: Fraction, intercept: Fraction
) -> frozenset[int]:
    return frozenset(
        tail
        for tail in values
        if tail + shift in values
        and values[tail + shift] - values[tail] == intercept + slope * tail
    )


def q_correlation(levels: frozenset[int]) -> dict[int, int]:
    difference_load = Counter(a - b for a in levels for b in levels)
    shifts = {
        first - second
        for first in difference_load
        for second in difference_load
    }
    return {
        h: sum(
            difference_load[q] * difference_load.get(q - h, 0)
            for q in shifts
        )
        for h in shifts
    }


def cell_triples(values: dict[int, int]) -> dict[int, int]:
    levels = frozenset(values)
    result: dict[int, int] = {}
    for shift in sorted(a - b for a in levels for b in levels if a != b):
        points = [
            (tail, values[tail + shift] - values[tail])
            for tail in levels
            if tail + shift in values
        ]
        lines: set[tuple[Fraction, Fraction]] = set()
        for first, second in combinations(points, 2):
            slope = Fraction(second[1] - first[1], second[0] - first[0])
            if slope == 0:
                continue
            intercept = Fraction(first[1]) - slope * first[0]
            lines.add((slope, intercept))
        total = 0
        for slope, intercept in lines:
            occupancy = sum(
                Fraction(value) == intercept + slope * tail
                for tail, value in points
            )
            if occupancy >= 3:
                total += comb(occupancy, 3)
        result[shift] = total
    return result


def verify_two_layer(
    values: dict[int, int],
    patches: list[Patch],
    theta: int,
    richness: int,
) -> dict[str, int]:
    theta_f = Fraction(theta)
    base = normalized_graph(values, theta_f)
    base_differences = difference_counts(base, base)
    base_energy = additive_energy(base)
    child_triples = sum(
        comb(load, 3)
        for difference, load in base_differences.items()
        if difference != (0, 0)
    )

    blocks: dict[Fraction, list[Patch]] = defaultdict(list)
    for patch in patches:
        eta = Fraction(patch.slope) - theta_f * patch.shift
        blocks[eta].append(patch)
    assert set(blocks) == {Fraction(3), Fraction(9)}

    total_block_weight = 0
    for eta, block in blocks.items():
        assert len(block) == 2
        sheared_tail = normalized_graph(values, theta_f, eta)
        cross = difference_counts(base, sheared_tail)
        sheared_energy = additive_energy(sheared_tail)
        cross_energy = sum(value * value for value in cross.values())
        internal_cross_energy = sum(
            base_differences[difference] * difference_counts(
                sheared_tail, sheared_tail
            )[difference]
            for difference in base_differences
        )
        assert sheared_energy == base_energy
        assert cross_energy == internal_cross_energy
        assert cross_energy <= base_energy

        parameters = [normalized_parameter(patch, theta_f) for patch in block]
        for patch, parameter in zip(block, parameters):
            for tail in patch.support:
                head = (
                    tail + patch.shift,
                    Fraction(values[tail + patch.shift])
                    - theta_f * (tail + patch.shift) ** 2 / 2,
                )
                tail_point = (
                    tail,
                    Fraction(values[tail])
                    - theta_f * tail * tail / 2
                    + eta * tail,
                )
                assert (
                    head[0] - tail_point[0],
                    head[1] - tail_point[1],
                ) == parameter
            assert cross[parameter] >= richness

        parameter_counts = difference_counts(parameters, parameters)
        for difference, load in parameter_counts.items():
            correlation = sum(
                value
                * cross.get(
                    (
                        point[0] - difference[0],
                        point[1] - difference[1],
                    ),
                    0,
                )
                for point, value in cross.items()
            )
            assert richness * richness * load <= correlation
            assert correlation <= cross_energy <= base_energy

        first, second = sorted(block, key=lambda item: item.shift)
        child = quotient(second, first)
        assert child == (3, 6, -16)
        first_parameter = normalized_parameter(first, theta_f)
        second_parameter = normalized_parameter(second, theta_f)
        difference = (
            second_parameter[0] - first_parameter[0],
            second_parameter[1] - first_parameter[1],
        )
        assert difference == (3, -25)
        support = derivative_support(values, *child)
        assert len(support) >= 3
        assert base_differences[difference] == len(support)
        block_weight = comb(len(support), 3)
        assert block_weight * richness * richness <= base_energy * child_triples
        total_block_weight += block_weight
    return {
        "base_energy": base_energy,
        "child_triples": child_triples,
        "block_weight": total_block_weight,
    }


def verify_global_partition(
    values: dict[int, int], patches: list[Patch], richness: int
) -> dict[str, int]:
    levels = frozenset(values)
    q_corr = q_correlation(levels)
    direct_weight = 0
    partition_weight = 0
    reverse: Counter[tuple[Fraction, Point]] = Counter()

    for lower, upper in combinations(sorted(patches, key=lambda p: p.shift), 2):
        assert upper.shift != lower.shift
        theta = Fraction(upper.slope - lower.slope, upper.shift - lower.shift)
        eta = Fraction(lower.slope) - theta * lower.shift
        assert Fraction(upper.slope) - theta * upper.shift == eta
        first_parameter = normalized_parameter(lower, theta)
        second_parameter = normalized_parameter(upper, theta)
        difference = (
            second_parameter[0] - first_parameter[0],
            second_parameter[1] - first_parameter[1],
        )
        child = quotient(upper, lower)
        assert child[0] == difference[0]
        normalized_intercept = Fraction(child[2]) - theta * child[0] ** 2 / 2
        assert normalized_intercept == difference[1]

        support = derivative_support(values, *child)
        weight = comb(len(support), 3)
        direct_weight += weight

        base = normalized_graph(values, theta)
        load = difference_counts(base, base)[difference]
        assert load == len(support)
        partition_weight += comb(load, 3)
        reverse[(theta, difference)] += 1

        nonshared = 0
        for first_tail in upper.support:
            for second_tail in lower.support:
                if first_tail == second_tail:
                    continue
                nonshared += 1
                recovered_eta = (
                    (
                        Fraction(values[first_tail + upper.shift])
                        - theta * (first_tail + upper.shift) ** 2 / 2
                    )
                    - (
                        Fraction(values[first_tail])
                        - theta * first_tail * first_tail / 2
                    )
                    - (
                        Fraction(values[second_tail + lower.shift])
                        - theta * (second_tail + lower.shift) ** 2 / 2
                    )
                    + (
                        Fraction(values[second_tail])
                        - theta * second_tail * second_tail / 2
                    )
                    - difference[1]
                ) / (first_tail - second_tail)
                assert recovered_eta == eta
        assert nonshared >= (richness - 1) ** 2

    assert direct_weight == partition_weight
    for (theta, difference), load in reverse.items():
        del theta
        assert load * (richness - 1) ** 2 <= q_corr[difference[0]]

    triples = cell_triples(values)
    weighted_cell_energy = sum(
        q_corr.get(shift, 0) * mass for shift, mass in triples.items()
    )
    assert direct_weight * (richness - 1) ** 2 <= weighted_cell_energy

    difference_load = Counter(a - b for a in levels for b in levels)
    assert sum(q_corr.values()) == len(levels) ** 4
    level_energy = sum(value * value for value in difference_load.values())
    assert max(q_corr.values()) == level_energy
    assert level_energy <= len(levels) ** 3
    return {
        "points": len(levels),
        "patches": len(patches),
        "direct_weight": direct_weight,
        "weighted_cell_energy": weighted_cell_energy,
        "level_energy": level_energy,
    }


def parabola_profile(half_size: int) -> tuple[int, ...]:
    length = 2 * half_size
    levels = frozenset(range(length))
    q_corr = q_correlation(levels)
    weighted_mass = sum(
        (half_size - h) * comb(length - h, 3)
        for h in range(1, half_size)
    )
    weighted_cell_energy = sum(
        q_corr[h] * comb(length - h, 3)
        for h in range(1, length)
    )
    assert weighted_mass * (half_size - 1) ** 2 <= weighted_cell_energy
    if half_size >= 4:
        assert weighted_cell_energy >= length**7 // 10_000
        assert weighted_cell_energy <= length**7
        quotient_bound = Fraction(weighted_cell_energy, (half_size - 1) ** 2)
        assert quotient_bound >= weighted_mass
        assert quotient_bound <= 100 * length**5
    return (
        length,
        weighted_mass,
        weighted_cell_energy,
        int(Fraction(weighted_cell_energy, (half_size - 1) ** 2)),
    )


def main() -> None:
    values, patches, theta, richness = synthetic_offset_family()
    local = verify_two_layer(values, patches, theta, richness)
    global_profile = verify_global_partition(values, patches, richness)
    parabolas = [
        parabola_profile(half_size)
        for half_size in (4, 8, 16, 32, 64, 100)
    ]
    print(
        "PASS",
        {
            "local": local,
            "global": global_profile,
            "parabolas": parabolas,
        },
    )


if __name__ == "__main__":
    main()
