#!/usr/bin/env python3
"""Verify the low-weight first-moment collapse."""

from __future__ import annotations

from itertools import product
from math import comb, isqrt
from random import Random


def pointed(load: int) -> int:
    return load * comb(load - 1, 2)


def pair_mass(load: int) -> int:
    return comb(load, 2)


def cutoff(weight: int) -> int:
    # floor((3 + sqrt(1 + 8W))/2), evaluated exactly.
    return (3 + isqrt(1 + 8 * weight)) // 2


def audit(loads: tuple[int, ...], threshold: int) -> None:
    assert threshold >= 3
    assert all(load >= 3 for load in loads)
    for load in loads:
        assert pointed(load) == (load - 2) * pair_mass(load)

    low = sum(pointed(load) for load in loads if load < threshold)
    pairs = sum(pair_mass(load) for load in loads if load < threshold)
    assert low <= (threshold - 3) * pairs

    # The high-endpoint reduction may retain any number of occurrences from
    # each cell.  Each retained occurrence still has weight C(r-1,2).
    ranges = [range(load + 1) for load in loads]
    for retained in product(*ranges):
        restricted = sum(
            keep * comb(load - 1, 2)
            for load, keep in zip(loads, retained)
            if load < threshold
        )
        assert restricted <= low <= (threshold - 3) * pairs


def audit_weight_cutoff(weight: int) -> None:
    bound = cutoff(weight)
    for load in range(3, 80):
        if comb(load - 1, 2) <= weight:
            assert load <= bound
        else:
            assert load > bound


def audit_dyadic(loads: tuple[int, ...], threshold: int) -> None:
    high = sum(pointed(load) for load in loads if load >= threshold)
    envelope = 0
    scale = threshold
    while scale <= max(loads, default=0):
        band_pairs = sum(
            pair_mass(load)
            for load in loads
            if scale <= load < 2 * scale
        )
        envelope += 2 * scale * band_pairs
        scale *= 2
    assert high < envelope or high == 0


def main() -> None:
    for length in range(1, 4):
        for loads in product(range(3, 8), repeat=length):
            for threshold in range(3, 10):
                audit(loads, threshold)
                audit_dyadic(loads, threshold)
    rng = Random(1208)
    for _ in range(500):
        loads = tuple(rng.randrange(3, 80) for _ in range(rng.randrange(1, 20)))
        threshold = rng.randrange(3, 50)
        low = sum(pointed(load) for load in loads if load < threshold)
        pairs = sum(pair_mass(load) for load in loads if load < threshold)
        assert low <= (threshold - 3) * pairs
        audit_dyadic(loads, threshold)
    for weight in range(1, 500):
        audit_weight_cutoff(weight)
    print("SWAP LOW-WEIGHT FIRST-MOMENT COLLAPSE: PASS")


if __name__ == "__main__":
    main()
