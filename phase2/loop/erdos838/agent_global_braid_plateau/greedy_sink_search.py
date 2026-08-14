#!/usr/bin/env python3
"""Seeded exact-arithmetic descent to weak trace-sink plateaus.

This is heuristic coverage: every reported terminal plateau is certified
locally (all of its equal-trace members and boundary edges are exhausted), but
the collection of starts is not exhaustive for n >= 8.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "phase2" / "loop" / "erdos838" / "agent_reflection_gate"))
import reflection_order_gate as gate  # noqa: E402


def plateau_boundary(n, seed):
    seed = gate.canonical_commutation_word(seed)
    trace = gate.evaluate_word(n, seed).trace
    members = [seed]
    seen = {seed}
    boundary = {}
    cursor = 0
    while cursor < len(members):
        word = members[cursor]
        cursor += 1
        for neighbor in gate.braid_neighbors_mod_commutation(n, word):
            value = gate.evaluate_word(n, neighbor, graded=True)
            if value.trace == trace:
                if neighbor not in seen:
                    seen.add(neighbor)
                    members.append(neighbor)
            else:
                boundary[neighbor] = value
    return members, boundary


def search(n: int, restarts: int, seed: int, max_rounds: int) -> dict:
    rng = random.Random(seed)
    sinks = {}
    starts = []
    for restart in range(restarts):
        word = gate.random_reduced_word(n, rng)
        start_trace = gate.evaluate_word(n, word).trace
        rounds = 0
        while rounds < max_rounds:
            rounds += 1
            members, boundary = plateau_boundary(n, word)
            lower = [(value.trace, value.first_moment / value.trace, w) for w, value in boundary.items() if value.trace < gate.evaluate_word(n, word).trace]
            if not lower:
                member_values = [(gate.evaluate_word(n, w, graded=True), w) for w in members]
                value, best_word = min(member_values, key=lambda x: (x[0].first_moment / x[0].trace, x[1]))
                key = tuple(sorted(members))
                sinks.setdefault(
                    key,
                    {
                        "multiplicity": 0,
                        "trace": value.trace,
                        "plateau_size": len(members),
                        "minimum_mean": [value.first_moment, value.trace],
                        "minimum_mean_deficit": value.mean_size - math.log2(n),
                        "minimum_mean_certificate": gate.make_certificate(n, best_word),
                        "boundary_size": len(boundary),
                        "minimum_boundary_trace": min((v.trace for v in boundary.values()), default=None),
                    },
                )["multiplicity"] += 1
                starts.append({"restart": restart, "start_trace": start_trace, "rounds": rounds, "sink_trace": value.trace})
                break
            _, _, word = min(lower)
        else:
            starts.append({"restart": restart, "start_trace": start_trace, "rounds": rounds, "failed_to_terminate": True})
    sink_rows = sorted(sinks.values(), key=lambda row: (row["trace"], row["minimum_mean"]))
    return {
        "mode": "heuristic_starts_with_certified_terminal_plateaus",
        "n": n,
        "seed": seed,
        "restarts": restarts,
        "max_rounds": max_rounds,
        "distinct_terminal_plateaus": len(sink_rows),
        "terminal_trace_histogram": dict(sorted(Counter(row["trace"] for row in sink_rows).items())),
        "best_terminal_mean_deficit": min(row["minimum_mean_deficit"] for row in sink_rows),
        "sink_plateaus": sink_rows,
        "starts": starts,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--restarts", type=int, default=10)
    parser.add_argument("--seed", type=int, default=838)
    parser.add_argument("--max-rounds", type=int, default=200)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = search(args.n, args.restarts, args.seed, args.max_rounds)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
