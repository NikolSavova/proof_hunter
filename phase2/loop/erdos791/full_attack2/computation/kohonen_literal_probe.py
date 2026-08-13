#!/usr/bin/env python3
"""Literal small-t probe for the Kohonen three-tile macro certificate.

The natural type-dependent expansion has 42t+8 roles on 42t+7 distinct
coordinates.  For t=2 this script also asks the exact fixed-coordinate model
whether all 91 coordinates can be partitioned into three roles with no
duplication.  A timeout remains UNKNOWN and is reported as such.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from phased_role_model import ROLES, phased_coverage, prefix_length, solve


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE.parents[1] / "kohonen_42_510.json"


def expand(raw: dict[str, list[int]], t: int) -> dict[str, set[int]]:
    block = t * t
    elementary = {
        "I": tuple(range(t + 1)),
        "J": tuple(i * t for i in range(t)),
        "K": tuple(i * (t + 1) for i in range(t)),
    }
    return {
        name: {block * q + x for q in raw[name] for x in elementary[name]}
        for name in ("I", "J", "K")
    } | {"L0": set(), "L1": set()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--t", type=int, default=2)
    parser.add_argument("--seconds", type=float, default=120)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raw = json.loads(args.certificate.read_text())
    placement = expand(raw, args.t)
    coordinates = tuple(sorted(set().union(*placement.values())))
    role_cost = sum(len(placement[name]) for name in ROLES)
    target_n = 510 * args.t * args.t - 1
    natural_prefix = prefix_length(phased_coverage(placement))
    no_duplication = solve(
        coordinates,
        target_n,
        args.seconds,
        8,
        791_422,
        fixed_cost=len(coordinates),
        allowed_roles=("I", "J", "K"),
    )
    result = {
        "status": "PASS",
        "meaning": (
            "the natural placement is independently decoded; the exact "
            "no-duplication question is separate and may be UNKNOWN"
        ),
        "t": args.t,
        "target_n": target_n,
        "coordinate_size": len(coordinates),
        "natural_role_cost": role_cost,
        "natural_role_defect": role_cost - len(coordinates),
        "natural_verified_prefix": natural_prefix,
        "natural_placement": {name: sorted(placement[name]) for name in ROLES},
        "fixed_cost_equal_coordinate_size_test": no_duplication,
    }
    if natural_prefix <= target_n or role_cost != len(coordinates) + 1:
        result["status"] = "FAIL"
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "status": result["status"],
                "coordinate_size": len(coordinates),
                "natural_role_cost": role_cost,
                "natural_verified_prefix": natural_prefix,
                "no_duplication_status": no_duplication["status"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
