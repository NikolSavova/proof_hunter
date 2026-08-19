#!/usr/bin/env python3
"""Exact regression checks for AMBIENT_CROSS_SUM_ENERGY_GATE.md."""

from __future__ import annotations

from collections import Counter

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_orthogonal_energy_product_ruler_barrier import (
    erdos_turan,
    squared_distance_sidon,
)
from verify_transverse_closure_witness import POINTS
from verify_transverse_row_source_c4 import SOURCE_POINTS


Point = tuple[int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def side_length(points: list[Point]) -> int:
    return max(
        max(x for x, _ in points) - min(x for x, _ in points),
        max(y for _, y in points) - min(y for _, y in points),
        1,
    )


def cross_sum(points: list[Point]) -> set[Point]:
    values = {
        add(left, rotate(right))
        for left in points
        for right in points
    }
    # This is the exact directness assertion |A+JA|=|A|^2.
    assert len(values) == len(points) ** 2
    return values


def difference_weights(points: list[Point]) -> Counter[Point]:
    return Counter(subtract(left, right) for left in points for right in points)


def profile(points: list[Point]) -> tuple[int, int, int, int, int]:
    assert squared_distance_sidon(points)
    k = len(points)
    m = side_length(points)
    values = cross_sum(points)
    reps = difference_weights(list(values))
    energy = sum(value * value for value in reps.values())
    maximum = max(value for shift, value in reps.items() if shift != (0, 0))

    # Coefficient-form verification of (1.1).  The autocorrelation of A+JA
    # is the convolution of the weighted A-difference function with its
    # quarter-turn.  We compare every coefficient, not only the energies.
    a_reps = difference_weights(points)
    predicted: Counter[Point] = Counter()
    for first, first_weight in a_reps.items():
        for second, second_weight in a_reps.items():
            predicted[add(first, rotate(second))] += first_weight * second_weight
    assert predicted == reps

    # Integer form of E >= k^8/(1024m^2).
    assert 1024 * m * m * energy >= k**8
    return k, m, energy, maximum, len(reps)


def ruler_points() -> list[Point]:
    ruler = erdos_turan(41, 40)
    return [(mark, 0) for mark in ruler[:20]] + [
        (0, mark) for mark in ruler[20:]
    ]


def main() -> None:
    families = [
        (
            "closure-30",
            POINTS[:30],
            (30, 150, 21_580_780, 152, 89_977),
        ),
        (
            "closure-40",
            POINTS[:40],
            (40, 223, 95_040_912, 231, 221_425),
        ),
        (
            "source-45",
            SOURCE_POINTS,
            (45, 324, 107_918_569, 137, 447_125),
        ),
        (
            "perpendicular-ruler-40",
            ruler_points(),
            (40, 3_202, 30_866_544, 110, 1_413_381),
        ),
        (
            "Costas-22",
            transformed_costas(23),
            (22, 131, 1_565_772, 28, 85_597),
        ),
    ]

    for name, points, expected in families:
        actual = profile(points)
        assert actual == expected
        k, m, energy, maximum, support = actual
        energy_ratio = energy / (k**5 + m * m * k * k)
        pointwise_ratio = maximum / (k + m * m / (k * k))
        print(
            name,
            actual,
            "energy-ratio",
            energy_ratio,
            "pointwise-ratio",
            pointwise_ratio,
            "support",
            support,
        )

    print("ambient cross-sum energy gate: PASS")


if __name__ == "__main__":
    main()
