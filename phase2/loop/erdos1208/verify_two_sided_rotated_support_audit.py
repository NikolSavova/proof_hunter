#!/usr/bin/env python3
"""Exact checks for TWO_SIDED_ROTATED_SUPPORT_AUDIT.md."""

from __future__ import annotations

from collections import Counter
from itertools import product


def erdos_turan_ruler(prime: int) -> list[int]:
    return [2 * prime * i + (i * i) % prime for i in range(prime)]


def is_sidon(values: list[int]) -> bool:
    sums: dict[int, tuple[int, int]] = {}
    for i, left in enumerate(values):
        for j in range(i, len(values)):
            value = left + values[j]
            if value in sums:
                return False
            sums[value] = (i, j)
    return True


def direct_sum(left: list[int], right: list[int]) -> bool:
    return len({x + y for x in left for y in right}) == len(left) * len(right)


def check_product_injection(left: list[int], right: list[int]) -> None:
    images: dict[tuple[int, int], tuple[int, int, int, int]] = {}
    for x1, x2, y1, y2 in product(left, left, right, right):
        image = (x1 + y1 - y2, y2 + x2 - x1)
        assert image not in images
        images[image] = (x1, x2, y1, y2)
    assert len(images) == len(left) ** 2 * len(right) ** 2


def sub(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] - right[0], left[1] - right[1]


def add(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] + right[0], left[1] + right[1]


def rotate(point: tuple[int, int]) -> tuple[int, int]:
    return -point[1], point[0]


def distance_sidon(points: list[tuple[int, int]]) -> bool:
    seen: set[int] = set()
    for i, left in enumerate(points):
        for right in points[:i]:
            dx, dy = sub(left, right)
            norm = dx * dx + dy * dy
            if norm in seen:
                return False
            seen.add(norm)
    return True


def rotated_energy(points: list[tuple[int, int]]) -> int:
    representations: Counter[tuple[int, int]] = Counter()
    for a, b, c in product(points, repeat=3):
        representations[add(a, rotate(sub(b, c)))] += 1
    return sum(value * value for value in representations.values())


def centered_residual(points: list[tuple[int, int]]) -> int:
    differences = {
        sub(left, right)
        for left in points
        for right in points
        if left != right
    }
    total = 0
    for d, u, v in product(differences, repeat=3):
        if add(u, v) == rotate(d):
            total += 1
    return total


def main() -> None:
    prime = 17
    ruler = erdos_turan_ruler(prime)
    assert is_sidon(ruler)

    size = 8
    left = ruler[:size]
    right = ruler[-size:]
    assert set(left).isdisjoint(right)
    assert direct_sum(left, right)
    check_product_injection(left, right)

    first = {x + y - z for x in left for y in right for z in right}
    second = {y + x - z for y in right for x in left for z in left}
    assert len(first) * len(second) >= size**4
    interval_bound = 6 * prime * prime + 1
    assert len(first) <= interval_bound
    assert len(second) <= interval_bound

    points = [
        (0, 2),
        (2, 31),
        (8, 0),
        (13, 12),
        (17, 25),
        (18, 19),
        (20, 18),
        (24, 29),
    ]
    assert distance_sidon(points)

    differences = {
        sub(left_point, right_point)
        for left_point in points
        for right_point in points
    }
    rotated_differences = {rotate(value) for value in differences}
    assert differences & rotated_differences == {(0, 0)}

    k = len(points)
    energy = rotated_energy(points)
    residual = centered_residual(points)
    assert energy == 2 * k**3 - k**2 + residual

    print("two-sided rotated-support audit: PASS")
    print(f"Erdos--Turan prime={prime}, split sizes=({size},{size})")
    print(f"third-sum sizes=({len(first)},{len(second)})")
    print(f"rotated energy={energy}, centered residual={residual}")


if __name__ == "__main__":
    main()
