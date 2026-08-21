#!/usr/bin/env python3
"""Verify the low normalized repeated-track ratio estimate."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product
from random import Random


def audit(
    cell_loads: list[int],
    occurrence_rows: list[set[int]],
    base_capacity: list[int],
    cutoff: int,
) -> None:
    assert all(load >= 3 for load in cell_loads)
    occurrence_count = sum(cell_loads)
    assert len(occurrence_rows) <= occurrence_count
    assert all(len(rows) <= 12 for rows in occurrence_rows)
    row_degree = Counter(row for rows in occurrence_rows for row in rows)
    low_mass = sum(
        Fraction(degree * (degree - 1), 2 * base_capacity[row])
        for row, degree in row_degree.items()
        if degree <= cutoff * base_capacity[row]
    )
    q_phys = sum(load * (load - 1) // 2 for load in cell_loads)
    assert occurrence_count <= q_phys
    assert sum(row_degree.values()) <= 12 * len(occurrence_rows)
    assert low_mass <= Fraction(cutoff, 2) * sum(row_degree.values())
    assert low_mass <= 6 * cutoff * q_phys


def exhaustive() -> None:
    for cell_count in range(1, 5):
        for loads in product(range(3, 7), repeat=cell_count):
            occurrence_count = sum(loads)
            # Extremal concentration and complete separation bracket all
            # first-moment patterns used by the proof.
            concentrated = [{0} for _ in range(occurrence_count)]
            separated = [{index} for index in range(occurrence_count)]
            for cutoff in (1, 2, 4, 8):
                audit(list(loads), concentrated, [1], cutoff)
                audit(
                    list(loads),
                    separated,
                    [1] * occurrence_count,
                    cutoff,
                )


def random_systems() -> None:
    rng = Random(1208202612)
    for _ in range(5000):
        loads = [rng.randrange(3, 15) for _ in range(rng.randrange(1, 12))]
        retained = rng.randrange(1, sum(loads) + 1)
        row_count = rng.randrange(1, 4 * retained + 1)
        occurrence_rows = [
            set(
                rng.sample(
                    range(row_count),
                    rng.randrange(1, min(12, row_count) + 1),
                )
            )
            for _ in range(retained)
        ]
        capacities = [rng.randrange(1, retained + 2) for _ in range(row_count)]
        for cutoff in (1, 2, 4, 8, 16):
            audit(loads, occurrence_rows, capacities, cutoff)


def main() -> None:
    exhaustive()
    random_systems()
    print("SWAP NORMALIZED TRACK RATIO: PASS")


if __name__ == "__main__":
    main()
