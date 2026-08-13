#!/usr/bin/env python3
"""Regression tests for exact point-footprint carry languages."""

from __future__ import annotations

import unittest

from automaton_predicate import coverage, prefix_length
from literal_verify import basis
from projective_triangle import transitions
from seven_slope_tiles import PHASE_RADIUS, SLOPES, admissible_scale, analytic_audit
from unbounded_cliques import admissible_scale as general_admissible
from unbounded_cliques import analytic_audit as general_audit
from unbounded_cliques import slope_family


class AutomatonTests(unittest.TestCase):
    def test_k7_symbolic_lattice_certificates(self) -> None:
        t = 251
        self.assertTrue(admissible_scale(t))
        rows = analytic_audit(t)
        self.assertEqual(len(rows), 21)
        self.assertTrue(
            all(
                row["divides_ab"]
                and row["required_radius"] <= PHASE_RADIUS
                and row["kernel_p"] == t * t
                and row["kernel_q"] == t * t
                and row["determinant"] == t * t
                and row["bounds_fit"]
                for row in rows
            )
        )

    def test_grid_macro_certificate_is_literal(self) -> None:
        p = {"V": {0}, **{f"R{a}": set() for a in SLOPES}}
        p["R0"] = {0}
        p["R10"] = {0, 1}
        p["R12"] = {0, 2}
        self.assertEqual(prefix_length(coverage(p, 20)), 4)
        t = 61
        B = t * t
        A = basis(p, t)
        sums = {x + y for x in A for y in A if x <= y}
        self.assertTrue(set(range(4 * B)) <= sums)

    def test_projective_triangle_trap(self) -> None:
        self.assertEqual(
            transitions(7),
            {"XY": ["XY", "YZ"], "YZ": ["XY", "YZ"], "XZ": ["XY", "YZ", "XZ"]},
        )

    def test_general_clique_algebra(self) -> None:
        r, t = 7, 3601
        self.assertEqual(slope_family(r), (0, 60, 120, 180, 240, 300, 360))
        self.assertTrue(general_admissible(t, r))
        self.assertTrue(
            all(
                row["kernel_p"] == t * t
                and row["kernel_q"] == t * t
                and row["determinant"] == t * t
                and row["bounds_fit"]
                for row in general_audit(t, r)
            )
        )


if __name__ == "__main__":
    unittest.main()
