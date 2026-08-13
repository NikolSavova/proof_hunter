#!/usr/bin/env python3
"""Enumerate every five-list type split for a fixed (ell,m) CP-SAT target."""

from __future__ import annotations

import argparse
import json
import time
from argparse import Namespace
from pathlib import Path

from four_tile_cp_sat import solve


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ell", type=int, required=True)
    parser.add_argument("--target", type=int, required=True)
    parser.add_argument("--seconds-per-split", type=float, default=10.0)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--seed", type=int, default=791)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rows = []
    found = None
    started = time.monotonic()
    index = 0
    # I must be nonempty because every direct full-square rule uses V.  Zero-I
    # splits cannot cover q=0 in this conservative predicate.
    for I in range(1, args.ell + 1):
        for J in range(args.ell + 1 - I):
            for K in range(args.ell + 1 - I - J):
                for L0 in range(args.ell + 1 - I - J - K):
                    L1 = args.ell - I - J - K - L0
                    counts = {"I": I, "J": J, "K": K, "L0": L0, "L1": L1}
                    result = solve(
                        Namespace(
                            counts=counts,
                            target=args.target,
                            bound=args.target - 1,
                            seconds=args.seconds_per_split,
                            workers=args.workers,
                            seed=args.seed + index,
                            log_progress=False,
                        )
                    )
                    index += 1
                    row = {
                        "counts": counts,
                        "status": result["status"],
                        "wall_seconds": result["wall_seconds"],
                        "branches": result["branches"],
                        "conflicts": result["conflicts"],
                    }
                    rows.append(row)
                    if result["status"] in ("OPTIMAL", "FEASIBLE"):
                        found = result
                        break
                if found:
                    break
            if found:
                break
        if found:
            break
    statuses = {status: sum(row["status"] == status for row in rows) for status in {row["status"] for row in rows}}
    payload = {
        "scope": "All type splits with I>=1; coordinates above target-1 cannot witness the target prefix.",
        "ell": args.ell,
        "target": args.target,
        "seconds_per_split": args.seconds_per_split,
        "splits_run": len(rows),
        "statuses": statuses,
        "found": found,
        "wall_seconds": time.monotonic() - started,
        "rows": rows,
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
