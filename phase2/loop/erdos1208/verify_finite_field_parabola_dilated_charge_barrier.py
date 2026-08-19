#!/usr/bin/env python3
"""Exact finite checks for the metric-free dilated-charge barrier."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from verify_dilated_internal_pair_sum_charge import (
    add,
    clean_start_fibres,
    dilation,
)
from verify_third_additive_energy_barrier import is_prime, parabola


Point = tuple[int, int]
Profile = tuple[int, Point, int, int, int, int, int, int, int, int]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def profile(prime: int) -> Profile:
    assert is_prime(prime)
    points = parabola(prime)

    directed_differences = {
        subtract(points[first], points[second])
        for first in range(prime)
        for second in range(prime)
        if first != second
    }
    assert len(directed_differences) == prime * (prime - 1)

    sums = [
        add(points[first], points[second])
        for first, second in combinations(range(prime), 2)
    ]
    assert len(sums) == len(set(sums))

    distance_multiplicities: Counter[int] = Counter()
    for first, second in combinations(range(prime), 2):
        difference = subtract(points[first], points[second])
        distance_multiplicities[
            difference[0] * difference[0] + difference[1] * difference[1]
        ] += 1
    assert max(distance_multiplicities.values()) > 1

    fibres = clean_start_fibres(points)
    difference = max(fibres, key=lambda value: len(fibres[value]))
    starts = fibres[difference]

    loads: Counter[Point] = Counter(
        add(start, dilation(pair_sum))
        for start in starts
        for pair_sum in sums
    )
    mass = len(starts) * len(sums)
    energy = sum(load * load for load in loads.values())
    assert len(loads) * energy >= mass * mass

    return (
        prime,
        difference,
        len(starts),
        len(sums),
        mass,
        len(loads),
        energy,
        max(loads.values()),
        max(distance_multiplicities.values()),
        len(distance_multiplicities),
    )


def main() -> None:
    expected: dict[int, Profile] = {
        17: (17, (-1, -1), 14, 136, 1_904, 1_703, 2_344, 4, 5, 60),
        31: (31, (1, -3), 86, 465, 39_990, 25_278, 82_946, 8, 8, 181),
        43: (43, (6, -5), 171, 903, 154_413, 71_970, 469_517, 12, 8, 334),
        61: (61, (1, -3), 336, 1_830, 614_880, 193_008,
             2_927_966, 19, 8, 655),
    }

    for prime, wanted in expected.items():
        actual = profile(prime)
        assert actual == wanted, (prime, actual, wanted)
        print(
            prime,
            actual,
            "normalized-energy",
            actual[6] / actual[4],
        )

    print("finite-field parabola dilated-charge barrier: PASS")


if __name__ == "__main__":
    main()
