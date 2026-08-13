#!/usr/bin/env python3
"""Audit all ordered carry transitions in the seven-slope tile language."""

from __future__ import annotations

import json
import sys
from itertools import combinations
from pathlib import Path

AUTOMATON = Path(__file__).resolve().parents[1] / "automaton"
sys.path.insert(0, str(AUTOMATON))

from seven_slope_tiles import SLOPES, admissible_scale, tile  # noqa: E402


def audit(t: int) -> dict:
    if not admissible_scale(t):
        raise ValueError(f"inadmissible scale {t}")
    block = t * t
    full = (1 << block) - 1
    footprints = []
    for a, b in combinations(SLOPES, 2):
        lower = carry = 0
        for x in tile(t, a):
            for y in tile(t, b):
                total = x + y
                if total < block:
                    lower |= 1 << total
                else:
                    carry |= 1 << (total - block)
        assert lower | carry == full
        footprints.append(((a, b), lower, carry))

    rows = []
    residual_union = 0
    for old, _old_lower, old_carry in footprints:
        for new, new_lower, _new_carry in footprints:
            residual = full & ~(old_carry | new_lower)
            residual_union |= residual
            rows.append((residual.bit_count(), old, new))
    rows.sort()
    return {
        "t": t,
        "block": block,
        "states": len(footprints),
        "ordered_transitions": len(rows),
        "legal_transitions": sum(count == 0 for count, _, _ in rows),
        "minimum_holes": rows[0][0],
        "median_holes": rows[len(rows) // 2][0],
        "maximum_holes": rows[-1][0],
        "maximum_hole_transition": [list(rows[-1][1]), list(rows[-1][2])],
        "residual_union_size": residual_union.bit_count(),
    }


def main() -> None:
    result = {
        "status": "PASS",
        "scope": "finite transition diagnostics, not an asymptotic theorem",
        "rows": [audit(t) for t in (101, 151, 251)],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
