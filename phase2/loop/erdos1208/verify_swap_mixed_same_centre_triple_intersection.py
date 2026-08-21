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
        for second in subsets:
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
        audit(v_fibres, w_fibres)


def main() -> None:
    exhaustive_small()
    random_systems()
    print("SWAP MIXED SAME-CENTRE TRIPLE INTERSECTION: PASS")


if __name__ == "__main__":
    main()
