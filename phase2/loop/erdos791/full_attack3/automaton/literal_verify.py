#!/usr/bin/env python3
"""Literal integer verifier for seven-slope point-footprint certificates."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from automaton_predicate import BOOTSTRAP, ROLE_NAMES, coverage, prefix_length
from seven_slope_tiles import SLOPES, admissible_scale, tile


def load(path: Path) -> tuple[dict[str, set[int]], int]:
    raw = json.loads(path.read_text())
    p = raw.get("placement", raw)
    placement = {name: set(p.get(name, [])) for name in ROLE_NAMES}
    if any(any(type(x) is not int or x < 0 for x in values) for values in placement.values()):
        raise ValueError("placements must be nonnegative integers")
    m = raw.get("m")
    if type(m) is not int or m <= 0:
        raise ValueError("certificate must have positive integer m")
    return placement, m


def elementary(t: int) -> dict[str, set[int]]:
    B = t * t
    return {
        BOOTSTRAP: set(range(t + 1)),
        **{f"R{a}": tile(t, a) for a in SLOPES},
    }


def basis(placement: dict[str, set[int]], t: int) -> set[int]:
    B = t * t
    e = elementary(t)
    return {
        B * macro + x
        for name in ROLE_NAMES
        for macro in placement[name]
        for x in e[name]
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--t", type=int, nargs="*", default=[61, 67])
    args = parser.parse_args()
    placement, m = load(args.certificate)
    abstract = prefix_length(coverage(placement, m + 32))
    if abstract < m:
        raise ValueError(f"abstract prefix {abstract}<m={m}")
    checks = []
    for t in args.t:
        if not admissible_scale(t):
            raise ValueError(f"inadmissible t={t}")
        B = t * t
        A = basis(placement, t)
        sums = {x + y for x in A for y in A if x <= y}
        missing = next((x for x in range(m * B) if x not in sums), None)
        checks.append(
            {
                "t": t,
                "basis_size": len(A),
                "required_through": m * B - 1,
                "pass": missing is None,
                "first_missing": missing,
            }
        )
    result = {
        "status": "PASS" if all(row["pass"] for row in checks) else "FAIL",
        "role_cost": sum(map(len, placement.values())),
        "m": m,
        "abstract_prefix": abstract,
        "literal_checks": checks,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
