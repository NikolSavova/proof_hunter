#!/usr/bin/env python3
"""Exact checks for the dyadic endpoint completion-box density gate."""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import product
from math import ceil, log2
import random

from analyze_affine_costas_energy import is_distance_sidon, welch
from analyze_swap_optimal_nested_cores import transformed_costas
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rich_fibres,
    rotate,
    subtract,
)


Point = tuple[int, int]


@dataclass(frozen=True)
class Record:
    group: int
    fibre: int
    corners: tuple[int, int, int, int]


def residual_records(records: list[Record]) -> tuple[list[Record], dict[int, int]]:
    groups: dict[int, list[Record]] = defaultdict(list)
    for record in records:
        groups[record.group].append(record)

    loads = {group: len(rows) for group, rows in groups.items()}
    residual = []
    for group, rows in groups.items():
        fibre_loads = Counter(record.fibre for record in rows)
        # The tie rule is deterministic but immaterial to the identity.
        major = min(
            fibre
            for fibre, load in fibre_loads.items()
            if load == max(fibre_loads.values())
        )
        residual.extend(record for record in rows if record.fibre != major)
    return residual, loads


def direct_energy(records: list[Record]) -> int:
    groups: dict[int, list[Record]] = defaultdict(list)
    for record in records:
        groups[record.group].append(record)
    return sum(
        len(rows)
        * (
            len(rows)
            - max(Counter(record.fibre for record in rows).values())
        )
        for rows in groups.values()
    )


def verify_one_abstract_system(records: list[Record], vertex_count: int) -> None:
    assert all(len(set(record.corners)) == 4 for record in records)
    residual, loads = residual_records(records)
    assert direct_energy(records) == sum(loads[row.group] for row in residual)

    degrees = Counter(
        corner for record in records for corner in record.corners
    )
    parallel_budget = (len(records) + 7) // 8
    assert len(records) <= 8 * parallel_budget
    assert sum(degrees.values()) <= 32 * parallel_budget
    maximum_load = max(loads.values(), default=0)
    for load_floor in [1 << exponent for exponent in range(0, 8)]:
        band = [
            record
            for record in residual
            if load_floor <= loads[record.group] < 2 * load_floor
        ]
        for reuse_cutoff in range(1, 10):
            low = [
                record
                for record in band
                if min(degrees[corner] for corner in record.corners)
                < reuse_cutoff
            ]
            weighted = sum(loads[record.group] for record in low)
            assert weighted < 2 * load_floor * reuse_cutoff * vertex_count
            high = [record for record in band if record not in low]
            band_weight = sum(loads[record.group] for record in band)
            assert band_weight == weighted + sum(
                loads[record.group] for record in high
            )
            assert band_weight <= (
                2 * load_floor * reuse_cutoff * vertex_count
                + 2 * load_floor * len(high)
            )
        band_weight = sum(loads[record.group] for record in band)
        assert band_weight <= 16 * load_floor * parallel_budget

    for parameter in range(1, maximum_load + 2):
        low_group_energy = sum(
            loads[record.group]
            for record in residual
            if loads[record.group] < parameter
        )
        assert low_group_energy <= 8 * parameter * parallel_budget

    # Check the global rich-corner decomposition (2.2) for several P.
    band_count = 1 + ceil(log2(2 * len(records))) if records else 1
    for parameter in range(1, 12):
        rich_weight = 0
        low_weight = 0
        for record in residual:
            load = loads[record.group]
            load_floor = 1 << (load.bit_length() - 1)
            threshold = parameter / load_floor
            if min(degrees[corner] for corner in record.corners) >= threshold:
                rich_weight += load
            else:
                low_weight += load
        assert direct_energy(records) == low_weight + rich_weight
        assert low_weight <= 2 * parameter * band_count * vertex_count

    assert maximum_load <= len(records)
    for reuse_cutoff in range(1, max(degrees.values(), default=0) + 2):
        rich_vertices = {
            vertex for vertex, degree in degrees.items() if degree >= reuse_cutoff
        }
        assert len(rich_vertices) * reuse_cutoff <= 32 * parallel_budget


def verify_abstract_completion_charge() -> None:
    rng = random.Random(1208)
    for vertex_count in range(4, 25):
        for _ in range(80):
            records = []
            group_count = rng.randint(1, 10)
            for group in range(group_count):
                for _ in range(rng.randint(1, 18)):
                    corners = tuple(rng.sample(range(vertex_count), 4))
                    records.append(
                        Record(group, rng.randrange(6), corners)
                    )
            verify_one_abstract_system(records, vertex_count)


def assert_vector_sidon(values: set[Point]) -> None:
    seen: dict[Point, tuple[Point, Point]] = {}
    for first in values:
        for second in values:
            if first == second:
                continue
            difference = subtract(first, second)
            assert difference not in seen
            seen[difference] = first, second


def footprint(values: set[Point], translation: Point) -> set[Point]:
    return {
        add(translation, add(rotate(first), linear(second)))
        for first, second in product(values, repeat=2)
    }


def verify_footprint_energy_and_depth() -> None:
    points = [(3 * x + y, x + 4 * y) for x, y in welch(17)]
    endpoint = points[0]
    role = {
        subtract(subtract(endpoint, other), (5, -7))
        for other in points
        if other != endpoint
    }
    assert_vector_sidon(role)

    rng = random.Random(481516)
    stars: list[tuple[set[Point], set[Point]]] = []
    role_list = sorted(role)
    for _ in range(30):
        size = rng.randint(1, min(9, len(role_list)))
        values = set(rng.sample(role_list, size))
        translation = (rng.randint(-6, 6), rng.randint(-6, 6))
        image = footprint(values, translation)
        h_value = len(values)

        # Direct energy check for J T + L T.
        representations = Counter(
            add(rotate(first), linear(second))
            for first, second in product(values, repeat=2)
        )
        energy = sum(load * load for load in representations.values())
        assert energy <= 2 * h_value * h_value - h_value
        assert len(image) * (2 * h_value * h_value - h_value) >= h_value**4
        assert 2 * len(image) >= h_value * h_value
        stars.append((values, image))

    depth = Counter(value for _, image in stars for value in image)
    maximum_depth = max(depth.values(), default=0)
    universe = set(depth)
    square_mass = sum(len(values) ** 2 for values, _ in stars)
    assert square_mass <= 2 * maximum_depth * len(universe)

    # Exhaust dyadic H subfamilies and the weighted inequality (1.9).
    for height_floor in (1, 2, 4, 8):
        selected = [
            (values, image)
            for values, image in stars
            if height_floor <= len(values) < 2 * height_floor
        ]
        if not selected:
            continue
        selected_depth = Counter(
            value for _, image in selected for value in image
        )
        delta = max(selected_depth.values())
        selected_universe = set(selected_depth)
        for load_floor in (1, 2, 4, 8):
            # Give each star any legal group load in [L,2L).
            loads = [
                rng.randint(load_floor, 2 * load_floor - 1)
                for _ in selected
            ]
            weighted = sum(
                load * len(values)
                for load, (values, _) in zip(loads, selected)
            )
            assert (
                weighted
                <= 4
                * load_floor
                * delta
                * len(selected_universe)
                / height_floor
            )


def verify_costas_matching_cross_support_barrier() -> None:
    points, differences = transformed_costas(23)
    assert is_distance_sidon(points)
    _, _, popular = rich_fibres(differences, adaptive=True)
    centre = (14, -11)
    ell = (50, 33)
    endpoint = (-124, -80)
    switch = (0, 23)
    h_value = add(ell, rotate(centre))
    rows = (
        ((-9, -11), (-69, 23), (27, -13), (-42, 10)),
        ((37, -57), (-23, 23), (-19, -13), (-42, 10)),
    )
    assert len({row[0] for row in rows}) == 2
    assert len({row[1] for row in rows}) == 2
    assert len({row[3] for row in rows}) == 1
    assert len({add(first[2], second[3]) for first in rows for second in rows}) == 2

    endpoint_map = {
        subtract(head, tail): (head, tail)
        for head in points
        for tail in points
        if head != tail
    }
    completion_vertices = set()
    for x_value, displacement, y_value, z_value in rows:
        q_value = subtract(centre, x_value)
        p_value = add(q_value, displacement)
        w_value = add(ell, linear(displacement))
        assert y_value == add(
            h_value,
            add(rotate((-x_value[0], -x_value[1])), rotate(displacement)),
        )
        assert z_value == add(
            h_value,
            add(rotate((-x_value[0], -x_value[1])), linear(displacement)),
        )
        assert {
            x_value,
            add(x_value, switch),
            y_value,
            subtract(y_value, rotate(switch)),
            z_value,
            subtract(z_value, rotate(switch)),
        } <= differences
        assert {
            q_value,
            subtract(q_value, switch),
            p_value,
            subtract(p_value, switch),
        } <= popular
        neighbour_label = add(centre, displacement)
        assert endpoint_map[neighbour_label][0] == endpoint

        vertices = (
            (p_value, x_value, ell),
            (subtract(p_value, switch), add(x_value, switch), ell),
            (q_value, x_value, w_value),
            (subtract(q_value, switch), add(x_value, switch), w_value),
        )
        assert len(set(vertices)) == 4
        for shift_value, first_start, second_start in vertices:
            assert shift_value in popular
            assert {
                first_start,
                add(first_start, shift_value),
                second_start,
                add(second_start, rotate(shift_value)),
            } <= differences
        completion_vertices.update(vertices)
    assert len(completion_vertices) == 8


def canonical_collision_colour(
    first_fibre: int,
    first_value: Point,
    second_fibre: int,
    second_value: Point,
) -> tuple[int, int, Point]:
    if first_fibre < second_fibre:
        return first_fibre, second_fibre, subtract(first_value, second_value)
    return second_fibre, first_fibre, subtract(second_value, first_value)


def verify_proper_collision_graph() -> None:
    rng = random.Random(314159)
    for fibre_count in range(2, 8):
        for _ in range(200):
            fibres: list[set[Point]] = []
            used: set[Point] = set()
            for _ in range(fibre_count):
                size = rng.randint(1, 7)
                fibre = set()
                while len(fibre) < size:
                    value = (rng.randrange(-30, 31), rng.randrange(-30, 31))
                    if value in used:
                        continue
                    used.add(value)
                    fibre.add(value)
                fibres.append(fibre)

            loads = [len(fibre) for fibre in fibres]
            total = sum(loads)
            largest = max(loads)
            residual = total - largest
            edge_count = sum(
                loads[first] * loads[second]
                for first in range(fibre_count)
                for second in range(first + 1, fibre_count)
            )
            envelope = total * residual
            assert edge_count <= envelope <= 2 * edge_count

            incident_colours: dict[tuple[int, Point], set[tuple[int, int, Point]]] = (
                defaultdict(set)
            )
            colour_edges: Counter[tuple[int, int, Point]] = Counter()
            for first in range(fibre_count):
                for second in range(first + 1, fibre_count):
                    for first_value in fibres[first]:
                        for second_value in fibres[second]:
                            colour = canonical_collision_colour(
                                first, first_value, second, second_value
                            )
                            for vertex in (
                                (first, first_value),
                                (second, second_value),
                            ):
                                assert colour not in incident_colours[vertex]
                                incident_colours[vertex].add(colour)
                            colour_edges[colour] += 1
            assert sum(colour_edges.values()) == edge_count
            # A proper colouring has matching colour classes.
            assert all(load <= total // 2 for load in colour_edges.values())


def main() -> None:
    verify_abstract_completion_charge()
    verify_footprint_energy_and_depth()
    verify_costas_matching_cross_support_barrier()
    verify_proper_collision_graph()
    print("SWAP COMPLETION-BOX DYADIC DENSITY GATE: PASS")


if __name__ == "__main__":
    main()
