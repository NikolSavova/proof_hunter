#!/usr/bin/env python3
"""Exact CP-SAT search for an interval basis with a unique-sum clique.

This probes (and can refute) the structural conjecture suggested by exhaustive
small data that the unique-representation graph of every interval basis is
4-colourable.  A model consists of membership variables for A subset [0,n],
unordered representation variables, and five marked vertices.  Every marked
pair is required to have sum at most n and exactly one representation in A.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ortools.sat.python import cp_model


def solve(n: int, clique_size: int, seconds: float, workers: int) -> dict[str, object]:
    model = cp_model.CpModel()
    member = [model.new_bool_var(f"a.{x}") for x in range(n + 1)]
    marked = [model.new_bool_var(f"c.{x}") for x in range(n + 1)]
    model.add(member[0] == 1)
    model.add(sum(marked) == clique_size)
    for x in range(n + 1):
        model.add_implication(marked[x], member[x])

    reps: list[list[cp_model.IntVar]] = [[] for _ in range(n + 1)]
    for x in range(n + 1):
        for y in range(x, n + 1):
            if x + y > n:
                break
            z = model.new_bool_var(f"r.{x}.{y}")
            model.add(z <= member[x])
            model.add(z <= member[y])
            model.add(z >= member[x] + member[y] - 1)
            reps[x + y].append(z)
    for q in range(n + 1):
        model.add(sum(reps[q]) >= 1)

    # Every pair of marked, distinct coordinates must be an edge of G_uniq.
    for x in range(n + 1):
        for y in range(x + 1, n + 1):
            if x + y > n:
                model.add(marked[x] + marked[y] <= 1)
                continue
            both = model.new_bool_var(f"cc.{x}.{y}")
            model.add(both <= marked[x])
            model.add(both <= marked[y])
            model.add(both >= marked[x] + marked[y] - 1)
            model.add(sum(reps[x + y]) == 1).only_enforce_if(both)

    model.minimize(sum(member))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    solver.parameters.symmetry_level = 3
    status_code = solver.solve(model)
    result: dict[str, object] = {
        "n": n,
        "clique_size": clique_size,
        "status": solver.status_name(status_code),
        "wall_time": solver.wall_time,
        "branches": solver.num_branches,
        "conflicts": solver.num_conflicts,
    }
    if status_code in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        basis = [x for x in range(n + 1) if solver.value(member[x])]
        clique = [x for x in range(n + 1) if solver.value(marked[x])]
        sums: dict[int, list[tuple[int, int]]] = {q: [] for q in range(n + 1)}
        for i, x in enumerate(basis):
            for y in basis[i:]:
                if x + y <= n:
                    sums[x + y].append((x, y))
        assert all(sums[q] for q in range(n + 1))
        assert all(
            x + y <= n and len(sums[x + y]) == 1
            for i, x in enumerate(clique)
            for y in clique[i + 1 :]
        )
        result.update(
            {
                "basis": basis,
                "basis_size": len(basis),
                "clique": clique,
                "clique_sums": {
                    str(x + y): sums[x + y]
                    for i, x in enumerate(clique)
                    for y in clique[i + 1 :]
                },
            }
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, nargs="+", required=True)
    parser.add_argument("--clique-size", type=int, default=5)
    parser.add_argument("--seconds", type=float, default=60.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rows = [solve(n, args.clique_size, args.seconds, args.workers) for n in args.n]
    payload = json.dumps({"rows": rows}, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
