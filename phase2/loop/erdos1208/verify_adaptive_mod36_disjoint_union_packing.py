#!/usr/bin/env python3
"""Checks for ADAPTIVE_MOD36_DISJOINT_UNION_PACKING.md."""

from __future__ import annotations

from itertools import combinations
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
BLOCKS = 3
RECORDS_PER_BLOCK = 2
TOTAL_RECORDS = BLOCKS * RECORDS_PER_BLOCK
FILLER_PRIME = 47
AREA_SCALE = 2 * TOTAL_RECORDS + 1
RANDOM_SEED = 12_083_647_470_03
TRANSLATION_BASE = 10**14
TARGET_GAP = -100 * AREA_SCALE * AREA_SCALE
SOURCE_GAP = -18 * TARGET_GAP
VERTICAL_MARKS = (0, 10, 24, 26)


def check_abstract_packing() -> None:
    random = Random(1_208_153)
    for _ in range(10_000):
        universe_size = random.randrange(1, 20)
        number_sets = random.randrange(1, 12)
        cell_cap = random.randrange(1, 8)
        supports = []
        multiplicities = []
        loads = []
        for _ in range(number_sets):
            support = {
                cell
                for cell in range(universe_size)
                if random.randrange(4) == 0
            }
            if not support:
                support = {random.randrange(universe_size)}
            multiplicity = random.randrange(1, 9)
            weights = [random.randrange(1, cell_cap + 1) for _ in support]
            supports.append(support)
            multiplicities.append(multiplicity)
            loads.append(sum(weights))

        depth = max(
            sum(cell in support for support in supports)
            for cell in range(universe_size)
        )
        maximum_multiplicity = max(multiplicities)
        mass = sum(
            multiplicity * load
            for multiplicity, load in zip(multiplicities, loads)
        )
        assert mass <= (
            cell_cap
            * maximum_multiplicity
            * depth
            * universe_size
        )

    # Every factor in the inequality can be sharp simultaneously.
    universe_size = 17
    cell_cap = 5
    maximum_multiplicity = 7
    supports = [set(range(universe_size)) for _ in range(3)]
    depth = 3
    mass = sum(
        maximum_multiplicity * cell_cap * len(support)
        for support in supports
    )
    assert mass == (
        cell_cap * maximum_multiplicity * depth * universe_size
    )
    print("abstract depth/multiplicity packing: PASS")


def check_residual_interval() -> None:
    for side in range(2, 10):
        radius = side - 1
        vectors = [
            (x, y)
            for x in range(-radius, radius + 1)
            for y in range(-radius, radius + 1)
        ]
        determinant_bound = max(
            abs(determinant(first, second))
            for first in vectors
            for second in vectors
        )
        assert determinant_bound == 2 * radius * radius
        source_area_bound = 2 * determinant_bound
        target_area_bound = 2 * determinant_bound
        residual_bound = source_area_bound + 18 * target_area_bound
        assert residual_bound == 76 * radius * radius
        assert 2 * residual_bound + 1 <= 153 * side * side
    print("153m^2 full-residual interval: PASS")


def norm2(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def build_plant() -> tuple:
    block_point_cost = BLOCKS * (8 * RECORDS_PER_BLOCK + 2)
    horizontal_count = block_point_cost + FILLER_PRIME + 4
    final_count = 2 * horizontal_count
    random = Random(RANDOM_SEED)

    for attempt in range(1, 101):
        points = [
            (AREA_SCALE * x, AREA_SCALE * y)
            for x, y in target_base(horizontal_count, final_count)
        ]
        anchors = []
        source_blocks = []
        global_record = 0
        half_source_gap = 900 * AREA_SCALE * AREA_SCALE

        for _ in range(BLOCKS):
            first_anchor = len(points)
            anchor_head = random_point(random)
            anchor_tail = random_point(random)
            points.extend((anchor_head, anchor_tail))
            translation = subtract(anchor_head, anchor_tail)
            anchors.append((first_anchor, first_anchor + 1, translation))

            source_pairs = []
            for _ in range(RECORDS_PER_BLOCK):
                parameter = 17 + 9 * global_record
                global_record += 1
                vectors = (
                    (half_source_gap - parameter, parameter + 1),
                    (half_source_gap - parameter - 1, parameter),
                )
                assert norm2(vectors[0]) - norm2(vectors[1]) == SOURCE_GAP

                role_sources = []
                for vector in vectors:
                    centre = random_point(random)
                    source = (len(points), len(points) + 1)
                    points.extend((centre, add(centre, vector)))
                    source_sum = add(points[source[0]], points[source[1]])

                    target_endpoint = random_point(random)
                    points.extend(
                        (
                            target_endpoint,
                            subtract(
                                add(source_sum, translation), target_endpoint
                            ),
                        )
                    )
                    role_sources.append(source)
                source_pairs.append((role_sources[0], role_sources[1]))
            source_blocks.append(source_pairs)

        assert len(points) == final_count - FILLER_PRIME
        if len(points) != len(set(points)):
            continue
        try:
            _, distances = pair_tables(points)
        except ValueError:
            continue
        labels = set(distances)
        if sum(label - SOURCE_GAP in labels for label in labels) != TOTAL_RECORDS:
            continue
        if sum(label - TARGET_GAP in labels for label in labels) != final_count + 1:
            continue
        return (
            points,
            anchors,
            source_blocks,
            horizontal_count,
            final_count,
            attempt,
        )
    raise AssertionError("multi-q planted search exhausted")


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
        if sum(label - SOURCE_GAP in labels for label in labels) != TOTAL_RECORDS:
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
    raise AssertionError("multi-q plant/filler union search exhausted")


def multi_q_certificate() -> tuple[int, ...]:
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
        anchors,
        source_blocks,
        horizontal_count,
        final_count,
        plant_attempt,
    ) = plant

    k = len(points)
    edge_count = len(distances)
    assert k == final_count == 210
    assert edge_count == k * (k - 1) // 2

    anchor_by_translation = {
        subtract(points[head], points[tail]): (head, tail)
        for head in range(k)
        for tail in range(k)
        if head != tail
    }
    assert len(anchor_by_translation) == k * (k - 1)

    planted_fibres = []
    source_starts = []
    for (head, tail, translation), source_pairs in zip(anchors, source_blocks):
        fibre = fibre_at(points, pair_sums, anchor_by_translation, translation)
        planted_fibres.append(fibre)
        assert len(fibre) == 2 * RECORDS_PER_BLOCK

        block_starts = []
        block_companions = []
        for source_pair in source_pairs:
            starts = tuple(
                add(points[first], points[second])
                for first, second in source_pair
            )
            block_starts.append(starts)
            source_starts.append(starts)
            assert common_clean_anchors(points, pair_sums, starts) == [
                (head, tail)
            ]
            for start in starts:
                total = add(start, points[head])
                companions, triples = companion_set(points, total, head)
                assert all(
                    set(first).isdisjoint(second)
                    for first, second in combinations(triples, 2)
                )
                block_companions.append(companions)
        assert set(sum(block_starts, ())) == set(fibre)
        assert all(
            first & second == {tail}
            for first, second in combinations(block_companions, 2)
        )

    edges = edge_data(points)
    edge_by_label = {label: (endpoints, vector) for label, endpoints, vector in edges}
    edge_by_endpoints = {
        endpoints: (label, vector) for label, endpoints, vector in edges
    }
    all_labels = set(edge_by_label)
    assert sum(label - SOURCE_GAP in all_labels for label in all_labels) == TOTAL_RECORDS
    assert sum(label - TARGET_GAP in all_labels for label in all_labels) == k + 1

    source_areas = []
    for source_pairs in source_blocks:
        for high_edge, low_edge in source_pairs:
            high_label, high_vector = edge_by_endpoints[high_edge]
            low_label, low_vector = edge_by_endpoints[low_edge]
            assert high_label - low_label == SOURCE_GAP
            source_areas.append(2 * determinant(high_vector, low_vector))
    assert source_areas == [
        -304130,
        -304094,
        -304058,
        -304022,
        -303986,
        -303950,
    ]

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
    assert [shift - shifts[0] for shift in shifts] == list(range(TOTAL_RECORDS))
    normalized_supports = [
        {shift + area for area in normalized_target} for shift in shifts
    ]
    full_supports = [
        {source_area + 18 * target_area for target_area in target_areas}
        for source_area in source_areas
    ]
    assert all(
        first.isdisjoint(second)
        for first, second in combinations(normalized_supports, 2)
    )
    assert all(
        first.isdisjoint(second)
        for first, second in combinations(full_supports, 2)
    )

    # Verify the fixed physical wedge.
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
    assert quotas == [1] * BLOCKS
    x_36 = BLOCKS * (RECORDS_PER_BLOCK - 1) * len(target_areas)
    assert x_36 == 630

    # Every source pair occurs at one q and every full support has depth one.
    source_multiplicity = 1
    support_depth = 1
    assert all(
        top.isdisjoint(tail)
        for top, tail in combinations(full_supports, 2)
    )

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
        source_multiplicity,
        support_depth,
        residue,
        min(source_areas),
        max(source_areas),
        max(max(abs(x), abs(y)) for x, y in points),
    )
    expected = (
        1,
        1,
        0,
        210,
        21945,
        3,
        12,
        210,
        2162,
        300798,
        991,
        176425,
        1,
        630,
        1,
        1,
        34,
        -304130,
        -303950,
        10000000000000000000010131534,
    )
    assert profile == expected, profile
    return profile


def main() -> None:
    check_abstract_packing()
    check_residual_interval()
    profile = multi_q_certificate()
    print("multi-q globally disjoint saturation", profile)
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
