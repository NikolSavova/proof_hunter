#!/usr/bin/env python3
"""Classify auxiliary endpoint-reuse patterns of fixed-row uv rectangles."""

from __future__ import annotations

from collections import Counter

from verify_transverse_closure_witness import POINTS
from verify_transverse_fixed_row_c4 import fixed_row_relations, projection_cycles


def degree_pattern(edges):
    degree = Counter()
    for left, right in edges:
        degree[left] += 1
        degree[right] += 1
    return tuple(sorted(degree.values(), reverse=True))


def main():
    relations = fixed_row_relations(POINTS, (0, -1))
    cycles = projection_cycles(relations, 0, 1)
    distinct_roles = Counter()
    distinct_actual = Counter()
    directed_pattern = Counter()
    undirected_pattern = Counter()
    repeated_actual = []
    for cycle in cycles:
        aux = [(relations[index][2], relations[index][3]) for index in cycle]
        distinct_roles[(len({x for x, _ in aux}), len({y for _, y in aux}))] += 1
        vertices = {item for edge in aux for item in edge}
        distinct_actual[len(vertices)] += 1
        directed_pattern[(tuple(sorted(Counter(x for x, _ in aux).values(), reverse=True)),
                          tuple(sorted(Counter(y for _, y in aux).values(), reverse=True)))] += 1
        undirected_pattern[degree_pattern(aux)] += 1
        if len(vertices) < 8:
            repeated_actual.append((cycle, aux))
    print("cycles", len(cycles))
    print("distinct roles", distinct_roles)
    print("distinct actual", distinct_actual)
    print("directed patterns", directed_pattern)
    print("undirected patterns", undirected_pattern)
    print("repeated examples", repeated_actual[:20])


if __name__ == "__main__":
    main()
