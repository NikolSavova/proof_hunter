#!/usr/bin/env python3
"""Endpoint wedge amplification for determinant-qualified rich norm gaps."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_metric_scalar_gap_codegree_barrier import perpendicular_gap_family
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
EdgeDatum = tuple[int, tuple[int, int], Point]


def edge_data(points: list[Point]) -> list[EdgeDatum]:
    output: list[EdgeDatum] = []
    for first, second in combinations(range(len(points)), 2):
        vector = (
            points[first][0] - points[second][0],
            points[first][1] - points[second][1],
        )
        output.append((
            vector[0] * vector[0] + vector[1] * vector[1],
            (first, second),
            vector,
        ))
    assert len({datum[0] for datum in output}) == len(output)
    return output


def determinant(left: Point, right: Point) -> int:
    return left[0] * right[1] - left[1] * right[0]


def wedge_count(edge_indices: list[int], edges: list[EdgeDatum]) -> tuple[int, int]:
    degree = Counter(
        vertex
        for edge_index in edge_indices
        for vertex in edges[edge_index][1]
    )
    return (
        sum(value * (value - 1) // 2 for value in degree.values()),
        max(degree.values(), default=0),
    )


def endpoint_profile(points: list[Point]) -> tuple[int, ...]:
    k = len(points)
    edges = edge_data(points)
    gap_loads: Counter[int] = Counter()
    first_edges: dict[int, list[int]] = defaultdict(list)
    records: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for first, first_data in enumerate(edges):
        for second, second_data in enumerate(edges):
            gap = first_data[0] - second_data[0]
            gap_loads[gap] += 1
            if gap:
                first_edges[gap].append(first)
                records[gap].append((first, second))

    total_wedges = 0
    lower_numerator = 0
    best = (0, 0, 0, 0)
    for gap, indices in first_edges.items():
        wedges, maximum_degree = wedge_count(indices, edges)
        total_wedges += wedges
        load = len(indices)
        lower_numerator += max(0, 2 * load * load - k * load)
        if load > best[0]:
            best = (load, gap, wedges, maximum_degree)

    complete_wedges = 0
    exact_lift = 0
    incident: dict[int, list[int]] = defaultdict(list)
    for edge_index, (_, endpoints, _) in enumerate(edges):
        for endpoint in endpoints:
            incident[endpoint].append(edge_index)
    for edge_indices in incident.values():
        for first, second in combinations(edge_indices, 2):
            complete_wedges += 1
            exact_lift += gap_loads[edges[first][0] - edges[second][0]] - 1
    assert total_wedges == exact_lift
    assert k * total_wedges >= lower_numerator
    assert complete_wedges == k * (k - 1) * (k - 2) // 2

    # The maximally rich gap has a simultaneous matching on both target
    # edge roles.  Greedy is enough for the universal 4k-7 denominator.
    rich_load, rich_gap, _, _ = best
    used_first: set[int] = set()
    used_second: set[int] = set()
    double_matching = 0
    for first, second in records[rich_gap]:
        if (
            set(edges[first][1]).isdisjoint(used_first)
            and set(edges[second][1]).isdisjoint(used_second)
        ):
            used_first.update(edges[first][1])
            used_second.update(edges[second][1])
            double_matching += 1
    assert double_matching * (4 * k - 7) >= rich_load

    # Check the same wedge lower bound after determinant truncation.
    for cutoff in (0, len(edges) // k, len(edges)):
        high_first: dict[int, list[int]] = defaultdict(list)
        for gap, pairs in records.items():
            for first, second in pairs:
                doubled_area = abs(2 * determinant(edges[first][2], edges[second][2]))
                if doubled_area > cutoff:
                    high_first[gap].append(first)
        high_wedges = 0
        high_lower_numerator = 0
        for indices in high_first.values():
            wedges, _ = wedge_count(indices, edges)
            high_wedges += wedges
            load = len(indices)
            high_lower_numerator += max(0, 2 * load * load - k * load)
        assert high_wedges <= total_wedges
        assert k * high_wedges >= high_lower_numerator

    return (
        k,
        len(edges),
        *best,
        total_wedges,
        lower_numerator,
        complete_wedges,
        double_matching,
    )


def closure_weighted_tail() -> tuple[tuple[int, int, int], ...]:
    points = POINTS[:40]
    labels: dict[Point, int] = {}
    distance_values: list[int] = []
    for first, second in combinations(points, 2):
        pair_sum = (first[0] + second[0], first[1] + second[1])
        value = (first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2
        labels[pair_sum] = value
        distance_values.append(value)
    gap_loads = Counter(
        first - second
        for first in distance_values
        for second in distance_values
    )
    source_loads: Counter[int] = Counter()
    for starts in clean_start_fibres(points).values():
        values = [labels[start] for start in starts]
        source_loads.update(first - second for first in values for second in values)

    output = []
    for threshold in (20, 40, 60, 80, 90, 100):
        rich_gaps = [
            gap for gap, load in gap_loads.items()
            if gap and load >= threshold
        ]
        output.append((
            threshold,
            len(rich_gaps),
            sum(source_loads[-18 * gap] for gap in rich_gaps),
        ))
    return tuple(output)


def main() -> None:
    expected = {
        "closure-20": (20, 190, 35, 48, 108, 6,
                       35_495, 244_076, 3_420, 6),
        "Costas-22": (22, 231, 19, -1_035, 37, 5,
                      13_808, 7_344, 4_620, 5),
        "parabola-43": (43, 903, 11, 189_216, 6, 3,
                        22_946, 0, 37_023, 4),
        "ruler-40": (40, 780, 24, -124_200, 234, 22,
                     161_576, 18_472, 29_640, 2),
        "quadratic-gap-32": (
            32, 496, 128, 505_447_028_499_293_771, 1_408, 16,
            86_444, 114_688, 14_880, 8,
        ),
    }
    families = [
        ("closure-20", POINTS[:20]),
        ("Costas-22", transformed_costas(23)),
        ("parabola-43", transformed_parabola_43()),
        ("ruler-40", ruler_points()),
        ("quadratic-gap-32", perpendicular_gap_family(8)[0]),
    ]
    for name, points in families:
        actual = endpoint_profile(points)
        assert actual == expected[name], (name, actual, expected[name])
        print(name, actual)

    tail = closure_weighted_tail()
    assert tail == (
        (20, 8_958, 7_374),
        (40, 1_612, 4_046),
        (60, 260, 1_454),
        (80, 30, 240),
        (90, 10, 70),
        (100, 2, 12),
    ), tail
    print("closure weighted tail", tail)
    print("metric scalar endpoint rich tail: PASS")


if __name__ == "__main__":
    main()
