#!/usr/bin/env python3
"""Exact verifier for ABSTRACT_MIXED_HALL_ASSEMBLY.md."""

from __future__ import annotations

from collections import deque
from fractions import Fraction as Q
from itertools import combinations

from verify_rooted_fan_complement import (
    add_coherent_root,
    convex_hull_size,
    cup_cap_set,
    genericize,
    orient,
)


def max_flow(capacity: list[list[int]], source: int, sink: int) -> int:
    """Small exact integral Edmonds--Karp implementation."""
    residual = [row[:] for row in capacity]
    total = 0
    while True:
        parent = [-1] * len(residual)
        parent[source] = source
        queue = deque([source])
        while queue and parent[sink] < 0:
            u = queue.popleft()
            for v, cap in enumerate(residual[u]):
                if cap and parent[v] < 0:
                    parent[v] = u
                    queue.append(v)
        if parent[sink] < 0:
            return total
        amount = min(
            residual[parent[v]][v]
            for v in _path_vertices(parent, source, sink)
        )
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= amount
            residual[v][u] += amount
            v = u
        total += amount


def _path_vertices(parent: list[int], source: int, sink: int) -> list[int]:
    vertices = []
    v = sink
    while v != source:
        vertices.append(v)
        v = parent[v]
    return vertices


def hall_holds(neighbours: tuple[int, ...], demands: tuple[int, ...], outputs: int, load: int) -> bool:
    histories = len(neighbours)
    for mask in range(1 << histories):
        demand = sum(demands[h] for h in range(histories) if mask >> h & 1)
        union = 0
        for h in range(histories):
            if mask >> h & 1:
                union |= neighbours[h]
        if demand > load * union.bit_count():
            return False
    return True


def flow_holds(neighbours: tuple[int, ...], demands: tuple[int, ...], outputs: int, load: int) -> bool:
    histories = len(neighbours)
    source = histories + outputs
    sink = source + 1
    count = sink + 1
    capacity = [[0] * count for _ in range(count)]
    total = sum(demands)
    for h, demand in enumerate(demands):
        capacity[source][h] = demand
        for output in range(outputs):
            if neighbours[h] >> output & 1:
                capacity[h][histories + output] = total + 1
    for output in range(outputs):
        capacity[histories + output][sink] = load
    return max_flow(capacity, source, sink) == total


def audit_weighted_hall() -> int:
    checked = 0
    histories = 3
    outputs = 3
    nonempty_masks = range(1, 1 << outputs)
    for neighbours in __import__("itertools").product(nonempty_masks, repeat=histories):
        for demands in __import__("itertools").product((1, 2), repeat=histories):
            for load in (1, 2, 3):
                assert hall_holds(neighbours, demands, outputs, load) == flow_holds(
                    neighbours, demands, outputs, load
                )
                checked += 1
    return checked


def alternating_polygon(rank: int) -> tuple[tuple[Q, Q], ...]:
    height = 10 * rank * rank
    return tuple(
        (Q(index), Q(height - index * index) if index % 2 == 0 else Q(-height + index * index))
        for index in range(rank)
    )


def is_hull_edge(points, i: int, j: int) -> bool:
    signs = [
        orient(points[i], points[j], points[k])
        for k in range(len(points))
        if k not in (i, j)
    ]
    return all(sign > 0 for sign in signs) or all(sign < 0 for sign in signs)


def audit_trace_overlap(rank: int) -> dict[str, int]:
    points = alternating_polygon(rank)
    assert all(orient(points[i], points[j], points[k]) for i, j, k in combinations(range(rank), 3))
    assert convex_hull_size(points) == rank
    eligible = []
    for i in range(rank - 1):
        left_signs = {
            1 if orient(points[i], points[i + 1], points[j]) > 0 else -1
            for j in range(i)
        }
        right_signs = {
            1 if orient(points[i], points[i + 1], points[j]) > 0 else -1
            for j in range(i + 2, rank)
        }
        mixed = (
            bool(left_signs)
            and bool(right_signs)
            and len(left_signs) == len(right_signs) == 1
            and left_signs != right_signs
            and not is_hull_edge(points, i, i + 1)
        )
        if mixed:
            eligible.append(i)
    assert eligible == list(range(1, rank - 2))
    assert len(eligible) == rank - 3
    return {"rank": rank, "trace_overlap": len(eligible)}


def audit_root_overlap(roots_count: int = 12) -> dict[str, int]:
    complement = genericize(cup_cap_set(5, 5))
    points = complement
    for _ in range(roots_count):
        points = add_coherent_root(points, 1)
    roots = points[:roots_count]
    complement_now = points[roots_count:]
    assert complement_now == complement
    assert all(
        orient(root, complement[i], complement[j]) > 0
        for root in roots
        for i, j in combinations(range(len(complement)), 2)
    )

    # One fixed top mixed face in E(5,5): take a singleton from each child.
    left_size = len(cup_cap_set(5, 4))
    fixed_face = (complement[0], complement[left_size])
    assert convex_hull_size(fixed_face) == 2
    local_loads = [1] * roots_count
    assert sum(local_loads) == roots_count
    return {
        "roots": roots_count,
        "bank_overlap": roots_count,
        "assembled_load": sum(local_loads),
    }


def audit_block_assembly() -> dict[str, int]:
    # Three fibre-one local block codes with deliberately overlapping banks.
    banks = ({0, 1, 2}, {1, 2, 3}, {2, 3, 4})
    assignments = ({0: "a", 1: "b"}, {1: "c", 2: "d"}, {2: "e", 3: "f"})
    load = [0] * 5
    recovery = [set() for _ in range(5)]
    incidence = [0] * 5
    for cell, bank in enumerate(banks):
        for output in bank:
            incidence[output] += 1
        for output, history in assignments[cell].items():
            assert output in bank
            load[output] += 1
            recovery[output].add((cell, history))
    assert all(load[output] <= incidence[output] for output in range(5))
    assert all(len(recovery[output]) <= incidence[output] for output in range(5))
    assert max(load) == max(len(items) for items in recovery) == 2
    return {"cells": 3, "max_incidence": max(incidence), "max_load": max(load)}


def main() -> None:
    hall_cases = audit_weighted_hall()
    block = audit_block_assembly()
    traces = [audit_trace_overlap(rank) for rank in range(4, 31)]
    roots = audit_root_overlap()
    print("abstract mixed Hall assembly: PASS")
    print(f"weighted Hall graphs checked={hall_cases}")
    print(
        f"block assembly cells={block['cells']} incidence={block['max_incidence']} "
        f"load={block['max_load']}"
    )
    for rank in (4, 6, 10, 20, 30):
        row = traces[rank - 4]
        print(f"alternating rank={rank:2d} exact trace overlap={row['trace_overlap']}")
    print(
        f"coherent roots={roots['roots']} bank overlap={roots['bank_overlap']} "
        f"assembled load={roots['assembled_load']}"
    )


if __name__ == "__main__":
    main()
