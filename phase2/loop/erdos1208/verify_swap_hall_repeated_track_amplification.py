#!/usr/bin/env python3
"""Verify Hall-deficiency amplification to repeated-track occurrence pairs."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from random import Random


def deficiency(
    selected: tuple[int, ...],
    weights: list[int],
    neighbours: list[set[int]],
    base_capacity: list[int],
    cutoff: int,
) -> int:
    rows = {row for occurrence in selected for row in neighbours[occurrence]}
    return sum(weights[occurrence] for occurrence in selected) - cutoff * sum(
        base_capacity[row] for row in rows
    )


def audit_system(
    weights: list[int], neighbours: list[set[int]], base_capacity: list[int]
) -> None:
    occurrence_count = len(weights)
    assert all(neighbours)
    assert all(capacity >= 1 for capacity in base_capacity)
    assert all(len(rows) <= 12 for rows in neighbours)
    weight_bound = max(weights)
    cutoff = 2 * weight_bound

    subsets = [
        tuple(index for index in range(occurrence_count) if mask >> index & 1)
        for mask in range(1 << occurrence_count)
    ]
    values = {
        selected: deficiency(
            selected, weights, neighbours, base_capacity, cutoff
        )
        for selected in subsets
    }
    maximum = max(values.values())
    maximizing = [selected for selected, value in values.items() if value == maximum]
    minimal = min(maximizing, key=lambda selected: (len(selected), selected))

    global_pairs = {
        (first, second)
        for first in range(occurrence_count)
        for second in range(first + 1, occurrence_count)
        if neighbours[first] & neighbours[second]
    }
    if maximum > 0:
        selected = minimal
        row_degree = {
            row: sum(row in neighbours[occurrence] for occurrence in selected)
            for row in {row for occurrence in selected for row in neighbours[occurrence]}
        }
        incidence = sum(row_degree.values())
        row_count = len(row_degree)
        row_pairs = sum(degree * (degree - 1) // 2 for degree in row_degree.values())
        distinct_pairs = {
            (first, second)
            for offset, first in enumerate(selected)
            for second in selected[offset + 1 :]
            if neighbours[first] & neighbours[second]
        }
        normalized_pairs = sum(
            Fraction(degree * (degree - 1), 2 * base_capacity[row])
            for row, degree in row_degree.items()
        )
        assert incidence >= len(selected)
        assert row_count < weight_bound * len(selected) / cutoff
        assert 2 * row_pairs > (cutoff / weight_bound - 1) * len(selected)
        assert row_pairs <= 12 * len(distinct_pairs)
        assert 24 * len(distinct_pairs) > (
            cutoff / weight_bound - 1
        ) * len(selected)
        assert 2 * normalized_pairs > Fraction(
            cutoff - weight_bound, weight_bound
        ) * len(selected)
        assert maximum <= sum(weights[index] for index in selected)
        assert maximum < 24 * weight_bound * len(distinct_pairs)
        assert maximum <= 24 * weight_bound * len(global_pairs)
        global_normalized_pairs = sum(
            Fraction(degree * (degree - 1), 2 * base_capacity[row])
            for row in range(len(base_capacity))
            if (
                degree
                := sum(row in row_neighbours for row_neighbours in neighbours)
            )
        )
        assert maximum < 2 * weight_bound * normalized_pairs
        assert maximum <= 2 * weight_bound * global_normalized_pairs

        # Inclusion-minimal maximizers have no private rows when L>W.
        assert all(degree >= 2 for degree in row_degree.values())


def exhaustive_systems() -> None:
    for occurrence_count in range(1, 6):
        for row_count in range(1, 5):
            masks = range(1, 1 << row_count)
            for encoded in product(masks, repeat=occurrence_count):
                neighbours = [
                    {row for row in range(row_count) if mask >> row & 1}
                    for mask in encoded
                ]
                for weights in (
                    [1] * occurrence_count,
                    [1 + index % 3 for index in range(occurrence_count)],
                ):
                    audit_system(weights, neighbours, [1] * row_count)


def random_systems() -> None:
    rng = Random(1208202611)
    for occurrence_count in range(2, 11):
        for _ in range(1500):
            row_count = rng.randrange(1, 10)
            neighbours = []
            for _occurrence in range(occurrence_count):
                size = rng.randrange(1, min(12, row_count) + 1)
                neighbours.append(set(rng.sample(range(row_count), size)))
            weights = [rng.randrange(1, 8) for _ in range(occurrence_count)]
            capacities = [rng.randrange(1, 5) for _ in range(row_count)]
            audit_system(weights, neighbours, capacities)


def main() -> None:
    exhaustive_systems()
    random_systems()
    print("SWAP HALL REPEATED-TRACK AMPLIFICATION: PASS")


if __name__ == "__main__":
    main()
