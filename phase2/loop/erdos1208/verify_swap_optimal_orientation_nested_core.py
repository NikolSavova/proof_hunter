#!/usr/bin/env python3
"""Exact finite audit for the optimal-orientation nested-core identity."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import product
from math import ceil, log2
import random

from analyze_swap_optimal_nested_cores import optimize_component


Edge = tuple[int, int]


@dataclass(frozen=True)
class Audit:
    vertices: int
    edges: int
    energy: int
    nested_mass: int
    balance_edges: int
    maximum_load: int
    dyadic_level: int


def optimum_orientation(vertices: int, edges: list[Edge]):
    """Brute-force the minimum squared-outdegree orientation."""
    assert vertices >= 1
    assert all(0 <= u < v < vertices for u, v in edges)
    assert len(edges) <= 18
    best = None
    best_bits = None
    best_loads = None
    for bits in product((0, 1), repeat=len(edges)):
        loads = [0] * vertices
        for bit, (u, v) in zip(bits, edges):
            loads[v if bit else u] += 1
        energy = sum(load * load for load in loads)
        key = (energy, loads, bits)
        if best is None or key < best:
            best = key
            best_bits = bits
            best_loads = loads
    assert best is not None and best_bits is not None and best_loads is not None
    return best[0], tuple(best_bits), tuple(best_loads)


def audit_graph(vertices: int, edges: list[Edge]) -> Audit:
    energy, bits, loads = optimum_orientation(vertices, edges)

    optimized_loads, _, _ = optimize_component(
        set(range(vertices)), Counter(edges)
    )
    assert sum(load * load for load in optimized_loads.values()) == energy

    minimum_sum = 0
    balance_edges = 0
    for bit, (u, v) in zip(bits, edges):
        tail, head = (v, u) if bit else (u, v)
        assert loads[tail] <= loads[head] + 1
        minimum_sum += min(loads[u], loads[v])
        if loads[tail] == loads[head] + 1:
            balance_edges += 1

    assert energy == minimum_sum + balance_edges

    maximum = max(loads, default=0)
    nested = 0
    level_edges: dict[int, int] = {}
    for level in range(1, maximum + 1):
        active = {v for v, load in enumerate(loads) if load >= level}
        count = sum(u in active and v in active for u, v in edges)
        level_edges[level] = count
        nested += count
    assert nested == minimum_sum
    assert nested <= energy <= len(edges) + nested

    if maximum == 0:
        dyadic_level = 0
    else:
        blocks = ceil(log2(maximum + 1))
        dyadic_levels = [1 << index for index in range(blocks)]
        dyadic_level = max(
            dyadic_levels, key=lambda level: level * level_edges.get(level, 0)
        )
        assert (
            dyadic_level * level_edges.get(dyadic_level, 0) * blocks
            >= nested
        )
        active_count = sum(load >= dyadic_level for load in loads)
        assert dyadic_level * active_count <= len(edges)
        if active_count:
            assert (
                level_edges.get(dyadic_level, 0) * len(edges)
                >= dyadic_level
                * level_edges.get(dyadic_level, 0)
                * active_count
            )

    return Audit(
        vertices,
        len(edges),
        energy,
        nested,
        balance_edges,
        maximum,
        dyadic_level,
    )


def fixed_cases() -> dict[str, tuple[int, list[Edge]]]:
    star = [(0, leaf) for leaf in range(1, 9)]
    parallel = [(0, 1)] * 11
    triangle = [(0, 1)] * 2 + [(1, 2)] * 3 + [(0, 2)] * 4
    complete_four = [(u, v) for u in range(4) for v in range(u + 1, 4)]
    mixed = [
        (0, 1),
        (0, 1),
        (0, 2),
        (1, 2),
        (1, 3),
        (1, 3),
        (2, 3),
        (2, 4),
        (3, 4),
        (3, 5),
        (4, 5),
    ]
    return {
        "star": (9, star),
        "parallel": (2, parallel),
        "triangle": (3, triangle),
        "complete_four": (4, complete_four),
        "mixed": (6, mixed),
    }


def random_cases() -> list[tuple[int, list[Edge]]]:
    rng = random.Random(1208)
    output = []
    for _ in range(120):
        vertices = rng.randint(2, 7)
        count = rng.randint(1, min(14, vertices * (vertices - 1)))
        edges = []
        for _ in range(count):
            u, v = rng.sample(range(vertices), 2)
            if u > v:
                u, v = v, u
            edges.append((u, v))
        output.append((vertices, edges))
    return output


def main() -> None:
    profiles = {}
    for name, (vertices, edges) in fixed_cases().items():
        profiles[name] = audit_graph(vertices, edges)

    # A star is completely absorbed by the balance term: its high-load
    # vertices form an independent set at every positive level.
    star = profiles["star"]
    assert star.energy == star.edges
    assert star.nested_mass == 0
    assert star.balance_edges == star.edges

    # A parallel bundle is the opposite equality model: both endpoints are
    # mutually loaded, and the nested term carries almost all the energy.
    parallel = profiles["parallel"]
    assert parallel.energy == 61
    assert parallel.nested_mass == 55
    assert parallel.balance_edges == 6

    random_profiles = [audit_graph(vertices, edges) for vertices, edges in random_cases()]
    assert len(random_profiles) == 120

    print("fixed profiles:")
    for name, profile in profiles.items():
        print(" ", name, profile)
    print("random multigraphs audited:", len(random_profiles))
    print("optimal-orientation nested-core identity: PASS")


if __name__ == "__main__":
    main()
