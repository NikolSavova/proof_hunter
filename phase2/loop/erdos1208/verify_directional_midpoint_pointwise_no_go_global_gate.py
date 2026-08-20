#!/usr/bin/env python3
"""Checks for DIRECTIONAL_MIDPOINT_POINTWISE_NO_GO_GLOBAL_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import gcd
import sys

sys.path.insert(0, "phase2/loop/erdos1208")

from verify_adaptive_cross_pair_transpose_graph import (  # noqa: E402
    transformed_costas,
)
from verify_ambient_centroid_endpoint_difference_hypergraph_gate import (  # noqa: E402
    directed_edges,
    primitive_unoriented,
    residue_parabola,
    shear,
)
from verify_large_determinant_closed_fibre_energy_gate import (  # noqa: E402
    direction_fibres,
)
from verify_metric_scalar_fourier_endpoint_no_go import (  # noqa: E402
    two_arm_instance,
)
from verify_transverse_closure_witness import POINTS  # noqa: E402

Point = tuple[int, int]
Direction = tuple[int, int]


def coordinate_height(points: list[Point]) -> int:
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    return max(max(xs) - min(xs), max(ys) - min(ys))


def directional_midpoint_profile(
    points: list[Point],
) -> tuple[
    Counter[Direction],
    dict[Direction, set[int]],
    dict[Point, int],
]:
    """Return H_w, direction contents, and clean midpoint loads L(q)."""
    _, by_vector = directed_edges(points)
    contents: dict[Direction, set[int]] = defaultdict(set)
    for first, second in combinations(range(len(points)), 2):
        vector = (
            points[second][0] - points[first][0],
            points[second][1] - points[first][1],
        )
        direction = primitive_unoriented(vector)
        contents[direction].add(gcd(abs(vector[0]), abs(vector[1])))

    pair_by_sum: dict[Point, tuple[int, int]] = {}
    for first, second in combinations(range(len(points)), 2):
        pair_sum = (
            points[first][0] + points[second][0],
            points[first][1] + points[second][1],
        )
        assert pair_sum not in pair_by_sum
        pair_by_sum[pair_sum] = (first, second)

    directional_loads: Counter[Direction] = Counter()
    midpoint_loads: dict[Point, int] = {}
    for direction, direction_contents in contents.items():
        for content in direction_contents:
            vector = (
                content * direction[0],
                content * direction[1],
            )
            distinguished_edge = by_vector[vector]
            load = 0
            for source_sum, source_pair in pair_by_sum.items():
                target_sum = (
                    source_sum[0] - vector[0],
                    source_sum[1] - vector[1],
                )
                target_pair = pair_by_sum.get(target_sum)
                if target_pair is None:
                    continue
                if len(set(distinguished_edge + source_pair + target_pair)) == 6:
                    load += 1
            midpoint_loads[vector] = load
            directional_loads[direction] += 4 * load

    return directional_loads, contents, midpoint_loads


def closed_fibre_profile(points: list[Point]) -> Counter[Direction]:
    by_vector, contents, partners, fibres = direction_fibres(points)
    profile: Counter[Direction] = Counter()
    for direction, direction_contents in contents.items():
        partner = partners[direction]
        for residue, fibre in fibres[direction].items():
            for content in direction_contents:
                first = (
                    content * direction[0],
                    content * direction[1],
                )
                for longitudinal in fibre:
                    if longitudinal + content not in fibre:
                        continue
                    second = (
                        longitudinal * direction[0]
                        + residue * partner[0],
                        longitudinal * direction[1]
                        + residue * partner[1],
                    )
                    third = (
                        -first[0] - second[0],
                        -first[1] - second[1],
                    )
                    endpoints = (
                        by_vector[first]
                        + by_vector[second]
                        + by_vector[third]
                    )
                    profile[direction] += len(set(endpoints)) == 6
    return profile


def directional_envelope(
    points: list[Point],
) -> tuple[int, Fraction, Fraction, tuple[Fraction, Direction, int, int]]:
    loads, contents, _ = directional_midpoint_profile(points)
    height = coordinate_height(points)
    k = len(points)
    denominator = sum(
        (
            Fraction(k * len(contents[direction]))
            + Fraction(
                height * height,
                max(abs(direction[0]), abs(direction[1])) ** 2,
            )
        )
        for direction in contents
    )
    rows = [
        (
            Fraction(loads[direction], 1)
            / (
                Fraction(k * len(contents[direction]))
                + Fraction(
                    height * height,
                    max(abs(direction[0]), abs(direction[1])) ** 2,
                )
            ),
            direction,
            loads[direction],
            len(contents[direction]),
        )
        for direction in contents
    ]
    return sum(loads.values()), denominator, max(row[0] for row in rows), max(rows)


def main() -> None:
    # Independent equality of the midpoint and closed-fibre formulations.
    small = shear(residue_parabola(7), 4)
    midpoint_small, _, _ = directional_midpoint_profile(small)
    assert midpoint_small == closed_fibre_profile(small)
    assert sum(midpoint_small.values()) == 72

    stress = shear(residue_parabola(43), 28)
    total, denominator, maximum_ratio, maximum_row = directional_envelope(stress)
    assert total == 380_556
    assert maximum_row[1:] == ((539, 19), 528, 1)
    assert maximum_ratio == Fraction(38_348_772, 3_468_257)
    assert total < denominator

    # The pointwise ratio grows throughout the standard genuine sheared
    # parabola certificates.
    expected_maxima = {
        7: 0.4585759068517689,
        11: 1.0666666666666667,
        13: 1.8110561261283664,
        17: 2.0823401950162514,
        19: 3.334786689377424,
        23: 4.57488255970566,
        29: 5.261750530488707,
        43: 11.057073336837496,
    }
    shears = {7: 4, 11: 6, 13: 6, 17: 11, 19: 10, 23: 13, 29: 14, 43: 28}
    for prime, shear_value in shears.items():
        _, _, ratio, _ = directional_envelope(
            shear(residue_parabola(prime), shear_value)
        )
        assert abs(float(ratio) - expected_maxima[prime]) < 1e-12

    # Other genuine distance-Sidon stresses satisfy the proposed summed
    # inequality with constant one; this is evidence, not a proof.
    families = {
        "closure-20": POINTS[:20],
        "closure-40": POINTS[:40],
        "Costas-17": transformed_costas(17),
        "Costas-23": transformed_costas(23),
        "two-arm-16": two_arm_instance(16)[0],
    }
    expected_totals = {
        "closure-20": 1_296,
        "closure-40": 24_840,
        "Costas-17": 3_816,
        "Costas-23": 18_684,
        "two-arm-16": 3_672,
    }
    for name, points in families.items():
        family_total, family_denominator, _, _ = directional_envelope(points)
        assert family_total == expected_totals[name]
        assert family_total <= family_denominator

    print("directional midpoint pointwise no-go/global gate: PASS")
    print(
        "p=43:",
        f"sum_Hw={total}, global_ratio={float(Fraction(total, 1) / denominator):.6f},",
        f"max_pointwise_ratio={float(maximum_ratio):.6f}, direction={maximum_row[1]}",
    )


if __name__ == "__main__":
    main()
