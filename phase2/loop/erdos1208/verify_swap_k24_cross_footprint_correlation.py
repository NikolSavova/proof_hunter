#!/usr/bin/env python3
"""Verify the exact cross-footprint orthogonal correlation gate."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations


Point = tuple[int, int]


def add(first: Point, second: Point) -> Point:
    return first[0] + second[0], first[1] + second[1]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def rotate(value: Point) -> Point:
    return -value[1], value[0]


def cross_difference(first: tuple[Point, ...], second: tuple[Point, ...]):
    return Counter(subtract(x_value, y_value) for x_value in first for y_value in second)


def footprint_multiplicity(offset: Point, values: tuple[Point, ...]):
    return Counter(
        add(offset, subtract(rotate(second), first))
        for first in values
        for second in values
    )


def direct_cross_energy(
    first_offset: Point,
    first: tuple[Point, ...],
    second_offset: Point,
    second: tuple[Point, ...],
) -> int:
    first_load = footprint_multiplicity(first_offset, first)
    second_load = footprint_multiplicity(second_offset, second)
    return sum(
        first_load[value] * second_load[value]
        for value in first_load.keys() & second_load.keys()
    )


def correlation_cross_energy(
    first_offset: Point,
    first: tuple[Point, ...],
    second_offset: Point,
    second: tuple[Point, ...],
) -> int:
    difference_load = cross_difference(first, second)
    offset_difference = subtract(first_offset, second_offset)
    return sum(
        load
        * difference_load[add(offset_difference, rotate(difference))]
        for difference, load in difference_load.items()
    )


def verify_pair_identity_and_fork() -> None:
    families = (
        (
            ((0, 0), (1, 2), (4, -1), (7, 5)),
            ((-2, 1), (3, 0), (5, 4)),
            ((3, -4), (-1, 6)),
        ),
        (
            tuple((x, x * x) for x in range(7)),
            tuple((x - 2, -x * x + 3) for x in range(6)),
            ((0, 0), (4, -7)),
        ),
    )
    for first, second, (first_offset, second_offset) in families:
        direct = direct_cross_energy(first_offset, first, second_offset, second)
        correlation = correlation_cross_energy(
            first_offset, first, second_offset, second
        )
        assert direct == correlation

        difference_load = cross_difference(first, second)
        cross_additive_energy = sum(load * load for load in difference_load.values())
        assert direct <= cross_additive_energy

        first_support = set(footprint_multiplicity(first_offset, first))
        second_support = set(footprint_multiplicity(second_offset, second))
        assert len(first_support & second_support) <= direct

        offset_difference = subtract(first_offset, second_offset)
        for level in range(1, 6):
            popular = {
                difference
                for difference, load in difference_load.items()
                if load >= level
                and difference_load[
                    add(offset_difference, rotate(difference))
                ]
                >= level
            }
            popular_mass = sum(
                difference_load[difference]
                * difference_load[add(offset_difference, rotate(difference))]
                for difference in popular
            )
            baseline = 2 * level * len(first) * len(second)
            assert direct <= baseline + popular_mass
            if direct > baseline:
                minimum_size = min(len(first), len(second))
                assert len(popular) * minimum_size**2 >= direct - baseline


def verify_family_identity() -> None:
    cells = (
        ((0, 0), ((0, 0), (1, 2), (4, -1), (7, 5))),
        ((3, -4), ((-2, 1), (3, 0), (5, 4))),
        ((-5, 2), tuple((x, x * x) for x in range(5))),
        ((1, 7), tuple((2 * x, -x * x) for x in range(4))),
    )
    multiplicities = [footprint_multiplicity(*cell) for cell in cells]
    supports = [set(load) for load in multiplicities]
    total_load: Counter[Point] = Counter()
    diagonal_energy = 0
    for load in multiplicities:
        total_load.update(load)
        diagonal_energy += sum(value * value for value in load.values())
    direct_family_energy = sum(
        sum(
            multiplicities[first][value] * multiplicities[second][value]
            for value in supports[first] & supports[second]
        )
        for first, second in combinations(range(len(cells)), 2)
    )
    square_identity = (
        sum(value * value for value in total_load.values()) - diagonal_energy
    ) // 2
    assert direct_family_energy == square_identity

    support_collision = sum(
        len(supports[first] & supports[second])
        for first, second in combinations(range(len(cells)), 2)
    )
    assert support_collision <= direct_family_energy

    for level in range(1, 5):
        active_product = 0
        popular_mass = 0
        for first_index, second_index in combinations(range(len(cells)), 2):
            pair_energy = direct_cross_energy(
                cells[first_index][0],
                cells[first_index][1],
                cells[second_index][0],
                cells[second_index][1],
            )
            if not pair_energy:
                continue
            active_product += len(cells[first_index][1]) * len(
                cells[second_index][1]
            )
            loads = cross_difference(
                cells[first_index][1], cells[second_index][1]
            )
            offset_difference = subtract(
                cells[first_index][0], cells[second_index][0]
            )
            popular_mass += sum(
                load * loads[add(offset_difference, rotate(difference))]
                for difference, load in loads.items()
                if load >= level
                and loads[add(offset_difference, rotate(difference))] >= level
            )
        assert direct_family_energy <= 2 * level * active_product + popular_mass


def verify_diagonal_baseline_barrier() -> None:
    for size in range(2, 13):
        values = tuple((2**index, 0) for index in range(size))
        load = footprint_multiplicity((0, 0), values)
        assert len(load) == size * size
        assert set(load.values()) == {1}
        energy = direct_cross_energy((0, 0), values, (0, 0), values)
        assert energy == size * size
        differences = cross_difference(values, values)
        assert differences[(0, 0)] == size
        assert all(
            multiplicity == 1
            for difference, multiplicity in differences.items()
            if difference != (0, 0)
        )
        level_two_popular = {
            difference
            for difference, multiplicity in differences.items()
            if multiplicity >= 2 and differences[rotate(difference)] >= 2
        }
        assert level_two_popular == {(0, 0)}
        assert energy <= 4 * size * size


def canonical_representations(
    offset: Point,
    values: tuple[Point, ...],
) -> dict[Point, tuple[Point, Point]]:
    output: dict[Point, tuple[Point, Point]] = {}
    for first in sorted(values):
        for second in sorted(values):
            value = add(offset, subtract(rotate(second), first))
            output.setdefault(value, (first, second))
    return output


def verify_dense_collision_common_chords() -> None:
    first = tuple((x, y) for x in range(3) for y in range(2))
    second = first
    first_offset = (0, 0)
    second_offset = (0, 0)
    first_representations = canonical_representations(first_offset, first)
    second_representations = canonical_representations(second_offset, second)
    cross_load = cross_difference(first, second)
    dense_seen = False
    for value in first_representations.keys() & second_representations.keys():
        first_pair = first_representations[value]
        second_pair = second_representations[value]
        first_difference = subtract(first_pair[0], second_pair[0])
        second_difference = subtract(first_pair[1], second_pair[1])
        if cross_load[first_difference] < 2 or cross_load[second_difference] < 2:
            continue
        dense_seen = True
        first_difference_pairs = sorted(
            (x_value, y_value)
            for x_value in first
            for y_value in second
            if subtract(x_value, y_value) == first_difference
        )
        second_difference_pairs = sorted(
            (x_value, y_value)
            for x_value in first
            for y_value in second
            if subtract(x_value, y_value) == second_difference
        )
        assert len(first_difference_pairs) >= 2
        assert len(second_difference_pairs) >= 2
        first_chord = subtract(
            first_difference_pairs[0][0], first_difference_pairs[1][0]
        )
        first_chord_prime = subtract(
            first_difference_pairs[0][1], first_difference_pairs[1][1]
        )
        second_chord = subtract(
            second_difference_pairs[0][0], second_difference_pairs[1][0]
        )
        second_chord_prime = subtract(
            second_difference_pairs[0][1], second_difference_pairs[1][1]
        )
        assert first_chord == first_chord_prime != (0, 0)
        assert second_chord == second_chord_prime != (0, 0)

        # Keeping the original second-parameter pair and replacing the
        # first-parameter pair by its two representations produces two
        # distinct points in both footprints.
        common_values = {
            add(
                first_offset,
                subtract(rotate(first_pair[1]), replacement[0]),
            )
            for replacement in first_difference_pairs[:2]
        }
        assert len(common_values) == 2
        assert common_values <= set(first_representations)
        assert common_values <= set(second_representations)
        break
    assert dense_seen


def verify_same_owner_resonant_capacity() -> None:
    owner_vertices = ("C0", "C1", "C2")
    resonances = ("e=0", "e=b-a", "e=L(a-b)")
    cells = {
        (centre, first, second, resonance)
        for centre in owner_vertices
        for first in owner_vertices
        for second in owner_vertices
        for resonance in resonances
        if len({centre, first, second}) == 3
    }
    assert len(cells) == 18
    assert len(list(combinations(cells, 2))) == 153
    for lower in range(3, 20):
        maximum_footprint = (2 * lower - 1) ** 2
        support_envelope = 153 * maximum_footprint
        weighted_envelope = 153 * (2 * lower - 1) ** 3
        assert support_envelope < 612 * lower**2
        assert weighted_envelope < 1224 * lower**3


def main() -> None:
    verify_pair_identity_and_fork()
    verify_family_identity()
    verify_diagonal_baseline_barrier()
    verify_dense_collision_common_chords()
    verify_same_owner_resonant_capacity()
    print("K2,4 cross-footprint orthogonal correlation gate: PASS")


if __name__ == "__main__":
    main()
