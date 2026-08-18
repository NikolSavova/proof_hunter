#!/usr/bin/env python3
"""Exact exploratory audit for the longest-edge transverse charge.

For a distance-Sidon point set A, enumerate transverse relations

    d = f + J e,       d,e,f in A-A.

The unique longest vector is charged with the relation.  Relations for which
``d`` is longest form a fixed-row family, represented by the endpoint edges
of ``e`` and ``f``.  Relations for which ``e`` is longest form a fixed-column
family, represented by the endpoint edges of ``d`` and ``f``.

The script tests whether each such family is independent in the union of its
two projected graphic matroids: equivalently, whether its relations can be
assigned to the two endpoint projections so that both assigned graphs are
forests.  The test uses the standard augmenting-path algorithm for matroid
intersection after duplicating every relation once for each projection.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass

from search_rotated_support import is_distance_sidon
from verify_transverse_closure_witness import POINTS as HEAVY_POINTS
from verify_transverse_row_source_c4 import EXTENSION


Point = tuple[int, int]
Edge = tuple[int, int]
Item = tuple[Edge, Edge]


DIAMETER_POINTS: list[Point] = [
    (10000, 0), (0, 0), (5612, -4466), (8654, -1554), (7480, 2291),
    (392, -751), (9641, -1143), (8838, 595), (8935, 1505),
    (2369, 3666), (3744, -1223), (3071, -3531), (7612, -3430),
    (4126, 4233), (3899, -2631), (4559, 727), (2136, 3928),
    (5570, -3911), (4976, 2614), (3478, -2375), (2740, 1559),
    (1932, 1377), (8004, 3513), (8526, 1022), (7924, -590),
    (7841, -547), (9189, -1914), (8915, 1103), (6943, 2875),
    (8454, -3186), (8988, 13), (1040, -1081), (291, 1484),
    (8799, 1431), (978, 318), (3910, -3568), (419, 1214),
    (2683, 4075), (4518, -4212), (9837, 1064), (9822, 725),
    (8956, 2861), (1769, 584), (9808, 1018), (6134, -4836),
    (1604, 3567), (6694, 4017), (9826, -662), (6504, 4362),
    (4039, 4810), (7340, 4360), (7463, -2210), (9915, -96),
    (6908, -2701), (6865, -2903), (1465, 3212), (2759, -2348),
    (2912, -736), (2368, -602), (9915, 353), (5418, 3714),
    (2966, -4336), (6256, -591), (6206, -4299), (1968, 3078),
    (9394, 2236), (2732, 3422), (255, -574), (9711, -341),
    (6509, -2757), (5146, 2750), (9303, -930), (8694, -1436),
    (8782, -1865), (6198, -4643), (6233, 3239), (8332, -1858),
    (7330, 2067), (5042, 4704), (5137, -3672), (8226, -555),
    (7370, -3261), (6990, -2493), (3203, 1709), (4869, 4240),
    (8539, -2334), (3104, 4575), (1905, -1037), (8067, -2821),
    (1959, 2985),
]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def norm2(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def edge_map(points: list[Point]) -> dict[Point, Edge]:
    return {
        subtract(points[i], points[j]): (i, j)
        for i in range(len(points))
        for j in range(len(points))
    }


def longest_families(points: list[Point]):
    """Return oriented fixed-row and fixed-column longest families.

    Only relations with ``d`` longest are inserted into ``rows``.  Relations
    with ``f`` longest are in bijection with these under
    ``(d,e,f) -> (f,-e,d)``.  Relations with ``e`` longest are inserted into
    ``columns`` directly.
    """

    edges = edge_map(points)
    labels = list(edges)
    label_set = set(labels)
    rows: dict[Point, list[Item]] = defaultdict(list)
    columns: dict[Point, list[Item]] = defaultdict(list)
    tie_count = 0
    relation_count = 0
    longest_counts = [0, 0, 0]
    for d in labels:
        if d == (0, 0):
            continue
        nd = norm2(d)
        for e in labels:
            if e == (0, 0) or d[0] * e[0] + d[1] * e[1] == 0:
                continue
            turned = rotate(e)
            f = d[0] - turned[0], d[1] - turned[1]
            if f == (0, 0) or f not in label_set:
                continue
            relation_count += 1
            ne, nf = norm2(e), norm2(f)
            maximum = max(nd, ne, nf)
            winners = (nd == maximum) + (ne == maximum) + (nf == maximum)
            if winners != 1:
                tie_count += 1
                continue
            if nd == maximum:
                longest_counts[0] += 1
                rows[d].append((edges[e], edges[f]))
            elif ne == maximum:
                longest_counts[1] += 1
                columns[e].append((edges[d], edges[f]))
            else:
                longest_counts[2] += 1
    return rows, columns, relation_count, tuple(longest_counts), tie_count


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))

    def find(self, vertex: int) -> int:
        while self.parent[vertex] != vertex:
            self.parent[vertex] = self.parent[self.parent[vertex]]
            vertex = self.parent[vertex]
        return vertex

    def union(self, left: int, right: int) -> bool:
        left, right = self.find(left), self.find(right)
        if left == right:
            return False
        self.parent[left] = right
        return True


@dataclass
class PartitionResult:
    rank: int
    assignment: list[int] | None


def matroid_union_rank(items: list[Item], vertex_count: int) -> PartitionResult:
    """Rank in the union of the two projected graphic matroids.

    Duplicate item ``i`` as ground elements ``2*i`` and ``2*i+1``.  The
    first matroid is the direct sum of the two graphic matroids.  The second
    is the partition matroid allowing at most one copy of each item.  Standard
    shortest augmenting paths find a maximum common independent set.
    """

    selected: set[int] = set()
    ground_size = 2 * len(items)

    while True:
        # Build the two selected forests and remember which selected ground
        # element labels every forest edge.
        forest_adjacency = [
            [[] for _ in range(vertex_count)],
            [[] for _ in range(vertex_count)],
        ]
        components = [UnionFind(vertex_count), UnionFind(vertex_count)]
        selected_copy: dict[int, int] = {}
        for copy in selected:
            item_index, side = divmod(copy, 2)
            left, right = items[item_index][side]
            assert components[side].union(left, right)
            forest_adjacency[side][left].append((right, copy))
            forest_adjacency[side][right].append((left, copy))
            assert item_index not in selected_copy
            selected_copy[item_index] = copy

        # In the matroid-intersection exchange graph, sources are unselected
        # copies addable to the direct-sum graphic matroid.  A selected copy x
        # has an arc x -> y precisely when x lies on y's fundamental cycle.
        sources: list[int] = []
        out_from_selected: dict[int, list[int]] = defaultdict(list)
        for candidate in range(ground_size):
            if candidate in selected:
                continue
            item_index, side = divmod(candidate, 2)
            left, right = items[item_index][side]
            if components[side].find(left) != components[side].find(right):
                sources.append(candidate)
                continue

            # Recover the unique path in the selected forest.
            parent: dict[int, tuple[int, int] | None] = {left: None}
            queue = deque([left])
            while queue and right not in parent:
                vertex = queue.popleft()
                for neighbour, copy in forest_adjacency[side][vertex]:
                    if neighbour in parent:
                        continue
                    parent[neighbour] = (vertex, copy)
                    queue.append(neighbour)
            assert right in parent
            vertex = right
            while vertex != left:
                previous, copy = parent[vertex]  # type: ignore[misc]
                out_from_selected[copy].append(candidate)
                vertex = previous

        # Sinks are unselected copies whose original item has no selected
        # copy.  Partition-matroid exchanges give the other arc direction.
        predecessor: dict[int, int | None] = {source: None for source in sources}
        queue = deque(sources)
        sink: int | None = None
        while queue and sink is None:
            current = queue.popleft()
            if current not in selected:
                item_index = current // 2
                occupying = selected_copy.get(item_index)
                if occupying is None:
                    sink = current
                    break
                neighbours = [occupying]
            else:
                neighbours = out_from_selected.get(current, [])
            for neighbour in neighbours:
                if neighbour in predecessor:
                    continue
                predecessor[neighbour] = current
                queue.append(neighbour)

        if sink is None:
            assignment: list[int] | None
            if len(selected) == len(items):
                assignment = [-1] * len(items)
                for copy in selected:
                    item_index, side = divmod(copy, 2)
                    assignment[item_index] = side
                assert all(side >= 0 for side in assignment)
            else:
                assignment = None
            return PartitionResult(len(selected), assignment)

        # Symmetric difference with the augmenting path.
        path: list[int] = []
        current: int | None = sink
        while current is not None:
            path.append(current)
            current = predecessor[current]
        for copy in path:
            if copy in selected:
                selected.remove(copy)
            else:
                selected.add(copy)

        # Cheap exact invariants catch an exchange-orientation error.
        assert len(selected) == len(selected_copy) + 1
        seen_items: set[int] = set()
        forests = [UnionFind(vertex_count), UnionFind(vertex_count)]
        for copy in selected:
            item_index, side = divmod(copy, 2)
            assert item_index not in seen_items
            seen_items.add(item_index)
            assert forests[side].union(*items[item_index][side])


def profile(name: str, points: list[Point], test_all: bool = True) -> None:
    assert is_distance_sidon(points)
    rows, columns, relation_count, role_counts, tie_count = longest_families(points)
    print(
        name,
        "k", len(points),
        "relations", relation_count,
        "roles", role_counts,
        "ties", tie_count,
        "max-row", max(map(len, rows.values()), default=0),
        "max-column", max(map(len, columns.values()), default=0),
    )
    assert tie_count == 0

    families = [("row", vector, items) for vector, items in rows.items()]
    families += [("column", vector, items) for vector, items in columns.items()]
    families.sort(key=lambda entry: len(entry[2]), reverse=True)
    if not test_all:
        families = families[:10]
    for family_name, vector, items in families:
        result = matroid_union_rank(items, len(points))
        if result.rank != len(items):
            print(
                "OBSTRUCTION", family_name, vector,
                "size", len(items), "union-rank", result.rank,
            )
            return
    print("two-forest PASS", name, "families", len(families))


def main() -> None:
    profile("heavy-30", HEAVY_POINTS[:30])
    profile("heavy-60", HEAVY_POINTS[:60], test_all=False)
    profile("heavy-120", HEAVY_POINTS, test_all=False)
    profile("heavy-122", HEAVY_POINTS + EXTENSION, test_all=False)
    profile("diameter-90", DIAMETER_POINTS)


if __name__ == "__main__":
    main()
