#!/usr/bin/env python3
"""Exact checks for the decorated-key metric transversal gate."""

from __future__ import annotations

from itertools import product
import random

from analyze_affine_costas_energy import is_distance_sidon
from analyze_swap_optimal_nested_cores import transformed_costas
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rotate,
    subtract,
)


Point = tuple[int, int]


def dot(first: Point, second: Point) -> int:
    return first[0] * second[0] + first[1] * second[1]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def norm(value: Point) -> int:
    return dot(value, value)


def negate(value: Point) -> Point:
    return -value[0], -value[1]


def scale(factor: int, value: Point) -> Point:
    return factor * value[0], factor * value[1]


def metric_cell(
    centre: Point,
    ell: Point,
    first_t: Point,
    second_t: Point,
    first_q: Point,
    second_q: Point,
) -> tuple[tuple[Point, Point, Point, Point, Point, Point], tuple[int, int, int]]:
    difference = subtract(first_t, second_t)
    key_shift = subtract(first_q, second_q)
    first_a = subtract(centre, first_q)
    first_b = add(ell, rotate(add(first_q, first_t)))
    first_c = add(ell, add(rotate(first_q), linear(first_t)))
    second_a = subtract(centre, second_q)
    second_b = add(ell, rotate(add(second_q, second_t)))
    second_c = add(ell, add(rotate(second_q), linear(second_t)))

    assert second_a == add(first_a, key_shift)
    assert second_b == subtract(
        first_b, rotate(add(key_shift, difference))
    )
    assert second_c == subtract(
        first_c, add(rotate(key_shift), linear(difference))
    )

    gaps = (
        norm(second_a) - norm(first_a),
        norm(second_b) - norm(first_b),
        norm(second_c) - norm(first_c),
    )
    return (
        first_a,
        second_a,
        first_b,
        second_b,
        first_c,
        second_c,
    ), gaps


def gap_directions(key_shift: Point, difference: Point) -> tuple[Point, Point, Point]:
    return (
        key_shift,
        add(key_shift, difference),
        subtract(add(key_shift, difference), rotate(difference)),
    )


def canonical_pair(key_shift: Point, difference: Point) -> tuple[int, int]:
    directions = gap_directions(key_shift, difference)
    return max(
        ((first, second) for first in range(3) for second in range(first + 1, 3)),
        key=lambda pair: (
            abs(determinant(directions[pair[0]], directions[pair[1]])),
            -pair[0],
            -pair[1],
        ),
    )


def verify_symbolic_normal_form() -> None:
    values = range(-3, 4)
    for entries in product(values, repeat=4):
        key_shift = entries[0], entries[1]
        difference = entries[2], entries[3]
        if difference == (0, 0):
            continue
        directions = gap_directions(key_shift, difference)
        pair_determinants = [
            determinant(directions[first], directions[second])
            for first in range(3)
            for second in range(first + 1, 3)
        ]
        a_value = determinant(key_shift, difference)
        b_value = dot(key_shift, difference)
        square = norm(difference)
        assert pair_determinants == [
            a_value,
            a_value - b_value,
            -(b_value + square),
        ]
        assert 3 * max(abs(value) for value in pair_determinants) >= square

    sharp_d = (3, 0)
    sharp_s = (-2, 1)
    sharp_determinants = [
        abs(determinant(first, second))
        for first, second in (
            (gap_directions(sharp_s, sharp_d)[0], gap_directions(sharp_s, sharp_d)[1]),
            (gap_directions(sharp_s, sharp_d)[0], gap_directions(sharp_s, sharp_d)[2]),
            (gap_directions(sharp_s, sharp_d)[1], gap_directions(sharp_s, sharp_d)[2]),
        )
    ]
    assert sharp_determinants == [3, 3, 3]
    assert 3 * sharp_determinants[0] == norm(sharp_d)


def verify_gap_linearization_and_injectivity() -> None:
    rng = random.Random(1208)
    for _ in range(5000):
        centre = rng.randrange(-20, 21), rng.randrange(-20, 21)
        ell = rng.randrange(-20, 21), rng.randrange(-20, 21)
        first_t = rng.randrange(-9, 10), rng.randrange(-9, 10)
        second_t = rng.randrange(-9, 10), rng.randrange(-9, 10)
        if first_t == second_t:
            continue
        first_q = rng.randrange(-20, 21), rng.randrange(-20, 21)
        key_shift = rng.randrange(-8, 9), rng.randrange(-8, 9)
        second_q = subtract(first_q, key_shift)

        _, gaps = metric_cell(
            centre, ell, first_t, second_t, first_q, second_q
        )
        difference = subtract(first_t, second_t)
        directions = gap_directions(key_shift, difference)
        first_a = subtract(centre, first_q)

        # Changing A by a vector changes each metric gap by exactly
        # twice its dot product with the corresponding direction.
        motion = rng.randrange(-5, 6), rng.randrange(-5, 6)
        moved_q = subtract(first_q, motion)
        moved_second_q = subtract(moved_q, key_shift)
        _, moved_gaps = metric_cell(
            centre, ell, first_t, second_t, moved_q, moved_second_q
        )
        moved_a = subtract(centre, moved_q)
        assert subtract(moved_a, first_a) == motion
        assert tuple(
            moved_gaps[index] - gaps[index] for index in range(3)
        ) == tuple(2 * dot(motion, direction) for direction in directions)

        first_index, second_index = canonical_pair(key_shift, difference)
        jacobian = 4 * abs(
            determinant(directions[first_index], directions[second_index])
        )
        assert 3 * jacobian >= 4 * norm(difference)

        # Exhaust a small box: the selected metric pair is injective in A.
        seen: dict[tuple[int, int], Point] = {}
        for candidate_a in product(range(-3, 4), repeat=2):
            candidate_q = subtract(centre, candidate_a)
            candidate_second_q = subtract(candidate_q, key_shift)
            _, candidate_gaps = metric_cell(
                centre,
                ell,
                first_t,
                second_t,
                candidate_q,
                candidate_second_q,
            )
            metric_key = (
                candidate_gaps[first_index], candidate_gaps[second_index]
            )
            assert metric_key not in seen
            seen[metric_key] = candidate_a


def verify_recursive_motion_signature() -> None:
    rng = random.Random(1729)
    for _ in range(10000):
        centre = rng.randrange(-20, 21), rng.randrange(-20, 21)
        ell = rng.randrange(-20, 21), rng.randrange(-20, 21)
        neighbour = rng.randrange(-12, 13), rng.randrange(-12, 13)
        shift = rng.randrange(-10, 11), rng.randrange(-10, 11)
        if shift == (0, 0):
            continue
        q_value = rng.randrange(-20, 21), rng.randrange(-20, 21)
        h_value = add(ell, rotate(centre))
        first_a = subtract(centre, q_value)
        first_b = add(h_value, subtract(rotate(neighbour), rotate(first_a)))
        first_c = add(first_b, neighbour)
        second_a = add(first_a, shift)
        second_b = subtract(first_b, rotate(shift))
        second_c = subtract(first_c, rotate(shift))
        gaps = (
            norm(second_a) - norm(first_a),
            norm(second_b) - norm(first_b),
            norm(second_c) - norm(first_c),
        )
        assert gaps[0] - gaps[1] == (
            2 * dot(h_value, rotate(shift))
            + 2 * dot(neighbour, shift)
        )
        assert gaps[1] - gaps[2] == 2 * dot(
            neighbour, rotate(shift)
        )

        recovered_dot = (
            gaps[0] - gaps[1] - 2 * dot(h_value, rotate(shift))
        ) // 2
        recovered_rotated_dot = (gaps[1] - gaps[2]) // 2
        square = norm(shift)
        recovered_numerator = add(
            scale(recovered_dot, shift),
            scale(recovered_rotated_dot, rotate(shift)),
        )
        assert recovered_numerator == scale(square, neighbour)
        assert 4 * abs(determinant(shift, rotate(shift))) == 4 * square


def combined_metric_key(
    centre: Point,
    ell: Point,
    key_shift: Point,
    difference: Point,
    recursive_shift: Point,
    first_a: Point,
    first_t: Point,
) -> tuple[int, int, int, int]:
    first_q = subtract(centre, first_a)
    second_q = subtract(first_q, key_shift)
    second_t = subtract(first_t, difference)
    _, original_gaps = metric_cell(
        centre, ell, first_t, second_t, first_q, second_q
    )
    pair = canonical_pair(key_shift, difference)

    h_value = add(ell, rotate(centre))
    first_b = add(h_value, subtract(rotate(first_t), rotate(first_a)))
    first_c = add(first_b, first_t)
    recursive_gaps = (
        norm(add(first_a, recursive_shift)) - norm(first_a),
        norm(subtract(first_b, rotate(recursive_shift))) - norm(first_b),
        norm(subtract(first_c, rotate(recursive_shift))) - norm(first_c),
    )
    return (
        original_gaps[pair[0]],
        original_gaps[pair[1]],
        recursive_gaps[0] - recursive_gaps[1],
        recursive_gaps[1] - recursive_gaps[2],
    )


def verify_product_transversality() -> None:
    rng = random.Random(271828)
    for _ in range(80):
        centre = rng.randrange(-12, 13), rng.randrange(-12, 13)
        ell = rng.randrange(-12, 13), rng.randrange(-12, 13)
        key_shift = rng.randrange(-5, 6), rng.randrange(-5, 6)
        difference = rng.randrange(-5, 6), rng.randrange(-5, 6)
        recursive_shift = rng.randrange(-5, 6), rng.randrange(-5, 6)
        if difference == (0, 0) or recursive_shift == (0, 0):
            continue
        directions = gap_directions(key_shift, difference)
        pair = canonical_pair(key_shift, difference)
        first_determinant = 4 * abs(
            determinant(directions[pair[0]], directions[pair[1]])
        )
        second_determinant = 4 * norm(recursive_shift)
        assert 3 * first_determinant >= 4 * norm(difference)
        assert (
            3 * first_determinant * second_determinant
            >= 16 * norm(difference) * norm(recursive_shift)
        )

        seen: dict[tuple[int, int, int, int], tuple[Point, Point]] = {}
        for first_a in product(range(-2, 3), repeat=2):
            for first_t in product(range(-2, 3), repeat=2):
                key = combined_metric_key(
                    centre,
                    ell,
                    key_shift,
                    difference,
                    recursive_shift,
                    first_a,
                    first_t,
                )
                assert key not in seen
                seen[key] = first_a, first_t


def verify_genuine_costas_collision() -> None:
    points, differences = transformed_costas(23)
    assert is_distance_sidon(points)
    centre = (14, -11)
    ell = (50, 33)
    switch = (0, 23)
    first_t = (-69, 23)
    second_t = (-23, 23)
    first_q = subtract(centre, (-9, -11))
    second_q = subtract(centre, (37, -57))
    key_shift = subtract(first_q, second_q)
    difference = subtract(first_t, second_t)
    assert key_shift == (46, -46)
    assert difference == (-46, 0)

    occurrences = []
    for motion in ((0, 0), negate(switch)):
        moved_first_q = add(first_q, motion)
        moved_second_q = add(second_q, motion)
        vectors, gaps = metric_cell(
            centre,
            ell,
            first_t,
            second_t,
            moved_first_q,
            moved_second_q,
        )
        assert set(vectors) <= differences
        occurrences.append((subtract(centre, moved_first_q), gaps))

    pair = canonical_pair(key_shift, difference)
    metric_keys = {
        (gaps[pair[0]], gaps[pair[1]]) for _, gaps in occurrences
    }
    assert len(metric_keys) == 2
    directions = gap_directions(key_shift, difference)
    assert 3 * 4 * abs(determinant(directions[pair[0]], directions[pair[1]])) >= (
        4 * norm(difference)
    )


def main() -> None:
    verify_symbolic_normal_form()
    verify_gap_linearization_and_injectivity()
    verify_recursive_motion_signature()
    verify_product_transversality()
    verify_genuine_costas_collision()
    print("SWAP DECORATED-KEY METRIC TRANSVERSAL GATE: PASS")


if __name__ == "__main__":
    main()
