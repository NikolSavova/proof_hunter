#!/usr/bin/env python3
"""Certificate for ADAPTIVE_MOD36_GLOBAL_DISJOINT_TRANSLATE_SATURATION.md.

The certificate combines four planted same-residue occurrences, a scaled
perpendicular target pencil, and a 47-point finite-field-parabola filler.
It verifies the actual adaptive denominator and the complete absence of
top--tail shifted-support intersections.
"""

from __future__ import annotations

from itertools import combinations, permutations
from math import ceil
from random import Random

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_gaussian_edge_vector_two_arm_barrier import dense_ruler
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
RECORDS = 4
FILLER_PRIME = 47
AREA_SCALE = 11
RANDOM_SEED = 1_208_364_747
TRANSLATION_BASE = 10**14
TARGET_GAP = -100 * AREA_SCALE * AREA_SCALE
SOURCE_GAP = -18 * TARGET_GAP
TARGET_VERTICAL_MARKS = (0, 10, 24, 26)


def norm2(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def target_base(horizontal_count: int, final_count: int) -> list[Point]:
    """A two-axis DS set with exactly two noncollinear target records per row."""
    horizontal_ruler = dense_ruler(horizontal_count)
    horizontal_scale = 2
    final_edge_count = final_count * (final_count - 1) // 2
    offset = max(
        final_edge_count + 1,
        max(TARGET_VERTICAL_MARKS) + 1,
        horizontal_scale * max(horizontal_ruler) + 1,
    )
    points = [
        *((offset + horizontal_scale * mark, 0) for mark in horizontal_ruler),
        *((0, mark) for mark in TARGET_VERTICAL_MARKS),
    ]
    _, distances = pair_tables(points)
    labels = set(distances)
    # The extra target-gap pair is the collinear vertical pair of edge
    # lengths 24^2 and 26^2; it has doubled area zero and is cut off later.
    assert sum(label + 100 in labels for label in labels) == 2 * horizontal_count + 1
    assert sum(label - 1800 in labels for label in labels) == 0
    return points


def build_plant() -> tuple[
    list[Point],
    int,
    Point,
    list[tuple[tuple[int, int], tuple[int, int]]],
    int,
    int,
]:
    """Build the scaled target pencil and four clean source records."""
    horizontal_count = 8 * RECORDS + FILLER_PRIME + 6
    final_count = 16 * RECORDS + 2 * FILLER_PRIME + 12
    random = Random(RANDOM_SEED)

    for attempt in range(1, 101):
        points = [
            (AREA_SCALE * x, AREA_SCALE * y)
            for x, y in target_base(horizontal_count, final_count)
        ]
        first_anchor = len(points)
        anchor_head = random_point(random)
        anchor_tail = random_point(random)
        points.extend((anchor_head, anchor_tail))
        translation = subtract(anchor_head, anchor_tail)

        source_pairs = []
        half_source_gap = 900 * AREA_SCALE * AREA_SCALE
        for record in range(RECORDS):
            parameter = 17 + 9 * record
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
                        subtract(add(source_sum, translation), target_endpoint),
                    )
                )
                role_sources.append(source)
            source_pairs.append((role_sources[0], role_sources[1]))

        assert len(points) == final_count - FILLER_PRIME
        if len(points) != len(set(points)):
            continue
        try:
            pair_tables(points)
        except ValueError:
            continue
        return (
            points,
            first_anchor,
            translation,
            source_pairs,
            horizontal_count,
            attempt,
        )
    raise AssertionError("scaled planted search exhausted")


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
        filler = [add(point, filler_translation) for point in scaled_filler]
        points = plant_points + filler
        if len(points) != len(set(points)):
            continue
        try:
            pair_sums, distances = pair_tables(points)
        except ValueError:
            continue
        return (
            points,
            pair_sums,
            distances,
            plant,
            filler_base,
            scale,
            offset,
            filler_translation,
        )
    raise AssertionError("scaled plant/filler union search exhausted")


def fibre_at(
    points: list[Point],
    pair_sums: dict[Point, tuple[int, int]],
    anchor_by_translation: dict[Point, tuple[int, int]],
    translation: Point,
) -> list[Point]:
    head, tail = anchor_by_translation[translation]
    return [
        start
        for start, source in pair_sums.items()
        if (target := pair_sums.get(add(start, translation))) is not None
        and len({head, tail, *source, *target}) == 6
    ]


def common_clean_anchors(
    points: list[Point],
    pair_sums: dict[Point, tuple[int, int]],
    starts: tuple[Point, Point],
) -> list[tuple[int, int]]:
    answer = []
    for head, tail in permutations(range(len(points)), 2):
        translation = subtract(points[head], points[tail])
        if all(
            (target := pair_sums.get(add(start, translation))) is not None
            and len({head, tail, *pair_sums[start], *target}) == 6
            for start in starts
        ):
            answer.append((head, tail))
    return answer


def triples_with_sum(points: list[Point], total: Point) -> set[tuple[int, int, int]]:
    point_index = {point: index for index, point in enumerate(points)}
    triples = set()
    for first, second in combinations(range(len(points)), 2):
        required = (
            total[0] - points[first][0] - points[second][0],
            total[1] - points[first][1] - points[second][1],
        )
        third = point_index.get(required)
        if third is not None and third != first and third != second:
            triples.add(tuple(sorted((first, second, third))))
    return triples


def companion_set(
    points: list[Point], total: Point, distinguished: int
) -> tuple[set[int], set[tuple[int, int, int]]]:
    triples = triples_with_sum(points, total)
    through = [triple for triple in triples if distinguished in triple]
    assert len(through) == 1
    companions = set().union(
        *(set(triple) for triple in triples if distinguished not in triple)
    )
    return companions, triples


def certificate() -> tuple[int, ...]:
    (
        points,
        pair_sums,
        distances,
        plant,
        filler_base,
        filler_scale,
        filler_offset,
        filler_translation,
    ) = build_union()
    (
        _,
        first_anchor,
        planted_translation,
        source_pairs,
        horizontal_count,
        plant_attempt,
    ) = plant

    k = len(points)
    edge_count = len(distances)
    assert k == 170
    assert edge_count == k * (k - 1) // 2

    anchor_by_translation = {
        subtract(points[head], points[tail]): (head, tail)
        for head in range(k)
        for tail in range(k)
        if head != tail
    }
    assert len(anchor_by_translation) == k * (k - 1)

    planted_fibre = fibre_at(
        points, pair_sums, anchor_by_translation, planted_translation
    )
    assert len(planted_fibre) == 2 * RECORDS

    source_starts = []
    for source_pair in source_pairs:
        starts = tuple(
            add(points[first], points[second]) for first, second in source_pair
        )
        source_starts.append(starts)
        assert set(starts) <= set(planted_fibre)
        assert common_clean_anchors(points, pair_sums, starts) == [
            (first_anchor, first_anchor + 1)
        ]
    assert set(sum(source_starts, ())) == set(planted_fibre)

    # The companion sets of all starts are a literal singleton sunflower.
    all_companions = []
    anchor_head = first_anchor
    anchor_tail = first_anchor + 1
    for starts in source_starts:
        record_companions = []
        for start in starts:
            total = add(start, points[anchor_head])
            companions, triples = companion_set(points, total, anchor_head)
            assert all(
                set(first).isdisjoint(second)
                for first, second in combinations(triples, 2)
            )
            assert anchor_tail in companions
            record_companions.append(companions)
            all_companions.append(companions)
        assert record_companions[0] & record_companions[1] == {anchor_tail}
    assert all(
        first & second == {anchor_tail}
        for first, second in combinations(all_companions, 2)
    )

    edges = edge_data(points)
    edge_by_label = {label: (endpoints, vector) for label, endpoints, vector in edges}
    edge_by_endpoints = {
        endpoints: (label, vector) for label, endpoints, vector in edges
    }
    all_labels = set(edge_by_label)
    assert sum(label - SOURCE_GAP in all_labels for label in all_labels) == RECORDS
    assert sum(label - TARGET_GAP in all_labels for label in all_labels) == k + 1

    # Exactly four selected source pairs occur in the planted clean fibre.
    selected_pairs = []
    for first_start in planted_fibre:
        first_edge = tuple(pair_sums[first_start])
        first_label = edge_by_endpoints[first_edge][0]
        for second_start in planted_fibre:
            if first_start == second_start:
                continue
            second_edge = tuple(pair_sums[second_start])
            second_label = edge_by_endpoints[second_edge][0]
            if first_label - second_label == SOURCE_GAP:
                selected_pairs.append((first_start, second_start))
    assert set(selected_pairs) == set(source_starts)

    source_areas = []
    for high_edge, low_edge in source_pairs:
        high_label, high_vector = edge_by_endpoints[high_edge]
        low_label, low_vector = edge_by_endpoints[low_edge]
        assert high_label - low_label == SOURCE_GAP
        source_areas.append(2 * determinant(high_vector, low_vector))
    assert source_areas == [-217730, -217694, -217658, -217622]
    assert len({area % 36 for area in source_areas}) == 1

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
    normalized_target_areas = {area // 2 for area in target_areas}
    assert all(area % (AREA_SCALE * AREA_SCALE) == 0 for area in normalized_target_areas)

    # Check the physical two-edge wedge whose two partners use TARGET_GAP.
    origin = horizontal_count + TARGET_VERTICAL_MARKS.index(0)
    vertical_ten = horizontal_count + TARGET_VERTICAL_MARKS.index(10)
    fixed_edges = (
        tuple(sorted((origin, 0))),
        tuple(sorted((origin, 1))),
    )
    partner_edges = (
        tuple(sorted((vertical_ten, 0))),
        tuple(sorted((vertical_ten, 1))),
    )
    assert (
        edge_by_endpoints[fixed_edges[0]][0]
        - edge_by_endpoints[fixed_edges[1]][0]
        == edge_by_endpoints[partner_edges[0]][0]
        - edge_by_endpoints[partner_edges[1]][0]
    )
    for fixed, partner in zip(fixed_edges, partner_edges):
        assert edge_by_endpoints[fixed][0] - edge_by_endpoints[partner][0] == TARGET_GAP
        assert abs(
            2
            * determinant(
                edge_by_endpoints[fixed][1], edge_by_endpoints[partner][1]
            )
        ) > edge_count

    residue = source_areas[0] % 36
    shifts = [(area - residue) // 36 for area in source_areas]
    assert [shift - shifts[0] for shift in shifts] == list(range(RECORDS))
    supports = [
        {shift + area for area in normalized_target_areas} for shift in shifts
    ]
    assert all(len(support) == k for support in supports)
    assert all(
        first.isdisjoint(second)
        for first, second in combinations(supports, 2)
    )

    # Construct the actual adaptive denominator from transported filler
    # translations, stopping at the first crossing of 4k^2.
    filler_fibres = clean_start_fibres(filler_base)
    transported = sorted(
        (
            ((filler_scale * q[0], filler_scale * q[1]), len(starts))
            for q, starts in filler_fibres.items()
        ),
        key=lambda item: (-item[1], item[0]),
    )
    fibre_mass = len(planted_fibre)
    selected_filler_translations = 0
    for translation, _ in transported:
        if translation == planted_translation:
            continue
        fibre_mass += len(
            fibre_at(points, pair_sums, anchor_by_translation, translation)
        )
        selected_filler_translations += 1
        if fibre_mass >= 4 * k * k:
            break
    assert 4 * k * k <= fibre_mass < 4 * k * k + edge_count

    quota = ceil(k * k * len(planted_fibre) / fibre_mass)
    assert quota == 2
    tail_count = RECORDS - quota
    x_36 = tail_count * len(target_areas)
    assert x_36 == 340

    # Loads are tied, so every possible top/tail split has zero support
    # intersection, not just one chosen ordering.
    assert all(
        sum(len(supports[top] & supports[tail]) for top in top_indices) == 0
        for top_indices in combinations(range(RECORDS), quota)
        for tail in set(range(RECORDS)) - set(top_indices)
    )

    profile = (
        plant_attempt,
        filler_scale,
        filler_offset,
        k,
        edge_count,
        len(planted_fibre),
        len(target_areas),
        len(filler_fibres),
        sum(map(len, filler_fibres.values())),
        selected_filler_translations,
        fibre_mass,
        quota,
        tail_count,
        x_36,
        residue,
        min(source_areas),
        max(source_areas),
        max(max(abs(x), abs(y)) for x, y in points),
    )
    expected = (
        1,
        1,
        0,
        170,
        14365,
        8,
        170,
        2162,
        300798,
        615,
        115680,
        2,
        2,
        340,
        34,
        -217730,
        -217622,
        10000000000000000000010131534,
    )
    assert profile == expected, profile
    return profile


def main() -> None:
    profile = certificate()
    print("global disjoint-translate saturation", profile)
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
