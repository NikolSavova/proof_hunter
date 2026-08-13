#!/usr/bin/env python3
"""Exact footprint verifier for the projective modular triangle."""

from __future__ import annotations

import argparse
import json

from projective_triangle import STATES, footprints, tiles, transitions


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, default=100)
    args = parser.parse_args()
    rows = []
    for q in range(3, args.through + 1):
        B, p = tiles(q)
        _, f = footprints(q)
        Q = set(range(B))
        rows.append(
            {
                "q": q,
                "B": B,
                "tile_sizes": {name: len(values) for name, values in p.items()},
                "footprints": {
                    name: {
                        "lower_size": len(f[name][0]),
                        "upper_size": len(f[name][1]),
                        "modular_union_size": len(f[name][0] | f[name][1]),
                    }
                    for name in STATES
                },
                "XY_exact_lower": f["XY"][0] == Q and not f["XY"][1],
                "YZ_exact_lower": f["YZ"][0] == Q and not f["YZ"][1],
                "XZ_modular": f["XZ"][0] | f["XZ"][1] == Q,
                "transition_graph": transitions(q),
                "transition_expected": transitions(q)
                == (
                    {name: list(STATES) for name in STATES}
                    if q == 3
                    else {"XY": ["XY", "YZ"], "YZ": ["XY", "YZ"], "XZ": list(STATES)}
                ),
            }
        )
    passed = all(
        row["XY_exact_lower"]
        and row["YZ_exact_lower"]
        and row["XZ_modular"]
        and row["transition_expected"]
        for row in rows
    )
    print(json.dumps({"status": "PASS" if passed else "FAIL", "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
