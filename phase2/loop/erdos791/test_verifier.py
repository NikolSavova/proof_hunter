#!/usr/bin/env python3
"""Small standard-library regression suite for the Erdős #791 verifier."""

import unittest

from verifier import DEFAULT_CERTIFICATE, load_certificate, prefix_length, tile_coverage


class CoverageTests(unittest.TestCase):
    def test_consecutive_parallelogram_rule_has_right_offset(self) -> None:
        # JK={3,4}; the adjacent pair certifies square 4, not square 3.
        self.assertEqual(tile_coverage(set(), {0, 1}, {3}), {4})

    def test_direct_square_rules(self) -> None:
        self.assertEqual(tile_coverage({2}, {3}, set()), {5})
        self.assertEqual(tile_coverage({2}, set(), {4}), {6})

    def test_kohonen_prefix(self) -> None:
        cert = load_certificate(DEFAULT_CERTIFICATE)
        covered = tile_coverage(cert["I"], cert["J"], cert["K"])
        self.assertEqual(prefix_length(covered), 510)
        self.assertNotIn(510, covered)
        self.assertEqual(sum(len(cert[key]) for key in ("I", "J", "K")), 42)


if __name__ == "__main__":
    unittest.main()
