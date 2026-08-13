#!/usr/bin/env python3
"""Enumerate the full literal carry transition graph at one admissible scale."""

from __future__ import annotations

import argparse
import json

from seven_slope_tiles import SLOPES, admissible_scale, tile


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--t", type=int, default=251)
    args = parser.parse_args()
    t = args.t
    if not admissible_scale(t):
        raise SystemExit("inadmissible scale")
    B = t * t
    Q = set(range(B))
    elementary = {a: tile(t, a) for a in SLOPES}
    footprints = {}
    for index, a in enumerate(SLOPES):
        for b in SLOPES[index + 1 :]:
            sums = {x + y for x in elementary[a] for y in elementary[b]}
            footprints[(a, b)] = (
                Q & sums,
                {x - B for x in sums if B <= x < 2 * B},
            )
    graph = {
        str(old): [
            list(new)
            for new in footprints
            if footprints[old][1] | footprints[new][0] == Q
        ]
        for old in footprints
    }
    graph_tuples = {
        old: [tuple(new) for new in graph[str(old)]] for old in footprints
    }
    indices: dict[tuple[int, int], int] = {}
    low: dict[tuple[int, int], int] = {}
    stack: list[tuple[int, int]] = []
    on_stack: set[tuple[int, int]] = set()
    components: list[list[tuple[int, int]]] = []

    def visit(vertex: tuple[int, int]) -> None:
        indices[vertex] = low[vertex] = len(indices)
        stack.append(vertex)
        on_stack.add(vertex)
        for target in graph_tuples[vertex]:
            if target not in indices:
                visit(target)
                low[vertex] = min(low[vertex], low[target])
            elif target in on_stack:
                low[vertex] = min(low[vertex], indices[target])
        if low[vertex] == indices[vertex]:
            component = []
            while True:
                target = stack.pop()
                on_stack.remove(target)
                component.append(target)
                if target == vertex:
                    break
            components.append(component)

    for edge in footprints:
        if edge not in indices:
            visit(edge)
    self_loops = all(list(edge) in graph[str(edge)] for edge in footprints)
    print(
        json.dumps(
            {
                "status": "PASS" if self_loops else "FAIL",
                "t": t,
                "B": B,
                "number_states": len(footprints),
                "number_transitions": sum(map(len, graph.values())),
                "number_nonself_transitions": sum(map(len, graph.values())) - len(footprints),
                "all_441_transitions": sum(map(len, graph.values())) == len(footprints) ** 2,
                "all_21_symbolically_expected_self_loops_present": self_loops,
                "strong_component_sizes": sorted(map(len, components), reverse=True),
                "acyclic_after_deleting_self_loops": all(len(component) == 1 for component in components),
                "footprint_sizes": {
                    str(edge): {"lower": len(parts[0]), "upper": len(parts[1])}
                    for edge, parts in footprints.items()
                },
                "transition_graph": graph,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
