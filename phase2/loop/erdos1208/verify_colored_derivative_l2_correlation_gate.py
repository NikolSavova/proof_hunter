#!/usr/bin/env python3
"""Verify the sharp colored derivative L2 correlation gate."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt


@dataclass(frozen=True)
class Patch:
    block: int
    shift: int
    slope: int
    intercept: int


def derivative_support(
    values: tuple[int, ...],
    shift: int,
    slope: Fraction,
    intercept: Fraction,
) -> tuple[int, ...]:
    return tuple(
        tail
        for tail in range(len(values))
        if 0 <= tail + shift < len(values)
        and values[tail + shift] - values[tail]
        == slope * tail + intercept
    )


def quotient(first: Patch, second: Patch) -> tuple[int, int, int]:
    slope = first.slope - second.slope
    return (
        first.shift - second.shift,
        slope,
        first.intercept - second.intercept - slope * second.shift,
    )


def normalized_color(
    first: Patch, second: Patch
) -> tuple[int, Fraction, Fraction, Fraction]:
    h, child_slope, child_intercept = quotient(first, second)
    assert h != 0
    theta = Fraction(child_slope, h)
    eta_first = Fraction(first.slope) - theta * first.shift
    eta_second = Fraction(second.slope) - theta * second.shift
    assert eta_first == eta_second
    first_center = Fraction(first.intercept) - theta * first.shift**2 / 2
    second_center = Fraction(second.intercept) - theta * second.shift**2 / 2
    center_difference = first_center - second_center
    assert center_difference == Fraction(child_intercept) - theta * h**2 / 2
    assert child_slope == theta * h
    assert child_intercept == center_difference + theta * h**2 / 2
    return h, theta, center_difference, eta_first


def colored_profile(
    values: tuple[int, ...], patches: list[Patch]
) -> tuple[int, dict[int, tuple[int, int, int]]]:
    parent_colors: dict[int, Counter[tuple[Fraction, Fraction]]] = defaultdict(Counter)
    direct_mass = 0
    for left, right in combinations(patches, 2):
        if left.shift == right.shift:
            continue
        first, second = (
            (left, right) if left.shift > right.shift else (right, left)
        )
        h, theta, center, _eta = normalized_color(first, second)
        parent_colors[h][(theta, center)] += 1
        child_slope = theta * h
        child_intercept = center + theta * h**2 / 2
        occupancy = len(
            derivative_support(
                values, h, child_slope, child_intercept
            )
        )
        direct_mass += comb(occupancy, 3)

    rows: dict[int, tuple[int, int, int]] = {}
    identity_mass = 0
    for h, colors in parent_colors.items():
        parent_energy = 0
        child_sixth = 0
        row_mass = 0
        for (theta, center), multiplicity in colors.items():
            occupancy = len(
                derivative_support(
                    values,
                    h,
                    theta * h,
                    center + theta * h**2 / 2,
                )
            )
            triple_weight = comb(occupancy, 3)
            row_mass += multiplicity * triple_weight
            if triple_weight:
                parent_energy += multiplicity**2
                child_sixth += triple_weight**2
        assert row_mass**2 <= parent_energy * child_sixth
        identity_mass += row_mass
        rows[h] = (row_mass, parent_energy, child_sixth)
    assert identity_mass == direct_mass
    return direct_mass, rows


def distance_sidon(values: tuple[int, ...]) -> bool:
    seen: set[int] = set()
    for first, second in combinations(range(len(values)), 2):
        norm = (second - first) ** 2 + (values[second] - values[first]) ** 2
        if norm in seen:
            return False
        seen.add(norm)
    return True


def verify_parabolas() -> None:
    for half_size in range(2, 33):
        size = 2 * half_size
        values = tuple(index * index for index in range(size))
        patches = [
            Patch(-1, shift, 2 * shift, shift * shift)
            for shift in range(1, half_size + 1)
        ]
        mass, rows = colored_profile(values, patches)
        expected = sum(
            (half_size - h) * comb(2 * half_size - h, 3)
            for h in range(1, half_size)
        )
        assert mass == expected
        for h in range(1, half_size):
            row_mass, parent_energy, child_sixth = rows[h]
            reverse = half_size - h
            triple = comb(2 * half_size - h, 3)
            assert row_mass == reverse * triple
            assert parent_energy == reverse**2
            assert child_sixth == triple**2
            assert row_mass**2 == parent_energy * child_sixth


B = 4
L = 3
GAMMA = (90762, 27201, -10283, -91079)
CONSTANT = (-351997, -573877, -50618, -650066)
VALUES = (
    -351997,
    -261234,
    -170469,
    -79702,
    11067,
    101838,
    -573877,
    -546675,
    -519471,
    -492265,
    -465057,
    -437847,
    -50618,
    -60900,
    -71180,
    -81458,
    -91734,
    -102008,
    -650066,
    -741144,
    -832220,
    -923294,
    -1014366,
    -1105436,
)


def multi_arc_patches() -> list[Patch]:
    return [
        Patch(
            block,
            shift,
            2 * shift,
            shift * shift
            + GAMMA[block] * shift
            - 4 * block * L * shift,
        )
        for block in range(B)
        for shift in range(1, L + 1)
    ]


def verify_multi_arc() -> None:
    assert distance_sidon(VALUES)
    patches = multi_arc_patches()
    for patch in patches:
        support = derivative_support(
            VALUES,
            patch.shift,
            Fraction(patch.slope),
            Fraction(patch.intercept),
        )
        intended = tuple(
            2 * patch.block * L + local
            for local in range(2 * L - patch.shift)
        )
        assert support == intended

    mass, rows = colored_profile(VALUES, patches)
    assert mass == 96
    assert rows == {
        1: (80, 16, 400),
        2: (16, 4, 64),
    }
    for row_mass, parent_energy, child_sixth in rows.values():
        assert row_mass == isqrt(parent_energy * child_sixth)
        assert row_mass**2 == parent_energy * child_sixth

    # Audit the active color table directly.  Internal colors have the
    # advertised multiplicity and occupancy; every cross-block color is
    # inactive, so it contributes neither to W nor to the parent L2 moment.
    colors: dict[int, Counter[tuple[Fraction, Fraction]]] = defaultdict(Counter)
    active: dict[int, dict[tuple[Fraction, Fraction], tuple[int, int]]] = defaultdict(dict)
    cross_occupancies: list[int] = []
    for left, right in combinations(patches, 2):
        if left.shift == right.shift:
            continue
        first, second = (
            (left, right) if left.shift > right.shift else (right, left)
        )
        h, theta, center, _eta = normalized_color(first, second)
        color = (theta, center)
        colors[h][color] += 1
        occupancy = len(
            derivative_support(
                VALUES,
                h,
                theta * h,
                center + theta * h**2 / 2,
            )
        )
        if first.block == second.block:
            active[h][color] = (colors[h][color], occupancy)
            assert theta == 2
            assert center == h * (GAMMA[first.block] - 4 * first.block * L)
            assert occupancy == 2 * L - h
        else:
            cross_occupancies.append(occupancy)
            assert occupancy <= 2

    assert max(cross_occupancies) <= 2
    for h in range(1, L):
        assert len(active[h]) == B
        # Re-read final multiplicities because the table above was populated
        # while pairs were still being accumulated.
        for color, (_partial, occupancy) in active[h].items():
            assert colors[h][color] == L - h
            assert occupancy == 2 * L - h


def verify_arbitrary_signs() -> None:
    samples = [
        (
            Patch(0, 7, 19, 31),
            Patch(1, 2, -1, -11),
        ),
        (
            Patch(0, 3, -8, 17),
            Patch(1, -4, 6, 9),
        ),
    ]
    for first, second in samples:
        h, theta, center, eta = normalized_color(first, second)
        assert first.slope == theta * first.shift + eta
        assert second.slope == theta * second.shift + eta
        child = quotient(first, second)
        assert child[0] == h
        assert child[1] == theta * h
        assert child[2] == center + theta * h**2 / 2


def main() -> None:
    verify_arbitrary_signs()
    verify_parabolas()
    verify_multi_arc()
    print(
        "PASS",
        {
            "parabola_sizes": "4..64",
            "multi_arc_points": len(VALUES),
            "multi_arc_weighted_mass": 96,
            "multi_arc_active_rows": {
                1: (80, 16, 400),
                2: (16, 4, 64),
            },
            "uncolored_gate": 1536,
        },
    )


if __name__ == "__main__":
    main()
