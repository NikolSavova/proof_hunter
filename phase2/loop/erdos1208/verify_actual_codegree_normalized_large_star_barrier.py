#!/usr/bin/env python3
"""Finite shadow of the actual-codegree large-star equality barrier."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
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
from verify_synchronized_global_multi_wedge_golomb_counterexample import SCALAR


Point = tuple[int, int]
ARM_COUNT = 12
RANDOM_SEED = 1208


def build_points() -> tuple[list[Point], int, list[int], list[tuple[int, int]], list[int]]:
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

    verticals: list[int] = []
    fixed_lengths: list[int] = []
    for vertical in range(1, 2_001, 2):
        fixed = (SCALAR + vertical * vertical + 1) // 2
        partner_horizontal = fixed - 1
        labels = {
            fixed * fixed,
            partner_horizontal * partner_horizontal + vertical * vertical,
        }
        labels.update((fixed - previous) ** 2 for previous in fixed_lengths)
        if len(labels) != 2 + len(fixed_lengths):
            continue
        if labels & used_labels:
            continue
        verticals.append(vertical)
        fixed_lengths.append(fixed)
        used_labels.update(labels)
        if len(verticals) == ARM_COUNT:
            break
    assert verticals == [1, 3, 27, 35, 93, 115, 117, 123, 173, 211, 213, 227]

    random = Random(RANDOM_SEED)
    points = list(core)
    origin = len(points)
    origin_point = (
        random.randrange(10**11, 10**12),
        random.randrange(10**11, 10**12),
    )
    points.append(origin_point)
    first_endpoints = []
    for fixed in fixed_lengths:
        first_endpoints.append(len(points))
        points.append((origin_point[0] + fixed, origin_point[1]))

    partner_edges = []
    for vertical, fixed in zip(verticals, fixed_lengths):
        centre = (
            random.randrange(10**11, 10**12),
            random.randrange(10**11, 10**12),
        )
        left = len(points)
        points.append(centre)
        right = len(points)
        points.append((centre[0] + fixed - 1, centre[1] + vertical))
        partner_edges.append((left, right))

    assert len(points) == 60 + 1 + 3 * ARM_COUNT
    pair_tables(points)
    return points, origin, first_endpoints, partner_edges, verticals


def profile() -> tuple[object, ...]:
    points, origin, first_endpoints, partner_edges, verticals = build_points()
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
    transverse_records = 0
    synchronized_pair_numerator = 0
    minimum_transverse = codegree
    maximum_transverse = 0
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
            transverse_records += transverse
            synchronized_pair_numerator += comb(transverse, 2)
            minimum_transverse = min(minimum_transverse, transverse)
            maximum_transverse = max(maximum_transverse, transverse)
    assert rich_bases == one_role

    edge_at_distance = {
        distance: edge_at_sum[pair_sum]
        for pair_sum, distance in distance_at_sum.items()
    }

    def edge_vector(edge: tuple[int, int]) -> Point:
        return subtract(points[edge[1]], points[edge[0]])

    def qualified_graph(scalar: int) -> tuple[list[tuple[int, int]], int]:
        eligible = []
        for distance, edge in edge_at_distance.items():
            partner = edge_at_distance.get(distance - scalar)
            if partner is None:
                continue
            if abs(2 * determinant(edge_vector(edge), edge_vector(partner))) > edge_count:
                eligible.append(edge)
        degrees = Counter(endpoint for edge in eligible for endpoint in edge)
        return eligible, sum(comb(degree, 2) for degree in degrees.values())

    eligible, wedge_weight = qualified_graph(SCALAR)
    reverse_eligible, reverse_wedge_weight = qualified_graph(-SCALAR)
    assert wedge_weight == comb(ARM_COUNT, 2)
    assert reverse_wedge_weight == 0

    for endpoint, partner_edge, vertical in zip(
        first_endpoints, partner_edges, verticals
    ):
        fixed_edge = (origin, endpoint)
        fixed_sum = add(points[fixed_edge[0]], points[fixed_edge[1]])
        partner_sum = add(points[partner_edge[0]], points[partner_edge[1]])
        assert distance_at_sum[fixed_sum] - distance_at_sum[partner_sum] == SCALAR
        assert abs(
            2
            * determinant(
                edge_vector(fixed_edge),
                edge_vector(partner_edge),
            )
        ) > edge_count

    distance_labels = set(distance_at_sum.values())
    gap_multiplicity = sum(
        distance - SCALAR in distance_labels for distance in distance_labels
    )
    reverse_gap_multiplicity = sum(
        distance + SCALAR in distance_labels for distance in distance_labels
    )

    direct_mass = one_role * wedge_weight
    normalized_transverse_mass = Fraction(
        transverse_records * wedge_weight, codegree
    )
    pre_normalized_transverse_mass = transverse_records * wedge_weight
    pre_normalized_pair_mass = Fraction(
        synchronized_pair_numerator * wedge_weight, codegree
    )
    outer_normalized_pair_mass = Fraction(
        synchronized_pair_numerator * wedge_weight, codegree * codegree
    )
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
        transverse_records,
        synchronized_pair_numerator,
        len(eligible),
        wedge_weight,
        len(reverse_eligible),
        reverse_wedge_weight,
        gap_multiplicity,
        reverse_gap_multiplicity,
        direct_mass,
        normalized_transverse_mass,
        pre_normalized_transverse_mass,
        pre_normalized_pair_mass,
        outer_normalized_pair_mass,
        edge_count * k**3,
        edge_count * k**4,
        max(max(abs(x), abs(y)) for x, y in points),
    )


def main() -> None:
    actual = profile()
    expected = (
        97,
        4_656,
        5_112,
        1_519_236,
        326,
        6_369,
        6_369,
        185,
        250,
        1_387_749,
        150_763_816,
        12,
        66,
        12,
        0,
        12,
        12,
        420_354,
        Fraction(45_795_717, 163),
        91_591_434,
        Fraction(4_975_205_928, 163),
        Fraction(2_487_602_964, 26_569),
        4_249_405_488,
        412_192_332_336,
        903_272_942_369,
    )
    assert actual == expected, (actual, expected)
    print("actual-codegree large-star profile", actual)
    print("pre-normalized Nk^4 gate: ASYMPTOTIC COUNTEREXAMPLE SHADOW PASS")


if __name__ == "__main__":
    main()
