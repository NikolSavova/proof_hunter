#!/usr/bin/env python3
"""Exact audits for the most natural reflected-diagonal tile variants.

The first table measures the unavoidable macroscopic hole left when unshifted
S+T tiles are placed at two consecutive t^2 blocks.  The exact observed value
is floor((t-1)^2/4), so one phase is asymptotically insufficient.

The second audit exhausts all pointwise perturbations

    T_e = {j(t-1)+e_j : 0 <= j <= t}, e_j in {0,1}, e_0=0,

through a requested t.  It asks whether a perturbation that preserves all t
residue classes modulo t (the basic H+T transversality condition) improves the
cyclic S+T footprint.  It does not, through the recorded finite range.
"""

from __future__ import annotations

import argparse
import itertools
import json


def audit(t: int) -> dict[str, object]:
    S = {i * (t + 1) for i in range(t)}
    T = {j * (t - 1) for j in range(t + 1)}
    D = {x + y for x in S for y in T}
    Q = set(range(t * t, 2 * t * t))
    unshifted_missing = len(Q - (D | {x + t * t for x in D}))
    base_cyclic = len({x % (t * t) for x in D})
    best_cyclic = -1
    best_eps: tuple[int, ...] | None = None
    admissible = 0
    for tail in itertools.product((0, 1), repeat=t):
        eps = (0, *tail)
        perturbed = {j * (t - 1) + eps[j] for j in range(t + 1)}
        if len({x % t for x in perturbed}) < t:
            continue
        admissible += 1
        footprint = len({(x + y) % (t * t) for x in S for y in perturbed})
        if footprint > best_cyclic:
            best_cyclic, best_eps = footprint, eps
    return {
        "t": t,
        "unshifted_two_block_missing": unshifted_missing,
        "floor_(t-1)^2_over_4": (t - 1) ** 2 // 4,
        "base_cyclic_footprint": base_cyclic,
        "admissible_01_perturbations": admissible,
        "best_admissible_cyclic_footprint": best_cyclic,
        "best_epsilon": list(best_eps) if best_eps is not None else None,
        "strict_improvement": best_cyclic > base_cyclic,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, default=18)
    args = parser.parse_args()
    rows = [audit(t) for t in range(2, args.through + 1)]
    print(
        json.dumps(
            {
                "through": args.through,
                "hole_formula_pass": all(
                    row["unshifted_two_block_missing"] == row["floor_(t-1)^2_over_4"]
                    for row in rows
                ),
                "no_admissible_01_improvement": not any(row["strict_improvement"] for row in rows),
                "rows": rows,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
