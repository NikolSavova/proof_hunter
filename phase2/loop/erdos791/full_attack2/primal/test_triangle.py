#!/usr/bin/env python3
"""Literal regression for the exact carry-triangle macro clause."""

from __future__ import annotations

import random
import unittest

from triangle_predicate import coverage_bits


def basis(p: dict[str, set[int]], t: int) -> set[int]:
    B = t * t
    E = {
        "I": set(range(t + 1)),
        "J": {i * t for i in range(t)},
        "K": {i * (t + 1) for i in range(t)},
        "L0": {i * (t - 1) for i in range(t + 1)},
        "L1": {1 + i * (t - 1) for i in range(t + 1)},
    }
    return {x + B * q for name, placements in p.items() for q in placements for x in E[name]}


class TriangleTests(unittest.TestCase):
    def test_random_abstract_squares_are_literal(self) -> None:
        rng = random.Random(791_848)
        for t in (2, 4, 6, 8):
            B = t * t
            for _ in range(50):
                p = {
                    name: set(rng.sample(range(14), rng.randint(0, 5)))
                    for name in ("I", "J", "K", "L0", "L1")
                }
                bits = coverage_bits(p, 28)
                A = basis(p, t)
                sums = {x + y for x in A for y in A if x <= y}
                for q in range(28):
                    if bits >> q & 1:
                        self.assertTrue(set(range(q * B, (q + 1) * B)) <= sums, (t, q, p))


if __name__ == "__main__":
    unittest.main()
