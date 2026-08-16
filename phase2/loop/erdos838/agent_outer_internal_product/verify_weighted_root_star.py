#!/usr/bin/env python3
"""Exact audit for WEIGHTED_ROOT_STAR_MINIMIZER_OBSTRUCTION.md."""

import json
import sys
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS / "agent_reflection_gate"))
import reflection_order_gate as gate  # noqa: E402


def cross(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull_indices(points):
    order = sorted(range(len(points)), key=lambda i: points[i])
    if len(order) <= 1:
        return order
    lower = []
    for i in order:
        while (len(lower) >= 2
               and cross(points[lower[-2]], points[lower[-1]], points[i]) <= 0):
            lower.pop()
        lower.append(i)
    upper = []
    for i in reversed(order):
        while (len(upper) >= 2
               and cross(points[upper[-2]], points[upper[-1]], points[i]) <= 0):
            upper.pop()
        upper.append(i)
    return lower[:-1] + upper[:-1]


def convex(points):
    return len(set(points)) == len(points) == len(hull_indices(points))


def canonical_triples(face, points):
    if len(face) <= 2:
        return set()
    local = [points[i] for i in face]
    cyclic = [face[i] for i in hull_indices(local)]
    h = len(cyclic)
    triples = set()
    for i in range(h):
        for j in range(h):
            if j not in (i, (i + 1) % h):
                triples.add(tuple(sorted((cyclic[i], cyclic[(i + 1) % h],
                                          cyclic[j]))))
    assert len(triples) <= h * (h - 2)
    return triples


def main():
    metadata_path = ERDOS / "agent_lex_minimizer_search" / "exact_realizable_n9.json"
    metadata = json.loads(metadata_path.read_text())
    points = [tuple(point) for point in metadata["coordinates_as_stored"]]
    n = len(points)
    assert n == metadata["n"] == 9
    assert metadata["record_count"] == 158817
    assert metadata["minimum_trace"] == 168
    assert metadata["minimum_trace_count_in_database"] == 1

    assert all(cross(*triple) != 0 for triple in combinations(points, 3))
    degree = {}
    for triple in combinations(range(n), 3):
        degree[triple] = sum(
            not convex([points[i] for i in triple + (p,)])
            for p in range(n) if p not in triple)

    faces = []
    weights = Counter()
    bad_total = 0
    cover_total = 0
    for size in range(n + 1):
        for face in combinations(range(n), size):
            selected = [points[i] for i in face]
            if not convex(selected):
                continue
            faces.append(face)
            triples = canonical_triples(face, points)
            weights.update(triples)
            cover_total += sum(degree[t] for t in triples)
            bad_labels = [
                p for p in range(n) if p not in face
                and not convex(selected + [points[p]])
            ]
            assert all(any(not convex([points[i] for i in t] + [points[p]])
                           for t in triples)
                       for p in bad_labels)
            bad_total += len(bad_labels)

    v = len(faces)
    moment = sum(map(len, faces))
    rank = max(map(len, faces))
    assert (v, moment, rank) == (169, 492, 5)
    assert bad_total == n * v - 2 * moment == 537
    assert cover_total == sum(degree[t] * weights[t] for t in degree) == 1002
    assert sum(weights.values()) == 258

    d_zero = F(n * v - 2 * moment, (rank - 2) * moment)
    threshold = d_zero / 2
    heavy = {t for t in degree if degree[t] >= threshold}
    heavy_weight = sum(weights[t] for t in heavy)
    heavy_cover = sum(degree[t] * weights[t] for t in heavy)
    source_count = sum(
        bool(canonical_triples(face, points) & heavy) for face in faces)
    assert d_zero == F(179, 492) and threshold == F(179, 984)
    assert heavy_weight == 258
    assert heavy_cover == 1002
    assert source_count == 123
    assert heavy_weight * 2 * (n - 3) >= bad_total
    assert source_count * 2 * (n - 3) * rank * (rank - 2) >= bad_total

    outer = tuple(sorted(hull_indices(points)))
    assert outer == (0, 1, 8)
    assert degree[outer] == n - 3 == 6
    for p in range(n):
        if p not in outer:
            # The first three entries are the outer vertices; p is local index 3.
            assert 3 not in hull_indices(
                [points[i] for i in outer] + [points[p]])

    sorted_points = sorted(points)
    roots = tuple(
        (i, j)
        for _, i, j in sorted(
            (F(sorted_points[j][1] - sorted_points[i][1],
               sorted_points[j][0] - sorted_points[i][0]), i, j)
            for i in range(n) for j in range(i + 1, n)
        )
    )
    word = gate.word_from_roots(n, roots)
    here = gate.evaluate_word(n, word, graded=True)
    assert here.trace == 168 and here.first_moment == 492
    assert here.graded == (0, 9, 36, 84, 36, 3)
    histogram = Counter()
    for neighbor in gate.braid_neighbors_mod_commutation(n, word):
        other = gate.evaluate_word(n, neighbor)
        histogram[(other.trace - here.trace,
                   other.first_moment - here.first_moment)] += 1
    assert histogram == Counter({(2, 8): 8, (2, 10): 3})

    print("PASS: weighted root-star minimizer obstruction")
    print("  weighted identities: W=258, circuit cover=1002, bad demand=537")
    print("  high-root source faces: 123/169")
    print("  outer triple: degree 6=n-3")
    print("  braid neighbors: 8 x (+2,+8), 3 x (+2,+10)")


if __name__ == "__main__":
    main()
