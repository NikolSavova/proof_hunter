#!/usr/bin/env python3
"""Greedy falsification search for the adaptive eight-corner gate.

Starting from a relation of maximum adaptive degree in the 60-point heavy
closure, force new completions at its currently weakest endpoint corners.
Every accepted point preserves exact distance-Sidonicity.  This is search
machinery, not part of a proof or certificate.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from itertools import product

from search_rotated_support import is_distance_sidon
from search_transverse_closure import old_squared_distances, preserves_distance_sidon
from verify_transverse_closure_witness import POINTS
from verify_transverse_eight_corner_gate import (
    Point,
    add,
    representation_fibres,
    rotate,
    subtract,
)


Roles = tuple[tuple[int, int], tuple[int, int], tuple[int, int]]


EXTENSION_TO_100 = [
    (-121, 391), (315, 86), (229, -285), (130, -367), (-335, -84),
    (-135, 375), (511, 223), (370, 178), (-11, 490), (437, 53),
    (25, -326), (690, 3), (149, -260), (424, 39), (-692, 25),
    (1076, 158), (-867, -206), (-273, 851), (-898, -305), (111, -842),
    (1105, 170), (33, -729), (277, -802), (-63, -643), (-506, 100),
    (-565, 44), (559, -66), (-205, 1462), (1434, 253), (191, -1213),
    (1428, 111), (2652, 410), (-1473, -239), (3386, 409), (1484, 285),
    (229, -1444), (1460, 285), (2345, 439), (1399, 278), (364, -2231),
]

EXTENSION_101_TO_120 = [
    (429, -2589), (490, -1417), (867, 235), (796, 314),
    (296, -1429), (-308, 1441), (1355, 257), (360, -935),
    (373, -2297), (-528, -264), (-288, -838), (770, -277),
    (-218, 419), (-131, 1166), (-245, 1063), (-1005, -337),
    (-1112, -285), (111, -1205), (1251, 86), (236, -1279),
]


# Keep the same relation throughout the extension.  Re-optimizing the seed
# after every restart would measure a different extremal problem and would
# make the saved 60--100 chain impossible to resume reproducibly.
BASE_RELATION: Roles = ((37, 6), (36, 5), (9, 19))


def scale(value: int, point: Point) -> Point:
    return value * point[0], value * point[1]


def contribution(role: int, endpoint: int, point: Point) -> Point:
    if role == 0:
        return scale(1 if endpoint == 0 else -1, point)
    if role == 1:
        return scale(-1 if endpoint == 0 else 1, point)
    rotated = rotate(point)
    return scale(-1 if endpoint == 0 else 1, rotated)


def invert_contribution(role: int, endpoint: int, value: Point) -> Point:
    if role == 0:
        return scale(1 if endpoint == 0 else -1, value)
    if role == 1:
        return scale(-1 if endpoint == 0 else 1, value)
    rotated = rotate(value)
    return scale(1 if endpoint == 0 else -1, rotated)


def is_transverse_relation(points: list[Point], roles: Roles) -> bool:
    d = subtract(points[roles[0][0]], points[roles[0][1]])
    e = subtract(points[roles[2][0]], points[roles[2][1]])
    return e != (0, 0) and d[0] * e[0] + d[1] * e[1] != 0


def all_relations(points: list[Point]) -> list[Roles]:
    relations: list[Roles] = []
    for fibre in representation_fibres(points).values():
        for first in fibre:
            for second in fibre:
                if first == second:
                    continue
                roles: Roles = (
                    (second[1], second[2]),
                    (first[1], first[2]),
                    (second[0], first[0]),
                )
                if is_transverse_relation(points, roles):
                    relations.append(roles)
    return relations


def corner_key(roles: Roles, mask: int) -> tuple[int, int, int]:
    return tuple(roles[role][(mask >> role) & 1] for role in range(3))


def find_seed_relation(points: list[Point]) -> Roles:
    relations = all_relations(points)
    degrees = [Counter(corner_key(roles, mask) for roles in relations) for mask in range(8)]
    return max(
        relations,
        key=lambda roles: (
            min(degrees[mask][corner_key(roles, mask)] for mask in range(8)),
            tuple(degrees[mask][corner_key(roles, mask)] for mask in range(8)),
            roles,
        ),
    )


def completion_degrees(points: list[Point], base: Roles) -> list[int]:
    point_set = set(points)
    answer = [0] * 8
    for mask in range(8):
        fixed = (0, 0)
        for role in range(3):
            endpoint = (mask >> role) & 1
            fixed = add(fixed, contribution(role, endpoint, points[base[role][endpoint]]))
        unknown_endpoints = tuple(1 - ((mask >> role) & 1) for role in range(3))
        for first, second in product(points, repeat=2):
            partial = add(
                contribution(0, unknown_endpoints[0], first),
                contribution(1, unknown_endpoints[1], second),
            )
            needed = scale(-1, add(fixed, partial))
            third = invert_contribution(2, unknown_endpoints[2], needed)
            if third not in point_set:
                continue
            indices = (points.index(first), points.index(second), points.index(third))
            roles = [list(pair) for pair in base]
            for role in range(3):
                roles[role][unknown_endpoints[role]] = indices[role]
            candidate_roles: Roles = tuple(tuple(pair) for pair in roles)  # type: ignore[assignment]
            if is_transverse_relation(points, candidate_roles):
                answer[mask] += 1
    return answer


def forced_candidate_gains(
    points: list[Point], base: Roles
) -> dict[Point, list[int]]:
    point_set = set(points)
    gains: dict[Point, list[int]] = defaultdict(lambda: [0] * 8)
    for mask in range(8):
        fixed = (0, 0)
        unknown_endpoints = []
        for role in range(3):
            endpoint = (mask >> role) & 1
            fixed = add(fixed, contribution(role, endpoint, points[base[role][endpoint]]))
            unknown_endpoints.append(1 - endpoint)

        for missing_role in range(3):
            present_roles = [role for role in range(3) if role != missing_role]
            for chosen in product(range(len(points)), repeat=2):
                partial = fixed
                indices: list[int | None] = [None, None, None]
                for role, index in zip(present_roles, chosen):
                    indices[role] = index
                    partial = add(
                        partial,
                        contribution(role, unknown_endpoints[role], points[index]),
                    )
                needed = scale(-1, partial)
                candidate = invert_contribution(
                    missing_role, unknown_endpoints[missing_role], needed
                )
                if candidate in point_set:
                    continue

                # Check transversality using coordinates directly, before the
                # candidate has an index in the point list.
                opposite_points = [
                    candidate if role == missing_role else points[indices[role]]  # type: ignore[index]
                    for role in range(3)
                ]
                endpoints = []
                for role in range(3):
                    pair = [None, None]
                    selected = (mask >> role) & 1
                    pair[selected] = points[base[role][selected]]
                    pair[1 - selected] = opposite_points[role]
                    endpoints.append(pair)
                d = subtract(endpoints[0][0], endpoints[0][1])  # type: ignore[arg-type]
                e = subtract(endpoints[2][0], endpoints[2][1])  # type: ignore[arg-type]
                if e == (0, 0) or d[0] * e[0] + d[1] * e[1] == 0:
                    continue
                gains[candidate][mask] += 1
    return gains


def extend(points: list[Point], base: Roles, target: int) -> list[Point]:
    while len(points) < target:
        degrees = completion_degrees(points, base)
        gains = forced_candidate_gains(points, base)
        old_distances = old_squared_distances(points)
        best = None
        valid = 0
        for candidate, vector in gains.items():
            if not preserves_distance_sidon(candidate, points, old_distances):
                continue
            valid += 1
            new_degrees = tuple(degrees[i] + vector[i] for i in range(8))
            score = (min(new_degrees), sum(new_degrees), new_degrees, candidate)
            if best is None or score > best[0]:
                best = score, candidate
        if best is None:
            print("STOP", len(points), "no valid forced candidate", flush=True)
            break
        _, candidate = best
        points.append(candidate)
        assert is_distance_sidon(points)
        exact = completion_degrees(points, base)
        print(
            "STEP", len(points), candidate,
            "valid", valid,
            "degrees", exact,
            "minimum", min(exact),
            flush=True,
        )
    return points


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, choices=(60, 100, 120), default=120)
    parser.add_argument("--target", type=int, default=130)
    args = parser.parse_args()
    points = list(POINTS[:60])
    if args.start >= 100:
        points.extend(EXTENSION_TO_100)
    if args.start >= 120:
        points.extend(EXTENSION_101_TO_120)
    base = BASE_RELATION
    assert is_transverse_relation(points, base)
    assert is_distance_sidon(points)
    print("BASE", base, "degrees", completion_degrees(points, base), flush=True)
    points = extend(points, base, args.target)
    print("POINTS =", repr(points))


if __name__ == "__main__":
    main()
