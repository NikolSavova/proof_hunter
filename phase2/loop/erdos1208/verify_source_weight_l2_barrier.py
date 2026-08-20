#!/usr/bin/env python3
"""Exact profiles for SOURCE_WEIGHT_L2_SIZE_BIASED_BARRIER.md."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_third_additive_energy_barrier import parabola, transform
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]


def distance2(first: Point, second: Point) -> int:
    return (first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2


def edge_labels(points: list[Point]) -> tuple[dict[Point, int], list[int]]:
    labels: dict[Point, int] = {}
    distances: list[int] = []
    for first, second in combinations(points, 2):
        pair_sum = first[0] + second[0], first[1] + second[1]
        label = distance2(first, second)
        assert pair_sum not in labels
        labels[pair_sum] = label
        distances.append(label)
    assert len(distances) == len(set(distances))
    return labels, distances


def dyadic_group(points: list[Point], h: int) -> list[list[Point]]:
    return [
        starts
        for starts in clean_start_fibres(points).values()
        if h <= len(starts) < 2 * h
    ]


def profile(points: list[Point], h: int) -> tuple[int | Fraction, ...]:
    k = len(points)
    n = k * (k - 1) // 2
    labels, distances = edge_labels(points)
    group = dyadic_group(points, h)
    q_count = len(group)
    total_mass = sum(map(len, group))
    second_row_mass = sum(len(starts) * (len(starts) - 1) for starts in group)

    full_source_weight: Counter[int] = Counter()
    divisible_source_weight: Counter[int] = Counter()
    codegrees: Counter[tuple[Point, Point]] = Counter()
    for starts in group:
        values = [labels[start] for start in starts]
        for first in starts:
            for second in starts:
                codegrees[first, second] += 1
        for first in values:
            for second in values:
                gap = first - second
                if not gap:
                    continue
                full_source_weight[gap] += 1
                if gap % 18 == 0:
                    divisible_source_weight[-gap // 18] += 1

    assert sum(full_source_weight.values()) == second_row_mass
    full_l2 = sum(value * value for value in full_source_weight.values())
    assert full_l2 * n * (n - 1) >= second_row_mass * second_row_mass
    assert full_l2 < 2 * h * total_mass * total_mass

    # Scaling every point by six multiplies every squared distance by 36.
    # Hence all source gaps become divisible by 18, and the resulting C_*
    # is exactly the full source weight under the injective key gap -> -2gap.
    scaled_source_weight = Counter({-2 * gap: value for gap, value in full_source_weight.items()})
    assert sum(value * value for value in scaled_source_weight.values()) == full_l2
    assert sum(scaled_source_weight.values()) == second_row_mass

    distance_gaps = Counter(first - second for first in distances for second in distances)
    fourth_incidence_moment = sum(value * value for value in codegrees.values())
    tilted_l2 = sum(
        Fraction(value * value, distance_gaps[-18 * gap])
        for gap, value in divisible_source_weight.items()
    )
    assert tilted_l2 <= fourth_incidence_moment
    assert fourth_incidence_moment <= 2 * total_mass * total_mass
    assert fourth_incidence_moment <= 4 * h * n * total_mass

    sufficient_scale = Fraction(
        n * (total_mass + k**3) ** 2,
        k**4,
    )
    ratio = Fraction(full_l2, 1) / sufficient_scale

    return (
        k,
        h,
        q_count,
        total_mass,
        second_row_mass,
        len(full_source_weight),
        max(full_source_weight.values(), default=0),
        full_l2,
        len(divisible_source_weight),
        sum(divisible_source_weight.values()),
        sum(value * value for value in divisible_source_weight.values()),
        fourth_incidence_moment,
        tilted_l2,
        ratio,
    )


def main() -> None:
    families = [
        ("closure-40", POINTS[:40], 8),
        ("parabola-31", transform(parabola(31)), 64),
        ("parabola-43", transform(parabola(43)), 128),
    ]
    expected_prefixes = {
        "closure-40": (
            40, 8, 694, 7_500, 77_136, 31_254, 24, 337_112,
            1_976, 5_546, 29_738, 225_724,
        ),
        "parabola-31": (
            31, 64, 262, 18_484, 1_291_164, 187_010, 42, 13_860_724,
            24_320, 173_380, 1_925_608, 14_458_572,
        ),
        "parabola-43": (
            43, 128, 598, 84_220, 11_823_100, 755_526, 130, 287_882_776,
            93_362, 1_505_624, 38_078_560, 286_617_058,
        ),
    }
    expected_tilted = {
        "closure-40": Fraction(
            85_845_880_880_289_116_019_912_838_789_427,
            56_888_532_886_874_893_290_342_154_080,
        ),
        "parabola-31": Fraction(8_945_031, 5),
        "parabola-43": Fraction(481_959_577, 14),
    }

    ratios: dict[str, float] = {}
    for name, points, h in families:
        actual = profile(points, h)
        assert actual[:12] == expected_prefixes[name], (name, actual[:12])
        assert actual[12] == expected_tilted[name], (name, actual[12])
        print(name)
        print("  k,h,Q,H,S2", actual[:5])
        print("  scaled-full support,max,L2", actual[5:8])
        print("  requested support,L1,L2", actual[8:11])
        print("  fourth incidence moment", actual[11])
        print("  tilted L2", actual[12], float(actual[12]))
        print("  sufficient-L2 ratio", float(actual[13]))
        ratios[name] = float(actual[13])

    assert ratios["parabola-31"] > 10
    assert ratios["parabola-43"] > 40
    print("source-weight L2 and size-biased barrier: PASS")


if __name__ == "__main__":
    main()
