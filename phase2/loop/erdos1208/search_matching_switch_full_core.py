#!/usr/bin/env python3
"""Perturb a 64-record translation core by edge-disjoint matching switches.

The start system is the smallest connected translation core whose universal
geometry separates all endpoint labels.  A two-edge switch destroys the
abelian translation symmetry while preserving each corner colour as a
perfect matching.  We retain only linear corner hypergraphs and use modular
Gaussian elimination to minimize forced squared-distance repetitions.
"""

from __future__ import annotations

import argparse
import math
import random
from collections import Counter, defaultdict
from itertools import combinations

from search_edge_disjoint_translation_core import translation_matchings
from search_full_eight_corner_core import Matching, analyze, analyze_mod, components


START_SHIFTS = (1, 2, 4, 8, 16, 32, 21, 42)


def corner_groups(matchings: tuple[Matching, ...]) -> list[list[list[int]]]:
    maps = []
    for role in range(3):
        for bit in range(2):
            maps.append(
                components(
                    tuple(
                        matchings[mask]
                        for mask in range(8)
                        if ((mask >> role) & 1) == bit
                    )
                )
            )
    groups_by_mask: list[list[list[int]]] = []
    for mask in range(8):
        groups: dict[tuple[int, int, int], list[int]] = defaultdict(list)
        for record in range(len(matchings[0])):
            key = (
                maps[mask & 1][record],
                maps[2 + ((mask >> 1) & 1)][record],
                maps[4 + ((mask >> 2) & 1)][record],
            )
            groups[key].append(record)
        groups_by_mask.append(list(groups.values()))
    return groups_by_mask


def is_linear_full_core(matchings: tuple[Matching, ...]) -> bool:
    seen_pairs: set[tuple[int, int]] = set()
    for groups in corner_groups(matchings):
        for group in groups:
            if len(group) < 2:
                return False
            for left, right in combinations(group, 2):
                pair = (left, right)
                if pair in seen_pairs:
                    return False
                seen_pairs.add(pair)
    return True


def switched_matching(
    matching: Matching,
    first: tuple[int, int],
    second: tuple[int, int],
    crossed: bool,
) -> Matching:
    a, b = first
    c, d = second
    new_pairs = ((a, d), (b, c)) if crossed else ((a, c), (b, d))
    result = list(matching)
    for left, right in new_pairs:
        result[left] = right
        result[right] = left
    return tuple(result)


def propose(
    matchings: tuple[Matching, ...], rng: random.Random
) -> tuple[Matching, ...] | None:
    colour = rng.randrange(8)
    matching = matchings[colour]
    edges = tuple((vertex, matching[vertex]) for vertex in range(len(matching)) if vertex < matching[vertex])
    first, second = rng.sample(edges, 2)
    candidate_matching = switched_matching(matching, first, second, bool(rng.randrange(2)))
    changed = set(first + second)
    for other_colour, other in enumerate(matchings):
        if other_colour == colour:
            continue
        if any(other[vertex] == candidate_matching[vertex] for vertex in changed):
            return None
    candidate = list(matchings)
    candidate[colour] = candidate_matching
    return tuple(candidate)


def search(steps: int, seed: int, temperature: float) -> None:
    rng = random.Random(seed)
    current = translation_matchings(6, START_SHIFTS)
    current_profile = analyze_mod(current)
    assert current_profile == (32, 13, 32, 64)
    assert is_linear_full_core(current)
    best = current_profile[2]
    accepted = 0
    valid = 0
    for step in range(steps):
        candidate = propose(current, rng)
        if candidate is None or not is_linear_full_core(candidate):
            continue
        profile = analyze_mod(candidate)
        if profile is None:
            continue
        valid += 1
        delta = profile[2] - current_profile[2]
        cooling = max(0.01, 1.0 - step / max(steps, 1))
        if delta <= 0 or rng.random() < math.exp(-delta / max(temperature * cooling, 1e-9)):
            current = candidate
            current_profile = profile
            accepted += 1
        if profile[2] < best:
            best = profile[2]
            print(
                "best",
                step,
                "profile",
                profile,
                "accepted",
                accepted,
                "valid",
                valid,
                flush=True,
            )
        if profile[2] == 0:
            exact_profile = analyze(candidate)
            print("GENERIC FULL-CORE COUNTEREXAMPLE", exact_profile, flush=True)
            return
    print("complete", "best", best, "current", current_profile, "accepted", accepted, "valid", valid)


def exhaust_one_switch() -> None:
    start = translation_matchings(6, START_SHIFTS)
    counts: Counter[str] = Counter()
    for colour, matching in enumerate(start):
        edges = tuple(
            (vertex, matching[vertex])
            for vertex in range(len(matching))
            if vertex < matching[vertex]
        )
        for first, second in combinations(edges, 2):
            for crossed in (False, True):
                candidate_matching = switched_matching(
                    matching, first, second, crossed
                )
                changed = set(first + second)
                if any(
                    any(
                        start[other_colour][vertex] == candidate_matching[vertex]
                        for vertex in changed
                    )
                    for other_colour in range(8)
                    if other_colour != colour
                ):
                    counts["edge-overlap"] += 1
                    continue
                candidate = list(start)
                candidate[colour] = candidate_matching
                candidate_tuple = tuple(candidate)
                if not is_linear_full_core(candidate_tuple):
                    counts["nonlinear"] += 1
                    continue
                profile = analyze_mod(candidate_tuple)
                assert profile is not None
                counts[str(profile)] += 1
    assert counts == Counter(
        {
            "nonlinear": 6_784,
            "edge-overlap": 896,
            "(29, 10, 37, 64)": 256,
        }
    )
    print("one-switch profiles", dict(counts))
    print("matching-switch local audit: PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=20_000)
    parser.add_argument("--seed", type=int, default=1208)
    parser.add_argument("--temperature", type=float, default=2.0)
    parser.add_argument("--exhaust-one-switch", action="store_true")
    args = parser.parse_args()
    if args.exhaust_one_switch:
        exhaust_one_switch()
        return
    search(args.steps, args.seed, args.temperature)


if __name__ == "__main__":
    main()
