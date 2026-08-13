#!/usr/bin/env python3
"""Cheap exhaustive direct-compatibility baseline at t=3,4.

Microtypes contain zero and have t or t+1 points.  An edge means the pair
sum contains the complete current interval [0,t^2-1].  At t=4 the script
also verifies an explicit seven-clique after allowing t+2 points.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

from footprint_core import direct_complete


K7_T4 = (
    (0, 1, 2, 3, 4, 5),
    (0, 1, 2, 3, 4, 10),
    (0, 1, 2, 3, 5, 10),
    (0, 1, 2, 3, 7, 12),
    (0, 1, 2, 3, 8, 12),
    (0, 1, 2, 6, 8, 12),
    (0, 1, 2, 5, 9, 12),
)


def types(t: int, extra: int) -> list[tuple[int, ...]]:
    block = t * t
    return [
        (0,) + tail
        for size in range(t, t + extra + 1)
        for tail in combinations(range(1, block), size - 1)
    ]


def graph(t: int) -> tuple[list[tuple[int, ...]], list[int], int]:
    vertices = types(t, 1)
    adjacency = [0] * len(vertices)
    edges = 0
    for i, left in enumerate(vertices):
        for j in range(i + 1, len(vertices)):
            if direct_complete(left, vertices[j], t * t):
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
                edges += 1
    return vertices, adjacency, edges


def maximum_clique(adjacency: list[int]) -> list[int]:
    best: list[int] = []

    def visit(chosen: list[int], candidates: int) -> None:
        nonlocal best
        if len(chosen) + candidates.bit_count() <= len(best):
            return
        if not candidates:
            if len(chosen) > len(best):
                best = chosen[:]
            return
        pool = candidates
        pivot = -1
        pivot_degree = -1
        while pool:
            bit = pool & -pool
            vertex = bit.bit_length() - 1
            degree = (candidates & adjacency[vertex]).bit_count()
            if degree > pivot_degree:
                pivot, pivot_degree = vertex, degree
            pool -= bit
        branches = candidates & ~adjacency[pivot] if pivot >= 0 else candidates
        while branches:
            bit = branches & -branches
            vertex = bit.bit_length() - 1
            visit(chosen + [vertex], candidates & adjacency[vertex])
            candidates -= bit
            branches -= bit
            if len(chosen) + candidates.bit_count() <= len(best):
                return

    visit([], (1 << len(adjacency)) - 1)
    return best


def dsatur_coloring(adjacency: list[int]) -> list[int]:
    colors = [-1] * len(adjacency)
    uncolored = set(range(len(adjacency)))
    saturation = [set() for _ in adjacency]
    degrees = [row.bit_count() for row in adjacency]
    while uncolored:
        vertex = max(uncolored, key=lambda v: (len(saturation[v]), degrees[v]))
        used = saturation[vertex]
        color = 0
        while color in used:
            color += 1
        colors[vertex] = color
        uncolored.remove(vertex)
        neighbors = adjacency[vertex]
        while neighbors:
            bit = neighbors & -neighbors
            neighbor = bit.bit_length() - 1
            if neighbor in uncolored:
                saturation[neighbor].add(color)
            neighbors -= bit
    for i, neighbors in enumerate(adjacency):
        while neighbors:
            bit = neighbors & -neighbors
            j = bit.bit_length() - 1
            if colors[i] == colors[j]:
                raise RuntimeError("invalid coloring")
            neighbors -= bit
    return colors


def bounded_coloring(
    adjacency: list[int], color_count: int, fixed_clique: list[int]
) -> list[int] | None:
    """Exact DSATUR backtracking, used for the small t=3 graph."""
    colors = [-1] * len(adjacency)
    uncolored = set(range(len(adjacency)))
    saturation = [set() for _ in adjacency]

    def assign(vertex: int, color: int) -> list[int]:
        colors[vertex] = color
        uncolored.remove(vertex)
        changed = []
        neighbors = adjacency[vertex]
        while neighbors:
            bit = neighbors & -neighbors
            neighbor = bit.bit_length() - 1
            if neighbor in uncolored and color not in saturation[neighbor]:
                saturation[neighbor].add(color)
                changed.append(neighbor)
            neighbors -= bit
        return changed

    def undo(vertex: int, color: int, changed: list[int]) -> None:
        colors[vertex] = -1
        uncolored.add(vertex)
        for neighbor in changed:
            active = adjacency[neighbor]
            still_present = False
            while active:
                bit = active & -active
                other = bit.bit_length() - 1
                if colors[other] == color:
                    still_present = True
                    break
                active -= bit
            if not still_present:
                saturation[neighbor].remove(color)

    def visit() -> bool:
        if not uncolored:
            return True
        vertex = max(
            uncolored,
            key=lambda v: (len(saturation[v]), adjacency[v].bit_count()),
        )
        for color in range(color_count):
            if color in saturation[vertex]:
                continue
            changed = assign(vertex, color)
            if visit():
                return True
            undo(vertex, color, changed)
        return False

    for color, vertex in enumerate(fixed_clique):
        assign(vertex, color)
    return colors if visit() else None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = []
    for t in (3, 4):
        vertices, adjacency, edge_count = graph(t)
        clique = maximum_clique(adjacency)
        coloring = (
            bounded_coloring(adjacency, 7, clique)
            if t == 3
            else dsatur_coloring(adjacency)
        )
        if coloring is None:
            raise RuntimeError("expected t=3 seven-coloring")
        rows.append(
            {
                "t": t,
                "block": t * t,
                "sizes": [t, t + 1],
                "vertices": len(vertices),
                "edges": edge_count,
                "maximum_clique_size": len(clique),
                "maximum_clique": [vertices[i] for i in clique],
                "verified_coloring_colors": max(coloring) + 1,
                "coloring": coloring,
            }
        )
    k7_pass = all(
        direct_complete(K7_T4[i], K7_T4[j], 16)
        for i in range(7)
        for j in range(i + 1, 7)
    )
    result = {
        "status": "PASS" if k7_pass else "FAIL",
        "scope": "exhaustive for sizes t,t+1 at t=3,4; explicit witness only for t+2",
        "rows": rows,
        "t4_size_t_plus_2_K7": {
            "types": K7_T4,
            "all_21_edges_direct_complete": k7_pass,
            "scalable_family_claimed": False,
        },
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "rows": rows, "K7": k7_pass}, sort_keys=True))


if __name__ == "__main__":
    main()
