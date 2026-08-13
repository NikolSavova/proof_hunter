#!/usr/bin/env python3
"""Exact CP-SAT search for the enlarged phased four-direction predicate."""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from ortools.sat.python import cp_model


NAMES = ("I", "J", "K", "L0", "L1")


def parse_counts(raw: str) -> dict[str, int]:
    values = [int(x) for x in raw.split(",")]
    if len(values) != 5 or any(x < 0 for x in values):
        raise argparse.ArgumentTypeError("counts must be I,J,K,L0,L1")
    return dict(zip(NAMES, values))


def and_var(model: cp_model.CpModel, terms: list[cp_model.IntVar], name: str) -> cp_model.IntVar:
    out = model.new_bool_var(name)
    for term in terms:
        model.add(out <= term)
    model.add(out >= sum(terms) - len(terms) + 1)
    return out


def sum_present(model, left, right, limit: int, label: str):
    out = []
    for q in range(limit):
        witnesses = [
            and_var(model, [left[a], right[q - a]], f"{label}_w{q}_{a}")
            for a in range(q + 1)
        ]
        present = model.new_bool_var(f"{label}_sum{q}")
        for witness in witnesses:
            model.add_implication(witness, present)
        model.add_bool_or(witnesses).only_enforce_if(present)
        out.append(present)
    return out


def pair_sums(a: set[int], b: set[int]) -> set[int]:
    return {x + y for x in a for y in b}


def coverage(placement: dict[str, set[int]]) -> set[int]:
    I, J, K, L0, L1 = (placement[name] for name in NAMES)
    ij, ik, il0 = pair_sums(I, J), pair_sums(I, K), pair_sums(I, L0)
    jk, jl0 = pair_sums(J, K), pair_sums(J, L0)
    il1, jl1 = pair_sums(I, L1), pair_sums(J, L1)
    kl0, kl1 = pair_sums(K, L0), pair_sums(K, L1)
    consecutive = lambda s: {q for q in s if q - 1 in s}
    return (
        ij | ik | il0 | consecutive(jk) | consecutive(jl0)
        | consecutive(il1) | consecutive(jl1)
        | {q for q in il1 if q - 1 in il0}
        | {q for q in jl0 if q - 1 in jl1}
        | {q for q in kl1 if q - 1 in kl0}
        | {q for q in kl0 if q - 1 in kl1}
    )


def prefix(placement: dict[str, set[int]], limit: int) -> int:
    covered = coverage(placement)
    return next((q for q in range(limit) if q not in covered), limit)


def literal_check(placement: dict[str, set[int]], t: int, m: int) -> dict[str, int | bool]:
    B = t * t
    elementary = {
        "I": set(range(t + 1)),
        "J": {i * t for i in range(t)},
        "K": {i * (t + 1) for i in range(t)},
        "L0": {i * (t - 1) for i in range(t + 1)},
        "L1": {i * (t - 1) + 1 for i in range(t + 1)},
    }
    basis = {
        x + B * q
        for name in NAMES for q in placement[name] for x in elementary[name]
    }
    sums = {a + b for a in basis for b in basis if a <= b}
    missing = next((x for x in range(m * B) if x not in sums), None)
    return {"t": t, "basis_size": len(basis), "pass": missing is None,
            "first_missing": -1 if missing is None else missing}


def solve(args) -> dict[str, object]:
    model = cp_model.CpModel()
    chosen = {
        name: [model.new_bool_var(f"{name}_{q}") for q in range(args.target)]
        for name in NAMES
    }
    for name in NAMES:
        model.add(sum(chosen[name]) == args.counts[name])
    model.add(chosen["I"][0] == 1)
    model.add_bool_or([chosen["J"][0], chosen["K"][0], chosen["L0"][0]])

    pair_specs = (
        ("ij", "I", "J"), ("ik", "I", "K"), ("il0", "I", "L0"),
        ("jk", "J", "K"), ("jl0", "J", "L0"),
        ("il1", "I", "L1"), ("jl1", "J", "L1"),
        ("kl0", "K", "L0"), ("kl1", "K", "L1"),
    )
    pairs = {
        label: sum_present(model, chosen[a], chosen[b], args.target, label)
        for label, a, b in pair_specs
    }
    for q in range(args.target):
        alternatives = [pairs["ij"][q], pairs["ik"][q], pairs["il0"][q]]
        if q:
            for label in ("jk", "jl0", "il1", "jl1"):
                alternatives.append(and_var(
                    model, [pairs[label][q - 1], pairs[label][q]], f"{label}_c{q}"
                ))
            alternatives.extend([
                and_var(model, [pairs["il0"][q - 1], pairs["il1"][q]], f"il01_{q}"),
                and_var(model, [pairs["jl1"][q - 1], pairs["jl0"][q]], f"jl10_{q}"),
                and_var(model, [pairs["kl0"][q - 1], pairs["kl1"][q]], f"kl01_{q}"),
                and_var(model, [pairs["kl1"][q - 1], pairs["kl0"][q]], f"kl10_{q}"),
            ])
        model.add_bool_or(alternatives)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.seconds
    solver.parameters.num_search_workers = args.workers
    solver.parameters.random_seed = args.seed
    solver.parameters.symmetry_level = 3
    started = time.monotonic()
    status_code = solver.solve(model)
    result: dict[str, object] = {
        "status": solver.status_name(status_code),
        "scope": "Exact enlarged phased predicate, fixed counts, coordinates [0,m-1]",
        "counts": args.counts,
        "ell": sum(args.counts.values()),
        "target": args.target,
        "seed": args.seed,
        "wall_seconds": time.monotonic() - started,
        "branches": solver.num_branches,
        "conflicts": solver.num_conflicts,
    }
    if status_code in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        placement = {
            name: {q for q, var in enumerate(chosen[name]) if solver.value(var)}
            for name in NAMES
        }
        verified = prefix(placement, args.target + 64)
        if verified < args.target:
            raise RuntimeError(f"independent predicate rejected witness at {verified}")
        direct = [literal_check(placement, t, args.target) for t in (2, 4, 6, 10)]
        if not all(row["pass"] for row in direct):
            raise RuntimeError(f"literal check rejected witness: {direct}")
        result["verified_prefix"] = verified
        result["placement"] = {name: sorted(placement[name]) for name in NAMES}
        result["literal_checks"] = direct
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--counts", type=parse_counts, required=True)
    parser.add_argument("--target", type=int, required=True)
    parser.add_argument("--seconds", type=float, default=300)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--seed", type=int, default=791)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = solve(args)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
