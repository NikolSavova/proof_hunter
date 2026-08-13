#!/usr/bin/env python3
"""Proof-producing CNF for bounded phased role cost on a fixed basis."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from phased_role_model import PAIR_SPECS, ROLES, representation_indices


class CNF:
    def __init__(self) -> None:
        self.nvars = 0
        self.clauses: list[list[int]] = []

    def var(self) -> int:
        self.nvars += 1
        return self.nvars

    def add(self, *lits: int) -> None:
        self.clauses.append(list(lits))

    def iff_and(self, out: int, a: int, b: int) -> None:
        self.add(-out, a)
        self.add(-out, b)
        self.add(-a, -b, out)

    def iff_or(self, out: int, terms: list[int]) -> None:
        if not terms:
            self.add(-out)
            return
        for term in terms:
            self.add(-term, out)
        self.add(-out, *terms)

    def at_most(self, inputs: list[int], bound: int) -> None:
        """Exact triangular unary counter, asserting sum(inputs)<=bound."""
        if bound >= len(inputs):
            return
        if bound < 0:
            self.add()
            return
        previous: list[int] = []
        limit = bound + 1
        for row, x in enumerate(inputs, start=1):
            current: list[int] = []
            for j in range(1, min(row, limit) + 1):
                y = self.var()
                current.append(y)
                a = previous[j - 1] if j <= len(previous) else None
                if j == 1:
                    if a is None:
                        self.add(-y, x)
                        self.add(-x, y)
                    else:
                        self.add(-a, y)
                        self.add(-x, y)
                        self.add(-y, a, x)
                else:
                    b = previous[j - 2]
                    if a is None:
                        self.add(-y, b)
                        self.add(-y, x)
                        self.add(-b, -x, y)
                    else:
                        self.add(-a, y)
                        self.add(-b, -x, y)
                        self.add(-y, a, b)
                        self.add(-y, a, x)
            previous = current
        self.add(-previous[bound])


def build(
    A: tuple[int, ...], n: int, max_cost: int, three_tile: bool
) -> tuple[CNF, dict[str, object]]:
    cnf = CNF()
    role = {name: [cnf.var() for _ in A] for name in ROLES}
    if three_tile:
        for name in ("L0", "L1"):
            for variable in role[name]:
                cnf.add(-variable)
    reps = representation_indices(A, n)
    present: dict[str, list[int]] = {label: [] for label, _, _ in PAIR_SPECS}
    for label, left, right in PAIR_SPECS:
        for q in range(n + 1):
            witnesses = []
            for i, j in reps[q]:
                w = cnf.var()
                cnf.iff_and(w, role[left][i], role[right][j])
                witnesses.append(w)
            out = cnf.var()
            cnf.iff_or(out, witnesses)
            present[label].append(out)

    for q in range(n + 1):
        alternatives = [present["ij"][q], present["ik"][q], present["il0"][q]]
        if q:
            for label in ("jk", "jl0", "il1", "jl1"):
                out = cnf.var()
                cnf.iff_and(out, present[label][q - 1], present[label][q])
                alternatives.append(out)
            for name, lower, upper in (
                ("il01", "il0", "il1"),
                ("jl10", "jl1", "jl0"),
                ("kl01", "kl0", "kl1"),
                ("kl10", "kl1", "kl0"),
            ):
                del name
                out = cnf.var()
                cnf.iff_and(out, present[lower][q - 1], present[upper][q])
                alternatives.append(out)
        cnf.add(*alternatives)
    role_inputs = [role[name][i] for name in ROLES for i in range(len(A))]
    cnf.at_most(role_inputs, max_cost)
    metadata: dict[str, object] = {
        "basis": list(A),
        "target_n": n,
        "max_role_cost": max_cost,
        "three_tile": three_tile,
        "variables": cnf.nvars,
        "clauses": len(cnf.clauses),
        "role_variables": role,
    }
    return cnf, metadata


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--basis", type=int, nargs="+", required=True)
    parser.add_argument("--target-n", type=int, required=True)
    parser.add_argument("--max-cost", type=int, required=True)
    parser.add_argument("--three-tile", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--metadata", type=Path)
    args = parser.parse_args()
    A = tuple(sorted(set(args.basis)))
    if len(A) != len(args.basis):
        raise SystemExit("basis entries must be distinct")
    cnf, metadata = build(A, args.target_n, args.max_cost, args.three_tile)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as handle:
        handle.write(f"p cnf {cnf.nvars} {len(cnf.clauses)}\n")
        for clause in cnf.clauses:
            handle.write(" ".join(map(str, clause)) + " 0\n")
    metadata["cnf_sha256"] = hashlib.sha256(args.output.read_bytes()).hexdigest()
    target = args.metadata or args.output.with_suffix(".json")
    target.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    print(json.dumps(metadata, sort_keys=True))


if __name__ == "__main__":
    main()
