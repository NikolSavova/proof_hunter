#!/usr/bin/env python3
"""Exact verifier for the swap-cell degeneracy charge in Erdős 1208."""

from __future__ import annotations

from collections import Counter, defaultdict
import heapq
import sys

from analyze_affine_costas_energy import is_distance_sidon, welch
from analyze_cross_endpoint_pair_charge import iter_records
from verify_determinant_prime_costas_resonance import ROWS, apply
from verify_orthogonal_two_support_gate import difference_set
from verify_radial_orthogonal_product_barrier import radial_set
from verify_seven_incidence_opposite_endpoint_charge import rich_fibres
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Cell = tuple[Point, Point]
Edge = tuple[Cell, Cell]
Fibre = tuple[Point, Point]
Profile = tuple[int, int, int, int, int, int, int]


def build_swap_multigraph(
    differences: set[Point],
) -> tuple[Counter[Edge], dict[Edge, list[Fibre]], int]:
    edge_multiplicity: Counter[Edge] = Counter()
    occurrences: dict[Edge, list[Fibre]] = defaultdict(list)
    ordered_mass = 0
    for fibre, q_forms, p_forms in iter_records(differences):
        first_cell = q_forms[0], p_forms[2]
        second_cell = p_forms[0], q_forms[2]
        assert first_cell != second_cell

        # Symmetric endpoint-core form from Section 7 of the note.
        base, ordinary_sum = fibre
        first_head, second_head = q_forms[0], p_forms[0]
        first_opposite = p_forms[2]
        linear_first = (
            first_head[0] - first_head[1],
            first_head[0] + first_head[1],
        )
        component = (
            first_opposite[0] - linear_first[0],
            first_opposite[1] - linear_first[1],
        )
        joined = (
            first_head[0] + second_head[0] - base[0],
            first_head[1] + second_head[1] - base[1],
        )
        rotated_joined = (-joined[1], joined[0])
        translation = (
            component[0] + rotated_joined[0],
            component[1] + rotated_joined[1],
        )
        assert (
            first_head[0] + translation[0],
            first_head[1] + translation[1],
        ) == p_forms[1]
        assert (
            second_head[0] + translation[0],
            second_head[1] + translation[1],
        ) == q_forms[1]
        assert component == (
            q_forms[2][0]
            - (second_head[0] - second_head[1]),
            q_forms[2][1]
            - (second_head[0] + second_head[1]),
        )
        assert base in differences
        assert ordinary_sum == (
            base[0] + first_opposite[0]
            + (second_head[0] - base[0])
            - (second_head[1] - base[1]),
            base[1] + first_opposite[1]
            + (second_head[0] - base[0])
            + (second_head[1] - base[1]),
        )
        edge = tuple(sorted((first_cell, second_cell)))
        if first_cell < second_cell:
            edge_multiplicity[edge] += 1
            occurrences[edge].append(fibre)
        ordered_mass += 1
    assert ordered_mass == 2 * sum(edge_multiplicity.values())
    assert all(
        edge_multiplicity[edge] == len(values)
        for edge, values in occurrences.items()
    )
    return edge_multiplicity, occurrences, ordered_mass


def degeneracy_orientation(
    edge_multiplicity: Counter[Edge],
) -> tuple[int, dict[Cell, int], dict[Cell, int]]:
    adjacency: dict[Cell, dict[Cell, int]] = defaultdict(dict)
    for (first, second), multiplicity in edge_multiplicity.items():
        adjacency[first][second] = multiplicity
        adjacency[second][first] = multiplicity

    current_degree = {
        vertex: sum(neighbours.values())
        for vertex, neighbours in adjacency.items()
    }
    heap = [(degree, vertex) for vertex, degree in current_degree.items()]
    heapq.heapify(heap)
    removed: set[Cell] = set()
    removal_rank: dict[Cell, int] = {}
    outdegree: dict[Cell, int] = {}
    degeneracy = 0

    while heap:
        degree, vertex = heapq.heappop(heap)
        if vertex in removed or degree != current_degree[vertex]:
            continue
        removal_rank[vertex] = len(removal_rank)
        removed.add(vertex)
        outdegree[vertex] = degree
        degeneracy = max(degeneracy, degree)
        for neighbour, multiplicity in adjacency[vertex].items():
            if neighbour in removed:
                continue
            current_degree[neighbour] -= multiplicity
            heapq.heappush(
                heap,
                (current_degree[neighbour], neighbour),
            )

    assert len(removal_rank) == len(adjacency)
    assert max(outdegree.values(), default=0) == degeneracy
    return degeneracy, removal_rank, outdegree


def charge_profile(differences: set[Point]) -> Profile:
    edge_multiplicity, occurrences, ordered_mass = build_swap_multigraph(
        differences
    )
    degeneracy, removal_rank, outdegree = degeneracy_orientation(
        edge_multiplicity
    )

    loads: Counter[tuple[int, Cell]] = Counter()
    local_keys: dict[Fibre, set[tuple[int, Cell]]] = defaultdict(set)
    for edge, multiplicity in edge_multiplicity.items():
        first, second = edge
        tail = first if removal_rank[first] < removal_rank[second] else second
        assert outdegree[tail] >= multiplicity
        for fibre in occurrences[edge]:
            # The two orientation bits distinguish the two ordered records
            # belonging to this unordered fibre pair.
            for orientation_bit in (0, 1):
                key = orientation_bit, tail
                assert key not in local_keys[fibre]
                local_keys[fibre].add(key)
                loads[key] += 1

    assert sum(loads.values()) == ordered_mass
    for vertex, degree in outdegree.items():
        assert loads[0, vertex] == degree
        assert loads[1, vertex] == degree

    charge_moment = sum(value * value for value in loads.values())
    assert charge_moment == 2 * sum(
        value * value for value in outdegree.values()
    )
    assert charge_moment <= degeneracy * ordered_mass

    _, support, _ = rich_fibres(differences, adaptive=True)
    return (
        len(differences),
        support,
        ordered_mass,
        len(outdegree),
        len(edge_multiplicity),
        degeneracy,
        charge_moment,
    )


def transformed_costas(
    prime: int,
    matrix: tuple[int, int, int, int] | None = None,
) -> set[Point]:
    if matrix is None:
        matrix, _ = ROWS[prime]
    points = [apply(matrix, point) for point in welch(prime)]
    assert is_distance_sidon(points)
    return difference_set(points)


def main() -> None:
    families: list[tuple[str, set[Point], Profile]] = [
        (
            "closure-30",
            difference_set(POINTS[:30]),
            (871, 62_273, 1_420, 1_382, 698, 2, 1_468),
        ),
        (
            "closure-40",
            difference_set(POINTS[:40]),
            (1_561, 156_057, 370_516, 216_909, 173_240, 9, 565_440),
        ),
        (
            "Costas-11",
            transformed_costas(11),
            (91, 707, 2_264, 1_558, 992, 4, 3_264),
        ),
        (
            "Costas-17",
            transformed_costas(17),
            (241, 2_299, 20_014, 12_397, 8_089, 6, 34_234),
        ),
        (
            "Costas-23",
            transformed_costas(23),
            (463, 4_513, 498_674, 133_927, 145_055, 12, 1_873_578),
        ),
        (
            "Costas-31",
            transformed_costas(31),
            (871, 9_495, 765_102, 286_810, 249_531, 19, 2_509_386),
        ),
        (
            "radial-4",
            radial_set(4),
            (29, 121, 8_330, 773, 1_417, 16, 67_646),
        ),
        (
            "radial-5",
            radial_set(5),
            (39, 181, 24_716, 1_437, 3_416, 26, 329_356),
        ),
        (
            "radial-6",
            radial_set(6),
            (53, 253, 93_290, 2_715, 8_881, 51, 2_377_470),
        ),
        (
            "radial-8",
            radial_set(8),
            (83, 431, 555_948, 6_769, 33_522, 121, 33_414_416),
        ),
    ]
    if "--extended" in sys.argv:
        families.extend(
            [
                (
                    "Costas-29",
                    transformed_costas(29),
                    (
                        757,
                        7_205,
                        1_522_546,
                        347_231,
                        409_109,
                        19,
                        7_241_154,
                    ),
                ),
                (
                    "Costas-37",
                    transformed_costas(37),
                    (
                        1_261,
                        13_917,
                        2_939_312,
                        837_964,
                        897_816,
                        18,
                        11_431_164,
                    ),
                ),
                (
                    "Costas-41",
                    transformed_costas(41),
                    (
                        1_561,
                        17_875,
                        4_629_690,
                        1_287_325,
                        1_366_981,
                        27,
                        19_155_158,
                    ),
                ),
                (
                    "Costas-43",
                    transformed_costas(43),
                    (
                        1_723,
                        19_819,
                        8_451_318,
                        1_910_376,
                        2_367_303,
                        31,
                        42_793_510,
                    ),
                ),
                (
                    "Costas-47-low-support",
                    transformed_costas(47, (-10, 11, 3, -8)),
                    (
                        2_071,
                        23_427,
                        25_194_336,
                        3_179_031,
                        5_430_646,
                        41,
                        210_516_264,
                    ),
                ),
            ]
        )

    for name, differences, expected in families:
        actual = charge_profile(differences)
        assert actual == expected, (name, actual, expected)
        number, support, mass, _, _, degeneracy, moment = actual
        adaptive_k = support / number
        print(
            name,
            actual,
            "degeneracy/K",
            degeneracy / adaptive_k if adaptive_k else 0.0,
            "charge-moment/(K mass)",
            moment / (adaptive_k * mass) if mass else 0.0,
        )

    print("SWAP-CELL DEGENERACY CHARGE: PASS")


if __name__ == "__main__":
    main()
