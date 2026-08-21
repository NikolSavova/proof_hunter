#!/usr/bin/env python3
"""Verify the same-centre switch-axis triple-intersection identity."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import comb
from random import Random

Point = tuple[int, int]


def add(first: Point, second: Point) -> Point:
    return first[0] + second[0], first[1] + second[1]


def sub(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def rotate(value: Point) -> Point:
    return -value[1], value[0]


def starts(values: set[Point], switch: Point) -> set[Point]:
    return {value for value in values if add(value, switch) in values}


def triple_load(values: set[Point], first: Point, second: Point) -> int:
    return len(starts(values, first) & starts(values, second))


def cross_difference_loads(
    first: set[Point], second: set[Point]
) -> Counter[Point]:
    return Counter(
        sub(second_value, first_value)
        for first_value in first
        for second_value in second
    )


def all_switches(families: list[set[Point]]) -> list[Point]:
    return sorted(
        {
            sub(second, first)
            for values in families
            for first in values
            for second in values
            if first != second
        }
    )


def perpendicular_footprint_audit(values: set[Point]) -> None:
    """Check the internal footprint / adaptive-density dichotomy."""
    load = len(values)
    differences = Counter(
        sub(first, second) for first in values for second in values
    )
    footprint_loads = Counter(
        sub(rotate(second), first)
        for first in values
        for second in values
    )
    energy = sum(value * value for value in footprint_loads.values())
    perpendicular_energy = sum(
        differences[shift] * differences[rotate(shift)]
        for shift in differences
    )
    assert energy == perpendicular_energy
    assert len(footprint_loads) * energy >= load**4

    # The two affine copies -S and J S may be translated independently
    # into D.  Their cross-sum contains a translate of J S-S.
    first_offset = (7, -11)
    second_offset = (-5, 13)
    difference_set = {
        add(first_offset, (-value[0], -value[1])) for value in values
    } | {
        add(second_offset, rotate(value)) for value in values
    }
    translated_footprint = {
        add(add(second_offset, first_offset), point)
        for point in footprint_loads
    }
    sumset = {add(first, second) for first in difference_set for second in difference_set}
    assert translated_footprint <= sumset

    for threshold in range(1, load + 2):
        rich_shifts = {
            shift
            for shift in differences
            if shift != (0, 0)
            and differences[shift] >= threshold
            and differences[rotate(shift)] >= threshold
        }
        rich_energy = sum(
            differences[shift] * differences[rotate(shift)]
            for shift in rich_shifts
        )
        assert perpendicular_energy <= (
            load * load
            + 2 * threshold * load * max(0, load - 1)
            + rich_energy
        )


def translate_partition_audit(first: set[Point], second: set[Point]) -> None:
    """Check the lossless refinement of the mixed second pencil."""
    translations = cross_difference_loads(first, second)
    cells = {
        difference: {
            value
            for value in first
            if add(value, difference) in second
        }
        for difference in translations
    }
    switches = {
        sub(left, right)
        for values in cells.values()
        for left in values
        for right in values
        if left != right
    }
    cross_third = 3 * sum(comb(load, 3) for load in translations.values())
    refined_third = 0
    for difference, values in cells.items():
        load = len(values)
        refined_third += sum(
            max(0, load - 2) * len(starts(values, switch))
            for switch in switches
        )
    assert 2 * cross_third == refined_third

    all_internal_switches = all_switches([first, second])
    for switch in all_internal_switches:
        cell_first_moment = sum(
            len(starts(values, switch)) for values in cells.values()
        )
        assert cell_first_moment == (
            len(starts(first, switch)) * len(starts(second, switch))
        )


def audit(v_fibres: list[set[Point]], w_fibres: list[set[Point]]) -> None:
    switches = all_switches(v_fibres + w_fibres)
    a_load = Counter()
    b_load = Counter()
    direct_collision = 0

    v_group_keys = {
        switch: {
            (index, value)
            for index, values in enumerate(v_fibres)
            for value in starts(values, switch)
        }
        for switch in switches
    }
    w_group_keys = {
        switch: {
            (index, value)
            for index, values in enumerate(w_fibres)
            for value in starts(values, switch)
        }
        for switch in switches
    }

    for first, second in combinations(switches, 2):
        a = sum(triple_load(values, first, second) for values in v_fibres)
        b = sum(triple_load(values, first, second) for values in w_fibres)
        assert a == len(v_group_keys[first] & v_group_keys[second])
        assert b == len(w_group_keys[first] & w_group_keys[second])
        a_load[first, second] = a
        b_load[first, second] = b
        direct_collision += len(
            {
                (v_key, w_key)
                for v_key in v_group_keys[first] & v_group_keys[second]
                for w_key in w_group_keys[first] & w_group_keys[second]
            }
        )

    collision = sum(a_load[pair] * b_load[pair] for pair in a_load)
    assert collision == direct_collision

    directed_switches = switches
    weighted_envelope = 0
    mixed_second_pencil = 0
    for switch in directed_switches:
        lambda_v = sum(len(starts(values, switch)) for values in v_fibres)
        lambda_w = sum(len(starts(values, switch)) for values in w_fibres)
        weighted_v = sum(
            max(0, len(values) - 2) * len(starts(values, switch))
            for values in v_fibres
        )
        weighted_w = sum(
            max(0, len(values) - 2) * len(starts(values, switch))
            for values in w_fibres
        )
        mixed_second_pencil += lambda_v * lambda_w
        weighted_envelope += min(
            lambda_w * weighted_v,
            lambda_v * weighted_w,
        )
    assert 2 * collision <= weighted_envelope

    cross_third_energy = 0
    cross_second_energy = 0
    maximum_cross_load = 0
    for v_values in v_fibres:
        for w_values in w_fibres:
            loads = cross_difference_loads(v_values, w_values)
            cross_third_energy += 3 * sum(
                comb(load, 3) for load in loads.values()
            )
            cross_second_energy += sum(
                comb(load, 2) for load in loads.values()
            )
            maximum_cross_load = max(
                maximum_cross_load,
                max(loads.values(), default=0),
            )
    assert collision == cross_third_energy
    assert collision <= max(0, maximum_cross_load - 2) * cross_second_energy

    v_triples = 3 * sum(comb(len(values), 3) for values in v_fibres)
    w_triples = 3 * sum(comb(len(values), 3) for values in w_fibres)
    assert sum(a_load.values()) == v_triples
    assert sum(b_load.values()) == w_triples

    theta_v = max(a_load.values(), default=0)
    theta_w = max(b_load.values(), default=0)
    assert collision <= min(
        theta_w * v_triples,
        theta_v * w_triples,
    )

    maximum = max(
        (len(values) for values in v_fibres + w_fibres),
        default=0,
    )
    assert weighted_envelope <= max(0, maximum - 2) * mixed_second_pencil
    v_wedges = sum(comb(len(values), 2) for values in v_fibres)
    w_wedges = sum(comb(len(values), 2) for values in w_fibres)
    assert v_triples <= maximum * v_wedges
    assert w_triples <= maximum * w_wedges
    assert theta_v <= maximum * len(v_fibres)
    assert theta_w <= maximum * len(w_fibres)
    assert collision <= maximum * maximum * min(
        len(w_fibres) * v_wedges,
        len(v_fibres) * w_wedges,
    )


def exhaustive_small() -> None:
    universe = [(0, 0), (1, 0), (0, 1), (1, 1)]
    subsets = [
        {universe[index] for index in range(len(universe)) if mask >> index & 1}
        for mask in range(1 << len(universe))
    ]
    for first in subsets:
        perpendicular_footprint_audit(first)
        for second in subsets:
            translate_partition_audit(first, second)
            audit([first], [second])


def random_systems() -> None:
    rng = Random(1208)
    box = [(x, y) for x in range(-2, 3) for y in range(-2, 3)]
    for _ in range(600):
        v_fibres = [
            {value for value in box if rng.randrange(5) == 0}
            for _ in range(rng.randrange(1, 5))
        ]
        w_fibres = [
            {value for value in box if rng.randrange(5) == 0}
            for _ in range(rng.randrange(1, 5))
        ]
        for values in v_fibres + w_fibres:
            perpendicular_footprint_audit(values)
        for first in v_fibres:
            for second in w_fibres:
                translate_partition_audit(first, second)
        audit(v_fibres, w_fibres)


def ambient_representation_domination_barrier() -> None:
    """A symmetric affine-copy model kills a D+D pointwise shortcut."""
    for load in (4, 6, 8, 12, 20):
        values = {(index, index * index) for index in range(load)}
        scale = 10**7
        first_copy = {
            (scale - value[0], -value[1]) for value in values
        }
        second_copy = {
            add((0, scale), rotate(value)) for value in values
        }
        difference_model = (
            first_copy
            | second_copy
            | {(-value[0], -value[1]) for value in first_copy | second_copy}
        )
        footprint = {
            add((scale, scale), sub(rotate(second), first))
            for first in values
            for second in values
        }
        assert len(footprint) == load * load
        ambient_load = Counter(
            add(first, second)
            for first in difference_model
            for second in difference_model
        )
        assert {ambient_load[value] for value in footprint} == {2}
        uniform_weight = 3 * comb(load, 3) / len(footprint)
        if load >= 8:
            assert uniform_weight > 2


def main() -> None:
    exhaustive_small()
    random_systems()
    ambient_representation_domination_barrier()
    print("SWAP MIXED SAME-CENTRE TRIPLE INTERSECTION: PASS")


if __name__ == "__main__":
    main()
