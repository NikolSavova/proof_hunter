#!/usr/bin/env python3
"""Exact audit of the shared-endpoint fixed-gap divisor obstruction."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb

from verify_metric_scalar_gap_codegree_barrier import (
    perpendicular_gap_family,
    squared_distance,
)


def divisor_count(value: int) -> int:
    value = abs(value)
    output = 1
    prime = 2
    while prime * prime <= value:
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        if exponent:
            output *= exponent + 1
        prime += 1
    if value > 1:
        output *= 2
    return output


def profile(length: int) -> tuple[int, ...]:
    points, gap, gap_load = perpendicular_gap_family(length)
    horizontal = points[: 2 * length]
    common_endpoints = points[2 * length :]
    first_marks = horizontal[0::2]
    partner_marks = horizontal[1::2]
    edge_count = comb(len(points), 2)

    factors = []
    minimum_determinant = None
    first_edges = []
    for first, partner in zip(first_marks, partner_marks):
        difference_factor = first[0] - partner[0]
        sum_factor = first[0] + partner[0]
        assert difference_factor * sum_factor == gap
        factors.append(abs(difference_factor))
        for endpoint in common_endpoints:
            assert (
                squared_distance(first, endpoint)
                - squared_distance(partner, endpoint)
                == gap
            )
            doubled_determinant = abs(
                2
                * (
                    (endpoint[0] - first[0])
                    * (endpoint[1] - partner[1])
                    - (endpoint[1] - first[1])
                    * (endpoint[0] - partner[0])
                )
            )
            minimum_determinant = (
                doubled_determinant
                if minimum_determinant is None
                else min(minimum_determinant, doubled_determinant)
            )
            first_edges.append((first, endpoint))
    assert len(factors) == len(set(factors))
    assert minimum_determinant is not None and minimum_determinant > edge_count

    degrees = Counter(point for edge in first_edges for point in edge)
    wedge_weight = sum(comb(degree, 2) for degree in degrees.values())
    expected_weight = length * comb(2 * length, 2) + 2 * length * comb(length, 2)
    assert wedge_weight == expected_weight
    assert gap_load == 2 * length * length
    assert length <= divisor_count(gap)

    return (
        len(points),
        edge_count,
        gap,
        divisor_count(gap),
        gap_load,
        wedge_weight,
        minimum_determinant,
        max(max(abs(x), abs(y)) for x, y in points),
    )


def main() -> None:
    expected = {
        2: (8, 28, 161_051, 6, 8, 16, 483_160, 241_594),
        4: (16, 120, 2_357_947_691, 10, 32, 160, 7_073_843_080, 3_536_921_794),
        8: (
            32,
            496,
            505_447_028_499_293_771,
            18,
            128,
            1_408,
            1_516_341_085_497_881_320,
            758_170_542_749_006_194,
        ),
    }
    for length, wanted in expected.items():
        actual = profile(length)
        assert actual == wanted, (length, actual, wanted)
        print("shared-endpoint divisor profile", length, actual)
    print("shared-endpoint bipartite scalar divisor no-go: PASS")


if __name__ == "__main__":
    main()
