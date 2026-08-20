#!/usr/bin/env python3
"""Verify the multi-arc component-color barrier."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import comb


B = 4
L = 3
BLOCK_LENGTH = 2 * L
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


@dataclass(frozen=True)
class Patch:
    block: int
    shift: int
    slope: int
    intercept: int
    support: frozenset[int]


def distance_sidon(values: tuple[int, ...]) -> bool:
    seen: dict[int, tuple[int, int]] = {}
    for first, second in combinations(range(len(values)), 2):
        norm = (second - first) ** 2 + (values[second] - values[first]) ** 2
        if norm in seen:
            return False
        seen[norm] = (first, second)
    return True


def derivative_support(
    values: tuple[int, ...],
    shift: int,
    slope: Fraction,
    intercept: Fraction,
) -> frozenset[int]:
    return frozenset(
        tail
        for tail in range(len(values))
        if 0 <= tail + shift < len(values)
        and values[tail + shift] - values[tail] == slope * tail + intercept
    )


def quotient(first: Patch, second: Patch) -> tuple[int, int, int]:
    slope = first.slope - second.slope
    return (
        first.shift - second.shift,
        slope,
        first.intercept - second.intercept - slope * second.shift,
    )


def rich_lines(
    values: tuple[int, ...], shift: int
) -> dict[tuple[Fraction, Fraction], frozenset[int]]:
    points = [
        (tail, values[tail + shift] - values[tail])
        for tail in range(len(values) - shift)
    ]
    candidates: set[tuple[Fraction, Fraction]] = set()
    for first, second in combinations(points, 2):
        slope = Fraction(second[1] - first[1], second[0] - first[0])
        if slope == 0:
            continue
        intercept = Fraction(first[1]) - slope * first[0]
        candidates.add((slope, intercept))
    result: dict[tuple[Fraction, Fraction], frozenset[int]] = {}
    for slope, intercept in candidates:
        support = frozenset(
            tail for tail, value in points if value == slope * tail + intercept
        )
        if len(support) >= 3:
            result[(slope, intercept)] = support
    return result


def interval_load(size: int, shift: int) -> int:
    return max(0, size - abs(shift))


def endpoint_correlation(size: int, shift: int) -> int:
    return sum(
        interval_load(size, difference)
        * interval_load(size, difference - shift)
        for difference in range(-(size - 1), size)
    )


def build_patches(values: tuple[int, ...]) -> list[Patch]:
    patches: list[Patch] = []
    for block in range(B):
        for shift in range(1, L + 1):
            slope = 2 * shift
            intercept = (
                shift * shift
                + GAMMA[block] * shift
                - 4 * block * L * shift
            )
            support = derivative_support(values, shift, slope, intercept)
            intended = frozenset(
                2 * block * L + local
                for local in range(BLOCK_LENGTH - shift)
            )
            assert support == intended
            assert L <= len(support) < 2 * L
            patches.append(Patch(block, shift, slope, intercept, support))
    return patches


def verify_polynomial_formula(values: tuple[int, ...]) -> None:
    for block in range(B):
        for local in range(BLOCK_LENGTH):
            level = 2 * block * L + local
            assert (
                values[level]
                == local * local + GAMMA[block] * local + CONSTANT[block]
            )
        for shift in range(1, L + 1):
            intercept = (
                shift * shift
                + GAMMA[block] * shift
                - 4 * block * L * shift
            )
            for local in range(BLOCK_LENGTH - shift):
                tail = 2 * block * L + local
                assert (
                    values[tail + shift] - values[tail]
                    == 2 * shift * tail + intercept
                )


def weighted_mass(
    values: tuple[int, ...], patches: list[Patch]
) -> tuple[int, int, int]:
    total = 0
    within = 0
    cross = 0
    for left, right in combinations(patches, 2):
        if left.shift == right.shift:
            continue
        first, second = (
            (left, right) if left.shift > right.shift else (right, left)
        )
        child = quotient(first, second)
        support = derivative_support(values, *child)
        contribution = comb(len(support), 3)
        total += contribution
        if first.block == second.block:
            within += contribution
            h = first.shift - second.shift
            expected_intercept = (
                h * h + h * (GAMMA[first.block] - 4 * first.block * L)
            )
            assert child == (h, 2 * h, expected_intercept)
            assert len(support) == 2 * L - h
        else:
            cross += contribution
            assert len(support) <= 2
    return total, within, cross


def minimum_gate(
    values: tuple[int, ...], patches: list[Patch]
) -> tuple[Fraction, list[tuple[int, int, int, Fraction]]]:
    shift_load = Counter(patch.shift for patch in patches)
    rows: list[tuple[int, int, int, Fraction]] = []
    total = Fraction(0)
    for h in range(1, L):
        parent_load = sum(
            load * shift_load.get(shift - h, 0)
            for shift, load in shift_load.items()
        )
        assert parent_load == B * B * (L - h)
        q_value = endpoint_correlation(len(values), h)
        lines = rich_lines(values, h)
        triple_mass = sum(comb(len(support), 3) for support in lines.values())
        internal_lines = {
            (
                Fraction(2 * h),
                Fraction(h * h + h * (GAMMA[block] - 4 * block * L)),
            )
            for block in range(B)
        }
        assert internal_lines <= set(lines)
        assert triple_mass == B * comb(2 * L - h, 3)
        coefficient = min(
            Fraction(parent_load),
            Fraction(q_value, (L - 1) ** 2),
        )
        assert coefficient == parent_load
        total += coefficient * triple_mass
        rows.append((h, parent_load, triple_mass, coefficient))
    return total, rows


def main() -> None:
    assert len(VALUES) == 2 * B * L
    verify_polynomial_formula(VALUES)
    assert distance_sidon(VALUES)
    patches = build_patches(VALUES)
    assert len(patches) == B * L

    total, within, cross = weighted_mass(VALUES, patches)
    expected = B * sum(
        (L - h) * comb(2 * L - h, 3) for h in range(1, L)
    )
    assert total == within == expected == 96
    assert cross == 0

    gate, rows = minimum_gate(VALUES, patches)
    assert gate == 1536
    assert gate == B * B * total
    assert rows == [
        (1, 32, 40, Fraction(32)),
        (2, 16, 16, Fraction(16)),
    ]

    print(
        "PASS",
        {
            "points": len(VALUES),
            "distances": comb(len(VALUES), 2),
            "patches": len(patches),
            "weighted_mass": total,
            "minimum_gate": int(gate),
            "gap": int(gate / total),
            "rows": rows,
        },
    )


if __name__ == "__main__":
    main()
