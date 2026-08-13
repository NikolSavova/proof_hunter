#!/usr/bin/env python3
"""Symbolic and bounded literal audit of the general K_r tile family."""

from __future__ import annotations

import argparse
import json
from math import lcm

from unbounded_cliques import (
    admissible_scale,
    analytic_audit,
    phase_radius,
    slope_family,
    tile,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through-r", type=int, default=8)
    parser.add_argument("--literal-through-r", type=int, default=5)
    args = parser.parse_args()
    rows = []
    for r in range(2, args.through_r + 1):
        D, C = slope_family(r), phase_radius(r)
        t = lcm(*D[1:]) + 1
        while not admissible_scale(t, r):
            t += lcm(*D[1:])
        B = t * t
        algebra = analytic_audit(t, r)
        symbolic = all(
            row["kernel_p"] == B
            and row["kernel_q"] == B
            and row["determinant"] == B
            and row["bounds_fit"]
            for row in algebra
        )
        literal = None
        if r <= args.literal_through_r:
            T = {a: tile(t, a, C) for a in D}
            literal = all(
                len({(x + y) % B for x in T[a] for y in T[b]}) == B
                for index, a in enumerate(D)
                for b in D[index + 1 :]
            )
        rows.append(
            {
                "r": r,
                "M": D[1],
                "slopes": D,
                "phase_radius": C,
                "audit_scale": t,
                "number_pair_edges": r * (r - 1) // 2,
                "symbolic_pass": symbolic,
                "literal_pass": literal,
            }
        )
    passed = all(row["symbolic_pass"] and row["literal_pass"] is not False for row in rows)
    print(json.dumps({"status": "PASS" if passed else "FAIL", "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
