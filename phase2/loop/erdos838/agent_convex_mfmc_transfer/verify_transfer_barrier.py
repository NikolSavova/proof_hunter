#!/usr/bin/env python3
"""Exact audit for the Hachimori--Nakamura transfer barrier.

The apex/concave-chain configuration is the exponential inverse-fibre family
from the visible-flip attack.  This script checks that every fixed-root stem
clutter is nevertheless Mengerian: for an internal chain root it is a cone
over a complete bipartite graph, and for every other root it is empty.

Thus absence of the HN Pentagon obstruction does not control the weighted
history fibres required by the Erdos 838 half-weight flow.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations


Point = tuple[int, int]


def orient(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def strictly_in_triangle(x: Point, tri: tuple[Point, Point, Point]) -> bool:
    a, b, c = tri
    s = [orient(a, b, x), orient(b, c, x), orient(c, a, x)]
    return all(v > 0 for v in s) or all(v < 0 for v in s)


def configuration(chain_points: int) -> tuple[list[Point], int]:
    """Return q_0,...,q_(N-1),p and the apex index."""
    n = chain_points
    ell = n - 1
    points = [(i, i * (ell - i)) for i in range(n)]
    points.append((-1, n * n))
    return points, n


def rooted_stems(points: list[Point], root: int) -> list[tuple[int, int, int]]:
    others = [i for i in range(len(points)) if i != root]
    return [
        tri
        for tri in combinations(others, 3)
        if strictly_in_triangle(points[root], tuple(points[i] for i in tri))
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chain-points", type=int, default=9)
    args = parser.parse_args()
    n = args.chain_points
    assert n >= 4
    points, apex = configuration(n)

    assert all(
        orient(points[i], points[j], points[k]) != 0
        for i, j, k in combinations(range(len(points)), 3)
    )

    stem_counts: dict[str, int] = {}
    mfmc_formula: dict[str, str] = {}
    for root in range(len(points)):
        actual = set(rooted_stems(points, root))
        if root == apex or root in (0, n - 1):
            expected: set[tuple[int, int, int]] = set()
        else:
            expected = {
                tuple(sorted((apex, left, right)))
                for left in range(root)
                for right in range(root + 1, n)
            }
        assert actual == expected, (root, actual ^ expected)
        stem_counts[str(root)] = len(actual)
        if actual:
            assert all(apex in edge for edge in actual)
            mfmc_formula[str(root)] = (
                "tau_w=nu_w=min(w_apex,sum_{i<root}w_i,"
                "sum_{i>root}w_i)"
            )

    internal = n - 2
    total_source_mass = Fraction((3**internal) - (2**internal), 4 * 2**internal)
    # This is 1/4*((3/2)^m-1), written exactly.
    assert total_source_mass == Fraction(1, 4) * (
        Fraction(3, 2) ** internal - 1
    )
    possible_rooted_circuit_states = sum(stem_counts.values())
    pigeonhole_load = total_source_mass / possible_rooted_circuit_states

    root_masses = {}
    for root in range(1, n - 1):
        mass = Fraction(1, 8) * Fraction(3, 2) ** (internal - 1)
        # Sum 2^{-|A_C|} over C containing this root.
        explicit = sum(
            Fraction(1, 2 ** (2 + len(chosen)))
            for size in range(1, internal + 1)
            for chosen in combinations(range(1, n - 1), size)
            if root in chosen
        )
        assert mass == explicit
        root_masses[str(root)] = str(mass)

    out = {
        "chain_points": n,
        "total_points": len(points),
        "general_position": True,
        "rooted_stem_counts": stem_counts,
        "fixed_root_mfmc_formula": mfmc_formula,
        "all_fixed_root_clutters_mfmc": True,
        "hidden_subset_count": 2**internal - 1,
        "hidden_subset_half_weight_mass": str(total_source_mass),
        "hidden_subset_half_weight_mass_float": float(total_source_mass),
        "root_conditioned_half_weight_masses": root_masses,
        "possible_single_rooted_circuit_states": possible_rooted_circuit_states,
        "pigeonhole_load_if_only_one_rooted_circuit_is_retained": str(
            pigeonhole_load
        ),
        "asymptotics": {
            "source_mass": "Theta((3/2)^(N-2))",
            "single_rooted_circuit_states": "Theta(N^3)",
            "minimum_state_congestion": "Omega((3/2)^N/N^3)",
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
