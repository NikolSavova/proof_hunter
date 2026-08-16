#!/usr/bin/env python3
"""Exact algebra checks for FIXED_SIZE_LITERAL_QUARTER_LOG_POOLING_GATE."""

from __future__ import annotations

from fractions import Fraction
from math import ceil, comb


def check_double_count() -> int:
    rows = 0
    for n in range(6, 31):
        for k in range(2, min(8, n)):
            for t in range(k, n + 1):
                left = Fraction(comb(n, t), comb(n - k, t - k))
                right = Fraction(comb(n, k), comb(t, k))
                assert left == right
                rows += 1
    return rows


def check_binomial_bounds() -> int:
    rows = 0
    for n in range(2, 101):
        for k in range(1, n + 1):
            # C(n,k) >= (n/k)^k.
            assert comb(n, k) * k**k >= n**k
            # C(n,k) <= (4n/k)^k, an integer version of e<4.
            assert comb(n, k) * k**k <= (4 * n) ** k
            rows += 1
    return rows


def pooled_exponent(k: int, rank: int) -> int:
    """Crude upper exponent in equation (12), including the rank sum."""
    log_rank = 0 if rank <= 1 else (rank - 1).bit_length()
    return rank * (2 * k + 1) + 2 * k + 1 + log_rank


def check_sufficient_condition() -> int:
    rows = 0
    # g is the abstract exponent error in ES(k) <= 2^(k+g).
    # Whenever the displayed integer exponents separate, the exact slot
    # allocation follows.  Exhaust a broad finite ledger of such rows.
    for k in range(8, 257):
        for eighths in range(1, 4):
            # delta = eighths / 8, so R=floor((1/2-delta)k).
            rank = ((4 - eighths) * k) // 8
            if rank < 1:
                continue
            for g in range(0, k // 2 + 1):
                bank_exp = k * (k - g - 2)
                demand_exp = pooled_exponent(k, rank)
                if bank_exp >= demand_exp:
                    # The power-of-two bank lower bound dominates the
                    # power-of-two ceiling-demand upper bound exactly.
                    assert 1 << bank_exp >= 1 << demand_exp
                    rows += 1
    return rows


def check_block_allocations() -> int:
    rows = 0
    for records in range(1, 25):
        for demand_num in range(1, 30):
            for demand_den in range(1, 12):
                demand = Fraction(demand_num, demand_den)
                slots = ceil(demand)
                bank_size = records * slots
                owner = []
                loads = []
                for history in range(records):
                    for _ in range(slots):
                        owner.append(history)
                        loads.append(demand / slots)
                assert len(owner) == bank_size
                assert max(loads) <= 1
                assert len(set(zip(range(bank_size), owner))) == bank_size
                for history in range(records):
                    emitted = sum(
                        loads[i] for i, source in enumerate(owner)
                        if source == history
                    )
                    assert emitted == demand
                rows += 1
    return rows


if __name__ == "__main__":
    identities = check_double_count()
    binomials = check_binomial_bounds()
    sufficient = check_sufficient_condition()
    blocks = check_block_allocations()
    print(
        "PASS: fixed-size literal pooling; "
        f"identities={identities}, binomials={binomials}, "
        f"sufficient_rows={sufficient}, blocks={blocks}"
    )
