#!/usr/bin/env python3
"""Stress-test a fixed-colour version of the transverse-energy gate.

Fix a realized edge ``t`` and put ``q=Jt``.  Its contribution to the global
transverse count is

    #{f in D : f+q in D and det(q,f) != 0},  D=A-A.

Every such occurrence is a signed four-point relation

    a-b-c+e=q.

Starting from the certified closure witness, this script repeatedly generates
all integral points forced by three roles of that relation, rejects every point
that repeats a Euclidean distance, and greedily maximizes the exact fixed-colour
count.  It is deterministic falsification machinery, not part of a proof.
"""

from __future__ import annotations

import argparse
from itertools import product

from search_rotated_support import is_distance_sidon
from search_transverse_closure import (
    Point,
    add,
    negate,
    old_squared_distances,
    preserves_distance_sidon,
    subtract,
)
from verify_transverse_closure_witness import FIXED_DIFFERENCE, POINTS
from verify_transverse_local_gate import differences


TRANSLATION = (-FIXED_DIFFERENCE[1], FIXED_DIFFERENCE[0])
ROLE_SIGNS = (1, -1, -1, 1)


def scale(sign: int, point: Point) -> Point:
    return point if sign == 1 else negate(point)


def forced_candidates(points: list[Point]) -> set[Point]:
    candidates: set[Point] = set()
    point_set = set(points)
    for missing in range(4):
        present = [role for role in range(4) if role != missing]
        for chosen in product(points, repeat=3):
            total = (0, 0)
            for role, point in zip(present, chosen):
                total = add(total, scale(ROLE_SIGNS[role], point))
            residual = subtract(TRANSLATION, total)
            candidate = scale(ROLE_SIGNS[missing], residual)
            if candidate not in point_set:
                candidates.add(candidate)
    return candidates


def is_transverse(edge: Point) -> bool:
    return (
        TRANSLATION[0] * edge[1]
        - TRANSLATION[1] * edge[0]
        != 0
    )


def colour_count(difference_set: set[Point]) -> int:
    return sum(
        is_transverse(edge)
        and add(edge, TRANSLATION) in difference_set
        for edge in difference_set
    )


def candidate_count(
    candidate: Point,
    points: list[Point],
    old_difference_set: set[Point],
    old_count: int,
) -> int:
    new_differences = {
        edge
        for point in points
        for edge in (
            subtract(candidate, point),
            subtract(point, candidate),
        )
    }
    full_difference_set = old_difference_set | new_differences
    new_as_source = sum(
        is_transverse(edge)
        and add(edge, TRANSLATION) in full_difference_set
        for edge in new_differences
    )
    old_as_source = sum(
        is_transverse(edge)
        and add(edge, TRANSLATION) in new_differences
        for edge in old_difference_set
    )
    return old_count + new_as_source + old_as_source


def extend(points: list[Point], target_size: int) -> list[Point]:
    assert is_distance_sidon(points)
    assert FIXED_DIFFERENCE in differences(points)
    while len(points) < target_size:
        old_distances = old_squared_distances(points)
        old_difference_set = differences(points)
        old_count = colour_count(old_difference_set)
        candidates = forced_candidates(points)

        best: tuple[int, Point] | None = None
        valid_count = 0
        for candidate in candidates:
            if not preserves_distance_sidon(candidate, points, old_distances):
                continue
            valid_count += 1
            score = candidate_count(
                candidate,
                points,
                old_difference_set,
                old_count,
            )
            choice = score, candidate
            if best is None or choice > best:
                best = choice

        if best is None:
            print("STOP no valid forced candidate", len(points), flush=True)
            break

        score, candidate = best
        points.append(candidate)
        exact = colour_count(differences(points))
        assert exact == score
        assert is_distance_sidon(points)
        print(
            "STEP",
            len(points),
            candidate,
            "valid",
            valid_count,
            "count",
            exact,
            "ratio",
            f"{exact / len(points):.6f}",
            "sqrt_ratio",
            f"{exact / len(points) ** 1.5:.6f}",
            flush=True,
        )
    return points


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=len(POINTS))
    parser.add_argument("--target", type=int, default=len(POINTS) + 10)
    args = parser.parse_args()
    if not (16 <= args.start <= len(POINTS)):
        raise ValueError("--start must include the certified fixed edge")
    points = extend(list(POINTS[: args.start]), args.target)
    print("POINTS =", repr(points))


if __name__ == "__main__":
    main()
