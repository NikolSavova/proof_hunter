#!/usr/bin/env python3
"""Bounded CP-SAT search for seven directly compatible microtypes.

This diagnostic fixes type zero to the initial interval [0,s-1].  It is not a
global nonexistence model.  SAT witnesses are decoded and independently
checked against all 21 complete-current-block conditions.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ortools.sat.python import cp_model

from footprint_core import direct_complete


KNOWN = {
    (4, 2): [
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 10],
        [0, 1, 2, 3, 5, 10],
        [0, 1, 2, 3, 7, 12],
        [0, 1, 2, 3, 8, 12],
        [0, 1, 2, 6, 8, 12],
        [0, 1, 2, 5, 9, 12],
    ],
    (5, 3): [
        [0, 1, 2, 3, 4, 5, 6, 7],
        [0, 1, 2, 3, 9, 10, 11, 19],
        [0, 2, 3, 5, 6, 8, 12, 19],
        [0, 1, 3, 4, 5, 8, 13, 21],
        [0, 1, 3, 4, 6, 8, 15, 21],
        [0, 1, 4, 5, 8, 9, 15, 20],
        [0, 1, 2, 5, 11, 12, 17, 23],
    ],
    (6, 4): [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [0, 1, 2, 6, 7, 8, 12, 17, 21, 30],
        [0, 1, 3, 4, 8, 9, 11, 18, 20, 30],
        [0, 1, 2, 3, 6, 8, 11, 15, 24, 34],
        [0, 1, 3, 4, 5, 7, 15, 17, 26, 32],
        [0, 1, 4, 5, 8, 10, 11, 17, 24, 31],
        [0, 1, 3, 4, 6, 7, 17, 18, 24, 33],
    ],
}


def solve(t: int, extra: int, seconds: float) -> dict[str, object]:
    block = t * t
    roles = 7
    size = t + extra
    model = cp_model.CpModel()
    active = [
        [model.new_bool_var(f"x.{role}.{point}") for point in range(block)]
        for role in range(roles)
    ]
    for role in range(roles):
        model.add(sum(active[role]) == size)
        model.add(active[role][0] == 1)
    for point in range(block):
        model.add(active[0][point] == (point < size))
    for left in range(roles):
        for right in range(left + 1, roles):
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
    # Weak permutation symmetry breaking on roles 1,...,6.
    coordinate_sums = []
    for role in range(1, roles):
        value = model.new_int_var(0, (block - 1) * size, f"coordinate_sum.{role}")
        model.add(value == sum(point * active[role][point] for point in range(block)))
        coordinate_sums.append(value)
    for index in range(len(coordinate_sums) - 1):
        model.add(coordinate_sums[index] <= coordinate_sums[index + 1])
    if (t, extra) in KNOWN:
        for role, points in enumerate(KNOWN[t, extra]):
            point_set = set(points)
            for point in range(block):
                model.add_hint(active[role][point], int(point in point_set))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = 8
    solver.parameters.random_seed = 791_300 + 10 * t + extra
    solver.parameters.symmetry_level = 3
    status_code = solver.solve(model)
    result: dict[str, object] = {
        "t": t,
        "block": block,
        "points_per_type": size,
        "overhead_points_minus_t": extra,
        "first_type_fixed_to_initial_interval": True,
        "status": solver.status_name(status_code),
        "wall_seconds": solver.wall_time,
        "branches": solver.num_branches,
        "conflicts": solver.num_conflicts,
    }
    if status_code in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        types = [
            [point for point in range(block) if solver.value(active[role][point])]
            for role in range(roles)
        ]
        verified = all(
            direct_complete(types[left], types[right], block)
            for left in range(roles)
            for right in range(left + 1, roles)
        )
        if not verified:
            raise RuntimeError("decoded K7 fails independent footprint check")
        result.update({"types": types, "all_21_edges_verified": True})
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=15)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cases = ((4, 2), (5, 2), (5, 3), (6, 3), (6, 4), (7, 4))
    rows = [solve(t, extra, args.seconds) for t, extra in cases]
    has_unknown = any(row["status"] == "UNKNOWN" for row in rows)
    result = {
        "status": "MIXED_SAT_UNKNOWN" if has_unknown else "PASS" if all(
            row["status"] in ("OPTIMAL", "FEASIBLE", "INFEASIBLE", "UNKNOWN")
            for row in rows
        ) else "FAIL",
        "scope": (
            "bounded fixed-initial-interval search; UNKNOWN is never promoted; "
            "SAT is an exact finite witness, not a scalable family"
        ),
        "rows": rows,
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
