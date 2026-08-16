#!/usr/bin/env python3
"""Regression suite for the mass-truncated weighted Kraft theorem."""

from __future__ import annotations

import math
import random
from fractions import Fraction
from itertools import combinations, permutations, product


def profiles(order, sizes, active=None):
    """Return weighted cap/cup rewards, or unweighted ranks on active labels."""
    n = len(sizes)
    if active is None:
        weight = [math.log2(1 + value) for value in sizes]
        cap = [0.0] * n
        cup = [0.0] * n
        for i, j in order:
            cap[i] = max(cap[i], cap[j] + weight[j])
            cup[j] = max(cup[j], cup[i] + weight[i])
        return cap, cup

    active = set(active)
    cap = [0] * n
    cup = [0] * n
    for i, j in order:
        if i not in active or j not in active:
            continue
        cap[i] = max(cap[i], cap[j] + 1)
        cup[j] = max(cup[j], cup[i] + 1)
    return cap, cup


def verify_row(order, sizes, s):
    m = len(sizes)
    total = sum(sizes)
    level = math.log2(total)
    q = math.log2(m)
    ell = [math.log2(value) for value in sizes]
    cap, cup = profiles(order, sizes)
    reward = [cap[i] + cup[i] for i in range(m)]
    bank = max(0.5 * ell[i] ** 2 + reward[i] for i in range(m))

    eps = -math.log2(1 - 2 ** (-s))
    theorem = 0.5 * (level - eps) ** 2 - 0.5 * (q + s) ** 2
    assert bank + 2e-10 >= theorem

    t = level - q - s
    if t > 0:
        active = tuple(i for i in range(m) if ell[i] + 1e-14 >= t)
        rank_cap, rank_cup = profiles(order, sizes, active)
        lengths = [rank_cap[i] + rank_cup[i] for i in active]
        kraft = sum((Fraction(1, 2 ** value) for value in lengths), Fraction())
        assert kraft <= 1
        for i, length in zip(active, lengths):
            assert reward[i] + 2e-10 >= t * length
        retained = sum(sizes[i] for i in active)
        assert retained > total * (1 - 2 ** (-s)) - 1e-9

        # Recheck each inequality in the analytic chain.
        retained_log = math.log2(retained)
        direct = t * retained_log - 0.5 * t * t
        square = 0.5 * retained_log ** 2 - 0.5 * (retained_log - t) ** 2
        assert abs(direct - square) < 1e-8
        assert bank + 2e-10 >= direct

    chosen = math.ceil(math.log2(level)) + 2
    explicit = (
        0.5 * level ** 2
        - 0.5 * (q + math.log2(level) + 3) ** 2
        - 1 / (3 * math.log(2))
    )
    assert bank + 2e-10 >= explicit
    if level >= 2 * (q + 1):
        optimized = (
            0.5 * level ** 2
            - 0.5 * (q + math.log2(level / (q + 1)) + 3) ** 2
            - (q + 1) / (3 * math.log(2))
        )
        assert bank + 2e-10 >= optimized
    return t > 0


def exhaustive_four() -> tuple[int, int]:
    edges = tuple(combinations(range(4), 2))
    rows = 0
    nontrivial = 0
    for order in permutations(edges):
        for sizes in product((1, 2, 8, 64), repeat=4):
            nontrivial += verify_row(order, sizes, 3)
            rows += 1
    return rows, nontrivial


def normalized_kraft_barrier() -> int:
    order = (
        (1, 2), (1, 3), (2, 3), (0, 3), (0, 2),
        (0, 1), (0, 4), (1, 4), (2, 4), (3, 4),
    )
    sizes = (256, 16, 16, 16, 256)
    count = 0
    for s in (1.5, 2, 3, 4, 5, 6):
        count += verify_row(order, sizes, s)
    return count


def random_rows() -> tuple[int, int]:
    rng = random.Random(83820260816)
    rows = 0
    nontrivial = 0
    for m in range(2, 17):
        edges = tuple(combinations(range(m), 2))
        for _ in range(900):
            order = list(edges)
            rng.shuffle(order)
            sizes = tuple(
                rng.choice((1, 2, 3, 5, 16, 257, 4096, 65537))
                for _ in range(m)
            )
            level = math.log2(sum(sizes))
            for s in (1, 2, math.ceil(math.log2(level)) + 2):
                nontrivial += verify_row(order, sizes, s)
                rows += 1
    return rows, nontrivial


def main() -> None:
    exhaustive, exhaustive_nontrivial = exhaustive_four()
    barrier_nontrivial = normalized_kraft_barrier()
    random_count, random_nontrivial = random_rows()
    print(
        "PASS: truncated weighted Kraft square mesh; "
        f"exhaustive_rows={exhaustive}; "
        f"exhaustive_nontrivial={exhaustive_nontrivial}; "
        f"normalized_barrier_nontrivial={barrier_nontrivial}; "
        f"random_rows={random_count}; random_nontrivial={random_nontrivial}"
    )


if __name__ == "__main__":
    main()
