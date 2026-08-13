#!/usr/bin/env python3
"""Exact scalable bounded-defect expansion of Kohonen's typed certificate."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from triangle_predicate import coverage_bits
from typed_predicate import NAMES, prefix_length


HERE = Path(__file__).resolve().parent
DEFAULT = HERE.parents[1] / "kohonen_42_510.json"


def expand(p: dict[str, set[int]], t: int) -> dict[str, set[int]]:
    B = t * t
    elementary = {
        "I": set(range(t + 1)),
        "J": {i * t for i in range(t)},
        "K": {i * (t + 1) for i in range(t)},
        "L0": {i * (t - 1) for i in range(t + 1)},
        "L1": {1 + i * (t - 1) for i in range(t + 1)},
    }
    return {
        name: {B * q + x for q in p[name] for x in elementary[name]}
        for name in NAMES
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path, default=DEFAULT)
    parser.add_argument("--through", type=int, default=20)
    args = parser.parse_args()
    raw = json.loads(args.certificate.read_text())
    raw = raw.get("placement", raw)
    p = {name: set(raw.get(name, [])) for name in NAMES}
    rows = []
    for t in range(2, args.through + 1, 2):
        placement = expand(p, t)
        role_cost = sum(map(len, placement.values()))
        coordinates = set().union(*placement.values())
        claimed_m = 510 * t * t + t
        prefix = prefix_length(coverage_bits(placement, claimed_m + 2), claimed_m + 2)
        rows.append(
            {
                "t": t,
                "coordinate_size": len(coordinates),
                "expected_coordinate_size_42t_plus_7": 42 * t + 7,
                "role_cost": role_cost,
                "expected_role_cost_42t_plus_8": 42 * t + 8,
                "role_defect": role_cost - len(coordinates),
                "claimed_m_510t2_plus_t": claimed_m,
                "abstract_prefix": prefix,
                "pass": len(coordinates) == 42 * t + 7
                and role_cost == 42 * t + 8
                and prefix >= claimed_m,
            }
        )
    result = {
        "status": "PASS" if all(row["pass"] for row in rows) else "FAIL",
        "scope": f"all even t through {args.through}",
        "rows": rows,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
