#!/usr/bin/env python3
"""Verify FIXED_SIZE_LITERAL_EXPLICIT_BOUNDARY_20260816.md."""

from __future__ import annotations

from fractions import Fraction
from math import ceil


def ceil_log2(value: int) -> int:
    assert value >= 1
    return 0 if value == 1 else (value - 1).bit_length()


def pooled_exponent(k: int, rank: int) -> int:
    return rank * (2 * k + 1) + 2 * k + 1 + ceil_log2(rank)


def cutoff(k: int, error: int) -> int:
    return (k - error) // 2 - 3


def check_exact_boundary() -> int:
    rows = 0
    for k in range(2, 801):
        for error in range(0, k + 1):
            rank = cutoff(k, error)
            if rank < 1:
                continue
            bank = k * (k - error - 2)
            demand = pooled_exponent(k, rank)
            assert demand <= bank
            # This is the displayed lower bound in (12), cleared of halves.
            gap = bank - demand
            display_twice = 3 * k + error + 4 - 2 * ceil_log2(k)
            assert 2 * gap >= display_twice
            rows += 1
    return rows


def check_fixed_gap_improvement() -> int:
    rows = 0
    # If G/k tends to zero, the explicit cutoff eventually beats every fixed
    # (1/2-delta)k cutoff.  Check the exact finite implication whenever its
    # transparent sufficient hypothesis G <= delta*k-8 holds.
    for k in range(16, 801):
        for denominator in range(2, 17):
            delta = Fraction(1, denominator)
            old = ((denominator - 2) * k) // (2 * denominator)
            for error in range(0, k + 1):
                if Fraction(error, 1) <= delta * k - 8:
                    assert cutoff(k, error) >= old
                    rows += 1
    return rows


def check_base_change() -> int:
    rows = 0
    # L=log_2 N=2k.  An abstract error G <= C sqrt(k log k)
    # becomes an O(sqrt(L log L)) displacement from L/4.  Squared integer
    # inequalities avoid floating point and verify the scale conversion.
    for k in range(16, 2001):
        ambient_log = 2 * k
        log_k = ceil_log2(k)
        log_l = ceil_log2(ambient_log)
        for constant in range(1, 7):
            # If G^2 <= C^2 k log k, then (2G)^2 <=
            # 2 C^2 L log L, a valid ambient O(sqrt(L log L)) bound.
            max_error_squared = constant**2 * k * log_k
            assert 4 * max_error_squared <= (
                2 * constant**2 * ambient_log * log_l
            )
            rows += 1
    return rows


def check_block_decoder() -> int:
    rows = 0
    for ambient in range(4, 65):
        for rank in range(1, min(8, ambient) + 1):
            demand = Fraction(ambient, 2**rank)
            slots = ceil(demand)
            for histories in range(1, 18):
                owners: list[int] = []
                loads: list[Fraction] = []
                for history in range(histories):
                    owners.extend([history] * slots)
                    loads.extend([demand / slots] * slots)
                assert len(owners) == histories * slots
                assert max(loads) <= 1
                for history in range(histories):
                    emitted = sum(
                        loads[index]
                        for index, owner in enumerate(owners)
                        if owner == history
                    )
                    assert emitted == demand
                # Every public output index has one owner/block.
                assert all(0 <= owner < histories for owner in owners)
                rows += 1
    return rows


if __name__ == "__main__":
    exact = check_exact_boundary()
    improvement = check_fixed_gap_improvement()
    base_change = check_base_change()
    blocks = check_block_decoder()
    print(
        "PASS: explicit quarter-log literal boundary; "
        f"exact={exact}, improvement={improvement}, "
        f"base_change={base_change}, blocks={blocks}"
    )
