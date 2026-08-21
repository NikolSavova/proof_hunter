#!/usr/bin/env python3
"""Exact checks for the endpoint-pencil/clean-codegree reduction."""

from __future__ import annotations

from itertools import combinations, product
from math import isqrt
import sys

from analyze_swap_optimal_nested_cores import profile, transformed_costas
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rotate,
    subtract,
)


Point = tuple[int, int]


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


def verify_endpoint_pencil_bound(
    adjacency: dict[int, set[int]],
    endpoint_sets: dict[int, frozenset[int]],
) -> None:
    assert set(adjacency) == set(endpoint_sets)
    for first, neighbours in adjacency.items():
        for second in neighbours:
            assert first in adjacency[second]
            assert endpoint_sets[first].isdisjoint(endpoint_sets[second])

    endpoint_loads: dict[int, int] = {}
    for endpoints in endpoint_sets.values():
        assert len(endpoints) == 4
        for endpoint in endpoints:
            endpoint_loads[endpoint] = endpoint_loads.get(endpoint, 0) + 1
    pencil = max(endpoint_loads.values(), default=0)

    clean_codegree = max(
        (
            len(adjacency[first] & adjacency[second])
            for first, second in combinations(adjacency, 2)
            if endpoint_sets[first].isdisjoint(endpoint_sets[second])
        ),
        default=0,
    )
    degeneracy = simple_degeneracy(adjacency)
    size = len(adjacency)
    assert degeneracy <= 1 + isqrt((4 * pencil + clean_codegree) * size)


def verify_abstract_endpoint_systems() -> None:
    endpoint_sets = {
        0: frozenset((0, 1, 2, 3)),
        1: frozenset((4, 5, 6, 7)),
        2: frozenset((0, 8, 9, 10)),
        3: frozenset((4, 11, 12, 13)),
        4: frozenset((1, 11, 14, 15)),
        5: frozenset((5, 8, 16, 17)),
    }
    allowed = [
        pair
        for pair in combinations(endpoint_sets, 2)
        if endpoint_sets[pair[0]].isdisjoint(endpoint_sets[pair[1]])
    ]
    for mask in range(1 << len(allowed)):
        adjacency = {vertex: set() for vertex in endpoint_sets}
        for index, (first, second) in enumerate(allowed):
            if mask >> index & 1:
                adjacency[first].add(second)
                adjacency[second].add(first)
        verify_endpoint_pencil_bound(adjacency, endpoint_sets)


def edge_base(
    ordinary_sum: Point,
    component: Point,
    first: Point,
    second: Point,
) -> Point:
    return rotate(
        subtract(
            subtract(
                subtract(ordinary_sum, component),
                linear(first),
            ),
            linear(second),
        )
    )


def verify_fixed_clean_eight_corner_normal_form() -> None:
    b_value = (7, -3)
    c_value = (-4, 11)
    u_value = (5, 8)
    y_value = (2, -9)
    component = (13, -2)
    r_value = (-6, 4)
    displacement = subtract(c_value, b_value)
    ordinary_c = add(u_value, y_value)
    ordinary_b = add(ordinary_c, r_value)

    phi = rotate(
        subtract(
            subtract(y_value, component),
            linear(c_value),
        )
    )
    base_c = add(u_value, phi)
    rotation_shift = rotate(add(r_value, linear(displacement)))
    base_b = add(base_c, rotation_shift)
    assert base_c == edge_base(
        ordinary_c, component, c_value, u_value
    )
    assert base_b == edge_base(
        ordinary_b, component, b_value, u_value
    )

    roles = (
        u_value,
        add(component, linear(u_value)),
        y_value,
        add(y_value, r_value),
        subtract(add(u_value, y_value), c_value),
        subtract(add(add(u_value, y_value), r_value), b_value),
        add(u_value, phi),
        add(add(u_value, phi), rotation_shift),
    )
    assert roles == (
        u_value,
        add(component, linear(u_value)),
        subtract(ordinary_c, u_value),
        subtract(ordinary_b, u_value),
        subtract(ordinary_c, c_value),
        subtract(ordinary_b, b_value),
        base_c,
        base_b,
    )

    popular_shifts = (
        tuple(-entry for entry in phi),
        subtract(tuple(-entry for entry in phi), rotation_shift),
        subtract(subtract(c_value, u_value), phi),
        subtract(
            subtract(subtract(b_value, u_value), phi),
            rotation_shift,
        ),
    )
    assert popular_shifts == (
        subtract(u_value, base_c),
        subtract(u_value, base_b),
        subtract(c_value, base_c),
        subtract(b_value, base_b),
    )

    # The four coefficient projections u, y, u+y, u+Jy are pairwise
    # determining.  Exhaust a small box and check injectivity for every pair.
    rows = []
    for ux, uy, yx, yy in product(range(-2, 3), repeat=4):
        u = (ux, uy)
        y = (yx, yy)
        rows.append((u, y, add(u, y), add(u, rotate(y))))
    for first, second in combinations(range(4), 2):
        assert len({(row[first], row[second]) for row in rows}) == len(rows)


def verify_diagonal_invariance() -> None:
    # The same four ordinary sums give a repeated-r collision from either
    # diagonal of the four-cycle.
    for s01, s12, s23, s30 in product(range(-3, 4), repeat=4):
        first_diagonal = s01 - s12 == s30 - s23
        second_diagonal = s01 - s30 == s12 - s23
        assert first_diagonal == second_diagonal


def verify_genuine_profiles() -> None:
    expected = {
        17: (
            (('components', 423),
             ('maximum_vertices', 5),
             ('maximum_simple_edges', 3),
             ('maximum_endpoint_pencil', 3),
             ('maximum_endpoint_pencil_vertex_product', 12)),
            (('opposite_pairs', 93),
             ('maximum_codegree', 1),
             ('four_cycles', 0),
             ('contact_pair_maximum_codegree', 1),
             ('clean_pair_maximum_codegree', 1),
             ('contact_pair_two_paths', 85),
             ('clean_pair_two_paths', 8)),
            (),
        ),
        23: (
            (('components', 10_496),
             ('maximum_vertices', 9),
             ('maximum_simple_edges', 14),
             ('maximum_endpoint_pencil', 5),
             ('maximum_endpoint_pencil_vertex_product', 45)),
            (('opposite_pairs', 19_701),
             ('maximum_codegree', 4),
             ('four_cycles', 1_492),
             ('contact_pair_maximum_codegree', 4),
             ('clean_pair_maximum_codegree', 3),
             ('contact_pair_two_paths', 14_852),
             ('clean_pair_two_paths', 7_611)),
            (((2, False, False), 482),
             ((2, True, False), 372),
             ((1, False, False), 294),
             ((1, True, True), 264),
             ((0, False, False), 52),
             ((0, False, True), 28)),
        ),
    }
    for prime, target in expected.items():
        points, differences = transformed_costas(prime)
        _, summary, _ = profile(differences, points)
        actual = (
            summary['matching_component_profile'],
            summary['matching_c4_profile'],
            summary['matching_c4_contact_r_routes'],
        )
        assert actual == target, (prime, actual, target)
        for (contact_diagonals, repeated_contact, repeated_clean), _ in (
            summary['matching_c4_contact_r_routes']
        ):
            if contact_diagonals == 1:
                assert repeated_contact == repeated_clean


def verify_larger_profile() -> None:
    points, differences = transformed_costas(37)
    _, summary, _ = profile(differences, points)
    assert summary['matching_component_profile'] == (
        ('components', 68_223),
        ('maximum_vertices', 11),
        ('maximum_simple_edges', 30),
        ('maximum_endpoint_pencil', 6),
        ('maximum_endpoint_pencil_vertex_product', 55),
    )
    assert summary['matching_c4_profile'] == (
        ('opposite_pairs', 277_028),
        ('maximum_codegree', 7),
        ('four_cycles', 63_119),
        ('contact_pair_maximum_codegree', 7),
        ('clean_pair_maximum_codegree', 6),
        ('contact_pair_two_paths', 160_349),
        ('clean_pair_two_paths', 220_808),
    )
    assert summary['matching_c4_contact_r_routes'] == (
        ((1, True, True), 17_016),
        ((1, False, False), 15_192),
        ((0, False, True), 8_796),
        ((0, False, False), 8_016),
        ((2, True, False), 7_496),
        ((2, False, False), 6_603),
    )


def main() -> None:
    verify_abstract_endpoint_systems()
    verify_fixed_clean_eight_corner_normal_form()
    verify_diagonal_invariance()
    verify_genuine_profiles()
    if '--larger' in sys.argv:
        verify_larger_profile()
    print('SWAP MATCHING ENDPOINT-PENCIL/CLEAN-CODEGREE: PASS')


if __name__ == '__main__':
    main()
