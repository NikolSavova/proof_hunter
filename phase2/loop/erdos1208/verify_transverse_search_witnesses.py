#!/usr/bin/env python3
"""Verify the exact witnesses found by search_transverse_local_gate.py."""

from __future__ import annotations

from search_rotated_support import is_distance_sidon, normalized
from search_transverse_local_gate import transverse_profile


Point = tuple[int, int]


WITNESSES: dict[int, list[Point]] = {
    12: [
        (0, 14), (10, 2), (13, 23), (16, 30), (20, 2), (25, 19),
        (26, 0), (26, 6), (27, 1), (27, 9), (29, 9), (29, 23),
    ],
    16: [
        (0, 2), (2, 31), (8, 0), (13, 12), (17, 25), (18, 19),
        (20, 18), (24, 29), (29, 40), (35, 7), (36, 8), (39, 9),
        (41, 9), (46, 0), (46, 1), (50, 25),
    ],
    20: [
        (0, 25), (0, 28), (3, 30), (10, 19), (10, 29), (11, 0),
        (14, 6), (15, 8), (15, 12), (16, 23), (20, 8), (20, 27),
        (23, 5), (25, 37), (32, 47), (34, 25), (36, 33), (41, 9),
        (50, 13), (51, 12),
    ],
}


EXPECTED = {
    12: (492, 22, 796),
    16: (926, 31, 1917),
    20: (3220, 35, 19733),
}


def main() -> None:
    for k, points in WITNESSES.items():
        assert len(points) == k
        assert len(set(points)) == k
        assert is_distance_sidon(points)
        assert normalized(points) == points
        profile = transverse_profile(points)
        assert profile == EXPECTED[k]
        edges, local, c4 = profile
        print(k, edges, local, c4)
    print("PASS")


if __name__ == "__main__":
    main()
