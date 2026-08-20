#!/usr/bin/env python3
"""Finite shadow of the pooled P_2 multi-wedge Golomb counterexample."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb
from random import Random

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_high_codegree_replacement_completion import add, subtract, tables
from verify_metric_scalar_endpoint_rich_tail import determinant
from verify_single_fibre_replacement_transition_barrier import pair_tables
from verify_synchronized_fixed_wedge_dyadic_golomb_counterexample import (
    CORE_SCALE,
    CORE_TRANSLATION,
    GENERATOR,
    PRIME,
    SOURCE_FIRST,
    SOURCE_SECOND,
    masks,
    ruzsa_ruler,
)


Point = tuple[int, int]
COPY_COUNT = 6
SCALAR = -2_673_600
RANDOM_SEED = 1208


def forced_labels(
    first_vertical: int, second_vertical: int
) -> tuple[list[int], list[int], set[int]]:
    verticals = (first_vertical, second_vertical)
    fixed = [(SCALAR + value * value + 1) // 2 for value in verticals]
    partner = [(SCALAR + value * value - 1) // 2 for value in verticals]
    labels = {
        fixed[0] ** 2,
        fixed[1] ** 2,
        partner[0] ** 2 + verticals[0] ** 2,
        partner[1] ** 2 + verticals[1] ** 2,
        (fixed[0] - fixed[1]) ** 2,
    }
    assert len(labels) == 5
    assert all(
        fixed_value * fixed_value
        - partner_value * partner_value
        - vertical * vertical
        == SCALAR
        for fixed_value, partner_value, vertical in zip(
            fixed, partner, verticals
        )
    )
    return fixed, partner, labels


def build_points() -> tuple[list[Point], list[tuple[int, ...]], list[tuple[int, int]]]:
    marks = ruzsa_ruler(PRIME, GENERATOR)
    core = [
        (
            CORE_TRANSLATION[0] + CORE_SCALE * mark,
            CORE_TRANSLATION[1],
        )
        for mark in marks
    ]
    _, core_distances = pair_tables(core)
    used_labels = set(core_distances)
    vertical_pairs: list[tuple[int, int]] = []
    parameter_data: list[tuple[list[int], list[int]]] = []
    for first, second in combinations(range(1, 401, 2), 2):
        fixed, partner, labels = forced_labels(first, second)
        if labels & used_labels:
            continue
        vertical_pairs.append((first, second))
        parameter_data.append((fixed, partner))
        used_labels.update(labels)
        if len(vertical_pairs) == COPY_COUNT:
            break
    assert vertical_pairs == [(1, 3), (5, 9), (7, 15), (11, 21), (13, 27), (17, 33)]

    random = Random(RANDOM_SEED)
    points = list(core)
    gadgets: list[tuple[int, ...]] = []
    for verticals, (fixed, partner) in zip(vertical_pairs, parameter_data):
        origin = (
            random.randrange(10**11, 10**12),
            random.randrange(10**11, 10**12),
        )
        first_centre = (
            random.randrange(10**11, 10**12),
            random.randrange(10**11, 10**12),
        )
        second_centre = (
            random.randrange(10**11, 10**12),
            random.randrange(10**11, 10**12),
        )
        indices = tuple(range(len(points), len(points) + 7))
        points.extend((
            origin,
            (origin[0] + fixed[0], origin[1]),
            (origin[0] + fixed[1], origin[1]),
            first_centre,
            (
                first_centre[0] + partner[0],
                first_centre[1] + verticals[0],
            ),
            second_centre,
            (
                second_centre[0] + partner[1],
                second_centre[1] + verticals[1],
            ),
        ))
        gadgets.append(indices)

    assert len(points) == 60 + 7 * COPY_COUNT
    pair_tables(points)
    return points, gadgets, vertical_pairs


def profile() -> tuple[int, ...]:
    points, gadgets, vertical_pairs = build_points()
    k = len(points)
    edge_count = comb(k, 2)
    edge_at_sum, distance_at_sum, anchor_at_difference = tables(points)
    fibres = clean_start_fibres(points)

    source_first = add(points[SOURCE_FIRST[0]], points[SOURCE_FIRST[1]])
    source_second = add(points[SOURCE_SECOND[0]], points[SOURCE_SECOND[1]])
    assert distance_at_sum[source_first] - distance_at_sum[source_second] == -18 * SCALAR
    translations = [
        translation
        for translation, starts in fibres.items()
        if source_first in starts and source_second in starts
    ]
    codegree = len(translations)
    anchor_edges = [set(anchor_at_difference[q]) for q in translations]
    first_edges = [set(edge_at_sum[add(source_first, q)]) for q in translations]
    second_edges = [set(edge_at_sum[add(source_second, q)]) for q in translations]
    anchor_masks = masks(anchor_edges)
    first_masks = masks(first_edges)
    second_masks = masks(second_edges)

    one_role = 0
    rich_bases = 0
    minimum_transverse = codegree
    maximum_transverse = 0
    synchronized_pair_mass = 0
    for left, right in combinations(range(codegree), 2):
        if bool(first_edges[left] & first_edges[right]) == bool(
            second_edges[left] & second_edges[right]
        ):
            continue
        one_role += 1
        forbidden = (
            anchor_masks[left]
            | anchor_masks[right]
            | first_masks[left]
            | first_masks[right]
            | second_masks[left]
            | second_masks[right]
        )
        transverse = codegree - forbidden.bit_count()
        if 2 * transverse >= codegree:
            rich_bases += 1
            minimum_transverse = min(minimum_transverse, transverse)
            maximum_transverse = max(maximum_transverse, transverse)
            synchronized_pair_mass += comb(transverse, 2)
    assert one_role == rich_bases

    # Each stored gadget contributes one distinct physical wedge at the
    # same scalar and at the final sharp determinant cutoff.
    for indices, verticals in zip(gadgets, vertical_pairs):
        origin, first, second, partner_a, partner_b, partner_c, partner_d = indices
        fixed_edges = ((origin, first), (origin, second))
        partner_edges = ((partner_a, partner_b), (partner_c, partner_d))
        for fixed_edge, partner_edge in zip(fixed_edges, partner_edges):
            fixed_vector = subtract(points[fixed_edge[1]], points[fixed_edge[0]])
            partner_vector = subtract(
                points[partner_edge[1]], points[partner_edge[0]]
            )
            assert (
                distance_at_sum[add(points[fixed_edge[0]], points[fixed_edge[1]])]
                - distance_at_sum[add(points[partner_edge[0]], points[partner_edge[1]])]
                == SCALAR
            )
            assert abs(2 * determinant(fixed_vector, partner_vector)) > edge_count
        assert (
            distance2(points[origin], points[first])
            - distance2(points[origin], points[second])
            == distance2(points[partner_a], points[partner_b])
            - distance2(points[partner_c], points[partner_d])
        )

    # Independently reconstruct the whole determinant-qualified first-edge
    # graph at the selected scalar and count its endpoint wedges.
    edge_at_distance = {
        distance: edge_at_sum[pair_sum]
        for pair_sum, distance in distance_at_sum.items()
    }

    def edge_vector(edge: tuple[int, int]) -> Point:
        return subtract(points[edge[1]], points[edge[0]])

    eligible = []
    for distance, edge in edge_at_distance.items():
        partner = edge_at_distance.get(distance - SCALAR)
        if partner is None:
            continue
        if abs(2 * determinant(edge_vector(edge), edge_vector(partner))) > edge_count:
            eligible.append(edge)
    degrees = Counter(endpoint for edge in eligible for endpoint in edge)
    wedge_weight = sum(comb(degree, 2) for degree in degrees.values())
    assert wedge_weight == COPY_COUNT

    # This construction is intentionally not a counterexample to the
    # original raw scalar aggregate.  Audit the two ordered fixed-gap
    # multiplicities separately from the much larger synchronized pool.
    distance_labels = set(distance_at_sum.values())
    positive_gap_multiplicity = sum(
        distance - SCALAR in distance_labels for distance in distance_labels
    )
    negative_gap_multiplicity = sum(
        distance + SCALAR in distance_labels for distance in distance_labels
    )
    assert positive_gap_multiplicity == negative_gap_multiplicity

    pooled_lower_bound = wedge_weight * synchronized_pair_mass
    nominal_global_scale = edge_count * k**5
    return (
        k,
        edge_count,
        len(fibres),
        sum(len(starts) for starts in fibres.values()),
        codegree,
        one_role,
        rich_bases,
        minimum_transverse,
        maximum_transverse,
        synchronized_pair_mass,
        len(eligible),
        wedge_weight,
        positive_gap_multiplicity,
        negative_gap_multiplicity,
        pooled_lower_bound,
        nominal_global_scale,
        max(max(abs(x), abs(y)) for x, y in points),
    )


def distance2(first: Point, second: Point) -> int:
    difference = subtract(first, second)
    return difference[0] * difference[0] + difference[1] * difference[1]


def main() -> None:
    actual = profile()
    expected = (
        102,
        5_151,
        3_990,
        1_323_216,
        320,
        6_169,
        6_169,
        182,
        245,
        139_373_896,
        12,
        6,
        12,
        12,
        836_243_376,
        56_871_202_172_832,
        903_272_942_369,
    )
    assert actual == expected, (actual, expected)
    print("global synchronized multi-wedge profile", actual)
    print("pooled P_2/Nk^5 gate: ASYMPTOTIC COUNTEREXAMPLE SHADOW PASS")


if __name__ == "__main__":
    main()
