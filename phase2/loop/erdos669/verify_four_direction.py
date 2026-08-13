#!/usr/bin/env python3
"""Exact verifier for the four-direction Erdős #669 construction.

No floating point arithmetic and no third-party packages are used.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from math import comb, gcd
from typing import Iterable

Line = tuple[int, int, int]
Point = tuple[int, int, int]


def primitive_projective(v: Iterable[int]) -> tuple[int, int, int]:
    """Canonical primitive representative of a nonzero projective 3-vector."""
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
    cross = (b * f - c * e, c * d - a * f, a * e - b * d)
    return primitive_projective(cross)


def construction(q: int) -> list[Line]:
    assert q >= 1
    lines: list[Line] = []
    lines.extend((0, 1, -i) for i in range(3 * q))       # y = i
    lines.extend((1, 0, -j) for j in range(3 * q))       # x = j
    lines.extend((1, -1, -c) for c in range(-2 * q, 2 * q))
    lines.extend((1, 1, -d) for d in range(q - 1, 5 * q - 1))
    lines = [primitive_projective(line) for line in lines]
    assert len(lines) == 14 * q
    assert len(set(lines)) == len(lines)
    return lines


def certified_grid_points(q: int) -> set[Point]:
    points: set[Point] = set()
    for i in range(3 * q):
        for j in range(3 * q):
            if -2 * q <= j - i < 2 * q and q - 1 <= i + j < 5 * q - 1:
                points.add(primitive_projective((j, i, 1)))
    return points


def enumerate_multiplicities(lines: list[Line]) -> dict[Point, set[int]]:
    incident: dict[Point, set[int]] = defaultdict(set)
    for right_index, right in enumerate(lines):
        for left_index in range(right_index):
            point = intersection(lines[left_index], right)
            incident[point].update((left_index, right_index))
    return dict(incident)


def centered_core_count(axis_count: int, diagonal_count: int) -> int:
    """Count the symmetric centered H/V/diagonal core exactly."""
    a = axis_count
    c = diagonal_count
    differences = range(-(c // 2), -(c // 2) + c)
    sums = range((a - 1) - c // 2, (a - 1) - c // 2 + c)
    return sum(
        (j - i in differences) and (i + j in sums)
        for i in range(a)
        for j in range(a)
    )


def verify_q(q: int) -> Counter[int]:
    lines = construction(q)
    certified = certified_grid_points(q)
    assert len(certified) == 7 * q * q

    incident = enumerate_multiplicities(lines)
    for point in certified:
        assert point in incident
        assert len(incident[point]) == 4

    multiplicities = Counter(len(indices) for indices in incident.values())
    assert multiplicities[4] >= 7 * q * q

    # Every pair of projective lines meets at exactly one enumerated point.
    assert sum(comb(r, 2) * count for r, count in multiplicities.items()) == comb(14 * q, 2)

    # Melchior: t_2 >= 3 + sum_{r>=4} (r-3)t_r.
    assert multiplicities[2] >= 3 + sum(
        (r - 3) * count for r, count in multiplicities.items() if r >= 4
    )
    return multiplicities


def verify_discrete_symmetric_optimum(q: int) -> None:
    """Exhaust the centered symmetric family with total budget 14q.

    There are a horizontal, a vertical, c slope-1 and c slope+1 lines, so
    a+c=7q. We count only the four-family grid core.
    """
    budget_half = 7 * q
    scores = [(centered_core_count(a, budget_half - a), a) for a in range(1, budget_half)]
    best_score = max(score for score, _ in scores)
    candidate_score = centered_core_count(3 * q, 4 * q)
    assert candidate_score == 7 * q * q
    assert candidate_score == best_score


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-q", type=int, default=12)
    args = parser.parse_args()
    assert args.max_q >= 1

    for q in range(1, args.max_q + 1):
        multiplicities = verify_q(q)
        verify_discrete_symmetric_optimum(q)
        summary = " ".join(f"t_{r}={multiplicities[r]}" for r in sorted(multiplicities))
        print(f"q={q:2d} n={14*q:3d} certified={7*q*q:4d} {summary} PASS")


if __name__ == "__main__":
    main()
