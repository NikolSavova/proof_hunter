#!/usr/bin/env python3
"""Checks the coloured mixed-support rectangle switch."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
import random


Vertex = tuple[str, int]
Edge = tuple[Vertex, Vertex]


def ordered_edge(left: Vertex, right: Vertex) -> Edge:
    assert left[0] == "V" and right[0] == "W"
    return left, right


def audit_graph(
    left: list[Vertex],
    right: list[Vertex],
    owners: dict[Edge, int],
) -> tuple[int, int, int, int, Counter[int]]:
    adjacency_left: dict[Vertex, set[Vertex]] = defaultdict(set)
    adjacency_right: dict[Vertex, set[Vertex]] = defaultdict(set)
    for first, second in owners:
        adjacency_left[first].add(second)
        adjacency_right[second].add(first)

    edges = len(owners)
    left_wedges = sum(
        len(adjacency_left[vertex]) * (len(adjacency_left[vertex]) - 1) // 2
        for vertex in left
    )
    right_wedges = sum(
        len(adjacency_right[vertex]) * (len(adjacency_right[vertex]) - 1) // 2
        for vertex in right
    )

    common_left: Counter[tuple[Vertex, Vertex]] = Counter()
    for neighbours in adjacency_left.values():
        for first, second in combinations(sorted(neighbours), 2):
            common_left[first, second] += 1
    common_right: Counter[tuple[Vertex, Vertex]] = Counter()
    for neighbours in adjacency_right.values():
        for first, second in combinations(sorted(neighbours), 2):
            common_right[first, second] += 1
    assert sum(common_left.values()) == left_wedges
    assert sum(common_right.values()) == right_wedges

    rectangles = sum(value * (value - 1) // 2 for value in common_left.values())
    assert rectangles == sum(
        value * (value - 1) // 2 for value in common_right.values()
    )
    maximum_common = max(
        (*common_left.values(), *common_right.values()),
        default=0,
    )

    owner_types: Counter[int] = Counter()
    cross_wedges = 0
    for vertex, neighbours in adjacency_left.items():
        for first, second in combinations(sorted(neighbours), 2):
            cross_wedges += owners[vertex, first] != owners[vertex, second]
    for vertex, neighbours in adjacency_right.items():
        for first, second in combinations(sorted(neighbours), 2):
            cross_wedges += owners[first, vertex] != owners[second, vertex]

    for first_left, second_left in combinations(left, 2):
        common = sorted(
            adjacency_left[first_left] & adjacency_left[second_left]
        )
        for first_right, second_right in combinations(common, 2):
            colours = (
                owners[ordered_edge(first_left, first_right)],
                owners[ordered_edge(first_left, second_right)],
                owners[ordered_edge(second_left, first_right)],
                owners[ordered_edge(second_left, second_right)],
            )
            transitions = sum(
                colours[first] != colours[second]
                for first, second in ((0, 1), (2, 3), (0, 2), (1, 3))
            )
            assert (len(set(colours)) == 1) == (transitions == 0)
            if transitions:
                assert transitions >= 2
            owner_types[transitions] += 1

    monochromatic = owner_types[0]
    nonmonochromatic = rectangles - monochromatic
    assert 2 * nonmonochromatic <= max(0, maximum_common - 1) * cross_wedges

    # Exact real-valued Cauchy lower bounds.
    if left:
        assert left_wedges >= Fraction(edges * edges, 2 * len(left)) - Fraction(
            edges, 2
        )
    if right:
        assert right_wedges >= Fraction(edges * edges, 2 * len(right)) - Fraction(
            edges, 2
        )
    right_pairs = len(right) * (len(right) - 1) // 2
    if right_pairs:
        assert rectangles >= Fraction(left_wedges * left_wedges, 2 * right_pairs) - Fraction(
            left_wedges, 2
        )
    left_pairs = len(left) * (len(left) - 1) // 2
    if left_pairs:
        assert rectangles >= Fraction(right_wedges * right_wedges, 2 * left_pairs) - Fraction(
            right_wedges, 2
        )

    return edges, rectangles, monochromatic, cross_wedges, owner_types


def verify_random_graphs() -> None:
    rng = random.Random(120812091)
    for _ in range(5000):
        left = [("V", index) for index in range(rng.randrange(1, 10))]
        right = [("W", index) for index in range(rng.randrange(1, 10))]
        owners = {}
        for first in left:
            for second in right:
                if rng.random() < 0.48:
                    owners[ordered_edge(first, second)] = rng.randrange(5)
        audit_graph(left, right, owners)


def verify_extreme_graphs() -> None:
    left = [("V", index) for index in range(7)]
    right = [("W", index) for index in range(8)]

    # One-group complete block: every rectangle is monochromatic.
    owners = {
        ordered_edge(first, second): 0
        for first in left
        for second in right
    }
    edges, rectangles, monochromatic, cross_wedges, owner_types = audit_graph(
        left, right, owners
    )
    assert edges == 56
    assert rectangles == 21 * 28
    assert monochromatic == rectangles
    assert cross_wedges == 0
    assert owner_types == Counter({0: rectangles})

    # Proper edge colours: every rectangle switches group at four vertices.
    owners = {
        ordered_edge(first, second): (first[1] + second[1]) % 8
        for first in left
        for second in right
    }
    _, rectangles, monochromatic, cross_wedges, owner_types = audit_graph(
        left, right, owners
    )
    assert monochromatic == 0
    assert owner_types[4] == rectangles
    assert cross_wedges > 0


def main() -> None:
    verify_random_graphs()
    verify_extreme_graphs()
    print("SWAP MIXED-SUPPORT RECTANGLE SWITCH: PASS")


if __name__ == "__main__":
    main()
