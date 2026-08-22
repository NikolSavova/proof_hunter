#!/usr/bin/env python3
"""Exact checks for SWAP_K24_PHYSICAL_OWNER_SUPPORT_NORMAL_FORM.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product


Point = tuple[int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def scale(coefficient: int, value: Point) -> Point:
    return coefficient * value[0], coefficient * value[1]


def rotate(value: Point) -> Point:
    return -value[1], value[0]


def linear(value: Point) -> Point:
    return add(value, rotate(value))


def norm(value: Point) -> int:
    return value[0] * value[0] + value[1] * value[1]


def difference_set(points: list[Point]) -> set[Point]:
    return {
        subtract(head, tail)
        for head in points
        for tail in points
        if head != tail
    }


def distance_sidon(points: list[Point]) -> bool:
    labels = [norm(subtract(left, right)) for left, right in combinations(points, 2)]
    return len(labels) == len(set(labels))


def q_fibre(
    differences: set[Point],
    popular: set[Point],
    centre: tuple[Point, Point],
    displacement: Point,
) -> set[Point]:
    c_value, ell_value = centre
    return {
        q_value
        for q_value in popular
        if add(q_value, displacement) in popular
        and subtract(c_value, q_value) in differences
        and add(
            ell_value,
            add(rotate(q_value), rotate(displacement)),
        )
        in differences
        and add(
            ell_value,
            add(rotate(q_value), linear(displacement)),
        )
        in differences
    }


def six_tracks(
    centre: tuple[Point, Point],
    a_value: Point,
    b_value: Point,
    e_value: Point,
    q_value: Point,
) -> tuple[Point, ...]:
    c_value, ell_value = centre
    second_q = subtract(q_value, e_value)
    return (
        subtract(c_value, q_value),
        add(ell_value, add(rotate(q_value), rotate(a_value))),
        add(ell_value, add(rotate(q_value), linear(a_value))),
        subtract(c_value, second_q),
        add(ell_value, add(rotate(second_q), rotate(b_value))),
        add(ell_value, add(rotate(second_q), linear(b_value))),
    )


def k24_key(tracks: tuple[Point, ...]) -> tuple[Point, ...]:
    return tuple(add(tracks[index], rotate(tracks[0])) for index in (1, 2, 4, 5))


def falling_three(value: int) -> int:
    return value * (value - 1) * (value - 2)


def check_owner_fibre_identity() -> None:
    # The identity is set-theoretic, so deliberately use asymmetric finite
    # D and P rather than geometry that might introduce accidental symmetry.
    differences = {
        (x, y) for x in range(-20, 21) for y in range(-20, 21)
    }
    popular = {
        (x, y)
        for x in range(-3, 4)
        for y in range(-3, 4)
        if (2 * x - y) % 3 != 1
    }
    centre = (2, -1), (-3, 2)
    a_value = (1, 2)
    b_value = (-2, 1)
    first = q_fibre(differences, popular, centre, a_value)
    second = q_fibre(differences, popular, centre, b_value)
    assert first and second

    loads = Counter(subtract(q_value, second_q) for q_value in first for second_q in second)
    direct_third = sum(falling_three(load) for load in loads.values())
    translated_third = 0
    for e_value, load in loads.items():
        selected = first & {add(e_value, value) for value in second}
        assert len(selected) == load
        keys = set()
        expected_z = add(centre[1], rotate(add(centre[0], a_value)))
        for q_value in selected:
            tracks = six_tracks(centre, a_value, b_value, e_value, q_value)
            assert all(value in differences for value in tracks)
            key = k24_key(tracks)
            keys.add(key)
            assert key[0] == expected_z
        assert len(keys) <= 1
        translated_third += falling_three(len(selected))
    assert direct_third == translated_third


def endpoint_vector(sign: int, endpoint: Point, other: Point) -> Point:
    return scale(sign, subtract(other, endpoint))


def owner_support_point(
    endpoint: Point,
    other_v: Point,
    other_w: Point,
    sign_v: int,
    sign_w: int,
    a_value: Point,
    b_value: Point,
) -> tuple[Point, Point]:
    v_value = endpoint_vector(sign_v, endpoint, other_v)
    w_value = endpoint_vector(sign_w, endpoint, other_w)
    c_value = subtract(v_value, a_value)
    ell_value = subtract(w_value, linear(b_value))
    z_value = add(ell_value, rotate(add(c_value, a_value)))
    assert z_value == subtract(add(w_value, rotate(v_value)), linear(b_value))
    return z_value, c_value


def check_endpoint_support_injectivity() -> None:
    points = [(0, 0), (1, 0), (0, 2), (3, 4), (8, 11)]
    assert distance_sidon(points)
    differences = difference_set(points)
    assert all(
        sum(norm_value == norm(value) for value in differences) <= 2
        for norm_value in {norm(value) for value in differences}
    )

    a_value = (2, -3)
    b_value = (-1, 4)
    for sign_v, sign_w in product((-1, 1), repeat=2):
        inverse: dict[tuple[Point, Point], tuple[Point, Point, Point]] = {}
        for endpoint in points:
            for other_v in points:
                for other_w in points:
                    if endpoint in (other_v, other_w):
                        continue
                    support = owner_support_point(
                        endpoint,
                        other_v,
                        other_w,
                        sign_v,
                        sign_w,
                        a_value,
                        b_value,
                    )
                    previous = inverse.setdefault(
                        support, (endpoint, other_v, other_w)
                    )
                    assert previous == (endpoint, other_v, other_w)

        # Retain the two cell-coordinate incidences V-a and W-Lb.  This is
        # the endpoint-weighted support in (3.5).
        selected_supports = {
            owner_support_point(
                endpoint,
                other_v,
                other_w,
                sign_v,
                sign_w,
                a_value,
                b_value,
            )
            for endpoint in points
            for other_v in points
            for other_w in points
            if endpoint not in (other_v, other_w)
            and subtract(
                endpoint_vector(sign_v, endpoint, other_v),
                a_value,
            )
            in differences
            and subtract(
                endpoint_vector(sign_w, endpoint, other_w),
                linear(b_value),
            )
            in differences
        }
        overlap_a = sum(add(start, a_value) in differences for start in differences)
        overlap_lb = sum(
            add(start, linear(b_value)) in differences for start in differences
        )
        assert len(selected_supports) <= (len(points) - 1) * min(
            overlap_a, overlap_lb
        )


def check_one_norm_inversion() -> None:
    points = [(0, 0), (1, 0), (0, 2), (3, 4), (8, 11)]
    assert distance_sidon(points)
    differences = difference_set(points)
    # For any fixed K2,4 key, reconstruction is injective in F0.  Radial
    # uniqueness therefore leaves at most f and -f after |F0|^2 is fixed.
    by_norm = Counter(norm(value) for value in differences)
    assert max(by_norm.values()) == 2

    z_values = ((5, -2), (1, 7), (-4, 3), (6, 6))
    reconstructed = {
        first: (
            first,
            subtract(z_values[0], rotate(first)),
            subtract(z_values[1], rotate(first)),
            add(first, (2, -1)),
            subtract(z_values[2], rotate(first)),
            subtract(z_values[3], rotate(first)),
        )
        for first in differences
    }
    assert len(reconstructed) == len(differences)
    for norm_value in by_norm:
        assert sum(norm(first) == norm_value for first in reconstructed) <= 2


def main() -> None:
    check_owner_fibre_identity()
    check_endpoint_support_injectivity()
    check_one_norm_inversion()
    print("K2,4 physical-owner support normal form: PASS")


if __name__ == "__main__":
    main()
