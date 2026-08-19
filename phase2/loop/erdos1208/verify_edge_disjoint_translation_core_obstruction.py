#!/usr/bin/env python3
"""Exhaust every connected edge-disjoint F_2-translation corner core.

Up to an invertible change of coordinates, eight labelled shift vectors are
the eight columns of the unique reduced-row-echelon generator of a subspace
of F_2^8.  This script enumerates those subspaces exactly.  It retains simple
column configurations (eight distinct nonzero shifts), tests whether the six
endpoint labels recover every record, and certifies either a universal point
coalescing which empties the full core or a parallelogram collision in one
endpoint role.  Exact two-record corner cores are recorded as a distinguished
subfamily.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from search_edge_disjoint_translation_core import (
    coalesced_translation_obstruction,
    face_spaces,
    intersection,
    valid_exact_core,
)


def rref_subspaces(n: int, dimension: int):
    """Yield the unique RREF row basis of every dimension-k subspace."""
    for pivots in combinations(range(n), dimension):
        pivot_set = set(pivots)
        free_positions = tuple(
            (row, column)
            for column in range(n)
            if column not in pivot_set
            for row, pivot in enumerate(pivots)
            if pivot < column
        )
        for assignment in range(1 << len(free_positions)):
            rows = [1 << pivot for pivot in pivots]
            for bit, (row, column) in enumerate(free_positions):
                if (assignment >> bit) & 1:
                    rows[row] |= 1 << column
            yield tuple(rows)


def columns(rows: tuple[int, ...], n: int = 8) -> tuple[int, ...]:
    return tuple(
        sum(((row >> column) & 1) << index for index, row in enumerate(rows))
        for column in range(n)
    )


def gaussian_binomial(n: int, k: int) -> int:
    numerator = 1
    denominator = 1
    for index in range(k):
        numerator *= (1 << (n - index)) - 1
        denominator *= (1 << (k - index)) - 1
    return numerator // denominator


def main() -> None:
    total = Counter()
    examples: dict[int, tuple[tuple[int, ...], object]] = {}
    for dimension in range(1, 9):
        dimension_count = 0
        dimension_profile = Counter()
        for rows in rref_subspaces(8, dimension):
            dimension_count += 1
            total["subspaces"] += 1
            shifts = columns(rows)
            if 0 in shifts or len(set(shifts)) != 8:
                continue
            total["simple"] += 1
            dimension_profile["simple"] += 1
            spaces = face_spaces(shifts)
            if intersection(spaces) != frozenset({0}):
                total["record-collapse"] += 1
                dimension_profile["record-collapse"] += 1
                continue
            total["full-core"] += 1
            dimension_profile["full-core"] += 1
            exact = valid_exact_core(shifts)
            if exact:
                total["exact-core"] += 1
                dimension_profile["exact-core"] += 1
            outcome, witness = coalesced_translation_obstruction(dimension, shifts)
            total[outcome] += 1
            dimension_profile[outcome] += 1
            if outcome == "empty-core":
                if exact:
                    total["exact-empty-core"] += 1
                examples.setdefault(dimension, (shifts, (outcome, witness)))
            else:
                if exact:
                    total["exact-translation-collision"] += 1
                examples.setdefault(dimension, (shifts, (outcome, witness)))
        assert dimension_count == gaussian_binomial(8, dimension)
        print(
            "dimension",
            dimension,
            "subspaces",
            dimension_count,
            "profile",
            dict(dimension_profile),
            "example",
            examples.get(dimension),
        )
    assert total["subspaces"] == sum(gaussian_binomial(8, k) for k in range(1, 9))
    assert total == Counter(
        {
            "subspaces": 417_198,
            "simple": 50_864,
            "record-collapse": 22_894,
            "full-core": 27_970,
            "empty-core": 27_389,
            "translation-collision": 581,
            "exact-core": 332,
            "exact-empty-core": 219,
            "exact-translation-collision": 113,
        }
    )
    print("totals", dict(total))
    print("edge-disjoint translation-core obstruction: PASS")


if __name__ == "__main__":
    main()
