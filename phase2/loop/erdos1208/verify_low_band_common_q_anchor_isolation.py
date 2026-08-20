#!/usr/bin/env python3
"""Anchor-isolation split for exact common-q fixed-wedge weights."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_metric_scalar_endpoint_rich_tail import determinant, edge_data
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def anchor_isolation_profile(points: list[Point]) -> tuple[int, ...]:
    point_count = len(points)
    edges = edge_data(points)
    edge_count = len(edges)
    cutoff = edge_count // point_count
    pair_sum_to_edge: dict[Point, int] = {}
    for edge_index, (_, (first, second), _) in enumerate(edges):
        pair_sum = (
            points[first][0] + points[second][0],
            points[first][1] + points[second][1],
        )
        assert pair_sum not in pair_sum_to_edge
        pair_sum_to_edge[pair_sum] = edge_index

    fibres = clean_start_fibres(points)
    indexed_fibres = {
        difference: {pair_sum_to_edge[start] for start in starts}
        for difference, starts in fibres.items()
    }
    fibre_mass = sum(len(starts) for starts in indexed_fibres.values())
    pair_translations: dict[tuple[int, int], list[Point]] = defaultdict(list)
    for difference, starts in indexed_fibres.items():
        for first, second in combinations(starts, 2):
            pair_translations[tuple(sorted((first, second)))].append(difference)

    source_weight: Counter[int] = Counter()
    source_pairs_by_gap: dict[
        int, list[tuple[tuple[int, int], list[Point]]]
    ] = defaultdict(list)
    for (first, second), translations in pair_translations.items():
        if len(translations) >= point_count:
            continue
        source_gap = edges[first][0] - edges[second][0]
        if source_gap and source_gap % 18 == 0:
            target_gap = -source_gap // 18
            source_weight[target_gap] += len(translations)
            source_pairs_by_gap[target_gap].append(
                ((first, second), translations)
            )
            source_weight[-target_gap] += len(translations)
            source_pairs_by_gap[-target_gap].append(
                ((second, first), translations)
            )

    target_load: Counter[int] = Counter()
    endpoint_records: dict[tuple[int, int], list[int]] = defaultdict(list)
    for first_index, first in enumerate(edges):
        for second in edges:
            target_gap = first[0] - second[0]
            if not target_gap:
                continue
            if abs(2 * determinant(first[2], second[2])) <= cutoff:
                continue
            target_load[target_gap] += 1
            for endpoint in first[1]:
                endpoint_records[target_gap, endpoint].append(first_index)

    rich_fixed_weights: Counter[tuple[int, int, int]] = Counter()
    rich_fixed_gaps: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for (target_gap, endpoint), first_edges in endpoint_records.items():
        if target_load[target_gap] < point_count or not source_weight[target_gap]:
            continue
        for first, second in combinations(first_edges, 2):
            physical_wedge = endpoint, *sorted((first, second))
            rich_fixed_weights[physical_wedge] += source_weight[target_gap]
            rich_fixed_gaps[physical_wedge].append(target_gap)

    maximizing_wedge, maximum_weight = max(
        rich_fixed_weights.items(), key=lambda item: item[1]
    )
    selected_gaps = set(rich_fixed_gaps[maximizing_wedge])

    directed_anchor = {
        subtract(points[first], points[second]): (first, second)
        for first in range(point_count)
        for second in range(point_count)
        if first != second
    }
    isolated_mass = 0
    remainder_mass = 0
    shared_head_wedges = 0
    shared_tail_wedges = 0
    literal_matching_mass = 0
    cross_only_mass = 0
    head_or_tail_mass = 0
    selected_pair_count = 0
    for target_gap in selected_gaps:
        for _, translations in source_pairs_by_gap[target_gap]:
            selected_pair_count += 1
            anchor_edges = [directed_anchor[q] for q in translations]
            head_degree = Counter(first for first, _ in anchor_edges)
            tail_degree = Counter(second for _, second in anchor_edges)
            endpoint_degree = Counter(
                endpoint for anchor_edge in anchor_edges for endpoint in anchor_edge
            )
            isolated = sum(
                head_degree[first] == 1 and tail_degree[second] == 1
                for first, second in anchor_edges
            )
            head_wedges = sum(
                degree * (degree - 1) // 2 for degree in head_degree.values()
            )
            tail_wedges = sum(
                degree * (degree - 1) // 2 for degree in tail_degree.values()
            )
            codegree = len(translations)
            isolated_mass += isolated
            remainder_mass += codegree - isolated
            shared_head_wedges += head_wedges
            shared_tail_wedges += tail_wedges
            if all(degree == 1 for degree in endpoint_degree.values()):
                literal_matching_mass += codegree
            elif head_wedges + tail_wedges == 0:
                cross_only_mass += codegree
            else:
                head_or_tail_mass += codegree

    assert maximum_weight == isolated_mass + remainder_mass
    assert remainder_mass <= 2 * (shared_head_wedges + shared_tail_wedges)

    # Independently switch the selected shared-head and shared-tail masses
    # into pairs of starts in fibre intersections.
    def selected(first: int, second: int) -> bool:
        source_gap = edges[first][0] - edges[second][0]
        return (
            bool(source_gap)
            and source_gap % 18 == 0
            and -source_gap // 18 in selected_gaps
            and len(pair_translations.get(tuple(sorted((first, second))), ()))
            < point_count
        )

    switched_head = 0
    switched_tail = 0
    for common in range(point_count):
        others = [vertex for vertex in range(point_count) if vertex != common]
        for first_other, second_other in combinations(others, 2):
            first_head_q = subtract(points[common], points[first_other])
            second_head_q = subtract(points[common], points[second_other])
            head_intersection = indexed_fibres.get(first_head_q, set()) & indexed_fibres.get(
                second_head_q, set()
            )
            for first, second in combinations(head_intersection, 2):
                switched_head += selected(first, second) + selected(second, first)

            first_tail_q = subtract(points[first_other], points[common])
            second_tail_q = subtract(points[second_other], points[common])
            tail_intersection = indexed_fibres.get(first_tail_q, set()) & indexed_fibres.get(
                second_tail_q, set()
            )
            for first, second in combinations(tail_intersection, 2):
                switched_tail += selected(first, second) + selected(second, first)

    assert switched_head == shared_head_wedges
    assert switched_tail == shared_tail_wedges

    return (
        point_count,
        fibre_mass,
        maximum_weight,
        len(selected_gaps),
        selected_pair_count,
        isolated_mass,
        remainder_mass,
        shared_head_wedges,
        shared_tail_wedges,
        literal_matching_mass,
        cross_only_mass,
        head_or_tail_mass,
        *maximizing_wedge,
    )


def main() -> None:
    expected = {
        20: (20, 648, 10, 4, 9, 8, 2, 1, 0, 8, 0, 2, 10, 60, 153),
        30: (30, 3_816, 69, 17, 57, 57, 12, 6, 0, 56, 0, 13, 17, 16, 232),
        40: (
            40, 12_420, 312, 27, 226, 224, 88, 44, 0, 210, 5, 97,
            17, 16, 322,
        ),
        50: (
            50, 26_532, 662, 43, 477, 523, 139, 72, 2, 496, 7, 159,
            12, 241, 326,
        ),
    }
    for size, wanted in expected.items():
        actual = anchor_isolation_profile(POINTS[:size])
        assert actual == wanted, (size, actual, wanted)
        print(f"closure-{size}", actual)
    print("low-band common-q anchor isolation: PASS")


if __name__ == "__main__":
    main()
