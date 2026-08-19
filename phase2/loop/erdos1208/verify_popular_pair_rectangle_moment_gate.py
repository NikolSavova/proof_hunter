#!/usr/bin/env python3
"""Exact checks for POPULAR_PAIR_RECTANGLE_MOMENT_GATE.md."""

from __future__ import annotations

from collections import Counter

from analyze_affine_costas_energy import welch
from verify_determinant_prime_costas_resonance import ROWS, apply
from verify_orthogonal_two_support_gate import difference_set
from verify_radial_orthogonal_product_barrier import radial_set
from verify_seven_incidence_opposite_endpoint_charge import (
    POINTS,
    add,
    linear,
    overlap_table,
    rich_fibres,
    rotate,
    scale,
    subtract,
)


Point = tuple[int, int]
ShiftPair = tuple[Point, Point]


def rectangle_data(
    differences: set[Point],
) -> tuple[
    int,
    int,
    set[Point],
    dict[ShiftPair, tuple[set[Point], set[Point], set[Point], set[Point]]],
]:
    overlaps = {shift: set(starts) for shift, starts in overlap_table(differences).items()}
    number = len(differences)
    support = len(overlaps)
    empty: set[Point] = set()
    popular = {
        shift
        for shift, starts in overlaps.items()
        if shift != (0, 0)
        and len(starts) * number > support
        and len(overlaps.get(rotate(shift), empty)) * number > support
    }

    rectangles = {}
    for shift in popular:
        negative_rotated = scale(-1, rotate(shift))
        for other in popular:
            if shift == other:
                continue
            first = overlaps[shift] & overlaps[other]
            if not first:
                continue
            gap = subtract(shift, other)
            last_gap = subtract(gap, rotate(other))
            opposite = (
                overlaps.get(gap, empty)
                & overlaps.get(last_gap, empty)
                & overlaps.get(negative_rotated, empty)
            )
            if not opposite:
                continue
            first_image = {add(scale(2, value), other) for value in first}
            opposite_image = {
                subtract(value, rotate(shift)) for value in opposite
            }
            assert len(first_image) == len(first)
            assert len(opposite_image) == len(opposite)
            rectangles[shift, other] = (
                first,
                opposite,
                first_image,
                opposite_image,
            )
    return number, support, popular, rectangles


def direct_loads(
    rectangles: dict[
        ShiftPair, tuple[set[Point], set[Point], set[Point], set[Point]]
    ]
) -> Counter[tuple[Point, Point]]:
    loads: Counter[tuple[Point, Point]] = Counter()
    for first, opposite, first_image, opposite_image in rectangles.values():
        assert len(first) == len(first_image)
        assert len(opposite) == len(opposite_image)
        for value in opposite_image:
            for total in first_image:
                loads[value, total] += 1
    return loads


def verify_nested_pair_mapping(
    differences: set[Point],
    popular: set[Point],
    rectangles: dict[
        ShiftPair, tuple[set[Point], set[Point], set[Point], set[Point]]
    ],
) -> tuple[int, int]:
    alpha_pairs = 0
    beta_pairs = 0
    for (shift, other), (first, opposite, _, _) in rectangles.items():
        assert shift in popular and other in popular and shift != other
        for base in first:
            for second_base in first:
                displacement = subtract(second_base, base)
                assert add(base, displacement) in differences
                assert add(add(base, shift), displacement) in differences
                assert add(add(base, other), displacement) in differences
                alpha_pairs += 1

        gap = subtract(shift, other)
        for x0 in opposite:
            for second_x0 in opposite:
                displacement = subtract(second_x0, x0)
                x1 = add(x0, gap)
                x3 = subtract(x0, rotate(shift))
                x2 = add(x3, linear(gap))
                assert add(x0, displacement) in differences
                assert add(x1, displacement) in differences
                assert add(x2, displacement) in differences
                assert add(x3, displacement) in differences
                assert rotate(subtract(x3, x0)) == shift
                assert subtract(shift, subtract(x1, x0)) == other
                beta_pairs += 1

    return alpha_pairs, beta_pairs


def profile(
    points: list[Point] | set[Point], verify_nested: bool = False
) -> tuple[int, int, int, int, int, int, int]:
    differences = difference_set(points) if not isinstance(points, set) else points
    number, support, popular, rectangles = rectangle_data(differences)
    loads = direct_loads(rectangles)
    off_diagonal = sum(
        len(first) * len(opposite)
        for first, opposite, _, _ in rectangles.values()
    )
    assert off_diagonal == sum(loads.values())
    load_moment = sum(value * value for value in loads.values())

    alpha_square = sum(
        len(first) ** 2 for first, _, _, _ in rectangles.values()
    )
    beta_square = sum(
        len(opposite) ** 2 for _, opposite, _, _ in rectangles.values()
    )
    assert off_diagonal * off_diagonal <= alpha_square * beta_square

    # Check the exact four-point reconstruction (3.4)--(3.5).
    for (shift, other), (_, opposite, _, _) in rectangles.items():
        gap = subtract(shift, other)
        for x0 in opposite:
            x1 = add(x0, gap)
            x3 = subtract(x0, rotate(shift))
            x2 = add(x3, linear(subtract(x1, x0)))
            assert x2 == subtract(x1, rotate(other))
            assert rotate(subtract(x3, x0)) == shift
            assert subtract(shift, subtract(x1, x0)) == other
            assert x0 in differences
            assert x1 in differences
            assert x2 in differences
            assert x3 in differences

    if verify_nested:
        assert verify_nested_pair_mapping(differences, popular, rectangles) == (
            alpha_square,
            beta_square,
        )

    return (
        number,
        support,
        len(rectangles),
        off_diagonal,
        load_moment,
        alpha_square,
        beta_square,
    )


def main() -> None:
    closure = profile(POINTS[:40], verify_nested=True)
    assert closure == (
        1_561,
        156_057,
        7_110,
        370_516,
        475_112,
        2_744_348,
        104_948,
    )
    print("closure-40", closure)

    costas_rows = {}
    for prime, (matrix, _) in ROWS.items():
        points = [apply(matrix, point) for point in welch(prime)]
        current = profile(points, verify_nested=(prime == 23))
        costas_rows[prime] = current
        print("Costas", prime, current)

    assert costas_rows[23] == (
        463,
        4_513,
        1_878,
        498_674,
        1_258_518,
        2_294_322,
        250_722,
    )

    radial = profile(radial_set(12))
    number, support, _, _, _, alpha_square, beta_square = radial
    assert alpha_square > 25 * support * support
    assert beta_square > 192 * number * number
    print("radial-12 negative control", radial)
    print("POPULAR-PAIR RECTANGLE MOMENT GATE: PASS")


if __name__ == "__main__":
    main()
