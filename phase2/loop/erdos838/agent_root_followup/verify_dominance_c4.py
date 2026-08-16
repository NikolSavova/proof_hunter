#!/usr/bin/env python3
"""Exact finite audit for DOMINANCE_C4_SUPERSATURATION.md."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations_with_replacement, permutations, product
from math import ceil, log2
from random import Random


def c4(rows: list[int]) -> int:
    return sum((u & v).bit_count() ** 2 for u in rows for v in rows)


def check_bound(rows: list[int], b: int) -> None:
    a = len(rows)
    m = sum(x.bit_count() for x in rows)
    if not m:
        return
    s = ceil(log2(a + b)) + 1
    assert Fraction(c4(rows), 1) >= Fraction(m**3, 2 * a * b * s**3)


def ferrers_audit(limit: int = 8) -> int:
    checked = 0
    for a in range(1, limit + 1):
        for b in range(1, limit + 1):
            for ds in combinations_with_replacement(range(b + 1), a):
                m = sum(ds)
                if not m:
                    continue
                C = sum(min(x, y) ** 2 for x in ds for y in ds)
                assert 2 * a * b * C >= m**3
                checked += 1
    return checked


def permutation_audit(limit: int = 3) -> int:
    checked = 0
    # First-coordinate ranks and second-coordinate ranks are independent
    # permutations of all labelled vertices.  Exhaustion through 3+3 has
    # 720^2 raw pairs; quotient by fixing the first order.
    for a in range(1, limit + 1):
        for b in range(1, limit + 1):
            n = a + b
            labels = list(range(n))
            for second in permutations(labels):
                pos2 = [0] * n
                for rank, v in enumerate(second):
                    pos2[v] = rank
                rows = []
                for x in range(b, n):
                    mask = 0
                    for y in range(b):
                        if y < x and pos2[y] < pos2[x]:
                            mask |= 1 << y
                    rows.append(mask)
                check_bound(rows, b)
                checked += 1
    return checked


def random_audit(trials: int = 10_000) -> None:
    rng = Random(838)
    for _ in range(trials):
        a = rng.randrange(1, 30)
        b = rng.randrange(1, 30)
        pts = [(rng.random(), rng.random(), side)
               for side, count in ((0, b), (1, a)) for _ in range(count)]
        ys = [p for p in pts if p[2] == 0]
        xs = [p for p in pts if p[2] == 1]
        rows = []
        for x1, x2, _ in xs:
            mask = 0
            for j, (y1, y2, _) in enumerate(ys):
                if y1 < x1 and y2 < x2:
                    mask |= 1 << j
            rows.append(mask)
        check_bound(rows, b)


if __name__ == "__main__":
    f = ferrers_audit()
    p = permutation_audit()
    random_audit()
    print(f"PASS: {f} Ferrers sequences, {p} exact dominance orders, 10000 random")
