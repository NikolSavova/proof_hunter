#!/usr/bin/env python3
"""Cheap deterministic baselines and seeded local search for Erdős #791.

The search keeps Kohonen's type counts (8,17,17), changes integer placement
coordinates, and scores every candidate with verifier.tile_coverage.  It is a
bounded pattern-discovery attempt, not an exhaustive nonexistence proof.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import time
from pathlib import Path
from typing import Iterable

from verifier import DEFAULT_CERTIFICATE, load_certificate, prefix_length, tile_coverage


Placement = tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]


def as_placement(cert: dict[str, object]) -> Placement:
    return tuple(tuple(cert[key]) for key in ("I", "J", "K"))  # type: ignore[return-value,arg-type]


def evaluate(place: Placement, target_m: int, horizon: int) -> tuple[int, int, int]:
    covered = tile_coverage(*place)
    prefix = prefix_length(covered)
    target_count = sum(q in covered for q in range(target_m))
    horizon_count = sum(q in covered for q in range(horizon))
    return prefix, target_count, horizon_count


def exhaustive_one_replacement(
    seed: Placement, target_m: int, horizon: int, coordinate_bound: int
) -> dict[str, object]:
    """Exhaust every fixed-type, one-coordinate replacement in [0,bound]."""
    seed_eval = evaluate(seed, target_m, horizon)
    best_eval = (-1, -1, -1)
    best_place: Placement | None = None
    evaluated = 0
    preserve_seed_prefix = 0
    for kind in range(3):
        old_values = seed[kind]
        occupied = set(old_values)
        for old in old_values:
            for new in range(coordinate_bound + 1):
                if new in occupied:
                    continue
                candidate = [list(values) for values in seed]
                candidate[kind].remove(old)
                candidate[kind].append(new)
                place = tuple(tuple(sorted(values)) for values in candidate)  # type: ignore[assignment]
                value = evaluate(place, target_m, horizon)
                evaluated += 1
                if value[0] >= seed_eval[0]:
                    preserve_seed_prefix += 1
                if value > best_eval:
                    best_eval, best_place = value, place
    return {
        "evaluated": evaluated,
        "coordinate_bound": coordinate_bound,
        "seed_evaluation": seed_eval,
        "best_nontrivial_evaluation": best_eval,
        "replacements_preserving_seed_prefix": preserve_seed_prefix,
        "best_nontrivial_placement": best_place,
    }


def exhaustive_two_local_replacements(
    seed: Placement, target_m: int, horizon: int, radius: int
) -> dict[str, object]:
    """Exhaust all valid pairs of coordinate moves of size at most ``radius``."""
    seed_eval = evaluate(seed, target_m, horizon)
    moves: list[tuple[int, int, int]] = []
    for kind, values in enumerate(seed):
        occupied = set(values)
        for old in values:
            for delta in range(-radius, radius + 1):
                new = old + delta
                if delta and new >= 0 and new not in occupied:
                    moves.append((kind, old, new))

    best_eval = (-1, -1, -1)
    best_place: Placement | None = None
    evaluated = 0
    preserve_seed_prefix = 0
    for index, first in enumerate(moves):
        for second in moves[index + 1 :]:
            # Moving the same original coordinate twice is not a two-coordinate move.
            if first[:2] == second[:2]:
                continue
            candidate = [list(values) for values in seed]
            valid = True
            for kind, old, new in (first, second):
                if old not in candidate[kind] or new in candidate[kind]:
                    valid = False
                    break
                candidate[kind].remove(old)
                candidate[kind].append(new)
            if not valid:
                continue
            place = tuple(tuple(sorted(values)) for values in candidate)  # type: ignore[assignment]
            value = evaluate(place, target_m, horizon)
            evaluated += 1
            if value[0] >= seed_eval[0]:
                preserve_seed_prefix += 1
            if value > best_eval:
                best_eval, best_place = value, place
    return {
        "evaluated": evaluated,
        "move_radius": radius,
        "seed_evaluation": seed_eval,
        "best_nontrivial_evaluation": best_eval,
        "replacements_preserving_seed_prefix": preserve_seed_prefix,
        "best_nontrivial_placement": best_place,
    }


def scalar_score(value: tuple[int, int, int], target_m: int) -> int:
    """Soft score permits temporary gaps while rewarding the exact target."""
    prefix, target_count, horizon_count = value
    return 10_000 * target_count + 10 * min(prefix, target_m) + horizon_count


def mutate(place: Placement, rng: random.Random, coordinate_bound: int) -> Placement:
    candidate = [list(values) for values in place]
    changes = 2 if rng.random() < 0.12 else 1
    for _ in range(changes):
        kind = rng.randrange(3)
        index = rng.randrange(len(candidate[kind]))
        old = candidate[kind][index]
        if rng.random() < 0.78:
            radius = 1 if rng.random() < 0.70 else rng.randint(2, 12)
            new = old + rng.choice((-radius, radius))
        else:
            new = rng.randrange(coordinate_bound + 1)
        if 0 <= new <= coordinate_bound and new not in candidate[kind]:
            candidate[kind][index] = new
            candidate[kind].sort()
    return tuple(tuple(values) for values in candidate)  # type: ignore[return-value]


def seeded_anneal(
    seed: Placement,
    target_m: int,
    horizon: int,
    coordinate_bound: int,
    steps: int,
    restarts: int,
    random_seed: int,
) -> dict[str, object]:
    rng = random.Random(random_seed)
    seed_eval = evaluate(seed, target_m, horizon)
    best_place = seed
    best_eval = seed_eval
    best_target_count = seed_eval[1]
    accepted = 0
    evaluated = 0
    started = time.monotonic()
    steps_per_restart = (steps + restarts - 1) // restarts

    for restart in range(restarts):
        current = seed
        current_eval = seed_eval
        current_score = scalar_score(current_eval, target_m)
        for local_step in range(steps_per_restart):
            if evaluated >= steps:
                break
            proposal = mutate(current, rng, coordinate_bound)
            proposal_eval = evaluate(proposal, target_m, horizon)
            proposal_score = scalar_score(proposal_eval, target_m)
            evaluated += 1
            fraction = local_step / max(1, steps_per_restart - 1)
            temperature = 40_000.0 * (250.0 / 40_000.0) ** fraction
            delta = proposal_score - current_score
            if delta >= 0 or rng.random() < math.exp(delta / temperature):
                current, current_eval, current_score = proposal, proposal_eval, proposal_score
                accepted += 1
            if proposal_eval[1] > best_target_count:
                best_target_count = proposal_eval[1]
            if proposal_eval > best_eval:
                best_place, best_eval = proposal, proposal_eval
            if proposal_eval[0] >= target_m:
                best_place, best_eval = proposal, proposal_eval
                return {
                    "status": "FOUND",
                    "evaluated": evaluated,
                    "accepted": accepted,
                    "elapsed_seconds": time.monotonic() - started,
                    "best_evaluation": best_eval,
                    "best_target_count": best_target_count,
                    "best_placement": best_place,
                }

    return {
        "status": "NO_IMPROVEMENT_FOUND",
        "evaluated": evaluated,
        "accepted": accepted,
        "elapsed_seconds": time.monotonic() - started,
        "best_evaluation": best_eval,
        "best_target_count": best_target_count,
        "best_placement": best_place,
    }


def placement_json(place: Iterable[Iterable[int]]) -> dict[str, list[int]]:
    return {key: list(values) for key, values in zip(("I", "J", "K"), place)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--target-m", type=int, default=511)
    parser.add_argument("--horizon", type=int, default=540)
    parser.add_argument("--coordinate-bound", type=int, default=540)
    parser.add_argument("--two-move-radius", type=int, default=6)
    parser.add_argument("--steps", type=int, default=250_000)
    parser.add_argument("--restarts", type=int, default=10)
    parser.add_argument("--seed", type=int, default=791)
    args = parser.parse_args()
    cert = load_certificate(args.certificate)
    seed = as_placement(cert)
    started = time.monotonic()
    baseline = exhaustive_one_replacement(
        seed, args.target_m, args.horizon, args.coordinate_bound
    )
    two_move_baseline = exhaustive_two_local_replacements(
        seed, args.target_m, args.horizon, args.two_move_radius
    )
    anneal = seeded_anneal(
        seed,
        args.target_m,
        args.horizon,
        args.coordinate_bound,
        args.steps,
        args.restarts,
        args.seed,
    )
    for section in (baseline, two_move_baseline, anneal):
        for key in ("best_nontrivial_placement", "best_placement"):
            if section.get(key) is not None:
                section[key] = placement_json(section[key])  # type: ignore[arg-type]
    output = {
        "method": (
            "exhaustive one-replacement, exhaustive bounded two-replacement, "
            "plus seeded simulated annealing"
        ),
        "exact_coverage_rule": "q in I+J or q in I+K or (q-1 in J+K and q in J+K)",
        "target_m": args.target_m,
        "horizon": args.horizon,
        "coordinate_bound": args.coordinate_bound,
        "random_seed": args.seed,
        "anneal_requested_steps": args.steps,
        "anneal_restarts": args.restarts,
        "baseline": baseline,
        "two_move_baseline": two_move_baseline,
        "anneal": anneal,
        "total_elapsed_seconds": time.monotonic() - started,
        "scope_warning": "Bounded heuristic search; NO_IMPROVEMENT_FOUND is not a nonexistence result.",
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
