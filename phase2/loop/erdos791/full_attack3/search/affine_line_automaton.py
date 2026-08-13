#!/usr/bin/env python3
"""Exact carry-transition automaton for affine grid-line microtypes.

Coordinates t*i+j identify the t by t block.  The types are every affine
line j=a*i+c (mod t), plus horizontal lines i=c.  A state/event is an
unordered pair of line types, represented by its exact low/carry footprints.
The transition e->f is legal exactly when carry(e) union low(f) is the full
next block.  SCCs expose genuine nonlocal periodic cycles.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

from footprint_core import literal_periodic_check, pair_footprint


def affine_lines(t: int) -> list[tuple[tuple[str | int, int], tuple[int, ...]]]:
    rows = [(('inf', c), tuple(c * t + j for j in range(t))) for c in range(t)]
    graphs = [
        ((a, c), tuple(t * i + ((a * i + c) % t) for i in range(t)))
        for a in range(t)
        for c in range(t)
    ]
    return rows + graphs


def strongly_connected(adjacency: list[list[int]]) -> list[list[int]]:
    index = [-1] * len(adjacency)
    low = [0] * len(adjacency)
    stack: list[int] = []
    on_stack = [False] * len(adjacency)
    components: list[list[int]] = []
    clock = 0

    def visit(v: int) -> None:
        nonlocal clock
        index[v] = low[v] = clock
        clock += 1
        stack.append(v)
        on_stack[v] = True
        for w in adjacency[v]:
            if index[w] < 0:
                visit(w)
                low[v] = min(low[v], low[w])
            elif on_stack[w]:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            component = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
                if w == v:
                    break
            components.append(component)

    for vertex in range(len(adjacency)):
        if index[vertex] < 0:
            visit(vertex)
    return components


def audit(t: int) -> dict[str, object]:
    block = t * t
    full = (1 << block) - 1
    types = affine_lines(t)
    events = []
    for left, right in combinations(range(len(types)), 2):
        low, high = pair_footprint(types[left][1], types[right][1], block)
        if low != full:  # direct-current events make any incoming state irrelevant
            events.append((left, right, low, high))
    adjacency = [
        [j for j, current in enumerate(events) if previous[3] | current[2] == full]
        for previous in events
    ]
    components = strongly_connected(adjacency)
    nonlocal_components = [component for component in components if len(component) > 1]
    self_loops = [i for i, neighbors in enumerate(adjacency) if i in neighbors]
    return {
        "t": t,
        "type_count": len(types),
        "partial_event_count": len(events),
        "transition_count": sum(map(len, adjacency)),
        "self_loop_count": len(self_loops),
        "nonlocal_periodic_SCC_count": len(nonlocal_components),
        "largest_nonlocal_SCC": max(map(len, nonlocal_components), default=0),
        "sample_self_loops": [
            [types[events[i][0]][0], types[events[i][1]][0]] for i in self_loops[:10]
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--t", type=int, nargs="+", default=[3, 5, 7, 11])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = [audit(t) for t in args.t]
    literal = [literal_periodic_check(t, 1, 6) for t in args.t]
    result = {
        "status": "PASS" if all(row["nonlocal_periodic_SCC_count"] == 0 for row in rows) and all(x["pass"] for x in literal) else "FAIL",
        "scope": "exact finite affine-line automata at the listed t; no asymptotic no-go claim",
        "rows": rows,
        "literal_stationary_cycle_checks": literal,
        "symbolic_sublemma": (
            "For a pair of t-point types whose B=t^2 ordered sums are "
            "modulo-complete, low and carry partition the block. Between two "
            "such exact events e->f iff low(e) is a subset of low(f); "
            "therefore a directed cycle of exact events forces identical low footprints."
        ),
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
