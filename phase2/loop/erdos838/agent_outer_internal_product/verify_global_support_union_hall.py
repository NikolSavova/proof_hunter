#!/usr/bin/env python3
"""Exact audit for GLOBAL_SUPPORT_UNION_HALL_CONSOLIDATION.md."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations, product
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent


def cross(a: tuple[Q, Q], b: tuple[Q, Q], c: tuple[Q, Q]) -> Q:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def strict_hull(points: tuple[tuple[Q, Q], ...]) -> tuple[tuple[Q, Q], ...]:
    ordered = sorted(set(points))
    if len(ordered) <= 2:
        return tuple(ordered)
    lower: list[tuple[Q, Q]] = []
    upper: list[tuple[Q, Q]] = []
    for p in ordered:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(ordered):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return tuple(lower[:-1] + upper[:-1])


def convex(points: tuple[tuple[Q, Q], ...]) -> bool:
    return len(strict_hull(points)) == len(set(points))


def hall_and_singleton_audit() -> dict[str, object]:
    """Exhaust the Hall ratios and the explicit proportional routing."""
    supports = (
        frozenset((0, 1, 2)),
        frozenset((1, 2, 3)),
        frozenset((1, 3, 4)),
        frozenset((0, 3, 4)),
    )
    demands = (Q(3, 2), Q(5, 4), Q(7, 4), Q(9, 8))
    banks = []
    capacities = {}
    for support in supports:
        bank = {
            frozenset(face)
            for rank in range(1, len(support) + 1)
            for face in combinations(sorted(support), rank)
        }
        banks.append(bank)
        for face in bank:
            capacities[face] = Q(1, 2 ** len(face))

    hall_value = Q(0)
    hall_witness = None
    for mask in range(1, 1 << len(supports)):
        active = [i for i in range(len(supports)) if mask & (1 << i)]
        neighborhood = set().union(*(banks[i] for i in active))
        ratio = sum(demands[i] for i in active) / sum(
            capacities[f] for f in neighborhood
        )
        if ratio > hall_value:
            hall_value = ratio
            hall_witness = active

    z = [sum(capacities[f] for f in bank) for bank in banks]
    proportional_loads = {
        face: sum(
            demands[i] / z[i]
            for i, bank in enumerate(banks)
            if face in bank
        )
        for face in capacities
    }
    max_proportional = max(proportional_loads.values())
    max_singleton = max(
        load for face, load in proportional_loads.items() if len(face) == 1
    )
    assert max_proportional == max_singleton
    assert hall_value <= max_singleton
    for face, load in proportional_loads.items():
        assert load <= min(proportional_loads[frozenset((x,))] for x in face)

    return {
        "contexts": len(supports),
        "nonempty_outputs": len(capacities),
        "exact_Hall_ratio": str(hall_value),
        "Hall_witness_contexts": hall_witness,
        "proportional_max_load": str(max_proportional),
        "singleton_max_load": str(max_singleton),
        "empty_face_excluded": True,
    }


def common_prefix_double_count_audit() -> dict[str, object]:
    supports = (
        frozenset((0, 1, 2, 3)),
        frozenset((0, 1, 4, 5)),
        frozenset((0, 2, 4, 6)),
        frozenset((1, 3, 5, 6)),
        frozenset((2, 3, 4, 5)),
    )
    weights = (Q(1), Q(2), Q(3, 2), Q(5, 2), Q(7, 4))
    n = 7
    results = {}
    for t in (1, 2, 3):
        codegrees = {
            frozenset(face): sum(
                weights[i] for i, support in enumerate(supports)
                if set(face) <= support
            )
            for face in combinations(range(n), t)
        }
        best_face, best_weight = max(codegrees.items(), key=lambda item: item[1])
        lower = Q(comb(4, t), comb(n, t)) * sum(weights)
        assert best_weight >= lower
        # Exact double-count identity before taking the minimum rank layer.
        incidence_sum = sum(codegrees.values())
        assert incidence_sum == comb(4, t) * sum(weights)
        results[str(t)] = {
            "best_face": sorted(best_face),
            "best_weight": str(best_weight),
            "guaranteed_average": str(lower),
            "weighted_incidence_sum": str(incidence_sum),
        }
    return {"n": n, "uniform_support_rank": 4, "layers": results}


def prefix_factorization_audit() -> dict[str, object]:
    q = 7
    prefix_rank = 3
    boolean_count = 2 ** (q - prefix_rank)
    boolean_half = Q(1, 2**prefix_rank) * Q(3, 2) ** (q - prefix_rank)

    role_sizes = (2, 3, 1, 4, 2)
    occupied = {1, 3}
    partial_count = 1
    partial_half = Q(1, 2 ** len(occupied))
    for i, size in enumerate(role_sizes):
        if i not in occupied:
            partial_count *= 1 + size
            partial_half *= 1 + Q(size, 2)

    # Direct enumeration checks the two products.
    assert boolean_count == len(tuple(product((0, 1), repeat=q - prefix_rank)))
    direct_partial = tuple(
        product(*(range(size + 1) if i not in occupied else (0,)
                  for i, size in enumerate(role_sizes)))
    )
    assert len(direct_partial) == partial_count
    direct_half = sum(
        Q(1, 2 ** (len(occupied) + sum(value != 0 for value in word)))
        for word in direct_partial
    )
    assert direct_half == partial_half
    return {
        "boolean": {
            "support_rank": q,
            "prefix_rank": prefix_rank,
            "prefixed_outputs": boolean_count,
            "prefixed_half_weight": str(boolean_half),
        },
        "partial": {
            "role_sizes": list(role_sizes),
            "occupied_roles": sorted(occupied),
            "prefixed_outputs": partial_count,
            "prefixed_half_weight": str(partial_half),
        },
    }


def induced_bank_prefix_failure() -> dict[str, object]:
    a = (Q(0), Q(0))
    b = (Q(6), Q(0))
    c = (Q(0), Q(6))
    x = (Q(1), Q(1))
    assert convex((a,))
    assert convex((b, c, x))
    assert not convex((a, b, c, x))
    return {
        "prefix": "{a}",
        "completion_face": "{b,c,x}",
        "prefix_union_completion_is_convex": False,
        "circuit_type": "1+3",
    }


def synchronized_support_regression() -> dict[str, object]:
    q = 7
    h = 8
    k = 3
    epsilon = Q(1, 10_000_000)
    cap = tuple((Q(i), Q(i * i)) for i in range(q))
    outer = tuple(
        (
            Q(-2) - j * epsilon,
            Q(-100 * q * q) + (j * epsilon) ** 2 + j * epsilon**3,
        )
        for j in range(1, h + 1)
    )
    assert convex(cap)
    assert convex(outer)
    assert all(
        cross(*triple) != 0 for triple in combinations((*outer, *cap), 3)
    )
    bad = sum(
        not convex((endpoint, *triple))
        for endpoint in outer
        for triple in combinations(cap, 3)
    )
    assert bad == h * comb(q, 3)

    contexts = comb(h, k)
    bank_capacity = Q(3, 2) ** q - 1
    total_demand = Q(contexts, 2**k)
    exact_load = total_demand / bank_capacity
    outer_capacity = Q(3, 2) ** h
    assert total_demand <= outer_capacity

    # Every nonempty prefix is shared by every context, and the completion
    # support is the same set Q-I.
    common_prefix_checks = 0
    for t in range(1, q + 1):
        for prefix in combinations(range(q), t):
            assert len(set(range(q)) - set(prefix)) == q - t
            common_prefix_checks += 1
    assert common_prefix_checks == 2**q - 1

    return {
        "cap_rank": q,
        "outer_shield_rank": h,
        "source_context_rank": k,
        "contexts": contexts,
        "literal_total_demand": str(total_demand),
        "identical_nonempty_bank_capacity": str(bank_capacity),
        "exact_Hall_load": str(exact_load),
        "outer_shield_half_capacity": str(outer_capacity),
        "rooted_1_plus_3_circuits_checked": bad,
        "nonempty_common_prefixes_checked": common_prefix_checks,
        "completion_multiplicity_at_every_prefix": contexts,
        "outer_shield_pays_literal_demand": True,
    }


def main() -> None:
    certificate = {
        "description": "global nonempty support-bank Hall routing, common prefixes, and synchronized-support regression",
        "Hall_and_singleton_domination": hall_and_singleton_audit(),
        "common_prefix_double_count": common_prefix_double_count_audit(),
        "prefix_factorizations": prefix_factorization_audit(),
        "arbitrary_induced_bank_prefix_failure": induced_bank_prefix_failure(),
        "synchronized_planar_support_regression": synchronized_support_regression(),
        "claims": [
            "fractional Hall min-load is the maximum demand-to-union-capacity ratio",
            "after deleting the empty face proportional load in every hereditary bank is singleton-dominated",
            "weighted rank-t double counting retains a common nonempty prefix without square loss",
            "Boolean and one-per-role partial cubes factor exactly over a common prefix",
            "arbitrary induced face banks do not factor over even a singleton prefix",
            "identical Boolean completion supports give an exact scalable planar bounded-rank quadratic-mass regression",
            "the regression exposes a convex outer shield whose half-weight pays the literal source demand",
        ],
    }
    output = HERE / "global_support_union_hall_certificate.json"
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
