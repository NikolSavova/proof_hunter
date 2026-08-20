#!/usr/bin/env python3
"""Exact audit of the isolated common-q matching/rank survivor."""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from itertools import combinations

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_metric_scalar_endpoint_rich_tail import determinant, edge_data
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]


def add(first: Point, second: Point) -> Point:
    return first[0] + second[0], first[1] + second[1]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def endpoint_sum(points: list[Point], endpoints: tuple[int, int]) -> Point:
    return add(points[endpoints[0]], points[endpoints[1]])


def profile(points: list[Point]) -> tuple[int, ...]:
    k = len(points)
    edges = edge_data(points)
    edge_count = len(edges)
    cutoff = edge_count // k

    pair_sums = [endpoint_sum(points, edge[1]) for edge in edges]
    pair_sum_to_edge = {pair_sum: index for index, pair_sum in enumerate(pair_sums)}
    assert len(pair_sum_to_edge) == edge_count

    fibres = clean_start_fibres(points)
    indexed_fibres = {
        q: {pair_sum_to_edge[start] for start in starts}
        for q, starts in fibres.items()
    }
    fibre_mass = sum(map(len, indexed_fibres.values()))

    pair_translations: dict[tuple[int, int], list[Point]] = defaultdict(list)
    for q, starts in indexed_fibres.items():
        for first, second in combinations(starts, 2):
            pair_translations[tuple(sorted((first, second)))].append(q)

    source_weight: Counter[int] = Counter()
    source_pairs_by_gap: dict[
        int, list[tuple[tuple[int, int], list[Point]]]
    ] = defaultdict(list)
    for (first, second), translations in pair_translations.items():
        if len(translations) >= k:
            continue
        source_gap = edges[first][0] - edges[second][0]
        if source_gap and source_gap % 18 == 0:
            target_gap = -source_gap // 18
            source_weight[target_gap] += len(translations)
            source_pairs_by_gap[target_gap].append(((first, second), translations))
            source_weight[-target_gap] += len(translations)
            source_pairs_by_gap[-target_gap].append(((second, first), translations))

    target_load: Counter[int] = Counter()
    endpoint_records: dict[tuple[int, int], list[int]] = defaultdict(list)
    for first_index, first in enumerate(edges):
        for second in edges:
            gap = first[0] - second[0]
            if not gap or abs(2 * determinant(first[2], second[2])) <= cutoff:
                continue
            target_load[gap] += 1
            for endpoint in first[1]:
                endpoint_records[gap, endpoint].append(first_index)

    fixed_weights: Counter[tuple[int, int, int]] = Counter()
    fixed_gaps: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for (gap, endpoint), first_edges in endpoint_records.items():
        if target_load[gap] < k or not source_weight[gap]:
            continue
        for first, second in combinations(first_edges, 2):
            wedge = endpoint, *sorted((first, second))
            fixed_weights[wedge] += source_weight[gap]
            fixed_gaps[wedge].append(gap)

    maximizing_wedge, fixed_weight = max(fixed_weights.items(), key=lambda item: item[1])
    selected_gaps = set(fixed_gaps[maximizing_wedge])
    assert len(selected_gaps) == len(fixed_gaps[maximizing_wedge])

    directed_anchor = {
        subtract(points[head], points[tail]): (head, tail)
        for head in range(k)
        for tail in range(k)
        if head != tail
    }
    assert len(directed_anchor) == k * (k - 1)

    isolated_mass = 0
    path_components = 0
    cycle_components = 0
    singleton_path_mass = 0
    longest_component = 0
    disjoint_target_checks = 0
    affine_row_checks = 0
    rich_lift = 0

    for gap in selected_gaps:
        assert target_load[gap] >= k
        for (first, second), translations in source_pairs_by_gap[gap]:
            assert edges[first][0] - edges[second][0] == -18 * gap
            anchors = {q: directed_anchor[q] for q in translations}
            head_degree = Counter(head for head, _ in anchors.values())
            tail_degree = Counter(tail for _, tail in anchors.values())
            isolated = {
                q: (head, tail)
                for q, (head, tail) in anchors.items()
                if head_degree[head] == 1 and tail_degree[tail] == 1
            }
            isolated_mass += len(isolated)
            rich_lift += len(isolated) * target_load[gap]

            # The isolated-anchor subgraph has indegree and outdegree at most
            # one, hence every weak component is a directed path or cycle.
            incoming = Counter(head for head, _ in isolated.values())
            outgoing = Counter(tail for _, tail in isolated.values())
            assert max(incoming.values(), default=0) <= 1
            assert max(outgoing.values(), default=0) <= 1
            adjacency: dict[int, set[int]] = defaultdict(set)
            for head, tail in isolated.values():
                adjacency[head].add(tail)
                adjacency[tail].add(head)
            unseen = set(adjacency)
            while unseen:
                start = next(iter(unseen))
                queue = deque([start])
                vertices: set[int] = set()
                while queue:
                    vertex = queue.popleft()
                    if vertex in vertices:
                        continue
                    vertices.add(vertex)
                    queue.extend(adjacency[vertex] - vertices)
                unseen -= vertices
                component_edges = sum(
                    head in vertices and tail in vertices
                    for head, tail in isolated.values()
                )
                longest_component = max(longest_component, component_edges)
                if all(incoming[v] == outgoing[v] == 1 for v in vertices):
                    assert component_edges == len(vertices)
                    cycle_components += 1
                else:
                    assert component_edges == len(vertices) - 1
                    path_components += 1
                    if component_edges == 1:
                        singleton_path_mass += 1

            for q, (head, tail) in isolated.items():
                target_first = pair_sum_to_edge[add(pair_sums[first], q)]
                target_second = pair_sum_to_edge[add(pair_sums[second], q)]
                assert target_first != target_second
                first_endpoints = edges[first][1]
                second_endpoints = edges[second][1]
                target_first_endpoints = edges[target_first][1]
                target_second_endpoints = edges[target_second][1]

                # The clean row equations and six-distinctness.
                for source_endpoints, target_endpoints in (
                    (first_endpoints, target_first_endpoints),
                    (second_endpoints, target_second_endpoints),
                ):
                    assert add(points[head], endpoint_sum(points, source_endpoints)) == add(
                        points[tail], endpoint_sum(points, target_endpoints)
                    )
                    assert {head, *source_endpoints}.isdisjoint({tail, *target_endpoints})

                # If these target edges met at x, rotating the distinguished
                # right endpoint from tail to x would put head-x in Q_p and
                # give the anchor head a second outgoing occurrence.
                assert set(target_first_endpoints).isdisjoint(target_second_endpoints)
                disjoint_target_checks += 1

                # Difference of the two common-translation rows annihilates
                # the constant and both coordinate columns exactly.
                coefficients: Counter[int] = Counter()
                coefficients.update(target_first_endpoints)
                coefficients.subtract(first_endpoints)
                coefficients.subtract(target_second_endpoints)
                coefficients.update(second_endpoints)
                assert sum(coefficients.values()) == 0
                for coordinate in (0, 1):
                    assert sum(
                        coefficient * points[vertex][coordinate]
                        for vertex, coefficient in coefficients.items()
                    ) == 0
                affine_row_checks += 1

    assert isolated_mass <= fixed_weight
    assert disjoint_target_checks == isolated_mass
    assert affine_row_checks == isolated_mass
    assert rich_lift >= k * isolated_mass

    return (
        k,
        fibre_mass,
        fixed_weight,
        isolated_mass,
        len(selected_gaps),
        path_components,
        cycle_components,
        singleton_path_mass,
        longest_component,
        disjoint_target_checks,
        rich_lift,
        *maximizing_wedge,
    )


def main() -> None:
    # Keeping these values literal turns later changes in any definition into
    # a visible failure.
    expected = {
        20: (20, 648, 10, 8, 4, 8, 0, 8, 1, 8, 166, 10, 60, 153),
        30: (30, 3_816, 69, 57, 17, 57, 0, 57, 1, 57, 2_535, 17, 16, 232),
        40: (
            40, 12_420, 312, 224, 27, 222, 0, 220, 2, 224, 13_919,
            17, 16, 322,
        ),
        50: (
            50, 26_532, 662, 523, 43, 520, 0, 517, 2, 523, 43_829,
            12, 241, 326,
        ),
    }
    for size in (20, 30, 40, 50):
        actual = profile(POINTS[:size])
        assert actual == expected[size], (size, actual, expected[size])
        print(f"closure-{size}", actual)
    print("low-band isolated matching/rank barrier: PASS")


if __name__ == "__main__":
    main()
