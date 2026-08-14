#!/usr/bin/env python3
"""Exact global plateau census for type-A reflection orders.

The vertices are commutation classes of reduced words for w_0.  Edges are
long braids.  We contract edges on which the reverse-product trace V is
constant, then record all trace-sink plateaus and their graded statistics.
All evaluations are exact integers/rationals.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter, deque
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
GATE_DIR = ROOT / "phase2" / "loop" / "erdos838" / "agent_reflection_gate"
sys.path.insert(0, str(GATE_DIR))
import reflection_order_gate as gate  # noqa: E402

Word = tuple[int, ...]


def enumerate_graph(n: int):
    start = gate.canonical_commutation_word(gate.bubble_word(n))
    queue = [start]
    seen = {start}
    adjacency: dict[Word, set[Word]] = {}
    evaluations = {}
    cursor = 0
    while cursor < len(queue):
        word = queue[cursor]
        cursor += 1
        evaluations[word] = gate.evaluate_word(n, word, graded=True)
        neighbors = gate.braid_neighbors_mod_commutation(n, word)
        adjacency[word] = neighbors
        for neighbor in neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return queue, adjacency, evaluations


def components_at_equal_trace(words, adjacency, evaluations):
    component_of: dict[Word, int] = {}
    components: list[list[Word]] = []
    for start in words:
        if start in component_of:
            continue
        trace = evaluations[start].trace
        cid = len(components)
        component = []
        todo = [start]
        component_of[start] = cid
        while todo:
            word = todo.pop()
            component.append(word)
            for neighbor in adjacency[word]:
                if evaluations[neighbor].trace != trace or neighbor in component_of:
                    continue
                component_of[neighbor] = cid
                todo.append(neighbor)
        components.append(component)
    return component_of, components


def frac_pair(x: Fraction) -> list[int]:
    return [x.numerator, x.denominator]


def census(n: int) -> dict:
    words, adjacency, evaluations = enumerate_graph(n)
    component_of, components = components_at_equal_trace(words, adjacency, evaluations)
    lower_neighbors: list[set[int]] = [set() for _ in components]
    higher_neighbors: list[set[int]] = [set() for _ in components]
    for word in words:
        c = component_of[word]
        trace = evaluations[word].trace
        for neighbor in adjacency[word]:
            d = component_of[neighbor]
            if c == d:
                continue
            other = evaluations[neighbor].trace
            if other < trace:
                lower_neighbors[c].add(d)
            elif other > trace:
                higher_neighbors[c].add(d)
            else:
                raise AssertionError("equal-trace edge escaped its component")

    sinks = [c for c in range(len(components)) if not lower_neighbors[c]]
    sink_rows = []
    for c in sinks:
        members = components[c]
        trace = evaluations[members[0]].trace
        means = [Fraction(evaluations[w].first_moment, trace) for w in members]
        moments = [evaluations[w].first_moment for w in members]
        profiles = [tuple(evaluations[w].graded[1:]) for w in members]
        cups = [evaluations[w].cup_total for w in members]
        caps = [evaluations[w].cap_total for w in members]
        best = min(members, key=lambda w: Fraction(evaluations[w].first_moment, trace))
        sink_rows.append(
            {
                "trace": trace,
                "plateau_size": len(members),
                "moment_range": [min(moments), max(moments)],
                "mean_range": [frac_pair(min(means)), frac_pair(max(means))],
                "mean_deficit_range": [
                    float(min(means)) - math.log2(n),
                    float(max(means)) - math.log2(n),
                ],
                "degree_range": [
                    min(len(p) for p in profiles), max(len(p) for p in profiles)
                ],
                "distinct_profiles": len(set(profiles)),
                "cup_range": [min(cups), max(cups)],
                "cap_range": [min(caps), max(caps)],
                "smallest_mean_certificate": gate.make_certificate(n, best),
            }
        )
    sink_rows.sort(key=lambda row: (row["trace"], row["mean_range"][0]))

    # Collapse symmetry-equivalent rows in the saved certificate.  Keeping a
    # full certificate for every sink made the n=7 output needlessly large.
    grouped_sinks: dict[tuple, dict] = {}
    for row in sink_rows:
        key = (
            row["trace"],
            row["plateau_size"],
            tuple(row["moment_range"]),
            tuple(tuple(x) for x in row["mean_range"]),
            tuple(row["degree_range"]),
            row["distinct_profiles"],
        )
        if key not in grouped_sinks:
            grouped_sinks[key] = {**row, "multiplicity": 1}
        else:
            grouped_sinks[key]["multiplicity"] += 1
            grouped_sinks[key]["cup_range"] = [
                min(grouped_sinks[key]["cup_range"][0], row["cup_range"][0]),
                max(grouped_sinks[key]["cup_range"][1], row["cup_range"][1]),
            ]
            grouped_sinks[key]["cap_range"] = [
                min(grouped_sinks[key]["cap_range"][0], row["cap_range"][0]),
                max(grouped_sinks[key]["cap_range"][1], row["cap_range"][1]),
            ]
    sink_types = list(grouped_sinks.values())

    # Every component reaches a sink by strict trace descent.  Compute the
    # best and worst terminal mean deficits over all reachable sinks.
    component_order = sorted(
        range(len(components)), key=lambda c: evaluations[components[c][0]].trace
    )
    reachable_sinks: list[set[int]] = [set() for _ in components]
    sink_set = set(sinks)
    for c in component_order:
        if c in sink_set:
            reachable_sinks[c].add(c)
        else:
            for d in lower_neighbors[c]:
                reachable_sinks[c].update(reachable_sinks[d])
        if not reachable_sinks[c]:
            raise AssertionError("strict trace DAG failed to reach a sink")

    trace_hist = Counter(evaluations[w].trace for w in words)
    plateau_sizes = Counter(len(component) for component in components)
    global_trace = min(trace_hist)
    global_words = [w for w in words if evaluations[w].trace == global_trace]
    global_means = [
        Fraction(evaluations[w].first_moment, global_trace) for w in global_words
    ]
    all_sink_means = [
        Fraction(pair[0], pair[1])
        for row in sink_rows
        for pair in row["mean_range"]
    ]
    return {
        "mode": "global_equal_trace_plateau_census",
        "n": n,
        "class_count": len(words),
        "edge_count": sum(map(len, adjacency.values())) // 2,
        "plateau_count": len(components),
        "plateau_size_histogram": dict(sorted(plateau_sizes.items())),
        "sink_plateau_count": len(sinks),
        "global_trace": global_trace,
        "global_trace_class_count": len(global_words),
        "global_mean_range": [frac_pair(min(global_means)), frac_pair(max(global_means))],
        "global_mean_deficit_range": [
            float(min(global_means)) - math.log2(n),
            float(max(global_means)) - math.log2(n),
        ],
        "all_sink_mean_deficit_range": [
            float(min(all_sink_means)) - math.log2(n),
            float(max(all_sink_means)) - math.log2(n),
        ],
        "sink_plateau_types": sink_types,
    }


def seeded_plateau(n: int, seed: Word) -> dict:
    """Certify one equal-trace plateau and every edge leaving it."""
    seed = gate.canonical_commutation_word(seed)
    seed_eval = gate.evaluate_word(n, seed, graded=True)
    trace = seed_eval.trace
    members = [seed]
    seen = {seed}
    cursor = 0
    boundary: dict[Word, object] = {}
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
    member_evals = [gate.evaluate_word(n, w, graded=True) for w in members]
    member_rows = [
        {
            "word": list(w),
            "graded": list(e.graded),
            "trace": e.trace,
            "first_moment": e.first_moment,
        }
        for w, e in sorted(zip(members, member_evals))
    ]
    boundary_hist = Counter(e.trace for e in boundary.values())
    best_index = min(
        range(len(members)),
        key=lambda i: (member_evals[i].first_moment, members[i]),
    )
    return {
        "mode": "seeded_equal_trace_plateau_certificate",
        "n": n,
        "trace": trace,
        "plateau_size": len(members),
        "members": member_rows,
        "boundary_size": len(boundary),
        "boundary_trace_histogram": dict(sorted(boundary_hist.items())),
        "minimum_boundary_trace": min((e.trace for e in boundary.values()), default=None),
        "is_weak_trace_sink": all(e.trace > trace for e in boundary.values()),
        "minimum_moment_certificate": gate.make_certificate(n, members[best_index]),
    }


def selftest() -> None:
    for n, count, minimum in [(3, 2, 7), (4, 8, 14), (5, 62, 26)]:
        result = census(n)
        assert result["class_count"] == count
        assert result["global_trace"] == minimum
        assert result["sink_plateau_count"] >= 1
    print("selftest passed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="?", type=int)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument(
        "--seed-word-json",
        type=Path,
        help="JSON array containing a reduced word; certify only its trace plateau",
    )
    args = parser.parse_args()
    if args.selftest:
        selftest()
        return
    if args.n is None:
        parser.error("n is required unless --selftest is used")
    if args.seed_word_json:
        result = seeded_plateau(args.n, tuple(json.loads(args.seed_word_json.read_text())))
    else:
        result = census(args.n)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
