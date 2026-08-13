#!/usr/bin/env python3
"""Sampling baseline for lower-bound conjectures in Erdos problem 838.

For small n this samples general-position integer point sets and counts every
convex-position subset exactly (integer orientation tests only).  Its purpose
is falsification: proposed universal lower bounds should be tested here before
we try to prove them.
"""

from __future__ import annotations

import argparse
import random
from itertools import combinations

Point = tuple[int, int]


def det(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def general_position(points: tuple[Point, ...]) -> bool:
    return len(set(points)) == len(points) and all(
        det(a, b, c) != 0 for a, b, c in combinations(points, 3)
    )


def hull_size(points: tuple[Point, ...]) -> int:
    if len(points) <= 2:
        return len(points)
    pts = sorted(points)
    lower: list[Point] = []
    for p in pts:
        while len(lower) >= 2 and det(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper: list[Point] = []
    for p in reversed(pts):
        while len(upper) >= 2 and det(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return len(lower[:-1]) + len(upper[:-1])


def convex_profile(points: tuple[Point, ...]) -> tuple[int, ...]:
    """Counts convex subsets by size, including the empty set."""
    out = [1]
    for k in range(1, len(points) + 1):
        out.append(sum(
            hull_size(tuple(subset)) == k
            for subset in combinations(points, k)
        ))
    return tuple(out)


def random_set(rng: random.Random, n: int, radius: int) -> tuple[Point, ...]:
    while True:
        points = tuple(
            (rng.randrange(-radius, radius + 1),
             rng.randrange(-radius, radius + 1))
            for _ in range(n)
        )
        if general_position(points):
            return points


def search(n: int, samples: int, radius: int, seed: int) -> None:
    rng = random.Random(seed)
    best_total: int | None = None
    best_profile: tuple[int, ...] | None = None
    best_points: tuple[Point, ...] | None = None
    for sample in range(1, samples + 1):
        points = random_set(rng, n, radius)
        profile = convex_profile(points)
        total = sum(profile)
        if best_total is None or total < best_total:
            best_total, best_profile, best_points = total, profile, points
            print(
                f"n={n} sample={sample} new_best={total} "
                f"profile={profile} points={points}",
                flush=True,
            )
    assert best_total is not None and best_profile is not None
    print(f"FINAL n={n} best={best_total} profile={best_profile} points={best_points}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, nargs="+", default=[6, 10])
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--radius", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=838)
    args = parser.parse_args()
    for n in args.n:
        search(n, args.samples, args.radius, args.seed + n)


if __name__ == "__main__":
    main()
