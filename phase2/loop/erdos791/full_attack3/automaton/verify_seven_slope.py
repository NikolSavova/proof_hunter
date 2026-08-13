#!/usr/bin/env python3
"""Independent symbolic/enumerative verifier for the seven-slope tiles."""

from __future__ import annotations

import argparse
import json

from seven_slope_tiles import (
    PHASE_RADIUS,
    SLOPES,
    admissible_scale,
    analytic_audit,
    tile,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--t", type=int, default=421)
    parser.add_argument("--skip-enumeration", action="store_true")
    args = parser.parse_args()
    t = args.t
    if not admissible_scale(t):
        raise SystemExit("scale must satisfy the stated coprimality and size hypotheses")
    B = t * t
    rows = analytic_audit(t)
    symbolic_pass = all(
        row.get("divides_ab")
        and row.get("required_radius", PHASE_RADIUS + 1) <= PHASE_RADIUS
        and row.get("kernel_p") == B
        and row.get("kernel_q") == B
        and row.get("determinant") == B
        and row.get("bounds_fit")
        for row in rows
    )
    tiles = {a: tile(t, a) for a in SLOPES}
    expected_sizes = {
        a: t if a == 0 else t + 2 * PHASE_RADIUS for a in SLOPES
    }
    size_pass = all(len(tiles[a]) == expected_sizes[a] for a in SLOPES)
    direct = []
    if not args.skip_enumeration:
        for index, a in enumerate(SLOPES):
            for b in SLOPES[index + 1 :]:
                residues = {(x + y) % B for x in tiles[a] for y in tiles[b]}
                direct.append(
                    {
                        "a": a,
                        "b": b,
                        "covered_residues": len(residues),
                        "pass": len(residues) == B,
                    }
                )
    direct_pass = all(row["pass"] for row in direct)
    result = {
        "status": "PASS" if symbolic_pass and size_pass and direct_pass else "FAIL",
        "t": t,
        "B": B,
        "slopes": SLOPES,
        "phase_radius": PHASE_RADIUS,
        "tile_sizes": {str(a): len(tiles[a]) for a in SLOPES},
        "symbolic_pass": symbolic_pass,
        "size_pass": size_pass,
        "analytic_pairs": rows,
        "enumerative_pairs": direct,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
