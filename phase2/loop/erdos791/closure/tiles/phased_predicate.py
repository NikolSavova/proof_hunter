#!/usr/bin/env python3
"""Exact abstract predicate for the two-phase reflected fourth direction.

For placement sets I,J,K,L0,L1, the bitset returned by ``coverage_bits`` is
certified by the elementary inclusions checked in ``phased_lemma_verify.py``.
The predicate is sufficient for literal A_t+A_t coverage for every even t.
"""

from __future__ import annotations


NAMES = ("I", "J", "K", "L0", "L1")


def sum_bits(left: set[int], right: set[int], limit: int) -> int:
    out = 0
    for a in left:
        for b in right:
            q = a + b
            if 0 <= q < limit:
                out |= 1 << q
    return out


def coverage_bits(placement: dict[str, set[int]], limit: int) -> int:
    I, J, K, L0, L1 = (placement[name] for name in NAMES)
    ij = sum_bits(I, J, limit)
    ik = sum_bits(I, K, limit)
    il0 = sum_bits(I, L0, limit)
    il1 = sum_bits(I, L1, limit)
    jk = sum_bits(J, K, limit)
    jl0 = sum_bits(J, L0, limit)
    jl1 = sum_bits(J, L1, limit)
    kl0 = sum_bits(K, L0, limit)
    kl1 = sum_bits(K, L1, limit)
    return (
        ij
        | ik
        | il0
        | (jk & (jk << 1))
        | (jl0 & (jl0 << 1))
        | ((il0 << 1) & il1)
        | (il1 & (il1 << 1))
        | ((jl1 << 1) & jl0)
        | (jl1 & (jl1 << 1))
        | ((kl0 << 1) & kl1)
        | ((kl1 << 1) & kl0)
    )


def prefix_length(bits: int, limit: int) -> int:
    missing = (~bits) & ((1 << limit) - 1)
    return limit if not missing else (missing & -missing).bit_length() - 1
