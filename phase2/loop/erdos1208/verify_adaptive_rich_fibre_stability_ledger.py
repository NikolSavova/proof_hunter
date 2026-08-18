#!/usr/bin/env python3
"""Exact checks for ADAPTIVE_RICH_FIBRE_STABILITY_LEDGER.md."""

from __future__ import annotations

from collections import Counter, defaultdict

from verify_orthogonal_two_support_gate import difference_set
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Label = tuple[Point, Point]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def linear(point: Point) -> Point:
    return point[0] - point[1], point[0] + point[1]


def verify_collinear_injection() -> None:
    for size in (2, 5, 11, 23):
        origin = (7, -11)
        direction = (3, 8)
        parameters = [index * index + 2 * index for index in range(size)]
        fibre = {
            add(origin, (parameter * direction[0], parameter * direction[1]))
            for parameter in parameters
        }
        first_translation = (13, 17)
        second_translation = (-19, 23)
        first_copy = {add(first_translation, value) for value in fibre}
        second_copy = {
            subtract(second_translation, linear(value)) for value in fibre
        }
        sums = {add(left, right) for left in first_copy for right in second_copy}
        assert len(fibre) == size
        assert len(sums) == size * size
        determinant = (
            direction[0] * linear(direction)[1]
            - direction[1] * linear(direction)[0]
        )
        assert determinant == direction[0] ** 2 + direction[1] ** 2
    print("collinear Cartesian support: PASS")


def closure_rich_fibres() -> tuple[
    set[Point], set[Point], dict[Label, set[Point]], Counter[Point]
]:
    differences = difference_set(POINTS[:30])
    number = len(differences)
    overlaps: dict[Point, list[Point]] = defaultdict(list)
    for endpoint in differences:
        for start in differences:
            overlaps[subtract(endpoint, start)].append(start)
    support = len(overlaps)
    rich = {
        shift
        for shift, starts in overlaps.items()
        if shift != (0, 0)
        and len(starts) * number > support
        and len(overlaps.get(rotate(shift), ())) * number > support
    }

    fibres: dict[Label, set[Point]] = defaultdict(set)
    for shift in rich:
        rotated = rotate(shift)
        for first_start in overlaps[shift]:
            first_endpoint = add(first_start, shift)
            for second_start in overlaps[rotated]:
                second_endpoint = add(second_start, rotated)
                ordinary_sum = add(first_endpoint, second_endpoint)
                fibres[first_start, ordinary_sum].add(shift)

    representation_counts = Counter(
        subtract(endpoint, start)
        for endpoint in differences
        for start in differences
    )
    return differences, rich, fibres, representation_counts


def verify_seven_incidence_identity() -> None:
    differences, rich, fibres, representations = closure_rich_fibres()
    mass = sum(len(fibre) for fibre in fibres.values())
    moment = sum(len(fibre) ** 2 for fibre in fibres.values())
    assert (mass, len(fibres), max(map(len, fibres.values())), moment) == (
        58_800,
        58_100,
        3,
        60_220,
    )

    by_difference: Counter[Point] = Counter()
    for (start, ordinary_sum), fibre in fibres.items():
        for shift in fibre:
            for other_shift in fibre:
                delta = subtract(other_shift, shift)
                first_endpoint = add(start, shift)
                second_endpoint = subtract(ordinary_sum, first_endpoint)
                second_start = subtract(second_endpoint, rotate(shift))

                assert add(first_endpoint, delta) in differences
                assert subtract(second_endpoint, delta) in differences
                assert subtract(second_start, linear(delta)) in differences
                recovered_start = add(
                    first_endpoint,
                    rotate(subtract(second_endpoint, second_start)),
                )
                assert recovered_start == start
                recovered_shift = tuple(
                    -value
                    for value in rotate(subtract(second_endpoint, second_start))
                )
                assert recovered_shift == shift
                assert shift in rich and other_shift in rich
                by_difference[delta] += 1

    assert sum(by_difference.values()) == moment
    assert by_difference[(0, 0)] == mass
    for delta, count in by_difference.items():
        raw_majorant = (
            representations[delta] ** 2
            * representations[linear(delta)]
        )
        assert count <= raw_majorant

    print(
        "seven-incidence closure-30",
        "mass", mass,
        "moment", moment,
        "off_diagonal", moment - mass,
        "active_differences", len(by_difference),
        "max_off_diagonal", max(
            count for delta, count in by_difference.items() if delta != (0, 0)
        ),
    )


def main() -> None:
    verify_collinear_injection()
    verify_seven_incidence_identity()
    print("adaptive rich-fibre stability ledger: PASS")


if __name__ == "__main__":
    main()
