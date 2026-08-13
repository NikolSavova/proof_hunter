#!/usr/bin/env python3
"""Exact H-S-T0 carry-triangle elementary lemma."""

from __future__ import annotations

import argparse
import json


def verify(t: int) -> dict[str, object]:
    H = {i * t for i in range(t)}
    S = {i * (t + 1) for i in range(t)}
    T = {i * (t - 1) for i in range(t + 1)}
    B = t * t
    Q = set(range(B, 2 * B))
    HS = {x + y for x in H for y in S}
    HT = {x + y for x in H for y in T}
    STB = {x + y + B for x in S for y in T}
    HSB = {x + B for x in HS}
    HTB = {x + B for x in HT}
    ST = {x + y for x in S for y in T}
    return {
        "t": t,
        "even": t % 2 == 0,
        "pass": Q <= HS | HT | STB,
        "missing": sorted(Q - (HS | HT | STB)),
        "reverse_pass": Q <= HSB | HTB | ST,
        "reverse_missing": sorted(Q - (HSB | HTB | ST)),
        "only_HS": len(Q & (HS - HT - STB)),
        "only_HT": len(Q & (HT - HS - STB)),
        "only_ST_shift_B": len(Q & (STB - HS - HT)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, default=100)
    args = parser.parse_args()
    rows = [verify(t) for t in range(2, args.through + 1, 2)]
    print(
        json.dumps(
            {
                "status": "PASS" if all(row["pass"] and row["reverse_pass"] for row in rows) else "FAIL",
                "scope": f"even t through {args.through}",
                "rows": rows,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
