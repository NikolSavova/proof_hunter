#!/usr/bin/env python3
"""Verify the balanced endpoint-track row reduction exactly."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
from random import Random


Token = tuple[int, int]


def compositions(total: int, parts: int) -> list[tuple[int, ...]]:
    if parts == 1:
        return [(total,)]
    rows: list[tuple[int, ...]] = []
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            rows.append((first,) + tail)
    return rows


def collision(loads: tuple[int, ...] | list[int]) -> int:
    return sum(load * (load - 1) // 2 for load in loads)


def audit_balancing_minimum() -> None:
    for bins in range(1, 6):
        for mass in range(13):
            quotient, remainder = divmod(mass, bins)
            expected = bins * quotient * (quotient - 1) // 2 + remainder * quotient
            assert min(collision(row) for row in compositions(mass, bins)) == expected


def audit_system(
    k: int,
    endpoint_occurrences: list[list[int]],
    tokens: list[dict[int, Token]],
    assigned_endpoint: list[int],
    weights: list[int],
) -> None:
    occurrence_count = len(tokens)
    assert len(assigned_endpoint) == occurrence_count == len(weights)
    assert all(
        occurrence in endpoint_occurrences[endpoint]
        for occurrence, endpoint in enumerate(assigned_endpoint)
    )
    assert all(len(endpoint_occurrences[endpoint]) >= 2 for endpoint in assigned_endpoint)

    token_occurrences: list[dict[Token, list[int]]] = []
    for endpoint, occurrences in enumerate(endpoint_occurrences):
        rows: dict[Token, list[int]] = defaultdict(list)
        for occurrence in occurrences:
            rows[tokens[occurrence][endpoint]].append(occurrence)
        token_occurrences.append(rows)

    first_rows: dict[tuple[int, Token], list[tuple[int, int]]] = defaultdict(list)
    for occurrence, endpoint in enumerate(assigned_endpoint):
        token = tokens[occurrence][endpoint]
        first_rows[endpoint, token].extend(
            (occurrence, decoration) for decoration in range(weights[occurrence])
        )

    key_records: dict[tuple[int, Token, Token], list[tuple[int, int, int]]] = (
        defaultdict(list)
    )
    row_profiles: list[tuple[int, int, int, int]] = []
    for (endpoint, first_token), records in sorted(first_rows.items()):
        available = token_occurrences[endpoint]
        allowed = sorted(
            token
            for token, occurrences in available.items()
            if token != first_token or len(occurrences) >= 2
        )
        assert allowed
        quotient, remainder = divmod(len(records), len(allowed))
        row_profiles.append((len(records), len(allowed), quotient, remainder))
        for index, (occurrence, decoration) in enumerate(records):
            partner_token = allowed[index % len(allowed)]
            candidates = [
                partner
                for partner in available[partner_token]
                if partner != occurrence
            ]
            assert candidates
            partner = candidates[(index // len(allowed)) % len(candidates)]
            key_records[endpoint, first_token, partner_token].append(
                (occurrence, decoration, partner)
            )

    mass = sum(weights)
    assert sum(map(len, key_records.values())) == mass
    for (endpoint, first_token, partner_token), records in key_records.items():
        for occurrence, _, partner in records:
            assert occurrence != partner
            assert assigned_endpoint[occurrence] == endpoint
            assert tokens[occurrence][endpoint] == first_token
            assert partner in endpoint_occurrences[endpoint]
            assert tokens[partner][endpoint] == partner_token

    for endpoint, first_token in first_rows:
        loads = sorted(
            len(records)
            for (key_endpoint, key_first, _), records in key_records.items()
            if (key_endpoint, key_first) == (endpoint, first_token)
        )
        assert max(loads) - min(loads) <= 1

    exact_collision = sum(collision([len(records)]) for records in key_records.values())
    formula_collision = sum(
        bins * quotient * (quotient - 1) // 2 + remainder * quotient
        for _, bins, quotient, remainder in row_profiles
    )
    assert exact_collision == formula_collision

    token_support = [len(rows) for rows in token_occurrences]
    capacity = sum(support * support for support in token_support)
    assert len(key_records) <= sum(profile[1] for profile in row_profiles) <= capacity
    assert capacity <= 144 * k * (k - 1) ** 2
    assert mass * mass <= len(key_records) * (mass + 2 * exact_collision) if mass else True

    for cutoff in (1, 2, 3, 5, 8, 13):
        light_mass = sum(
            row_mass
            for row_mass, bins, _, _ in row_profiles
            if row_mass <= cutoff * bins
        )
        assert light_mass <= cutoff * sum(
            bins
            for row_mass, bins, _, _ in row_profiles
            if row_mass <= cutoff * bins
        )
        assert light_mass <= cutoff * capacity
        assert light_mass <= 144 * cutoff * k * (k - 1) ** 2


def deterministic_systems() -> None:
    # One token repeated twice and one distinct token: the same-token partner
    # is legal, and every row has two allowed partner tokens.
    k = 4
    endpoint_occurrences = [[0, 1, 2], [0, 2], [1], [2]]
    tokens = [
        {0: (0, 1), 1: (1, 0)},
        {0: (0, 1), 2: (2, 0)},
        {0: (3, 2), 1: (4, 0), 3: (5, 0)},
    ]
    audit_system(k, endpoint_occurrences, tokens, [0, 0, 0], [7, 4, 5])

    # Every assigned row is a singleton token, so it must use another token.
    endpoint_occurrences = [[0, 1, 2, 3], [0], [1], [2, 3], []]
    tokens = [
        {0: (0, 1), 1: (1, 0)},
        {0: (0, 2), 2: (1, 0)},
        {0: (0, 3), 3: (1, 0)},
        {0: (0, 4), 3: (2, 0)},
    ]
    audit_system(5, endpoint_occurrences, tokens, [0, 0, 0, 0], [1, 2, 8, 13])


def random_systems() -> None:
    rng = Random(1208)
    for k in range(3, 11):
        for _ in range(120):
            occurrence_count = rng.randrange(2, 2 * k + 5)
            footprints: list[list[int]] = []
            for _occurrence in range(occurrence_count):
                size = rng.randrange(2, min(k, 6) + 1)
                footprints.append(rng.sample(range(k), size))
            endpoint_occurrences = [[] for _ in range(k)]
            tokens: list[dict[int, Token]] = []
            for occurrence, footprint in enumerate(footprints):
                token_row: dict[int, Token] = {}
                for slot, endpoint in enumerate(footprint):
                    endpoint_occurrences[endpoint].append(occurrence)
                    # The bounded slot and opposite label intentionally create
                    # both singleton and repeated token classes.
                    token_row[endpoint] = (slot % 12, rng.randrange(k - 1))
                tokens.append(token_row)

            eligible = [
                endpoint
                for endpoint, occurrences in enumerate(endpoint_occurrences)
                if len(occurrences) >= 2
            ]
            if not eligible:
                continue
            retained = [
                occurrence
                for occurrence, footprint in enumerate(footprints)
                if any(endpoint in eligible for endpoint in footprint)
            ]
            remap = {old: new for new, old in enumerate(retained)}
            restricted_tokens = [tokens[old] for old in retained]
            restricted_endpoint_occurrences = [[] for _ in range(k)]
            for old in retained:
                for endpoint in footprints[old]:
                    restricted_endpoint_occurrences[endpoint].append(remap[old])
            assigned = [
                rng.choice(
                    [
                        endpoint
                        for endpoint in footprints[old]
                        if len(restricted_endpoint_occurrences[endpoint]) >= 2
                    ]
                )
                for old in retained
            ]
            weights = [rng.randrange(1, 30) for _ in retained]
            audit_system(
                k,
                restricted_endpoint_occurrences,
                restricted_tokens,
                assigned,
                weights,
            )


def main() -> None:
    audit_balancing_minimum()
    deterministic_systems()
    random_systems()
    print("SWAP BALANCED TRACK ROW: PASS")


if __name__ == "__main__":
    main()
