#!/usr/bin/env python3
"""Exact common-q low-codegree wedge decomposition on closure prefixes."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_low_band_fixed_wedge_rich_pencil_counterexample import (
    perpendicular_rich_candidate,
)
from verify_metric_scalar_endpoint_rich_tail import determinant, edge_data
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]


def common_q_wedge_profile(points: list[Point]) -> tuple[int, ...]:
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
    fibre_mass = sum(len(starts) for starts in fibres.values())
    source_pair_mass = sum(
        len(starts) * (len(starts) - 1) for starts in fibres.values()
    )
    source_codegree: Counter[tuple[int, int]] = Counter()
    indexed_fibres: list[list[int]] = []
    for starts in fibres.values():
        indexed = [pair_sum_to_edge[start] for start in starts]
        indexed_fibres.append(indexed)
        for first, second in combinations(indexed, 2):
            source_codegree[tuple(sorted((first, second)))] += 1

    low_source_weight: Counter[int] = Counter()
    determinant_cells: Counter[tuple[int, int]] = Counter()
    for (first, second), codegree in source_codegree.items():
        if codegree >= point_count:
            continue
        source_gap = edges[first][0] - edges[second][0]
        if source_gap and source_gap % 18 == 0:
            target_gap = -source_gap // 18
            doubled_area = 2 * determinant(edges[first][2], edges[second][2])
            low_source_weight[target_gap] += codegree
            determinant_cells[target_gap, doubled_area] += codegree
            low_source_weight[-target_gap] += codegree
            determinant_cells[-target_gap, -doubled_area] += codegree

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

    target_wedges: Counter[int] = Counter()
    fixed_wedge_weight: Counter[tuple[int, int, int]] = Counter()
    rich_fixed_wedge_weight: Counter[tuple[int, int, int]] = Counter()
    for (target_gap, endpoint), first_edges in endpoint_records.items():
        assert len(first_edges) == len(set(first_edges))
        for first, second in combinations(first_edges, 2):
            target_wedges[target_gap] += 1
            physical_wedge = endpoint, *sorted((first, second))
            weight = low_source_weight[target_gap]
            if weight:
                fixed_wedge_weight[physical_wedge] += weight
                if target_load[target_gap] >= point_count:
                    rich_fixed_wedge_weight[physical_wedge] += weight

    collapsed_wedge_mass = sum(
        source_weight * target_wedges[target_gap]
        for target_gap, source_weight in low_source_weight.items()
    )
    rich_collapsed_wedge_mass = sum(
        source_weight * target_wedges[target_gap]
        for target_gap, source_weight in low_source_weight.items()
        if target_load[target_gap] >= point_count
    )
    determinant_decomposed_mass = sum(
        source_weight * target_wedges[target_gap]
        for (target_gap, _), source_weight in determinant_cells.items()
    )

    # Expand once more over the actual common translation q.  Each occurrence
    # of a source pair in a fibre contributes one copy of the same wedge load.
    common_q_wedge_mass = 0
    rich_common_q_wedge_mass = 0
    for indexed in indexed_fibres:
        for first, second in combinations(indexed, 2):
            codegree = source_codegree[tuple(sorted((first, second)))]
            if codegree >= point_count:
                continue
            for left, right in ((first, second), (second, first)):
                source_gap = edges[left][0] - edges[right][0]
                if not source_gap or source_gap % 18:
                    continue
                target_gap = -source_gap // 18
                common_q_wedge_mass += target_wedges[target_gap]
                if target_load[target_gap] >= point_count:
                    rich_common_q_wedge_mass += target_wedges[target_gap]

    assert collapsed_wedge_mass == common_q_wedge_mass
    assert rich_collapsed_wedge_mass == rich_common_q_wedge_mass
    assert determinant_decomposed_mass == collapsed_wedge_mass
    assert sum(fixed_wedge_weight.values()) == collapsed_wedge_mass
    assert (
        sum(rich_fixed_wedge_weight.values())
        == rich_collapsed_wedge_mass
    )

    rich_source_mass = sum(
        source_weight
        for target_gap, source_weight in low_source_weight.items()
        if target_load[target_gap] >= point_count
    )
    required_wedge_scale = edge_count * (fibre_mass + point_count**3)

    return (
        point_count,
        edge_count,
        cutoff,
        len(fibres),
        fibre_mass,
        source_pair_mass,
        len(source_codegree),
        max(source_codegree.values(), default=0),
        len(low_source_weight),
        sum(low_source_weight.values()),
        rich_source_mass,
        len(determinant_cells),
        max(determinant_cells.values(), default=0),
        collapsed_wedge_mass,
        rich_collapsed_wedge_mass,
        max(fixed_wedge_weight.values(), default=0),
        max(rich_fixed_wedge_weight.values(), default=0),
        required_wedge_scale,
    )


def main() -> None:
    expected = {
        20: (
            20, 190, 9, 312, 648, 1_072, 469, 4, 58, 80, 38, 70, 2,
            2_852, 2_409, 10, 10, 1_643_120,
        ),
        30: (
            30, 435, 14, 828, 3_816, 19_448, 7_980, 6, 616, 1_306,
            548, 1_088, 6, 86_553, 67_083, 83, 69, 13_404_960,
        ),
        40: (
            40, 780, 19, 1_518, 12_420, 120_456, 45_865, 12, 2_300,
            8_654, 3_940, 6_596, 9, 880_682, 709_530, 336, 312,
            59_607_600,
        ),
        50: (
            50, 1_225, 24, 2_420, 26_532, 353_008, 131_785, 14,
            5_568, 25_558, 11_524, 19_072, 11, 3_381_191, 2_761_895,
            712, 662, 185_626_700,
        ),
    }
    for size, wanted in expected.items():
        actual = common_q_wedge_profile(POINTS[:size])
        assert actual == wanted, (size, actual, wanted)
        print(f"closure-{size}", actual)

    perpendicular_points, *_ = perpendicular_rich_candidate(3)
    perpendicular = common_q_wedge_profile(perpendicular_points)
    expected_perpendicular = (
        34, 561, 16, 500, 4_086, 46_384, 8_741, 12, 1_900, 5_640, 0,
        1_900, 17, 1, 0, 1, 0, 24_341_790,
    )
    assert perpendicular == expected_perpendicular, (
        perpendicular,
        expected_perpendicular,
    )
    print("perpendicular-rich-pencil", perpendicular)
    print("low-band common-q wedge decomposition: PASS")


if __name__ == "__main__":
    main()
