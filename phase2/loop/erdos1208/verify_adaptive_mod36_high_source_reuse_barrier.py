#!/usr/bin/env python3
"""Checks for ADAPTIVE_MOD36_HIGH_SOURCE_REUSE_BARRIER.md."""

from __future__ import annotations

from itertools import combinations, product
from math import ceil
from random import Random

from verify_adaptive_mod36_global_disjoint_translate_saturation import (
    companion_set,
    common_clean_anchors,
    fibre_at,
    target_base,
)
from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_low_band_isolated_translation_excess_gate import (
    add,
    distance2,
    random_point,
    subtract,
)
from verify_metric_scalar_endpoint_rich_tail import determinant, edge_data
from verify_metric_scalar_universal_matrix_and_ruler_stress import (
    finite_field_parabola,
    lex_transform,
)
from verify_single_fibre_replacement_transition_barrier import pair_tables


Point = tuple[int, int]
TRANSLATIONS = 4
FILLER_PRIME = 47
AREA_SCALE = 5
RANDOM_SEED = 120_815_347
TRANSLATION_BASE = 10**14
TARGET_GAP = -100 * AREA_SCALE * AREA_SCALE
SOURCE_GAP = -18 * TARGET_GAP
VERTICAL_MARKS = (0, 10, 24, 26)


def check_directed_isolation_capacity() -> None:
    # Cross-oriented contacts are allowed: a directed cycle has every head
    # outdegree one and every tail indegree one, but its underlying edges are
    # not a matching.  Thus the universal capacity is one edge per available
    # anchor vertex, not one edge per two vertices.
    for vertices in range(3, 20):
        cycle = [(index, (index + 1) % vertices) for index in range(vertices)]
        outdegrees = [0] * vertices
        indegrees = [0] * vertices
        for head, tail in cycle:
            outdegrees[head] += 1
            indegrees[tail] += 1
        assert outdegrees == [1] * vertices
        assert indegrees == [1] * vertices
        assert len(cycle) == vertices
        assert len(cycle) > vertices // 2

        matching = [(2 * index, 2 * index + 1) for index in range(vertices // 2)]
        assert len(set(sum(matching, ()))) == 2 * len(matching)
        assert len(matching) == vertices // 2
    print("directed isolation versus literal matching capacity: PASS")


def norm2(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def build_plant() -> tuple:
    horizontal_count = 10 * TRANSLATIONS + FILLER_PRIME + 12
    final_count = 2 * horizontal_count
    random = Random(RANDOM_SEED)

    for attempt in range(1, 101):
        points = [
            (AREA_SCALE * x, AREA_SCALE * y)
            for x, y in target_base(horizontal_count, final_count)
        ]

        source_pairs = []
        source_starts = []
        half_source_gap = 900 * AREA_SCALE * AREA_SCALE
        for parameter in (17, 26):
            vectors = (
                (half_source_gap - parameter, parameter + 1),
                (half_source_gap - parameter - 1, parameter),
            )
            assert norm2(vectors[0]) - norm2(vectors[1]) == SOURCE_GAP
            role_sources = []
            starts = []
            for vector in vectors:
                centre = random_point(random)
                source = (len(points), len(points) + 1)
                points.extend((centre, add(centre, vector)))
                role_sources.append(source)
                starts.append(add(points[source[0]], points[source[1]]))
            source_pairs.append((role_sources[0], role_sources[1]))
            source_starts.append((starts[0], starts[1]))

        anchors = []
        for _ in range(TRANSLATIONS):
            first_anchor = len(points)
            anchor_head = random_point(random)
            anchor_tail = random_point(random)
            points.extend((anchor_head, anchor_tail))
            translation = subtract(anchor_head, anchor_tail)
            anchors.append((first_anchor, first_anchor + 1, translation))

            for start in sum(source_starts, ()):
                target_endpoint = random_point(random)
                points.extend(
                    (
                        target_endpoint,
                        subtract(add(start, translation), target_endpoint),
                    )
                )

        assert len(points) == final_count - FILLER_PRIME
        if len(points) != len(set(points)):
            continue
        try:
            _, distances = pair_tables(points)
        except ValueError:
            continue
        labels = set(distances)
        if sum(label - SOURCE_GAP in labels for label in labels) != 2:
            continue
        if sum(label - TARGET_GAP in labels for label in labels) != final_count + 1:
            continue
        return (
            points,
            source_pairs,
            source_starts,
            anchors,
            horizontal_count,
            final_count,
            attempt,
        )
    raise AssertionError("high-reuse planted search exhausted")


def build_union() -> tuple:
    plant = build_plant()
    plant_points = plant[0]
    _, plant_distances = pair_tables(plant_points)
    filler_base = [
        lex_transform(FILLER_PRIME, point)
        for point in finite_field_parabola(FILLER_PRIME)
    ]
    plant_labels = set(plant_distances)

    scale = next(
        candidate
        for candidate in range(1, 1_000)
        if plant_labels.isdisjoint(
            {
                candidate * candidate * distance2(first, second)
                for first, second in combinations(filler_base, 2)
            }
        )
    )
    scaled_filler = [(scale * x, scale * y) for x, y in filler_base]

    for offset in range(100):
        parameter = TRANSLATION_BASE + offset
        filler_translation = (parameter, parameter * parameter)
        points = plant_points + [
            add(point, filler_translation) for point in scaled_filler
        ]
        if len(points) != len(set(points)):
            continue
        try:
            pair_sums, distances = pair_tables(points)
        except ValueError:
            continue
        labels = set(distances)
        if sum(label - SOURCE_GAP in labels for label in labels) != 2:
            continue
        return (
            points,
            pair_sums,
            distances,
            plant,
            filler_base,
            scale,
            offset,
        )
    raise AssertionError("high-reuse plant/filler union search exhausted")


def certificate() -> tuple[int, ...]:
    (
        points,
        pair_sums,
        distances,
        plant,
        filler_base,
        filler_scale,
        filler_offset,
    ) = build_union()
    (
        _,
        source_pairs,
        source_starts,
        anchors,
        horizontal_count,
        final_count,
        plant_attempt,
    ) = plant

    k = len(points)
    edge_count = len(distances)
    assert k == final_count == 198
    assert edge_count == k * (k - 1) // 2

    anchor_by_translation = {
        subtract(points[head], points[tail]): (head, tail)
        for head in range(k)
        for tail in range(k)
        if head != tail
    }
    assert len(anchor_by_translation) == k * (k - 1)

    expected_anchor_edges = [(head, tail) for head, tail, _ in anchors]
    planted_fibres = []
    for head, tail, translation in anchors:
        fibre = fibre_at(points, pair_sums, anchor_by_translation, translation)
        planted_fibres.append(fibre)
        assert len(fibre) == 4
        assert set(fibre) == set(sum(source_starts, ()))

        block_companions = []
        for starts in source_starts:
            for start in starts:
                total = add(start, points[head])
                companions, triples = companion_set(points, total, head)
                assert all(
                    set(first).isdisjoint(second)
                    for first, second in combinations(triples, 2)
                )
                block_companions.append(companions)
        assert all(
            first & second == {tail}
            for first, second in combinations(block_companions, 2)
        )

    # Both source pairs have exactly the same linearly large anchor matching.
    for starts in source_starts:
        assert common_clean_anchors(points, pair_sums, starts) == expected_anchor_edges
    assert len(set(sum(expected_anchor_edges, ()))) == 2 * TRANSLATIONS
    assert set(sum(expected_anchor_edges, ())).isdisjoint(
        set(sum(sum(source_pairs, ()), ()))
    )
    assert TRANSLATIONS <= (k - 4) // 2

    edges = edge_data(points)
    edge_by_label = {label: (endpoints, vector) for label, endpoints, vector in edges}
    edge_by_endpoints = {
        endpoints: (label, vector) for label, endpoints, vector in edges
    }
    labels = set(edge_by_label)
    assert sum(label - SOURCE_GAP in labels for label in labels) == 2
    assert sum(label - TARGET_GAP in labels for label in labels) == k + 1

    source_areas = []
    for high_edge, low_edge in source_pairs:
        high_label, high_vector = edge_by_endpoints[high_edge]
        low_label, low_vector = edge_by_endpoints[low_edge]
        assert high_label - low_label == SOURCE_GAP
        source_areas.append(2 * determinant(high_vector, low_vector))
    assert source_areas == [-44930, -44894]
    assert source_areas[0] % 36 == source_areas[1] % 36

    target_areas = []
    for first_label, (_, first_vector) in edge_by_label.items():
        second = edge_by_label.get(first_label - TARGET_GAP)
        if second is None:
            continue
        area = 2 * determinant(first_vector, second[1])
        if abs(area) > edge_count:
            target_areas.append(area)
    assert len(target_areas) == k
    assert len(set(target_areas)) == k
    normalized_target = {area // 2 for area in target_areas}
    assert all(area % (AREA_SCALE * AREA_SCALE) == 0 for area in normalized_target)

    residue = source_areas[0] % 36
    shifts = [(area - residue) // 36 for area in source_areas]
    assert shifts[1] - shifts[0] == 1
    supports = [
        {shift + area for area in normalized_target} for shift in shifts
    ]
    assert supports[0].isdisjoint(supports[1])

    # Physical wedge audit.
    origin = horizontal_count + VERTICAL_MARKS.index(0)
    vertical_ten = horizontal_count + VERTICAL_MARKS.index(10)
    fixed_edges = (
        tuple(sorted((origin, 0))),
        tuple(sorted((origin, 1))),
    )
    partner_edges = (
        tuple(sorted((vertical_ten, 0))),
        tuple(sorted((vertical_ten, 1))),
    )
    for fixed, partner in zip(fixed_edges, partner_edges):
        assert edge_by_endpoints[fixed][0] - edge_by_endpoints[partner][0] == TARGET_GAP
        assert abs(
            2
            * determinant(
                edge_by_endpoints[fixed][1], edge_by_endpoints[partner][1]
            )
        ) > edge_count

    filler_fibres = clean_start_fibres(filler_base)
    fibre_mass = sum(map(len, planted_fibres))
    selected_filler_translations = 0
    planted_translations = {translation for _, _, translation in anchors}
    for translation, _ in sorted(
        (
            ((filler_scale * q[0], filler_scale * q[1]), len(starts))
            for q, starts in filler_fibres.items()
        ),
        key=lambda item: (-item[1], item[0]),
    ):
        if translation in planted_translations:
            continue
        fibre_mass += len(
            fibre_at(points, pair_sums, anchor_by_translation, translation)
        )
        selected_filler_translations += 1
        if fibre_mass >= 4 * k * k:
            break
    assert 4 * k * k <= fibre_mass < 4 * k * k + edge_count

    quotas = [
        ceil(k * k * len(fibre) / fibre_mass) for fibre in planted_fibres
    ]
    assert quotas == [1] * TRANSLATIONS
    x_36 = TRANSLATIONS * len(target_areas)
    assert x_36 == 792

    # Tied loads may be ordered independently in each fibre.  Every ordering
    # leaves one tail, keeps total mass fixed, and gives one source pair
    # multiplicity at least half the number of translations.
    minimum_maximum_reuse = TRANSLATIONS
    for top_choices in product((0, 1), repeat=TRANSLATIONS):
        tail_counts = [0, 0]
        for top in top_choices:
            tail_counts[1 - top] += 1
        assert sum(tail_counts) == TRANSLATIONS
        minimum_maximum_reuse = min(minimum_maximum_reuse, max(tail_counts))
    assert minimum_maximum_reuse == ceil(TRANSLATIONS / 2)

    profile = (
        plant_attempt,
        filler_scale,
        filler_offset,
        k,
        edge_count,
        len(anchors),
        sum(map(len, planted_fibres)),
        len(target_areas),
        len(filler_fibres),
        sum(map(len, filler_fibres.values())),
        selected_filler_translations,
        fibre_mass,
        quotas[0],
        x_36,
        minimum_maximum_reuse,
        residue,
        min(source_areas),
        max(source_areas),
        max(max(abs(x), abs(y)) for x, y in points),
    )
    expected = (
        1,
        1,
        0,
        198,
        19503,
        4,
        16,
        198,
        2162,
        300798,
        865,
        156955,
        1,
        792,
        2,
        34,
        -44930,
        -44894,
        10000000000000000000010131534,
    )
    assert profile == expected, profile
    return profile


def main() -> None:
    check_directed_isolation_capacity()
    profile = certificate()
    print("high same-source reuse", profile)
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
