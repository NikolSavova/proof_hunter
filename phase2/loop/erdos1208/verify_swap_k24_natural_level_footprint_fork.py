#!/usr/bin/env python3
"""Verify the natural-core / perpendicular-footprint density fork."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations

from verify_swap_k24_ambient_owner_core_saturation import optimal_loads


Point = tuple[int, int]


def add(first: Point, second: Point) -> Point:
    return first[0] + second[0], first[1] + second[1]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def rotate(value: Point) -> Point:
    return -value[1], value[0]


def difference_counts(values: frozenset[Point]) -> Counter[Point]:
    return Counter(subtract(first, second) for first in values for second in values)


def footprint_counts(values: frozenset[Point]) -> Counter[Point]:
    return Counter(
        subtract(rotate(second), first)
        for first in values
        for second in values
    )


def perpendicular_energy(values: frozenset[Point]) -> int:
    differences = difference_counts(values)
    return sum(
        multiplicity * differences[rotate(direction)]
        for direction, multiplicity in differences.items()
    )


def popular_perpendicular_directions(
    values: frozenset[Point], threshold: int
) -> frozenset[Point]:
    differences = difference_counts(values)
    return frozenset(
        direction
        for direction, multiplicity in differences.items()
        if direction != (0, 0)
        and multiplicity >= threshold
        and differences[rotate(direction)] >= threshold
    )


def third_mass(size: int) -> int:
    return size * (size - 1) * (size - 2) // 2


def verify_energy_identity() -> None:
    ground = tuple((x, y) for x in range(3) for y in range(3))
    for size in range(1, 7):
        for chosen in combinations(ground, size):
            values = frozenset(chosen)
            representations = footprint_counts(values)
            assert sum(representations.values()) == size * size
            assert sum(value * value for value in representations.values()) == (
                perpendicular_energy(values)
            )
            assert len(representations) * perpendicular_energy(values) >= size**4
            # The torsion-free sumset lower bound in this concrete model.
            assert len(representations) >= 2 * size - 1


def verify_compressed_fork() -> None:
    # Dense boxes genuinely enter the compressed branch, so the quantified
    # conclusion is tested nonvacuously rather than only symbolically.
    for side in range(5, 10):
        values = frozenset(
            (x, y) for x in range(side) for y in range(side)
        )
        size = len(values)
        energy = perpendicular_energy(values)
        footprint_size = len(footprint_counts(values))
        for level in range(1, max(2, size // 20)):
            if 8 * level * footprint_size > size * size:
                continue
            popular = popular_perpendicular_directions(values, level)
            popular_mass = sum(
                difference_counts(values)[direction]
                * difference_counts(values)[rotate(direction)]
                for direction in popular
            )
            assert energy >= 8 * level * size * size
            assert popular_mass >= 5 * level * size * size
            assert len(popular) >= 5 * level

            # Translated copies of -S and JS inside a literal reservoir D
            # make every direction in H_L popular in both perpendicular
            # difference channels.
            first_shift = (10_000, -20_000)
            second_shift = (-30_000, 40_000)
            first_track = {
                subtract(first_shift, value) for value in values
            }
            second_track = {
                add(second_shift, rotate(value)) for value in values
            }
            reservoir = frozenset(first_track | second_track)
            reservoir_differences = difference_counts(reservoir)
            source_differences = difference_counts(values)
            for direction in popular:
                assert reservoir_differences[direction] >= source_differences[direction]
                assert reservoir_differences[rotate(direction)] >= (
                    source_differences[rotate(direction)]
                )


def verify_dyadic_family_bound() -> None:
    cells = []
    for side, translate in ((3, (0, 0)), (4, (20, 5)), (5, (-17, 31))):
        values = frozenset(
            (x + translate[0], y + translate[1])
            for x in range(side)
            for y in range(side)
        )
        cells.append(values)

    for lower in range(3, 20):
        band = [values for values in cells if lower <= len(values) < 2 * lower]
        if not band:
            continue
        for level in range(1, 5):
            expansive = []
            compressed = []
            for values in band:
                footprint = frozenset(footprint_counts(values))
                if 8 * level * len(footprint) > len(values) ** 2:
                    expansive.append((values, footprint))
                else:
                    compressed.append((values, footprint))

            depth: Counter[Point] = Counter()
            universe: set[Point] = set()
            expansive_mass = 0
            for values, footprint in expansive:
                depth.update(footprint)
                universe.update(footprint)
                expansive_mass += third_mass(len(values))
            depth_maximum = max(depth.values(), default=0)
            assert expansive_mass <= (
                8 * level * lower * depth_maximum * len(universe)
            )

            compressed_incidence = 0
            compressed_mass = 0
            for values, _ in compressed:
                popular = popular_perpendicular_directions(values, level)
                compressed_incidence += len(popular)
                compressed_mass += third_mass(len(values))
            assert compressed_mass * 5 * level <= (
                4 * lower**3 * compressed_incidence
            )


def verify_natural_owner_level() -> None:
    for load in range(1, 25):
        _, optima = optimal_loads(
            3, ((0, 1, load), (0, 2, load))
        )
        natural_level = 2 * load // 3
        for loads, _ in optima:
            assert min(loads) >= natural_level

    # The combined certificate: every compressed owner of load r has three
    # vertices in U_floor(2r/3) and at least 5L perpendicular popular
    # directions.  A large box supplies a nonvacuous compressed set.
    values = frozenset((x, y) for x in range(8) for y in range(8))
    load = len(values)
    level = 2
    assert 8 * level * len(footprint_counts(values)) <= load * load
    _, optima = optimal_loads(3, ((0, 1, load), (0, 2, load)))
    assert all(min(loads) >= 2 * load // 3 for loads, _ in optima)
    assert len(popular_perpendicular_directions(values, level)) >= 5 * level


def verify_constants() -> None:
    for size in range(3, 100):
        assert third_mass(size) <= size**3 // 2
        for lower in range((size + 1) // 2, size + 1):
            if lower <= size < 2 * lower:
                assert third_mass(size) < 4 * lower**3
    assert Fraction(4, 5) < 1


def main() -> None:
    verify_energy_identity()
    verify_compressed_fork()
    verify_dyadic_family_bound()
    verify_natural_owner_level()
    verify_constants()
    print("K2,4 natural-level footprint/density fork: PASS")


if __name__ == "__main__":
    main()
