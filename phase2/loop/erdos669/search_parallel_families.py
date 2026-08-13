#!/usr/bin/env python3
"""Search rational parallel-family arrangements for many exact-k vertices.

This is a discovery tool, not a proof artifact.  A family (a,b,w) means the w
projective lines a*x+b*y=c with c in a centered interval of consecutive
integers.  All intersections are canonicalized in exact integer homogeneous
coordinates, so the reported multiplicity counts are exact.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import reduce
from itertools import combinations
from math import gcd
import random


def centered(width: int) -> range:
    return range(-(width // 2), width - width // 2)


def canonical(v: tuple[int, int, int]) -> tuple[int, int, int]:
    g = reduce(gcd, (abs(x) for x in v if x), 0)
    v = tuple(x // g for x in v)
    for x in v:
        if x:
            return v if x > 0 else tuple(-y for y in v)
    raise ValueError("zero projective vector")


def vertices(families: tuple[tuple[int, int, int], ...]) -> Counter[int]:
    lines = [canonical((a, b, -c)) for a, b, w in families for c in centered(w)]
    incidences: dict[tuple[int, int, int], set[int]] = {}
    for i, j in combinations(range(len(lines)), 2):
        a, b, c = lines[i]
        d, e, f = lines[j]
        p = (b * f - c * e, c * d - a * f, a * e - b * d)
        if p == (0, 0, 0):
            continue
        incidences.setdefault(canonical(p), set()).update((i, j))
    return Counter(map(len, incidences.values()))


def primitive_directions(radius: int) -> list[tuple[int, int]]:
    ans = []
    for a in range(0, radius + 1):
        for b in range(-radius, radius + 1):
            if (a, b) == (0, 0) or gcd(a, abs(b)) != 1:
                continue
            if a == 0 and b < 0:
                continue
            ans.append((a, b))
    return ans


def allocate(total: int, count: int, rng: random.Random) -> list[int]:
    cuts = sorted(rng.sample(range(2, total - 1), count - 1))
    widths = [cuts[0], *(b - a for a, b in zip(cuts, cuts[1:])), total - cuts[-1]]
    return widths if min(widths) >= 2 else allocate(total, count, rng)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--budget", type=int, default=70)
    parser.add_argument("--families", type=int, default=5)
    parser.add_argument("--radius", type=int, default=3)
    parser.add_argument("--trials", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=669)
    parser.add_argument("--k", type=int, default=4)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    directions = primitive_directions(args.radius)

    # The certified 3:3:4:4 construction is the search baseline when available.
    baseline = ((1, 0, 15), (0, 1, 15), (1, -1, 20), (1, 1, 20))
    counts = vertices(baseline)
    best = (counts[args.k] / args.budget**2, baseline, counts)
    print("baseline", best)

    for trial in range(args.trials):
        dirs = rng.sample(directions, args.families)
        widths = allocate(args.budget, args.families, rng)
        fam = tuple((*direction, width) for direction, width in zip(dirs, widths))
        counts = vertices(fam)
        score = counts[args.k] / args.budget**2
        if score > best[0]:
            best = (score, fam, counts)
            print("winner", trial, best, flush=True)
    print("best", best)


if __name__ == "__main__":
    main()
