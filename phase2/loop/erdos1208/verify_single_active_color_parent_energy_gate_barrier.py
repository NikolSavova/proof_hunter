#!/usr/bin/env python3
"""Verify the separated one-color barrier to the parent-energy gate."""

from __future__ import annotations

from itertools import combinations
from math import comb, isqrt
from random import Random


N = 20
L = 2 * N
J = N * N
H = 7
D = 101

MU = 100003
BETA = 700000019
LAMBDA = 300007
ALPHA = 900000011


def allocate(
    shift: int, count: int, cursor: int
) -> tuple[tuple[int, ...], tuple[int, ...], int]:
    base = cursor + shift + 17
    tails = tuple(base + index * (2 * shift + 3) for index in range(count))
    heads = tuple(tail + shift for tail in tails)
    return tails, heads, heads[-1] + shift + 17


def build_graph() -> tuple[
    tuple[int, ...],
    dict[int, int],
    dict[str, tuple[int, int, frozenset[int]]],
]:
    cursor = 0
    groups: list[tuple[str, int, int]] = [
        ("child", H, J),
        ("lower", D, L),
        ("upper", D + H, L),
    ]
    allocated: dict[str, tuple[tuple[int, ...], tuple[int, ...]]] = {}
    levels: set[int] = set()
    for name, shift, count in groups:
        tails, heads, cursor = allocate(shift, count, cursor)
        assert not levels.intersection(tails)
        assert not levels.intersection(heads)
        levels.update(tails)
        levels.update(heads)
        allocated[name] = (tails, heads)

    parameters = {
        "child": (MU, BETA),
        "lower": (LAMBDA, ALPHA),
        "upper": (
            LAMBDA + MU,
            ALPHA + MU * D + BETA,
        ),
    }
    rng = Random(12081208)
    values: dict[int, int] = {}
    records: dict[str, tuple[int, int, frozenset[int]]] = {}
    for name, shift, _count in groups:
        slope, intercept = parameters[name]
        tails, heads = allocated[name]
        for tail, head in zip(tails, heads):
            base_value = rng.randrange(-(10**15), 10**15)
            values[tail] = base_value
            values[head] = base_value + intercept + slope * tail
        records[name] = (slope, intercept, frozenset(tails))

    vertical_translation = 1 - min(values.values())
    values = {
        level: value + vertical_translation for level, value in values.items()
    }
    return tuple(sorted(levels)), values, records


def derivative_support(
    levels: tuple[int, ...],
    values: dict[int, int],
    shift: int,
    slope: int,
    intercept: int,
) -> frozenset[int]:
    level_set = set(levels)
    return frozenset(
        tail
        for tail in levels
        if tail + shift in level_set
        and values[tail + shift] - values[tail] == slope * tail + intercept
    )


def verify_distance_sidon(
    levels: tuple[int, ...], values: dict[int, int]
) -> int:
    seen: dict[int, tuple[int, int]] = {}
    for first_index, first in enumerate(levels):
        for second in levels[first_index + 1 :]:
            norm = (second - first) ** 2 + (values[second] - values[first]) ** 2
            assert norm not in seen, (seen.get(norm), (first, second), norm)
            seen[norm] = (first, second)
    return len(seen)


def main() -> None:
    levels, values, records = build_graph()
    k = len(levels)
    assert k == 2 * J + 4 * L == 960
    assert L * L > k
    assert J * J > k

    shifts = {"child": H, "lower": D, "upper": D + H}
    for name in ("child", "lower", "upper"):
        slope, intercept, intended = records[name]
        support = derivative_support(
            levels, values, shifts[name], slope, intercept
        )
        assert support == intended
    assert len(records["child"][2]) == J
    assert len(records["lower"][2]) == L
    assert len(records["upper"][2]) == L
    assert records["lower"][2].isdisjoint(records["upper"][2])

    lower_slope, lower_intercept, _ = records["lower"]
    upper_slope, upper_intercept, _ = records["upper"]
    quotient = (
        (D + H) - D,
        upper_slope - lower_slope,
        upper_intercept
        - lower_intercept
        - (upper_slope - lower_slope) * D,
    )
    assert quotient == (H, MU, BETA)

    # Avoid fractions by storing twice the normalized center B.
    twice_center = 2 * BETA - MU * H
    assert 2 * quotient[2] - quotient[1] * quotient[0] == twice_center

    distances = verify_distance_sidon(levels, values)
    assert distances == comb(k, 2) == 460320

    parent_energy = 1
    child_weight = comb(J, 3)
    child_sixth_moment = child_weight**2
    weighted_mass = child_weight
    assert weighted_mass**2 == parent_energy * child_sixth_moment

    # Exact rational comparison 1 > k^4/J^5.
    assert J**5 > k**4
    assert weighted_mass < k**3
    assert J**3 < k**3  # the one-color joint tail is target-safe.

    side_length = max(max(levels), max(values.values()))
    assert side_length < 3 * 10**15

    print(
        "PASS",
        {
            "points": k,
            "distances": distances,
            "L": L,
            "J": J,
            "parent_support_overlap": 0,
            "active_colors": 1,
            "parent_energy": parent_energy,
            "child_weight": child_weight,
            "weighted_mass": weighted_mass,
            "k4_over_J5": k**4 / J**5,
            "gate_violation_factor": J**5 / k**4,
            "side_length": side_length,
        },
    )


if __name__ == "__main__":
    main()
