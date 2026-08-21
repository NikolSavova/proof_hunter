#!/usr/bin/env python3
"""Exact checks for the weighted endpoint-pencil gate."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
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
    assert lambda_sum <= 8 * edge_mass
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
    weighted_pencil_statistics(
        {
            0: frozenset(),
            1: frozenset((0, 1)),
            2: frozenset((2, 3, 4, 5)),
        },
        {(0, 1): 7, (0, 2): 11},
    )


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


def verify_role_refined_key_rigidity() -> None:
    # The integer parabola is vector-Sidon: a nonzero directed difference
    # recovers both the index difference and the index sum.
    points = [(index, index * index) for index in range(7)]
    differences = {}
    for first, second in product(range(len(points)), repeat=2):
        if first == second:
            continue
        value = subtract(points[first], points[second])
        assert value not in differences
        differences[value] = first, second

    centre = (17, -9)
    endpoint = points[0]
    displacements = {
        index: subtract(subtract(endpoint, points[index]), centre)
        for index in range(1, len(points))
    }
    q_fibres = {
        index: [
            (3 * index + offset, 5 * index - 2 * offset)
            for offset in range(1 + index % 3)
        ]
        for index in displacements
    }

    key_neighbour_pairs: dict[
        tuple[Point, Point], set[tuple[int, int]]
    ] = {}
    for first_index, second_index in product(displacements, repeat=2):
        if first_index == second_index:
            continue
        first_t = displacements[first_index]
        second_t = displacements[second_index]
        for first_q in q_fibres[first_index]:
            for second_q in q_fibres[second_index]:
                first_p = add(first_q, first_t)
                second_p = add(second_q, second_t)
                key = (
                    subtract(first_t, second_t),
                    rotate(subtract(first_p, second_p)),
                )
                key_neighbour_pairs.setdefault(key, set()).add(
                    (first_index, second_index)
                )
    assert all(len(rows) == 1 for rows in key_neighbour_pairs.values())


def verify_common_r_unification() -> None:
    component = (9, -14)
    centre = (7, 2)
    first_t = (-5, 8)
    second_t = (6, -3)
    first_q = (4, 11)
    second_q = (-8, 5)
    first_p = add(first_q, first_t)
    second_p = add(second_q, second_t)
    first_roles = edge_roles(component, centre, first_p, first_q)
    second_roles = edge_roles(component, centre, second_p, second_q)

    displacement = subtract(first_t, second_t)
    eta = subtract(first_q, second_q)
    middle = rotate(add(eta, displacement))
    last = add(middle, displacement)
    assert (
        subtract(first_roles[0], second_roles[0]),
        subtract(first_roles[4], second_roles[4]),
        subtract(first_roles[3], second_roles[3]),
    ) == (tuple(-entry for entry in eta), middle, last)

    common_r = last
    common_displacement = tuple(-entry for entry in displacement)
    assert add(common_r, common_displacement) == middle
    assert rotate(add(common_r, linear(common_displacement))) == tuple(
        -entry for entry in eta
    )
    assert add(
        common_r,
        subtract(rotate(middle), middle),
    ) == tuple(-entry for entry in eta)


def verify_key_support_collision_fork() -> None:
    # Each entry is the multiplicity of one decorated key.  Exhausting
    # small lists checks both the local Cauchy fork and its global sum.
    local_rows: list[tuple[int, int, int]] = []
    for length in range(1, 6):
        for loads in product(range(1, 5), repeat=length):
            mass = sum(loads)
            support = len(loads)
            collisions = sum(load * (load - 1) // 2 for load in loads)
            assert mass * mass <= support * (mass + 2 * collisions)
            local_rows.append((mass, support, collisions))
    for first in local_rows[::97]:
        for second in local_rows[::113]:
            mass = first[0] + second[0]
            support = first[1] + second[1]
            collisions = first[2] + second[2]
            assert mass * mass <= support * (mass + 2 * collisions)
            if mass > 2 * support:
                assert collisions * 4 * support >= mass * mass


def verify_collision_orthogonal_switch() -> None:
    component = (5, -12)
    centre = (8, 3)
    first_t = (-4, 9)
    second_t = (7, -6)
    first_q = (11, -2)
    second_q = (-3, 10)
    shift = (6, 5)
    first_q_prime = subtract(first_q, shift)
    second_q_prime = subtract(second_q, shift)
    ell = add(component, linear(centre))

    for displacement, q_value, q_prime in (
        (first_t, first_q, first_q_prime),
        (second_t, second_q, second_q_prime),
    ):
        x_value = subtract(centre, q_value)
        x_prime = subtract(centre, q_prime)
        y_value = add(ell, rotate(add(q_value, displacement)))
        y_prime = add(ell, rotate(add(q_prime, displacement)))
        z_value = add(ell, add(rotate(q_value), linear(displacement)))
        z_prime = add(ell, add(rotate(q_prime), linear(displacement)))
        assert subtract(x_value, x_prime) == tuple(-entry for entry in shift)
        assert subtract(y_value, y_prime) == rotate(shift)
        assert subtract(z_value, z_prime) == rotate(shift)

    assert subtract(first_q, second_q) == subtract(
        first_q_prime, second_q_prime
    )
    assert add(first_q, second_q_prime) == add(
        first_q_prime, second_q
    )


def verify_genuine_profiles() -> None:
    expected = {
        17: (
            (5, 129, 202, (6, 5)),
            (5, 2, 3, 4, 2, 4, 2, 6, 1),
            (202, 200, 2),
        ),
        23: (
            (12, 53_281, 70_261, (53, 12)),
            (12, 4, 4, 10, 3, 9, 3, 50, 2),
            (70_261, 67_245, 3_140),
        ),
    }
    for prime, (target, copy_target, key_target) in expected.items():
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
        copy_row = summary["matching_endpoint_pencil_copy_profiles"][0][0]
        assert copy_row[:9] == copy_target, (prime, copy_row, copy_target)
        key_row = dict(summary["matching_endpoint_key_dichotomy"])
        assert (
            key_row["pair_mass"],
            key_row["support"],
            key_row["collisions"],
        ) == key_target
        assert key_row["pair_mass"] == actual["endpoint_pencil_wedge_upper"]
        assert key_row["pair_mass"] ** 2 <= key_row["support"] * (
            key_row["pair_mass"] + 2 * key_row["collisions"]
        )


def verify_larger_profile() -> None:
    points, differences = transformed_costas(37)
    _, summary, _ = profile(differences, points)
    actual = dict(summary["matching_weighted_endpoint_pencil_profile"])
    assert actual["maximum_weighted_endpoint_pencil"] == 15
    assert actual["endpoint_contact_weighted_wedges"] == 617_488
    assert actual["endpoint_pencil_wedge_upper"] == 713_968
    assert actual["maximum_contact_pencil_ratio"] == (38, 7)
    copy_row = summary["matching_endpoint_pencil_copy_profiles"][0][0]
    assert copy_row[:9] == (15, 3, 6, 8, 3, 10, 3, 50, 5)
    key_row = dict(summary["matching_endpoint_key_dichotomy"])
    assert (
        key_row["pair_mass"],
        key_row["support"],
        key_row["collisions"],
    ) == (713_968, 672_204, 44_110)
    assert key_row["pair_mass"] == actual["endpoint_pencil_wedge_upper"]
    assert key_row["pair_mass"] ** 2 <= key_row["support"] * (
        key_row["pair_mass"] + 2 * key_row["collisions"]
    )


def main() -> None:
    verify_finite_weighted_systems()
    verify_centre_normal_form()
    verify_same_oriented_endpoint_collision()
    verify_role_refined_key_rigidity()
    verify_common_r_unification()
    verify_key_support_collision_fork()
    verify_collision_orthogonal_switch()
    verify_genuine_profiles()
    if "--larger" in sys.argv:
        verify_larger_profile()
    print("SWAP MATCHING WEIGHTED ENDPOINT-PENCIL GATE: PASS")


if __name__ == "__main__":
    main()
