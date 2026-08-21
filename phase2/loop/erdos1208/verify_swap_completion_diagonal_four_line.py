#!/usr/bin/env python3
"""Verify the diagonal completion-line normalization."""

from __future__ import annotations

from collections import Counter
from random import Random

Point = tuple[int, int]


def add(first: Point, second: Point) -> Point:
    return first[0] + second[0], first[1] + second[1]


def sub(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def rotate(value: Point) -> Point:
    return -value[1], value[0]


def linear(value: Point) -> Point:
    return add(value, rotate(value))


def translate(values: set[Point], shift: Point) -> set[Point]:
    return {add(value, shift) for value in values}


def line(
    differences: set[Point], popular: set[Point], terminal: Point, start: Point
) -> set[Point]:
    assert terminal in differences and start in differences
    return {
        shift
        for shift in popular
        if sub(terminal, shift) in differences
        and add(start, rotate(shift)) in differences
    }


def parallel_fibre_direct(
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
        and sub(c_value, q_value) in differences
        and add(add(ell_value, rotate(q_value)), rotate(displacement))
        in differences
        and add(add(ell_value, rotate(q_value)), linear(displacement))
        in differences
    }


def audit(differences: set[Point], popular: set[Point]) -> None:
    lines = {
        (terminal, start): line(differences, popular, terminal, start)
        for terminal in differences
        for start in differences
    }

    completion_mass = sum(
        sum(
            1
            for first_start in differences
            for second_start in differences
            if add(first_start, shift) in differences
            and add(second_start, rotate(shift)) in differences
        )
        for shift in popular
    )
    assert sum(map(len, lines.values())) == completion_mass

    for shift in popular:
        line_degree = sum(shift in values for values in lines.values())
        parallel_load = sum(
            add(start, shift) in differences for start in differences
        )
        perpendicular_load = sum(
            add(start, rotate(shift)) in differences for start in differences
        )
        assert line_degree == parallel_load * perpendicular_load

    for first_shift in popular:
        for second_shift in popular:
            codegree = sum(
                first_shift in values and second_shift in values
                for values in lines.values()
            )
            first_factor = sum(
                sub(terminal, first_shift) in differences
                and sub(terminal, second_shift) in differences
                for terminal in differences
            )
            second_factor = sum(
                add(start, rotate(first_shift)) in differences
                and add(start, rotate(second_shift)) in differences
                for start in differences
            )
            assert codegree == first_factor * second_factor

    active: list[tuple[tuple[Point, Point], Point, set[Point]]] = []
    for c_value in differences:
        for ell_value in differences:
            centre = c_value, ell_value
            for displacement in differences:
                terminal = add(c_value, displacement)
                second_terminal = add(ell_value, linear(displacement))
                if terminal not in differences or second_terminal not in differences:
                    continue
                direct = parallel_fibre_direct(
                    differences, popular, centre, displacement
                )
                factored = lines[c_value, second_terminal] & translate(
                    lines[terminal, ell_value],
                    (-displacement[0], -displacement[1]),
                )
                assert direct == factored
                active.append((centre, displacement, direct))

    for centre, first_displacement, first_fibre in active:
        compatible = [row for row in active if row[0] == centre]
        c_value, ell_value = centre
        first_terminal = add(c_value, first_displacement)
        first_second = add(ell_value, linear(first_displacement))
        for _, second_displacement, second_fibre in compatible:
            second_terminal = add(c_value, second_displacement)
            second_second = add(ell_value, linear(second_displacement))
            shifts = {
                sub(first, second)
                for first in first_fibre
                for second in second_fibre
            }
            for shift in shifts:
                direct = {
                    value
                    for value in first_fibre
                    if sub(value, shift) in second_fibre
                }
                four_line = (
                    lines[c_value, first_second]
                    & translate(
                        lines[first_terminal, ell_value],
                        (-first_displacement[0], -first_displacement[1]),
                    )
                    & translate(lines[c_value, second_second], shift)
                    & translate(
                        lines[second_terminal, ell_value],
                        sub(shift, second_displacement),
                    )
                )
                assert direct == four_line


def random_audits() -> None:
    rng = Random(1208)
    box = [(x, y) for x in range(-2, 3) for y in range(-2, 3)]
    for _ in range(80):
        differences = {
            value for value in box if rng.randrange(3) == 0
        } | {(0, 0)}
        differences |= {(-value[0], -value[1]) for value in differences}
        popular = {
            value for value in box if value != (0, 0) and rng.randrange(3) == 0
        }
        audit(differences, popular)


def main() -> None:
    random_audits()
    print("SWAP COMPLETION DIAGONAL FOUR-LINE GATE: PASS")


if __name__ == "__main__":
    main()
