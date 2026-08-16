#!/usr/bin/env python3
"""Exact verifier for JOINT_DETACHED_BANK_RANK_PROMOTION.md."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations
from math import ceil, comb

from verify_label_replacing_es_mixed_code import cup_coefficients, size
from verify_local_trace_hall_matching_barrier import audit_multi_trace
from verify_weighted_history_hall_barrier import es_profile


def unrank_combination(n: int, rank: int, index: int) -> tuple[int, ...]:
    """Zero-based lexicographic unranking."""
    assert 0 <= index < comb(n, rank)
    out = []
    lower = 0
    for position in range(rank):
        for value in range(lower, n):
            remaining = rank - position - 1
            count = comb(n - value - 1, remaining) if remaining else 1
            if index < count:
                out.append(value)
                lower = value + 1
                break
            index -= count
    assert len(out) == rank
    return tuple(out)


def rank_combination(n: int, subset: tuple[int, ...]) -> int:
    """Inverse of unrank_combination in lexicographic order."""
    index = 0
    lower = 0
    rank = len(subset)
    for position, value in enumerate(subset):
        remaining = rank - position - 1
        for skipped in range(lower, value):
            index += comb(n - skipped - 1, remaining) if remaining else 1
        lower = value + 1
    return index


def audit_matching_counts(m: int) -> dict[str, object]:
    ambient = 4 * m
    histories = 2 * m**3
    demand = Q(ambient, 8)
    total_demand = histories * demand
    assert total_demand == m**4

    detached_two = m * (m + 1)
    all_two = comb(ambient, 1) + comb(ambient, 2)
    all_three = all_two + comb(ambient, 3)
    assert Q(total_demand, detached_two) == Q(m**3, m + 1)
    assert all_two <= ambient**2
    assert all_three <= ambient**3
    assert Q(total_demand, all_two) >= Q(ambient**2, 256)
    assert Q(total_demand, all_three) >= Q(ambient, 256)

    tokens = histories * ceil(demand)
    rank_four = 2 * comb(m, 4) if m >= 4 else 0
    rank_five = 2 * comb(m, 5) if m >= 5 else 0
    if m >= 47:
        assert 14 * rank_four >= tokens
    if m >= 70:
        assert rank_five >= tokens
    if m == 70:
        assert rank_five == 24_206_028
        assert tokens == 24_010_000
    return {
        "m": m,
        "ambient": ambient,
        "histories": histories,
        "demand": demand,
        "rank_two_load": Q(total_demand, detached_two),
        "tokens": tokens,
        "rank_four": rank_four,
        "rank_five": rank_five,
    }


def audit_rank_four_code(m: int = 70, copies: int = 14) -> dict[str, object]:
    row = audit_matching_counts(m)
    block_size = ceil(row["demand"])
    bank = row["rank_four"]
    per_side = comb(m, 4)
    used = row["histories"] * block_size
    assert used <= copies * bank

    slot_samples = {0, block_size - 1, bank - 1, bank, used - 2, used - 1}
    for slot_index in slot_samples:
        copy, physical_index = divmod(slot_index, bank)
        side, local_index = divmod(physical_index, per_side)
        assert 0 <= copy < copies and side in (0, 1)
        subset = unrank_combination(m, 4, local_index)
        assert rank_combination(m, subset) == local_index
        history_index, within_block = divmod(slot_index, block_size)
        assert 0 <= history_index < row["histories"]
        assert 0 <= within_block < block_size

    max_list = 0
    max_load = Q(0)
    for physical_index in (0, 1, bank // 2, bank - 2, bank - 1):
        histories = set()
        slots_used = 0
        for copy in range(copies):
            slot = copy * bank + physical_index
            if slot < used:
                slots_used += 1
                histories.add(slot // block_size)
        assert len(histories) == slots_used
        max_list = max(max_list, len(histories))
        max_load = max(max_load, slots_used * row["demand"] / block_size)
    assert max_list <= copies and max_load <= copies
    return {
        "m": m,
        "bank": bank,
        "used": used,
        "copies": copies,
        "max_sample_list": max_list,
        "max_sample_load": max_load,
    }


def audit_rank_five_code(m: int = 70) -> dict[str, object]:
    row = audit_matching_counts(m)
    block_size = ceil(row["demand"])
    used = row["histories"] * block_size
    per_side = comb(m, 5)
    capacity = 2 * per_side
    assert used <= capacity

    # Output index -> (side, five-subset) -> output index -> history block.
    samples = {
        0,
        1,
        block_size - 1,
        block_size,
        per_side - 1,
        per_side,
        used - 2,
        used - 1,
    }
    for output_index in samples:
        side, local_index = divmod(output_index, per_side)
        assert side in (0, 1)
        subset = unrank_combination(m, 5, local_index)
        assert rank_combination(m, subset) == local_index
        reconstructed = side * per_side + rank_combination(m, subset)
        assert reconstructed == output_index
        history_index, slot = divmod(output_index, block_size)
        assert 0 <= history_index < row["histories"]
        assert 0 <= slot < block_size

        # Decode history index as (side, trace-left, trace-right, apex).
        history_side, remainder = divmod(history_index, m**3)
        trace_left, remainder = divmod(remainder, m**2)
        trace_right, apex = divmod(remainder, m)
        assert history_side in (0, 1)
        assert all(0 <= value < m for value in (trace_left, trace_right, apex))

    load = row["demand"] / block_size
    assert load <= 1
    return {
        "m": m,
        "capacity": capacity,
        "used": used,
        "block_size": block_size,
        "load": load,
    }


def audit_es_joint(k: int) -> dict[str, object]:
    coefficients = cup_coefficients(k, k)
    m = size(k, k)
    roots = m
    ambient = 2 * m
    per_root_tokens = sum(
        count * ceil(Q(ambient, 1 << (rank + 1)))
        for rank, count in enumerate(coefficients)
    )
    tokens = roots * per_root_tokens
    w = es_profile(k - 1, k, Q(1))[2]
    capacity = w * w
    cups_half = es_profile(k, k, Q(1, 2))[2]
    cups_one = es_profile(k, k, Q(1))[2]
    upper_tokens = roots * (Q(ambient, 2) * cups_half + cups_one)
    assert tokens <= upper_tokens
    if k in (5, 6):
        assert capacity < tokens
    else:
        assert capacity >= upper_tokens
        assert capacity >= tokens

    assert cups_one == sum(coefficients)
    if k >= 20:
        exponent = (k - 3) * (k - 2) // 2
        assert exponent >= 8 * k - 11
        assert w >= 1 << exponent
        assert m <= 1 << (2 * k - 4)
        assert w >= 2 * (4**k) * m**3
        assert cups_one <= (4**k) * m * w
    return {
        "k": k,
        "m": m,
        "tokens": tokens,
        "capacity": capacity,
        "upper_tokens": upper_tokens,
        "margin": Q(capacity, tokens),
    }


def main() -> None:
    # Exact geometry for a balanced multi-trace row, plus symbolic scaling.
    geometry = audit_multi_trace(m=10, traces_per_side=10)
    matching_rows = [audit_matching_counts(m) for m in range(2, 201)]
    rank_four_code = audit_rank_four_code()
    code = audit_rank_five_code()
    es_rows = [audit_es_joint(k) for k in range(5, 31)]

    print("joint detached-bank rank promotion: PASS")
    print(
        f"geometry matching m=10 traces={geometry['traces']} "
        f"detached overlap={geometry['detached_face_overlap']}"
    )
    for m in (4, 16, 32, 70, 100, 200):
        row = matching_rows[m - 2]
        print(
            f"matching m={m:3d} rank2_load={float(row['rank_two_load']):.4e} "
            f"rank5_capacity/tokens="
            f"{(float(Q(row['rank_five'], row['tokens'])) if row['rank_five'] else 0):.4e}"
        )
    print(
        f"rank4 code m={rank_four_code['m']} bank={rank_four_code['bank']} "
        f"used={rank_four_code['used']} copies={rank_four_code['copies']} "
        f"sample_list={rank_four_code['max_sample_list']} "
        f"sample_load={rank_four_code['max_sample_load']}"
    )
    print(
        f"rank5 code m={code['m']} capacity={code['capacity']} used={code['used']} "
        f"block={code['block_size']} load={code['load']}"
    )
    for k in (5, 6, 7, 8, 10, 15, 20, 30):
        row = es_rows[k - 5]
        margin = float(row["margin"]) if k <= 20 else None
        margin_text = f"{margin:.4e}" if margin is not None else f">=2^{row['margin'].numerator.bit_length() - row['margin'].denominator.bit_length()}"
        print(
            f"E({k},{k}) roots=m={row['m']:10d} joint margin={margin_text}"
        )


if __name__ == "__main__":
    main()
