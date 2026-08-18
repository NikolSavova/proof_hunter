#!/usr/bin/env python3
"""Exact global profile of the 120-point transverse-closure witness."""

from __future__ import annotations

from search_rotated_support import is_distance_sidon, support_size
from verify_transverse_closure_witness import POINTS
from verify_transverse_color_closure import maximum_collinearity, transverse_colour_counts
from verify_transverse_local_gate import differences, local_overlap


def main() -> None:
    assert len(POINTS) == 120
    assert is_distance_sidon(POINTS)

    difference_set = differences(POINTS)
    overlaps = [local_overlap(d, difference_set) for d in difference_set]

    assert len(difference_set) == 120 * 119 + 1
    assert sum(overlaps) == 2_798_384
    assert max(overlaps) == 948
    assert sum(value * value for value in overlaps) == 726_091_848
    assert sum(value**3 for value in overlaps) == 222_525_228_920
    assert {
        threshold: sum(value >= threshold for value in overlaps)
        for threshold in (1, 2, 4, 8, 16, 32, 64, 128, 256, 512)
    } == {
        1: 14278,
        2: 14278,
        4: 14278,
        8: 14268,
        16: 14190,
        32: 13872,
        64: 12708,
        128: 9644,
        256: 4228,
        512: 24,
    }
    rotated_support = support_size(POINTS)
    assert rotated_support == 1_011_786
    colour_counts = transverse_colour_counts(difference_set)
    assert sum(colour_counts.values()) == sum(overlaps)
    assert max(colour_counts.values()) == 522
    assert sum(value * value for value in colour_counts.values()) == 718_246_448
    assert maximum_collinearity(POINTS) == 3

    print("points", len(POINTS))
    print("differences", len(difference_set))
    print("transverse_edges", sum(overlaps) // 2)
    print("maximum_local_overlap", max(overlaps))
    print("maximum_colour_overlap", max(colour_counts.values()))
    print("row_second_moment", sum(value * value for value in overlaps))
    print("colour_second_moment", sum(value * value for value in colour_counts.values()))
    print("rotated_support", rotated_support)
    print("maximum_collinearity", maximum_collinearity(POINTS))
    print("PASS")


if __name__ == "__main__":
    main()
