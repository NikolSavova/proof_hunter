#!/usr/bin/env python3
"""Exact checks for SWAP_MATCHING_C4_COMMON_NEIGHBOUR_GATE.md."""

from __future__ import annotations

from itertools import combinations
from math import isqrt

from analyze_cross_endpoint_pair_charge import iter_records
from analyze_swap_optimal_nested_cores import profile, transformed_costas
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rotate,
    subtract,
)


Point = tuple[int, int]


def verify_edge_normal_form(prime: int) -> int:
    _, differences = transformed_costas(prime)
    checked = 0
    for (base, ordinary_sum), q_forms, p_forms in iter_records(differences):
        b_value = q_forms[0]
        c_value = p_forms[0]
        ell_b = p_forms[2]
        ell_c = q_forms[2]
        z_value = subtract(ell_b, linear(b_value))
        assert ell_c == add(z_value, linear(c_value))

        reconstructed_base = rotate(
            subtract(
                subtract(
                    subtract(ordinary_sum, z_value),
                    linear(b_value),
                ),
                linear(c_value),
            )
        )
        assert reconstructed_base == base
        assert (
            base,
            b_value,
            c_value,
            subtract(ordinary_sum, b_value),
            subtract(ordinary_sum, c_value),
            ell_c,
            ell_b,
        ) == (
            base,
            q_forms[0],
            p_forms[0],
            q_forms[1],
            p_forms[1],
            q_forms[2],
            p_forms[2],
        )

        q_value = subtract(b_value, base)
        p_value = subtract(c_value, base)
        assert q_value != p_value
        checked += 1
    return checked


def simple_degeneracy(adjacency: dict[int, set[int]]) -> int:
    remaining = set(adjacency)
    answer = 0
    while remaining:
        vertex = min(
            remaining,
            key=lambda item: len(adjacency[item] & remaining),
        )
        answer = max(answer, len(adjacency[vertex] & remaining))
        remaining.remove(vertex)
    return answer


def maximum_codegree(adjacency: dict[int, set[int]]) -> int:
    return max(
        (
            len(adjacency[first] & adjacency[second])
            for first, second in combinations(adjacency, 2)
        ),
        default=0,
    )


def verify_codegree_degeneracy_bound() -> None:
    # Exhaust every simple graph through six vertices.
    for number in range(1, 7):
        pairs = list(combinations(range(number), 2))
        for mask in range(1 << len(pairs)):
            adjacency = {vertex: set() for vertex in range(number)}
            for index, (first, second) in enumerate(pairs):
                if mask >> index & 1:
                    adjacency[first].add(second)
                    adjacency[second].add(first)
            degeneracy = simple_degeneracy(adjacency)
            codegree = maximum_codegree(adjacency)
            # d(d-1) <= r(h-1), with the forest case d<=1.
            assert degeneracy <= 1 or (
                degeneracy * (degeneracy - 1)
                <= codegree * (number - 1)
            )
            upper = 1 + isqrt(codegree * number)
            assert degeneracy <= upper


def verify_genuine_profiles() -> None:
    expected = {
        17: (
            (("components", 423),
             ("maximum_vertices", 5),
             ("maximum_simple_edges", 3),
             ("maximum_endpoint_pencil", 3),
             ("maximum_endpoint_pencil_vertex_product", 12)),
            (("opposite_pairs", 93),
             ("maximum_codegree", 1),
             ("four_cycles", 0),
             ("contact_pair_maximum_codegree", 1),
             ("clean_pair_maximum_codegree", 1),
             ("contact_pair_two_paths", 85),
             ("clean_pair_two_paths", 8)),
            (),
        ),
        23: (
            (("components", 10_496),
             ("maximum_vertices", 9),
             ("maximum_simple_edges", 14),
             ("maximum_endpoint_pencil", 5),
             ("maximum_endpoint_pencil_vertex_product", 45)),
            (("opposite_pairs", 19_701),
             ("maximum_codegree", 4),
             ("four_cycles", 1_492),
             ("contact_pair_maximum_codegree", 4),
             ("clean_pair_maximum_codegree", 3),
             ("contact_pair_two_paths", 14_852),
             ("clean_pair_two_paths", 7_611)),
            (
                ((14, 4), 532),
                ((13, 4), 377),
                ((15, 4), 360),
                ((12, 4), 98),
                ((16, 4), 76),
                ((11, 4), 20),
                ((13, 3), 8),
                ((13, -1), 4),
                ((14, -1), 4),
                ((11, -1), 4),
                ((10, -1), 4),
                ((14, 3), 2),
                ((10, 4), 2),
                ((12, -1), 1),
            ),
        ),
    }
    for prime, target in expected.items():
        points, differences = transformed_costas(prime)
        _, summary, _ = profile(differences, points)
        actual = (
            summary["matching_component_profile"],
            summary["matching_c4_profile"],
            summary["matching_c4_endpoints"],
        )
        assert actual == target, (prime, actual, target)


def main() -> None:
    assert verify_edge_normal_form(11) == 2_264
    assert verify_edge_normal_form(17) == 20_014
    verify_codegree_degeneracy_bound()
    verify_genuine_profiles()
    print("SWAP MATCHING-C4 COMMON-NEIGHBOUR GATE: PASS")


if __name__ == "__main__":
    main()
