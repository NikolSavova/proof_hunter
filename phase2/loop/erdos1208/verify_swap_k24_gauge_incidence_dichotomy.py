#!/usr/bin/env python3
"""Exact checks for SWAP_K24_GAUGE_INCIDENCE_DICHOTOMY.md."""

from __future__ import annotations

from collections import Counter
from itertools import product
from math import comb
from random import Random


def profile(
    cells_by_key: dict[int, list[frozenset[int]]], threshold: int
) -> tuple[int, int, int, int, int, int]:
    assert threshold >= 2
    total = 0
    low = 0
    ambient = 0
    high_envelope = 0
    maximum_column_degree = 0
    for cells in cells_by_key.values():
        degrees = Counter(value for cell in cells for value in cell)
        maximum_column_degree = max(
            maximum_column_degree, max(degrees.values(), default=0)
        )
        high_values = {
            value for value, degree in degrees.items() if degree >= threshold
        }
        union = set(degrees)
        ambient += 3 * comb(len(union), 3)
        for cell in cells:
            load = len(cell)
            high_load = len(cell & high_values)
            low_load = load - high_load
            total += 3 * comb(load, 3)
            low += 3 * comb(low_load, 3)
            if high_load:
                high_envelope += 3 * high_load * comb(load - 1, 2)
    assert low <= 3 * (threshold - 1) * (ambient // 3)
    assert total <= low + high_envelope
    return (
        total,
        low,
        ambient,
        high_envelope,
        maximum_column_degree,
        sum(len(cells) for cells in cells_by_key.values()),
    )


def exhaustive_small() -> None:
    # Exhaust every 3-row by 3-column incidence matrix, including empty
    # rows.  This checks both inequalities with no geometric assumptions.
    for mask in range(1 << 9):
        cells = []
        for row in range(3):
            cells.append(
                frozenset(
                    column
                    for column in range(3)
                    if mask & (1 << (3 * row + column))
                )
            )
        for threshold in (2, 3, 4):
            profile({0: cells}, threshold)


def seeded_random() -> None:
    random = Random(1208)
    for _ in range(500):
        cells_by_key: dict[int, list[frozenset[int]]] = {}
        for key in range(random.randrange(1, 6)):
            universe = random.randrange(1, 10)
            cells_by_key[key] = [
                frozenset(
                    value
                    for value in range(universe)
                    if random.randrange(3) == 0
                )
                for _ in range(random.randrange(1, 9))
            ]
        for threshold in (2, 3, 5, 8):
            profile(cells_by_key, threshold)


def sharp_models() -> None:
    # A complete gauge rectangle: mu cells share the same r first-track
    # values.  The low-degree factor Delta is power-sharp just below the
    # threshold, and the high pencil is unavoidable at the threshold.
    for multiplicity, load in product(range(1, 8), range(3, 9)):
        cells = [frozenset(range(load)) for _ in range(multiplicity)]
        below = profile({0: cells}, multiplicity + 1)
        assert below[0] == 3 * multiplicity * comb(load, 3)
        assert below[1] == below[0]
        assert below[2] == 3 * comb(load, 3)
        at = profile({0: cells}, max(2, multiplicity))
        if multiplicity >= 2:
            assert at[1] == 0
            assert at[3] >= at[0]

    # Disjoint cells have column degree one and are charged exactly through
    # the ambient union at a harmless convexity loss.
    cells = [
        frozenset(range(4 * index, 4 * index + 4)) for index in range(6)
    ]
    total, low, ambient, high, maximum, _ = profile({0: cells}, 2)
    assert total == low == 6 * 3 * comb(4, 3)
    assert ambient > total
    assert high == 0
    assert maximum == 1


def main() -> None:
    exhaustive_small()
    seeded_random()
    sharp_models()
    print("K2,4 gauge-incidence dichotomy: PASS")


if __name__ == "__main__":
    main()
