#!/usr/bin/env python3
"""Endpoint arrays and exact local braid slacks at the finite lex minima."""

from __future__ import annotations

import json
import math
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "agent_reflection_gate"))
import reflection_order_gate as gate  # noqa: E402


def coordinate_evaluation(filename, n):
    data = json.loads((HERE / filename).read_text())
    points = sorted(map(tuple, data["coordinates_as_stored"]))
    roots = tuple(
        (i, j)
        for _, i, j in sorted(
            (Fraction(points[j][1] - points[i][1], points[j][0] - points[i][0]), i, j)
            for i in range(n)
            for j in range(i + 1, n)
        )
    )
    return gate.evaluate_roots(n, roots)


def endpoint_row(e):
    weights = [
        [e.cups[i][j] * e.caps[i][j] for j in range(e.n)] for i in range(e.n)
    ]
    positive = [x for row in weights for x in row if x]
    entropy = -sum((x / e.trace) * math.log2(x / e.trace) for x in positive)
    return {
        "trace": e.trace,
        "cup_total": e.cup_total,
        "cap_total": e.cap_total,
        "endpoint_max": e.endpoint_max,
        "cup_row_sums": [sum(row) for row in e.cups],
        "cap_row_sums": [sum(row) for row in e.caps],
        "endpoint_product_weights": weights,
        "endpoint_distribution_entropy_bits": entropy,
        "entropy_deficit_from_uniform_on_endpoint_pairs": math.log2(len(positive)) - entropy,
    }


def main():
    e8 = coordinate_evaluation("exact_realizable_n8_independent.json", 8)
    e9 = coordinate_evaluation("exact_realizable_n9.json", 9)
    core = json.loads((HERE / "exact_n8_core.json").read_text())
    word = tuple(core["word_zero_based"])
    here = gate.evaluate_word(8, word)
    histogram = Counter()
    for neighbor in gate.braid_neighbors_mod_commutation(8, word):
        other = gate.evaluate_word(8, neighbor)
        histogram[(other.trace - here.trace, other.first_moment - here.first_moment)] += 1
    output = {
        "coordinate_endpoint_arrays": {"n8": endpoint_row(e8), "n9": endpoint_row(e9)},
        "n8_global_lex_class_all_heap_exposed_neighbor_slacks": {
            "neighbor_count": sum(histogram.values()),
            "delta_V_delta_M_histogram": {
                f"{dv},{dm}": count for (dv, dm), count in sorted(histogram.items())
            },
        },
    }
    (HERE / "boundary_probe.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
