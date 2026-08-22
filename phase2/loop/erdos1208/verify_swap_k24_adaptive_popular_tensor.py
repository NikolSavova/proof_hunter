#!/usr/bin/env python3
"""Exact checks for SWAP_K24_ADAPTIVE_POPULAR_THREE_FACTOR_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product


Point = tuple[int, int]
Colour = tuple[Point, Point, Point]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def negate(value: Point) -> Point:
    return -value[0], -value[1]


def rotate(value: Point) -> Point:
    return -value[1], value[0]


def falling_three(value: int) -> int:
    return value * (value - 1) * (value - 2)


def triple_differences(values: set[Point]) -> Counter[tuple[Point, Point]]:
    """Return T_X(h,g) on pairwise-distinct ordered triples."""

    return Counter(
        (subtract(second, first), subtract(third, first))
        for first, second, third in product(values, repeat=3)
        if len({first, second, third}) == 3
    )


def tensor_loads(
    first_tracks: set[Point],
    positive_starts: set[Point],
    popular_starts: set[Point],
) -> Counter[tuple[Point, Point]]:
    """Return r(z,c) from the three sets in (1.2)."""

    return Counter(
        (add(positive, rotate(first)), add(first, popular))
        for first in first_tracks
        for positive in positive_starts
        for popular in popular_starts
    )


def check_tensor_identity(
    first_tracks: set[Point],
    positive_starts: set[Point],
    popular_starts: set[Point],
) -> tuple[int, int]:
    loads = tensor_loads(first_tracks, positive_starts, popular_starts)
    direct = sum(falling_three(load) for load in loads.values())

    first_triples = triple_differences(first_tracks)
    positive_triples = triple_differences(positive_starts)
    popular_triples = triple_differences(popular_starts)
    correlation = 0
    for (first_shift, second_shift), first_count in first_triples.items():
        rotated_first = negate(rotate(first_shift))
        rotated_second = negate(rotate(second_shift))
        correlation += (
            first_count
            * positive_triples[rotated_first, rotated_second]
            * popular_triples[
                negate(first_shift), negate(second_shift)
            ]
        )

    assert direct == correlation
    return direct, max(loads.values(), default=0)


def generated_two_track_colours(
    values: set[Point],
) -> dict[Point, set[Point]]:
    output: dict[Point, set[Point]] = defaultdict(set)
    for first, second in product(values, repeat=2):
        output[subtract(second, first)].add(first)
    return output


def generated_four_track_colours(
    values: set[Point],
) -> dict[Colour, set[Point]]:
    output: dict[Colour, set[Point]] = defaultdict(set)
    for first, second, fourth, fifth in product(values, repeat=4):
        a_value = subtract(second, first)
        d_value = subtract(fourth, first)
        b_value = subtract(fifth, fourth)
        e_value = add(subtract(b_value, a_value), rotate(d_value))
        output[a_value, b_value, e_value].add(first)
    return output


def generated_popular_colours(
    values: set[Point],
) -> dict[Colour, set[Point]]:
    output: dict[Colour, set[Point]] = defaultdict(set)
    for first, second, third, fourth in product(values, repeat=4):
        a_value = subtract(second, first)
        e_value = subtract(first, third)
        b_value = subtract(fourth, third)
        output[a_value, b_value, e_value].add(first)
    return output


def check_colour_parametrizations() -> None:
    differences = {(0, 0), (2, 0), (0, 1), (3, 2)}
    popular = {(0, 0), (1, 0), (0, 2), (2, 1), (3, 0)}

    two_track = generated_two_track_colours(differences)
    four_track = generated_four_track_colours(differences)
    popular_four = generated_popular_colours(popular)
    assert sum(map(len, two_track.values())) == len(differences) ** 2
    assert sum(map(len, four_track.values())) == len(differences) ** 4
    assert sum(map(len, popular_four.values())) == len(popular) ** 4

    for e_value, starts in two_track.items():
        assert starts == {
            first
            for first in differences
            if add(first, e_value) in differences
        }
    for (a_value, b_value, e_value), starts in four_track.items():
        d_value = rotate(subtract(b_value, add(a_value, e_value)))
        assert starts == {
            first
            for first in differences
            if add(first, a_value) in differences
            and add(first, d_value) in differences
            and add(add(first, d_value), b_value) in differences
        }
    for (a_value, b_value, e_value), starts in popular_four.items():
        assert starts == {
            first
            for first in popular
            if add(first, a_value) in popular
            and subtract(first, e_value) in popular
            and add(subtract(first, e_value), b_value) in popular
        }


def check_selected_row_formula() -> None:
    first_tracks = {(0, 0), (1, 0), (0, 1), (1, 1), (2, 1)}
    positive_starts = {(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)}
    popular_starts = {(0, 0), (1, 0), (0, 1), (1, 1), (2, 1)}
    loads = tensor_loads(first_tracks, positive_starts, popular_starts)

    for (z_value, centre), load in loads.items():
        reconstructed = {
            first
            for first in first_tracks
            if subtract(z_value, rotate(first)) in positive_starts
            and subtract(centre, first) in popular_starts
        }
        assert len(reconstructed) == load

    direct, maximum = check_tensor_identity(
        first_tracks, positive_starts, popular_starts
    )
    assert direct > 0
    assert maximum >= 3

    # Seeded asymmetric stresses ensure that no symmetry of a square grid
    # is being used by the tensor identity.
    samples = (
        (
            {(0, 0), (2, 0), (1, 3), (4, 1)},
            {(1, 0), (0, 2), (3, 2), (4, -1), (2, 4)},
            {(0, 1), (2, 2), (-1, 3), (3, 0)},
        ),
        (
            {(0, 0), (1, 2), (3, 1), (4, 5), (-1, 4)},
            {(2, 0), (0, 1), (3, 3), (5, 2)},
            {(0, 0), (2, -1), (1, 3), (4, 2), (-2, 1)},
        ),
    )
    for sample in samples:
        check_tensor_identity(*sample)


def main() -> None:
    check_colour_parametrizations()
    check_selected_row_formula()
    print("K2,4 adaptive-popular three-factor tensor: PASS")


if __name__ == "__main__":
    main()
