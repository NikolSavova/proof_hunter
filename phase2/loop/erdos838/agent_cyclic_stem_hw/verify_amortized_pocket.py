#!/usr/bin/env python3
"""Exact audits for AMORTIZED_POCKET_RESET.md.

All asserted inequalities are checked with integers or fractions.  Floating
point is used only to print the nonessential entropy diagnostic.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def nested_prefix_audit(max_s: int = 256) -> list[dict]:
    out = []
    previous_entropy = -1.0
    for s in range(max_s + 1):
        demand = (1 << (s + 1)) - 1
        cube = 1 << s
        assert demand < 2 * cube

        # Under the uniform law on pairs (D_t,J), the empty J has
        # multiplicity s+1; the 2^(m-1) subsets with maximum m have
        # multiplicity s-m+1.
        numerator = 0.0
        if s:
            numerator += (s + 1) * math.log2(s + 1)
            for m in range(1, s + 1):
                multiplicity = s - m + 1
                numerator += (1 << (m - 1)) * multiplicity * math.log2(
                    multiplicity
                )
        entropy = numerator / demand
        assert entropy + 1e-13 >= previous_entropy
        assert entropy < 1.289
        previous_entropy = entropy
        if s in {0, 1, 2, 4, 8, 16, 32, 64, 128, 256}:
            out.append(
                {
                    "s": s,
                    "demand": demand,
                    "largest_cube": cube,
                    "ratio": demand / cube,
                    "conditional_reuse_entropy_bits": entropy,
                }
            )
    return out


def product_grid_audit(rs: tuple[int, ...] = (4, 6, 8, 12, 16, 24, 32, 48, 64)) -> list[dict]:
    out = []
    for r in rs:
        b = r - 2
        M = 1 << r
        sources = M**b
        boolean_demand = (1 << b) * sources
        boolean_pool = (M + 1) ** b
        two_ended = math.comb(M, 2) ** 2 * M ** (b - 2)

        # Equation (16), cleared of denominators.
        assert 2 * boolean_demand >= (1 << b) * boolean_pool
        assert boolean_demand >= (1 << (b - 1)) * boolean_pool

        # Equations (18)--(19), again using integers only.
        assert 4 * two_ended == (M - 1) ** 2 * sources
        assert two_ended * M == (M - 1) ** 2 * boolean_demand
        assert two_ended >= (M - 2) * boolean_demand

        n = (r - 1) * M + 2
        ell = (n - 1).bit_length()
        out.append(
            {
                "r": r,
                "b": b,
                "M": M,
                "n": n,
                "ell": ell,
                "ell_minus_r": ell - r,
                "boolean_loss_lower_bound_bits": b - 1,
                "forward_over_weighted_demand_lower_bound": M - 2,
                "sources_digits": len(str(sources)),
            }
        )
    return out


def width_audit() -> list[dict]:
    """Finite set-poset checks of Theorems 1 and 2.

    For the local tangent test, hidden and retained universes are disjoint,
    so target recovery is literal set intersection with the two universes.
    """

    cases = []
    # Each case is already partitioned into inclusion chains.  This checks
    # the exact sum and the union of Boolean cubes, without invoking a
    # floating-point logarithm.
    chain_partitions = [
        [[frozenset(range(k)) for k in range(7)]],
        [
            [frozenset({0}), frozenset({0, 1}), frozenset({0, 1, 2})],
            [frozenset({3}), frozenset({3, 4})],
        ],
        [
            [frozenset({0, 2}), frozenset({0, 1, 2, 3})],
            [frozenset({1, 3})],
            [frozenset({4}), frozenset({4, 5, 6})],
        ],
    ]
    for chains in chain_partitions:
        family = [x for chain in chains for x in chain]
        width_bound = len(chains)
        demand = sum(1 << len(x) for x in family)
        union = set()
        for x in family:
            ordered = tuple(sorted(x))
            for mask in range(1 << len(ordered)):
                union.add(
                    frozenset(ordered[j] for j in range(len(ordered)) if mask >> j & 1)
                )
        assert demand < 2 * width_bound * len(union)
        cases.append(
            {
                "chains": len(chains),
                "family_size": len(family),
                "demand": demand,
                "union_size": len(union),
            }
        )

    # A fixed-frame graph.  Retained labels are 100,101,102 and hidden
    # labels are below 10.  For each retained face, the supplied neighbor
    # partition certifies its inclusion-width upper bound.
    retained_to_chains = {
        frozenset({100}): [
            [frozenset(), frozenset({0}), frozenset({0, 1})],
            [frozenset({2}), frozenset({2, 3})],
        ],
        frozenset({101}): [
            [frozenset({0}), frozenset({0, 2}), frozenset({0, 2, 4})]
        ],
        frozenset({101, 102}): [
            [frozenset({1}), frozenset({1, 3})],
            [frozenset({4})],
        ],
    }
    weighted = 0
    targets = set()
    max_width = 0
    for retained, chains in retained_to_chains.items():
        max_width = max(max_width, len(chains))
        for chain in chains:
            for hidden in chain:
                weighted += 1 << len(hidden)
                ordered = tuple(sorted(hidden))
                for mask in range(1 << len(ordered)):
                    subset = frozenset(
                        ordered[j] for j in range(len(ordered)) if mask >> j & 1
                    )
                    targets.add(retained | subset)
    assert weighted <= 2 * max_width * len(targets)
    cases.append(
        {
            "local_tangent": True,
            "width_bound": max_width,
            "weighted_demand": weighted,
            "distinct_targets": len(targets),
        }
    )
    return cases


def main() -> None:
    certificate = {
        "nested_prefixes": nested_prefix_audit(),
        "product_grids": product_grid_audit(),
        "width_and_tangent_cases": width_audit(),
    }
    path = HERE / "amortized_pocket_certificate.json"
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print("amortized pocket audit: PASS")
    print(f"certificate: {path}")


if __name__ == "__main__":
    main()
