#!/usr/bin/env python3
"""Inspect the largest variable-longest rectangle charge classes."""

from __future__ import annotations

from collections import Counter, defaultdict

from analyze_transverse_longest_charge import DIAMETER_POINTS
from verify_transverse_closure_witness import POINTS as HEAVY_POINTS
from verify_transverse_fixed_row_c4 import ROLE_PAIRS, fixed_row_relations, projection_cycles
from analyze_fixed_row_cycle_longest_charge import (
    canonical,
    coordinate_groups,
    cycle_edges,
    norm2,
)


def inspect(points, row):
    endpoint = {
        (points[i][0] - points[j][0], points[i][1] - points[j][1]): (i, j)
        for i in range(len(points))
        for j in range(len(points))
    }
    fixed = endpoint[row]
    relations = fixed_row_relations(points, row)
    best = None
    for projection in ROLE_PAIRS:
        classes = defaultdict(list)
        for cycle in projection_cycles(relations, *projection):
            edges = cycle_edges(relations, cycle, projection, fixed)
            edges.discard(canonical(fixed))
            charge = max(edges, key=lambda edge: norm2(points, edge))
            classes[charge].append(cycle)
        edge, cycles = max(classes.items(), key=lambda item: len(item[1]))
        candidate = len(cycles), projection, edge, cycles
        if best is None or candidate[0] > best[0]:
            best = candidate
    count, projection, edge, cycles = best
    print("best", count, projection, edge, points[edge[0]], points[edge[1]], norm2(points, edge))
    vertex_frequency = Counter()
    relation_frequency = Counter()
    cycle_vertices = []
    for cycle in cycles:
        vertices = {item for index in cycle for item in relations[index]}
        cycle_vertices.append(vertices)
        vertex_frequency.update(vertices)
        relation_frequency.update(cycle)
    print("vertex frequency", vertex_frequency.most_common(20))
    print("relation frequency", relation_frequency.most_common(20))
    intersections = Counter(
        len(cycle_vertices[i] & cycle_vertices[j])
        for i in range(len(cycles))
        for j in range(i)
    )
    print("pair intersections", intersections)
    print("cycles", cycles[:12])


def main():
    print("heavy")
    inspect(HEAVY_POINTS, (0, -1))
    print("diameter")
    inspect(DIAMETER_POINTS, (10_000, 0))


if __name__ == "__main__":
    main()
