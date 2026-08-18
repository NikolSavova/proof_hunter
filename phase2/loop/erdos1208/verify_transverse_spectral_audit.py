#!/usr/bin/env python3
"""Exact finite audit for the failed spectral strengthenings."""

from __future__ import annotations

from collections import Counter

from verify_transverse_closure_witness import FIXED_DIFFERENCE, POINTS
from verify_transverse_local_gate import differences


def quarter_turn(point: tuple[int, int]) -> tuple[int, int]:
    return -point[1], point[0]


def add(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] - right[0], left[1] - right[1]


def dot(left: tuple[int, int], right: tuple[int, int]) -> int:
    return left[0] * right[0] + left[1] * right[1]


def is_transverse_relation(row, colour, difference_set) -> bool:
    return (
        colour != (0, 0)
        and dot(row, colour) != 0
        and subtract(row, quarter_turn(colour)) in difference_set
    )


def colour_degree(colour, difference_set) -> int:
    turn = quarter_turn(colour)
    return sum(
        dot(add(edge, turn), colour) != 0
        and add(edge, turn) in difference_set
        for edge in difference_set
    )


def fixed_row_two_step(points) -> tuple[int, int]:
    difference_set = differences(points)
    neighbours = [
        colour
        for colour in difference_set
        if is_transverse_relation(FIXED_DIFFERENCE, colour, difference_set)
    ]
    return len(neighbours), sum(
        colour_degree(colour, difference_set) for colour in neighbours
    )


def mixed_energy(points) -> int:
    difference_set = list(differences(points))
    representations = Counter(
        subtract(left, right)
        for left in difference_set
        for right in difference_set
    )
    return sum(
        count * representations.get(quarter_turn(delta), 0)
        for delta, count in representations.items()
    )


def main() -> None:
    expected_two_step = {
        60: (339, 36_740),
        70: (422, 57_028),
        80: (514, 81_504),
        90: (614, 114_692),
        100: (719, 161_478),
        110: (830, 213_652),
        120: (948, 276_604),
    }
    for size, expected in expected_two_step.items():
        actual = fixed_row_two_step(POINTS[:size])
        assert actual == expected
        print("two_step", size, *actual)

    expected_mixed = {
        20: 1_735_609,
        30: 16_135_769,
        40: 76_060_041,
        50: 231_533_961,
        60: 581_578_857,
        70: 1_344_282_105,
    }
    for size, expected in expected_mixed.items():
        actual = mixed_energy(POINTS[:size])
        assert actual == expected
        print("mixed_energy", size, actual)

    print("PASS")


if __name__ == "__main__":
    main()
