#!/usr/bin/env python3
"""Inspect quarter-turn orbit occupancy for a fixed transverse row."""

from __future__ import annotations

from collections import Counter

from verify_transverse_closure_witness import POINTS
from verify_transverse_local_gate import differences


def rotate(point):
    return -point[1], point[0]


def transform(edge, row=(0, -1)):
    turned = rotate(edge)
    return row[0] - turned[0], row[1] - turned[1]


def main():
    dset = differences(POINTS)
    seen = set()
    occupancy = Counter()
    directed_edges = Counter()
    examples = {}
    for edge in dset:
        if edge in seen:
            continue
        orbit = []
        current = edge
        while current not in orbit:
            orbit.append(current)
            current = transform(current)
        assert current == edge and len(orbit) in (1, 2, 4)
        seen.update(orbit)
        present = tuple(item in dset for item in orbit)
        count = sum(present)
        occupancy[(len(orbit), count)] += 1
        adjacency = sum(
            present[index] and present[(index + 1) % len(orbit)]
            for index in range(len(orbit))
        )
        directed_edges[(len(orbit), count, adjacency)] += 1
        examples.setdefault((len(orbit), count, adjacency), orbit)
    print("occupancy", sorted(occupancy.items()))
    print("directed", sorted(directed_edges.items()))
    for key in sorted(examples):
        if key[2] >= 2:
            print(key, examples[key])


if __name__ == "__main__":
    main()
