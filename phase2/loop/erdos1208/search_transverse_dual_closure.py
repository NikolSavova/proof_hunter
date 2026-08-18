#!/usr/bin/env python3
"""Try to force one heavy row and one heavy colour simultaneously.

The fixed row is ``d=FIXED_DIFFERENCE`` in

    d = f + J e,

and the fixed colour is ``e=FIXED_DIFFERENCE`` (so its translation is
``J e``).  Candidates forced by either four-point relation are pooled, exact
distance-Sidon feasibility is enforced, and the product of the two exact
counts is greedily maximized.  This is deterministic falsification machinery
for the proposed row/colour uncertainty gate.
"""

from __future__ import annotations

import argparse

from search_rotated_support import is_distance_sidon
from search_transverse_closure import (
    candidate_overlap,
    forced_candidates as row_candidates,
    old_squared_distances,
    preserves_distance_sidon,
)
from search_transverse_color_closure import (
    candidate_count,
    colour_count,
    forced_candidates as colour_candidates,
)
from verify_transverse_closure_witness import FIXED_DIFFERENCE, POINTS
from verify_transverse_local_gate import differences, local_overlap


def extend(points: list[tuple[int, int]], target_size: int) -> list[tuple[int, int]]:
    assert is_distance_sidon(points)
    assert FIXED_DIFFERENCE in differences(points)
    while len(points) < target_size:
        old_distances = old_squared_distances(points)
        old_difference_set = differences(points)
        old_row = local_overlap(FIXED_DIFFERENCE, old_difference_set)
        old_colour = colour_count(old_difference_set)
        candidates = row_candidates(points) | colour_candidates(points)

        best: tuple[int, int, int, tuple[int, int]] | None = None
        valid_count = 0
        for candidate in candidates:
            if not preserves_distance_sidon(candidate, points, old_distances):
                continue
            valid_count += 1
            row = candidate_overlap(
                candidate,
                points,
                old_difference_set,
                old_row,
            )
            colour = candidate_count(
                candidate,
                points,
                old_difference_set,
                old_colour,
            )
            # Product first, then the smaller count, then deterministic ties.
            choice = row * colour, min(row, colour), row + colour, candidate
            if best is None or choice > best:
                best = choice

        if best is None:
            print("STOP no valid forced candidate", len(points), flush=True)
            break

        _, _, _, candidate = best
        points.append(candidate)
        difference_set = differences(points)
        row = local_overlap(FIXED_DIFFERENCE, difference_set)
        colour = colour_count(difference_set)
        assert is_distance_sidon(points)
        print(
            "STEP",
            len(points),
            candidate,
            "valid",
            valid_count,
            "row",
            row,
            "colour",
            colour,
            "product_ratio",
            f"{row * colour / len(points) ** 3:.6f}",
            flush=True,
        )
    return points


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=16)
    parser.add_argument("--target", type=int, default=50)
    args = parser.parse_args()
    if not (16 <= args.start <= len(POINTS)):
        raise ValueError("--start must include the certified fixed edge")
    points = extend(list(POINTS[: args.start]), args.target)
    print("POINTS =", repr(points))


if __name__ == "__main__":
    main()
