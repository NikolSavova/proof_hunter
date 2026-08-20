#!/usr/bin/env python3
"""Exact checks for GAUSSIAN_MULTIPLIER_ORTHOGONALITY_AUDIT.md."""

from __future__ import annotations

from itertools import combinations
from math import comb, isqrt

from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]


def norm2(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def multiply(alpha: Point, vector: Point) -> Point:
    a, b = alpha
    x, y = vector
    return a * x - b * y, b * x + a * y


def gaussian_multipliers(norm: int) -> list[Point]:
    """One representative of every Gaussian integer modulo sign."""
    radius = isqrt(norm)
    output = []
    for a in range(-radius, radius + 1):
        for b in range(-radius, radius + 1):
            if a * a + b * b != norm:
                continue
            if a > 0 or (a == 0 and b > 0):
                output.append((a, b))
    return output


def directed_differences(points: list[Point]) -> set[Point]:
    output = {
        (left[0] - right[0], left[1] - right[1])
        for left in points
        for right in points
        if left != right
    }
    assert len(output) == len(points) * (len(points) - 1)
    squared_norms = {norm2(vector) for vector in output}
    assert len(squared_norms) == comb(len(points), 2)
    return output


def shell_audit(points: list[Point], norm: int) -> tuple[int, int, int, int]:
    multipliers = gaussian_multipliers(norm)
    difference = directed_differences(points)
    supports = [
        {multiply(alpha, vector) for vector in difference}
        for alpha in multipliers
    ]
    k = len(points)
    r = len(multipliers)

    assert all(len(support) == k * (k - 1) for support in supports)
    for left, right in combinations(supports, 2):
        assert left.isdisjoint(right)
        # The zero coefficient contributes k^2; there is no nonzero overlap.
        assert k * k + len(left & right) == k * k

    union = set().union(*supports)
    assert len(union) == r * k * (k - 1)
    coordinate_radius = max(
        max(abs(x), abs(y)) for support in supports for x, y in support
    )
    width = max(
        max(point[0] for point in points) - min(point[0] for point in points),
        max(point[1] for point in points) - min(point[1] for point in points),
    )
    maximum_l1 = max(abs(a) + abs(b) for a, b in multipliers)
    assert maximum_l1 * maximum_l1 <= 2 * norm
    assert coordinate_radius <= width * maximum_l1

    # Exact summed L2 moment from all diagonal and cross terms.
    individual_second_moment = 2 * k * k - k
    summed_second_moment = (
        r * individual_second_moment + r * (r - 1) * k * k
    )
    expected = r * r * k * k + r * k * (k - 1)
    assert summed_second_moment == expected

    box_capacity = (2 * coordinate_radius + 1) ** 2 - 1
    assert len(union) <= box_capacity
    return norm, r, len(union), summed_second_moment


def representation_audit(limit: int = 5_000) -> tuple[int, int, int]:
    best_n = 0
    best_r = 0
    for norm in range(1, limit + 1):
        r = len(gaussian_multipliers(norm))
        assert r <= 2 * norm
        if r and (best_n == 0 or norm * best_r < best_n * r):
            best_n, best_r = norm, r
    assert (best_n, best_r) == (1, 2)
    return best_n, best_r, limit


def main() -> None:
    points = POINTS[:20]
    expected = {
        1: (1, 2, 760, 2_360),
        5: (5, 4, 1_520, 7_920),
        25: (25, 6, 2_280, 16_680),
        65: (65, 8, 3_040, 28_640),
        325: (325, 12, 4_560, 62_160),
        1_105: (1_105, 16, 6_080, 108_480),
    }
    for norm, wanted in expected.items():
        actual = shell_audit(points, norm)
        assert actual == wanted, (norm, actual, wanted)
        print("common-norm shell", actual)

    scan = representation_audit()
    print("best n/r scan", scan)

    large_expected = {
        1_105: 16,
        5_525: 24,
        27_625: 32,
        160_225: 48,
        801_125: 64,
    }
    for norm, wanted in large_expected.items():
        actual = len(gaussian_multipliers(norm))
        assert actual == wanted, (norm, actual, wanted)
        print("large shell", norm, actual, norm / actual)

    print("Gaussian multiplier orthogonality audit: PASS")


if __name__ == "__main__":
    main()
