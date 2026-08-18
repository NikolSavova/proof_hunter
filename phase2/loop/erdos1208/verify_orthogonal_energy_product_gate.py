#!/usr/bin/env python3
"""Historical exact profiles for the now-false energy-product gate.

The asymptotic perpendicular-ruler counterexample is checked separately by
``verify_orthogonal_energy_product_ruler_barrier.py``.
"""

from __future__ import annotations

from collections import Counter

from verify_orthogonal_switching_rich_tail import (
    concrete_quadratic_instance,
    difference_set,
    parabola,
    transform,
)
from verify_radial_orthogonal_product_barrier import radial_set
from verify_transverse_closure_witness import POINTS

Point = tuple[int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def energy_profile(differences: set[Point]) -> tuple[int, int, int, int, int]:
    ordinary = Counter(
        add(first, second)
        for first in differences
        for second in differences
    )
    orthogonal = Counter(
        add(first, rotate(second))
        for first in differences
        for second in differences
    )
    return (
        len(differences),
        len(ordinary),
        len(orthogonal),
        sum(value * value for value in ordinary.values()),
        sum(value * value for value in orthogonal.values()),
    )


def ratio(profile: tuple[int, int, int, int, int]) -> float:
    number, _, _, ordinary_energy, orthogonal_energy = profile
    return ordinary_energy * orthogonal_energy / number**5


def verify_complete_difference_profiles() -> None:
    families = (
        ("closure-15", difference_set(POINTS[:15]),
         (211, 7_801, 13_641, 491_179, 240_353)),
        ("closure-20", difference_set(POINTS[:20]),
         (381, 16_097, 24_305, 2_590_997, 1_735_609)),
        ("closure-25", difference_set(POINTS[:25]),
         (601, 32_823, 48_085, 8_460_337, 6_301_921)),
        ("closure-30", difference_set(POINTS[:30]),
         (871, 62_273, 89_977, 20_508_519, 16_135_769)),
        ("parabola-31", difference_set(transform(parabola(31))),
         (931, 9_779, 866_761, 191_031_539, 866_761)),
        ("quadratic-18", difference_set(concrete_quadratic_instance()[0]),
         (307, 23_869, 90_473, 761_635, 101_801)),
        (
            "small-constant-counterexample",
            difference_set(((0, 0), (0, 2), (2, 4), (3, 2), (3, 3))),
            (21, 107, 153, 2_941, 1_817),
        ),
    )
    for name, differences, expected in families:
        actual = energy_profile(differences)
        assert actual == expected
        print(name, actual, "normalized_product", ratio(actual))


def verify_radial_failure() -> None:
    families = (
        (8, (83, 431, 685, 176_051, 98_649)),
        (12, (165, 935, 1_509, 1_301_613, 726_009)),
        (20, (395, 2_515, 4_101, 16_205_523, 9_013_113)),
        (30, (815, 5_569, 9_141, 133_519_415, 74_411_737)),
    )
    previous = 0.0
    for side, expected in families:
        actual = energy_profile(radial_set(side))
        assert actual == expected
        current = ratio(actual)
        assert current > previous
        previous = current
        print("radial", side, actual, "normalized_product", current)


def main() -> None:
    verify_complete_difference_profiles()
    verify_radial_failure()
    print("historical energy-product profiles: PASS (gate itself is false)")


if __name__ == "__main__":
    main()
