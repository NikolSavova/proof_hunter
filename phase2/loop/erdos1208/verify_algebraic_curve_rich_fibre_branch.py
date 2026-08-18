#!/usr/bin/env python3
"""Exact regressions for ALGEBRAIC_CURVE_RICH_FIBRE_BRANCH.md."""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable


Point = tuple[int, int]


def linear(point: Point) -> Point:
    """Apply I+J: (x,y) -> (x-y,x+y)."""
    return point[0] - point[1], point[0] + point[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def image_profile(points: list[Point]) -> tuple[int, int]:
    counts = Counter(
        subtract(left, linear(right))
        for left in points
        for right in points
    )
    return len(counts), max(counts.values())


def verify_family(
    name: str,
    parameterization: Callable[[int], Point],
    degree: int,
) -> None:
    for size in (5, 11, 23, 47):
        parameters = [index * index + 3 * index + 1 for index in range(size)]
        points = [parameterization(value) for value in parameters]
        assert len(set(points)) == size
        support, maximum_fibre = image_profile(points)
        assert maximum_fibre <= degree * degree
        assert support * degree * degree >= size * size
    print(name, "degree", degree, "PASS")


def main() -> None:
    verify_family("line", lambda t: (2 * t + 1, 5 * t - 3), 1)
    verify_family("parabola", lambda t: (t, t * t + 2 * t), 2)
    verify_family("cubic", lambda t: (t, t**3 - 2 * t), 3)
    print("algebraic-curve rich-fibre branch: PASS")


if __name__ == "__main__":
    main()
