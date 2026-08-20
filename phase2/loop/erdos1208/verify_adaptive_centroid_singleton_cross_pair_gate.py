#!/usr/bin/env python3
"""Checks for ADAPTIVE_CENTROID_SINGLETON_CROSS_PAIR_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from random import Random


Vector = tuple[int, ...]
Point = tuple[int, int]
Edge = tuple[int, int]


def add(first, second):
    return tuple(x + y for x, y in zip(first, second))


def subtract(first, second):
    return tuple(x - y for x, y in zip(first, second))


def chain_forms(length: int) -> tuple[list[Vector], list[Edge]]:
    """a=A, b=B, x_i=X_i, y_i=C+i(A-B)-X_i."""
    dimension = length + 4

    def form(coefficients: dict[int, int]) -> Vector:
        answer = [0] * dimension
        for index, coefficient in coefficients.items():
            answer[index] = coefficient
        return tuple(answer)

    points = [form({0: 1}), form({1: 1})]
    edges = []
    for index in range(length + 1):
        variable = index + 3
        first = len(points)
        points.extend(
            (
                form({variable: 1}),
                form({2: 1, 0: index, 1: -index, variable: -1}),
            )
        )
        edges.append((first, first + 1))
    return points, edges


def pair_sum_table(points) -> dict[Vector, Edge]:
    table = {}
    for edge in combinations(range(len(points)), 2):
        value = add(points[edge[0]], points[edge[1]])
        assert value not in table
        table[value] = edge
    return table


def clean_fibres(points) -> dict[tuple[int, int], set[Edge]]:
    pair_sums = pair_sum_table(points)
    fibres = {}
    for head, tail in permutations(range(len(points)), 2):
        q = subtract(points[head], points[tail])
        starts = set()
        for source_sum, source in pair_sums.items():
            target = pair_sums.get(add(source_sum, q))
            if target is not None and len({head, tail, *source, *target}) == 6:
                starts.add(source)
        if starts:
            fibres[head, tail] = starts
    return fibres


def triple_classes(points) -> dict[Vector, list[tuple[int, int, int]]]:
    classes = defaultdict(list)
    for triple in combinations(range(len(points)), 3):
        value = add(add(points[triple[0]], points[triple[1]]), points[triple[2]])
        classes[value].append(triple)
    return classes


def check_symbolic_chain() -> None:
    for length in range(2, 13):
        points, edges = chain_forms(length)

        directed = {}
        for ordered_edge in permutations(range(len(points)), 2):
            difference = subtract(points[ordered_edge[0]], points[ordered_edge[1]])
            assert difference not in directed
            directed[difference] = ordered_edge

        pair_sum_table(points)
        fibres = clean_fibres(points)
        q_forward = (0, 1)
        q_backward = (1, 0)
        assert fibres[q_forward] == set(edges[:-1])
        assert fibres[q_backward] == set(edges[1:])

        for first, second in combinations(range(length), 2):
            source_pair = {edges[first], edges[second]}
            common = [
                anchor for anchor, starts in fibres.items()
                if source_pair <= starts
            ]
            assert q_forward in common
            heads = Counter(head for head, _ in common)
            tails = Counter(tail for _, tail in common)
            assert heads[0] == 1
            assert tails[1] == 1

        classes = triple_classes(points)
        for triples in classes.values():
            for first, second in combinations(triples, 2):
                assert set(first).isdisjoint(second)

        companion_sets = []
        for index in range(length):
            centroid = add(points[0], add(points[edges[index][0]], points[edges[index][1]]))
            triples = classes[centroid]
            assert len(triples) == 2
            source_triple = next(triple for triple in triples if 0 in triple)
            assert set(source_triple) == {0, *edges[index]}
            companion = set().union(*map(set, triples)) - set(source_triple)
            assert companion == {1, *edges[index + 1]}
            companion_sets.append(companion)
        for first, second in combinations(companion_sets, 2):
            assert first & second == {1}

        vertices = length
        occurrence_edges = vertices * (vertices - 1) // 2
        unweighted_pair_functional_num = occurrence_edges * (occurrence_edges - 1) // 2
        assert 2 * unweighted_pair_functional_num >= (vertices - 1) ** 4 // 4
        assert 2 * vertices <= len(points) - 4
    print("symbolic centroid-chain singleton cliques n=2..12: PASS")


def check_cross_pair_identity() -> None:
    for length in range(0, 8):
        for loads in product(range(1, 6), repeat=length):
            ordered = sorted(loads, reverse=True)
            for quota in range(1, 10):
                split = min(quota, length)
                tail = sum(ordered[split:])
                cross = sum(
                    min(ordered[first], ordered[second])
                    for first in range(split)
                    for second in range(split, length)
                )
                assert cross == split * tail
                if quota <= length:
                    assert cross == quota * tail
                else:
                    assert tail == cross == 0
    print("exact top-tail minimum identity: PASS")


def distance2(first: Point, second: Point) -> int:
    x = first[0] - second[0]
    y = first[1] - second[1]
    return x * x + y * y


def numeric_chain_candidate(random: Random, length: int, radius: int) -> tuple[list[Point], list[Edge]]:
    def point() -> Point:
        return random.randint(-radius, radius), random.randint(-radius, radius)

    a, b, centre = point(), point(), point()
    points = [a, b]
    edges = []
    for index in range(length + 1):
        x = point()
        y = (
            centre[0] + index * (a[0] - b[0]) - x[0],
            centre[1] + index * (a[1] - b[1]) - x[1],
        )
        first = len(points)
        points.extend((x, y))
        edges.append((first, first + 1))
    return points, edges


def check_numeric_certificate() -> None:
    random = Random(1_208_202_608_20)
    length = 6
    radius = 10**6
    for attempt in range(1, 101):
        points, edges = numeric_chain_candidate(random, length, radius)
        if len(set(points)) != len(points):
            continue
        distances = [distance2(points[i], points[j]) for i, j in combinations(range(len(points)), 2)]
        if len(distances) != len(set(distances)):
            continue
        try:
            fibres = clean_fibres(points)
        except AssertionError:
            continue
        if fibres.get((0, 1)) != set(edges[:-1]):
            continue
        valid = True
        for first, second in combinations(range(length), 2):
            source_pair = {edges[first], edges[second]}
            common = [anchor for anchor, starts in fibres.items() if source_pair <= starts]
            heads = Counter(head for head, _ in common)
            tails = Counter(tail for _, tail in common)
            if (0, 1) not in common or heads[0] != 1 or tails[1] != 1:
                valid = False
                break
        if valid:
            break
    else:
        raise AssertionError("numeric chain finite-avoidance search exhausted")

    coordinate_span = max(max(point) for point in points) - min(min(point) for point in points)
    profile = (
        attempt,
        len(points),
        len(distances),
        len(fibres),
        len(fibres[0, 1]),
        length * (length - 1) // 2,
        coordinate_span,
    )
    assert profile == (1, 16, 120, 98, 6, 15, 8647623), profile
    print("integral distance-Sidon chain certificate", profile)


def main() -> None:
    check_symbolic_chain()
    check_cross_pair_identity()
    check_numeric_certificate()
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
