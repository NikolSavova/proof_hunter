#!/usr/bin/env python3
"""Exact verifier for the fixed-endpoint four-corner stopping-set barrier."""

from __future__ import annotations

from collections import Counter, defaultdict, deque

from search_four_corner_core import (
    build_forms,
    has_distinct_forms,
    repeated_norms,
)
from search_rotated_support import is_distance_sidon
from verify_transverse_eight_corner_gate import relation_corner_keys


Point = tuple[int, int]


MATCHINGS = (
    (1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14),
    (10, 12, 14, 9, 7, 6, 5, 4, 15, 3, 0, 13, 1, 11, 2, 8),
    (8, 9, 12, 13, 10, 11, 14, 15, 0, 1, 4, 5, 2, 3, 6, 7),
    (3, 4, 11, 0, 1, 15, 8, 12, 6, 10, 9, 2, 7, 14, 13, 5),
)


POINTS: list[Point] = [
    (-9048621, -7744044),
    (3049367, 6256974),
    (3087513, -639438),
    (5906080, 5930828),
    (7175276, -4068084),
    (3980185, 909628),
    (-8695986, 2238058),
    (8284787, 3910653),
    (-1651015, -2986014),
    (6318754, -2705703),
    (8842200, 1494153),
    (1678991, -1500511),
    (-9311957, -9681893),
    (-8403910, -9108922),
    (8395133, -6065154),
    (22813910, -3481669),
    (15809662, -11914074),
    (16640333, -24592716),
    (10485487, -8364454),
    (3480984, -6822911),
    (16067107, -13710721),
    (21368618, -23606385),
    (8739007, -11597589),
    (19415967, -8629791),
    (-1186020, 7347123),
    (7590926, -11795836),
    (23744684, -26754902),
    (22459969, -25699756),
    (35662551, -38616599),
    (15045177, -24552578),
    (9451006, -21718636),
]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def rotate(value: Point) -> Point:
    return -value[1], value[0]


def verify_relations(relations: list[tuple[int, ...]]) -> None:
    assert len(relations) == 16
    for a0, a1, b0, b1, p, c1 in relations:
        d = subtract(POINTS[a0], POINTS[a1])
        f = subtract(POINTS[b0], POINTS[b1])
        e = subtract(POINTS[p], POINTS[c1])
        je = rotate(e)
        assert d == (f[0] + je[0], f[1] + je[1])
        assert e != (0, 0)
        assert d[0] * e[0] + d[1] * e[1] != 0

    corner_keys = [
        tuple(
            (
                relation[(mask & 1)],
                relation[2 + ((mask >> 1) & 1)],
                relation[4 + ((mask >> 2) & 1)],
            )
            for mask in range(8)
        )
        for relation in relations
    ]
    for mask in range(4):
        degrees = Counter(keys[mask] for keys in corner_keys)
        assert set(degrees.values()) == {2}
        assert len(degrees) == 8
    for mask in range(4, 8):
        degrees = Counter(keys[mask] for keys in corner_keys)
        assert set(degrees.values()) == {1}
        assert len(degrees) == 16


def simultaneous_core(relations: list[tuple[tuple[int, int, int], ...]], masks: tuple[int, ...]) -> set[int]:
    buckets: list[dict[tuple[int, int, int], set[int]]] = [defaultdict(set) for _ in range(8)]
    for index, keys in enumerate(relations):
        for mask in masks:
            buckets[mask][keys[mask]].add(index)
    active = set(range(len(relations)))
    queue = deque(
        index
        for index, keys in enumerate(relations)
        if any(len(buckets[mask][keys[mask]]) < 2 for mask in masks)
    )
    while queue:
        index = queue.popleft()
        if index not in active:
            continue
        active.remove(index)
        for mask in masks:
            bucket = buckets[mask][relations[index][mask]]
            bucket.discard(index)
            if len(bucket) == 1:
                queue.append(next(iter(bucket)))
    return active


def main() -> None:
    forms, subsystem = build_forms(MATCHINGS)
    assert len(forms) == len(POINTS) == 31
    assert has_distinct_forms(forms)
    assert repeated_norms(forms) == []
    assert is_distance_sidon(POINTS)
    verify_relations(subsystem)

    complete = relation_corner_keys(POINTS)
    assert len(complete) == 584
    profiles = (
        len(simultaneous_core(complete, (0, 1, 2, 3))),
        len(simultaneous_core(complete, (4, 5, 6, 7))),
        len(simultaneous_core(complete, tuple(range(8)))),
    )
    assert profiles == (32, 32, 0)
    print("four-corner stopping-set barrier", len(POINTS), len(subsystem), profiles)
    print("four-corner stopping-set barrier: PASS")


if __name__ == "__main__":
    main()
