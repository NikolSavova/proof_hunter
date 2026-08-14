#!/usr/bin/env python3
"""Exact max-plus hull-chain witnesses for the fitted cyclic three-map IFS.

This is deliberately independent of the counting matrices.  It processes the
edge-slope order twice, replacing addition by maximum and retaining an actual
monotone path.  Opposite paths with common endpoints form a convex subset.
Point labels are IFS digit words, outermost digit first.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
LEX = HERE.parent / "agent_lex_minimizer_search"
sys.path.insert(0, str(LEX))
import triangular_ifs_probe as ifs  # noqa: E402


def max_paths(n: int, edges):
    """Return best increasing-index paths for every ordered endpoint pair."""
    rows: list[list[tuple[int, ...] | None]] = [[None] * n for _ in range(n)]
    for i in range(n):
        rows[i][i] = (i,)
    for i, j in edges:
        for s, old_path in enumerate(rows[i]):
            if old_path is None:
                continue
            candidate = old_path + (j,)
            current = rows[j][s]
            if current is None or len(candidate) > len(current):
                rows[j][s] = candidate
    return rows


def best_convex_witness(points_with_labels):
    ordered = sorted(points_with_labels, key=lambda item: item[0])
    points = [item[0] for item in ordered]
    labels = [item[1] for item in ordered]
    n = len(points)
    slopes = sorted(
        ((points[j][1] - points[i][1]) / (points[j][0] - points[i][0]), i, j)
        for i in range(n)
        for j in range(i + 1, n)
    )
    edges = [(i, j) for _, i, j in slopes]
    cups = max_paths(n, edges)
    caps = max_paths(n, reversed(edges))
    best = None
    for s in range(n):
        for t in range(s + 1, n):
            cup = cups[t][s]
            cap = caps[t][s]
            if cup is None or cap is None:
                continue
            size = len(cup) + len(cap) - 2
            key = (size, tuple(labels[i] for i in cup), tuple(labels[i] for i in cap))
            if best is None or key > best[0]:
                best = (key, cup, cap)
    if best is None:
        raise AssertionError("no endpoint pair")
    (_, cup_words, cap_words), cup, cap = best
    union = sorted(set(cup) | set(cap))
    return {
        "n": n,
        "maximum_convex_size": len(union),
        "left_endpoint": list(labels[cup[0]]),
        "right_endpoint": list(labels[cup[-1]]),
        "cup_words": [list(word) for word in cup_words],
        "cap_words": [list(word) for word in cap_words],
        "convex_words": [list(labels[i]) for i in union],
    }


def main() -> None:
    data = json.loads((LEX / "exact_realizable_n9.json").read_text())
    points = sorted(tuple(map(Fraction, p)) for p in data["coordinates_as_stored"])
    groups = ((0, 1, 5), (2, 3, 4), (6, 7, 8))
    clusters = [[points[i] for i in group] for group in groups]
    macro = [ifs.centroid(cluster) for cluster in clusters]
    permutations = ((0, 1, 2), (2, 0, 1), (0, 2, 1))
    maps, _ = ifs.make_maps(macro, clusters, permutations, Fraction(1))

    current = [(point, (digit,)) for digit, point in enumerate(macro)]
    rows = []
    for depth in range(1, 7):
        if depth > 1:
            current = [
                (transform(point), (digit,) + word)
                for digit, transform in enumerate(maps)
                for point, word in current
            ]
        row = best_convex_witness(current)
        row["depth"] = depth
        rows.append(row)
        print(depth, row["n"], row["maximum_convex_size"])

    output = {
        "mode": "exact rational max-plus opposite-path certificate",
        "permutations": [list(p) for p in permutations],
        "rows": rows,
    }
    (HERE / "cyclic_ifs_maxplus_certificate.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )


if __name__ == "__main__":
    main()
