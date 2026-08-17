#!/usr/bin/env python3
"""Exact finite checks for the parallel-line rotated-support lemma.

The proof in PARALLEL_LINE_SUPPORT_LEMMA.md is symbolic.  This verifier checks
its set identity and lower bound in every pair direction for deterministic
random-greedy distance-Sidon sets, together with the stored perpendicular
ruler witness.  It uses integer coordinates only.
"""

from __future__ import annotations

from collections import Counter
from math import gcd
import random


Point = tuple[int, int]


def norm_squared(left: Point, right: Point) -> int:
    return (left[0] - right[0]) ** 2 + (left[1] - right[1]) ** 2


def is_distance_sidon(points: list[Point]) -> bool:
    distances = [
        norm_squared(points[i], points[j])
        for i in range(len(points))
        for j in range(i)
    ]
    return len(distances) == len(set(distances))


def greedy(side: int, seed: int) -> list[Point]:
    rng = random.Random(seed)
    universe = [(x, y) for x in range(side) for y in range(side)]
    rng.shuffle(universe)
    points: list[Point] = []
    distances: set[int] = set()
    for point in universe:
        new = [norm_squared(point, old) for old in points]
        if len(new) == len(set(new)) and distances.isdisjoint(new):
            points.append(point)
            distances.update(new)
    return points


def primitive_directions(points: list[Point]) -> set[Point]:
    result: set[Point] = set()
    for i, (x, y) in enumerate(points):
        for u, v in points[:i]:
            dx, dy = x - u, y - v
            divisor = gcd(abs(dx), abs(dy))
            dx, dy = dx // divisor, dy // divisor
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            result.add((dx, dy))
    return result


def full_support(points: list[Point]) -> set[Point]:
    return {
        (a[0] - b[1] + c[1], a[1] + b[0] - c[0])
        for a in points
        for b in points
        for c in points
    }


def check_direction(points: list[Point], direction: Point) -> None:
    dx, dy = direction
    lines: dict[int, list[Point]] = {}
    for point in points:
        lines.setdefault(dx * point[1] - dy * point[0], []).append(point)

    scalar_differences = {0}
    restricted_outputs: set[Point] = set()
    for line in lines.values():
        for b in line:
            for c in line:
                vector = (b[0] - c[0], b[1] - c[1])
                # The vector is an integer multiple of the primitive direction.
                scalar = vector[0] // dx if dx else vector[1] // dy
                assert vector == (scalar * dx, scalar * dy)
                scalar_differences.add(scalar)
                for a in points:
                    restricted_outputs.add(
                        (a[0] - vector[1], a[1] + vector[0])
                    )

    q_value = sum(len(line) * (len(line) - 1) for line in lines.values())
    projections = {dx * x + dy * y for x, y in points}
    assert len(scalar_differences) == q_value + 1
    assert len(restricted_outputs) >= len(points) + len(projections) * q_value
    assert restricted_outputs <= full_support(points)


def main() -> None:
    perpendicular = [
        (0, 0),
        (1, 0),
        (4, 0),
        (9, 0),
        (0, 16),
        (0, 23),
        (0, 33),
        (0, 35),
    ]
    instances = [perpendicular]
    instances.extend(greedy(side, 1208 + side) for side in range(5, 18))

    checks = 0
    for points in instances:
        assert is_distance_sidon(points)
        for direction in primitive_directions(points):
            check_direction(points, direction)
            checks += 1

    print("instances", len(instances))
    print("directions", checks)
    print("PASS")


if __name__ == "__main__":
    main()
