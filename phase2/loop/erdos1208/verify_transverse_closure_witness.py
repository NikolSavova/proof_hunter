#!/usr/bin/env python3
"""Exact certificate for the relation-closure adversary to the local gate."""

from __future__ import annotations

from collections import Counter

from search_rotated_support import is_distance_sidon
from verify_transverse_local_gate import differences, local_overlap


POINTS = [
    (0, 2), (2, 31), (8, 0), (13, 12), (17, 25), (18, 19),
    (20, 18), (24, 29), (29, 40), (35, 7), (36, 8), (39, 9),
    (41, 9), (46, 0), (46, 1), (50, 25), (12, 49), (16, 21),
    (39, 37), (45, -26), (70, 14), (-7, -19), (8, -34),
    (45, -29), (-46, 6), (-24, -44), (53, -58), (22, -65),
    (104, 24), (-42, 60), (-44, 57), (-44, -79), (100, 14),
    (61, -91), (126, -74), (66, 99), (-33, -5), (-64, -16),
    (-40, -120), (-97, -21), (-99, 68), (113, 76), (-60, 97),
    (100, -119), (-93, -107), (38, -171), (-91, -62),
    (-116, 132), (161, 158), (56, 169), (70, 189), (205, -42),
    (147, 83), (245, 108), (129, -218), (96, 229), (188, -64),
    (-26, -178), (-179, 115), (258, 93),
    (-158, -126), (-179, 29), (30, -188), (263, -134), (286, 80),
    (67, -269), (313, 30), (237, -265), (228, 260), (47, 293),
    (-184, 206), (357, 234), (297, -214), (184, -347), (361, 203),
    (-276, 238), (111, -329), (443, 233), (207, -360), (338, -329),
    (355, 320), (230, -460), (-4, -335), (-187, -253), (495, 4),
    (438, -132), (-237, -336), (170, -505), (487, -137), (-54, -451),
    (580, 5), (-236, -20), (599, -59), (-219, 284), (529, 152),
    (590, 285), (403, 349), (-241, 474), (-352, 26), (505, 425),
    (148, -497), (-160, -437), (-73, -295), (772, -147), (686, -237),
    (522, -448), (195, -693), (-477, -212), (575, -135), (193, 745),
    (648, -207), (333, -609), (230, 715), (219, -743), (175, -769),
    (813, 145), (1009, 134), (756, -481), (721, 1), (-87, -687),
]

FIXED_DIFFERENCE = (0, -1)


def subtract(left, right):
    return left[0] - right[0], left[1] - right[1]


def graph_rank(edges: list[tuple[int, int]], size: int) -> int:
    parent = list(range(size))

    def find(vertex: int) -> int:
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    rank = 0
    for left, right in edges:
        left, right = find(left), find(right)
        if left != right:
            parent[left] = right
            rank += 1
    return rank


def local_relations(points):
    edge = {
        subtract(points[i], points[j]): (i, j)
        for i in range(len(points))
        for j in range(len(points))
    }
    p, q = edge[FIXED_DIFFERENCE]
    relations = []
    for e, (x, y) in edge.items():
        if e == (0, 0) or e[1] == 0:
            continue
        f = e[1], -1 - e[0]
        if f in edge:
            u, v = edge[f]
            relations.append((u, v, x, y))
    return p, q, relations


def core_profile(points):
    p, q, relations = local_relations(points)
    core = [
        relation
        for relation in relations
        if p not in relation and q not in relation
    ]
    e_edges = [(x, y) for _, _, x, y in core]
    f_edges = [(u, v) for u, v, _, _ in core]
    return (
        len(core),
        graph_rank(e_edges, len(points)),
        graph_rank(f_edges, len(points)),
    )


def relation_degeneracy(points) -> int:
    _, _, relations = local_relations(points)
    hyperedges = [set(relation) for relation in relations]
    active_edges = set(range(len(hyperedges)))
    active_vertices = set(range(len(points)))
    degeneracy = 0
    while active_edges:
        degrees = Counter(
            vertex
            for edge_index in active_edges
            for vertex in hyperedges[edge_index]
        )
        vertex = min(active_vertices, key=lambda item: degrees[item])
        degeneracy = max(degeneracy, degrees[vertex])
        active_edges = {
            edge_index
            for edge_index in active_edges
            if vertex not in hyperedges[edge_index]
        }
        active_vertices.remove(vertex)
    return degeneracy


def main() -> None:
    for size, expected_local, expected_core in (
        (17, 36, (29, 13, 13)),
        (29, 113, (96, 26, 26)),
        (44, 216, (196, 41, 41)),
        (47, 237, (216, 44, 44)),
        (60, 339, (317, 57, 57)),
        (63, 364, (342, 60, 60)),
        (70, 422, (400, 67, 67)),
        (76, 478, (456, 73, 73)),
        (80, 514, (492, 77, 77)),
        (81, 525, (503, 78, 78)),
        (90, 614, (592, 87, 87)),
        (100, 719, (696, 97, 97)),
        (105, 773, (750, 102, 102)),
        (110, 830, (807, 107, 107)),
        (120, 948, (925, 117, 117)),
    ):
        points = POINTS[:size]
        assert is_distance_sidon(points)
        difference_set = differences(points)
        maximum, maximizing_d = max(
            (local_overlap(d, difference_set), d) for d in difference_set
        )
        assert maximum == expected_local
        assert local_overlap(FIXED_DIFFERENCE, difference_set) == maximum
        assert core_profile(points) == expected_core
        print(size, maximum, maximizing_d, expected_core)

    assert relation_degeneracy(POINTS) == 13
    print("degeneracy", 13)
    print("PASS")


if __name__ == "__main__":
    main()
