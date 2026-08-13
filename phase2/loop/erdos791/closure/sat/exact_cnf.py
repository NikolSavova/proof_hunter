#!/usr/bin/env python3
"""Proof-oriented CNF encoding for the three-tile Erdos 791 problem.

Coordinates outside 0..m-1 can be discarded from any solution, so membership
variables only use this finite interval.  We normalize min(I)=0.  Coverage of
q=0 then forces 0 in J or K.  If their cardinalities agree, exchanging J and K
lets us choose 0 in J and apply a conditional lexicographic symmetry break.

The encoding channels every pair witness and every represented sum in both
directions.  Thus a SAT assignment decodes directly to a verifier certificate,
while an UNSAT proof applies to the exact finite problem for the requested
cardinalities (up to the documented, sound normalizations).
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


class CNF:
    def __init__(self) -> None:
        self.nvars = 0
        self.names: dict[str, int] = {}
        self.clauses: list[list[int]] = []

    def var(self, name: str) -> int:
        old = self.names.get(name)
        if old is not None:
            return old
        self.nvars += 1
        self.names[name] = self.nvars
        return self.nvars

    def add(self, *lits: int) -> None:
        self.clauses.append(list(lits))

    def iff_and(self, out: int, a: int, b: int) -> None:
        self.add(-out, a)
        self.add(-out, b)
        self.add(-a, -b, out)

    def iff_or(self, out: int, inputs: list[int]) -> None:
        if not inputs:
            self.add(-out)
            return
        for x in inputs:
            self.add(-x, out)
        self.add(-out, *inputs)

    def iff_equal_bits(self, out: int, a: int, b: int) -> None:
        # out <-> (a == b)
        self.add(-out, -a, b)
        self.add(-out, a, -b)
        self.add(a, b, out)
        self.add(-a, -b, out)

    def at_most_one(self, inputs: list[int], tag: str) -> None:
        """Linear, propagation-complete at-most-one via exact prefix ORs."""
        if len(inputs) < 2:
            return
        prefix = inputs[0]
        for index, x in enumerate(inputs[1:], start=1):
            self.add(-prefix, -x)
            new_prefix = self.var(f"amo.{tag}.{index}")
            self.iff_or(new_prefix, [prefix, x])
            prefix = new_prefix

    def convex_bits(self, inputs: list[int], tag: str) -> None:
        """Require the true inputs to form at most one contiguous interval."""
        if len(inputs) < 3:
            return
        seen = inputs[0]
        ended: int | None = None
        for index, x in enumerate(inputs[1:], start=1):
            if ended is not None:
                self.add(-ended, -x)
            gap = self.var(f"convex.gap.{tag}.{index}")
            # gap <-> seen AND NOT x
            self.add(-gap, seen)
            self.add(-gap, -x)
            self.add(-seen, x, gap)
            new_seen = self.var(f"convex.seen.{tag}.{index}")
            self.iff_or(new_seen, [seen, x])
            if ended is None:
                ended = gap
            else:
                new_ended = self.var(f"convex.ended.{tag}.{index}")
                self.iff_or(new_ended, [ended, gap])
                ended = new_ended
            seen = new_seen

    def at_least_counter(self, inputs: list[int], limit: int, tag: str) -> list[int]:
        """Return exact unary outputs y[j-1] <-> sum(inputs) >= j."""
        if limit <= 0:
            return []
        previous: list[int] = []
        for row, x in enumerate(inputs, start=1):
            width = min(row, limit)
            current: list[int] = []
            for j in range(1, width + 1):
                y = self.var(f"cnt.{tag}.{row}.{j}")
                current.append(y)
                a = previous[j - 1] if j <= len(previous) else None
                if j == 1:
                    # y <-> a OR x, where absent a is false.
                    if a is None:
                        self.add(-y, x)
                        self.add(-x, y)
                    else:
                        self.add(-a, y)
                        self.add(-x, y)
                        self.add(-y, a, x)
                else:
                    b = previous[j - 2] if j - 1 <= len(previous) else None
                    if a is None and b is None:
                        self.add(-y)
                    elif a is None:
                        # y <-> b AND x
                        self.add(-y, b)
                        self.add(-y, x)
                        self.add(-b, -x, y)
                    elif b is None:
                        # This case is unreachable for a triangular counter.
                        self.add(-a, y)
                        self.add(-y, a)
                    else:
                        # y <-> a OR (b AND x)
                        self.add(-a, y)
                        self.add(-b, -x, y)
                        self.add(-y, a, b)
                        self.add(-y, a, x)
            previous = current
        return previous

    def exactly(self, inputs: list[int], count: int, tag: str) -> None:
        if not 0 <= count <= len(inputs):
            self.add()
            return
        if count == 0:
            for x in inputs:
                self.add(-x)
            return
        outputs = self.at_least_counter(inputs, min(len(inputs), count + 1), tag)
        self.add(outputs[count - 1])
        if count < len(inputs):
            self.add(-outputs[count])

    def range_count(
        self, inputs: list[int], lower: int, upper: int, tag: str
    ) -> None:
        if lower > upper or lower > len(inputs) or upper < 0:
            self.add()
            return
        lower = max(lower, 0)
        upper = min(upper, len(inputs))
        outputs = self.at_least_counter(inputs, min(len(inputs), upper + 1), tag)
        if lower:
            self.add(outputs[lower - 1])
        if upper < len(inputs):
            self.add(-outputs[upper])


def build(
    ell: int,
    m: int,
    counts: tuple[int, int, int],
    capacity_cuts: bool,
    lex_symmetry: bool,
    k0_case: int | None,
    fixed: dict[str, list[int]] | None,
    units: list[tuple[str, int, int]],
) -> tuple[CNF, dict[str, object]]:
    ni, nj, nk = counts
    cnf = CNF()
    membership = {
        family: [cnf.var(f"{family}.{p}") for p in range(m)]
        for family in ("I", "J", "K")
    }
    for family, count in zip(("I", "J", "K"), counts):
        cnf.exactly(membership[family], count, f"card_{family}")

    # At q=0, the tile rule itself forces 0 in I and in at least one of J,K.
    # When the latter cardinalities agree, exchanging them lets us choose J.
    cnf.add(membership["I"][0])
    if nj == nk:
        cnf.add(membership["J"][0])
    else:
        cnf.add(membership["J"][0], membership["K"][0])
    if k0_case is not None:
        cnf.add(membership["K"][0] if k0_case else -membership["K"][0])

    sum_vars: dict[str, list[int]] = {}
    witness_vars: dict[str, list[list[int]]] = {}
    for ab in ("IJ", "IK", "JK"):
        a_family, b_family = ab
        sums: list[int] = []
        witness_rows: list[list[int]] = []
        for q in range(m):
            witnesses: list[int] = []
            for a in range(q + 1):
                b = q - a
                w = cnf.var(f"w.{ab}.{q}.{a}")
                cnf.iff_and(w, membership[a_family][a], membership[b_family][b])
                witnesses.append(w)
            s = cnf.var(f"sum.{ab}.{q}")
            cnf.iff_or(s, witnesses)
            sums.append(s)
            witness_rows.append(witnesses)
        sum_vars[ab] = sums
        witness_vars[ab] = witness_rows

    direct: list[int] = []
    consecutive: list[int] = []
    for q in range(m):
        d = cnf.var(f"direct.{q}")
        cnf.iff_or(d, [sum_vars["IJ"][q], sum_vars["IK"][q]])
        direct.append(d)
        c = cnf.var(f"consecutive.{q}")
        if q == 0:
            cnf.add(-c)
        else:
            cnf.iff_and(c, sum_vars["JK"][q - 1], sum_vars["JK"][q])
        consecutive.append(c)
        cnf.add(d, c)

    if lex_symmetry and nj == nk:
        # If K also contains zero, choose the representative J >=lex K.
        # With K0=false the earlier J0 normalization already fixes orientation.
        k0 = membership["K"][0]
        prefix = None  # positions before p are equal; empty prefix is true.
        for p in range(1, m):
            if prefix is None:
                cnf.add(-k0, membership["J"][p], -membership["K"][p])
            else:
                cnf.add(
                    -k0,
                    -prefix,
                    membership["J"][p],
                    -membership["K"][p],
                )
            same = cnf.var(f"lex.same.{p}")
            cnf.iff_equal_bits(same, membership["J"][p], membership["K"][p])
            if prefix is None:
                prefix = same
            else:
                new_prefix = cnf.var(f"lex.prefix.{p}")
                cnf.iff_and(new_prefix, prefix, same)
                prefix = new_prefix

    cut_bounds: dict[str, list[int]] = {}
    extremal_cuts: list[str] = []
    if capacity_cuts:
        # A family with a,b elements has at most a*b distinct pair sums.
        # A set of at most nj*nk occupied JK sums has at most nj*nk-1 adjacent
        # pairs.  These are redundant globally but substantially strengthen UP.
        d_lower = max(0, m - (nj * nk - 1))
        c_lower = max(0, m - ni * (nj + nk))
        bounds = {
            "sum_IJ": (max(0, d_lower - ni * nk), min(m, ni * nj)),
            "sum_IK": (max(0, d_lower - ni * nj), min(m, ni * nk)),
            "sum_JK": (c_lower + 1 if c_lower else 0, min(m, nj * nk)),
            "direct": (d_lower, min(m, ni * (nj + nk))),
            "consecutive": (c_lower, min(m, nj * nk - 1)),
        }
        vectors = {
            "sum_IJ": sum_vars["IJ"],
            "sum_IK": sum_vars["IK"],
            "sum_JK": sum_vars["JK"],
            "direct": direct,
            "consecutive": consecutive,
        }
        for tag, (lo, hi) in bounds.items():
            cut_bounds[tag] = [lo, hi]
            cnf.range_count(vectors[tag], lo, hi, f"cut_{tag}")

        pair_capacities = {"IJ": ni * nj, "IK": ni * nk, "JK": nj * nk}
        pair_families = {"IJ": ("I", "J"), "IK": ("I", "K"), "JK": ("J", "K")}
        for ab, capacity in pair_capacities.items():
            lo, hi = bounds[f"sum_{ab}"]
            if lo == hi == capacity:
                # Every selected pair must land below m and all its sums must
                # be distinct.  These clauses follow from exact cardinality,
                # but exposing them makes extremal cases dramatically easier.
                for q, witnesses in enumerate(witness_vars[ab]):
                    cnf.at_most_one(witnesses, f"pairs_{ab}_{q}")
                left, right = pair_families[ab]
                for a in range(m):
                    for b in range(m - a, m):
                        cnf.add(-membership[left][a], -membership[right][b])
                extremal_cuts.append(f"{ab} pair sums all in-range and distinct")

        if bounds["direct"][0] == bounds["sum_IJ"][1] + bounds["sum_IK"][1]:
            for q in range(m):
                cnf.add(-sum_vars["IJ"][q], -sum_vars["IK"][q])
            extremal_cuts.append("IJ and IK sumsets disjoint")
        if bounds["direct"][1] + bounds["consecutive"][1] == m:
            for q in range(m):
                cnf.add(-direct[q], -consecutive[q])
            extremal_cuts.append("direct and consecutive coverage disjoint")
        if (
            bounds["sum_JK"][0] == bounds["sum_JK"][1]
            and bounds["consecutive"][0]
            == bounds["consecutive"][1]
            == bounds["sum_JK"][0] - 1
        ):
            cnf.convex_bits(sum_vars["JK"], "sum_JK")
            extremal_cuts.append("JK sumset is one interval")

    if fixed is not None:
        chosen = {key: set(fixed[key]) for key in ("I", "J", "K")}
        for family in ("I", "J", "K"):
            for p, var in enumerate(membership[family]):
                cnf.add(var if p in chosen[family] else -var)
    for family, position, value in units:
        if family not in membership or not 0 <= position < m:
            raise ValueError(f"invalid unit coordinate {family}:{position}={value}")
        cnf.add(membership[family][position] if value else -membership[family][position])

    metadata: dict[str, object] = {
        "ell": ell,
        "m": m,
        "counts": list(counts),
        "normalization": (
            ["0 in I", "0 in J (after J/K exchange; equal J,K counts)"]
            if nj == nk
            else ["0 in I", "0 in J or 0 in K (forced by q=0)"]
        ),
        "k0_case": k0_case,
        "lex_symmetry": lex_symmetry and nj == nk,
        "capacity_cuts": capacity_cuts,
        "cut_bounds": cut_bounds,
        "extremal_cuts": extremal_cuts,
        "extra_units": [f"{family}:{position}={value}" for family, position, value in units],
        "membership_variables": membership,
        "variables": cnf.nvars,
        "clauses": len(cnf.clauses),
    }
    return cnf, metadata


def load_fixed(path: Path, counts: tuple[int, int, int]) -> dict[str, list[int]]:
    fixed = json.loads(path.read_text())
    for key, count in zip(("I", "J", "K"), counts):
        if key not in fixed or len(fixed[key]) != count:
            raise ValueError(f"fixed certificate has wrong {key} cardinality")
    # Apply the same sound J/K normalization as the CNF.
    if 0 not in fixed["J"] and 0 in fixed["K"] and counts[1] == counts[2]:
        fixed["J"], fixed["K"] = fixed["K"], fixed["J"]
    return fixed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ell", type=int, required=True)
    parser.add_argument("--m", type=int, required=True)
    parser.add_argument("--counts", type=int, nargs=3, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--metadata", type=Path)
    parser.add_argument("--no-capacity-cuts", action="store_true")
    parser.add_argument("--no-lex-symmetry", action="store_true")
    parser.add_argument("--k0-case", type=int, choices=(0, 1))
    parser.add_argument("--fix-certificate", type=Path)
    parser.add_argument(
        "--unit",
        action="append",
        default=[],
        metavar="FAMILY:POSITION=BIT",
        help="add a membership unit, e.g. --unit I:1=0",
    )
    args = parser.parse_args()

    counts = tuple(args.counts)
    fixed = load_fixed(args.fix_certificate, counts) if args.fix_certificate else None
    units: list[tuple[str, int, int]] = []
    for raw in args.unit:
        try:
            left, raw_value = raw.split("=", 1)
            family, raw_position = left.split(":", 1)
            value = int(raw_value)
            if value not in (0, 1):
                raise ValueError
            units.append((family, int(raw_position), value))
        except ValueError as exc:
            raise SystemExit(f"invalid --unit {raw!r}; expected FAMILY:POSITION=BIT") from exc
    cnf, metadata = build(
        args.ell,
        args.m,
        counts,
        not args.no_capacity_cuts,
        not args.no_lex_symmetry,
        args.k0_case,
        fixed,
        units,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as out:
        out.write(f"p cnf {cnf.nvars} {len(cnf.clauses)}\n")
        for clause in cnf.clauses:
            out.write(" ".join(map(str, clause)) + " 0\n")
    digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
    metadata["cnf_sha256"] = digest
    metadata_path = args.metadata or args.output.with_suffix(".json")
    metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    print(json.dumps(metadata, sort_keys=True))


if __name__ == "__main__":
    main()
