#!/usr/bin/env python3
"""Exact profiles for the fixed-distance-gap weighted-tail audit."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import isqrt
from random import Random

from verify_metric_scalar_aggregate_many_fibre_audit import clean_start_fibres
from verify_metric_scalar_pair_sum_charge import pair_labels
from verify_third_additive_energy_barrier import (
    parabola,
    squared_distance,
    transform,
)
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]


def gap_maximum(points: list[Point]) -> int:
    labels = list(pair_labels(points).values())
    loads = Counter(
        first - second
        for first in labels
        for second in labels
        if first != second
    )
    return max(loads.values())


def joint_profile(points: list[Point]) -> tuple[int, ...]:
    labels = pair_labels(points)
    distance_values = list(labels.values())
    target_loads = Counter(
        first - second
        for first in distance_values
        for second in distance_values
    )
    fibres = clean_start_fibres(points)
    codegrees: Counter[int] = Counter()
    for starts in fibres.values():
        values = [labels[start] for start in starts]
        for first in values:
            for second in values:
                difference = second - first
                if difference and difference % 18 == 0:
                    codegrees[difference // 18] += 1

    codegree_mass = sum(codegrees.values())
    absent_mass = sum(
        multiplicity
        for gap, multiplicity in codegrees.items()
        if target_loads[gap] == 0
    )
    singleton_mass = sum(
        multiplicity
        for gap, multiplicity in codegrees.items()
        if target_loads[gap] == 1
    )
    popular_mass = codegree_mass - absent_mass - singleton_mass
    weighted_overlap = sum(
        multiplicity * target_loads[gap]
        for gap, multiplicity in codegrees.items()
    )
    return (
        len(points),
        len(distance_values),
        sum(map(len, fibres.values())),
        sum(len(starts) * (len(starts) - 1) for starts in fibres.values()),
        codegree_mass,
        absent_mass,
        singleton_mass,
        popular_mass,
        weighted_overlap,
        max(load for gap, load in target_loads.items() if gap),
        max(target_loads[gap] for gap in codegrees),
    )


def sums_of_two_squares(bound: int) -> list[tuple[int, Point]]:
    output: list[tuple[int, Point]] = []
    for value in range(1, bound + 1):
        for first in range(isqrt(value) + 1):
            remainder = value - first * first
            second = isqrt(remainder)
            if second * second == remainder:
                output.append((value, (first, second)))
                break
    return output


def contaminated_high_fibre() -> tuple[int, ...]:
    # The parabola core is a compact finite stand-in for the asymptotic
    # two-arm core in Theorem 5.1.
    points = transform(parabola(61))
    fibres = clean_start_fibres(points)
    inherited_fibre = max(map(len, fibres.values()))
    seen_distances = {
        squared_distance(first, second)
        for first, second in combinations(points, 2)
    }
    assert len(seen_distances) == len(points) * (len(points) - 1) // 2

    controlled = sums_of_two_squares(100)
    scale = 100_000
    controlled_labels = {scale * scale * value for value, _ in controlled}
    assert len(controlled_labels) == len(controlled)
    assert controlled_labels.isdisjoint(seen_distances)

    random = Random(1208)
    attempts = 0
    radius = 10**12
    for _, vector in controlled:
        while True:
            attempts += 1
            first = (
                random.randrange(-radius, radius),
                random.randrange(-radius, radius),
            )
            second = (
                first[0] + scale * vector[0],
                first[1] + scale * vector[1],
            )
            if first == second or first in points or second in points:
                continue
            new_labels = [squared_distance(first, second)]
            for old in points:
                new_labels.extend((
                    squared_distance(first, old),
                    squared_distance(second, old),
                ))
            if len(new_labels) != len(set(new_labels)):
                continue
            if set(new_labels) & seen_distances:
                continue
            points.extend((first, second))
            seen_distances.update(new_labels)
            break

    assert len(seen_distances) == len(points) * (len(points) - 1) // 2
    pair_sums: set[Point] = set()
    for first, second in combinations(points, 2):
        total = first[0] + second[0], first[1] + second[1]
        assert total not in pair_sums
        pair_sums.add(total)

    radial_values = [value for value, _ in controlled]
    radial_gap_loads = Counter(
        first - second
        for first in radial_values
        for second in radial_values
        if first != second
    )
    popular_gap, popular_load = max(
        radial_gap_loads.items(), key=lambda item: item[1]
    )
    assert popular_load == 25
    # The corresponding controlled full-distance gap has at least this load.
    full_gap = scale * scale * popular_gap
    controlled_full_load = sum(
        first - second == full_gap
        for first in controlled_labels
        for second in controlled_labels
    )
    assert controlled_full_load == popular_load
    assert inherited_fibre > 2 * len(points)

    return (
        len(points),
        len(seen_distances),
        inherited_fibre,
        len(controlled),
        popular_gap,
        popular_load,
        attempts,
        max(abs(coordinate) for point in points for coordinate in point),
    )


def main() -> None:
    closure_expected = {20: 35, 40: 100, 60: 164, 80: 215, 100: 275}
    for size, expected in closure_expected.items():
        actual = gap_maximum(POINTS[:size])
        assert actual == expected, (size, actual, expected)
        print("closure-gap", size, actual)

    parabola_expected = {17: 3, 31: 6, 43: 8, 61: 9}
    for prime, expected in parabola_expected.items():
        actual = gap_maximum(transform(parabola(prime)))
        assert actual == expected, (prime, actual, expected)
        print("parabola-gap", prime, actual)

    joint_expected = {
        "closure-40": (
            40, 780, 12_420, 120_456, 8_654, 0, 0, 8_654,
            347_362, 100, 100,
        ),
        "parabola-31": (
            31, 465, 48_402, 2_731_648, 366_704, 349_098, 14_434,
            3_172, 21_448, 6, 6,
        ),
        "parabola-43": (
            43, 903, 190_278, 21_934_416, 2_792_682, 2_559_820,
            203_734, 29_128, 269_490, 8, 7,
        ),
    }
    families = {
        "closure-40": POINTS[:40],
        "parabola-31": transform(parabola(31)),
        "parabola-43": transform(parabola(43)),
    }
    for name, points in families.items():
        actual = joint_profile(points)
        assert actual == joint_expected[name], (name, actual, joint_expected[name])
        print("joint", name, actual)

    contaminated = contaminated_high_fibre()
    assert contaminated == (
        147, 10_731, 336, 43, -8, 25, 43, 994_256_611_946,
    ), contaminated
    print("contaminated-high-fibre", contaminated)
    print("fixed-distance-gap weighted-tail audit: PASS")


if __name__ == "__main__":
    main()
