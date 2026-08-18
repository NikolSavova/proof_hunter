#!/usr/bin/env python3
"""Exact checks for ORTHOGONAL_PRODUCT_PARALLEL_COVER.md."""

from __future__ import annotations

from collections import Counter

from search_rotated_support import is_distance_sidon
from verify_orthogonal_two_support_gate import (
    add,
    dense_perpendicular_points,
    difference_set,
    erdos_turan,
    rotate,
)


Point = tuple[int, int]


def parallel_profile(points: list[Point]) -> tuple[int, int, int, int, int, int]:
    assert is_distance_sidon(points)
    rows: Counter[int] = Counter(y for _, y in points)
    within = {
        first[0] - second[0]
        for first in points
        for second in points
        if first[1] == second[1]
    }
    exact_size = 1 + sum(value * (value - 1) for value in rows.values())
    assert len(within) == exact_size

    differences = difference_set(points)
    horizontal_fibres = {x for x, _ in differences}
    assert len(horizontal_fibres) >= len(within)
    assert {(value, 0) for value in within} <= differences
    assert {rotate((value, 0)) for value in within} <= {
        rotate(value) for value in differences
    }

    ordinary = {
        add(first, second)
        for first in differences
        for second in differences
    }
    orthogonal = {
        add(first, rotate(second))
        for first in differences
        for second in differences
    }
    number = len(differences)
    assert len(ordinary) >= 2 * number - 1
    assert len(orthogonal) >= len(within) ** 2
    assert len(ordinary) * len(orthogonal) >= (
        (2 * number - 1) * len(within) ** 2
    )
    return (
        number,
        len(within),
        len(horizontal_fibres),
        len(ordinary),
        len(orthogonal),
        len(rows),
    )


def main() -> None:
    line = [(mark, 0) for mark in erdos_turan(11)[:10]]
    line_profile = parallel_profile(line)
    assert line_profile == (91, 91, 91, 615, 8_281, 1)
    print("line-10", line_profile)

    perpendicular = parallel_profile(dense_perpendicular_points())
    assert perpendicular == (1_561, 381, 381, 431_225, 1_413_381, 21)
    print("dense-perpendicular-40", perpendicular)
    print("orthogonal product parallel-cover theorem: PASS")


if __name__ == "__main__":
    main()
