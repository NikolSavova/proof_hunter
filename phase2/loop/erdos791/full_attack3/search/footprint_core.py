#!/usr/bin/env python3
"""Exact point-footprint primitives for one B=t^2 integer block."""

from __future__ import annotations

from collections.abc import Iterable


def pair_footprint(left: Iterable[int], right: Iterable[int], block: int) -> tuple[int, int]:
    """Return bit masks in the current block and the carry-one block."""
    low = high = 0
    for x in left:
        for y in right:
            total = x + y
            if not 0 <= total < 2 * block:
                raise ValueError("microtype coordinates must lie in [0,B)")
            if total < block:
                low |= 1 << total
            else:
                high |= 1 << (total - block)
    return low, high


def transition_complete(previous: tuple[int, int], current: tuple[int, int], block: int) -> bool:
    """Whether carry(previous) union low(current) fills the whole block."""
    full = (1 << block) - 1
    return previous[1] | current[0] == full


def direct_complete(left: Iterable[int], right: Iterable[int], block: int) -> bool:
    return pair_footprint(left, right, block)[0] == (1 << block) - 1


def missing_points(left: Iterable[int], right: Iterable[int], block: int) -> list[int]:
    low, _ = pair_footprint(left, right, block)
    return [q for q in range(block) if not (low >> q) & 1]


def literal_periodic_check(t: int, slope: int, blocks: int) -> dict[str, object]:
    """Literal check of a stationary H--affine-line carry cycle.

    V+H initializes block zero.  Consecutive copies of H+L_slope then cover
    blocks 1,...,blocks-1.  This is a correctness test for the automaton, not
    an efficient #791 construction: its macro role cost is linear in blocks.
    """
    block = t * t
    V = set(range(t + 1))
    H = {i * t for i in range(t)}
    line = {t * i + (slope * i % t) for i in range(t)}
    literal = V | H
    for q in range(blocks):
        literal |= {block * q + x for x in line}
    sums = {x + y for x in literal for y in literal}
    first_missing = next((q for q in range(blocks * block) if q not in sums), blocks * block)
    return {
        "t": t,
        "slope": slope,
        "blocks": blocks,
        "literal_size": len(literal),
        "required_through": blocks * block - 1,
        "first_missing": first_missing,
        "pass": first_missing == blocks * block,
    }
