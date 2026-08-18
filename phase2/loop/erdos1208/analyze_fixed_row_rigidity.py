#!/usr/bin/env python3
"""Exact modular ranks of the fixed-row distance-Sidon stress families."""

from __future__ import annotations

from analyze_transverse_longest_charge import DIAMETER_POINTS
from verify_transverse_closure_witness import POINTS as HEAVY_POINTS
from verify_transverse_fixed_row_c4 import fixed_row_relations
from verify_welch_relation_rigidity import (
    MODULUS,
    SQRT_MINUS_ONE,
    row_dot,
    sparse_rank,
)


def difference(left, right):
    return left[0] - right[0], left[1] - right[1]


def relation_rows(points, row):
    endpoint = {
        difference(points[i], points[j]): (i, j)
        for i in range(len(points))
        for j in range(len(points))
    }
    p, q = endpoint[row]
    rows = []
    for u, v, x, y in fixed_row_relations(points, row):
        equation = {}
        for index, coefficient in (
            (u, 1),
            (v, -1),
            (x, SQRT_MINUS_ONE),
            (y, -SQRT_MINUS_ONE),
            (p, -1),
            (q, 1),
        ):
            value = (equation.get(index, 0) + coefficient) % MODULUS
            if value:
                equation[index] = value
            else:
                equation.pop(index, None)
        rows.append(equation)
    return rows


def profile(points, row):
    rows = relation_rows(points, row)
    constants = [1] * len(points)
    coordinates = [
        (x + SQRT_MINUS_ONE * y) % MODULUS
        for x, y in points
    ]
    assert all(row_dot(equation, constants) == 0 for equation in rows)
    assert all(row_dot(equation, coordinates) == 0 for equation in rows)
    rank = sparse_rank(rows)
    return len(rows), rank, len(points) - rank


def main():
    for size in (17, 30, 45, 60, 90, 120):
        print("heavy", size, profile(HEAVY_POINTS[:size], (0, -1)))
    for size in (35, 45, 70, 90):
        print("diameter", size, profile(DIAMETER_POINTS[:size], (10_000, 0)))


if __name__ == "__main__":
    main()
