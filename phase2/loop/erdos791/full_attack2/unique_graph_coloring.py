#!/usr/bin/env python3
"""Exact coloring/deletion experiments for unique-representation graphs."""

import argparse
import json
from pathlib import Path

from ortools.sat.python import cp_model


def unique_graph(A, n):
    counts = {}
    witness = {}
    for i, a in enumerate(A):
        for j in range(i, len(A)):
            s = a + A[j]
            if s <= n:
                counts[s] = counts.get(s, 0) + 1
                witness[s] = (i, j)
    edges = []
    loops = []
    for s, count in counts.items():
        if count != 1:
            continue
        i, j = witness[s]
        (loops if i == j else edges).append((i, j) if i != j else i)
    return edges, loops


def colorable(k, edges, colors, seconds):
    model = cp_model.CpModel()
    x = [model.new_int_var(0, colors - 1, f"x{i}") for i in range(k)]
    model.add(x[0] == 0)
    for i, j in edges:
        model.add(x[i] != x[j])
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_workers = 8
    status = solver.solve(model)
    return solver.status_name(status), [solver.value(v) for v in x] if status in (cp_model.OPTIMAL, cp_model.FEASIBLE) else None


def min_delete_to_color(k, edges, colors, seconds):
    model = cp_model.CpModel()
    x = [model.new_int_var(0, colors - 1, f"x{i}") for i in range(k)]
    deleted = [model.new_bool_var(f"d{i}") for i in range(k)]
    for z, (i, j) in enumerate(edges):
        same = model.new_bool_var(f"same{z}")
        model.add(x[i] == x[j]).only_enforce_if(same)
        model.add(x[i] != x[j]).only_enforce_if(same.Not())
        model.add_bool_or([deleted[i], deleted[j], same.Not()])
    model.minimize(sum(deleted))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_workers = 8
    status = solver.solve(model)
    return solver.status_name(status), solver.objective_value, solver.best_objective_bound


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("basis", type=Path)
    ap.add_argument("--colors-through", type=int, default=6)
    ap.add_argument("--delete-colors", type=int, default=4)
    ap.add_argument("--seconds", type=float, default=60)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    d = json.loads(args.basis.read_text())
    A = sorted(set(d.get("A", d.get("I", []) + d.get("J", []) + d.get("K", []))))
    n = int(d.get("n", d.get("m", 0) - 1))
    edges, loops = unique_graph(A, n)
    rows = []
    for colors in range(2, args.colors_through + 1):
        status, coloring = colorable(len(A), edges, colors, args.seconds)
        rows.append({"colors": colors, "status": status, "coloring": coloring})
        if coloring is not None:
            break
    ds, obj, bound = min_delete_to_color(len(A), edges, args.delete_colors, args.seconds)
    out = {
        "basis_size": len(A), "range": n, "unique_edges": len(edges),
        "unique_loops": len(loops), "coloring_attempts": rows,
        "delete_to_colors": args.delete_colors, "deletion_status": ds,
        "minimum_deleted": obj, "deletion_best_bound": bound,
    }
    print(json.dumps(out, indent=2))
    if args.output: args.output.write_text(json.dumps(out, indent=2) + "\n")


if __name__ == "__main__":
    main()
