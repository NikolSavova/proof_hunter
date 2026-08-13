#!/usr/bin/env python3
"""Exact CP-SAT optimizer for the cross-cover cost of one finite basis."""

import argparse
import json
from pathlib import Path

from ortools.sat.python import cp_model


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("basis", type=Path)
    ap.add_argument("--seconds", type=float, default=600)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    data = json.loads(args.basis.read_text())
    A = sorted(set(data.get("A", data.get("I", []) + data.get("J", []) + data.get("K", []))))
    n = int(data.get("m", 0)) - 1 if "m" in data else int(data["n"])
    model = cp_model.CpModel()
    V = [model.new_bool_var(f"V_{i}") for i in range(len(A))]
    H = [model.new_bool_var(f"H_{i}") for i in range(len(A))]
    for q in range(n + 1):
        witnesses = []
        for i, x in enumerate(A):
            y = q - x
            if y not in A:
                continue
            j = A.index(y)
            w = model.new_bool_var(f"w_{q}_{i}_{j}")
            model.add(w <= V[i])
            model.add(w <= H[j])
            model.add(w >= V[i] + H[j] - 1)
            witnesses.append(w)
        if not witnesses:
            raise SystemExit(f"basis misses {q}")
        model.add_bool_or(witnesses)
    model.minimize(sum(V) + sum(H))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.seconds
    solver.parameters.num_workers = 8
    solver.parameters.log_search_progress = True
    status = solver.solve(model)
    out = {
        "status": solver.status_name(status),
        "basis_size": len(A),
        "range": n,
        "minimum_cross_cover_cost": int(round(solver.objective_value))
            if status in (cp_model.OPTIMAL, cp_model.FEASIBLE) else None,
        "best_bound": solver.best_objective_bound,
        "V": [A[i] for i in range(len(A)) if status in (cp_model.OPTIMAL, cp_model.FEASIBLE) and solver.value(V[i])],
        "H": [A[i] for i in range(len(A)) if status in (cp_model.OPTIMAL, cp_model.FEASIBLE) and solver.value(H[i])],
        "wall_seconds": solver.wall_time,
        "branches": solver.num_branches,
        "conflicts": solver.num_conflicts,
    }
    print(json.dumps(out, indent=2))
    if args.output:
        args.output.write_text(json.dumps(out, indent=2) + "\n")


if __name__ == "__main__":
    main()
