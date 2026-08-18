#!/usr/bin/env python3
"""Charge fixed-row projection rectangles to their longest involved A-edge."""

from __future__ import annotations

from collections import Counter

from analyze_transverse_longest_charge import DIAMETER_POINTS
from verify_transverse_closure_witness import POINTS as HEAVY_POINTS
from verify_transverse_fixed_row_c4 import (
    ROLE_PAIRS,
    fixed_row_relations,
    projection_cycles,
)


def norm2(points, edge):
    a, b = edge
    dx = points[a][0] - points[b][0]
    dy = points[a][1] - points[b][1]
    return dx * dx + dy * dy


def canonical(edge):
    return tuple(sorted(edge))


def coordinate_groups(relations, cycle, role):
    return sorted({relations[index][role] for index in cycle})


def cycle_edges(relations, cycle, projection, fixed_edge):
    first, second = projection
    answer = {canonical(fixed_edge)}

    # The two side edges in the selected C4 projection.
    for role in (first, second):
        values = coordinate_groups(relations, cycle, role)
        assert len(values) == 2
        answer.add(canonical(tuple(values)))

    # The two distinguished row edges in every relation.
    for index in cycle:
        u, v, x, y = relations[index]
        answer.add(canonical((u, v)))
        answer.add(canonical((x, y)))
    return answer


def profile(points, row, choose_longest=True):
    endpoint = {
        (points[i][0] - points[j][0], points[i][1] - points[j][1]): (i, j)
        for i in range(len(points))
        for j in range(len(points))
    }
    fixed_edge = endpoint[row]
    relations = fixed_row_relations(points, row)
    result = []
    for projection in ROLE_PAIRS:
        charge = Counter()
        role = Counter()
        cycles = projection_cycles(relations, *projection)
        for cycle in cycles:
            edges = cycle_edges(relations, cycle, projection, fixed_edge)
            # The fixed row edge is present in every rectangle and can be a
            # strict global diameter, so charge to the longest *variable*
            # edge instead.
            edges.discard(canonical(fixed_edge))
            longest = (max if choose_longest else min)(
                edges, key=lambda edge: norm2(points, edge)
            )
            charge[longest] += 1
            if longest in {
                canonical(tuple(coordinate_groups(relations, cycle, selected)))
                for selected in projection
            }:
                role["side"] += 1
            else:
                role["relation"] += 1
        result.append(
            (
                len(cycles),
                max(charge.values(), default=0),
                sum(value * value for value in charge.values()),
                dict(role),
            )
        )
    return result


def main():
    for size in (30, 60, 90, 120):
        print("heavy longest", size, profile(HEAVY_POINTS[:size], (0, -1)))
        print("heavy shortest", size, profile(HEAVY_POINTS[:size], (0, -1), False))
    for size in (35, 45, 70, 90):
        print("diameter longest", size, profile(DIAMETER_POINTS[:size], (10_000, 0)))
        print("diameter shortest", size, profile(DIAMETER_POINTS[:size], (10_000, 0), False))


if __name__ == "__main__":
    main()
