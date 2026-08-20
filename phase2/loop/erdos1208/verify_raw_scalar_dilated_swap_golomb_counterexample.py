#!/usr/bin/env python3
"""Finite certificate for the dilated-copy swap kill of the raw scalar gate."""

from __future__ import annotations

from itertools import combinations
from math import comb

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_metric_scalar_pair_sum_charge import pair_labels
from verify_raw_scalar_golomb_planting_square_budget import ruzsa_core
from verify_single_fibre_replacement_transition_barrier import pair_tables


Point = tuple[int, int]
PRIME = 31
TRANSLATION = (1_121_776_528, 8_095_936_488)


def distance2(first: Point, second: Point) -> int:
    return (first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2


def build_points() -> tuple[list[Point], list[Point], list[int]]:
    marks = [point[0] // 6 for point in ruzsa_core(PRIME)]
    horizontal = [(6 * mark, 0) for mark in marks]
    diagonal = [
        (TRANSLATION[0] + mark, TRANSLATION[1] + mark)
        for mark in marks
    ]
    points = horizontal + diagonal
    pair_tables(points)
    return points, horizontal, marks


def profile() -> tuple[int, ...]:
    points, horizontal, marks = build_points()
    n = len(horizontal)
    k = len(points)
    edge_count = comb(k, 2)
    labels = pair_labels(points)

    # Corresponding horizontal/diagonal edges have norm ratio exactly 18.
    corresponding: dict[Point, int] = {}
    for first, second in combinations(range(n), 2):
        horizontal_sum = (
            horizontal[first][0] + horizontal[second][0],
            0,
        )
        diagonal_first = points[n + first]
        diagonal_second = points[n + second]
        diagonal_sum = (
            diagonal_first[0] + diagonal_second[0],
            diagonal_first[1] + diagonal_second[1],
        )
        horizontal_distance = distance2(horizontal[first], horizontal[second])
        diagonal_distance = distance2(diagonal_first, diagonal_second)
        assert horizontal_distance == 18 * diagonal_distance
        assert labels[horizontal_sum] == horizontal_distance
        assert labels[diagonal_sum] == diagonal_distance
        corresponding[horizontal_sum] = diagonal_distance

    core_fibres = clean_start_fibres(horizontal)
    full_fibres = clean_start_fibres(points)
    for difference, starts in core_fibres.items():
        assert set(starts) <= set(full_fibres[difference])

    total_h = sum(map(len, core_fibres.values()))
    sum_h_squared = sum(len(starts) ** 2 for starts in core_fibres.values())
    swap_mass = sum(
        len(starts) * (len(starts) - 1)
        for starts in core_fibres.values()
    )
    assert swap_mass == sum_h_squared - total_h

    # Every ordered distinct source pair gives one ordered off-diagonal
    # scalar collision by swapping its corresponding diagonal target edges.
    checked = 0
    for starts in core_fibres.values():
        for first in starts:
            for second in starts:
                if first == second:
                    continue
                assert (
                    labels[first] + 18 * corresponding[second]
                    == labels[second] + 18 * corresponding[first]
                )
                checked += 1
    assert checked == swap_mass

    return (
        n,
        k,
        edge_count,
        len(core_fibres),
        total_h,
        sum_h_squared,
        swap_mass,
        edge_count * k**3,
        max(max(abs(x), abs(y)) for x, y in points),
    )


def main() -> None:
    actual = profile()
    expected = (
        30,
        60,
        1_770,
        870,
        82_746,
        8_233_370,
        8_150_624,
        382_320_000,
        8_095_937_388,
    )
    assert actual == expected, (actual, expected)
    print("raw scalar dilated-copy swap profile", actual)
    print("raw scalar aggregate: ASYMPTOTIC COUNTEREXAMPLE SHADOW PASS")


if __name__ == "__main__":
    main()
