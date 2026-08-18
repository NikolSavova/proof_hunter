#!/usr/bin/env python3
"""Exact checks for ORTHOGONAL_RUZSA_HIGH_SUPPORT_BRANCH.md."""

from __future__ import annotations

from itertools import combinations

from search_rotated_support import is_distance_sidon
from verify_orthogonal_two_support_gate import (
    add,
    dense_perpendicular_points,
    difference_set,
    rotate,
)
from verify_third_additive_energy_barrier import parabola, transform
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]


def support_profile(points: list[Point] | tuple[Point, ...]) -> tuple[int, int, int]:
    assert is_distance_sidon(points)
    differences = difference_set(list(points))
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
    assert len(orthogonal) ** 2 >= number * len(ordinary)
    return number, len(ordinary), len(orthogonal)


def verify_named_families() -> None:
    families = (
        ("closure-20", POINTS[:20], (381, 16_097, 24_305)),
        ("parabola-31", transform(parabola(31)), (931, 9_779, 866_761)),
        (
            "dense-perpendicular-40",
            dense_perpendicular_points(),
            (1_561, 431_225, 1_413_381),
        ),
    )
    for name, points, expected in families:
        actual = support_profile(points)
        assert actual == expected
        number, ordinary, orthogonal = actual
        assert ordinary * orthogonal >= number**3 or ordinary < number ** (5 / 3)
        print(name, actual, "ruzsa_ratio", orthogonal**2 / (number * ordinary))


def verify_small_grids() -> None:
    best_ratio = 0.0
    best: tuple[Point, ...] | None = None
    valid = 0
    for side in (3, 4):
        grid = [(x, y) for x in range(side) for y in range(side)]
        for size in range(3, min(6, len(grid)) + 1):
            for points in combinations(grid, size):
                if not is_distance_sidon(points):
                    continue
                valid += 1
                number, ordinary, orthogonal = support_profile(points)
                ratio = number * ordinary / orthogonal**2
                if ratio > best_ratio:
                    best_ratio = ratio
                    best = points
    assert best is not None
    assert best_ratio <= 1
    print("small-grid sets", valid, "tightest_ratio", best_ratio, "witness", best)


def main() -> None:
    verify_named_families()
    verify_small_grids()
    print("orthogonal Ruzsa high-support branch: PASS")


if __name__ == "__main__":
    main()
