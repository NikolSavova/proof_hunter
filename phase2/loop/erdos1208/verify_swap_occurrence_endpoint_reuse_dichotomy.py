#!/usr/bin/env python3
"""Verify the occurrence-endpoint reuse dichotomy."""

from __future__ import annotations

from itertools import combinations
from math import comb
from random import Random

Footprint = frozenset[int]
Cell = tuple[Footprint, ...]


def endpoint_degrees(cells: tuple[Cell, ...], k: int) -> list[int]:
    degrees = [0] * k
    for cell in cells:
        for footprint in cell:
            assert 2 <= len(footprint) <= 12
            for endpoint in footprint:
                assert 0 <= endpoint < k
                degrees[endpoint] += 1
    return degrees


def greedy_colouring(
    occurrences: list[tuple[int, int, Footprint]],
) -> list[int]:
    colours: list[int] = []
    for _, _, footprint in occurrences:
        forbidden = {
            colours[index]
            for index, (_, _, previous) in enumerate(occurrences[: len(colours)])
            if footprint & previous
        }
        colour = 0
        while colour in forbidden:
            colour += 1
        colours.append(colour)
    return colours


def audit_system(cells: tuple[Cell, ...], k: int) -> None:
    degrees = endpoint_degrees(cells, k)
    delta = max(degrees, default=0)
    occurrences = [
        (cell_index, occurrence_index, footprint)
        for cell_index, cell in enumerate(cells)
        for occurrence_index, footprint in enumerate(cell)
    ]
    colours = greedy_colouring(occurrences)
    colour_count = max(colours, default=-1) + 1

    for first, second in combinations(range(len(occurrences)), 2):
        if colours[first] == colours[second]:
            assert not (occurrences[first][2] & occurrences[second][2])
    if occurrences:
        assert colour_count <= 12 * delta - 11

    colour_loads: dict[int, int] = {}
    cell_colour_loads: dict[tuple[int, int], int] = {}
    for (cell_index, _, _), colour in zip(occurrences, colours):
        colour_loads[colour] = colour_loads.get(colour, 0) + 1
        key = cell_index, colour
        cell_colour_loads[key] = cell_colour_loads.get(key, 0) + 1
    assert all(load <= k // 2 for load in colour_loads.values())

    cubic_mass = 3 * sum(comb(len(cell), 3) for cell in cells)
    if delta:
        assert cubic_mass <= 108 * delta**3 * k**3

    # Check the two convexity steps used in the proof independently.
    if colour_count:
        sum_cell_cubes = sum(len(cell) ** 3 for cell in cells)
        coloured_cell_cubes = sum(
            load**3 for load in cell_colour_loads.values()
        )
        assert sum_cell_cubes <= colour_count**2 * coloured_cell_cubes
        for colour in range(colour_count):
            assert sum(
                load**3
                for (cell_index, current_colour), load in cell_colour_loads.items()
                if current_colour == colour
            ) <= colour_loads.get(colour, 0) ** 3

    for threshold in range(2, max(3, delta + 2)):
        high_endpoints = {
            endpoint
            for endpoint, degree in enumerate(degrees)
            if degree >= threshold
        }
        low_cells: list[int] = []
        high_counts: list[int] = []
        canonical_endpoint_envelope = 0
        for cell in cells:
            high = [
                footprint
                for footprint in cell
                if footprint & high_endpoints
            ]
            high_counts.append(len(high))
            low_cells.append(len(cell) - len(high))
            for footprint in cell:
                high_members = footprint & high_endpoints
                canonical_endpoint_envelope += bool(high_members) * comb(
                    max(0, len(cell) - 1), 2
                )

        low_mass = 3 * sum(comb(load, 3) for load in low_cells)
        high_mass = cubic_mass - low_mass
        high_union_envelope = 3 * sum(
            high * comb(max(0, len(cell) - 1), 2)
            for high, cell in zip(high_counts, cells)
        )
        canonical_endpoint_envelope *= 3
        assert high_mass <= high_union_envelope
        assert high_union_envelope == canonical_endpoint_envelope
        assert low_mass <= 108 * (threshold - 1) ** 3 * k**3
        assert cubic_mass <= (
            108 * (threshold - 1) ** 3 * k**3
            + canonical_endpoint_envelope
        )


def exhaustive_small() -> None:
    base = tuple(
        frozenset(pair) for pair in combinations(range(4), 2)
    )
    # Exhaust every collection of at most two cells whose occurrence lists
    # are initial segments of the six possible two-point footprints.
    for first_size in range(7):
        for second_size in range(7):
            cells = tuple(
                cell
                for cell in (base[:first_size], base[::-1][:second_size])
                if cell
            )
            audit_system(cells, 4)


def random_stress() -> None:
    rng = Random(12082026)
    for k in range(5, 31):
        for _ in range(80):
            cells = []
            for _ in range(rng.randrange(1, 12)):
                occurrences = []
                for _ in range(rng.randrange(1, 15)):
                    size = rng.randrange(2, min(12, k) + 1)
                    occurrences.append(
                        frozenset(rng.sample(range(k), size))
                    )
                cells.append(tuple(occurrences))
            audit_system(tuple(cells), k)


def main() -> None:
    exhaustive_small()
    random_stress()
    print("SWAP OCCURRENCE ENDPOINT REUSE DICHOTOMY: PASS")


if __name__ == "__main__":
    main()
