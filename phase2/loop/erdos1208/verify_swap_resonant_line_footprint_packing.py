#!/usr/bin/env python3
"""Exact checks for the three resonant line-footprint bounds."""

from __future__ import annotations

from collections import Counter
from itertools import product
from math import gcd
import random

from analyze_affine_costas_energy import is_distance_sidon, welch
from analyze_swap_optimal_nested_cores import transformed_costas
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rotate,
    subtract,
)


Point = tuple[int, int]


def conjugate_linear(value: Point) -> Point:
    return value[0] + value[1], value[1] - value[0]


def assert_vector_sidon(values: set[Point]) -> None:
    representations: dict[Point, tuple[Point, Point]] = {}
    for first, second in product(values, repeat=2):
        if first == second:
            continue
        difference = subtract(first, second)
        assert difference not in representations
        representations[difference] = first, second


def energy(first: set[Point], second: set[Point]) -> int:
    loads = Counter(add(left, right) for left, right in product(first, second))
    return sum(load * load for load in loads.values())


def verify_three_footprint_energies() -> None:
    points = [(3 * x + y, x + 4 * y) for x, y in welch(17)]
    rng = random.Random(1208)
    for size in range(1, 10):
        for _ in range(100):
            values = set(rng.sample(points, size))
            assert_vector_sidon(values)
            rotated = {rotate(value) for value in values}
            linear_values = {linear(value) for value in values}
            negative = {(-value[0], -value[1]) for value in values}
            conjugate = {conjugate_linear(value) for value in values}
            rows = (
                (rotated, linear_values),
                (values, values),
                (conjugate, negative),
            )
            for first, second in rows:
                actual = energy(first, second)
                assert actual <= 2 * size * size - size
                support = {
                    add(left, right) for left, right in product(first, second)
                }
                assert 2 * len(support) >= size * size


def verify_line_aggregation() -> None:
    rng = random.Random(1618033)
    for distinct_values in range(1, 30):
        for _ in range(200):
            multiplicities = [rng.randrange(1, 20) for _ in range(distinct_values)]
            total = sum(multiplicities)
            square_mass = sum(value * value for value in multiplicities)
            all_pairs = total * (total - 1) // 2
            assert 2 * all_pairs <= distinct_values * square_mass


def primitive(value: Point) -> Point:
    content = gcd(abs(value[0]), abs(value[1]))
    assert content
    return value[0] // content, value[1] // content


def verify_line_capacity() -> None:
    rng = random.Random(57721)
    for _ in range(20000):
        bound = rng.randrange(1, 50)
        direction = rng.randrange(-20, 21), rng.randrange(-20, 21)
        if direction == (0, 0):
            continue
        step = primitive(direction)
        capacity = 1 + 4 * bound // max(abs(step[0]), abs(step[1]))
        start = (
            rng.randrange(-2 * bound, 2 * bound + 1),
            rng.randrange(-2 * bound, 2 * bound + 1),
        )
        points = []
        for coefficient in range(-4 * bound - 5, 4 * bound + 6):
            point = (
                start[0] + coefficient * step[0],
                start[1] + coefficient * step[1],
            )
            if max(abs(point[0]), abs(point[1])) <= 2 * bound:
                points.append(point)
        assert len(set(points)) <= capacity


def verify_genuine_constant_z_repair() -> None:
    points, differences = transformed_costas(23)
    assert is_distance_sidon(points)
    rows = (
        ((-9, -11), (-69, 23), (27, -13), (-42, 10)),
        ((37, -57), (-23, 23), (-19, -13), (-42, 10)),
    )
    assert all(row[0] in differences and row[2] in differences for row in rows)
    assert len({row[3] for row in rows}) == 1
    failed = {
        add(first[2], second[3]) for first, second in product(rows, repeat=2)
    }
    corrected = {
        add(first[0], second[2]) for first, second in product(rows, repeat=2)
    }
    assert len(failed) == 2
    assert len(corrected) == 4

    t_values = {row[1] for row in rows}
    assert_vector_sidon(t_values)
    conjugate = {conjugate_linear(value) for value in t_values}
    negative = {(-value[0], -value[1]) for value in t_values}
    support = {add(left, right) for left, right in product(conjugate, negative)}
    assert len(support) == 4


def main() -> None:
    verify_three_footprint_energies()
    verify_line_aggregation()
    verify_line_capacity()
    verify_genuine_constant_z_repair()
    print("SWAP RESONANT LINE-FOOTPRINT PACKING GATE: PASS")


if __name__ == "__main__":
    main()
