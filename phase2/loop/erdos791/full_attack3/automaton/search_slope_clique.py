#!/usr/bin/env python3
"""Exhaust bounded integer slopes for seven pairwise index-B lattices."""

from __future__ import annotations

import argparse
import json
from itertools import combinations

from seven_slope_tiles import pair_parameters


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--maximum", type=int, default=60)
    args = parser.parse_args()
    values = list(range(args.maximum + 1))
    adjacency = {
        a: {
            b
            for b in values
            if b > a and pair_parameters(a, b)["divides_ab"]
        }
        for a in values
    }
    best: tuple[int, tuple[int, ...]] | None = None
    number = 0

    def visit(current: list[int], candidates: list[int]) -> None:
        nonlocal best, number
        if len(current) == 7:
            number += 1
            radius = max(
                int(pair_parameters(a, b)["required_radius"])
                for a, b in combinations(current, 2)
            )
            answer = (radius, tuple(current))
            if best is None or answer < best:
                best = answer
            return
        if len(current) + len(candidates) < 7:
            return
        while candidates:
            value = candidates.pop(0)
            visit(
                current + [value],
                [other for other in candidates if other in adjacency[value]],
            )

    visit([], values[:])
    print(
        json.dumps(
            {
                "status": "PASS" if best else "NO_CLIQUE",
                "scope": f"all seven-subsets of integer slopes [0,{args.maximum}]",
                "number_of_seven_cliques": number,
                "minimum_phase_radius": None if best is None else best[0],
                "lexicographically_first_minimizer": None if best is None else best[1],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
