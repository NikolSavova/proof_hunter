#!/usr/bin/env python3
"""Exact arithmetic audit for the recursive E-module half barrier.

This verifies the binary profile/rank recurrences, stationary tropical
coefficients, several hostile nonstationary E(r,s) schedules, and a finite
Pareto census of all oriented strong trees.  The asymptotic all-tree lower
bound is proved in the companion markdown artifact.
"""

from __future__ import annotations

from functools import lru_cache
from math import comb, log2


Profile = tuple[int, int, int, int]  # size, caps, cups, convex subsets
Rank = tuple[int, int, int, int]     # size, cap rank, cup rank, face rank


def compose_profile(a: Profile, b: Profile) -> Profile:
    na, ca, ua, va = a
    nb, cb, ub, vb = b
    return (na + nb,
            ca * (1 + nb) + cb,
            ua + ub * (1 + na),
            va + vb + ca * ub)


def compose_rank(a: Rank, b: Rank) -> Rank:
    na, ca, ua, va = a
    nb, cb, ub, vb = b
    return (na + nb,
            max(ca + 1, cb),
            max(ua, ub + 1),
            max(va, vb, ca + ub))


def e_module(r: int, s: int, leaf, compose):
    """Apply the expanded E(r,s) binary tree to a common leaf state."""
    cache = {}

    def go(rr: int, ss: int):
        if rr == 2 or ss == 2:
            return leaf
        key = rr, ss
        if key not in cache:
            cache[key] = compose(go(rr, ss - 1), go(rr - 1, ss))
        return cache[key]

    return go(r, s)


def log2_int(value: int) -> float:
    """Stable log2 of an arbitrarily large positive integer."""
    assert value > 0
    bits = value.bit_length()
    if bits <= 53:
        return log2(value)
    shift = bits - 53
    return shift + log2(value >> shift)


def stationary_rows(k: int, depths: tuple[int, ...]):
    profile: Profile = (1, 1, 1, 1)
    rows = []
    for depth in range(1, max(depths) + 1):
        profile = e_module(k, k, profile, compose_profile)
        if depth in depths:
            n, c, u, v = profile
            length = log2_int(n)
            rows.append((depth, length, log2_int(c) / length ** 2,
                         log2_int(u) / length ** 2,
                         log2_int(v) / length ** 2))
    macro_size = comb(2 * k - 4, k - 2)
    predicted = (k - 2) / log2(macro_size)
    assert predicted >= 0.5
    return macro_size, predicted, rows


def run_schedule(schedule: list[tuple[int, int]]) -> tuple[Profile, list]:
    profile: Profile = (1, 1, 1, 1)
    rows = []
    for step, (r, s) in enumerate(schedule, 1):
        profile = e_module(r, s, profile, compose_profile)
        n, c, u, v = profile
        length = log2_int(n)
        rows.append((step, r, s, length,
                     log2_int(c) / length ** 2,
                     log2_int(u) / length ** 2,
                     log2_int(v) / length ** 2))
    return profile, rows


def pareto_census(max_n: int):
    """All nondominated exact (C,U,V) states through max_n leaves."""
    states: dict[int, set[tuple[int, int, int]]] = {1: {(1, 1, 1)}}
    rows = []
    for n in range(2, max_n + 1):
        raw = set()
        for left_size in range(1, n):
            right_size = n - left_size
            for ca, ua, va in states[left_size]:
                for cb, ub, vb in states[right_size]:
                    raw.add((ca * (1 + right_size) + cb,
                             ua + ub * (1 + left_size),
                             va + vb + ca * ub))
        ordered = sorted(raw, key=lambda z: (z[2], z[0], z[1]))
        frontier: list[tuple[int, int, int]] = []
        for candidate in ordered:
            if any(old[0] <= candidate[0]
                   and old[1] <= candidate[1]
                   and old[2] <= candidate[2]
                   for old in frontier):
                continue
            frontier = [old for old in frontier
                        if not (candidate[0] <= old[0]
                                and candidate[1] <= old[1]
                                and candidate[2] <= old[2])]
            frontier.append(candidate)
        states[n] = set(frontier)
        best = min(frontier, key=lambda z: z[2])
        rows.append((n, len(raw), len(frontier), best,
                     log2(best[2]) / log2(n) ** 2))
    return rows


def main() -> None:
    # Exact E(r,s) support sizes and ranks, including the reset macro.
    for r in range(3, 13):
        for s in range(3, 13):
            rank = e_module(r, s, (1, 1, 1, 1), compose_rank)
            expected_size = comb(r + s - 4, r - 2)
            assert rank == (expected_size, s - 1, r - 1, r + s - 4)
            assert expected_size <= 2 ** (rank[1] + rank[2] - 2)

    reset_rank: Rank = (1, 1, 1, 1)
    reset_rows = []
    for h in range(1, 9):
        reset_rank = e_module(7, 7, reset_rank, compose_rank)
        assert reset_rank == (252 ** h, 5 * h + 1, 5 * h + 1, 10 * h)
        reset_rows.append((h,) + reset_rank)

    # Stationary exact integer powers converge to the tropical fixed point.
    stationary = {}
    for k in (4, 7, 12, 20):
        stationary[k] = stationary_rows(k, (1, 2, 4, 8, 12))
        macro_size, predicted, rows = stationary[k]
        # The depth-12 value has the expected finite-size direction.  A
        # generous tolerance avoids pretending that convergence is fast.
        assert rows[-1][-1] >= 0.5
        assert abs(rows[-1][-1] - predicted) < 0.08

    # Hostile actual ramps: alternate cap-heavy and cup-heavy E modules;
    # grow balanced modules; and repeat the perfect-reset macro.
    schedules = {
        "alternating": [(3, 12) if j % 2 == 0 else (12, 3)
                        for j in range(16)],
        "growing_balanced": [(k, k) for k in range(3, 15)],
        "reset_E77": [(7, 7)] * 12,
        "sawtooth": ([(3, 9), (5, 8), (8, 5), (9, 3)] * 4),
    }
    schedule_rows = {}
    for name, schedule in schedules.items():
        profile, rows = run_schedule(schedule)
        assert profile[3] >= profile[0]  # every singleton is a face
        schedule_rows[name] = rows

    # Exact exhaustive regression of every oriented binary strong tree
    # through twelve leaves.  This is evidence/recurrence QA, not the proof
    # of the asymptotic theorem.
    census = pareto_census(12)
    expected_min_v = {
        2: 3, 3: 7, 4: 14, 5: 26, 6: 45, 7: 75,
        8: 120, 9: 184, 10: 271, 11: 389, 12: 542,
    }
    assert {row[0]: row[3][2] for row in census} == expected_min_v

    print("PASS")
    print("  E(r,s) ranks checked for 3<=r,s<=12")
    print("  perfect-reset rank rows (h,n,cap,cup,face):", reset_rows)
    print("  stationary tropical rows:")
    for k, (macro_size, predicted, rows) in stationary.items():
        print(f"    E({k},{k}): size={macro_size}, fixed_point={predicted:.12f}, "
              f"depth12_V={rows[-1][-1]:.12f}")
    print("  nonstationary schedules (final C,U,V coefficients):")
    for name, rows in schedule_rows.items():
        final = rows[-1]
        print(f"    {name}: depth={final[0]}, logN={final[3]:.6f}, "
              f"C={final[4]:.9f}, U={final[5]:.9f}, V={final[6]:.9f}")
    print("  exact Pareto census rows (n,raw,frontier,best,coefficient):")
    for row in census:
        print("   ", row)


if __name__ == "__main__":
    main()
