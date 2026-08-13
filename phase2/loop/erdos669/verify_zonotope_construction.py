#!/usr/bin/env python3
"""Exact verifier for the lattice-zonotope construction for Erdős #669.

The script uses only integer arithmetic and the Python standard library.  For
Simpson's nested minimum-area direction sets it verifies:

* determinant area D and family widths;
* the exact line count n=2Dq+k;
* all projective intersections and their complete multiplicities;
* the exact finite t_k count Dq^2+kq+1;
* the predicted q=1 points at infinity;
* pair counting and Melchior's inequality.

This is a verification artifact, not an independent proof that Simpson's listed
areas are globally minimal; that theorem is cited in ZONOTOPE_CONSTRUCTION.md.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from itertools import combinations
from math import comb, gcd
from typing import Iterable

Vector = tuple[int, int]
Line = tuple[int, int, int]
Point = tuple[int, int, int]


# Successive edge directions in Simpson's minimum-area parallel-sided polygons.
SIMPSON_DIRECTIONS: tuple[Vector, ...] = (
    (0, 1),
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 5),
    (1, 5),
    (2, 7),
    (1, 6),
    (2, 9),
    (1, 7),
)

SIMPSON_AREAS = {
    2: 1,
    3: 3,
    4: 7,
    5: 14,
    6: 24,
    7: 40,
    8: 59,
    9: 87,
    10: 121,
    11: 164,
}

PALASTI = {
    4: (7, 200),
    5: (2, 135),
    6: (47, 4860),
    7: (3, 490),
    8: (1, 270),
    9: (3, 1000),
    10: (1, 480),
    11: (1, 750),
}


def determinant(left: Vector, right: Vector) -> int:
    return left[0] * right[1] - left[1] * right[0]


def primitive_projective(v: Iterable[int]) -> tuple[int, int, int]:
    """Return the canonical primitive representative of a projective vector."""
    values = tuple(v)
    common = 0
    for value in values:
        common = gcd(common, abs(value))
    assert common > 0
    values = tuple(value // common for value in values)
    for value in values:
        if value:
            return tuple(-x for x in values) if value < 0 else values
    raise AssertionError("zero projective vector")


def intersection(left: Line, right: Line) -> Point:
    a, b, c = left
    d, e, f = right
    return primitive_projective((b * f - c * e, c * d - a * f, a * e - b * d))


def determinant_area(vectors: tuple[Vector, ...]) -> int:
    return sum(abs(determinant(left, right)) for left, right in combinations(vectors, 2))


def lattice_index(vectors: tuple[Vector, ...]) -> int:
    index = 0
    for left, right in combinations(vectors, 2):
        index = gcd(index, abs(determinant(left, right)))
    return index


def widths(vectors: tuple[Vector, ...]) -> tuple[int, ...]:
    return tuple(
        sum(abs(determinant(vector, other)) for other in vectors)
        for vector in vectors
    )


def rotate(vector: Vector) -> Vector:
    return -vector[1], vector[0]


def cross(origin: Vector, left: Vector, right: Vector) -> int:
    return determinant(
        (left[0] - origin[0], left[1] - origin[1]),
        (right[0] - origin[0], right[1] - origin[1]),
    )


def convex_hull(points: Iterable[Vector]) -> tuple[Vector, ...]:
    """Andrew monotone-chain hull, excluding collinear nonvertices."""
    ordered = sorted(set(points))
    assert len(ordered) >= 3
    lower: list[Vector] = []
    for point in ordered:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper: list[Vector] = []
    for point in reversed(ordered):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return tuple(lower[:-1] + upper[:-1])


def zonotope_hull(vectors: tuple[Vector, ...]) -> tuple[Vector, ...]:
    """Hull of all subset sums of the rotated generators."""
    points = {(0, 0)}
    for generator in map(rotate, vectors):
        points |= {(x + generator[0], y + generator[1]) for x, y in tuple(points)}
    return convex_hull(points)


def doubled_polygon_area(polygon: tuple[Vector, ...]) -> int:
    return abs(sum(determinant(left, right) for left, right in zip(polygon, polygon[1:] + polygon[:1])))


def boundary_lattice_intervals(polygon: tuple[Vector, ...]) -> int:
    return sum(
        gcd(abs(right[0] - left[0]), abs(right[1] - left[1]))
        for left, right in zip(polygon, polygon[1:] + polygon[:1])
    )


def support_interval(vector: Vector, vectors: tuple[Vector, ...]) -> tuple[int, int]:
    """Support interval of v on Z=sum_j [0,R v_j]."""
    values = [-determinant(vector, other) for other in vectors]
    return sum(min(0, value) for value in values), sum(max(0, value) for value in values)


def construction(vectors: tuple[Vector, ...], q: int) -> list[Line]:
    lines: list[Line] = []
    for vector in vectors:
        lower, upper = support_interval(vector, vectors)
        a, b = vector
        lines.extend((a, b, -level) for level in range(q * lower, q * upper + 1))
    lines = [primitive_projective(line) for line in lines]
    assert len(lines) == len(set(lines))
    return lines


def enumerate_multiplicities(lines: list[Line]) -> dict[Point, set[int]]:
    incident: dict[Point, set[int]] = defaultdict(set)
    for right_index, right in enumerate(lines):
        for left_index in range(right_index):
            point = intersection(lines[left_index], right)
            incident[point].update((left_index, right_index))
    return dict(incident)


def verify(k: int, q: int) -> Counter[int]:
    vectors = SIMPSON_DIRECTIONS[:k]
    assert all(gcd(abs(a), abs(b)) == 1 for a, b in vectors)
    assert all(determinant(left, right) != 0 for left, right in combinations(vectors, 2))
    assert lattice_index(vectors) == 1

    area = determinant_area(vectors)
    assert area == SIMPSON_AREAS[k]
    family_widths = widths(vectors)
    assert sum(family_widths) == 2 * area

    # Independent geometric reconstruction of the subset-sum zonotope.
    polygon = zonotope_hull(vectors)
    assert len(polygon) == 2 * k
    assert doubled_polygon_area(polygon) == 2 * area
    assert boundary_lattice_intervals(polygon) == 2 * k
    for vector, width in zip(vectors, family_widths):
        values = [vector[0] * x + vector[1] * y for x, y in polygon]
        assert max(values) - min(values) == width

    lines = construction(vectors, q)
    assert len(lines) == 2 * area * q + k

    incident = enumerate_multiplicities(lines)
    finite_exact = {
        point for point, indices in incident.items()
        if point[2] != 0 and len(indices) == k
    }
    expected_finite = area * q * q + k * q + 1
    assert len(finite_exact) == expected_finite

    infinity_exact = {
        point for point, indices in incident.items()
        if point[2] == 0 and len(indices) == k
    }
    expected_infinity = sum(q * width + 1 == k for width in family_widths)
    assert len(infinity_exact) == expected_infinity
    if q >= 2:
        assert not infinity_exact

    multiplicities = Counter(len(indices) for indices in incident.values())
    assert multiplicities[k] == expected_finite + expected_infinity
    assert sum(comb(r, 2) * count for r, count in multiplicities.items()) == comb(len(lines), 2)
    assert multiplicities[2] >= 3 + sum(
        (r - 3) * count for r, count in multiplicities.items() if r >= 4
    )
    return multiplicities


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-k", type=int, default=4)
    parser.add_argument("--max-k", type=int, default=10)
    parser.add_argument("--max-q", type=int, default=2)
    args = parser.parse_args()
    assert 2 <= args.min_k <= args.max_k <= len(SIMPSON_DIRECTIONS)
    assert args.max_q >= 1

    for k in range(args.min_k, args.max_k + 1):
        vectors = SIMPSON_DIRECTIONS[:k]
        area = determinant_area(vectors)
        family_widths = widths(vectors)
        comparison = ""
        if k in PALASTI:
            numerator, denominator = PALASTI[k]
            lhs = denominator
            rhs = 4 * area * numerator
            relation = ">" if lhs > rhs else "=" if lhs == rhs else "<"
            comparison = f" zonotope {relation} Palasti"
        print(
            f"k={k:2d} D={area:3d} widths={family_widths} "
            f"coefficient=1/{4*area}{comparison}"
        )
        for q in range(1, args.max_q + 1):
            multiplicities = verify(k, q)
            n = 2 * area * q + k
            exact_finite = area * q * q + k * q + 1
            summary = " ".join(
                f"t_{r}={multiplicities[r]}" for r in sorted(multiplicities)
            )
            print(
                f"  q={q} n={n} finite_exact_k={exact_finite} "
                f"{summary} PASS"
            )


if __name__ == "__main__":
    main()
