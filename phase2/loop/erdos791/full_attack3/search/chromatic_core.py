#!/usr/bin/env python3
"""Generate and verify the 14-type, seven-chromatic direct-footprint core."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from exhaustive_baseline import bounded_coloring, maximum_clique
from footprint_core import direct_complete, missing_points


TYPES = (
    (0, 1, 2, 3),
    (0, 1, 2, 4),
    (0, 1, 2, 5),
    (0, 1, 2, 6),
    (0, 1, 2, 7),
    (0, 1, 3, 4),
    (0, 1, 3, 5),
    (0, 1, 3, 6),
    (0, 1, 3, 7),
    (0, 1, 4, 7),
    (0, 1, 5, 7),
    (0, 2, 3, 5),
    (0, 2, 4, 5),
    (0, 2, 4, 7),
)

# A checked proper coloring of the core using colors 0,...,6.
SEVEN_COLORING = (6, 0, 3, 4, 6, 1, 4, 5, 2, 1, 3, 0, 3, 2)
SIX_CLIQUE = (0, 2, 3, 7, 9, 13)


def edges() -> list[tuple[int, int]]:
    return [
        (i, j)
        for i in range(len(TYPES))
        for j in range(i + 1, len(TYPES))
        if direct_complete(TYPES[i], TYPES[j], 9)
    ]


def vertex_deletion_colorings(
    edge_list: list[tuple[int, int]],
) -> list[dict[str, object]]:
    edge_set = set(edge_list)
    answer = []
    for deleted in range(len(TYPES)):
        vertices = [v for v in range(len(TYPES)) if v != deleted]
        adjacency = []
        for left in vertices:
            mask = 0
            for index, right in enumerate(vertices):
                if left != right and (min(left, right), max(left, right)) in edge_set:
                    mask |= 1 << index
            adjacency.append(mask)
        clique = maximum_clique(adjacency)
        coloring = bounded_coloring(adjacency, 6, clique)
        if coloring is None:
            raise RuntimeError(f"deletion of {deleted} is still not six-colorable")
        lifted = [None] * len(TYPES)
        for index, vertex in enumerate(vertices):
            lifted[vertex] = coloring[index]
        answer.append({"deleted_vertex": deleted, "six_coloring": lifted})
    return answer


def write_six_color_cnf(path: Path) -> dict[str, object]:
    edge_list = edges()
    colors = 6
    variable = lambda vertex, color: colors * vertex + color + 1
    clauses: list[list[int]] = []
    for vertex in range(len(TYPES)):
        clauses.append([variable(vertex, color) for color in range(colors)])
        for left in range(colors):
            for right in range(left + 1, colors):
                clauses.append([-variable(vertex, left), -variable(vertex, right)])
    for left, right in edge_list:
        for color in range(colors):
            clauses.append([-variable(left, color), -variable(right, color)])
    text = f"p cnf {len(TYPES) * colors} {len(clauses)}\n" + "".join(
        " ".join(map(str, clause)) + " 0\n" for clause in clauses
    )
    path.write_text(text)
    return {
        "variables": len(TYPES) * colors,
        "clauses": len(clauses),
        "sha256": hashlib.sha256(text.encode()).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--cnf", type=Path)
    args = parser.parse_args()
    edge_list = edges()
    proper = all(SEVEN_COLORING[i] != SEVEN_COLORING[j] for i, j in edge_list)
    clique_verified = all(
        (SIX_CLIQUE[i], SIX_CLIQUE[j]) in edge_list
        for i in range(len(SIX_CLIQUE))
        for j in range(i + 1, len(SIX_CLIQUE))
    )
    nonedges = [
        {"left": i, "right": j, "missing": missing_points(TYPES[i], TYPES[j], 9)}
        for i in range(len(TYPES))
        for j in range(i + 1, len(TYPES))
        if (i, j) not in edge_list
    ]
    deletion_colorings = vertex_deletion_colorings(edge_list)
    cnf = write_six_color_cnf(args.cnf) if args.cnf else None
    result = {
        "status": "PASS"
        if proper and clique_verified and len(edge_list) == 59
        else "FAIL",
        "claim": (
            "The displayed 14-vertex direct-complete footprint graph has "
            "chromatic number seven.  The JSON verifies the upper bound; "
            "the companion six-color CNF plus DRAT proves the lower bound."
        ),
        "t": 3,
        "block": 9,
        "points_per_type": 4,
        "types": TYPES,
        "edges": edge_list,
        "edge_count": len(edge_list),
        "six_clique": SIX_CLIQUE,
        "six_clique_verified": clique_verified,
        "nonedges_with_missing_points": nonedges,
        "seven_coloring": SEVEN_COLORING,
        "seven_coloring_verified": proper,
        "vertex_deletion_six_colorings": deletion_colorings,
        "vertex_critical_verified": len(deletion_colorings) == len(TYPES),
        "six_color_cnf": cnf,
        "scalable_family_claimed": False,
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "edges": len(edge_list), "cnf": cnf}, sort_keys=True))


if __name__ == "__main__":
    main()
