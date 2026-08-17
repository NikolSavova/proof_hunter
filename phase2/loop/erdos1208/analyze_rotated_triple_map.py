#!/usr/bin/env python3
"""Experimental stress test for the map (a,b,c) -> a + J(b-c).

This is exploratory only.  It greedily constructs distance-Sidon subsets of
square grids and measures the representation function of the rotated triple
map.  The output is intended to falsify overly optimistic multiplicity
conjectures before they enter a proof attempt.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import random


def greedy(m: int, trials: int, seed: int) -> list[tuple[int, int]]:
    rng = random.Random(seed)
    points = [(x, y) for x in range(m) for y in range(m)]
    best: list[tuple[int, int]] = []
    for _ in range(trials):
        rng.shuffle(points)
        chosen: list[tuple[int, int]] = []
        used: set[int] = set()
        for x, y in points:
            new = [(x - u) ** 2 + (y - v) ** 2 for u, v in chosen]
            if len(new) == len(set(new)) and used.isdisjoint(new):
                chosen.append((x, y))
                used.update(new)
        if len(chosen) > len(best):
            best = chosen[:]
    return best


def profile(a: list[tuple[int, int]]) -> tuple[int, int, int, float, int]:
    reps: Counter[tuple[int, int]] = Counter()
    # Exclude b=c: those k^2 diagonal triples all map to their apex a and
    # create an irrelevant representation spike of size k.
    for ax, ay in a:
        for bx, by in a:
            for cx, cy in a:
                if (bx, by) == (cx, cy):
                    continue
                # J(dx,dy)=(-dy,dx).
                reps[(ax - (by - cy), ay + (bx - cx))] += 1
    k = len(a)
    triples = k * k * (k - 1)
    energy = sum(v * v for v in reps.values())
    return k, len(reps), max(reps.values()), energy / triples, energy


def collision_types(a: list[tuple[int, int]]) -> Counter[tuple[int, int]]:
    """Count unordered pairs of distinct triples by overlap and union size."""
    fibres: defaultdict[tuple[int, int], list[tuple[int, int, int]]] = defaultdict(list)
    for ai, (ax, ay) in enumerate(a):
        for bi, (bx, by) in enumerate(a):
            for ci, (cx, cy) in enumerate(a):
                if bi == ci:
                    continue
                fibres[(ax - (by - cy), ay + (bx - cx))].append((ai, bi, ci))
    ans: Counter[tuple[int, int]] = Counter()
    for triples in fibres.values():
        for i, left in enumerate(triples):
            for right in triples[i + 1 :]:
                same_positions = sum(x == y for x, y in zip(left, right))
                ans[(same_positions, len(set(left + right)))] += 1
    return ans


def translate_incidence_profile(a: list[tuple[int, int]]) -> tuple[int, int, int]:
    """Return support size and the numbers of 6- and 8-cycle witnesses.

    The right vertices are the oriented differences d=b-c and the left
    vertices are points of A+J(A-A).  The neighbourhood of d is A+Jd.
    Vector-Sidon uniqueness makes this graph C4-free.  A 6-cycle is therefore
    exactly a triple of difference-columns whose three pairwise intersection
    points exist and are distinct.  The 8-cycle count is deliberately omitted
    for now; the returned third coordinate records the largest degree in the
    auxiliary column-intersection graph, which is the useful cheap diagnostic.
    """
    differences = {
        (bx - cx, by - cy)
        for bx, by in a
        for cx, cy in a
    }
    columns: dict[tuple[int, int], set[tuple[int, int]]] = {}
    for dx, dy in differences:
        columns[(dx, dy)] = {(ax - dy, ay + dx) for ax, ay in a}

    labels = list(columns)
    intersections: dict[tuple[int, int], tuple[int, int]] = {}
    neighbours: list[set[int]] = [set() for _ in labels]
    for i, left in enumerate(labels):
        for j in range(i):
            meet = columns[left] & columns[labels[j]]
            assert len(meet) <= 1
            if meet:
                intersections[(j, i)] = next(iter(meet))
                neighbours[i].add(j)
                neighbours[j].add(i)

    six_cycles = 0
    for i in range(len(labels)):
        higher = [j for j in neighbours[i] if j > i]
        for pos, j in enumerate(higher):
            for ell in higher[pos + 1 :]:
                if ell not in neighbours[j]:
                    continue
                points = {
                    intersections[tuple(sorted((i, j)))],
                    intersections[tuple(sorted((i, ell)))],
                    intersections[tuple(sorted((j, ell)))],
                }
                if len(points) == 3:
                    six_cycles += 1

    support = set().union(*columns.values())
    return len(support), six_cycles, max(map(len, neighbours), default=0)


def main() -> None:
    for m, trials in [(20, 200), (40, 120), (80, 50), (120, 25)]:
        a = greedy(m, trials, 1208 + m)
        k, image, max_rep, normalized_energy, energy = profile(a)
        print(
            f"m={m:3d} k={k:2d} image={image:6d} "
            f"k^3/image={k**3/image:7.3f} maxrep={max_rep:3d} "
            f"energy/k^3={normalized_energy:8.3f} energy={energy}"
        )
        if m == 40:
            print("  collision types (same positions, union size):", sorted(collision_types(a).items()))
        if m <= 40:
            support, six_cycles, max_column_degree = translate_incidence_profile(a)
            print(
                f"  translate graph: support={support} "
                f"C6={six_cycles} max-column-degree={max_column_degree}"
            )


if __name__ == "__main__":
    main()
