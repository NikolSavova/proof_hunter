#!/usr/bin/env python3
"""Exact finite checker for the reflected-diagonal elementary tile lemmas."""

from __future__ import annotations

import argparse
import json


def segments(t: int) -> dict[str, set[int]]:
    return {
        "V": set(range(t + 1)),
        "H": {i * t for i in range(t)},
        "S": {i * (t + 1) for i in range(t)},
        "T": {i * (t - 1) for i in range(t + 1)},
    }


def add(a: set[int], b: set[int]) -> set[int]:
    return {x + y for x in a for y in b}


def verify(t: int) -> dict[str, object]:
    e = segments(t)
    q0 = set(range(t * t))
    q1 = set(range(t * t, 2 * t * t))
    st = add(e["S"], e["T"])
    return {
        "t": t,
        "even": t % 2 == 0,
        "V+H_contains_Q": q0 <= add(e["V"], e["H"]),
        "V+S_contains_Q": q0 <= add(e["V"], e["S"]),
        "V+T_contains_Q": q0 <= add(e["V"], e["T"]),
        "H+S_two_consecutive_contains_next_Q": q1 <= (add(e["H"], e["S"]) | {x + t * t for x in add(e["H"], e["S"])}),
        "H+T_two_consecutive_contains_next_Q": q1 <= (add(e["H"], e["T"]) | {x + t * t for x in add(e["H"], e["T"])}),
        "S+T_cross_phase_contains_next_Q": q1 <= (st | {x + t * t + 1 for x in st}),
        "S+T_missing_cross_phase": len(q1 - (st | {x + t * t + 1 for x in st})),
        "S+T_reverse_cross_phase_contains_next_Q": q1 <= ({x + 1 for x in st} | {x + t * t for x in st}),
        "S+T_missing_reverse_cross_phase": len(q1 - ({x + 1 for x in st} | {x + t * t for x in st})),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, default=100)
    args = parser.parse_args()
    rows = [verify(t) for t in range(2, args.through + 1)]
    even_pass = all(
        all(
            value
            for key, value in row.items()
            if key not in {"t", "even", "S+T_missing_cross_phase", "S+T_missing_reverse_cross_phase"}
        )
        for row in rows
        if row["even"]
    )
    print(json.dumps({"even_t_pass": even_pass, "through": args.through, "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
