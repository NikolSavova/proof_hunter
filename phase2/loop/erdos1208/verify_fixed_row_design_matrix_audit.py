#!/usr/bin/env python3
"""Exact finite checks for FIXED_ROW_DESIGN_MATRIX_AUDIT.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from analyze_transverse_longest_charge import DIAMETER_POINTS
from verify_transverse_closure_witness import POINTS as HEAVY_POINTS
from verify_transverse_fixed_row_c4 import fixed_row_relations
from verify_welch_relation_rigidity import (
    MODULUS,
    SQRT_MINUS_ONE,
    sparse_rank,
)


COEFFICIENTS = (1, -1, SQRT_MINUS_ONE, -SQRT_MINUS_ONE)


def add_entry(row: dict[int, int], column: int, coefficient: int) -> None:
    value = (row.get(column, 0) + coefficient) % MODULUS
    if value:
        row[column] = value
    else:
        row.pop(column, None)


def subtract(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    result = dict(left)
    for column, coefficient in right.items():
        add_entry(result, column, -coefficient)
    return result


def actual_rows(points, difference):
    rows = []
    for relation in fixed_row_relations(points, difference):
        row: dict[int, int] = {}
        for column, coefficient in zip(relation, COEFFICIENTS):
            add_entry(row, column, coefficient)
        assert row
        rows.append(row)
    return rows


def role_rows(points, difference):
    size = len(points)
    rows = []
    relations = fixed_row_relations(points, difference)
    for relation in relations:
        row = {
            role * size + label: coefficient % MODULUS
            for role, (label, coefficient) in enumerate(zip(relation, COEFFICIENTS))
        }
        assert len(row) == 4
        rows.append(row)
    return relations, rows


def active_profile(rows):
    active = set().union(*(row.keys() for row in rows))
    rank = sparse_rank(rows)
    return len(active), rank, len(active) - rank


def maximum_pair_overlap(rows):
    overlaps = Counter()
    for row in rows:
        for left, right in combinations(sorted(row), 2):
            overlaps[left, right] += 1
    return max(overlaps.values(), default=0)


def homogeneous_actual_rows(points, difference, affine_rows):
    endpoints = {
        (points[i][0] - points[j][0], points[i][1] - points[j][1]): (i, j)
        for i in range(len(points))
        for j in range(len(points))
    }
    p, q = endpoints[difference]
    result = []
    for affine in affine_rows:
        row = dict(affine)
        add_entry(row, p, -1)
        add_entry(row, q, 1)
        result.append(row)
    return result


def check_case(name, points, difference, expected):
    actual = actual_rows(points, difference)
    centered_actual = [subtract(row, actual[0]) for row in actual[1:]]
    homogeneous = homogeneous_actual_rows(points, difference, actual)
    relations, roles = role_rows(points, difference)
    centered_roles = [subtract(row, roles[0]) for row in roles[1:]]

    assert len(relations) == expected["relations"]
    assert sparse_rank(actual) == expected["actual_rank"]
    assert sparse_rank(centered_actual) == expected["centered_actual_rank"]
    assert sparse_rank(homogeneous) == expected["homogeneous_rank"]
    assert active_profile(roles) == expected["role_profile"]
    assert active_profile(centered_roles) == expected["centered_role_profile"]

    # Different role columns occur together at most once because every pair
    # of roles determines the full relation.  Merged actual labels have at
    # most the twelve ordered choices of two distinct roles.
    assert maximum_pair_overlap(roles) == 1
    assert maximum_pair_overlap(actual) <= 12

    degree = Counter(column for row in roles for column in row)
    assert min(degree.values()) >= 1

    print(
        name,
        "relations", len(relations),
        "actual ranks", sparse_rank(actual), sparse_rank(centered_actual),
        "role profiles", active_profile(roles), active_profile(centered_roles),
        "pair overlaps", maximum_pair_overlap(roles), maximum_pair_overlap(actual),
    )


def main() -> None:
    assert SQRT_MINUS_ONE * SQRT_MINUS_ONE % MODULUS == MODULUS - 1
    check_case(
        "heavy",
        HEAVY_POINTS[:120],
        (0, -1),
        {
            "relations": 948,
            "actual_rank": 119,
            "centered_actual_rank": 118,
            "homogeneous_rank": 118,
            "role_profile": (478, 473, 5),
            "centered_role_profile": (478, 472, 6),
        },
    )
    check_case(
        "diameter",
        DIAMETER_POINTS[:90],
        (10_000, 0),
        {
            "relations": 266,
            "actual_rank": 86,
            "centered_actual_rank": 85,
            "homogeneous_rank": 85,
            "role_profile": (248, 233, 15),
            "centered_role_profile": (248, 232, 16),
        },
    )

    # Arithmetic in the symbolic corank estimate of Section 2.
    assert 12 * 64 == 768
    assert 12 * 12 * 64 == 9216
    print("PASS")


if __name__ == "__main__":
    main()
