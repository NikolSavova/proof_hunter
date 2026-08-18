#!/usr/bin/env python3
"""Exact certificate for the 45-point row/colour hybrid closure witness."""

from __future__ import annotations

from search_rotated_support import is_distance_sidon, support_size
from search_transverse_color_closure import colour_count
from verify_transverse_closure_witness import FIXED_DIFFERENCE
from verify_transverse_color_closure import maximum_collinearity, transverse_colour_counts
from verify_transverse_local_gate import differences, local_overlap


POINTS = [
    (0, 2), (2, 31), (8, 0), (13, 12), (17, 25), (18, 19),
    (20, 18), (24, 29), (29, 40), (35, 7), (36, 8), (39, 9),
    (41, 9), (46, 0), (46, 1), (50, 25), (12, 27), (69, -15),
    (63, -6), (53, -28), (54, -32), (43, 58), (-18, 41),
    (81, -22), (31, -68), (65, -63), (106, -38), (122, -44),
    (-43, 62), (84, 77), (78, 71), (-27, -50), (81, 119),
    (108, 46), (-24, -37), (-68, 79), (110, 116), (-56, 73),
    (175, -84), (-108, 103), (133, 155), (-43, -121),
    (-134, 126), (-68, -148), (-67, -100),
]


def main() -> None:
    assert len(POINTS) == 45
    assert is_distance_sidon(POINTS)
    difference_set = differences(POINTS)
    fixed_row = local_overlap(FIXED_DIFFERENCE, difference_set)
    fixed_colour = colour_count(difference_set)
    assert (fixed_row, fixed_colour) == (147, 292)

    rows = [local_overlap(edge, difference_set) for edge in difference_set]
    columns = list(transverse_colour_counts(difference_set).values())
    assert sum(rows) == sum(columns)
    assert sum(rows) == 64_912
    assert max(rows) == 147
    assert max(columns) == 292
    assert sum(value * value for value in rows) == 2_800_568
    assert sum(value * value for value in columns) == 3_316_352
    assert support_size(POINTS) == 66_203
    assert maximum_collinearity(POINTS) == 3

    print("points", len(POINTS))
    print("differences", len(difference_set))
    print("fixed_row", fixed_row)
    print("fixed_colour", fixed_colour)
    print("fixed_product", fixed_row * fixed_colour)
    print("global_transverse", sum(rows))
    print("row_second_moment", sum(value * value for value in rows))
    print("colour_second_moment", sum(value * value for value in columns))
    print("rotated_support", support_size(POINTS))
    print("maximum_collinearity", maximum_collinearity(POINTS))
    print("PASS")


if __name__ == "__main__":
    main()
