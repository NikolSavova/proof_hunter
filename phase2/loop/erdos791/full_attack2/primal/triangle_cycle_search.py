#!/usr/bin/env python3
"""Search periodic carry-triangle certificates in cyclic macro groups.

This search is deliberately at the macro/carry layer.  It asks for J,K,L
subsets of Z_n such that every residue q has one of the two exact triangle
witness orientations:

    q in J+K and J+L, q-1 in K+L; or
    q-1 in J+K and J+L, q in K+L.

The output measures role cost |J|+|K|+|L|.  Cyclic wraparound is not itself an
integer initial-interval certificate; a separate lift lemma would be required.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


def sums_mod(A: set[int], B: set[int], n: int) -> set[int]:
    return {(a + b) % n for a in A for b in B}


def covers(J: set[int], K: set[int], L: set[int], n: int) -> bool:
    jk = sums_mod(J, K, n)
    jl = sums_mod(J, L, n)
    kl = sums_mod(K, L, n)
    return all(
        (q in jk and q in jl and (q - 1) % n in kl)
        or ((q - 1) % n in jk and (q - 1) % n in jl and q in kl)
        for q in range(n)
    )


def search(n: int) -> dict[str, object]:
    universe = range(n)
    subsets = [set(c) for size in range(1, n + 1) for c in itertools.combinations(universe, size)]
    subsets.sort(key=len)
    best = None
    checked = 0
    for J in subsets:
        for K in subsets:
            if best and len(J) + len(K) + 1 >= best[0]:
                break
            for L in subsets:
                cost = len(J) + len(K) + len(L)
                if best and cost >= best[0]:
                    break
                checked += 1
                if covers(J, K, L, n):
                    best = (cost, J, K, L)
                    break
    if best is None:
        raise RuntimeError("no cyclic certificate")
    cost, J, K, L = best
    return {
        "n": n,
        "minimum_role_cost": cost,
        "density_n_over_cost_squared": n / (cost * cost),
        "J": sorted(J),
        "K": sorted(K),
        "L": sorted(L),
        "triples_checked": checked,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, default=8)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rows = [search(n) for n in range(2, args.through + 1)]
    result = {
        "status": "PASS",
        "scope": "Exhaustive cyclic macro triangle search; not an integer lift.",
        "rows": rows,
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
