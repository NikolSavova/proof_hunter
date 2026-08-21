#!/usr/bin/env python3
"""Exact checks for the reverse endpoint-star incidence gate."""

from __future__ import annotations

from collections import Counter
from itertools import product

from analyze_affine_costas_energy import welch
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rotate,
    subtract,
)


Point = tuple[int, int]


def inverse_linear(value: Point) -> Point | None:
    if (value[0] + value[1]) % 2 or (value[1] - value[0]) % 2:
        return None
    return (
        (value[0] + value[1]) // 2,
        (value[1] - value[0]) // 2,
    )


def verify_reverse_normal_form() -> None:
    centre = (7, -4)
    ell = (3, 11)
    switch = (2, -3)
    q_value = (-5, 6)
    displacement = (4, 1)
    h_value = add(ell, rotate(centre))

    x_value = subtract(centre, q_value)
    y_value = add(h_value, add(rotate((-x_value[0], -x_value[1])), rotate(displacement)))
    z_value = add(h_value, add(rotate((-x_value[0], -x_value[1])), linear(displacement)))

    # Compare with the original Q_{C,t} formulas.
    assert y_value == add(ell, rotate(add(q_value, displacement)))
    assert z_value == add(add(ell, rotate(q_value)), linear(displacement))
    assert subtract(z_value, y_value) == displacement
    assert add(
        subtract(linear(y_value), rotate(z_value)), rotate(x_value)
    ) == h_value

    d_values = {
        x_value,
        add(x_value, switch),
        y_value,
        subtract(y_value, rotate(switch)),
        z_value,
        subtract(z_value, rotate(switch)),
    }
    popular = {
        q_value,
        subtract(q_value, switch),
        add(q_value, displacement),
        subtract(add(q_value, displacement), switch),
    }

    recovered = []
    for candidate_x in d_values:
        candidate_q = subtract(centre, candidate_x)
        candidate_y = add(
            h_value,
            add(rotate((-candidate_x[0], -candidate_x[1])), rotate(displacement)),
        )
        candidate_z = add(
            h_value,
            add(rotate((-candidate_x[0], -candidate_x[1])), linear(displacement)),
        )
        if not {
            candidate_x,
            add(candidate_x, switch),
            candidate_y,
            subtract(candidate_y, rotate(switch)),
            candidate_z,
            subtract(candidate_z, rotate(switch)),
        } <= d_values:
            continue
        if not {
            candidate_q,
            subtract(candidate_q, switch),
            add(candidate_q, displacement),
            subtract(add(candidate_q, displacement), switch),
        } <= popular:
            continue
        recovered.append(candidate_x)
    assert x_value in recovered

    key = (
        x_value,
        add(x_value, switch),
        y_value,
        subtract(y_value, rotate(switch)),
    )
    recovered_q = subtract(centre, key[0])
    recovered_t = subtract(z_value, y_value)
    assert recovered_q == q_value
    assert recovered_t == displacement

    # The same record is a square of four perpendicular completions.
    p_value = add(q_value, displacement)
    w_value = add(ell, linear(displacement))
    completions = {
        p_value: (x_value, ell),
        subtract(p_value, switch): (add(x_value, switch), ell),
        q_value: (x_value, w_value),
        subtract(q_value, switch): (add(x_value, switch), w_value),
    }
    completion_d = set()
    for shift_value, (first_start, second_start) in completions.items():
        completion_d.update(
            (
                first_start,
                add(first_start, shift_value),
                second_start,
                add(second_start, rotate(shift_value)),
            )
        )
    assert completion_d == d_values | {
        centre,
        add(centre, displacement),
        ell,
        add(ell, linear(displacement)),
    }
    assert subtract(w_value, ell) == linear(subtract(p_value, q_value))
    assert add(x_value, q_value) == centre

    # A crossed diagonal of the completion square globally reconstructs
    # the centre, switch, neighbour displacement, and both neighbour labels.
    diagonal_first = p_value, x_value, ell
    diagonal_second = (
        subtract(q_value, switch),
        add(x_value, switch),
        w_value,
    )
    recovered_u = subtract(diagonal_second[1], diagonal_first[1])
    recovered_q = add(diagonal_second[0], recovered_u)
    recovered_t = subtract(diagonal_first[0], recovered_q)
    recovered_c = add(diagonal_first[1], recovered_q)
    recovered_v = add(diagonal_first[1], diagonal_first[0])
    recovered_w = diagonal_second[2]
    assert recovered_u == switch
    assert recovered_q == q_value
    assert recovered_t == displacement
    assert recovered_c == centre
    assert recovered_v == add(centre, displacement)
    assert recovered_w == w_value
    assert subtract(recovered_w, diagonal_first[2]) == linear(recovered_t)
    assert (
        subtract(diagonal_first[0], recovered_u),
        diagonal_second[1],
        diagonal_first[2],
    ) in {
        (shift_value, first_start, second_start)
        for shift_value, (first_start, second_start) in completions.items()
    }
    assert (recovered_q, x_value, recovered_w) in {
        (shift_value, first_start, second_start)
        for shift_value, (first_start, second_start) in completions.items()
    }


def directed_differences(points: list[Point]) -> set[Point]:
    return {
        subtract(first, second)
        for first in points
        for second in points
        if first != second
    }


def assert_vector_sidon(values: set[Point]) -> None:
    seen: dict[Point, tuple[Point, Point]] = {}
    for first in values:
        for second in values:
            if first == second:
                continue
            difference = subtract(first, second)
            assert difference not in seen, (difference, seen[difference], (first, second))
            seen[difference] = first, second


def role_sets(points: list[Point], endpoint: Point, centre: Point, ell: Point) -> tuple[set[Point], ...]:
    first_head = {
        subtract(subtract(endpoint, other), centre)
        for other in points
        if other != endpoint
    }
    first_tail = {
        subtract(subtract(other, endpoint), centre)
        for other in points
        if other != endpoint
    }
    second_head = {
        preimage
        for other in points
        if other != endpoint
        for preimage in [inverse_linear(subtract(subtract(endpoint, other), ell))]
        if preimage is not None
    }
    second_tail = {
        preimage
        for other in points
        if other != endpoint
        for preimage in [inverse_linear(subtract(subtract(other, endpoint), ell))]
        if preimage is not None
    }
    return first_head, first_tail, second_head, second_tail


def verify_role_sidon_and_footprint() -> None:
    # The Welch graph is vector-Sidon; the affine transform avoids parity
    # degeneracy in the two L^{-1} role samples.
    points = [(3 * x + y, x + 4 * y) for x, y in welch(13)]
    assert_vector_sidon(set(points))
    differences = directed_differences(points)
    assert len(differences) == len(points) * (len(points) - 1)

    endpoint = points[0]
    centre = (5, -7)
    ell = (2, 8)
    roles = role_sets(points, endpoint, centre, ell)
    assert all(roles)
    for role in roles:
        assert_vector_sidon(role)

        sum_loads = Counter(
            add(rotate(first), linear(second))
            for first, second in product(role, repeat=2)
        )
        energy = sum(load * load for load in sum_loads.values())
        size = len(role)
        assert energy <= 2 * size * size - size
        assert len(sum_loads) * energy >= size**4
        assert 2 * len(sum_loads) >= size * size

        # Check the exact classification of every nonzero energy solution.
        solutions = 0
        for first, second, third, fourth in product(role, repeat=4):
            if add(rotate(first), linear(second)) != add(
                rotate(third), linear(fourth)
            ):
                continue
            solutions += 1
            d_value = subtract(first, third)
            e_value = subtract(fourth, second)
            assert rotate(d_value) == linear(e_value)
            assert d_value == subtract(e_value, rotate(e_value))
        assert solutions == energy


def main() -> None:
    verify_reverse_normal_form()
    verify_role_sidon_and_footprint()
    print("SWAP ENDPOINT REVERSE-STAR INCIDENCE GATE: PASS")


if __name__ == "__main__":
    main()
