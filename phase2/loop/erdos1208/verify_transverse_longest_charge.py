#!/usr/bin/env python3
"""Exact certificate for TRANSVERSE_LONGEST_EDGE_CHARGE_AUDIT.md."""

from __future__ import annotations

from collections import Counter

from analyze_transverse_longest_charge import (
    DIAMETER_POINTS,
    edge_map,
    longest_families,
    matroid_union_rank,
    norm2,
    rotate,
)
from search_rotated_support import is_distance_sidon


Point = tuple[int, int]
Edge = tuple[int, int]
Item = tuple[Edge, Edge]


FIXED_DIAMETER = (10000, 0)


def fixed_row_items(points: list[Point]) -> list[Item]:
    edges = edge_map(points)
    labels = set(edges)
    fixed_norm = norm2(FIXED_DIAMETER)
    items: list[Item] = []
    for edge in labels:
        if edge == (0, 0) or FIXED_DIAMETER[0] * edge[0] == 0:
            continue
        turned = rotate(edge)
        image = (
            FIXED_DIAMETER[0] - turned[0],
            FIXED_DIAMETER[1] - turned[1],
        )
        if (
            image != (0, 0)
            and image in labels
            and norm2(edge) < fixed_norm
            and norm2(image) < fixed_norm
        ):
            items.append((edges[edge], edges[image]))
    return items


def hypergraph_degeneracy(items: list[Item], vertex_count: int) -> int:
    hyperedges = [set(first + second) for first, second in items]
    active_edges = set(range(len(hyperedges)))
    active_vertices = set(range(vertex_count))
    degeneracy = 0
    while active_edges:
        degrees = Counter(
            vertex
            for edge_index in active_edges
            for vertex in hyperedges[edge_index]
        )
        vertex = min(active_vertices, key=lambda item: degrees[item])
        degeneracy = max(degeneracy, degrees[vertex])
        active_edges = {
            edge_index
            for edge_index in active_edges
            if vertex not in hyperedges[edge_index]
        }
        active_vertices.remove(vertex)
    return degeneracy


def unoriented(edge: Edge) -> Edge:
    return tuple(sorted(edge))  # type: ignore[return-value]


def verify_geometry() -> None:
    assert len(DIAMETER_POINTS) == 90
    assert DIAMETER_POINTS[:2] == [(10000, 0), (0, 0)]
    assert is_distance_sidon(DIAMETER_POINTS)
    radius_squared = 4990 * 4990
    assert all(
        (x - 5000) ** 2 + y * y < radius_squared
        for x, y in DIAMETER_POINTS[2:]
    )
    diameter_squared = 10000 * 10000
    assert all(
        (DIAMETER_POINTS[i][0] - DIAMETER_POINTS[j][0]) ** 2
        + (DIAMETER_POINTS[i][1] - DIAMETER_POINTS[j][1]) ** 2
        < diameter_squared
        for i in range(len(DIAMETER_POINTS))
        for j in range(i)
        if {i, j} != {0, 1}
    )
    print("geometry", len(DIAMETER_POINTS), "strict global diameter")


def verify_checkpoints() -> None:
    expected = {
        35: (61, 61, 3),
        45: (90, 83, 3),
        70: (180, 133, 4),
        90: (266, 173, 5),
    }
    for size, target in expected.items():
        items = fixed_row_items(DIAMETER_POINTS[:size])
        profile = (
            len(items),
            matroid_union_rank(items, size).rank,
            hypergraph_degeneracy(items, size),
        )
        assert profile == target
        print("checkpoint", size, profile)


def verify_global_profile() -> None:
    points = DIAMETER_POINTS
    rows, columns, total, roles, ties = longest_families(points)
    assert total == 336_428
    assert roles == (114_876, 106_676, 114_876)
    assert ties == 0
    assert len(rows[FIXED_DIAMETER]) == 266

    edges = edge_map(points)
    charges: Counter[Edge] = Counter()
    for vector, family in rows.items():
        # Swapping d and f is a fixed-point-free involution on the two
        # non-column longest roles, so the row count is doubled.
        charges[unoriented(edges[vector])] += 2 * len(family)
    for vector, family in columns.items():
        charges[unoriented(edges[vector])] += len(family)

    assert sum(charges.values()) == total
    assert max(charges.values()) == 1124
    assert charges[(0, 1)] == 1124
    moment = sum(value * value for value in charges.values())
    assert moment == 50_120_272
    print("global", total, roles, max(charges.values()), moment)


def main() -> None:
    verify_geometry()
    verify_checkpoints()
    verify_global_profile()
    print("PASS")


if __name__ == "__main__":
    main()
