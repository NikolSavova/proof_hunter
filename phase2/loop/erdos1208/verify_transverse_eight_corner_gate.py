#!/usr/bin/env python3
"""Exact stress test for the adaptive eight-corner transverse gate.

For each transverse relation d=f+Je, choose one endpoint from each of its
three uniquely oriented A-edges.  There are eight such projections.  This
script computes every projection degree and verifies that each tested
relation is light in at least one corner, including the compact-anchor
third-moment obstruction.
"""

from collections import Counter, defaultdict

from search_rotated_support import is_distance_sidon
from verify_foreign_shift_averaging_barrier import build_instance
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Triple = tuple[int, int, int]


EXPECTED = {
    "closure-30": (26_428, 5, 41_696, (9, 10, 10, 9, 9, 10, 10, 9)),
    "closure-45": (107_720, 6, 191_272, (13, 12, 12, 13, 13, 12, 12, 13)),
    "closure-60": (259_516, 8, 477_864, (14,) * 8),
    "compact-anchor-117": (159_888, 6, 320_484, (6, 12, 12, 6, 6, 12, 12, 6)),
}


def add(x: Point, y: Point) -> Point:
    return x[0] + y[0], x[1] + y[1]


def subtract(x: Point, y: Point) -> Point:
    return x[0] - y[0], x[1] - y[1]


def rotate(x: Point) -> Point:
    return -x[1], x[0]


def representation_fibres(points: list[Point]) -> dict[Point, list[Triple]]:
    fibres: dict[Point, list[Triple]] = defaultdict(list)
    for a in range(len(points)):
        for b in range(len(points)):
            for c in range(len(points)):
                if b == c:
                    continue
                output = add(points[a], rotate(subtract(points[b], points[c])))
                fibres[output].append((a, b, c))
    return fibres


def relation_corner_keys(points: list[Point]) -> list[tuple[Triple, ...]]:
    relations: list[tuple[Triple, ...]] = []
    for fibre in representation_fibres(points).values():
        for first in fibre:
            for second in fibre:
                if first == second:
                    continue

                # If first=(a0,b0,c0) and second=(a1,b1,c1), equality
                # a0+J(b0-c0)=a1+J(b1-c1) becomes
                # d=f+Je for the three oriented endpoint pairs below.
                roles = (
                    (second[1], second[2]),
                    (first[1], first[2]),
                    (second[0], first[0]),
                )
                d = subtract(points[roles[0][0]], points[roles[0][1]])
                e = subtract(points[roles[2][0]], points[roles[2][1]])
                if e == (0, 0) or d[0] * e[0] + d[1] * e[1] == 0:
                    continue

                relations.append(
                    tuple(
                        tuple(roles[role][(mask >> role) & 1] for role in range(3))
                        for mask in range(8)
                    )
                )
    return relations


def verify(name: str, points: list[Point]) -> None:
    assert is_distance_sidon(points)
    relations = relation_corner_keys(points)
    projection_degrees = [Counter(keys[mask] for keys in relations) for mask in range(8)]
    minimum_degrees = [
        min(projection_degrees[mask][keys[mask]] for mask in range(8))
        for keys in relations
    ]
    profile = (
        len(relations),
        max(minimum_degrees),
        sum(minimum_degrees),
        tuple(max(degrees.values()) for degrees in projection_degrees),
    )
    assert profile == EXPECTED[name]
    print(
        name,
        "points", len(points),
        "relations", profile[0],
        "maximum adaptive degree", profile[1],
        "mean adaptive degree", profile[2] / profile[0],
    )


def main() -> None:
    verify("closure-30", POINTS[:30])
    verify("closure-45", POINTS[:45])
    verify("closure-60", POINTS[:60])
    _, _, compact_anchor_points = build_instance()
    verify("compact-anchor-117", compact_anchor_points)
    print("PASS")


if __name__ == "__main__":
    main()
