#!/usr/bin/env python3
"""Verify endpoint-pencil amplification into two-track star keys."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb
from random import Random

Edge = tuple[int, int]
Occurrence = tuple[Edge, ...]
StarKey = tuple[int, int, int, int, int]


def footprint(occurrence: Occurrence) -> frozenset[int]:
    return frozenset(endpoint for edge in occurrence for endpoint in edge)


def first_slot_at(occurrence: Occurrence, endpoint: int) -> tuple[int, int]:
    for role, edge in enumerate(occurrence):
        for side, value in enumerate(edge):
            if value == endpoint:
                return 2 * role + side, edge[1 - side]
    raise AssertionError("endpoint absent from occurrence")


def audit_system(
    cells: tuple[tuple[int, ...], ...],
    occurrences: tuple[Occurrence, ...],
    k: int,
    threshold: int,
) -> None:
    assert threshold >= 2
    occurrence_cell: dict[int, int] = {}
    for cell_index, cell in enumerate(cells):
        for occurrence in cell:
            assert occurrence not in occurrence_cell
            occurrence_cell[occurrence] = cell_index
    assert set(occurrence_cell) == set(range(len(occurrences)))
    assert all(len(occurrence) == 6 for occurrence in occurrences)
    assert all(
        head != tail and 0 <= head < k and 0 <= tail < k
        for occurrence in occurrences
        for head, tail in occurrence
    )

    footprints = tuple(map(footprint, occurrences))
    endpoint_occurrences: dict[int, list[int]] = {
        endpoint: [] for endpoint in range(k)
    }
    for occurrence, endpoints in enumerate(footprints):
        for endpoint in endpoints:
            endpoint_occurrences[endpoint].append(occurrence)
    degrees = tuple(
        len(endpoint_occurrences[endpoint]) for endpoint in range(k)
    )
    high_endpoints = {
        endpoint for endpoint, degree in enumerate(degrees) if degree >= threshold
    }

    assigned_endpoint: dict[int, int] = {}
    pointed_count = 0
    for occurrence, endpoints in enumerate(footprints):
        available = endpoints & high_endpoints
        if not available:
            continue
        assigned_endpoint[occurrence] = min(available)
        cell = cells[occurrence_cell[occurrence]]
        pointed_count += comb(len(cell) - 1, 2)

    amplified: dict[StarKey, list[tuple[int, tuple[int, int], int]]] = {}
    amplified_count = 0
    for occurrence, endpoint in assigned_endpoint.items():
        cell = cells[occurrence_cell[occurrence]]
        other_parameters = [value for value in cell if value != occurrence]
        first_slot, first_other = first_slot_at(
            occurrences[occurrence], endpoint
        )
        for pointed_pair in combinations(other_parameters, 2):
            for partner in endpoint_occurrences[endpoint]:
                if partner == occurrence:
                    continue
                second_slot, second_other = first_slot_at(
                    occurrences[partner], endpoint
                )
                key = (
                    endpoint,
                    first_slot,
                    first_other,
                    second_slot,
                    second_other,
                )
                amplified.setdefault(key, []).append(
                    (occurrence, pointed_pair, partner)
                )
                amplified_count += 1

    expected_amplified = sum(
        comb(len(cells[occurrence_cell[occurrence]]) - 1, 2)
        * (degrees[endpoint] - 1)
        for occurrence, endpoint in assigned_endpoint.items()
    )
    assert amplified_count == expected_amplified
    assert amplified_count >= (threshold - 1) * pointed_count
    assert len(amplified) <= 144 * k * (k - 1) ** 2

    collision_count = sum(comb(len(records), 2) for records in amplified.values())
    assert amplified_count**2 <= len(amplified) * (
        amplified_count + 2 * collision_count
    ) if amplified else amplified_count == 0

    collision_types: Counter[str] = Counter()
    for records in amplified.values():
        for first, second in combinations(records, 2):
            first_occurrence, first_pair, first_partner = first
            second_occurrence, second_pair, second_partner = second
            assert first != second
            if first_occurrence != second_occurrence:
                collision_types["first_track_reuse"] += 1
            if first_partner != second_partner:
                collision_types["second_track_reuse"] += 1
            if (
                first_occurrence == second_occurrence
                and first_partner == second_partner
            ):
                assert first_pair != second_pair
                collision_types["internal_pointed_pair"] += 1
    assert sum(collision_types.values()) >= collision_count


def deterministic_cases() -> None:
    occurrences: tuple[Occurrence, ...] = (
        ((0, 1), (0, 2), (3, 4), (1, 4), (2, 3), (0, 4)),
        ((0, 2), (0, 3), (1, 4), (2, 4), (1, 3), (0, 1)),
        ((0, 3), (0, 4), (1, 2), (1, 3), (2, 4), (0, 2)),
        ((0, 4), (0, 1), (2, 3), (1, 2), (3, 4), (0, 3)),
    )
    audit_system(((0, 1, 2, 3),), occurrences, 5, 2)


def random_stress() -> None:
    rng = Random(1208202603)
    for k in range(5, 20):
        for _ in range(100):
            cell_sizes = []
            remaining = rng.randrange(3, 22)
            while remaining:
                size = min(remaining, rng.randrange(1, 7))
                cell_sizes.append(size)
                remaining -= size
            occurrences = []
            cells = []
            for size in cell_sizes:
                cell = []
                for _ in range(size):
                    edges = []
                    for _ in range(6):
                        head = rng.randrange(k)
                        tail = rng.randrange(k - 1)
                        if tail >= head:
                            tail += 1
                        edges.append((head, tail))
                    cell.append(len(occurrences))
                    occurrences.append(tuple(edges))
                cells.append(tuple(cell))
            for threshold in (2, 3, 5, 8):
                audit_system(
                    tuple(cells), tuple(occurrences), k, threshold
                )


def main() -> None:
    deterministic_cases()
    random_stress()
    print("SWAP ENDPOINT PENCIL AMPLIFIED STAR KEY: PASS")


if __name__ == "__main__":
    main()
