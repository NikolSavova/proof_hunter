#!/usr/bin/env python3
"""Exact checks for the eight-involution commutator stability lemma."""

from __future__ import annotations

import random

from search_edge_disjoint_translation_core import translation_matchings
from search_matching_switch_full_core import START_SHIFTS, switched_matching


Matching = tuple[int, ...]


def canonical_word(matchings: tuple[Matching, ...], mask: int, point: int) -> int:
    for colour, matching in enumerate(matchings):
        if (mask >> colour) & 1:
            point = matching[point]
    return point


def commutator_bad_set(matchings: tuple[Matching, ...]) -> frozenset[int]:
    size = len(matchings[0])
    return frozenset(
        point
        for point in range(size)
        if any(
            matchings[left][matchings[right][point]]
            != matchings[right][matchings[left][point]]
            for left in range(len(matchings))
            for right in range(left + 1, len(matchings))
        )
    )


def stable_orbits(
    matchings: tuple[Matching, ...]
) -> tuple[frozenset[int], tuple[frozenset[int], ...]]:
    colours = len(matchings)
    size = len(matchings[0])
    bad = commutator_bad_set(matchings)
    contaminated = frozenset(
        point
        for point in range(size)
        if any(
            canonical_word(matchings, mask, point) in bad
            for mask in range(1 << colours)
        )
    )
    assert len(contaminated) <= (1 << colours) * len(bad)
    good = set(range(size)) - set(contaminated)
    orbits = []
    while good:
        root = next(iter(good))
        orbit = frozenset(
            canonical_word(matchings, mask, root)
            for mask in range(1 << colours)
        )
        assert orbit <= good
        for point in orbit:
            assert point not in bad
            assert all(matching[point] in orbit for matching in matchings)
            assert all(
                matchings[left][matchings[right][point]]
                == matchings[right][matchings[left][point]]
                for left in range(colours)
                for right in range(left + 1, colours)
            )
        assert len(orbit) & (len(orbit) - 1) == 0
        orbits.append(orbit)
        good.difference_update(orbit)
    return contaminated, tuple(orbits)


def assert_perfect_edge_disjoint(matchings: tuple[Matching, ...]) -> None:
    size = len(matchings[0])
    for colour, matching in enumerate(matchings):
        assert sorted(matching) == list(range(size))
        assert all(matching[matching[point]] == point for point in range(size))
        assert all(matching[point] != point for point in range(size))
        for other in matchings[:colour]:
            assert all(matching[point] != other[point] for point in range(size))


def one_switch_control() -> tuple[Matching, ...]:
    start = translation_matchings(6, START_SHIFTS)
    colour = 0
    matching = start[colour]
    candidate_matching = switched_matching(
        matching,
        (0, matching[0]),
        (60, matching[60]),
        False,
    )
    candidate = list(start)
    candidate[colour] = candidate_matching
    return tuple(candidate)


def random_perfect_matchings(size: int, colours: int, seed: int) -> tuple[Matching, ...]:
    rng = random.Random(seed)
    matchings = []
    used = [set() for _ in range(size)]
    for _ in range(colours):
        for _attempt in range(10_000):
            vertices = list(range(size))
            rng.shuffle(vertices)
            pairs = list(zip(vertices[::2], vertices[1::2]))
            if any(right in used[left] for left, right in pairs):
                continue
            matching = list(range(size))
            for left, right in pairs:
                matching[left] = right
                matching[right] = left
                used[left].add(right)
                used[right].add(left)
            matchings.append(tuple(matching))
            break
        else:
            raise AssertionError("could not generate edge-disjoint matchings")
    return tuple(matchings)


def main() -> None:
    translation = translation_matchings(6, START_SHIFTS)
    switched = one_switch_control()
    random_control = random_perfect_matchings(64, 8, 1208)
    for name, matchings in (
        ("translation", translation),
        ("one-switch", switched),
        ("random", random_control),
    ):
        assert_perfect_edge_disjoint(matchings)
        bad = commutator_bad_set(matchings)
        contaminated, orbits = stable_orbits(matchings)
        print(
            name,
            "bad",
            len(bad),
            "contaminated",
            len(contaminated),
            "stable-orbits",
            tuple(sorted(map(len, orbits))),
        )
    assert commutator_bad_set(translation) == frozenset()
    assert tuple(map(len, stable_orbits(translation)[1])) == (64,)
    print("corner-matching commutator stability: PASS")


if __name__ == "__main__":
    main()
