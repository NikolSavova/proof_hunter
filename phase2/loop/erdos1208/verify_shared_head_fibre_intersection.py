#!/usr/bin/env python3
"""Checks for SHARED_HEAD_FIBRE_INTERSECTION_SWITCH.md."""

from __future__ import annotations

from collections import Counter

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_metric_scalar_squareclass_transverse import endpoint_map
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Profile = tuple[int, ...]


def add(first: Point, second: Point) -> Point:
    return first[0] + second[0], first[1] + second[1]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def profile(points: list[Point]) -> Profile:
    k_value = len(points)
    fibres = {
        difference: set(starts)
        for difference, starts in clean_start_fibres(points).items()
    }
    endpoints = endpoint_map(points)
    clean_mass = sum(map(len, fibres.values()))
    number_edges = k_value * (k_value - 1) // 2
    exceptional_limit = (k_value - 3) // 2

    # Recover the unique ordered anchors of every realized difference and
    # form the shared-head incidence degrees d_a(s).
    anchors: dict[Point, tuple[Point, Point]] = {}
    for head in points:
        for tail in points:
            if head != tail:
                difference = subtract(head, tail)
                assert difference not in anchors
                anchors[difference] = (head, tail)
    head_degrees: Counter[tuple[Point, Point]] = Counter()
    for difference, starts in fibres.items():
        head, tail = anchors[difference]
        for start in starts:
            head_degrees[head, start] += 1
    assert sum(head_degrees.values()) == clean_mass

    total_intersection = 0
    total_nonexceptional = 0
    total_exceptional = 0
    ordered_second_falling = 0
    maximum_intersection = 0
    exceptional_by_tail: Counter[Point] = Counter()
    nonexceptional_output_load: Counter[tuple[Point, Point, Point]] = Counter()

    for head in points:
        for first_tail in points:
            if first_tail == head:
                continue
            first_difference = subtract(head, first_tail)
            first_fibre = fibres.get(first_difference, set())
            for second_tail in points:
                if second_tail in (head, first_tail):
                    continue
                second_difference = subtract(head, second_tail)
                tail_difference = subtract(second_tail, first_tail)
                intersection = first_fibre.intersection(
                    fibres.get(second_difference, set())
                )
                intersection_size = len(intersection)
                maximum_intersection = max(maximum_intersection, intersection_size)
                total_intersection += intersection_size
                ordered_second_falling += intersection_size * (intersection_size - 1)

                exceptional_sources: list[frozenset[Point]] = []
                exceptional_count = 0
                for start in intersection:
                    switched_start = add(start, second_difference)
                    if switched_start in fibres.get(tail_difference, set()):
                        total_nonexceptional += 1
                        nonexceptional_output_load[
                            second_tail, first_tail, switched_start
                        ] += 1
                        # The reconstructed head must avoid the six points
                        # in this output clean record.
                        switched_target = add(switched_start, tail_difference)
                        forbidden = {
                            second_tail, first_tail,
                            *endpoints[switched_start],
                            *endpoints[switched_target],
                        }
                        assert len(forbidden) == 6 and head not in forbidden
                        continue

                    total_exceptional += 1
                    exceptional_count += 1
                    exceptional_by_tail[tail_difference] += 1
                    first_target = set(endpoints[switched_start])
                    second_target = set(endpoints[add(start, first_difference)])
                    common = first_target.intersection(second_target)
                    assert len(common) == 1
                    outer = next(iter(common))
                    assert first_target == {outer, first_tail}
                    assert second_target == {outer, second_tail}
                    source_edge = frozenset(endpoints[start])
                    assert source_edge.isdisjoint({head, first_tail, second_tail})
                    exceptional_sources.append(source_edge)

                # Exceptional source edges form a matching outside the
                # three fixed anchors.
                exceptional_vertices = [
                    vertex for edge in exceptional_sources for vertex in edge
                ]
                assert len(exceptional_vertices) == len(set(exceptional_vertices))
                assert exceptional_count <= exceptional_limit
                assert intersection_size <= (
                    len(fibres.get(tail_difference, set())) + exceptional_limit
                )

    assert total_intersection == total_nonexceptional + total_exceptional
    assert total_exceptional == 2 * clean_mass
    assert total_nonexceptional <= (k_value - 6) * clean_mass
    assert total_intersection <= (k_value - 4) * clean_mass
    assert max(nonexceptional_output_load.values(), default=0) <= k_value - 6

    degree_falling = sum(
        degree * (degree - 1) for degree in head_degrees.values()
    )
    degree_square = sum(degree * degree for degree in head_degrees.values())
    assert degree_falling == total_intersection
    assert degree_square == clean_mass + total_intersection
    assert degree_square <= (k_value - 3) * clean_mass

    # Reciprocal intersection moment (1.9), kept in exact cross-multiplied
    # form record by record.
    reciprocal_moment = 0.0
    square_moment = 0
    for head in points:
        for first_tail in points:
            if first_tail == head:
                continue
            for second_tail in points:
                if second_tail in (head, first_tail):
                    continue
                first_fibre = fibres.get(subtract(head, first_tail), set())
                second_fibre = fibres.get(subtract(head, second_tail), set())
                intersection_size = len(first_fibre.intersection(second_fibre))
                tail_size = len(fibres.get(subtract(second_tail, first_tail), set()))
                denominator = tail_size + exceptional_limit
                assert intersection_size <= denominator
                reciprocal_moment += intersection_size * intersection_size / denominator
                square_moment += intersection_size * intersection_size
    assert reciprocal_moment <= total_intersection + 1e-9
    assert reciprocal_moment <= (k_value - 4) * clean_mass + 1e-9

    # The H_2-sensitive head-codegree moment bound (5.6).
    fibre_square_mass = sum(len(starts) ** 2 for starts in fibres.values())
    head_bound = (
        (k_value - 6)
        * (fibre_square_mass + exceptional_limit * clean_mass)
        + 2 * (number_edges + exceptional_limit) * clean_mass
    )
    assert square_moment <= head_bound
    assert sum(exceptional_by_tail.values()) == 2 * clean_mass

    return (
        k_value,
        clean_mass,
        total_intersection,
        total_nonexceptional,
        total_exceptional,
        maximum_intersection,
        degree_square,
        ordered_second_falling,
        max(exceptional_by_tail.values(), default=0),
    )


def main() -> None:
    families = [
        ("closure-20", POINTS[:20]),
        ("closure-40", POINTS[:40]),
        ("Costas-22", transformed_costas(23)),
        ("parabola-43", transformed_parabola_43()),
        ("ruler-40", ruler_points()),
    ]
    expected: dict[str, Profile] = {
        "closure-20": (20, 648, 1_296, 0, 1_296, 2, 1_944, 240, 15),
        "closure-40": (
            40, 12_420, 32_616, 7_776, 24_840, 7, 45_036, 24_844, 54,
        ),
        "Costas-22": (
            22, 9_342, 36_180, 17_496, 18_684, 12, 45_522, 145_820, 75,
        ),
        "parabola-43": (
            43, 190_278, 1_507_104, 1_126_548, 380_556, 49,
            1_697_382, 34_799_420, 348,
        ),
        "ruler-40": (
            40, 4_914, 11_286, 1_458, 9_828, 5, 16_200, 7_776, 33,
        ),
    }
    for name, points in families:
        actual = profile(points)
        assert actual == expected[name], (name, actual, expected[name])
        print(name, actual)

    print("shared-head fibre intersection switch: PASS")


if __name__ == "__main__":
    main()
