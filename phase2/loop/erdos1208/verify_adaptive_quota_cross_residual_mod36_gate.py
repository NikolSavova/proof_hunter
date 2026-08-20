#!/usr/bin/env python3
"""Checks for ADAPTIVE_QUOTA_CROSS_RESIDUAL_MOD36_GATE.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations, product
from random import Random

from verify_low_band_isolated_translation_excess_gate import (
    add,
    distance2,
    perpendicular_base,
    random_point,
    subtract,
)
from verify_metric_scalar_endpoint_rich_tail import determinant, edge_data
from verify_single_fibre_replacement_transition_barrier import pair_tables


Point = tuple[int, int]
TARGET_GAP = -100
RECORDS = 10


def check_residue_quota_identity() -> None:
    # Exhaust small labelled profiles.  An occurrence is (source area, load).
    atoms = tuple(product(range(-4, 5, 2), range(1, 5)))
    for length in range(0, 5):
        for occurrences in product(atoms, repeat=length):
            for quota in range(1, 5):
                discarded = 0
                tail_load = 0
                cross_minimum = 0
                by_residue = {}
                for area, load in occurrences:
                    by_residue.setdefault(area % 36, []).append(load)
                for loads in by_residue.values():
                    ordered = sorted(loads, reverse=True)
                    split = min(quota, len(ordered))
                    discarded += split
                    tail_load += sum(ordered[split:])
                    cross_minimum += sum(
                        min(ordered[first], ordered[second])
                        for first in range(split)
                        for second in range(split, len(ordered))
                    )
                assert discarded <= 18 * quota
                # Empty residue classes contribute zero; every nonempty tail
                # class has exactly quota top witnesses.
                assert cross_minimum == quota * tail_load
    random = Random(36_1208)
    for _ in range(2_000):
        length = random.randrange(30)
        quota = random.randrange(1, 15)
        occurrences = [
            (2 * random.randrange(-100, 101), random.randrange(1, 10_000))
            for _ in range(length)
        ]
        tail_load = 0
        cross_minimum = 0
        by_residue = {}
        for area, load in occurrences:
            by_residue.setdefault(area % 36, []).append(load)
        for loads in by_residue.values():
            ordered = sorted(loads, reverse=True)
            split = min(quota, len(ordered))
            tail_load += sum(ordered[split:])
            cross_minimum += sum(
                min(ordered[first], ordered[second])
                for first in range(split)
                for second in range(split, len(ordered))
            )
        assert cross_minimum == quota * tail_load
    print("mod-36 quota and top-tail identity: PASS")


def generalized_planted_candidate(random: Random) -> tuple[
    list[Point], int, list[tuple[tuple[int, int], tuple[int, int]]], int
]:
    horizontal_count = 8 * RECORDS + 8
    point_count = 16 * RECORDS + 16
    points = perpendicular_base(horizontal_count, point_count)

    first_anchor = len(points)
    anchor_head = random_point(random)
    anchor_tail = random_point(random)
    points.extend((anchor_head, anchor_tail))
    q = subtract(anchor_head, anchor_tail)

    source_pairs = []
    half_source_gap = 900
    for record in range(RECORDS):
        parameter = 17 + 7 * record
        high_vector = half_source_gap - parameter, parameter + 1
        low_vector = half_source_gap - parameter - 1, parameter
        assert distance2(high_vector, (0, 0)) - distance2(low_vector, (0, 0)) == 1_800

        role_sources = []
        for vector in (high_vector, low_vector):
            centre = random_point(random)
            source = (len(points), len(points) + 1)
            points.extend((centre, add(centre, vector)))
            source_sum = add(points[source[0]], points[source[1]])

            target_endpoint = random_point(random)
            points.extend((target_endpoint, subtract(add(source_sum, q), target_endpoint)))
            role_sources.append(source)
        source_pairs.append((role_sources[0], role_sources[1]))

    assert len(points) == point_count
    return points, first_anchor, source_pairs, horizontal_count


def clean_starts_at_q(points, pair_sums, q) -> set[Point]:
    starts = set()
    for start, source in pair_sums.items():
        target = pair_sums.get(add(start, q))
        if target is not None:
            # The anchor endpoints are supplied by the caller in the exact
            # certificate; this helper only finds translated pair sums.
            starts.add(start)
    return starts


def common_clean_anchors(points, pair_sums, starts) -> list[tuple[int, int]]:
    answer = []
    for head, tail in permutations(range(len(points)), 2):
        q = subtract(points[head], points[tail])
        valid = True
        for start in starts:
            source = pair_sums[start]
            target = pair_sums.get(add(start, q))
            if target is None or len({head, tail, *source, *target}) != 6:
                valid = False
                break
        if valid:
            answer.append((head, tail))
    return answer


def numeric_residual_support_barrier() -> None:
    random = Random(1_208_36_10)
    for attempt in range(1, 101):
        points, first_anchor, source_pairs, horizontal_count = generalized_planted_candidate(random)
        if len(set(points)) != len(points):
            continue
        try:
            pair_sums, distances = pair_tables(points)
        except ValueError:
            continue
        break
    else:
        raise AssertionError("ten-record planted search exhausted")

    k = len(points)
    edge_count = len(distances)
    assert edge_count == k * (k - 1) // 2
    anchor = (first_anchor, first_anchor + 1)
    q = subtract(points[anchor[0]], points[anchor[1]])

    # Check the displayed fibre and the two records used below without
    # reconstructing every clean fibre.
    displayed_starts = []
    for source_pair in source_pairs:
        starts = tuple(add(points[i], points[j]) for i, j in source_pair)
        displayed_starts.append(starts)
        for start in starts:
            target = pair_sums.get(add(start, q))
            assert target is not None
            assert len({*anchor, *pair_sums[start], *target}) == 6
    q_starts = {
        start for start, source in pair_sums.items()
        if (target := pair_sums.get(add(start, q))) is not None
        and len({*anchor, *source, *target}) == 6
    }
    assert q_starts == set(sum(displayed_starts, ()))

    for record in (0, 9):
        common = common_clean_anchors(points, pair_sums, displayed_starts[record])
        assert common == [anchor]

    edges = edge_data(points)
    by_label = {label: (endpoints, vector) for label, endpoints, vector in edges}
    by_endpoints = {endpoints: (label, vector) for label, endpoints, vector in edges}
    target_areas = []
    for first_label, (_, first_vector) in by_label.items():
        second = by_label.get(first_label - TARGET_GAP)
        if second is None:
            continue
        _, second_vector = second
        area = 2 * determinant(first_vector, second_vector)
        if abs(area) > edge_count:
            target_areas.append(area)

    assert len(target_areas) == k
    assert len(set(target_areas)) == k
    assert all(area % 4 == 0 for area in target_areas)

    source_areas = []
    for source_first, source_second in source_pairs:
        first_vector = by_endpoints[source_first][1]
        second_vector = by_endpoints[source_second][1]
        source_areas.append(2 * determinant(first_vector, second_vector))
    assert source_areas[9] - source_areas[0] == 252
    assert source_areas[9] % 36 == source_areas[0] % 36

    residue = source_areas[0] % 36
    shifts = [(area - residue) // 36 for area in (source_areas[0], source_areas[9])]
    normalized_target = {area // 2 for area in target_areas}
    first_support = {shifts[0] + value for value in normalized_target}
    second_support = {shifts[1] + value for value in normalized_target}
    assert shifts[1] - shifts[0] == 7
    assert first_support.isdisjoint(second_support)

    profile = (
        attempt,
        k,
        edge_count,
        horizontal_count,
        len(q_starts),
        len(target_areas),
        min(source_areas),
        max(source_areas),
        source_areas[0] % 36,
        shifts[1] - shifts[0],
        len(first_support & second_support),
        max(max(abs(x), abs(y)) for x, y in points),
    )
    expected = (1, 176, 15400, 88, 20, 176, -1730, -1478, 34, 7, 0, 2803083518575)
    assert profile == expected, profile
    print("same-residue disjoint residual supports", profile)


def main() -> None:
    check_residue_quota_identity()
    numeric_residual_support_barrier()
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
