#!/usr/bin/env python3
"""Verify the support/collision fork for natural-level K2,4 footprints."""

from __future__ import annotations

from collections import Counter
from math import isqrt


Point = tuple[int, int]


def add(first: Point, second: Point) -> Point:
    return first[0] + second[0], first[1] + second[1]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def rotate(value: Point) -> Point:
    return -value[1], value[0]


def linear(value: Point) -> Point:
    return subtract(value, rotate(value))


def footprint(c_value: Point, z_value: Point, values: frozenset[Point]):
    offset = add(z_value, linear(c_value))
    return frozenset(
        add(offset, subtract(rotate(second), first))
        for first in values
        for second in values
    )


def representations(
    c_value: Point,
    z_value: Point,
    values: frozenset[Point],
) -> dict[Point, tuple[Point, Point]]:
    offset = add(z_value, linear(c_value))
    output: dict[Point, tuple[Point, Point]] = {}
    for first in sorted(values):
        for second in sorted(values):
            value = add(offset, subtract(rotate(second), first))
            output.setdefault(value, (first, second))
    return output


def third_mass(size: int) -> int:
    return size * (size - 1) * (size - 2) // 2


def verify_incidence_fork() -> None:
    families = (
        (
            frozenset((x, y) for x in range(3) for y in range(3)),
            frozenset((x + 1, y - 2) for x in range(3) for y in range(3)),
            frozenset((x, 2 * x) for x in range(9)),
        ),
        (
            frozenset((x, x * x) for x in range(7)),
            frozenset((x, -x * x) for x in range(7)),
        ),
    )
    for values_family in families:
        cells = []
        for index, values in enumerate(values_family):
            c_value = 3 * index, -5 * index
            z_value = 7 * index, 2 * index
            cells.append((c_value, z_value, values))

        depths: Counter[Point] = Counter()
        incidence = 0
        for c_value, z_value, values in cells:
            cell_footprint = footprint(c_value, z_value, values)
            incidence += len(cell_footprint)
            depths.update(cell_footprint)
        support = len(depths)
        collision = sum(value * (value - 1) // 2 for value in depths.values())
        square_depth = sum(value * value for value in depths.values())
        assert square_depth == incidence + 2 * collision
        assert incidence * incidence <= support * square_depth
        # Squaring avoids floating-point use in I <= X+sqrt(2XQ).
        assert incidence <= support or (
            (incidence - support) ** 2 <= 2 * support * collision
        )


def verify_collision_normal_form() -> None:
    first_values = frozenset((x, y) for x in range(4) for y in range(3))
    second_values = frozenset((x - 2, y + 1) for x in range(4) for y in range(3))
    c_value = (7, -4)
    z_value = (11, 6)
    other_c = (-5, 9)

    first = sorted(first_values)[2]
    second = sorted(first_values)[-3]
    other_first = sorted(second_values)[4]
    other_second = sorted(second_values)[-2]
    collision_value = add(
        add(z_value, linear(c_value)),
        subtract(rotate(second), first),
    )
    other_z = subtract(
        subtract(
            add(collision_value, other_first),
            linear(other_c),
        ),
        rotate(other_second),
    )
    assert collision_value in footprint(c_value, z_value, first_values)
    assert collision_value in footprint(other_c, other_z, second_values)

    delta_c = subtract(c_value, other_c)
    delta_z = subtract(z_value, other_z)
    first_delta = subtract(first, other_first)
    second_delta = subtract(second, other_second)
    assert add(delta_z, linear(delta_c)) == subtract(
        first_delta, rotate(second_delta)
    )

    first_f0 = subtract(c_value, first)
    first_f1 = subtract(z_value, rotate(first_f0))
    other_f0 = subtract(other_c, other_first)
    other_f1 = subtract(other_z, rotate(other_f0))
    second_f0 = subtract(c_value, second)
    second_f1 = subtract(z_value, rotate(second_f0))
    other_second_f0 = subtract(other_c, other_second)
    other_second_f1 = subtract(other_z, rotate(other_second_f0))
    assert subtract(first_f0, other_f0) == subtract(delta_c, first_delta)
    assert subtract(first_f1, other_f1) == add(
        subtract(delta_z, rotate(delta_c)), rotate(first_delta)
    )
    assert subtract(second_f0, other_second_f0) == subtract(
        delta_c, second_delta
    )
    assert subtract(second_f1, other_second_f1) == add(
        subtract(delta_z, rotate(delta_c)), rotate(second_delta)
    )
    u_value = subtract(delta_c, first_delta)
    h_value = subtract(first_delta, second_delta)
    assert subtract(first_f0, other_f0) == u_value
    assert subtract(second_f0, other_second_f0) == add(u_value, h_value)
    assert subtract(second_f1, other_second_f1) == (
        -u_value[0], -u_value[1]
    )
    assert subtract(first_f1, other_f1) == subtract(
        rotate(h_value), u_value
    )

    # Canonical representatives make every occupied cell/value incidence
    # and every unordered collision pair literal and multiplicity-free.
    first_representatives = representations(c_value, z_value, first_values)
    second_representatives = representations(other_c, other_z, second_values)
    common = set(first_representatives) & set(second_representatives)
    assert collision_value in common
    for value in common:
        assert first_representatives[value][0] in first_values
        assert first_representatives[value][1] in first_values
        assert second_representatives[value][0] in second_values
        assert second_representatives[value][1] in second_values


def verify_weighted_expansive_bound() -> None:
    cells = []
    lower = 9
    level = 1
    for index, side in enumerate((3, 3, 4, 4)):
        values = frozenset(
            (x + 2 * index, y - index)
            for x in range(side)
            for y in range(side)
        )
        assert lower <= len(values) < 2 * lower
        c_value = 5 * index, -3 * index
        z_value = -2 * index, 7 * index
        cell_footprint = footprint(c_value, z_value, values)
        assert 8 * level * len(cell_footprint) > len(values) ** 2
        cells.append((values, cell_footprint))

    depths: Counter[Point] = Counter()
    mass = 0
    incidence = 0
    for values, cell_footprint in cells:
        mass += third_mass(len(values))
        incidence += len(cell_footprint)
        depths.update(cell_footprint)
        assert third_mass(len(values)) < 8 * level * lower * len(
            cell_footprint
        )
    support = len(depths)
    collision = sum(value * (value - 1) // 2 for value in depths.values())
    assert mass < 8 * level * lower * incidence
    assert incidence * incidence <= support * (incidence + 2 * collision)

    # Integer check of the displayed radical upper envelope.
    radical_floor = isqrt(2 * support * collision)
    radical_ceiling = radical_floor + (radical_floor**2 < 2 * support * collision)
    assert incidence <= support + radical_ceiling


def main() -> None:
    verify_incidence_fork()
    verify_collision_normal_form()
    verify_weighted_expansive_bound()
    print("K2,4 natural footprint support/collision gate: PASS")


if __name__ == "__main__":
    main()
