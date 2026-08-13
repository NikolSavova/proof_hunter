#!/usr/bin/env python3
"""Macro predicate for the V/H bootstrap plus seven-slope point automaton."""

from __future__ import annotations

from seven_slope_tiles import SLOPES


BOOTSTRAP = "V"
ROLE_NAMES = (BOOTSTRAP,) + tuple(f"R{a}" for a in SLOPES)


def pair_sums(left: set[int], right: set[int]) -> set[int]:
    return {a + b for a in left for b in right}


def coverage(placement: dict[str, set[int]], limit: int) -> set[int]:
    out = pair_sums(placement[BOOTSTRAP], placement["R0"])
    for index, a in enumerate(SLOPES):
        for b in SLOPES[index + 1 :]:
            sums = pair_sums(placement[f"R{a}"], placement[f"R{b}"])
            out |= {q for q in sums if q - 1 in sums}
    return {q for q in out if 0 <= q < limit}


def prefix_length(values: set[int]) -> int:
    q = 0
    while q in values:
        q += 1
    return q
