#!/usr/bin/env python3
"""Generate a proof-capable DIMACS encoding of the local #791 search.

This deliberately uses only elementary Tseitin clauses and a fully equivalent
unary cardinality circuit.  A SAT model decodes to literal placement sets; an
UNSAT result can be accompanied by a DRAT proof from a proof-producing solver.
The seed is normalized by swapping J and K, matching the ``0 in J`` symmetry
break before the replacement-radius constraint is imposed.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path


SEED = {
    "I": [0, 5, 112, 117, 122, 127, 132, 137],
    # normalized orientation: published K becomes J
    "J": [0, 1, 2, 3, 4, 224, 225, 226, 227, 228, 229, 367, 368, 369, 370, 371, 372],
    "K": [10, 16, 22, 28, 34, 40, 46, 52, 58, 64, 70, 76, 82, 88, 94, 100, 106],
}


@dataclass
class CNF:
    next_var: int = 1
    clauses: list[tuple[int, ...]] = field(default_factory=list)
    names: dict[str, int] = field(default_factory=dict)

    def var(self, name: str) -> int:
        value = self.next_var
        self.next_var += 1
        self.names[name] = value
        return value

    def add(self, *literals: int) -> None:
        if not literals:
            raise ValueError("empty clause")
        self.clauses.append(tuple(literals))

    @property
    def num_vars(self) -> int:
        return self.next_var - 1


def equivalence_and(cnf: CNF, out: int, left: int, right: int) -> None:
    cnf.add(-out, left)
    cnf.add(-out, right)
    cnf.add(-left, -right, out)


def equivalence_or(cnf: CNF, out: int, inputs: list[int]) -> None:
    for value in inputs:
        cnf.add(-value, out)
    cnf.add(-out, *inputs)


def at_least_counter(cnf: CNF, inputs: list[int], limit: int, label: str) -> list[int]:
    """Return variables for 'at least j' (j=1..limit), with exact semantics."""
    previous: list[int] = []
    for i, x in enumerate(inputs, start=1):
        current: list[int] = []
        for j in range(1, min(i, limit) + 1):
            y = cnf.var(f"count_{label}_{i}_{j}")
            a = previous[j - 1] if j <= len(previous) else None  # old count >= j
            b = previous[j - 2] if j >= 2 else 0  # old count >= j-1; 0 means TRUE
            if a is None and b == 0:
                # y <-> x
                cnf.add(-y, x)
                cnf.add(-x, y)
            elif a is None:
                # y <-> (b AND x)
                cnf.add(-y, b)
                cnf.add(-y, x)
                cnf.add(-b, -x, y)
            elif b == 0:
                # y <-> (a OR x)
                cnf.add(-a, y)
                cnf.add(-x, y)
                cnf.add(-y, a, x)
            else:
                # y <-> (a OR (b AND x))
                cnf.add(-a, y)
                cnf.add(-b, -x, y)
                cnf.add(-y, a, b)
                cnf.add(-y, a, x)
            current.append(y)
        previous = current
    return previous


def exactly(cnf: CNF, inputs: list[int], count: int, label: str) -> None:
    outputs = at_least_counter(cnf, inputs, count + 1, label)
    cnf.add(outputs[count - 1])
    cnf.add(-outputs[count])


def at_most(cnf: CNF, inputs: list[int], count: int, label: str) -> None:
    if count >= len(inputs):
        return
    outputs = at_least_counter(cnf, inputs, count + 1, label)
    cnf.add(-outputs[count])


def normalize_seed(
    seed: dict[str, list[int]], counts: tuple[int, int, int]
) -> dict[str, list[int]]:
    normalized = {name: sorted(seed[name]) for name in ("I", "J", "K")}
    if 0 not in normalized["J"] and 0 in normalized["K"]:
        if counts[1] != counts[2]:
            raise ValueError("cannot swap J/K seed orientation with unequal counts")
        normalized["J"], normalized["K"] = normalized["K"], normalized["J"]
    if tuple(len(normalized[name]) for name in ("I", "J", "K")) != counts:
        raise ValueError("seed type counts do not match --counts")
    return normalized


def build(
    target_m: int,
    bound: int,
    counts: tuple[int, int, int],
    radius: int | None,
    seed: dict[str, list[int]] | None,
) -> tuple[CNF, dict[str, object]]:
    if bound < target_m - 1:
        raise ValueError("bound must be at least target_m-1")
    cnf = CNF()
    chosen = {
        name: [cnf.var(f"{name}_{p}") for p in range(bound + 1)]
        for name in ("I", "J", "K")
    }
    named_counts = dict(zip(("I", "J", "K"), counts))
    for name, count in named_counts.items():
        exactly(cnf, chosen[name], count, f"exact_{name}")
    cnf.add(chosen["I"][0])
    # When |J|=|K| their roles are interchangeable, so this is a valid
    # symmetry normalization.  A local seed radius also uses this orientation.
    if counts[1] == counts[2] or radius is not None:
        cnf.add(chosen["J"][0])

    sum_present: dict[str, list[int]] = {}
    for label, left_name, right_name in (
        ("IJ", "I", "J"),
        ("IK", "I", "K"),
        ("JK", "J", "K"),
    ):
        present: list[int] = []
        for q in range(target_m):
            witnesses: list[int] = []
            for a in range(max(0, q - bound), min(bound, q) + 1):
                b = q - a
                witness = cnf.var(f"w_{label}_{q}_{a}")
                equivalence_and(cnf, witness, chosen[left_name][a], chosen[right_name][b])
                witnesses.append(witness)
            value = cnf.var(f"sum_{label}_{q}")
            equivalence_or(cnf, value, witnesses)
            present.append(value)
        sum_present[label] = present

    # u OR v OR (d_prev AND d_here), distributed without another Tseitin var.
    for q in range(target_m):
        u = sum_present["IJ"][q]
        v = sum_present["IK"][q]
        if q == 0:
            cnf.add(u, v)
        else:
            cnf.add(u, v, sum_present["JK"][q - 1])
            cnf.add(u, v, sum_present["JK"][q])

    if radius is not None:
        if seed is None:
            raise ValueError("--radius requires a compatible seed")
        if any(p > bound for name in ("I", "J", "K") for p in seed[name]):
            raise ValueError("seed coordinate exceeds coordinate bound")
        absent_seed = [-chosen[name][p] for name in ("I", "J", "K") for p in seed[name]]
        at_most(cnf, absent_seed, radius, "seed_absences")
    metadata: dict[str, object] = {
        "encoding": "Tseitin membership/pair-sums + exact unary cardinality",
        "target_m": target_m,
        "coordinate_bound": bound,
        "fixed_type_counts": list(counts),
        "max_replacements_from_normalized_seed": radius,
        "seed_orientation": seed,
        "variables": cnf.num_vars,
        "clauses": len(cnf.clauses),
        "chosen_variables": {
            name: {str(p): variable for p, variable in enumerate(values)}
            for name, values in chosen.items()
        },
    }
    return cnf, metadata


def write_dimacs(cnf: CNF, path: Path) -> None:
    with path.open("w", encoding="ascii") as handle:
        handle.write(f"p cnf {cnf.num_vars} {len(cnf.clauses)}\n")
        for clause in cnf.clauses:
            handle.write(" ".join(map(str, clause)))
            handle.write(" 0\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-m", type=int, default=511)
    parser.add_argument("--coordinate-bound", type=int, default=510)
    parser.add_argument("--counts", type=int, nargs=3, default=[8, 17, 17], metavar=("I", "J", "K"))
    parser.add_argument("--radius", type=int)
    parser.add_argument("--seed-certificate", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--metadata", type=Path, required=True)
    args = parser.parse_args()
    counts = tuple(args.counts)
    if args.seed_certificate:
        raw_seed = json.loads(args.seed_certificate.read_text(encoding="utf-8"))
        seed = normalize_seed({name: raw_seed[name] for name in ("I", "J", "K")}, counts)
    elif counts == (8, 17, 17):
        seed = normalize_seed(SEED, counts)
    else:
        seed = None
    cnf, metadata = build(
        args.target_m,
        args.coordinate_bound,
        counts,
        args.radius,
        seed,
    )
    write_dimacs(cnf, args.output)
    args.metadata.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in metadata.items() if k != "chosen_variables"}, indent=2))


if __name__ == "__main__":
    main()
