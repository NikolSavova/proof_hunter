#!/usr/bin/env python3
"""Try to lift the t=3 seven-chromatic topology with t+1 points per type.

Type zero is fixed to [0,t], as it is in the t=3 core.  Therefore an UNSAT
result is exact for this normalization but is not a global obstruction to a
different realization of a seven-chromatic graph.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ortools.sat.python import cp_model

from chromatic_core import TYPES, edges
from footprint_core import direct_complete


def solve(t: int, seconds: float) -> dict[str, object]:
    block = t * t
    size = t + 1
    model = cp_model.CpModel()
    active = [
        [model.new_bool_var(f"x.{role}.{point}") for point in range(block)]
        for role in range(len(TYPES))
    ]
    for role in range(len(TYPES)):
        model.add(sum(active[role]) == size)
        model.add(active[role][0] == 1)
    for point in range(block):
        model.add(active[0][point] == (point < size))
    for left, right in edges():
        for target in range(block):
            witnesses = []
            for point in range(target + 1):
                witness = model.new_bool_var(
                    f"w.{left}.{right}.{target}.{point}"
                )
                model.add(witness <= active[left][point])
                model.add(witness <= active[right][target - point])
                model.add(
                    witness
                    >= active[left][point] + active[right][target - point] - 1
                )
                witnesses.append(witness)
            model.add_bool_or(witnesses)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = 8
    solver.parameters.random_seed = 791_400 + t
    solver.parameters.symmetry_level = 3
    status_code = solver.solve(model)
    result: dict[str, object] = {
        "t": t,
        "block": block,
        "points_per_type": size,
        "type_zero_fixed_to": list(range(size)),
        "status": solver.status_name(status_code),
        "wall_seconds": solver.wall_time,
        "branches": solver.num_branches,
        "conflicts": solver.num_conflicts,
    }
    if status_code in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        decoded = [
            [point for point in range(block) if solver.value(active[role][point])]
            for role in range(len(TYPES))
        ]
        if not all(direct_complete(decoded[i], decoded[j], block) for i, j in edges()):
            raise RuntimeError("decoded lift fails")
        result.update({"types": decoded, "all_59_required_edges_verified": True})
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=30)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = [solve(t, args.seconds) for t in (4, 5, 6, 7)]
    unknown = any(row["status"] == "UNKNOWN" for row in rows)
    result = {
        "status": "HAS_UNKNOWN" if unknown else "COMPLETE_IN_NORMALIZED_SCOPE",
        "scope": (
            "fixed 14-vertex edge topology, each type has t+1 points and "
            "contains zero, type zero fixed to [0,t]; not a global seven-chromatic no-go"
        ),
        "rows": rows,
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
