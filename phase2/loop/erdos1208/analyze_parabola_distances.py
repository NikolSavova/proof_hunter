#!/usr/bin/env python3
"""Collision profile and greedy rainbow subsets for integer parabola points."""

from __future__ import annotations

import argparse
from collections import Counter
import random


def distance(a: int, b: int) -> int:
    return (a - b) ** 2 * (1 + (a + b) ** 2)


def profile(n: int):
    multiplicity = Counter(
        distance(a, b)
        for a in range(n)
        for b in range(a)
    )
    pairs = n * (n - 1) // 2
    collisions = sum(value * (value - 1) // 2 for value in multiplicity.values())
    return pairs, len(multiplicity), max(multiplicity.values(), default=0), collisions


def greedy(n: int, trials: int, seed: int):
    rng = random.Random(seed)
    best = []
    vertices = list(range(n))
    for _ in range(trials):
        rng.shuffle(vertices)
        selected = []
        used = set()
        for vertex in vertices:
            new = [distance(vertex, other) for other in selected]
            if len(set(new)) != len(new) or any(value in used for value in new):
                continue
            selected.append(vertex)
            used.update(new)
        if len(selected) > len(best):
            best = list(selected)
    return sorted(best)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max", type=int, default=1000)
    parser.add_argument("--trials", type=int, default=200)
    args = parser.parse_args()
    values = []
    n = 20
    while n <= args.max:
        values.append(n)
        n *= 2
    if values[-1] != args.max:
        values.append(args.max)
    for n in values:
        stats = profile(n)
        witness = greedy(n, args.trials, n)
        print(n, stats, len(witness), witness if n <= 100 else "")


if __name__ == "__main__":
    main()
