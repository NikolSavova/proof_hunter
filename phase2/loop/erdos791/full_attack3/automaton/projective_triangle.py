#!/usr/bin/env python3
"""Exact projective-size modular carry triangle and point transition automaton."""

from __future__ import annotations


STATES = ("XY", "YZ", "XZ")


def tiles(q: int) -> tuple[int, dict[str, set[int]]]:
    if q < 3:
        raise ValueError(q)
    B = q * q - q + 1
    X = {(q - 1) * i for i in range(q)}
    Y = set(range(q))
    Z = {0} | {1 + q * i for i in range(q - 1)}
    return B, {"X": X, "Y": Y, "Z": Z}


def footprints(q: int) -> tuple[int, dict[str, tuple[set[int], set[int]]]]:
    B, p = tiles(q)
    Q = set(range(B))
    out: dict[str, tuple[set[int], set[int]]] = {}
    for name, left, right in (("XY", "X", "Y"), ("YZ", "Y", "Z"), ("XZ", "X", "Z")):
        sums = {x + y for x in p[left] for y in p[right]}
        out[name] = (Q & sums, {x - B for x in sums if B <= x < 2 * B})
    return B, out


def transitions(q: int) -> dict[str, list[str]]:
    B, f = footprints(q)
    Q = set(range(B))
    return {
        old: [new for new in STATES if f[old][1] | f[new][0] == Q]
        for old in STATES
    }


def direct_macro_coverage(
    placement: dict[str, set[int]], limit: int, q: int
) -> set[int]:
    """Literal point-footprint predicate, not a square-Boolean shortcut."""
    B, p = tiles(q)
    A = {
        name: {B * macro + x for macro in placement[name] for x in p[name]}
        for name in ("X", "Y", "Z")
    }
    sums = {x + y for name in A for x in A[name] for name2 in A for y in A[name2]}
    return {
        macro
        for macro in range(limit)
        if set(range(macro * B, (macro + 1) * B)) <= sums
    }
