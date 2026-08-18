#!/usr/bin/env python3
"""Exact checks for TRANSVERSE_FIXED_ROW_C4_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

from analyze_transverse_longest_charge import DIAMETER_POINTS
from verify_transverse_closure_witness import POINTS as HEAVY_POINTS
from verify_transverse_row_source_c4 import edge_map, row_sources, subtract, rotate


Point = tuple[int, int]
Relation = tuple[int, int, int, int]
ROLE_PAIRS = tuple(combinations(range(4), 2))


def fixed_row_relations(points: list[Point], row: Point) -> list[Relation]:
    """Return the unique (u,v,x,y) tuples in the transverse fixed row."""

    edges = edge_map(points)
    answer: list[Relation] = []
    for edge, (x, y) in edges.items():
        if edge == (0, 0) or row[0] * edge[0] + row[1] * edge[1] == 0:
            continue
        image = subtract(row, rotate(edge))
        if image not in edges:
            continue
        u, v = edges[image]
        answer.append((u, v, x, y))
    return answer


def projection_profile(
    relations: list[Relation], first: int, second: int
) -> tuple[int, int]:
    """Return (unlabelled C4 count, maximum pair-codegree)."""

    adjacency: dict[int, list[int]] = defaultdict(list)
    edge_pairs: set[tuple[int, int]] = set()
    for relation in relations:
        projected = relation[first], relation[second]
        assert projected not in edge_pairs
        edge_pairs.add(projected)
        adjacency[projected[0]].append(projected[1])

    common: Counter[tuple[int, int]] = Counter()
    for neighbours in adjacency.values():
        for pair in combinations(sorted(neighbours), 2):
            common[pair] += 1
    cycles = sum(value * (value - 1) // 2 for value in common.values())
    return cycles, max(common.values(), default=0)


def all_profiles(relations: list[Relation]) -> list[tuple[int, int]]:
    return [projection_profile(relations, i, j) for i, j in ROLE_PAIRS]


def verify_pair_linearity(points: list[Point], row: Point) -> None:
    relations = fixed_row_relations(points, row)
    for i, j in ROLE_PAIRS:
        assert len({(item[i], item[j]) for item in relations}) == len(relations)


def verify_fixed_row_tables() -> None:
    heavy_expected = {
        30: (119, [(100, 5), (72, 4), (68, 3), (63, 4), (87, 4), (59, 4)]),
        60: (339, [(462, 7), (476, 5), (450, 5), (492, 6), (433, 5), (449, 6)]),
        90: (614, [(1015, 7), (1058, 6), (1088, 7), (1068, 7), (1225, 8), (1081, 7)]),
        120: (948, [(1869, 7), (1922, 7), (1923, 7), (2008, 8), (2063, 8), (2071, 8)]),
    }
    for size, (count, profiles) in heavy_expected.items():
        points = HEAVY_POINTS[:size]
        relations = fixed_row_relations(points, (0, -1))
        assert len(relations) == count
        assert all_profiles(relations) == profiles
        verify_pair_linearity(points, (0, -1))
        print("heavy fixed row", size, count, profiles)

    diameter_expected = {
        35: (61, [(56, 5), (23, 4), (24, 3), (24, 4), (27, 3), (16, 3)]),
        45: (90, [(96, 5), (54, 4), (57, 4), (46, 4), (38, 3), (28, 3)]),
        70: (180, [(243, 7), (131, 4), (158, 6), (154, 6), (152, 4), (108, 7)]),
        90: (266, [(473, 9), (243, 6), (262, 6), (312, 6), (447, 6), (230, 7)]),
    }
    for size, (count, profiles) in diameter_expected.items():
        points = DIAMETER_POINTS[:size]
        relations = fixed_row_relations(points, (10_000, 0))
        assert len(relations) == count
        assert all_profiles(relations) == profiles
        verify_pair_linearity(points, (10_000, 0))
        print("diameter fixed row", size, count, profiles)


def projection_cycles(relations: list[Relation], first: int, second: int) -> set[tuple[int, ...]]:
    """Return each projection C4 as its sorted four relation indices."""

    adjacency: dict[int, dict[int, int]] = defaultdict(dict)
    for index, relation in enumerate(relations):
        left, right = relation[first], relation[second]
        assert right not in adjacency[left]
        adjacency[left][right] = index

    answer: set[tuple[int, ...]] = set()
    left_vertices = sorted(adjacency)
    for left_index, left in enumerate(left_vertices):
        for other in left_vertices[left_index + 1 :]:
            common = sorted(set(adjacency[left]) & set(adjacency[other]))
            for right, other_right in combinations(common, 2):
                answer.add(
                    tuple(
                        sorted(
                            (
                                adjacency[left][right],
                                adjacency[left][other_right],
                                adjacency[other][right],
                                adjacency[other][other_right],
                            )
                        )
                    )
                )
    return answer


def verify_cycle_nonredundancy() -> None:
    relations = fixed_row_relations(HEAVY_POINTS, (0, -1))
    families = [projection_cycles(relations, i, j) for i, j in ROLE_PAIRS]
    assert [len(family) for family in families] == [1869, 1922, 1923, 2008, 2063, 2071]
    union = set().union(*families)
    multiplicities = Counter(sum(cycle in family for family in families) for cycle in union)
    assert len(union) == 11_852
    assert multiplicities == {1: 11_850, 3: 2}
    print("projection cycle union", len(union), dict(multiplicities))


def row_pair_cycle_categories(points: list[Point]) -> tuple[int, int, int]:
    """Return row-source C4 mass for generic, D, and JD row differences."""

    rows = row_sources(points)
    row_list = list(rows)
    differences = set(row_list)
    turned_differences = {rotate(edge) for edge in differences}

    source_rows: dict[int, list[int]] = defaultdict(list)
    for row_index, row in enumerate(row_list):
        for source in rows[row]:
            source_rows[source].append(row_index)

    common: Counter[tuple[int, int]] = Counter()
    for indices in source_rows.values():
        for pair in combinations(indices, 2):
            common[pair] += 1

    categories = Counter()
    for (first, second), codegree in common.items():
        if codegree < 2:
            continue
        delta = subtract(row_list[first], row_list[second])
        mass = codegree * (codegree - 1) // 2
        assert not (delta in differences and delta in turned_differences)
        if delta in differences:
            categories["D"] += mass
        elif delta in turned_differences:
            categories["JD"] += mass
        else:
            categories["generic"] += mass
    return categories["generic"], categories["D"], categories["JD"]


def verify_row_pair_categories() -> None:
    expected = {
        20: (14_257, 11_443, 7_367),
        40: (2_525_415, 1_009_024, 749_608),
        60: (19_883_439, 5_399_578, 4_087_094),
    }
    for size, target in expected.items():
        value = row_pair_cycle_categories(HEAVY_POINTS[:size])
        assert value == target
        print("row-pair categories", size, value)


def main() -> None:
    verify_fixed_row_tables()
    verify_cycle_nonredundancy()
    verify_row_pair_categories()
    print("PASS")


if __name__ == "__main__":
    main()
