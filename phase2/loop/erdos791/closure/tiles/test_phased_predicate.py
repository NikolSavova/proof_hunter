#!/usr/bin/env python3
"""Regression tests for every clause in the enlarged phased predicate."""

from __future__ import annotations

import random
import unittest

from phased_predicate import coverage_bits
from phased_verify import basis
from staircase_family import obstruction_terms, parameters, placement


class PhasedPredicateTests(unittest.TestCase):
    def test_abstract_squares_are_literal(self) -> None:
        rng = random.Random(791_20260813)
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
                        self.assertTrue(
                            set(range(q * B, (q + 1) * B)) <= sums,
                            (t, q, p),
                        )

    def test_staircase_formula_and_obstruction(self) -> None:
        rng = random.Random(85_294)
        for _ in range(100):
            r = rng.randint(1, 10)
            u = rng.randint(r + 1, r + 12)
            s = rng.randint(r, 7 * r + 10)
            z = rng.randint(0, 10)
            _, _, D, _, m = parameters(r, u, s, z)
            p = placement(r, u, s, z, last_as_l0=bool(z and rng.randrange(2)))
            bits = coverage_bits(p, m + D + 8)
            missing = (~bits) & ((1 << (m + D + 8)) - 1)
            prefix = (missing & -missing).bit_length() - 1
            self.assertEqual(prefix, m)
            self.assertGreaterEqual(obstruction_terms(r, u, s, z)["gap_85ell2_minus_294m"], 0)


if __name__ == "__main__":
    unittest.main()
