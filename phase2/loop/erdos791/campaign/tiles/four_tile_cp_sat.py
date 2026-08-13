#!/usr/bin/env python3
"""CP-SAT feasibility search for the conservative four-tile predicate.

The mathematical predicate and type names are documented in
``four_tile_search.py``.  FEASIBLE placements are independently re-evaluated
with that module.  INFEASIBLE is relative to the supplied type counts and
coordinate box; OR-Tools does not provide a portable proof certificate.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from ortools.sat.python import cp_model

sys.path.insert(0, str(Path(__file__).resolve().parent))
from four_tile_search import NAMES, coverage_bits, parse_counts, prefix_length  # noqa: E402


def and_var(model: cp_model.CpModel, terms: list[cp_model.IntVar], name: str) -> cp_model.IntVar:
    out = model.new_bool_var(name)
    for term in terms:
        model.add(out <= term)
    model.add(out >= sum(terms) - len(terms) + 1)
    return out


def sum_present(
    model: cp_model.CpModel,
    left: list[cp_model.IntVar],
    right: list[cp_model.IntVar],
    limit: int,
    label: str,
) -> list[cp_model.IntVar]:
    out = []
    for q in range(limit):
        witnesses = [
            and_var(model, [left[a], right[q - a]], f"{label}_w{q}_{a}")
            for a in range(q + 1)
            if a < len(left) and q - a < len(right)
        ]
        present = model.new_bool_var(f"{label}_sum{q}")
        for witness in witnesses:
            model.add_implication(witness, present)
        model.add_bool_or(witnesses).only_enforce_if(present)
        out.append(present)
    return out


def solve(args: argparse.Namespace) -> dict[str, object]:
    model = cp_model.CpModel()
    chosen = {
        name: [model.new_bool_var(f"{name}_{q}") for q in range(args.bound + 1)]
        for name in NAMES
    }
    for name in NAMES:
        model.add(sum(chosen[name]) == args.counts[name])

    # The only rule able to cover square zero is one of I+J, I+K, I+L0.
    model.add(chosen["I"][0] == 1)
    model.add_bool_or([chosen["J"][0], chosen["K"][0], chosen["L0"][0]])

    pairs = {
        label: sum_present(model, chosen[a], chosen[b], args.target, label)
        for label, a, b in (
            ("ij", "I", "J"),
            ("ik", "I", "K"),
            ("il", "I", "L0"),
            ("jk", "J", "K"),
            ("jl", "J", "L0"),
            ("kl0", "K", "L0"),
            ("kl1", "K", "L1"),
        )
    }
    for q in range(args.target):
        alternatives = [pairs["ij"][q], pairs["ik"][q], pairs["il"][q]]
        if q:
            alternatives.extend(
                [
                    and_var(model, [pairs["jk"][q - 1], pairs["jk"][q]], f"jk_c{q}"),
                    and_var(model, [pairs["jl"][q - 1], pairs["jl"][q]], f"jl_c{q}"),
                    and_var(model, [pairs["kl0"][q - 1], pairs["kl1"][q]], f"kl_01_{q}"),
                    and_var(model, [pairs["kl1"][q - 1], pairs["kl0"][q]], f"kl_10_{q}"),
                ]
            )
        model.add_bool_or(alternatives)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.seconds
    solver.parameters.num_search_workers = args.workers
    solver.parameters.random_seed = args.seed
    solver.parameters.log_search_progress = args.log_progress
    started = time.monotonic()
    status_code = solver.solve(model)
    status = solver.status_name(status_code)
    result: dict[str, object] = {
        "status": status,
        "scope": "Exact conservative four-tile predicate for fixed counts and coordinate box.",
        "counts": args.counts,
        "ell": sum(args.counts.values()),
        "target": args.target,
        "bound": args.bound,
        "wall_seconds": time.monotonic() - started,
        "solver_wall_seconds": solver.wall_time,
        "branches": solver.num_branches,
        "conflicts": solver.num_conflicts,
        "seed": args.seed,
    }
    if status_code in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        placement = {
            name: {q for q, var in enumerate(chosen[name]) if solver.value(var)}
            for name in NAMES
        }
        prefix = prefix_length(coverage_bits(placement, args.target + 64), args.target + 64)
        if prefix < args.target:
            raise RuntimeError(f"independent evaluator rejected solver placement: prefix {prefix}")
        result["verified_prefix"] = prefix
        result["placement"] = {name: sorted(values) for name, values in placement.items()}
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--counts", type=parse_counts, required=True)
    parser.add_argument("--target", type=int, required=True)
    parser.add_argument("--bound", type=int)
    parser.add_argument("--seconds", type=float, default=300.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--seed", type=int, default=79104)
    parser.add_argument("--log-progress", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.bound is None:
        args.bound = args.target - 1
    result = solve(args)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
