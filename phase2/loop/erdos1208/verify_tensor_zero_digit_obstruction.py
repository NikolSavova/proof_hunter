#!/usr/bin/env python3
"""Exact audit of the zero-digit flaw in the discarded tensor argument."""

from __future__ import annotations


Point = tuple[int, int]


BASE: tuple[Point, ...] = (
    (1, 2),
    (4, 6),
    (4, 4),
    (9, 12),
    (8, 8),
    (10, 10),
)


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def multiply(weight: Point, point: Point) -> Point:
    """Multiply two Gaussian integers."""
    a, b = weight
    x, y = point
    return a * x - b * y, a * y + b * x


def squared_norm(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def difference_set(points: set[Point]) -> set[Point]:
    return {subtract(first, second) for first in points for second in points}


def repeated_squared_distances(points: set[Point]) -> bool:
    seen: set[int] = set()
    ordered = sorted(points)
    for index, first in enumerate(ordered):
        for second in ordered[:index]:
            value = squared_norm(subtract(first, second))
            if value in seen:
                return True
            seen.add(value)
    return False


def main() -> None:
    # This weight is large enough to make the two-coordinate digit map
    # injective; no genericity or floating-point calculation is involved.
    weight = (100, 37)
    tensor = {
        add(first, multiply(weight, second))
        for first in BASE
        for second in BASE
    }
    assert len(tensor) == len(BASE) ** 2 == 36

    b, c, x, y = BASE[:4]
    first_pair = (
        add(b, multiply(weight, x)),
        add(c, multiply(weight, x)),
    )
    second_pair = (
        add(b, multiply(weight, y)),
        add(c, multiply(weight, y)),
    )
    assert set(first_pair) != set(second_pair)
    first_difference = subtract(*first_pair)
    second_difference = subtract(*second_pair)
    assert first_difference == second_difference == subtract(b, c)
    assert squared_norm(first_difference) == squared_norm(second_difference)
    assert repeated_squared_distances(tensor)

    base_differences = difference_set(set(BASE))
    tensor_differences = difference_set(tensor)
    assert len(base_differences) == 31
    assert len(tensor_differences) == 31**2 == 961
    required_if_sidon = len(tensor) * (len(tensor) - 1) + 1
    assert required_if_sidon == 1261
    assert len(tensor_differences) < required_if_sidon

    print("base/tensor sizes", len(BASE), len(tensor))
    print("repeated displacement", first_difference)
    print("actual/required difference counts", len(tensor_differences), required_if_sidon)
    print("tensor zero-digit obstruction: PASS")


if __name__ == "__main__":
    main()
