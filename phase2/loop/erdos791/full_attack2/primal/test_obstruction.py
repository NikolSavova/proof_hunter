#!/usr/bin/env python3
"""Regression tests for the unique-sum/chromatic role obstruction."""

from __future__ import annotations

import unittest

from role_defect_obstruction import (
    count_forced_defect,
    max_edges_after_deleting_to_r_colorable,
    representation_data,
)


class ObstructionTests(unittest.TestCase):
    def test_exact_turan_values(self) -> None:
        self.assertEqual(max_edges_after_deleting_to_r_colorable(8, 0, 4), 24)
        self.assertEqual(max_edges_after_deleting_to_r_colorable(8, 1, 4), 25)
        self.assertEqual(max_edges_after_deleting_to_r_colorable(4, 0, 8), 6)
        self.assertEqual(count_forced_defect(8, 25, 4), 1)

    def test_diagonal_bound_is_not_an_optimum_formula(self) -> None:
        counts, edges, loops = representation_data((0, 1, 3, 4, 5), 9)
        self.assertEqual(len(counts), 10)
        self.assertEqual(len(edges), 4)
        self.assertEqual({row["vertex"] for row in loops}, {0, 1})

    def test_present_role_graph_has_chromatic_number_four(self) -> None:
        roles = ("I", "J", "K", "L0", "L1")
        edges = {
            frozenset(edge)
            for edge in (
                ("I", "J"), ("I", "K"), ("I", "L0"), ("I", "L1"),
                ("J", "K"), ("J", "L0"), ("J", "L1"),
                ("K", "L0"), ("K", "L1"),
            )
        }
        clique = ("I", "J", "K", "L0")
        self.assertTrue(
            all(frozenset((a, b)) in edges for i, a in enumerate(clique) for b in clique[i + 1 :])
        )
        color = {"I": 0, "J": 1, "K": 2, "L0": 3, "L1": 3}
        self.assertTrue(all(color[a] != color[b] for a, b in map(tuple, edges)))
        self.assertEqual(set(roles), set(color))


if __name__ == "__main__":
    unittest.main()
