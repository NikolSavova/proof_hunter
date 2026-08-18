#!/usr/bin/env python3
"""Extend the exact relation-closure adversary for the transverse local gate.

For a fixed realized difference d, every local relation has the form

    u - v + J(x - y) = d.

Starting from the certified witness, this script generates every integral point
obtained by choosing three roles from the current set and solving for the fourth.
It rejects candidates that repeat a Euclidean distance and greedily maximizes the
new exact local overlap.  The search is deterministic; it is evidence/falsification
machinery, not part of a proof.
"""

from __future__ import annotations

import argparse
from itertools import product

from search_rotated_support import is_distance_sidon
from verify_transverse_closure_witness import (
    FIXED_DIFFERENCE,
    POINTS,
    relation_degeneracy,
)
from verify_transverse_local_gate import differences, local_overlap

Point = tuple[int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def negate(point: Point) -> Point:
    return -point[0], -point[1]


def quarter_turn(point: Point) -> Point:
    return -point[1], point[0]


def inverse_quarter_turn(point: Point) -> Point:
    return point[1], -point[0]


def scale_by_role(role: int, point: Point) -> Point:
    """Coefficient of u,v,x,y in u-v+Jx-Jy, respectively."""
    if role == 0:
        return point
    if role == 1:
        return negate(point)
    if role == 2:
        return quarter_turn(point)
    if role == 3:
        return negate(quarter_turn(point))
    raise ValueError(role)


def divide_by_role(role: int, point: Point) -> Point:
    """Divide a Gaussian integer point by the unit coefficient of a role."""
    if role == 0:
        return point
    if role == 1:
        return negate(point)
    if role == 2:
        return inverse_quarter_turn(point)
    if role == 3:
        return quarter_turn(point)
    raise ValueError(role)


def forced_candidates(points: list[Point]) -> set[Point]:
    candidates: set[Point] = set()
    point_set = set(points)
    for missing in range(4):
        present = [role for role in range(4) if role != missing]
        for chosen in product(points, repeat=3):
            total = (0, 0)
            for role, point in zip(present, chosen):
                total = add(total, scale_by_role(role, point))
            residual = subtract(FIXED_DIFFERENCE, total)
            candidate = divide_by_role(missing, residual)
            if candidate not in point_set:
                candidates.add(candidate)
    return candidates


def squared_distance(left: Point, right: Point) -> int:
    dx = left[0] - right[0]
    dy = left[1] - right[1]
    return dx * dx + dy * dy


def old_squared_distances(points: list[Point]) -> set[int]:
    return {
        squared_distance(points[i], points[j])
        for i in range(len(points))
        for j in range(i)
    }


def preserves_distance_sidon(
    candidate: Point,
    points: list[Point],
    old_distances: set[int],
) -> bool:
    new_distances = [squared_distance(candidate, point) for point in points]
    return (
        len(set(new_distances)) == len(new_distances)
        and old_distances.isdisjoint(new_distances)
    )


def inverse_affine_turn(point: Point) -> Point:
    # T_d(e)=d-J(e), so T_d^{-1}(f)=-J(d-f)=J(f-d).
    return quarter_turn(subtract(point, FIXED_DIFFERENCE))


def is_transverse(edge: Point) -> bool:
    return (
        FIXED_DIFFERENCE[0] * edge[0]
        + FIXED_DIFFERENCE[1] * edge[1]
        != 0
    )


def candidate_overlap(
    candidate: Point,
    points: list[Point],
    old_difference_set: set[Point],
    old_overlap: int,
) -> int:
    new_differences = {
        difference
        for point in points
        for difference in (
            subtract(candidate, point),
            subtract(point, candidate),
        )
    }
    full_difference_set = old_difference_set | new_differences

    new_as_source = sum(
        is_transverse(edge)
        and subtract(FIXED_DIFFERENCE, quarter_turn(edge))
        in full_difference_set
        for edge in new_differences
    )
    old_as_source = sum(
        inverse_affine_turn(image) in old_difference_set
        and is_transverse(inverse_affine_turn(image))
        for image in new_differences
    )
    return old_overlap + new_as_source + old_as_source


def extend(points: list[Point], target_size: int) -> list[Point]:
    assert is_distance_sidon(points)
    while len(points) < target_size:
        old_distances = old_squared_distances(points)
        old_difference_set = differences(points)
        old_overlap = local_overlap(FIXED_DIFFERENCE, old_difference_set)
        candidates = forced_candidates(points)

        best: tuple[int, Point] | None = None
        valid_count = 0
        for candidate in candidates:
            if not preserves_distance_sidon(candidate, points, old_distances):
                continue
            valid_count += 1
            score = candidate_overlap(
                candidate,
                points,
                old_difference_set,
                old_overlap,
            )
            choice = score, candidate
            if best is None or choice > best:
                best = choice

        if best is None:
            print("STOP no valid forced candidate", len(points), flush=True)
            break

        score, candidate = best
        points.append(candidate)
        exact = local_overlap(FIXED_DIFFERENCE, differences(points))
        assert exact == score
        assert is_distance_sidon(points)
        degeneracy = relation_degeneracy(points)
        print(
            "STEP",
            len(points),
            candidate,
            "valid",
            valid_count,
            "overlap",
            exact,
            "ratio",
            f"{exact / len(points):.6f}",
            "degeneracy",
            degeneracy,
            flush=True,
        )
    return points


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=len(POINTS))
    parser.add_argument("--target", type=int, default=len(POINTS) + 10)
    args = parser.parse_args()
    if not (2 <= args.start <= len(POINTS)):
        raise ValueError("--start must select a certified POINTS prefix")
    points = extend(list(POINTS[: args.start]), args.target)
    print("POINTS =", repr(points))


if __name__ == "__main__":
    main()
