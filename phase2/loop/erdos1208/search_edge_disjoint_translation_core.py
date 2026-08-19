#!/usr/bin/env python3
"""Search edge-disjoint translation models for a full eight-corner core.

The records are F_2^m and corner colour ``mask`` pairs x with x+shift[mask].
The eight shifts are required to be distinct, so the resulting corner
hypergraph is linear.  Each endpoint label is a connected component of the
four matchings on one cube face.  We retain only systems in which every
corner fibre has exactly two records and the six endpoint labels recover the
record, then use the exact relation-system analyzer modulo a split prime to
count universally forced squared-distance collisions.
"""

from __future__ import annotations

import argparse
import random
from collections import Counter

from search_full_eight_corner_core import Matching, analyze_mod


def span(vectors: tuple[int, ...]) -> frozenset[int]:
    values = {0}
    for vector in vectors:
        values |= {value ^ vector for value in tuple(values)}
    return frozenset(values)


def face_spaces(shifts: tuple[int, ...]) -> tuple[frozenset[int], ...]:
    return tuple(
        span(tuple(shifts[mask] for mask in range(8) if ((mask >> role) & 1) == bit))
        for role in range(3)
        for bit in range(2)
    )


def annihilator(m: int, space: frozenset[int]) -> frozenset[int]:
    return frozenset(
        character
        for character in range(1 << m)
        if all((character & vector).bit_count() % 2 == 0 for vector in space)
    )


def intersection(spaces: tuple[frozenset[int], ...]) -> frozenset[int]:
    result = set(spaces[0])
    for space in spaces[1:]:
        result.intersection_update(space)
    return frozenset(result)


def valid_exact_core(shifts: tuple[int, ...]) -> bool:
    spaces = face_spaces(shifts)
    if intersection(spaces) != frozenset({0}):
        return False
    for mask, shift in enumerate(shifts):
        selected = (
            spaces[mask & 1],
            spaces[2 + ((mask >> 1) & 1)],
            spaces[4 + ((mask >> 2) & 1)],
        )
        if intersection(selected) != frozenset({0, shift}):
            return False
    return True


def translation_matchings(m: int, shifts: tuple[int, ...]) -> tuple[Matching, ...]:
    return tuple(
        tuple(record ^ shift for record in range(1 << m))
        for shift in shifts
    )


def translation_collision_witness(
    m: int, shifts: tuple[int, ...]
) -> tuple[int, int, int] | None:
    """Find a universal parallelogram collision within one endpoint role.

    A character can carry a nonzero Fourier coefficient only if it occurs in
    at least two endpoint annihilators.  If no active character is odd on
    both independent quotient directions d,h, then every universal solution
    obeys Delta_d f(x+h)=Delta_d f(x) in that endpoint role.
    """
    spaces = face_spaces(shifts)
    annihilators = tuple(annihilator(m, space) for space in spaces)
    multiplicity = Counter(
        character for characters in annihilators for character in characters
    )
    for role, (space, characters) in enumerate(zip(spaces, annihilators)):
        active = tuple(
            character
            for character in characters
            if character and multiplicity[character] >= 2
        )
        quotient_directions = tuple(vector for vector in range(1, 1 << m) if vector not in space)
        for d in quotient_directions:
            for h in quotient_directions:
                if (d ^ h) in space:
                    continue
                if not any(
                    (character & d).bit_count() % 2
                    and (character & h).bit_count() % 2
                    for character in active
                ):
                    return role, d, h
    return None


def point_separation_failure(
    m: int, shifts: tuple[int, ...]
) -> tuple[int, int] | None:
    """Find two endpoint labels forced to be the same in every solution."""
    spaces = face_spaces(shifts)
    annihilators = tuple(annihilator(m, space) for space in spaces)
    multiplicity = Counter(
        character for characters in annihilators for character in characters
    )
    for role, (space, characters) in enumerate(zip(spaces, annihilators)):
        active = tuple(
            character
            for character in characters
            if character and multiplicity[character] >= 2
        )
        for direction in range(1, 1 << m):
            if direction in space:
                continue
            if all((character & direction).bit_count() % 2 == 0 for character in active):
                return role, direction
    return None


def coalesced_translation_obstruction(
    m: int, shifts: tuple[int, ...]
) -> tuple[str, tuple[int, ...]]:
    """Classify the core after all universally forced point equalities.

    The active characters in one endpoint role separate exactly the cosets
    of their common kernel K_s.  Replacing H_s by K_s therefore performs the
    canonical within-role coalescing.  Translation invariance makes every
    corner fibre a coset of the corresponding triple intersection modulo the
    common six-role record kernel.
    """
    spaces = face_spaces(shifts)
    annihilators = tuple(annihilator(m, space) for space in spaces)
    multiplicity = Counter(
        character for characters in annihilators for character in characters
    )
    active_by_role = tuple(
        tuple(
            character
            for character in characters
            if character and multiplicity[character] >= 2
        )
        for characters in annihilators
    )
    coalesced_spaces = tuple(
        frozenset(
            direction
            for direction in range(1 << m)
            if all(
                (character & direction).bit_count() % 2 == 0
                for character in active
            )
        )
        for active in active_by_role
    )
    record_kernel = intersection(coalesced_spaces)
    for mask in range(8):
        selected = (
            coalesced_spaces[mask & 1],
            coalesced_spaces[2 + ((mask >> 1) & 1)],
            coalesced_spaces[4 + ((mask >> 2) & 1)],
        )
        if intersection(selected) == record_kernel:
            return "empty-core", (mask,)
    for role, (space, active) in enumerate(zip(coalesced_spaces, active_by_role)):
        quotient_directions = tuple(
            vector for vector in range(1, 1 << m) if vector not in space
        )
        for d in quotient_directions:
            for h in quotient_directions:
                if (d ^ h) in space:
                    continue
                if not any(
                    (character & d).bit_count() % 2
                    and (character & h).bit_count() % 2
                    for character in active
                ):
                    return "translation-collision", (role, d, h)
    raise AssertionError((m, shifts, coalesced_spaces))


def search(m: int, trials: int, seed: int, witness_only: bool) -> None:
    rng = random.Random(seed)
    universe = list(range(1, 1 << m))
    counts: Counter[str] = Counter()
    best: tuple[int, tuple[int, ...], tuple[int, int, int, int]] | None = None
    for trial in range(trials):
        shifts = tuple(rng.sample(universe, 8))
        if not valid_exact_core(shifts):
            counts["invalid-core"] += 1
            continue
        counts["exact-core"] += 1
        witness = translation_collision_witness(m, shifts)
        if witness is not None:
            counts["translation-collision"] += 1
        elif witness_only:
            print("NO TRANSLATION-COLLISION WITNESS", trial, shifts, flush=True)
            break
        if witness_only:
            continue
        profile = analyze_mod(translation_matchings(m, shifts))
        if profile is None:
            counts["degenerate-geometry"] += 1
            continue
        counts["geometric"] += 1
        repeats = profile[2]
        if best is None or repeats < best[0]:
            best = repeats, shifts, profile
            print(
                "best",
                trial,
                "shifts",
                shifts,
                "profile",
                profile,
                "translation-witness",
                witness,
                flush=True,
            )
        if repeats == 0:
            print("GENERIC EDGE-DISJOINT FULL-CORE COUNTEREXAMPLE", flush=True)
            break
    print("counts", dict(counts))
    print("final-best", None if best is None else best)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, default=6)
    parser.add_argument("--trials", type=int, default=10_000)
    parser.add_argument("--seed", type=int, default=1208)
    parser.add_argument("--witness-only", action="store_true")
    args = parser.parse_args()
    search(args.m, args.trials, args.seed, args.witness_only)


if __name__ == "__main__":
    main()
