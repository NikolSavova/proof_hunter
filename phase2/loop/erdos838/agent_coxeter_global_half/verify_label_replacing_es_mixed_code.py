#!/usr/bin/env python3
"""Exact verifier for LABEL_REPLACING_ES_MIXED_CODE.md."""

from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import ceil, comb

from verify_rooted_fan_complement import (
    add_coherent_root,
    convex_hull_size,
    cup_cap_lengths,
    cup_cap_set,
    genericize,
    orient,
    root_order,
)
from verify_weighted_history_hall_barrier import es_profile


@lru_cache(None)
def size(r: int, s: int) -> int:
    return comb(r + s - 4, r - 2)


@lru_cache(None)
def cup_coefficients(r: int, s: int) -> tuple[int, ...]:
    """Coefficients of the nonempty cup polynomial U_{r,s}(t)."""
    if r == 2 or s == 2:
        return (0, 1)
    left = cup_coefficients(r, s - 1)
    right = cup_coefficients(r - 1, s)
    out = [0] * max(len(left), len(right) + 1)
    for rank, count in enumerate(left):
        out[rank] += count
    for rank, count in enumerate(right):
        out[rank] += count
        out[rank + 1] += size(r, s - 1) * count
    return tuple(out)


def evaluate(coefficients: tuple[int, ...], activity: Q) -> Q:
    return sum(
        (count * activity**rank for rank, count in enumerate(coefficients)),
        Q(0),
    )


def is_cup(points, subset: tuple[int, ...]) -> bool:
    return all(
        orient(points[subset[index]], points[subset[index + 1]], points[subset[index + 2]]) > 0
        for index in range(len(subset) - 2)
    )


def is_cap(points, subset: tuple[int, ...]) -> bool:
    return all(
        orient(points[subset[index]], points[subset[index + 1]], points[subset[index + 2]]) < 0
        for index in range(len(subset) - 2)
    )


def homogeneous_subsets(points, sign: int) -> list[tuple[int, ...]]:
    cup_rank, cap_rank = cup_cap_lengths(points)
    max_rank = cup_rank if sign > 0 else cap_rank
    predicate = is_cup if sign > 0 else is_cap
    return [
        subset
        for rank in range(1, max_rank + 1)
        for subset in combinations(range(len(points)), rank)
        if predicate(points, subset)
    ]


def symbolic_row(k: int) -> dict[str, object]:
    coefficients = cup_coefficients(k, k)
    m = size(k, k)
    n = m + 1
    cups_one = evaluate(coefficients, Q(1))
    cups_half = evaluate(coefficients, Q(1, 2))
    assert cups_one == es_profile(k, k, Q(1))[2]
    assert cups_half == es_profile(k, k, Q(1, 2))[2]

    w = es_profile(k - 1, k, Q(1))[2]
    top_mixed = w * w
    exact_tokens = sum(
        count * ceil(Q(n, 1 << (rank + 1)))
        for rank, count in enumerate(coefficients)
    )
    upper_tokens = Q(n, 2) * cups_half + cups_one
    assert exact_tokens <= upper_tokens
    assert top_mixed >= upper_tokens
    assert top_mixed >= exact_tokens

    # Uniform estimates used for k >= 16.
    path_product = 1
    for r in range(3, k):
        path_product *= 1 + size(r, k - 1)
    assert w >= path_product
    assert cups_one <= (4**k) * w * (1 + Q(m, 2))
    assert cups_one <= (4**k) * m * w
    if k >= 16:
        exponent = (k - 3) * (k - 2) // 2
        assert w >= 1 << exponent
        assert exponent >= 6 * k - 8
        assert m <= 1 << (2 * k - 4)
        assert w >= 3 * (4 ** (k - 1)) * m * m

    return {
        "k": k,
        "m": m,
        "cups": int(cups_one),
        "tokens": exact_tokens,
        "upper_tokens": upper_tokens,
        "top_mixed": top_mixed,
        "margin": Q(top_mixed, 1) / upper_tokens,
        "terminal_codewords": ceil(Q(n, 1 << k)),
    }


def geometric_code(k: int = 5) -> dict[str, int]:
    points = genericize(cup_cap_set(k, k))
    m = len(points)
    n = m + 1
    left_size = size(k, k - 1)
    left = points[:left_size]
    right = points[left_size:]

    histories = homogeneous_subsets(points, 1)
    rooted = add_coherent_root(points, 1)
    reflection_time = {root: index for index, root in enumerate(root_order(rooted))}
    for history in histories:
        shifted = tuple(index + 1 for index in history)
        path = ((0, shifted[0]),) + tuple(
            (shifted[index], shifted[index + 1])
            for index in range(len(shifted) - 1)
        )
        times = tuple(reflection_time[edge] for edge in path)
        assert all(a < b for a, b in zip(times, times[1:]))
        assert convex_hull_size(
            (rooted[0],) + tuple(rooted[index] for index in shifted)
        ) == len(shifted) + 1
    left_caps_local = homogeneous_subsets(left, -1)
    right_cups_local = homogeneous_subsets(right, 1)
    left_caps = [tuple(index for index in cap) for cap in left_caps_local]
    right_cups = [
        tuple(left_size + index for index in cup) for cup in right_cups_local
    ]
    assert len(histories) == es_profile(k, k, Q(1))[2]
    expected_factor = es_profile(k - 1, k, Q(1))[2]
    assert len(left_caps) == len(right_cups) == expected_factor

    mixed = [cap + cup for cap in left_caps for cup in right_cups]
    left_cap_set = set(left_caps)
    right_cup_set = set(right_cups)
    assert len(mixed) == len(set(mixed))
    assert all(convex_hull_size(tuple(points[index] for index in face)) == len(face) for face in mixed)
    assert all(
        tuple(index for index in face if index < left_size) in left_cap_set
        and tuple(index for index in face if index >= left_size) in right_cup_set
        for face in mixed
    )

    block_owner: dict[int, int] = {}
    cursor = 0
    emitted = Q(0)
    max_load = Q(0)
    terminal = tuple(range(k - 1))
    terminal_codewords = 0
    for history_index, history in enumerate(histories):
        demand = Q(n, 1 << (len(history) + 1))
        block_size = ceil(demand)
        for output_index in range(cursor, cursor + block_size):
            assert output_index not in block_owner
            block_owner[output_index] = history_index
        load = demand / block_size
        assert load <= 1
        emitted += load * block_size
        max_load = max(max_load, load)
        if history == terminal:
            terminal_codewords = block_size
        cursor += block_size

    assert cursor <= len(mixed)
    assert len(block_owner) == cursor
    assert emitted == Q(n, 2) * es_profile(k, k, Q(1, 2))[2]
    assert all(0 <= owner < len(histories) for owner in block_owner.values())
    assert terminal_codewords == ceil(Q(n, 1 << k))
    return {
        "k": k,
        "m": m,
        "histories": len(histories),
        "mixed": len(mixed),
        "used": cursor,
        "max_load_num": max_load.numerator,
        "max_load_den": max_load.denominator,
        "terminal_codewords": terminal_codewords,
    }


def main() -> None:
    rows = [symbolic_row(k) for k in range(5, 41)]
    geometry = geometric_code()
    expected_margins = {
        5: 3.444356515041204,
        6: 58.82983791309642,
        8: 1310457.123462918,
        10: 16568611038510.205,
        12: 1.5738173977334888e23,
        15: 4.82931092306667e43,
    }
    for row in rows:
        if row["k"] in expected_margins:
            got = float(row["margin"])
            want = expected_margins[row["k"]]
            assert abs(got - want) <= 1e-12 * max(1.0, abs(want))

    print("label-replacing ES mixed code: PASS")
    print(
        f"geometry E({geometry['k']},{geometry['k']}) m={geometry['m']} "
        f"histories={geometry['histories']} mixed={geometry['mixed']} "
        f"used={geometry['used']} max_load="
        f"{geometry['max_load_num']}/{geometry['max_load_den']} "
        f"terminal_codewords={geometry['terminal_codewords']}"
    )
    for k in (5, 6, 8, 10, 12, 15, 20, 30, 40):
        row = rows[k - 5]
        margin = row["margin"]
        tokens = row["tokens"]
        token_text = str(tokens) if k <= 12 else f"{tokens.bit_length()} bits"
        if k < 40:
            margin_text = f"{float(margin):.4e}"
        else:
            margin_bits = margin.numerator.bit_length() - margin.denominator.bit_length()
            margin_text = f">=2^{margin_bits}"
        print(
            f"symbolic k={k:2d} m={row['m']:22d} "
            f"tokens={token_text} terminal={row['terminal_codewords']} "
            f"margin={margin_text}"
        )


if __name__ == "__main__":
    main()
