#!/usr/bin/env python3
"""Exact verifier for MAXIMAL_CUP_HISTORY_MIXED_BARRIER.md."""

from __future__ import annotations

from itertools import combinations
from math import comb

from verify_rooted_fan_complement import (
    add_coherent_root,
    convex_hull_size,
    cup_cap_set,
    genericize,
    orient,
    root_order,
)


def geometric_row(k: int) -> dict[str, object]:
    points = genericize(cup_cap_set(k, k))
    m = len(points)
    assert m == comb(2 * k - 4, k - 2)

    # Repeatedly taking the left child in the recursive construction leaves
    # E(k,3), which occupies the first k-1 positions.
    terminal = tuple(range(k - 1))
    assert len(terminal) == comb(k - 1, k - 2)
    assert all(
        orient(points[i], points[j], points[l]) > 0
        for i, j, l in combinations(terminal, 3)
    )
    assert convex_hull_size(tuple(points[i] for i in terminal)) == k - 1

    # If a larger convex face contained the terminal cup, deletion of all
    # but one added point would give a one-point convex extension.
    extensions = []
    for x in range(k - 1, m):
        candidate = terminal + (x,)
        if convex_hull_size(tuple(points[i] for i in candidate)) == k:
            extensions.append(x)
    assert not extensions

    rooted = add_coherent_root(points, 1)
    roots = root_order(rooted)
    time = {root: index for index, root in enumerate(roots)}
    history = tuple(index + 1 for index in terminal)
    path_edges = ((0, history[0]),) + tuple(
        (history[index], history[index + 1])
        for index in range(len(history) - 1)
    )
    path_times = tuple(time[edge] for edge in path_edges)
    assert all(a < b for a, b in zip(path_times, path_times[1:]))
    assert convex_hull_size((rooted[0],) + tuple(rooted[i] for i in history)) == k

    return {
        "k": k,
        "m": m,
        "history_rank": k,
        "extensions": len(extensions),
        "path_times": path_times,
    }


def symbolic_row(k: int) -> dict[str, object]:
    m = comb(2 * k - 4, k - 2)
    assert comb(k - 1, k - 2) == k - 1
    assert (1 << (2 * k - 4)) <= (2 * k - 3) * m

    # Squared exact form of (m+1)/2^k >= sqrt(m)/(4 sqrt(2k-3)).
    numerator = m + 1
    denominator = 1 << k
    assert numerator * numerator * 16 * (2 * k - 3) >= m * denominator * denominator
    return {
        "k": k,
        "m": m,
        "load_numerator": numerator,
        "load_denominator": denominator,
        "load": numerator / denominator,
    }


def main() -> None:
    geometry = [geometric_row(k) for k in (4, 5, 6)]
    symbols = [symbolic_row(k) for k in range(4, 41)]
    print("maximal cup-history mixed-bank barrier: PASS")
    for row in geometry:
        print(
            f"geometry E({row['k']},{row['k']}) m={row['m']:2d} "
            f"rank={row['history_rank']} extensions={row['extensions']} "
            f"times={row['path_times']}"
        )
    for k in (6, 8, 10, 12, 16, 20, 30, 40):
        row = symbols[k - 4]
        print(
            f"symbolic k={k:2d} m={row['m']:22d} "
            f"forced_load={row['load']:.6e}"
        )


if __name__ == "__main__":
    main()
