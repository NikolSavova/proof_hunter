#!/usr/bin/env python3
"""Exploratory translation-graph profile for B=A+JA.

For a greedy distance-Sidon set A, this measures the largest nonzero
autocorrelation r_{B-B}(t).  For the maximizing translation it also regards
B intersect (B+t) as a bipartite graph on the two A coordinates and counts
4-cycles.  This tests whether a Zarankiewicz-type sparsity statement could
underlie an energy bound.
"""

from collections import Counter

from analyze_rotated_triple_map import greedy


def add(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] + y[0], x[1] + y[1]


def sub(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] - y[0], x[1] - y[1]


def rot(x: tuple[int, int]) -> tuple[int, int]:
    return -x[1], x[0]


def c4_count(cells: list[tuple[int, int]]) -> int:
    rows: dict[int, set[int]] = {}
    for i, j in cells:
        rows.setdefault(i, set()).add(j)
    total = 0
    row_sets = list(rows.values())
    for p, left in enumerate(row_sets):
        for right in row_sets[p + 1 :]:
            common = len(left & right)
            total += common * (common - 1) // 2
    return total


def profile(side: int, trials: int) -> None:
    a = greedy(side, trials, 91208 + side)
    k = len(a)
    b: dict[tuple[int, int], tuple[int, int]] = {}
    for i, x in enumerate(a):
        for j, y in enumerate(a):
            point = add(x, rot(y))
            assert point not in b
            b[point] = (i, j)

    counts: Counter[tuple[int, int]] = Counter()
    points = list(b)
    for x in points:
        for y in points:
            if x != y:
                counts[sub(x, y)] += 1
    t, multiplicity = counts.most_common(1)[0]
    cells = [indices for point, indices in b.items() if sub(point, t) in b]
    degrees = Counter(i for i, _ in cells)
    print(
        "side", side,
        "k", k,
        "max_r", multiplicity,
        "max_r/k", round(multiplicity / k, 4),
        "rows", len(degrees),
        "max_row_degree", max(degrees.values()),
        "c4", c4_count(cells),
    )


if __name__ == "__main__":
    for m, attempts in [(20, 160), (40, 250), (80, 350), (120, 450)]:
        profile(m, attempts)
