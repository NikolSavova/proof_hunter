#!/usr/bin/env python3
"""Enumerate every type split for one enhanced four-tile threshold."""

from __future__ import annotations

import argparse
import json
from itertools import product
from pathlib import Path
from types import SimpleNamespace

from enhanced_four_tile_cp_sat import NAMES, solve


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ell", type=int, required=True)
    parser.add_argument("--target", type=int, required=True)
    parser.add_argument("--seconds-per-split", type=float, default=10)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = []
    capacity_killed = 0
    for raw in product(range(args.ell + 1), repeat=4):
        last = args.ell - sum(raw)
        if last < 0:
            continue
        values = (*raw, last)
        counts = dict(zip(NAMES, values))
        if counts["I"] == 0 or not (counts["J"] or counts["K"] or counts["L0"]):
            continue
        i, j, k, l0, l1 = values
        # Sum of separate witness-capacity ceilings.  Overlap only lowers the
        # actual coverage, so falling below target is a rigorous exclusion.
        capacity = (
            i*j + i*k + i*l0
            + max(0, j*k-1) + max(0, j*l0-1)
            + max(0, i*l1-1) + max(0, j*l1-1)
            + min(i*l0, i*l1) + min(j*l0, j*l1)
            + 2*min(k*l0, k*l1)
        )
        if capacity < args.target:
            capacity_killed += 1
            continue
        run = SimpleNamespace(
            counts=counts, target=args.target, seconds=args.seconds_per_split,
            workers=args.workers, seed=791000 + len(rows),
        )
        result = solve(run)
        rows.append({
            "counts": counts, "status": result["status"],
            "wall_seconds": result["wall_seconds"],
            "branches": result["branches"], "conflicts": result["conflicts"],
        })
        if "placement" in result:
            payload = {"status": "FOUND", "ell": args.ell, "target": args.target,
                       "capacity_killed": capacity_killed,
                       "tested_splits": len(rows), "result": result, "rows": rows}
            args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
            print(json.dumps(result, indent=2, sort_keys=True))
            return
    statuses = {status: sum(row["status"] == status for row in rows)
                for status in sorted({row["status"] for row in rows})}
    final_status = "NO_WITNESS" if set(statuses) <= {"INFEASIBLE"} else "UNKNOWN"
    payload = {"status": final_status, "ell": args.ell, "target": args.target,
               "capacity_killed": capacity_killed,
               "tested_splits": len(rows), "statuses": statuses, "rows": rows}
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in payload.items() if k != "rows"}, indent=2))


if __name__ == "__main__":
    main()
