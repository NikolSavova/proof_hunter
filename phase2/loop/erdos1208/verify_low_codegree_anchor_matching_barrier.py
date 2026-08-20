#!/usr/bin/env python3
"""Exact checks for the low-codegree matching-anchor barrier."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from random import Random

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_gaussian_edge_vector_two_arm_barrier import dense_ruler
from verify_single_fibre_replacement_transition_barrier import (
    determinant,
    distance2,
    pair_tables,
    sub,
)
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
MATCHING_RECORDS = 6
TARGET_RECORDS = 7
TARGET_HORIZONTAL = 1_000
RANDOM_SEED = 1208
RADIUS = 10**12


def add(*points: Point) -> Point:
    return sum(point[0] for point in points), sum(point[1] for point in points)


def random_point(random: Random) -> Point:
    return random.randint(-RADIUS, RADIUS), random.randint(-RADIUS, RADIUS)


def anchor_star_profile(points: list[Point]) -> tuple[int, ...]:
    """Exhaustively check the fixed-head and fixed-tail star lemmas."""
    k = len(points)
    endpoint_edge: dict[Point, tuple[int, int]] = {}
    for first, second in combinations(range(k), 2):
        endpoint_edge[add(points[first], points[second])] = first, second

    difference_edge: dict[Point, tuple[int, int]] = {}
    for first in range(k):
        for second in range(k):
            if first != second:
                difference = sub(points[first], points[second])
                assert difference not in difference_edge
                difference_edge[difference] = first, second

    fibres = clean_start_fibres(points)
    common: dict[tuple[Point, Point], list[Point]] = defaultdict(list)
    for translation, starts in fibres.items():
        for first in starts:
            for second in starts:
                if first != second:
                    common[first, second].append(translation)

    incoming_groups = 0
    outgoing_groups = 0
    maximum_incoming = 0
    maximum_outgoing = 0
    maximum_rotations = 0
    for (first_start, second_start), translations in common.items():
        anchors = {translation: difference_edge[translation] for translation in translations}
        by_first: dict[int, list[Point]] = defaultdict(list)
        by_second: dict[int, list[Point]] = defaultdict(list)
        for translation, (first_anchor, second_anchor) in anchors.items():
            by_first[first_anchor].append(translation)
            by_second[second_anchor].append(translation)

        # A common second anchor forces pairwise-disjoint target edges in
        # each of the two source roles.
        for group in by_second.values():
            maximum_incoming = max(maximum_incoming, len(group))
            if len(group) >= 2:
                incoming_groups += 1
            for start in (first_start, second_start):
                target_edges = [
                    set(endpoint_edge[add(start, translation)])
                    for translation in group
                ]
                assert all(
                    left.isdisjoint(right)
                    for left, right in combinations(target_edges, 2)
                )

        # A common first anchor gives equal-sum target triples. Distinct
        # triples are disjoint, and one triple has at most three rotations.
        for group in by_first.values():
            maximum_outgoing = max(maximum_outgoing, len(group))
            if len(group) >= 2:
                outgoing_groups += 1
            for start in (first_start, second_start):
                triples: list[frozenset[int]] = []
                for translation in group:
                    second_anchor = anchors[translation][1]
                    target = set(endpoint_edge[add(start, translation)])
                    triples.append(frozenset(target | {second_anchor}))
                loads = Counter(triples)
                maximum_rotations = max(maximum_rotations, max(loads.values(), default=0))
                assert max(loads.values(), default=0) <= 3
                distinct = list(loads)
                assert all(
                    left.isdisjoint(right)
                    for left, right in combinations(distinct, 2)
                )

    return (
        len(common),
        incoming_groups,
        outgoing_groups,
        maximum_incoming,
        maximum_outgoing,
        maximum_rotations,
    )


def matching_candidate(random: Random) -> tuple:
    """Plant one exact common-source pair with a matching anchor graph."""
    target_gap = -4 * (TARGET_HORIZONTAL + 1)
    half_source_gap = 36 * (TARGET_HORIZONTAL + 1)
    parameter = 17
    low_vector = half_source_gap - parameter - 1, parameter
    high_vector = half_source_gap - parameter, parameter + 1
    assert distance2(high_vector, (0, 0)) - distance2(low_vector, (0, 0)) == (
        -18 * target_gap
    )

    points: list[Point] = []
    source_edges: list[tuple[int, int]] = []
    for vector in (high_vector, low_vector):
        centre = random_point(random)
        source_edges.append((len(points), len(points) + 1))
        points.extend((centre, add(centre, vector)))
    starts = [add(points[first], points[second]) for first, second in source_edges]

    anchors: list[tuple[int, int]] = []
    first_targets: list[tuple[int, int]] = []
    second_targets: list[tuple[int, int]] = []
    for _ in range(MATCHING_RECORDS):
        first_anchor = random_point(random)
        second_anchor = random_point(random)
        translation = sub(first_anchor, second_anchor)
        first_target_endpoint = random_point(random)
        second_target_endpoint = random_point(random)

        anchors.append((len(points), len(points) + 1))
        points.extend((first_anchor, second_anchor))
        first_targets.append((len(points), len(points) + 1))
        points.extend(
            (
                first_target_endpoint,
                sub(add(starts[0], translation), first_target_endpoint),
            )
        )
        second_targets.append((len(points), len(points) + 1))
        points.extend(
            (
                second_target_endpoint,
                sub(add(starts[1], translation), second_target_endpoint),
            )
        )

    # An independent determinant-rich target-gap star.
    star_centre = len(points)
    star_point = random_point(random)
    points.append(star_point)
    marks = dense_ruler(TARGET_RECORDS)
    verticals = [10**6 + 100 * mark for mark in marks]
    target_records: list[tuple[int, int]] = []
    for vertical in verticals:
        first_vector = TARGET_HORIZONTAL, vertical
        second_vector = TARGET_HORIZONTAL + 2, vertical
        leaf = len(points)
        points.append(add(star_point, first_vector))
        partner_first = len(points)
        partner_centre = random_point(random)
        points.extend((partner_centre, add(partner_centre, second_vector)))
        target_records.append((leaf, partner_first))

    return (
        points,
        source_edges,
        anchors,
        first_targets,
        second_targets,
        star_centre,
        target_records,
        target_gap,
    )


def planted_matching_profile() -> tuple[int, ...]:
    random = Random(RANDOM_SEED)
    for attempt in range(1, 101):
        data = matching_candidate(random)
        points = data[0]
        if len(points) != len(set(points)):
            continue
        try:
            pair_sums, distances = pair_tables(points)
        except ValueError:
            continue
        labels = set(distances)
        target_gap = data[7]
        if sum(1 for label in labels if label - (-18 * target_gap) in labels) != 1:
            continue
        break
    else:
        raise AssertionError("finite-avoidance specialization search exhausted")

    (
        points,
        source_edges,
        prescribed_anchors,
        first_targets,
        second_targets,
        star_centre,
        target_records,
        target_gap,
    ) = data
    k = len(points)
    n = len(distances)
    starts = [add(points[first], points[second]) for first, second in source_edges]

    # Enumerate every clean fibre, not only the planted rows.
    fibres = clean_start_fibres(points)
    common_translations = [
        translation
        for translation, fibre_starts in fibres.items()
        if starts[0] in fibre_starts and starts[1] in fibre_starts
    ]
    prescribed_translations = {
        sub(points[first], points[second]) for first, second in prescribed_anchors
    }
    assert set(common_translations) == prescribed_translations
    codegree = len(common_translations)
    assert codegree == MATCHING_RECORDS < k

    difference_edges = {
        sub(points[first], points[second]): (first, second)
        for first in range(k)
        for second in range(k)
        if first != second
    }
    full_anchor_edges = [difference_edges[q] for q in common_translations]
    assert len({vertex for edge in full_anchor_edges for vertex in edge}) == 2 * codegree

    for anchor, first_target, second_target in zip(
        prescribed_anchors, first_targets, second_targets
    ):
        translation = sub(points[anchor[0]], points[anchor[1]])
        assert set(pair_sums[add(starts[0], translation)]) == set(first_target)
        assert set(pair_sums[add(starts[1], translation)]) == set(second_target)
        assert len({*anchor, *source_edges[0], *first_target}) == 6
        assert len({*anchor, *source_edges[1], *second_target}) == 6
        assert set(first_target).isdisjoint(second_target)
        assert difference_edges[translation] == anchor

    source_gap = distance2(points[source_edges[0][0]], points[source_edges[0][1]]) - (
        distance2(points[source_edges[1][0]], points[source_edges[1][1]])
    )
    assert source_gap == -18 * target_gap
    raw_source_gap_count = sum(1 for label in labels if label - source_gap in labels)
    assert raw_source_gap_count == 1

    cutoff = n
    qualified_records = 0
    qualified_first_edges: list[set[int]] = []
    for leaf, partner_first in target_records:
        partner_second = partner_first + 1
        first_vector = sub(points[leaf], points[star_centre])
        second_vector = sub(points[partner_second], points[partner_first])
        assert distance2(points[star_centre], points[leaf]) - distance2(
            points[partner_first], points[partner_second]
        ) == target_gap
        assert abs(2 * determinant(first_vector, second_vector)) > cutoff
        qualified_records += 1
        qualified_first_edges.append({star_centre, leaf})

    degrees = Counter(vertex for edge in qualified_first_edges for vertex in edge)
    target_wedges = sum(degree * (degree - 1) // 2 for degree in degrees.values())
    assert target_wedges == TARGET_RECORDS * (TARGET_RECORDS - 1) // 2

    # Audit the full determinant-qualified target cell, so the reported U
    # is exact rather than merely the planted lower bound.
    full_qualified_records = 0
    for first_label, first_edge in distances.items():
        second_label = first_label - target_gap
        if second_label not in distances:
            continue
        second_edge = distances[second_label]
        first_vector = sub(points[first_edge[1]], points[first_edge[0]])
        second_vector = sub(points[second_edge[1]], points[second_edge[0]])
        if abs(2 * determinant(first_vector, second_vector)) > cutoff:
            full_qualified_records += 1
    assert full_qualified_records == qualified_records

    # Because the raw opposite-scale gap has one representation, its full
    # low-codegree common-q mass is exactly this one codegree.
    low_band_mass = codegree
    assert low_band_mass == MATCHING_RECORDS * raw_source_gap_count

    return (
        attempt,
        k,
        n,
        codegree,
        raw_source_gap_count,
        low_band_mass,
        full_qualified_records,
        target_wedges,
        cutoff,
        target_gap,
    )


def main() -> None:
    closure = anchor_star_profile(POINTS[:22])
    assert closure == (2_276, 8, 388, 2, 3, 3), closure
    print("closure-22 anchor-star profile", closure)

    planted = planted_matching_profile()
    assert planted == (1, 62, 1_891, 6, 1, 6, 7, 21, 1_891, -4_004), planted
    print("exact matching low-codegree profile", planted)
    print("low-codegree anchor-matching barrier: PASS")


if __name__ == "__main__":
    main()
