#!/usr/bin/env python3
"""Targeted falsification search for the transverse local gate.

This complements ``search_rotated_support.py``.  It keeps the exact
distance-Sidon constraint but maximizes one of three diagnostics of the
transverse collision graph: its edge count, maximum local degree, or number
of four-cycles.  Scoring is recomputed exactly after every valid proposed
point replacement, so the intended range is k <= about 24.
"""

from __future__ import annotations

import argparse
from collections import Counter
import math
import random

from search_rotated_support import (
    SearchState,
    candidate_point,
    greedy_seed,
    normalized,
)
from verify_adversarial_support_witnesses import WITNESSES


Point = tuple[int, int]


def transverse_profile(points: list[Point]) -> tuple[int, int, int]:
    differences = sorted(
        {
            (left[0] - right[0], left[1] - right[1])
            for left in points
            for right in points
        }
    )
    difference_set = set(differences)
    adjacency = [set() for _ in differences]
    for right, d_prime in enumerate(differences):
        for left, d in enumerate(differences[:right]):
            delta = d_prime[0] - d[0], d_prime[1] - d[1]
            if (-delta[1], delta[0]) not in difference_set:
                continue
            if d[0] * d_prime[1] - d[1] * d_prime[0] == 0:
                continue
            adjacency[left].add(right)
            adjacency[right].add(left)

    common_pairs: Counter[tuple[int, int]] = Counter()
    for neighbours in adjacency:
        ordered = sorted(neighbours)
        for right in range(len(ordered)):
            for left in range(right):
                common_pairs[(ordered[left], ordered[right])] += 1
    c4 = sum(value * (value - 1) // 2 for value in common_pairs.values()) // 2
    return (
        sum(map(len, adjacency)) // 2,
        max(map(len, adjacency), default=0),
        c4,
    )


def objective_value(profile: tuple[int, int, int], objective: str) -> int:
    return profile[{"edges": 0, "local": 1, "c4": 2}[objective]]


def anneal(
    initial: list[Point],
    side: int,
    steps: int,
    seed: int,
    objective: str,
) -> tuple[list[Point], tuple[int, int, int], dict[str, int]]:
    rng = random.Random(seed)
    state = SearchState(initial[:])
    current_profile = transverse_profile(state.points)
    current_score = objective_value(current_profile, objective)
    best_points = state.points[:]
    best_profile = current_profile
    best_score = current_score
    valid = accepted = improving = 0

    initial_temperature = {
        "local": max(2.0, len(initial) / 3),
        "edges": max(10.0, len(initial) ** 2),
        "c4": max(100.0, len(initial) ** 3),
    }[objective]
    final_temperature = 0.05

    for step in range(steps):
        index = rng.randrange(len(initial))
        candidate = candidate_point(state, index, side, rng)
        proposal = state.propose_replacement(index, candidate)
        if proposal is None:
            continue
        valid += 1
        trial = state.points[:]
        trial[index] = candidate
        trial_profile = transverse_profile(trial)
        trial_score = objective_value(trial_profile, objective)
        fraction = step / max(1, steps - 1)
        temperature = initial_temperature * (
            final_temperature / initial_temperature
        ) ** fraction
        delta = trial_score - current_score
        if delta >= 0 or rng.random() < math.exp(delta / temperature):
            proposal[1]()
            accepted += 1
            current_profile = trial_profile
            current_score = trial_score
            if delta > 0:
                improving += 1
            if current_score > best_score:
                best_score = current_score
                best_profile = current_profile
                best_points = state.points[:]

    assert transverse_profile(best_points) == best_profile
    return best_points, best_profile, {
        "valid": valid,
        "accepted": accepted,
        "improving": improving,
    }


def parse_sizes(value: str) -> list[int]:
    return [int(item) for item in value.split(",") if item]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", type=parse_sizes, default=[12, 16, 20])
    parser.add_argument("--objective", choices=["local", "edges", "c4"], default="local")
    parser.add_argument("--steps", type=int, default=5_000)
    parser.add_argument("--restarts", type=int, default=3)
    parser.add_argument("--padding", type=int, default=20)
    parser.add_argument("--seed", type=int, default=1208)
    args = parser.parse_args()

    for k in args.sizes:
        if k in WITNESSES:
            base = WITNESSES[k]
            side = max(max(x for x, _ in base), max(y for _, y in base)) + args.padding + 1
        else:
            side = 4 * k
            base = greedy_seed(k, side, random.Random(args.seed + k))

        best_points = base
        best_profile = transverse_profile(base)
        best_score = objective_value(best_profile, args.objective)
        aggregate = Counter()
        for restart in range(args.restarts):
            points, profile, stats = anneal(
                base,
                side,
                args.steps,
                args.seed + 1009 * k + restart,
                args.objective,
            )
            aggregate.update(stats)
            score = objective_value(profile, args.objective)
            if score > best_score:
                best_points, best_profile, best_score = points, profile, score

        edges, local, c4 = best_profile
        print(
            f"k={k:2d} objective={args.objective} score={best_score} "
            f"Etr={edges} maxlocal={local} maxlocal/k={local/k:.6f} "
            f"C4={c4} C4/k^4={c4/k**4:.6f} "
            f"valid={aggregate['valid']} accepted={aggregate['accepted']}"
        )
        print("  points", normalized(best_points))


if __name__ == "__main__":
    main()
