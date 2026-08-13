#!/usr/bin/env python3
"""Explore the one-coordinate move component near the 20/115 family seed."""

from __future__ import annotations

import argparse
from collections import Counter, deque


TARGET = 116
SEED = (
    (0, 3, 34, 37, 40, 43),
    (6, 10, 14, 18, 22, 26, 30),
    (0, 1, 2, 68, 69, 70, 71),
)


def holes(state: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    I, J, K = state
    ij = {a + b for a in I for b in J}
    ik = {a + b for a in I for b in K}
    jk = {a + b for a in J for b in K}
    return tuple(
        q
        for q in range(TARGET)
        if not (q in ij or q in ik or (q > 0 and q - 1 in jk and q in jk))
    )


def explore(max_holes: int) -> tuple[int, Counter[int]]:
    queue = deque([(SEED, 0)])
    seen = {SEED}
    depths: Counter[int] = Counter()
    while queue:
        state, depth = queue.popleft()
        depths[depth] += 1
        for color, values in enumerate(state):
            for old in values:
                for new in range(TARGET):
                    if new in values:
                        continue
                    candidate = list(state)
                    candidate[color] = tuple(sorted((set(values) - {old}) | {new}))
                    next_state = tuple(candidate)
                    if next_state in seen:
                        continue
                    missing = holes(next_state)
                    if not missing:
                        print(f"FOUND at depth {depth + 1}: {next_state}")
                        return -1, depths
                    if len(missing) <= max_holes:
                        seen.add(next_state)
                        queue.append((next_state, depth + 1))
    return len(seen), depths


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-holes", type=int, default=6)
    args = parser.parse_args()
    size, depths = explore(args.max_holes)
    if size < 0:
        raise SystemExit(0)
    print(f"EXHAUSTED states={size} max_holes={args.max_holes} max_depth={max(depths)}")
    print("depth_counts", dict(sorted(depths.items())))


if __name__ == "__main__":
    main()
