#!/usr/bin/env python3
"""Exact experiments on strictly nested triangular cages.

Each new triangle is obtained by a positive rational stochastic map of the
previous triangle, so containment is certified by construction.  Convex
subsets are counted from orientation signs using endpoint cap/cup DPs; no
subset enumeration is needed.
"""

from __future__ import annotations

import argparse
import math
import random
from fractions import Fraction as F
from itertools import combinations


Point = tuple[F, F]


def orient(a: Point, b: Point, c: Point) -> int:
    z = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return (z > 0) - (z < 0)


def general_position(points: list[Point]) -> bool:
    return all(orient(points[i], points[j], points[k]) for i, j, k in combinations(range(len(points)), 3))


def child_triangle(parent: tuple[Point, Point, Point], rng: random.Random, denominator: int) -> tuple[Point, Point, Point]:
    """A random strict barycentric image of parent, rejecting degeneracy."""
    while True:
        rows = []
        for _ in range(3):
            raw = [rng.randint(1, denominator - 2) for _ in range(3)]
            total = sum(raw)
            rows.append(tuple(F(x, total) for x in raw))
        child = tuple(
            (
                sum(row[j] * parent[j][0] for j in range(3)),
                sum(row[j] * parent[j][1] for j in range(3)),
            )
            for row in rows
        )
        if orient(*child):
            return child  # every row is strictly positive, hence strict containment


def nested_triangles(depth: int, seed: int, denominator: int = 20) -> list[tuple[Point, Point, Point]]:
    rng = random.Random(seed)
    cages: list[tuple[Point, Point, Point]] = [
        ((F(0), F(0)), (F(100), F(0)), (F(0), F(100)))
    ]
    points = list(cages[0])
    while len(cages) < depth:
        candidate = child_triangle(cages[-1], rng, denominator)
        if general_position(points + list(candidate)):
            cages.append(candidate)
            points.extend(candidate)
    return cages


def chain_counts(points: list[Point], sign: int) -> dict[tuple[int, int], int]:
    points = sorted(points)
    n = len(points)
    result: dict[tuple[int, int], int] = {}
    for start in range(n):
        ending: dict[tuple[int, int], int] = {}
        for final in range(start + 1, n):
            ending[(start, final)] = 1
        for middle in range(start + 1, n):
            for final in range(middle + 1, n):
                value = ending.get((middle, final), 0)
                for previous in range(start, middle):
                    if (previous, middle) in ending and orient(points[previous], points[middle], points[final]) == sign:
                        value += ending[(previous, middle)]
                if value:
                    ending[(middle, final)] = value
        for final in range(start + 1, n):
            result[(start, final)] = sum(ending.get((middle, final), 0) for middle in range(start, final))
    return result


def convex_total(cages: list[tuple[Point, Point, Point]]) -> int:
    points = [p for cage in cages for p in cage]
    caps = chain_counts(points, -1)
    cups = chain_counts(points, 1)
    return len(points) + sum(caps[key] * cups[key] for key in caps)


def search(depth: int, samples: int, seed: int) -> None:
    best: tuple[int, int] | None = None
    for sample in range(samples):
        cages = nested_triangles(depth, seed + sample)
        value = convex_total(cages)
        if best is None or value < best[0]:
            best = (value, seed + sample)
            print(f"D={depth} sample={sample} W={value} log2W={math.log2(value):.6f} seed={seed+sample}", flush=True)
    print(f"FINAL D={depth} n={3*depth} best={best}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, nargs="+", default=[2, 3, 4, 5, 6, 8, 10])
    parser.add_argument("--samples", type=int, default=20)
    parser.add_argument("--seed", type=int, default=838)
    args = parser.parse_args()
    for depth in args.depth:
        search(depth, args.samples, args.seed + 1000 * depth)


if __name__ == "__main__":
    main()
