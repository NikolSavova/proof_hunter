#!/usr/bin/env python3
"""Exact checks for SUPPORT_ADAPTIVE_POPULAR_OVERLAP_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict

from analyze_affine_costas_energy import smallest_transform, welch
from verify_orthogonal_switching_rich_tail import concrete_quadratic_instance
from verify_orthogonal_two_support_gate import (
    dense_perpendicular_points,
    difference_set,
)
from verify_radial_orthogonal_product_barrier import radial_set
from verify_third_additive_energy_barrier import parabola, transform
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def popular_profile(differences: set[Point]) -> tuple[int, int, int, int, int]:
    """Return N,S,E_perp,nonzero rich tail, and number of rich shifts."""
    number = len(differences)
    representations = Counter(
        add(left, right)
        for left in differences
        for right in differences
    )
    support = len(representations)
    assert sum(representations.values()) == number * number

    energy = 0
    zero = 0
    low_first = 0
    low_second = 0
    rich_tail = 0
    rich_shifts = 0
    for shift, value in representations.items():
        rotated = representations.get(rotate(shift), 0)
        term = value * rotated
        energy += term
        if shift == (0, 0):
            zero += term
        elif value * number <= support:
            low_first += term
        elif rotated * number <= support:
            low_second += term
        else:
            rich_tail += term
            rich_shifts += 1

    budget = number * support
    assert zero == number * number <= budget
    assert low_first <= budget
    assert low_second <= budget
    assert energy == zero + low_first + low_second + rich_tail
    assert energy <= 3 * budget + rich_tail
    return number, support, energy, rich_tail, rich_shifts


def rich_fibre_profile(
    differences: set[Point],
) -> tuple[int, int, int, int]:
    """Return tail mass, label support, max load, and second moment."""
    number = len(differences)
    overlaps: dict[Point, list[Point]] = defaultdict(list)
    for endpoint in differences:
        for start in differences:
            overlaps[
                endpoint[0] - start[0], endpoint[1] - start[1]
            ].append(start)
    support = len(overlaps)
    rich = {
        shift
        for shift, starts in overlaps.items()
        if shift != (0, 0)
        and len(starts) * number > support
        and len(overlaps.get(rotate(shift), ())) * number > support
    }

    loads: Counter[tuple[Point, Point]] = Counter()
    for shift in rich:
        rotated = rotate(shift)
        for first_start in overlaps[shift]:
            first_endpoint = add(first_start, shift)
            for second_start in overlaps[rotated]:
                second_endpoint = add(second_start, rotated)
                ordinary_sum = add(first_endpoint, second_endpoint)
                loads[first_start, ordinary_sum] += 1

    return (
        sum(loads.values()),
        len(loads),
        max(loads.values(), default=0),
        sum(value * value for value in loads.values()),
    )


def print_profile(name: str, differences: set[Point]) -> float:
    number, support, energy, tail, shifts = popular_profile(differences)
    ratio = tail / (number * support)
    print(
        name,
        "N", number,
        "S", support,
        "energy", energy,
        "tail", tail,
        "shifts", shifts,
        "tail/(NS)", ratio,
    )
    return ratio


def main() -> None:
    closure_ratios = []
    for size in (20, 30, 40, 50, 60, 70):
        ratio = print_profile(
            f"closure-{size}", difference_set(POINTS[:size])
        )
        closure_ratios.append(ratio)
    assert max(closure_ratios) < 0.007

    fibre_families = (
        (
            "rich-fibre closure-30",
            difference_set(POINTS[:30]),
            (58_800, 58_100, 3, 60_220),
        ),
        (
            "rich-fibre closure-40",
            difference_set(POINTS[:40]),
            (1_634_032, 1_481_835, 13, 2_004_548),
        ),
        (
            "rich-fibre radial-8",
            radial_set(8),
            (89_528, 18_069, 18, 645_476),
        ),
        (
            "rich-fibre radial-12",
            radial_set(12),
            (693_008, 79_157, 35, 9_209_244),
        ),
    )
    for name, differences, expected in fibre_families:
        actual = rich_fibre_profile(differences)
        assert actual == expected
        print(name, actual)

    costas_expected = {
        11: ((6, 6), (91, 707, 10_857, 2_496, 4),
             (2_496, 2_416, 2, 2_656)),
        17: ((-11, 11), (241, 2_299, 67_873, 9_504, 4),
             (9_504, 9_466, 2, 9_580)),
        23: ((13, 13), (463, 4_513, 304_953, 90_584, 12),
             (90_584, 83_812, 4, 104_880)),
        31: ((-22, 23), (871, 9_495, 885_841, 127_200, 12),
             (127_200, 123_278, 3, 135_112)),
    }
    for prime, (expected_transform, expected_popular, expected_fibre) in (
        costas_expected.items()
    ):
        points = welch(prime)
        shear, stretch = smallest_transform(points)
        assert (shear, stretch) == expected_transform
        points = [
            (x + shear * y, stretch * y)
            for x, y in points
        ]
        differences = difference_set(points)
        assert popular_profile(differences) == expected_popular
        actual_fibre = rich_fibre_profile(differences)
        assert actual_fibre == expected_fibre
        print(f"rich-fibre Costas-{prime}", actual_fibre)

    zero_tail_families = (
        ("parabola-31", difference_set(transform(parabola(31)))),
        ("dense-perpendicular-40", difference_set(dense_perpendicular_points())),
        ("quadratic-18", difference_set(concrete_quadratic_instance()[0])),
    )
    for name, differences in zero_tail_families:
        assert print_profile(name, differences) == 0

    radial_ratios = []
    for side in (8, 12, 20, 30):
        ratio = print_profile(f"radial-{side}", radial_set(side))
        radial_ratios.append(ratio)
    assert radial_ratios[0] > 2
    assert radial_ratios[-1] > 16
    assert all(
        later > earlier
        for earlier, later in zip(radial_ratios, radial_ratios[1:])
    )

    print("support-adaptive popular-overlap gate: PASS")


if __name__ == "__main__":
    main()
