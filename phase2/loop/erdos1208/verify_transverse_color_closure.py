#!/usr/bin/env python3
"""Exact certificate for the 65-point fixed-colour closure witness."""

from __future__ import annotations

from collections import Counter
from math import gcd

from search_rotated_support import is_distance_sidon, support_size
from search_transverse_color_closure import TRANSLATION, colour_count, is_transverse
from verify_transverse_local_gate import differences, local_overlap


POINTS = [
    (0, 2), (2, 31), (8, 0), (13, 12), (17, 25), (18, 19),
    (20, 18), (24, 29), (29, 40), (35, 7), (36, 8), (39, 9),
    (41, 9), (46, 0), (46, 1), (50, 25), (73, -3), (69, -15),
    (63, -6), (46, 7), (101, -28), (105, -27), (89, -21),
    (136, -51), (158, -55), (203, -86), (247, -107), (-120, 95),
    (296, -137), (-62, 68), (-183, 132), (-65, 68), (-74, 65),
    (-198, 139), (379, -190), (305, -145), (347, -167),
    (541, -276), (667, -350), (582, -297), (472, -230),
    (-277, 183), (694, -365), (394, -198), (331, -159),
    (-386, 251), (267, -125), (275, -133), (-40, 51),
    (-431, 281), (431, -221), (-241, 169), (-494, 306),
    (160, -68), (653, -342), (780, -418), (-311, 208),
    (-319, 202), (349, -164), (950, -510), (-371, 232),
    (-747, 454), (-798, 485), (-650, 395), (796, -425),
]

FIXED_EDGE = (0, -1)


def maximum_collinearity(points: list[tuple[int, int]]) -> int:
    answer = 1
    for index, point in enumerate(points):
        directions: Counter[tuple[int, int]] = Counter()
        for other_index, other in enumerate(points):
            if index == other_index:
                continue
            dx, dy = other[0] - point[0], other[1] - point[1]
            divisor = gcd(abs(dx), abs(dy))
            dx, dy = dx // divisor, dy // divisor
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            directions[dx, dy] += 1
        answer = max(answer, 1 + max(directions.values(), default=0))
    return answer


def transverse_colour_counts(difference_set: set[tuple[int, int]]) -> Counter[int]:
    counts: Counter[int] = Counter()
    for edge in difference_set:
        if edge == (0, 0):
            continue
        translation = (-edge[1], edge[0])
        counts[edge] = sum(
            translation[0] * source[1] - translation[1] * source[0] != 0
            and (
                source[0] + translation[0],
                source[1] + translation[1],
            )
            in difference_set
            for source in difference_set
        )
    return counts


def main() -> None:
    assert len(POINTS) == 65
    assert is_distance_sidon(POINTS)
    difference_set = differences(POINTS)
    assert FIXED_EDGE in difference_set
    assert TRANSLATION == (1, 0)
    assert colour_count(difference_set) == 1_010

    direct = sum(
        is_transverse(source)
        and (
            source[0] + TRANSLATION[0],
            source[1] + TRANSLATION[1],
        )
        in difference_set
        for source in difference_set
    )
    assert direct == 1_010

    local_counts = [local_overlap(edge, difference_set) for edge in difference_set]
    colour_counts = transverse_colour_counts(difference_set)
    assert sum(local_counts) == sum(colour_counts.values())
    assert sum(local_counts) == 45_044
    assert max(local_counts) == 43
    assert sum(value * value for value in local_counts) == 660_000
    assert max(colour_counts.values()) == 1_010
    assert sum(value * value for value in colour_counts.values()) == 12_509_352
    assert support_size(POINTS) == 251_195
    assert maximum_collinearity(POINTS) == 4

    print("points", len(POINTS))
    print("differences", len(difference_set))
    print("fixed_colour", direct)
    print("global_transverse", sum(local_counts))
    print("maximum_local", max(local_counts))
    print("maximum_colour", max(colour_counts.values()))
    print("row_second_moment", sum(value * value for value in local_counts))
    print("colour_second_moment", sum(value * value for value in colour_counts.values()))
    print("rotated_support", support_size(POINTS))
    print("maximum_collinearity", maximum_collinearity(POINTS))
    print("PASS")


if __name__ == "__main__":
    main()
