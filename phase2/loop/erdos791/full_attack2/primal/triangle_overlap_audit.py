#!/usr/bin/env python3
"""Exact footprint/accounting audit for the H-S-T carry triangle."""

from __future__ import annotations

import argparse
import json


def audit(t: int) -> dict[str, int | bool]:
    H = {i * t for i in range(t)}
    S = {i * (t + 1) for i in range(t)}
    T = {i * (t - 1) for i in range(t + 1)}
    B = t * t
    Q = set(range(B, 2 * B))
    hs = Q & {x + y for x in H for y in S}
    ht = Q & {x + y for x in H for y in T}
    st = Q & {x + y + B for x in S for y in T}
    multiplicity = len(hs) + len(ht) + len(st)
    return {
        "t": t,
        "even": t % 2 == 0,
        "union_is_Q": hs | ht | st == Q,
        "HS_size": len(hs),
        "HT_size": len(ht),
        "ST_shifted_size": len(st),
        "sum_with_multiplicity": multiplicity,
        "expected_3t2_over_2": 3 * t * t // 2,
        "overlap_excess": multiplicity - t * t,
        "expected_t2_over_2": t * t // 2,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, default=100)
    args = parser.parse_args()
    rows = [audit(t) for t in range(2, args.through + 1, 2)]
    passed = all(
        row["union_is_Q"]
        and row["sum_with_multiplicity"] == row["expected_3t2_over_2"]
        and row["overlap_excess"] == row["expected_t2_over_2"]
        for row in rows
    )
    print(json.dumps({"status": "PASS" if passed else "FAIL", "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
