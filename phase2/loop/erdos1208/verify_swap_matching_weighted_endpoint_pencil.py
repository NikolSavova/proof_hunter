#!/usr/bin/env python3
"""Exact checks for the weighted endpoint-pencil gate."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import sys

from analyze_swap_optimal_nested_cores import profile, transformed_costas
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rotate,
    subtract,
)


Point = tuple[int, int]


def weighted_pencil_statistics(
    endpoint_sets: dict[int, frozenset[int]],
    weights: dict[tuple[int, int], int],
) -> tuple[int, int, int, Fraction]:
    adjacency: dict[int, dict[int, int]] = {
        vertex: {} for vertex in endpoint_sets
    }
    for (first, second), weight in weights.items():
        assert first < second and weight > 0
        assert endpoint_sets[first].isdisjoint(endpoint_sets[second])
        adjacency[first][second] = weight
        adjacency[second][first] = weight

    edge_mass = sum(weights.values())
    contact_wedges = 0
    pencil_mass = 0
    lambda_sum = 0
    theta = Fraction(0)
    for centre, neighbours in adjacency.items():
        rows = list(neighbours.items())
        contact_wedges += sum(
            first_weight * second_weight
            for (
                (first, first_weight),
                (second, second_weight),
            ) in combinations(rows, 2)
            if endpoint_sets[first] & endpoint_sets[second]
        )
        for endpoint in set().union(
            *(endpoint_sets[neighbour] for neighbour in neighbours)
        ):
            local_weights = [
                weight
                for neighbour, weight in rows
                if endpoint in endpoint_sets[neighbour]
            ]
            load = sum(local_weights)
            pair_mass = (
                load * load
                - sum(weight * weight for weight in local_weights)
            ) // 2
            lambda_sum += load
            pencil_mass += pair_mass
            if load:
                theta = max(theta, Fraction(pair_mass, load))

    assert contact_wedges <= pencil_mass
    assert lambda_sum == 8 * edge_mass
    assert pencil_mass <= 8 * theta * edge_mass
    return edge_mass, contact_wedges, pencil_mass, theta


def verify_finite_weighted_systems() -> None:
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
        weights = {
            pair: 1 + ((mask + index) % 3)
            for index, pair in enumerate(allowed)
            if mask >> index & 1
        }
        weighted_pencil_statistics(endpoint_sets, weights)

    # A single heavy parallel fibre contributes no contact-pencil pair mass.
    result = weighted_pencil_statistics(
        {0: frozenset(range(4)), 1: frozenset(range(4, 8))},
        {(0, 1): 1000},
    )
    assert result == (1000, 0, 0, Fraction(0))


def edge_roles(
    component: Point,
    centre: Point,
    p_value: Point,
    q_value: Point,
) -> tuple[Point, ...]:
    ell = add(component, linear(centre))
    base = subtract(centre, q_value)
    neighbour = add(centre, subtract(p_value, q_value))
    radius = add(component, rotate(add(centre, p_value)))
    return (
        base,
        neighbour,
        centre,
        add(neighbour, radius),
        add(centre, radius),
        add(component, linear(neighbour)),
        ell,
    )


def verify_centre_normal_form() -> None:
    component = (11, -7)
    centre = (3, 8)
    p_value = (-5, 4)
    q_value = (6, -2)
    ell = add(component, linear(centre))
    roles = edge_roles(component, centre, p_value, q_value)
    assert roles == (
        subtract(centre, q_value),
        add(centre, subtract(p_value, q_value)),
        centre,
        subtract(add(ell, linear(p_value)), q_value),
        add(ell, rotate(p_value)),
        add(ell, linear(subtract(p_value, q_value))),
        ell,
    )
    base, neighbour = roles[:2]
    assert subtract(centre, base) == q_value
    assert subtract(neighbour, base) == p_value


def verify_same_oriented_endpoint_collision() -> None:
    component = (13, -4)
    centre = (-2, 7)
    endpoint = (19, 11)
    other_first = (5, -3)
    other_second = (-8, 6)
    first_neighbour = subtract(endpoint, other_first)
    second_neighbour = subtract(endpoint, other_second)
    first_q = (4, -9)
    second_q = (-7, 3)
    first_p = add(first_q, subtract(first_neighbour, centre))
    second_p = add(second_q, subtract(second_neighbour, centre))

    first_roles = edge_roles(component, centre, first_p, first_q)
    second_roles = edge_roles(component, centre, second_p, second_q)
    delta = subtract(first_neighbour, second_neighbour)
    rho = rotate(subtract(first_p, second_p))
    differences = tuple(
        subtract(first_roles[index], second_roles[index])
        for index in (0, 1, 4, 3, 5)
    )
    assert differences == (
        add(delta, rotate(rho)),
        delta,
        rho,
        add(delta, rho),
        linear(delta),
    )
    assert delta == subtract(other_second, other_first)
    assert subtract(first_p, second_p) == tuple(-x for x in rotate(rho))
    assert subtract(first_q, second_q) == tuple(
        -x for x in add(delta, rotate(rho))
    )


def verify_genuine_profiles() -> None:
    expected = {
        17: (5, 129, 202, (6, 5)),
        23: (12, 53_281, 70_261, (53, 12)),
    }
    for prime, target in expected.items():
        points, differences = transformed_costas(prime)
        _, summary, _ = profile(differences, points)
        actual = dict(summary["matching_weighted_endpoint_pencil_profile"])
        row = (
            actual["maximum_weighted_endpoint_pencil"],
            actual["endpoint_contact_weighted_wedges"],
            actual["endpoint_pencil_wedge_upper"],
            actual["maximum_contact_pencil_ratio"],
        )
        assert row == target, (prime, row, target)


def verify_larger_profile() -> None:
    points, differences = transformed_costas(37)
    _, summary, _ = profile(differences, points)
    actual = dict(summary["matching_weighted_endpoint_pencil_profile"])
    assert actual["maximum_weighted_endpoint_pencil"] == 15
    assert actual["endpoint_contact_weighted_wedges"] == 617_488
    assert actual["endpoint_pencil_wedge_upper"] == 713_968
    assert actual["maximum_contact_pencil_ratio"] == (38, 7)


def main() -> None:
    verify_finite_weighted_systems()
    verify_centre_normal_form()
    verify_same_oriented_endpoint_collision()
    verify_genuine_profiles()
    if "--larger" in sys.argv:
        verify_larger_profile()
    print("SWAP MATCHING WEIGHTED ENDPOINT-PENCIL GATE: PASS")


if __name__ == "__main__":
    main()
