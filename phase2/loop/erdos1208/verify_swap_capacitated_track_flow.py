#!/usr/bin/env python3
"""Verify the exact capacitated endpoint-track flow reduction."""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from itertools import combinations, product
from random import Random


Token = tuple[int, int]
Row = tuple[int, Token]


def maximum_flow(
    weights: list[int], neighbours: list[list[int]], capacities: list[int]
) -> int:
    left_count = len(weights)
    right_count = len(capacities)
    source = left_count + right_count
    sink = source + 1
    graph: list[list[list[int]]] = [[] for _ in range(sink + 1)]

    def add_edge(start: int, end: int, capacity: int) -> None:
        graph[start].append([end, capacity, len(graph[end])])
        graph[end].append([start, 0, len(graph[start]) - 1])

    for left, weight in enumerate(weights):
        add_edge(source, left, weight)
        for right in neighbours[left]:
            add_edge(left, left_count + right, weight)
    for right, capacity in enumerate(capacities):
        add_edge(left_count + right, sink, capacity)

    flow = 0
    while True:
        level = [-1] * len(graph)
        level[source] = 0
        queue = deque([source])
        while queue:
            vertex = queue.popleft()
            for end, capacity, _ in graph[vertex]:
                if capacity and level[end] < 0:
                    level[end] = level[vertex] + 1
                    queue.append(end)
        if level[sink] < 0:
            return flow
        cursor = [0] * len(graph)

        def push(vertex: int, amount: int) -> int:
            if vertex == sink:
                return amount
            while cursor[vertex] < len(graph[vertex]):
                edge = graph[vertex][cursor[vertex]]
                end, capacity, reverse = edge
                if capacity and level[end] == level[vertex] + 1:
                    sent = push(end, min(amount, capacity))
                    if sent:
                        edge[1] -= sent
                        graph[end][reverse][1] += sent
                        return sent
                cursor[vertex] += 1
            return 0

        while True:
            sent = push(source, sum(weights))
            if not sent:
                break
            flow += sent


def subset_deficiency(
    weights: list[int], neighbours: list[list[int]], capacities: list[int]
) -> int:
    best = 0
    for mask in range(1 << len(weights)):
        selected = [index for index in range(len(weights)) if mask >> index & 1]
        row_union = {
            row for occurrence in selected for row in neighbours[occurrence]
        }
        best = max(
            best,
            sum(weights[index] for index in selected)
            - sum(capacities[row] for row in row_union),
        )
    return best


def exhaustive_flow_identity() -> None:
    for left_count in range(1, 5):
        for right_count in range(1, 4):
            nonempty_masks = range(1, 1 << right_count)
            for masks in product(nonempty_masks, repeat=left_count):
                neighbours = [
                    [right for right in range(right_count) if mask >> right & 1]
                    for mask in masks
                ]
                # Two weight/capacity patterns suffice to exercise nonuniform
                # supply, shared rows, and zero residual capacity.
                for weights, capacities in (
                    ([1] * left_count, [1] * right_count),
                    (
                        [1 + index % 3 for index in range(left_count)],
                        [1 + (2 * index) % 3 for index in range(right_count)],
                    ),
                ):
                    flow = maximum_flow(weights, neighbours, capacities)
                    deficiency = subset_deficiency(weights, neighbours, capacities)
                    assert sum(weights) - flow == deficiency


def build_rows(
    k: int,
    occurrence_tokens: list[dict[int, set[Token]]],
) -> tuple[list[Row], list[int], list[list[int]]]:
    token_occurrences: Counter[Row] = Counter()
    endpoint_support: dict[int, set[Token]] = defaultdict(set)
    for token_map in occurrence_tokens:
        for endpoint, tokens in token_map.items():
            for token in tokens:
                token_occurrences[endpoint, token] += 1
                endpoint_support[endpoint].add(token)
    rows = sorted(token_occurrences)
    row_index = {row: index for index, row in enumerate(rows)}
    base_capacity = [
        len(endpoint_support[endpoint])
        - int(token_occurrences[endpoint, token] == 1)
        for endpoint, token in rows
    ]
    assert all(capacity >= 1 for capacity in base_capacity)
    neighbours = [
        sorted(
            row_index[endpoint, token]
            for endpoint, tokens in token_map.items()
            for token in tokens
        )
        for token_map in occurrence_tokens
    ]
    assert sum(base_capacity) <= sum(
        len(tokens) ** 2 for tokens in endpoint_support.values()
    )
    assert sum(base_capacity) <= 144 * k * (k - 1) ** 2
    return rows, base_capacity, neighbours


def deterministic_track_systems() -> None:
    # Many occurrences share one physical track.  Deficiency is real at L=1,
    # and the subset formula finds it exactly.
    occurrences = [
        {0: {(0, 1)}, 1: {(1, 0)}} for _ in range(7)
    ]
    _, capacities, neighbours = build_rows(3, occurrences)
    weights = [1] * len(occurrences)
    assert sum(weights) - maximum_flow(weights, neighbours, capacities) == 5
    assert subset_deficiency(weights, neighbours, capacities) == 5

    # Additional intrinsic tracks create enough capacity to route every copy.
    occurrences = [
        {
            0: {(0, 1), (2, index + 1)},
            1: {(1, 0)},
            2: {(3, index)},
        }
        for index in range(6)
    ]
    _, capacities, neighbours = build_rows(8, occurrences)
    weights = [3, 1, 4, 1, 5, 2]
    assert maximum_flow(weights, neighbours, capacities) == sum(weights)


def random_track_systems() -> None:
    rng = Random(1208202610)
    for k in range(3, 10):
        for _ in range(250):
            occurrence_count = rng.randrange(1, 8)
            occurrences: list[dict[int, set[Token]]] = []
            for _occurrence in range(occurrence_count):
                endpoint_count = rng.randrange(2, min(k, 5) + 1)
                endpoints = rng.sample(range(k), endpoint_count)
                token_map: dict[int, set[Token]] = {}
                for endpoint in endpoints:
                    token_count = rng.randrange(1, 4)
                    token_map[endpoint] = {
                        (rng.randrange(12), rng.randrange(k - 1))
                        for _ in range(token_count)
                    }
                occurrences.append(token_map)
            # Remove endpoints of degree one: the live construction only uses
            # high endpoints, and every retained occurrence must keep a row.
            endpoint_degree = Counter(
                endpoint for token_map in occurrences for endpoint in token_map
            )
            restricted = [
                {
                    endpoint: tokens
                    for endpoint, tokens in token_map.items()
                    if endpoint_degree[endpoint] >= 2
                }
                for token_map in occurrences
            ]
            retained = [token_map for token_map in restricted if token_map]
            if not retained:
                continue
            _, base_capacity, neighbours = build_rows(k, retained)
            weights = [rng.randrange(1, 7) for _ in retained]
            for cutoff in (1, 2, 4):
                capacities = [cutoff * capacity for capacity in base_capacity]
                flow = maximum_flow(weights, neighbours, capacities)
                deficiency = subset_deficiency(weights, neighbours, capacities)
                assert sum(weights) - flow == deficiency
                assert flow <= sum(capacities)

            for weight_cutoff in (1, 2, 4):
                for degree_cutoff in (1, 2, 4):
                    row_degree = Counter(
                        row for row_list in neighbours for row in row_list
                    )
                    good = [
                        occurrence
                        for occurrence, weight in enumerate(weights)
                        if weight <= weight_cutoff
                        and all(
                            row_degree[row] <= degree_cutoff
                            for row in neighbours[occurrence]
                        )
                    ]
                    if not good:
                        continue
                    good_weights = [weights[occurrence] for occurrence in good]
                    good_neighbours = [
                        neighbours[occurrence] for occurrence in good
                    ]
                    good_capacity = [
                        weight_cutoff * degree_cutoff * capacity
                        for capacity in base_capacity
                    ]
                    assert maximum_flow(
                        good_weights, good_neighbours, good_capacity
                    ) == sum(good_weights)


def main() -> None:
    exhaustive_flow_identity()
    deterministic_track_systems()
    random_track_systems()
    print("SWAP CAPACITATED TRACK FLOW: PASS")


if __name__ == "__main__":
    main()
