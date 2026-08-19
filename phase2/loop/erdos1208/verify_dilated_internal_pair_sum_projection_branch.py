#!/usr/bin/env python3
"""Exact checks for the projection-sparse dilated charge branch."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from verify_dilated_internal_pair_sum_charge import (
    add,
    clean_start_fibres,
    dilation,
)
from verify_orthogonal_energy_product_ruler_barrier import (
    erdos_turan,
    squared_distance_sidon,
)
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Projection = tuple[int, int]


def project(point: Point, functional: Projection) -> int:
    return point[0] * functional[0] + point[1] * functional[1]


def pair_sums(points: list[Point]) -> list[Point]:
    values = [
        add(points[first], points[second])
        for first, second in combinations(range(len(points)), 2)
    ]
    assert len(values) == len(set(values))
    return values


def profile(points: list[Point], functional: Projection) -> tuple[int, ...]:
    assert functional != (0, 0)
    assert squared_distance_sidon(points)
    sums = pair_sums(points)
    projection_values = {project(value, functional) for value in sums}
    fibres = clean_start_fibres(points)

    total_mass = 0
    total_energy = 0
    maximum_load = 0
    maximum_ratio_numerator = 0
    maximum_ratio_denominator = 1

    for starts in fibres.values():
        loads: Counter[Point] = Counter()
        label_pairs: dict[Point, set[tuple[int, int]]] = {}
        for start in starts:
            for pair_sum in sums:
                key = add(start, dilation(pair_sum))
                labels = (
                    project(start, functional),
                    project(pair_sum, functional),
                )
                bucket = label_pairs.setdefault(key, set())
                assert labels not in bucket
                bucket.add(labels)
                loads[key] += 1

        mass = len(starts) * len(sums)
        energy = sum(load * load for load in loads.values())
        bound = len(projection_values) ** 2 * mass
        assert energy <= bound
        assert max(loads.values(), default=0) <= len(projection_values) ** 2

        total_mass += mass
        total_energy += energy
        maximum_load = max(maximum_load, max(loads.values(), default=0))
        if energy * maximum_ratio_denominator > maximum_ratio_numerator * mass:
            maximum_ratio_numerator = energy
            maximum_ratio_denominator = mass

    return (
        len(points),
        len(sums),
        len(projection_values),
        len(fibres),
        total_mass,
        total_energy,
        maximum_load,
        maximum_ratio_numerator,
        maximum_ratio_denominator,
    )


def collinear_ruler() -> list[Point]:
    return [(mark, 0) for mark in erdos_turan(17, 16)]


def main() -> None:
    families = [
        (
            "collinear-ruler-16",
            collinear_ruler(),
            (0, 1),
            (16, 120, 1, 240, 196_560, 196_560, 1,
             1_320, 1_320),
        ),
        (
            "closure-30-y",
            POINTS[:30],
            (0, 1),
            (30, 435, 160, 828, 1_659_960, 1_670_720, 3,
             4_161, 3_915),
        ),
        (
            "closure-30-diagonal",
            POINTS[:30],
            (1, 1),
            (30, 435, 180, 828, 1_659_960, 1_670_720, 3,
             4_161, 3_915),
        ),
    ]

    for name, points, functional, expected in families:
        actual = profile(points, functional)
        assert actual == expected, (name, actual, expected)
        print(name, actual)

    print("dilated internal pair-sum projection branch: PASS")


if __name__ == "__main__":
    main()
