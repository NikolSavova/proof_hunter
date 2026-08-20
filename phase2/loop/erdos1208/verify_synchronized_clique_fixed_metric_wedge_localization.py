#!/usr/bin/env python3
"""Verify the synchronized-clique/fixed-metric-wedge localization theorem."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb

import verify_high_codegree_transverse_equal_area_rank_flat_barrier as rank_flat
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_high_codegree_replacement_completion import (
    add,
    subtract,
    tables,
)


Point = tuple[int, int]
Edge = tuple[int, int]
Wedge = tuple[int, Edge, Edge]


def determinant(left: Point, right: Point) -> int:
    return left[0] * right[1] - left[1] * right[0]


def source_profile(
    points: list[Point],
) -> tuple[Counter[int], tuple[int, ...], dict[tuple[Point, Point], int]]:
    """Compute K_2, retaining every ordered source pair and four translations."""

    k = len(points)
    edge_at_sum, distance_at_sum, anchor_at_difference = tables(points)
    fibres = clean_start_fibres(points)
    distance_values = set(distance_at_sum.values())
    target_gaps = {
        first - second
        for first in distance_values
        for second in distance_values
    }

    common: dict[tuple[Point, Point], list[Point]] = defaultdict(list)
    for translation, starts in fibres.items():
        for first in starts:
            for second in starts:
                if first == second:
                    continue
                source_gap = distance_at_sum[first] - distance_at_sum[second]
                if source_gap % 18 == 0 and -source_gap // 18 in target_gaps:
                    common[first, second].append(translation)

    K_2: Counter[int] = Counter()
    upper_profile: Counter[int] = Counter()
    B_by_pair: dict[tuple[Point, Point], int] = {}
    high_pairs = 0
    positive_pairs = 0
    one_role_bases = 0
    rich_bases = 0
    maximum_B = 0

    for pair, translations in common.items():
        first, second = pair
        codegree = len(translations)
        if codegree < k:
            continue
        high_pairs += 1

        anchor_edges = [set(anchor_at_difference[q]) for q in translations]
        first_edges = [set(edge_at_sum[add(first, q)]) for q in translations]
        second_edges = [set(edge_at_sum[add(second, q)]) for q in translations]

        def conflict_masks(edges: list[set[int]]) -> list[int]:
            return [
                sum(1 << j for j, other in enumerate(edges) if edge & other)
                for edge in edges
            ]

        anchor_conflicts = conflict_masks(anchor_edges)
        first_conflicts = conflict_masks(first_edges)
        second_conflicts = conflict_masks(second_edges)

        B_2 = 0
        pair_one_role = 0
        pair_rich = 0
        for left, right in combinations(range(codegree), 2):
            first_meets = bool(first_edges[left] & first_edges[right])
            second_meets = bool(second_edges[left] & second_edges[right])
            if first_meets == second_meets:
                continue
            pair_one_role += 1
            forbidden = (
                anchor_conflicts[left]
                | anchor_conflicts[right]
                | first_conflicts[left]
                | first_conflicts[right]
                | second_conflicts[left]
                | second_conflicts[right]
            )
            transverse = codegree - forbidden.bit_count()
            if 2 * transverse >= codegree:
                pair_rich += 1
                B_2 += comb(transverse, 2)

        # A c-edge simple graph has at most (k-2)c adjacent edge pairs.
        assert pair_one_role <= 2 * (k - 2) * codegree
        assert B_2 <= comb(codegree, 2) * pair_one_role
        assert B_2 < (k - 2) * codegree**3

        one_role_bases += pair_one_role
        rich_bases += pair_rich
        B_by_pair[pair] = B_2
        scalar = -(
            distance_at_sum[first] - distance_at_sum[second]
        ) // 18
        upper_profile[scalar] += comb(codegree, 2) * pair_one_role
        if B_2:
            positive_pairs += 1
            K_2[scalar] += B_2
            maximum_B = max(maximum_B, B_2)

    # Reversing the source order preserves B_2 and reverses the scalar.
    assert all(B == B_by_pair[(second, first)] for (first, second), B in B_by_pair.items())
    assert all(load == K_2[-scalar] for scalar, load in K_2.items())
    assert all(load <= upper_profile[scalar] for scalar, load in K_2.items())

    statistics = (
        high_pairs,
        positive_pairs,
        one_role_bases,
        rich_bases,
        len(K_2),
        sum(K_2.values()),
        maximum_B,
    )
    return K_2, statistics, B_by_pair


def fixed_wedge_localization(
    points: list[Point], K_2: Counter[int], cutoff: int
) -> tuple[int, Counter[Wedge], dict[Wedge, set[int]], int]:
    """Compute both sides of sum_r K_2(r)W_(r,L)=sum_w Phi_(2,L)(w)."""

    edge_at_sum, distance_at_sum, _ = tables(points)
    edge_at_distance = {
        distance: edge_at_sum[pair_sum]
        for pair_sum, distance in distance_at_sum.items()
    }

    def vector(edge: Edge) -> Point:
        first, second = edge
        return subtract(points[second], points[first])

    fixed_load: Counter[Wedge] = Counter()
    shift_sets: dict[Wedge, set[int]] = defaultdict(set)
    scalar_sum = 0
    wedge_sum = 0

    for scalar, load in K_2.items():
        eligible: list[Edge] = []
        for first_distance, first_edge in edge_at_distance.items():
            partner_edge = edge_at_distance.get(first_distance - scalar)
            if partner_edge is None:
                continue
            if abs(2 * determinant(vector(first_edge), vector(partner_edge))) <= cutoff:
                continue
            eligible.append(first_edge)

        endpoint_edges: dict[int, list[Edge]] = defaultdict(list)
        for edge in eligible:
            for endpoint in edge:
                endpoint_edges[endpoint].append(edge)

        W_r = 0
        for endpoint, incident in endpoint_edges.items():
            for first_edge, second_edge in combinations(incident, 2):
                ordered = tuple(sorted((first_edge, second_edge)))
                wedge: Wedge = (endpoint, ordered[0], ordered[1])
                # For fixed w and r, distinct distances make both partners unique.
                assert scalar not in shift_sets[wedge]
                shift_sets[wedge].add(scalar)
                fixed_load[wedge] += load
                W_r += 1
        scalar_sum += load * W_r
        wedge_sum += W_r

    assert scalar_sum == sum(fixed_load.values())
    assert all(
        fixed_load[wedge] == sum(K_2[scalar] for scalar in shifts)
        for wedge, shifts in shift_sets.items()
    )
    # Exact finite Cauchy check for (5.3), without floating point.
    assert all(
        fixed_load[wedge] ** 2
        <= len(shifts) * sum(K_2[scalar] ** 2 for scalar in shifts)
        for wedge, shifts in shift_sets.items()
    )
    return scalar_sum, fixed_load, shift_sets, wedge_sum


def verify_rank_flat_planted_pair() -> tuple[int, ...]:
    """Recompute B_2 and the two planted fixed-wedge charges exactly."""

    translations = list(rank_flat.SELECTED_Q)
    codegree = len(translations)
    anchor_edges = [set(rank_flat.template_anchor[q]) for q in translations]
    first_edges = [rank_flat.first_edges[q] for q in translations]
    second_edges = [rank_flat.second_edges[q] for q in translations]

    def conflict_masks(edges: list[set[int]]) -> list[int]:
        return [
            sum(1 << j for j, other in enumerate(edges) if edge & other)
            for edge in edges
        ]

    anchor_conflicts = conflict_masks(anchor_edges)
    first_conflicts = conflict_masks(first_edges)
    second_conflicts = conflict_masks(second_edges)

    one_role = 0
    rich = 0
    B_2 = 0
    expanded_four_translation_count = 0
    for left, right in combinations(range(codegree), 2):
        first_meets = bool(first_edges[left] & first_edges[right])
        second_meets = bool(second_edges[left] & second_edges[right])
        if first_meets == second_meets:
            continue
        one_role += 1
        forbidden = (
            anchor_conflicts[left]
            | anchor_conflicts[right]
            | first_conflicts[left]
            | first_conflicts[right]
            | second_conflicts[left]
            | second_conflicts[right]
        )
        transverse_indices = [
            index
            for index in range(codegree)
            if not (forbidden & (1 << index))
        ]
        transverse = len(transverse_indices)
        if 2 * transverse >= codegree:
            rich += 1
            B_2 += comb(transverse, 2)
            for first_pool, second_pool in combinations(transverse_indices, 2):
                # Literal four-fibre membership and disjoint base/pool roles.
                assert first_pool not in (left, right)
                assert second_pool not in (left, right)
                for index in (left, right, first_pool, second_pool):
                    q = rank_flat.new_q[translations[index]]
                    assert rank_flat.clean(q, rank_flat.source_s)
                    assert rank_flat.clean(q, rank_flat.source_t)
                expanded_four_translation_count += 1

    assert (one_role, rich, B_2, expanded_four_translation_count) == (
        183,
        77,
        27140,
        27140,
    )

    assert rank_flat.wedge_count(rank_flat.negative_representations) == 1
    assert rank_flat.wedge_count(rank_flat.positive_representations) == 1
    planted_pooled_mass = B_2 * (
        rank_flat.wedge_count(rank_flat.negative_representations)
        + rank_flat.wedge_count(rank_flat.positive_representations)
    )
    assert planted_pooled_mass == 54280
    assert Fraction(B_2, rank_flat.k**4) < Fraction(6, 1000)
    return one_role, rich, B_2, planted_pooled_mass


def main() -> None:
    points = transformed_parabola_43()
    k = len(points)
    N = comb(k, 2)
    cutoff = 20

    K_2, statistics, _ = source_profile(points)
    assert statistics == (
        7972,
        7972,
        2053352,
        1116236,
        7270,
        547712688,
        535281,
    ), statistics

    pooled_mass, fixed_load, shift_sets, metric_wedge_count = (
        fixed_wedge_localization(points, K_2, cutoff)
    )
    maximum_fixed = max(fixed_load.values())
    maximum_wedge = max(fixed_load, key=fixed_load.get)
    maximum_shifts = sorted(shift_sets[maximum_wedge])
    maximum_shift_loads = [K_2[scalar] for scalar in maximum_shifts]
    assert pooled_mass == 94435636
    assert maximum_fixed == 736977
    assert max(K_2.values()) == 657408
    assert maximum_shifts == [-50080, -5856]
    assert maximum_shift_loads == [149756, 587221]
    assert maximum_fixed > 9 * k**3
    assert maximum_fixed < Fraction(22, 100) * k**4
    assert Fraction(pooled_mass, N * k**5) < Fraction(8, 10000)
    assert fixed_load[maximum_wedge] == sum(
        K_2[scalar] for scalar in shift_sets[maximum_wedge]
    )

    rank_statistics = verify_rank_flat_planted_pair()
    print(
        "PASS",
        {
            "parabola_k": k,
            "cutoff": cutoff,
            "source_profile": statistics,
            "metric_wedge_occurrences": metric_wedge_count,
            "pooled_mass": pooled_mass,
            "fixed_wedge_support": len(fixed_load),
            "maximum_fixed_wedge": maximum_fixed,
            "maximum_fixed_wedge_shift_support": len(shift_sets[maximum_wedge]),
            "maximum_fixed_wedge_shifts": maximum_shifts,
            "maximum_fixed_wedge_shift_loads": maximum_shift_loads,
            "maximum_scalar_profile_load": max(K_2.values()),
            "rank_flat": rank_statistics,
        },
    )


if __name__ == "__main__":
    main()
