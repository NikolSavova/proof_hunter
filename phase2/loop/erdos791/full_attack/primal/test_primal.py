#!/usr/bin/env python3
"""Regression tests for the primal phased predicate and interleaved family."""

from __future__ import annotations

import random
import unittest

from interleaved_cycle import construct
from phased_predicate import coverage_bits, prefix_length
from primal_verify import basis


class PrimalTests(unittest.TestCase):
    def test_interleaved_formula(self) -> None:
        for k in range(1, 16):
            for h in range(2, 16):
                p, ell, m = construct(k, h)
                self.assertEqual(ell, 2 * k + 2 * h)
                self.assertEqual(m, 4 * k * h)
                self.assertEqual(prefix_length(coverage_bits(p, m + 32), m + 32), m)
                self.assertEqual(ell * ell - 4 * m, 4 * (k - h) ** 2)

    def test_random_abstract_squares_are_literal(self) -> None:
        rng = random.Random(791_314159)
        for t in (2, 4, 6, 8):
            B = t * t
            for _ in range(40):
                p = {
                    name: set(rng.sample(range(12), rng.randint(0, 4)))
                    for name in ("I", "J", "K", "L0", "L1")
                }
                bits = coverage_bits(p, 24)
                A = basis(p, t)
                sums = {x + y for x in A for y in A if x <= y}
                for q in range(24):
                    if bits >> q & 1:
                        self.assertTrue(set(range(q * B, (q + 1) * B)) <= sums)


if __name__ == "__main__":
    unittest.main()
