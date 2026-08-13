#!/usr/bin/env python3
"""Re-optimize the exact k<=8 extremal role audit with carry triangles enabled.

This imports the already-verified fixed-coordinate CP-SAT channels from the
sibling computation lane, but writes output only in this lane.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATION = HERE.parent / "computation"
sys.path.insert(0, str(COMPUTATION))

from ortools.sat.python import cp_model  # type: ignore  # noqa: E402
import phased_role_model as base  # type: ignore  # noqa: E402

from triangle_predicate import coverage_bits  # noqa: E402
from typed_predicate import prefix_length  # noqa: E402
from typed_verify import literal  # noqa: E402


def solve(A: tuple[int, ...], n: int, seconds: float) -> dict[str, object]:
    model = cp_model.CpModel()
    reps = base.representation_indices(A, n)
    role = {
        name: [model.new_bool_var(f"{name}.{i}") for i in range(len(A))]
        for name in base.ROLES
    }
    present = {label: [] for label, _, _ in base.PAIR_SPECS}
    for label, left, right in base.PAIR_SPECS:
        for q in range(n + 1):
            witnesses = [
                base.and_var(
                    model,
                    (role[left][i], role[right][j]),
                    f"w.{label}.{q}.{i}.{j}",
                )
                for i, j in reps[q]
            ]
            present[label].append(base.or_channel(model, witnesses, f"s.{label}.{q}"))
    for q in range(n + 1):
        alternatives = [present["ij"][q], present["ik"][q], present["il0"][q]]
        if q:
            alternatives += [
                base.and_var(
                    model,
                    (present[label][q - 1], present[label][q]),
                    f"adj.{label}.{q}",
                )
                for label in ("jk", "jl0", "il1", "jl1")
            ]
            alternatives += [
                base.and_var(
                    model,
                    (present[a][q - 1], present[b][q]),
                    f"mix.{a}.{b}.{q}",
                )
                for a, b in (
                    ("il0", "il1"),
                    ("jl1", "jl0"),
                    ("kl0", "kl1"),
                    ("kl1", "kl0"),
                )
            ]
            alternatives += [
                base.and_var(
                    model,
                    (present["jk"][q], present["jl0"][q], present["kl0"][q - 1]),
                    f"triangle.a.{q}",
                ),
                base.and_var(
                    model,
                    (present["jk"][q - 1], present["jl0"][q - 1], present["kl0"][q]),
                    f"triangle.b.{q}",
                ),
            ]
        model.add_bool_or(alternatives)
    cost = sum(role[name][i] for name in base.ROLES for i in range(len(A)))
    model.minimize(cost)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = 8
    solver.parameters.symmetry_level = 3
    status_code = solver.solve(model)
    status = solver.status_name(status_code)
    out: dict[str, object] = {"status": status}
    if status_code in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        placement = {
            name: {A[i] for i in range(len(A)) if solver.value(role[name][i])}
            for name in base.ROLES
        }
        verified = prefix_length(coverage_bits(placement, n + 32), n + 32)
        if verified <= n:
            raise RuntimeError((A, placement, verified))
        out.update(
            {
                "role_cost": int(solver.value(cost)),
                "placement": {name: sorted(values) for name, values in placement.items()},
                "verified_prefix": verified,
                "literal_checks": [literal(placement, t, n + 1) for t in (2, 4)],
            }
        )
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=COMPUTATION / "EXTREMAL_ROLE_RESULTS.json",
    )
    parser.add_argument("--output", type=Path, default=HERE / "TRIANGLE_ROLE_RESULTS.json")
    parser.add_argument("--seconds", type=float, default=30.0)
    args = parser.parse_args()
    source = json.loads(args.input.read_text())
    rows = []
    for row in source["rows"]:
        answers = []
        for item in row["bases"]:
            A = tuple(item["basis"])
            answer = solve(A, row["R_k"], args.seconds)
            answers.append(
                {
                    "basis": list(A),
                    "ordinary_five_list_cost": item["five_list"].get("minimum_role_cost"),
                    "triangle_five_list": answer,
                }
            )
        rows.append({"k": row["k"], "R_k": row["R_k"], "answers": answers})
        print(f"k={row['k']} complete", flush=True)
    payload = {
        "status": "PASS"
        if all(
            item["triangle_five_list"]["status"] == "OPTIMAL"
            for row in rows
            for item in row["answers"]
        )
        else "INCOMPLETE",
        "scope": "all interval-range extremal bases for 1<=k<=8",
        "rows": rows,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
