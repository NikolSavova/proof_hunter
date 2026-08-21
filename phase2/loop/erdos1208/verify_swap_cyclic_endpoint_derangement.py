#!/usr/bin/env python3
"""Verify the cyclic endpoint-derangement gate."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import comb
from random import Random

Token = tuple[int, int]


def internal_formula(weight: int, partner_count: int) -> int:
    quotient, remainder = divmod(weight, partner_count)
    return partner_count * comb(quotient, 2) + remainder * quotient


def audit_system(
    k: int,
    endpoint_occurrences: tuple[tuple[int, ...], ...],
    assigned_endpoint: tuple[int, ...],
    weights: tuple[int, ...],
    tokens: tuple[dict[int, Token], ...],
) -> None:
    occurrence_count = len(assigned_endpoint)
    assert len(weights) == occurrence_count == len(tokens)
    positions: dict[tuple[int, int], int] = {}
    for endpoint, occurrences in enumerate(endpoint_occurrences):
        assert len(set(occurrences)) == len(occurrences)
        for position, occurrence in enumerate(occurrences):
            assert 0 <= occurrence < occurrence_count
            assert endpoint in tokens[occurrence]
            positions[endpoint, occurrence] = position

    key_records: dict[
        tuple[int, int, int, int, int], list[tuple[int, int, int]]
    ] = defaultdict(list)
    expected_internal = 0
    total = 0
    for occurrence, (endpoint, weight) in enumerate(
        zip(assigned_endpoint, weights)
    ):
        occurrences = endpoint_occurrences[endpoint]
        degree = len(occurrences)
        assert degree >= 2
        position = positions[endpoint, occurrence]
        first_slot, first_other = tokens[occurrence][endpoint]
        assert 0 <= first_slot < 12
        assert 0 <= first_other < k and first_other != endpoint
        expected_internal += internal_formula(weight, degree - 1)
        for decoration in range(weight):
            shift = 1 + decoration % (degree - 1)
            partner = occurrences[(position + shift) % degree]
            assert partner != occurrence
            second_slot, second_other = tokens[partner][endpoint]
            assert 0 <= second_slot < 12
            assert 0 <= second_other < k and second_other != endpoint
            key_records[
                (
                    endpoint,
                    first_slot,
                    first_other,
                    second_slot,
                    second_other,
                )
            ].append((occurrence, decoration, partner))
            total += 1

    assert total == sum(weights)
    assert len(key_records) <= 144 * k * (k - 1) ** 2
    collision = sum(comb(len(records), 2) for records in key_records.values())
    assert total * total <= len(key_records) * (total + 2 * collision)

    internal = 0
    track_reuse = 0
    internal_by_band: Counter[int] = Counter()
    for records in key_records.values():
        for first, second in combinations(records, 2):
            first_occurrence, first_decoration, first_partner = first
            second_occurrence, second_decoration, second_partner = second
            if (
                first_occurrence == second_occurrence
                and first_partner == second_partner
            ):
                internal += 1
                weight = weights[first_occurrence]
                band = 1 << (weight.bit_length() - 1)
                internal_by_band[band] += 1
                endpoint = assigned_endpoint[first_occurrence]
                degree = len(endpoint_occurrences[endpoint])
                assert (
                    first_decoration - second_decoration
                ) % (degree - 1) == 0
            else:
                track_reuse += 1
                # Equality of the key gives the repeated first track if the
                # first owners differ, and the repeated second track if the
                # partners differ.
                assert (
                    first_occurrence != second_occurrence
                    or first_partner != second_partner
                )
    assert internal == expected_internal
    assert collision == internal + track_reuse
    assert 2 * internal <= sum(
        weight * weight
        // (len(endpoint_occurrences[endpoint]) - 1)
        for endpoint, weight in zip(assigned_endpoint, weights)
    )
    assert all(
        band_mass <= 4 * k * band * band
        for band, band_mass in internal_by_band.items()
    )


def random_system(rng: Random, k: int, occurrence_count: int) -> None:
    footprints = []
    tokens: list[dict[int, Token]] = []
    for _ in range(occurrence_count):
        size = rng.randrange(2, min(k, 12) + 1)
        footprint = tuple(sorted(rng.sample(range(k), size)))
        footprints.append(footprint)
        token_map: dict[int, Token] = {}
        for endpoint in footprint:
            other = rng.randrange(k - 1)
            if other >= endpoint:
                other += 1
            token_map[endpoint] = rng.randrange(12), other
        tokens.append(token_map)
    endpoint_occurrences = tuple(
        tuple(
            occurrence
            for occurrence, footprint in enumerate(footprints)
            if endpoint in footprint
        )
        for endpoint in range(k)
    )
    eligible = [
        occurrence
        for occurrence, footprint in enumerate(footprints)
        if any(len(endpoint_occurrences[x]) >= 2 for x in footprint)
    ]
    if not eligible:
        return
    assigned = []
    weights = []
    kept_tokens = []
    old_to_new = {old: new for new, old in enumerate(eligible)}
    restricted_endpoint_occurrences = tuple(
        tuple(old_to_new[o] for o in occurrences if o in old_to_new)
        for occurrences in endpoint_occurrences
    )
    # Restriction can destroy eligibility, so retain only systems in which
    # every chosen endpoint still has a partner.  The exhaustive deterministic
    # systems below cover the boundary cases.
    for old in eligible:
        candidates = [
            x
            for x in footprints[old]
            if len(restricted_endpoint_occurrences[x]) >= 2
        ]
        if not candidates:
            return
        assigned.append(min(candidates))
        weights.append(rng.randrange(1, 40))
        kept_tokens.append(tokens[old])
    audit_system(
        k,
        restricted_endpoint_occurrences,
        tuple(assigned),
        tuple(weights),
        tuple(kept_tokens),
    )


def exhaustive_cycles() -> None:
    for degree in range(2, 9):
        k = degree + 1
        occurrences = tuple(range(degree))
        endpoint_occurrences = (occurrences,) + tuple(() for _ in range(k - 1))
        tokens = tuple(
            {0: (occurrence % 12, occurrence + 1)}
            for occurrence in occurrences
        )
        for weight in range(1, 25):
            audit_system(
                k,
                endpoint_occurrences,
                (0,) * degree,
                (weight,) * degree,
                tokens,
            )


def main() -> None:
    exhaustive_cycles()
    rng = Random(120820260821)
    for k in range(5, 28):
        for _ in range(80):
            random_system(rng, k, rng.randrange(3, 35))
    print("SWAP CYCLIC ENDPOINT DERANGEMENT: PASS")


if __name__ == "__main__":
    main()
