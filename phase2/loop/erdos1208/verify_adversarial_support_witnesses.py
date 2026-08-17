#!/usr/bin/env python3
"""Exact verifier for the stored adversarial rotated-support witnesses."""

from search_rotated_support import (
    is_distance_sidon,
    parallel_line_bound,
    support_size,
    translate_collision_profile,
)


WITNESSES = {
    12: [
        (0, 8), (3, 18), (5, 21), (8, 10), (8, 18), (11, 10),
        (13, 12), (15, 0), (15, 11), (15, 12), (16, 17), (21, 8),
    ],
    16: [
        (0, 10), (1, 25), (3, 13), (7, 4), (12, 3), (13, 2),
        (18, 33), (19, 17), (20, 35), (23, 7), (23, 9), (23, 10),
        (23, 18), (25, 17), (26, 0), (27, 12),
    ],
    20: [
        (0, 25), (0, 28), (3, 30), (10, 19), (10, 29), (11, 0),
        (14, 6), (15, 8), (15, 12), (16, 23), (20, 8), (20, 27),
        (23, 5), (25, 37), (32, 47), (34, 25), (36, 33), (41, 9),
        (50, 13), (51, 12),
    ],
    24: [
        (0, 64), (3, 55), (6, 66), (9, 44), (10, 40), (15, 3),
        (15, 15), (15, 38), (23, 7), (23, 35), (28, 13), (31, 40),
        (31, 80), (34, 61), (35, 36), (36, 64), (40, 0), (44, 54),
        (48, 37), (49, 34), (50, 41), (51, 17), (58, 39), (69, 47),
    ],
    28: [
        (0, 34), (8, 34), (17, 82), (18, 51), (23, 19), (38, 14),
        (39, 43), (40, 77), (44, 39), (46, 27), (48, 0), (49, 69),
        (49, 82), (51, 67), (54, 32), (54, 69), (55, 30), (61, 44),
        (62, 79), (62, 97), (68, 92), (71, 77), (75, 33), (79, 47),
        (79, 66), (86, 71), (101, 35), (114, 49),
    ],
}


EXPECTED = {
    12: (1083, 13, 656, 108, 3),
    16: (2669, 15, 1546, 184, 4),
    20: (5216, 7, 3220, 200, 3),
    24: (9468, 12, 4940, 244, 3),
    28: (15411, 23, 7402, 220, 2),
}


def main() -> None:
    for k, points in WITNESSES.items():
        assert len(points) == k
        assert is_distance_sidon(points)
        support = support_size(points)
        parallel, transverse = translate_collision_profile(points)
        line_bound, richness, _ = parallel_line_bound(points)
        assert (support, parallel, transverse, line_bound, richness) == EXPECTED[k]
        print(k, support, parallel, transverse, line_bound, richness)
    print("PASS")


if __name__ == "__main__":
    main()
