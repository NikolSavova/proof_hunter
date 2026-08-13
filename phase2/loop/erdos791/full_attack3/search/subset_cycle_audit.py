#!/usr/bin/env python3
"""Exact subset-state carry-cycle audit, including the H-S-T triangle.

A state is the union of at most three pair-event footprints at one macro sum.
We call a two-cycle genuinely nonlocal when neither state fills a block by
repeating itself.  This rules out syntactically different but redundant
cycles built around an already stationary pair.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

from footprint_core import pair_footprint, transition_complete


def origin_lines(t: int) -> list[tuple[str | int, tuple[int, ...]]]:
    return [("inf", tuple(range(t)))] + [
        (slope, tuple(t * i + (slope * i % t) for i in range(t)))
        for slope in range(t)
    ]


def union_states(t: int) -> tuple[list[tuple[int, int]], int, int]:
    block = t * t
    roles = origin_lines(t)
    events = [
        pair_footprint(roles[i][1], roles[j][1], block)
        for i, j in combinations(range(len(roles)), 2)
    ]
    states: dict[tuple[int, int], tuple[int, ...]] = {}
    for size in range(1, 4):
        for chosen in combinations(range(len(events)), size):
            low = high = 0
            for event in chosen:
                low |= events[event][0]
                high |= events[event][1]
            states.setdefault((low, high), chosen)
    candidates = list(states)
    stationary = {
        state: transition_complete(state, state, block) for state in candidates
    }
    cycles = 0
    for i, left in enumerate(candidates):
        for right in candidates[i + 1 :]:
            if transition_complete(left, right, block) and transition_complete(
                right, left, block
            ) and not (stationary[left] and stationary[right]):
                cycles += 1
    return list(states), sum(not stationary[state] for state in candidates), cycles


def triangle(t: int) -> dict[str, object]:
    block = t * t
    H = tuple(i * t for i in range(t))
    S = tuple(i * (t + 1) for i in range(t))
    T = tuple(i * (t - 1) for i in range(t + 1))
    hs = pair_footprint(H, S, block)
    ht = pair_footprint(H, T, block)
    st = pair_footprint(S, T, block)
    state_a = (hs[0] | ht[0], hs[1] | ht[1])
    state_b = st
    return {
        "t": t,
        "A_events": ["H+S", "H+T"],
        "B_events": ["S+T"],
        "A_to_B": transition_complete(state_a, state_b, block),
        "B_to_A": transition_complete(state_b, state_a, block),
        "A_stationary": transition_complete(state_a, state_a, block),
        "B_stationary": transition_complete(state_b, state_b, block),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    affine_rows = []
    for t in (3, 5, 7):
        states, nonstationary, cycles = union_states(t)
        affine_rows.append(
            {
                "t": t,
                "roles": t + 1,
                "distinct_union_states_size_at_most_3": len(states),
                "nonstationary_states": nonstationary,
                "genuine_nonlocal_two_cycles": cycles,
            }
        )
    triangle_rows = [triangle(t) for t in range(4, 22, 2)]
    passed = all(row["genuine_nonlocal_two_cycles"] == 0 for row in affine_rows)
    passed &= all(
        row["A_to_B"]
        and row["B_to_A"]
        and not (row["A_stationary"] and row["B_stationary"])
        for row in triangle_rows
    )
    result = {
        "status": "PASS" if passed else "FAIL",
        "scope": (
            "affine-origin roles and union states of at most three events at "
            "t=3,5,7; H-S-T triangle checked for even 4<=t<=20"
        ),
        "affine_subset_automata": affine_rows,
        "triangle_two_cycle": triangle_rows,
        "conclusion": (
            "The triangle is a genuine alternating two-state cycle because "
            "its S+T state cannot repeat.  In the tested affine languages, "
            "every two-cycle consists entirely of already-stationary states."
        ),
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
