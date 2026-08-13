#!/usr/bin/env python3
"""Audit how the canonical K7 transition graph changes with scale."""

from __future__ import annotations

import json

from seven_slope_tiles import SLOPES, admissible_scale, tile


SCALES = (61, 67, 71, 101, 127, 151, 181, 211, 241, 251, 271, 301, 331, 421)


def main() -> None:
    rows = []
    for t in SCALES:
        if not admissible_scale(t):
            continue
        B, Q = t * t, set(range(t * t))
        elementary = {a: tile(t, a) for a in SLOPES}
        footprints = {}
        for index, a in enumerate(SLOPES):
            for b in SLOPES[index + 1 :]:
                sums = {x + y for x in elementary[a] for y in elementary[b]}
                footprints[(a, b)] = (
                    Q & sums,
                    {x - B for x in sums if B <= x < 2 * B},
                )
        transitions = [
            (old, new)
            for old in footprints
            for new in footprints
            if footprints[old][1] | footprints[new][0] == Q
        ]
        rows.append(
            {
                "t": t,
                "number_transitions": len(transitions),
                "number_nonself_transitions": sum(old != new for old, new in transitions),
                "only_self_loops": all(old == new for old, new in transitions),
            }
        )
    print(json.dumps({"status": "PASS", "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
