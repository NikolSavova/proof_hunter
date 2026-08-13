#!/usr/bin/env python3
"""Exhaust translations of the projective triangle at small q."""

from __future__ import annotations

import argparse
import json

from projective_triangle import STATES, tiles


def transition_count(q: int, shifts: tuple[int, int, int]) -> int:
    B, p = tiles(q)
    Q = set(range(B))
    p = {
        name: {(x + shifts[index]) % B for x in p[name]}
        for index, name in enumerate(("X", "Y", "Z"))
    }
    f = {}
    for name, left, right in (("XY", "X", "Y"), ("YZ", "Y", "Z"), ("XZ", "X", "Z")):
        sums = {x + y for x in p[left] for y in p[right]}
        f[name] = (Q & sums, {x - B for x in sums if B <= x < 2 * B})
    return sum(f[old][1] | f[new][0] == Q for old in STATES for new in STATES)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, default=6)
    args = parser.parse_args()
    rows = []
    for q in range(3, args.through + 1):
        B, _ = tiles(q)
        best = -1
        witness = None
        for x in range(B):
            for y in range(B):
                for z in range(B):
                    count = transition_count(q, (x, y, z))
                    if count > best:
                        best, witness = count, (x, y, z)
        rows.append(
            {
                "q": q,
                "B": B,
                "translations_checked": B**3,
                "maximum_of_nine_transitions": best,
                "first_best_translation": witness,
            }
        )
    print(json.dumps({"status": "PASS", "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
