#!/usr/bin/env python3
"""Direct exact census of the vertical blow-up classification.

This deliberately uses a four-point skeleton that has an interior point, so
the test rejects non-convex macro block sets.  The micro set has both cap and
cup triples.  All 2^16 subsets of the rational realization are inspected.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations, product

from audit_geometry import Point, is_cap, is_convex, is_cup, orient_table


S = (
    Point(F(0), F(0)),
    Point(F(1), F(11)),       # interior to the unsheared triangle
    Point(F(2), F(23)),
    Point(F(4), F(40)),
)
Q = S
EPSILON = F(1, 128)


def points() -> tuple[Point, ...]:
    return tuple(
        Point(s.x + EPSILON**2 * q.x,
              s.y + EPSILON * q.y,
              word=f"{i}:{j}", block=i)
        for i, s in enumerate(S)
        for j, q in enumerate(Q)
    )


def nonempty_subsets(indices: tuple[int, ...]):
    for size in range(1, len(indices) + 1):
        yield from combinations(indices, size)


def main() -> None:
    pts = points()
    orient = orient_table(pts)
    macro = orient_table(S)
    micro = orient_table(Q)
    q = len(Q)

    actual: set[frozenset[int]] = set()
    failures = []
    for size in range(1, len(pts) + 1):
        for subset in combinations(range(len(pts)), size):
            if not is_convex(subset, orient):
                continue
            blocks = sorted({i // q for i in subset})
            if len(blocks) < 2:
                continue
            actual.add(frozenset(subset))
            pieces = {
                b: tuple(i for i in subset if i // q == b)
                for b in blocks
            }
            local_first = tuple(i % q for i in pieces[blocks[0]])
            local_last = tuple(i % q for i in pieces[blocks[-1]])
            ok = (
                is_cap(local_first, micro)
                and is_cup(local_last, micro)
                and all(len(pieces[b]) == 1 for b in blocks[1:-1])
                and is_convex(tuple(blocks), macro)
            )
            if not ok:
                failures.append(subset)

    predicted: set[frozenset[int]] = set()
    for size in range(2, len(S) + 1):
        for blocks in combinations(range(len(S)), size):
            if not is_convex(blocks, macro):
                continue
            first_indices = tuple(blocks[0] * q + j for j in range(q))
            last_indices = tuple(blocks[-1] * q + j for j in range(q))
            first_caps = [
                sub for sub in nonempty_subsets(first_indices)
                if is_cap(tuple(i % q for i in sub), micro)
            ]
            last_cups = [
                sub for sub in nonempty_subsets(last_indices)
                if is_cup(tuple(i % q for i in sub), micro)
            ]
            middle_choices = [
                tuple(b * q + j for j in range(q)) for b in blocks[1:-1]
            ]
            for cap, cup in product(first_caps, last_cups):
                for middle in product(*middle_choices):
                    predicted.add(frozenset((*cap, *middle, *cup)))

    assert not failures, failures[:3]
    assert actual == predicted, (
        list(actual - predicted)[:3], list(predicted - actual)[:3]
    )
    assert all(is_convex(tuple(sorted(x)), orient) for x in predicted)
    print(f"epsilon={EPSILON}; points={len(pts)}")
    print(f"spanning convex subsets: actual=predicted={len(actual)}")
    print("endpoint/intermediate/macro classification and converse: PASS")


if __name__ == "__main__":
    main()
