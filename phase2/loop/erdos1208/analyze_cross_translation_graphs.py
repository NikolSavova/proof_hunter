#!/usr/bin/env python3
"""Exploratory translation-graph profile for B=A+JA.

For a greedy distance-Sidon set A, this measures the largest nonzero
autocorrelation r_{B-B}(t).  For the maximizing translation it also regards
B intersect (B+t) as a bipartite graph on the two A coordinates and counts
4-cycles.  This tests whether a Zarankiewicz-type sparsity statement could
underlie an energy bound.
"""

from collections import Counter
from itertools import combinations

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


def max_common_neighbors(
    cells: list[tuple[int, int]], number_of_rows: int
) -> int:
    rows: dict[int, set[int]] = {}
    for i, j in cells:
        rows.setdefault(i, set()).add(j)
    answer = 0
    for chosen in combinations(rows.values(), number_of_rows):
        answer = max(answer, len(set.intersection(*chosen)))
    return answer


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
    differences = {
        sub(x, y)
        for x in a
        for y in a
        if x != y
    }
    rotated_differences = {rot(x) for x in differences}
    overlap = sum(
        1 for x in differences if sub(t, x) in rotated_differences
    )
    baseline = k * int(t in differences or t in rotated_differences)
    assert multiplicity == overlap + baseline
    degrees = Counter(i for i, _ in cells)
    print(
        "side", side,
        "k", k,
        "max_r", multiplicity,
        "max_r/k", round(multiplicity / k, 4),
        "M", overlap,
        "M/k", round(overlap / k, 4),
        "baseline", baseline,
        "rows", len(degrees),
        "max_row_degree", max(degrees.values()),
        "c4", c4_count(cells),
        "common3", max_common_neighbors(cells, 3),
        "common4", max_common_neighbors(cells, 4),
    )

    if k <= 20:
        all_cells: dict[tuple[int, int], list[tuple[int, int]]] = {}
        for x, indices in b.items():
            for y in points:
                if x != y:
                    all_cells.setdefault(sub(x, y), []).append(indices)
        global_common3 = max(
            max_common_neighbors(translation_cells, 3)
            for translation_cells in all_cells.values()
        )
        global_common4 = max(
            max_common_neighbors(translation_cells, 4)
            for translation_cells in all_cells.values()
        )
        print(
            "side", side,
            "global_common3", global_common3,
            "global_common4", global_common4,
        )


if __name__ == "__main__":
    for m, attempts in [(20, 160), (40, 250), (80, 350), (120, 450)]:
        profile(m, attempts)
