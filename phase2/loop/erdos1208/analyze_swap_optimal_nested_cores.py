#!/usr/bin/env python3
"""Measure exact quadratic-optimal nested cores in the Erdős 1208 swap graph.

The optimizer uses path reversals.  Reversing a directed path moves one unit
of outdegree from its first vertex to its last vertex.  An orientation is
quadratic-optimal exactly when no directed path goes from load at least two
larger to load at least two smaller.  Components of the stored swap graphs
are tiny, so the resulting exact algorithm is fast despite large global
record counts.

This is a diagnostic, not a proof of the remaining endpoint-geometric gate.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import ceil, log2
import sys

from analyze_affine_costas_energy import is_distance_sidon, welch
from verify_determinant_prime_costas_resonance import ROWS, apply
from verify_orthogonal_two_support_gate import difference_set
from verify_radial_orthogonal_product_barrier import radial_set
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rich_fibres,
    rotate,
    subtract,
)
from verify_swap_cell_component_gate import cell_invariant
from verify_swap_cell_degeneracy_charge import build_swap_multigraph
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Cell = tuple[Point, Point]
Edge = tuple[Cell, Cell]
Fibre = tuple[Point, Point]


@dataclass(frozen=True)
class CoreProfile:
    vertices: int
    edge_copies: int
    optimum_energy: int
    nested_mass: int
    balance_mass: int
    maximum_load: int
    dyadic_level: int
    core_vertices: int
    core_edge_copies: int
    core_distinct_edges: int
    core_components: int
    maximum_component_edge_copies: int
    maximum_parallel_multiplicity: int
    distinct_shifts: int
    maximum_shift_multiplicity: int
    distinct_fibres: int
    maximum_fibre_multiplicity: int


def connected_components(edge_multiplicity: Counter[Edge]) -> list[set[Cell]]:
    adjacency: dict[Cell, set[Cell]] = defaultdict(set)
    for first, second in edge_multiplicity:
        adjacency[first].add(second)
        adjacency[second].add(first)

    unseen = set(adjacency)
    output = []
    while unseen:
        root = unseen.pop()
        component = {root}
        queue = [root]
        while queue:
            vertex = queue.pop()
            for neighbour in adjacency[vertex]:
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    component.add(neighbour)
                    queue.append(neighbour)
        output.append(component)
    return output


def optimize_component(
    vertices: set[Cell],
    edge_multiplicity: Counter[Edge],
) -> tuple[dict[Cell, int], dict[Cell, dict[Cell, int]], int]:
    """Return exact optimal loads and directed multiplicities.

    We start by orienting every parallel class according to the canonical
    cell order.  While a directed path joins loads differing by at least two,
    reverse the largest energy-decreasing batch supported on that path.
    Absence of such a path is the standard exchange certificate for a
    minimum separable-convex orientation.
    """

    directed: dict[Cell, dict[Cell, int]] = {
        vertex: defaultdict(int) for vertex in vertices
    }
    loads = {vertex: 0 for vertex in vertices}
    for (first, second), multiplicity in edge_multiplicity.items():
        if first not in vertices:
            continue
        directed[first][second] += multiplicity
        loads[first] += multiplicity

    reversals = 0
    while True:
        best_gap = 1
        best_path: list[Cell] | None = None
        for source in sorted(vertices, key=lambda vertex: loads[vertex], reverse=True):
            parent: dict[Cell, Cell | None] = {source: None}
            queue = deque([source])
            while queue:
                vertex = queue.popleft()
                for neighbour, multiplicity in directed[vertex].items():
                    if multiplicity <= 0 or neighbour in parent:
                        continue
                    parent[neighbour] = vertex
                    queue.append(neighbour)

            target = min(parent, key=lambda vertex: loads[vertex])
            gap = loads[source] - loads[target]
            if gap <= best_gap:
                continue
            path = [target]
            while path[-1] != source:
                previous = parent[path[-1]]
                assert previous is not None
                path.append(previous)
            path.reverse()
            best_gap = gap
            best_path = path

        if best_path is None:
            break

        capacity = min(
            directed[first][second]
            for first, second in zip(best_path, best_path[1:])
        )
        batch = min(capacity, best_gap // 2)
        assert batch >= 1
        source, target = best_path[0], best_path[-1]
        old_energy = sum(load * load for load in loads.values())
        for first, second in zip(best_path, best_path[1:]):
            directed[first][second] -= batch
            directed[second][first] += batch
        loads[source] -= batch
        loads[target] += batch
        new_energy = sum(load * load for load in loads.values())
        assert new_energy < old_energy
        reversals += batch

    # The path-exchange optimality certificate in particular implies the
    # one-edge inequality used by the nested-core identity.
    for first in vertices:
        for second, multiplicity in directed[first].items():
            if multiplicity:
                assert loads[first] <= loads[second] + 1

    assert sum(loads.values()) == sum(
        multiplicity
        for edge, multiplicity in edge_multiplicity.items()
        if edge[0] in vertices
    )
    return loads, directed, reversals


def exact_optimum(
    edge_multiplicity: Counter[Edge],
) -> tuple[dict[Cell, int], int, int]:
    loads: dict[Cell, int] = {}
    total_energy = 0
    total_reversals = 0
    components = connected_components(edge_multiplicity)
    component_index = {
        vertex: index
        for index, component in enumerate(components)
        for vertex in component
    }
    component_edges = [Counter() for _ in components]
    for edge, multiplicity in edge_multiplicity.items():
        index = component_index[edge[0]]
        assert component_index[edge[1]] == index
        component_edges[index][edge] = multiplicity

    for component, edges in zip(components, component_edges):
        component_loads, _, reversals = optimize_component(
            component, edges
        )
        loads.update(component_loads)
        total_energy += sum(load * load for load in component_loads.values())
        total_reversals += reversals
    return loads, total_energy, total_reversals


def profile(
    differences: set[Point],
    points: list[Point] | None = None,
) -> tuple[CoreProfile, dict[str, tuple[tuple[object, int], ...]], int]:
    edge_multiplicity, occurrences, ordered_mass = build_swap_multigraph(
        differences
    )
    _, ordinary_support, adaptive_popular = rich_fibres(
        differences, adaptive=True
    )
    assert ordinary_support >= len(differences)
    loads, energy, reversals = exact_optimum(edge_multiplicity)
    edge_copies = sum(edge_multiplicity.values())
    assert ordered_mass == 2 * edge_copies

    minimum_histogram: Counter[int] = Counter()
    balance_mass = 0
    for (first, second), multiplicity in edge_multiplicity.items():
        minimum_histogram[min(loads[first], loads[second])] += multiplicity
        # In an optimum, each copy can be oriented so the nested identity's
        # remainder is exactly the number of copies whose tail has load one
        # larger.  The value is forced by energy minus the minimum sum.
    nested_mass = sum(level * count for level, count in minimum_histogram.items())
    balance_mass = energy - nested_mass
    assert 0 <= balance_mass <= edge_copies

    maximum_load = max(loads.values(), default=0)
    blocks = ceil(log2(maximum_load + 1)) if maximum_load else 0
    dyadic_levels = [1 << index for index in range(blocks)]

    def edge_count(level: int) -> int:
        return sum(
            multiplicity
            for (first, second), multiplicity in edge_multiplicity.items()
            if loads[first] >= level and loads[second] >= level
        )

    dyadic_level = max(
        dyadic_levels,
        key=lambda level: level * edge_count(level),
        default=0,
    )
    core = {vertex for vertex, load in loads.items() if load >= dyadic_level}
    core_edges = Counter(
        {
            edge: multiplicity
            for edge, multiplicity in edge_multiplicity.items()
            if edge[0] in core and edge[1] in core
        }
    )
    core_edge_copies = sum(core_edges.values())
    assert not maximum_load or dyadic_level * core_edge_copies * blocks >= nested_mass
    assert dyadic_level * len(core) <= edge_copies

    component_mass: Counter[Point] = Counter()
    shift_mass: Counter[Point] = Counter()
    fibre_mass: Counter[Fibre] = Counter()
    endpoint_types: Counter[str] = Counter()
    potential_edge_types: Counter[str] = Counter()
    potential_shift_mass: Counter[Point] = Counter()
    potential_fibres: Counter[tuple[str, Point, Point]] = Counter()
    matching_adjacency: dict[Cell, Counter[Cell]] = defaultdict(Counter)
    matching_records: dict[Cell, list[tuple[Cell, Fibre]]] = defaultdict(list)
    cell_records: dict[Cell, list[tuple[Point, Point, Point, Point, Point]]] = (
        defaultdict(list)
    )
    endpoint_map: dict[Point, tuple[Point, Point]] = {}
    if points is not None:
        for head in points:
            for tail in points:
                if head == tail:
                    continue
                value = subtract(head, tail)
                assert value not in endpoint_map
                endpoint_map[value] = head, tail

    def endpoints(value: Point) -> set[Point]:
        return set(endpoint_map.get(value, ()))

    def endpoint_relation(first_value: Point, second_value: Point) -> str:
        first_pair = endpoint_map.get(first_value)
        second_pair = endpoint_map.get(second_value)
        if first_pair is None or second_pair is None:
            return "none"
        if first_pair[0] == second_pair[0] or first_pair[1] == second_pair[1]:
            return "parallel"
        if first_pair[0] == second_pair[1] or first_pair[1] == second_pair[0]:
            return "cross"
        return "none"

    def mixed_potentials(cell: Cell) -> tuple[Point, Point] | None:
        b_pair = endpoint_map.get(cell[0])
        ell_pair = endpoint_map.get(cell[1])
        if b_pair is None or ell_pair is None:
            return None
        alpha = subtract(ell_pair[0], linear(b_pair[0]))
        beta = subtract(ell_pair[1], linear(b_pair[1]))
        assert subtract(alpha, beta) == cell_invariant(cell)
        return alpha, beta

    def inverse_linear(value: Point) -> Point:
        assert (value[0] + value[1]) % 2 == 0
        assert (value[1] - value[0]) % 2 == 0
        return (
            (value[0] + value[1]) // 2,
            (value[1] - value[0]) // 2,
        )

    for (first, second), multiplicity in core_edges.items():
        invariant = cell_invariant(first)
        assert invariant == cell_invariant(second)
        component_mass[invariant] += multiplicity
        shift = subtract(second[0], first[0])
        assert second[1] == (
            first[1][0] + linear(shift)[0],
            first[1][1] + linear(shift)[1],
        )
        shift_mass[shift] += multiplicity
        fibre_mass.update(occurrences[(first, second)])
        for base, ordinary_sum in occurrences[(first, second)]:
            w_value = subtract(ordinary_sum, base)
            q_value = subtract(first[0], base)
            p_value = inverse_linear(subtract(w_value, first[1]))
            assert second[0] == (
                base[0] + p_value[0],
                base[1] + p_value[1],
            )
            assert second[1] == subtract(w_value, linear(q_value))
            q_head = first[0]
            p_head = second[0]
            z_q = subtract(w_value, q_value)
            z_p = subtract(w_value, p_value)
            l_q = second[1]
            l_p = first[1]
            # Five moving roles relative to each fixed endpoint cell.
            cell_records[first].append((base, p_head, z_q, z_p, l_q))
            cell_records[second].append((base, q_head, z_p, z_q, l_p))
        if points is not None:
            first_b, first_ell = first
            second_b, second_ell = second
            b_relation = endpoint_relation(first_b, second_b)
            ell_relation = endpoint_relation(first_ell, second_ell)
            cross_shared = bool(
                (endpoints(first_b) | endpoints(second_b))
                & (endpoints(first_ell) | endpoints(second_ell))
            )
            if b_relation == "parallel":
                assert shift in differences or (
                    -shift[0], -shift[1]
                ) in differences
            if ell_relation == "parallel":
                linear_shift = linear(shift)
                assert linear_shift in differences or (
                    -linear_shift[0], -linear_shift[1]
                ) in differences
            category = (
                {"parallel": "B", "cross": "b", "none": "-"}[b_relation]
                + {"parallel": "L", "cross": "l", "none": "-"}[
                    ell_relation
                ]
                + ("X" if cross_shared else "-")
            )
            endpoint_types[category] += multiplicity
            if category == "---":
                matching_adjacency[first][second] += multiplicity
                matching_adjacency[second][first] += multiplicity
                matching_records[first].extend(
                    (second, fibre) for fibre in occurrences[(first, second)]
                )
                matching_records[second].extend(
                    (first, fibre) for fibre in occurrences[(first, second)]
                )
            first_potentials = mixed_potentials(first)
            second_potentials = mixed_potentials(second)
            if first_potentials is None or second_potentials is None:
                potential_edge_types["zero"] += multiplicity
            else:
                same_alpha = first_potentials[0] == second_potentials[0]
                same_beta = first_potentials[1] == second_potentials[1]
                potential_shift_mass[
                    subtract(second_potentials[0], first_potentials[0])
                ] += multiplicity
                potential_edge_types[
                    ("A" if same_alpha else "-")
                    + ("B" if same_beta else "-")
                ] += multiplicity

    if points is not None:
        for cell in core:
            potentials = mixed_potentials(cell)
            if potentials is None:
                continue
            invariant = cell_invariant(cell)
            potential_fibres["A", invariant, potentials[0]] += 1
            potential_fibres["B", invariant, potentials[1]] += 1

    top_cells = []
    for cell, records in cell_records.items():
        distinct = tuple(len({record[index] for record in records}) for index in range(5))
        maxima = tuple(
            max(Counter(record[index] for record in records).values())
            for index in range(5)
        )
        top_cells.append(
            (
                cell,
                loads[cell],
                len(records),
                distinct,
                maxima,
            )
        )
    top_cells.sort(key=lambda row: (row[1], row[2], row[0]), reverse=True)

    matching_wedges: Counter[str] = Counter()
    matching_wedge_fibres: Counter[str] = Counter()
    matching_degrees = {
        centre: sum(neighbours.values())
        for centre, neighbours in matching_adjacency.items()
    }
    matching_common_neighbours: Counter[tuple[Cell, Cell]] = Counter()
    matching_common_neighbour_lists: dict[
        tuple[Cell, Cell], list[Cell]
    ] = defaultdict(list)
    matching_pair_r_copies: Counter[tuple[Cell, Cell, Point]] = Counter()
    matching_pair_r_centres: Counter[tuple[Cell, Cell, Point]] = Counter()
    matching_zdr_copies: Counter[tuple[Point, Point, Point]] = Counter()
    matching_zdr_centres: Counter[tuple[Point, Point, Point]] = Counter()
    matching_opposite_r_support: Counter[tuple[Cell, Cell]] = Counter()
    matching_c4_r_overlap: Counter[tuple[int, int]] = Counter()
    matching_c4_contact_r_routes: Counter[tuple[int, bool, bool]] = Counter()
    matching_c4_missing_r_routes: Counter[bool] = Counter()
    matching_component_vertices: dict[Point, set[Cell]] = defaultdict(set)
    matching_component_edges: Counter[Point] = Counter()
    for centre, neighbours in matching_adjacency.items():
        component = cell_invariant(centre)
        matching_component_vertices[component].add(centre)
        matching_component_vertices[component].update(neighbours)
        matching_component_edges[component] += len(neighbours)
    # Every underlying simple edge was seen once from each endpoint.
    assert all(value % 2 == 0 for value in matching_component_edges.values())
    matching_translate_profiles = []
    matching_component_endpoint_pencils: dict[Point, int] = {}
    matching_component_weighted_endpoint_pencils: dict[Point, int] = {}
    matching_component_contact_wedges: Counter[Point] = Counter()
    matching_component_pencil_wedge_upper: Counter[Point] = Counter()
    matching_weighted_endpoint_pencil_rows: list[
        tuple[int, int, int, Point, Cell, Point]
    ] = []
    matching_contact_pencil_rows: list[
        tuple[Fraction, int, int, int, Point, Cell, Point]
    ] = []
    matching_endpoint_pencil_copy_rows: list[
        tuple[int, int, int, int, int, int, int, int, int, Point, Cell, Point]
    ] = []
    matching_endpoint_key_pair_mass = 0
    matching_endpoint_key_support = 0
    matching_endpoint_key_collisions = 0
    matching_endpoint_switch_lambda = 0
    matching_endpoint_switch_pencil = 0
    matching_endpoint_switch_theta = Fraction(0)
    matching_endpoint_switch_residual = 0
    matching_endpoint_switch_residual_product = 0
    matching_endpoint_switch_class_pencil: Counter[str] = Counter()
    matching_endpoint_switch_class_lambda: Counter[str] = Counter()
    matching_endpoint_switch_class_residual: Counter[str] = Counter()
    matching_endpoint_switch_class_residual_product: Counter[str] = Counter()
    matching_endpoint_metric_product_mass: Counter[int] = Counter()
    matching_endpoint_metric_product_reciprocal = Fraction(0)
    matching_endpoint_metric_product_minimum: int | None = None
    matching_endpoint_metric_resonance_mass: Counter[str] = Counter()
    matching_endpoint_reverse_cross_support_ratio = Fraction(0)
    matching_endpoint_reverse_cross_support_row: tuple[object, ...] = ()
    matching_resonant_footprint_incidences = 0
    matching_resonant_diagonal_footprint_incidences = 0
    matching_resonant_footprint_owners: dict[
        tuple[object, ...], tuple[object, ...]
    ] = {}
    matching_resonant_footprint_depth: Counter[tuple[object, ...]] = Counter()
    matching_resonant_footprint_edge_reuse: Counter[
        tuple[object, ...]
    ] = Counter()
    matching_resonant_footprint_corner_degree: Counter[
        tuple[object, ...]
    ] = Counter()
    matching_resonant_footprint_difference_degree: Counter[
        tuple[object, ...]
    ] = Counter()
    for component, vertices in sorted(
        matching_component_vertices.items(),
        key=lambda item: (len(item[1]), item[0]),
        reverse=True,
    )[:8]:
        cover = Counter(
            (
                vertex[0][0] + difference[0],
                vertex[0][1] + difference[1],
            )
            for vertex in vertices
            for difference in differences
        )
        matching_translate_profiles.append(
            (
                component,
                len(vertices),
                len(cover),
                len(vertices) * len(differences) / len(cover),
                max(cover.values(), default=0),
            )
        )
    if points is not None:
        for component, vertices in matching_component_vertices.items():
            endpoint_load = Counter(
                endpoint
                for vertex in vertices
                for value in vertex
                for endpoint in endpoints(value)
            )
            matching_component_endpoint_pencils[component] = max(
                endpoint_load.values(), default=0
            )
        for centre, neighbours in matching_adjacency.items():
            component = cell_invariant(centre)
            weighted_pencil = Counter()
            endpoint_neighbour_weights: dict[Point, list[int]] = defaultdict(
                list
            )
            rows = list(neighbours.items())
            for neighbour, multiplicity in rows:
                for endpoint in endpoints(neighbour[0]) | endpoints(
                    neighbour[1]
                ):
                    weighted_pencil[endpoint] += multiplicity
                    endpoint_neighbour_weights[endpoint].append(multiplicity)
            matching_component_weighted_endpoint_pencils[component] = max(
                matching_component_weighted_endpoint_pencils.get(component, 0),
                max(weighted_pencil.values(), default=0),
            )
            for endpoint, weights in endpoint_neighbour_weights.items():
                load = sum(weights)
                pair_mass = (
                    load * load - sum(weight * weight for weight in weights)
                ) // 2
                matching_weighted_endpoint_pencil_rows.append(
                    (
                        load,
                        len(weights),
                        max(weights),
                        component,
                        centre,
                        endpoint,
                    )
                )
                matching_contact_pencil_rows.append(
                    (
                        Fraction(pair_mass, load),
                        pair_mass,
                        load,
                        len(weights),
                        component,
                        centre,
                        endpoint,
                    )
                )
                copies = []
                for neighbour, fibre in matching_records[centre]:
                    if endpoint not in (
                        endpoints(neighbour[0]) | endpoints(neighbour[1])
                    ):
                        continue
                    base, _ = fibre
                    q_value = subtract(centre[0], base)
                    p_value = subtract(neighbour[0], base)
                    first_pair = endpoint_map.get(neighbour[0])
                    second_pair = endpoint_map.get(neighbour[1])
                    endpoint_roles = (
                        first_pair[0] if first_pair else None,
                        first_pair[1] if first_pair else None,
                        second_pair[0] if second_pair else None,
                        second_pair[1] if second_pair else None,
                    )
                    assert endpoint_roles.count(endpoint) == 1
                    role = endpoint_roles.index(endpoint)
                    other_endpoints = (
                        first_pair[1] if first_pair else None,
                        first_pair[0] if first_pair else None,
                        second_pair[1] if second_pair else None,
                        second_pair[0] if second_pair else None,
                    )
                    other_endpoint = other_endpoints[role]
                    assert other_endpoint is not None
                    copies.append(
                        (
                            neighbour,
                            base,
                            p_value,
                            q_value,
                            role,
                            other_endpoint,
                        )
                    )
                assert len(copies) == load
                q_loads = Counter(row[3] for row in copies)
                p_loads = Counter(row[2] for row in copies)
                key_loads = Counter()
                for first, second in combinations(copies, 2):
                    if first[0] == second[0]:
                        continue
                    # Canonicalize the unordered copy pair before taking
                    # its two-coordinate parameter difference.
                    if (first[0], first[1]) > (second[0], second[1]):
                        first, second = second, first
                    first_t = subtract(first[2], first[3])
                    second_t = subtract(second[2], second[3])
                    key_loads[
                        first[4],
                        second[4],
                        subtract(second[5], first[5]),
                        subtract(first_t, second_t),
                        rotate(subtract(first[2], second[2])),
                    ] += 1
                assert sum(key_loads.values()) == pair_mass
                matching_endpoint_key_pair_mass += pair_mass
                matching_endpoint_key_support += len(key_loads)
                matching_endpoint_key_collisions += sum(
                    value * (value - 1) // 2
                    for value in key_loads.values()
                )

                q_fibres: dict[Cell, set[Point]] = defaultdict(set)
                for copy in copies:
                    assert copy[3] not in q_fibres[copy[0]]
                    q_fibres[copy[0]].add(copy[3])
                fibre_internal_differences: dict[Cell, Counter[Point]] = {}
                active_switches: set[Point] = set()
                for neighbour, q_values in q_fibres.items():
                    internal = Counter(
                        subtract(first, second)
                        for first in q_values
                        for second in q_values
                        if first != second
                    )
                    fibre_internal_differences[neighbour] = internal
                    active_switches.update(internal)
                for switch in active_switches:
                    switch_weights = [
                        internal[switch]
                        for internal in fibre_internal_differences.values()
                        if internal[switch]
                    ]
                    switch_load = sum(switch_weights)
                    switch_pair = (
                        switch_load * switch_load
                        - sum(weight * weight for weight in switch_weights)
                    ) // 2
                    matching_endpoint_switch_lambda += switch_load
                    matching_endpoint_switch_pencil += switch_pair
                    matching_endpoint_switch_theta = max(
                        matching_endpoint_switch_theta,
                        Fraction(switch_pair, switch_load),
                    )
                    matching_endpoint_switch_residual = max(
                        matching_endpoint_switch_residual,
                        switch_load - max(switch_weights),
                    )
                    switch_residual = switch_load - max(switch_weights)
                    matching_endpoint_switch_residual_product += (
                        switch_residual * switch_load
                    )

                    active_neighbours = [
                        (neighbour, internal[switch])
                        for neighbour, internal in fibre_internal_differences.items()
                        if internal[switch]
                    ]
                    metric_edge_mass = 0
                    for (
                        (first_neighbour, first_weight),
                        (second_neighbour, second_weight),
                    ) in combinations(active_neighbours, 2):
                        first_t = subtract(first_neighbour[0], centre[0])
                        second_t = subtract(second_neighbour[0], centre[0])
                        physical_difference = subtract(first_t, second_t)
                        metric_product = (
                            (switch[0] * switch[0] + switch[1] * switch[1])
                            * (
                                physical_difference[0] * physical_difference[0]
                                + physical_difference[1] * physical_difference[1]
                            )
                        )
                        assert metric_product > 0
                        weight = first_weight * second_weight
                        metric_edge_mass += weight
                        matching_endpoint_metric_product_mass[
                            metric_product.bit_length() - 1
                        ] += weight
                        matching_endpoint_metric_product_reciprocal += Fraction(
                            weight, metric_product
                        )
                        if matching_endpoint_metric_product_minimum is None:
                            matching_endpoint_metric_product_minimum = metric_product
                        else:
                            matching_endpoint_metric_product_minimum = min(
                                matching_endpoint_metric_product_minimum,
                                metric_product,
                            )
                    assert metric_edge_mass == switch_pair

                    # Resolve each internal representation so that the
                    # three exact global-Jacobian resonances retain s.
                    resonance_edge_mass = 0
                    for (
                        (first_neighbour, _),
                        (second_neighbour, _),
                    ) in combinations(active_neighbours, 2):
                        first_t = subtract(first_neighbour[0], centre[0])
                        second_t = subtract(second_neighbour[0], centre[0])
                        physical_difference = subtract(first_t, second_t)
                        first_starts = [
                            q_value
                            for q_value in q_fibres[first_neighbour]
                            if subtract(q_value, switch)
                            in q_fibres[first_neighbour]
                        ]
                        second_starts = [
                            q_value
                            for q_value in q_fibres[second_neighbour]
                            if subtract(q_value, switch)
                            in q_fibres[second_neighbour]
                        ]
                        for first_q in first_starts:
                            for second_q in second_starts:
                                key_shift = subtract(first_q, second_q)
                                gamma = subtract(
                                    (
                                        -rotate(key_shift)[0],
                                        -rotate(key_shift)[1],
                                    ),
                                    linear(physical_difference),
                                )
                                mask = "".join(
                                    name
                                    for name, active in (
                                        (
                                            "q",
                                            key_shift[0] * switch[1]
                                            - key_shift[1] * switch[0]
                                            == 0,
                                        ),
                                        (
                                            "p",
                                            (
                                                key_shift[0]
                                                + physical_difference[0]
                                            )
                                            * switch[1]
                                            - (
                                                key_shift[1]
                                                + physical_difference[1]
                                            )
                                            * switch[0]
                                            == 0,
                                        ),
                                        (
                                            "D",
                                            gamma[0] * switch[0]
                                            + gamma[1] * switch[1]
                                            == 0,
                                        ),
                                    )
                                    if active
                                )
                                matching_endpoint_metric_resonance_mass[
                                    mask or "nonresonant"
                                ] += 1
                                resonance_edge_mass += 1
                    assert resonance_edge_mass == switch_pair

                    # Reconstruct the literal reverse records, discard one
                    # largest t-fibre exactly as in G_2, and measure the
                    # cross-support Y+Z inside each physical endpoint role.
                    # This is diagnostic evidence for the matching-heavy
                    # branch; no support inequality is assumed here.
                    largest_neighbour = min(
                        (
                            neighbour
                            for neighbour in q_fibres
                            if fibre_internal_differences[neighbour][switch]
                            == max(switch_weights)
                        ),
                        default=None,
                    )
                    reverse_by_role: dict[
                        int, list[tuple[Point, Point, Point, Point]]
                    ] = defaultdict(list)
                    h_value = add(centre[1], rotate(centre[0]))
                    for neighbour, q_values in q_fibres.items():
                        if neighbour == largest_neighbour:
                            continue
                        first_pair = endpoint_map.get(neighbour[0])
                        second_pair = endpoint_map.get(neighbour[1])
                        endpoint_roles = (
                            first_pair[0] if first_pair else None,
                            first_pair[1] if first_pair else None,
                            second_pair[0] if second_pair else None,
                            second_pair[1] if second_pair else None,
                        )
                        assert endpoint_roles.count(endpoint) == 1
                        role = endpoint_roles.index(endpoint)
                        displacement = subtract(neighbour[0], centre[0])
                        for q_value in q_values:
                            if subtract(q_value, switch) not in q_values:
                                continue
                            x_value = subtract(centre[0], q_value)
                            y_value = add(
                                h_value,
                                add(
                                    rotate((-x_value[0], -x_value[1])),
                                    rotate(displacement),
                                ),
                            )
                            z_value = add(
                                h_value,
                                add(
                                    rotate((-x_value[0], -x_value[1])),
                                    linear(displacement),
                                ),
                            )
                            assert y_value in differences
                            assert z_value in differences
                            reverse_by_role[role].append(
                                (x_value, displacement, y_value, z_value)
                            )
                    assert sum(map(len, reverse_by_role.values())) == switch_residual
                    for role, reverse_rows in reverse_by_role.items():
                        row_count = len(reverse_rows)
                        if row_count < 2:
                            continue
                        y_values = {row[2] for row in reverse_rows}
                        z_values = {row[3] for row in reverse_rows}
                        cross_support = {
                            add(y_value, z_value)
                            for y_value in y_values
                            for z_value in z_values
                        }
                        ratio = Fraction(row_count * row_count, len(cross_support))
                        if ratio > matching_endpoint_reverse_cross_support_ratio:
                            matching_endpoint_reverse_cross_support_ratio = ratio
                            matching_endpoint_reverse_cross_support_row = (
                                row_count,
                                len(y_values),
                                len(z_values),
                                len(cross_support),
                                max(Counter(row[0] for row in reverse_rows).values()),
                                max(Counter(row[1] for row in reverse_rows).values()),
                                role,
                                component,
                                centre,
                                endpoint,
                                switch,
                                tuple(sorted(reverse_rows)),
                            )

                        # Every resonant quadratic footprint becomes
                        # injective after retaining its physical difference
                        # and natural completion corner.  Profile both the
                        # undecorated depth and the two degree projections.
                        # A row is (X,t,Y,Z), while q=c-X, p=q+t and
                        # W=ell+Lt.
                        c_value, ell_value = centre
                        branch_groups: dict[
                            str, dict[Point, list[tuple[Point, Point, Point, Point]]]
                        ] = {
                            "q": defaultdict(list),
                            "p": defaultdict(list),
                            "D": defaultdict(list),
                        }
                        for row in reverse_rows:
                            x_start, displacement, _, z_start = row
                            q_value = subtract(c_value, x_start)
                            p_value = add(q_value, displacement)
                            branch_groups["q"][q_value].append(row)
                            branch_groups["p"][p_value].append(row)
                            branch_groups["D"][z_start].append(row)

                        for branch, groups in branch_groups.items():
                            for coordinate, star_rows in groups.items():
                                assert len({row[1] for row in star_rows}) == len(
                                    star_rows
                                )
                                representations: dict[
                                    Point,
                                    tuple[
                                        tuple[Point, Point, Point, Point],
                                        tuple[Point, Point, Point, Point],
                                    ],
                                ] = {}
                                for first_row in star_rows:
                                    for second_row in star_rows:
                                        if branch == "q":
                                            footprint_value = add(
                                                first_row[2], second_row[3]
                                            )
                                        elif branch == "p":
                                            footprint_value = add(
                                                first_row[0], second_row[3]
                                            )
                                        else:
                                            footprint_value = add(
                                                first_row[0], second_row[2]
                                            )
                                        candidate = first_row, second_row
                                        previous = representations.get(
                                            footprint_value
                                        )
                                        candidate_is_diagonal = (
                                            first_row[1] == second_row[1]
                                        )
                                        previous_is_diagonal = (
                                            previous is not None
                                            and previous[0][1] == previous[1][1]
                                        )
                                        if previous is None or (
                                            candidate_is_diagonal,
                                            candidate,
                                        ) < (
                                            previous_is_diagonal,
                                            previous,
                                        ):
                                            representations[footprint_value] = candidate

                                star_identity = (
                                    centre,
                                    endpoint,
                                    switch,
                                    role,
                                    branch,
                                    coordinate,
                                )
                                for footprint_value, (
                                    first_row,
                                    second_row,
                                ) in representations.items():
                                    x_start, first_t, _, _ = first_row
                                    difference = subtract(first_t, second_row[1])
                                    if difference == (0, 0):
                                        matching_resonant_diagonal_footprint_incidences += 1
                                        continue
                                    q_value = subtract(c_value, x_start)
                                    p_value = add(q_value, first_t)
                                    if branch in ("q", "p"):
                                        corner = p_value, x_start, ell_value
                                    else:
                                        w_value = add(ell_value, linear(first_t))
                                        corner = q_value, x_start, w_value
                                    decorated_key = (
                                        switch,
                                        role,
                                        branch,
                                        footprint_value,
                                        difference,
                                        corner,
                                    )
                                    previous_owner = (
                                        matching_resonant_footprint_owners.setdefault(
                                            decorated_key, star_identity
                                        )
                                    )
                                    assert previous_owner == star_identity
                                    matching_resonant_footprint_incidences += 1
                                    prefix = switch, role, branch, footprint_value
                                    matching_resonant_footprint_depth[prefix] += 1
                                    matching_resonant_footprint_edge_reuse[
                                        switch, role, branch, difference, corner
                                    ] += 1
                                    matching_resonant_footprint_corner_degree[
                                        prefix + (corner,)
                                    ] += 1
                                    matching_resonant_footprint_difference_degree[
                                        prefix + (difference,)
                                    ] += 1
                    switch_class = (
                        "popular" if switch in adaptive_popular else "nonpopular"
                    )
                    matching_endpoint_switch_class_pencil[
                        switch_class
                    ] += switch_pair
                    matching_endpoint_switch_class_lambda[
                        switch_class
                    ] += switch_load
                    matching_endpoint_switch_class_residual[
                        switch_class
                    ] = max(
                        matching_endpoint_switch_class_residual[switch_class],
                        switch_residual,
                    )
                    matching_endpoint_switch_class_residual_product[
                        switch_class
                    ] += switch_residual * switch_load
                matching_endpoint_pencil_copy_rows.append(
                    (
                        load,
                        len(weights),
                        max(weights),
                        len(q_loads),
                        max(q_loads.values(), default=0),
                        len(p_loads),
                        max(p_loads.values(), default=0),
                        len(key_loads),
                        max(key_loads.values(), default=0),
                        component,
                        centre,
                        endpoint,
                    )
                )
            matching_component_pencil_wedge_upper[component] += sum(
                (
                    sum(weights) ** 2
                    - sum(weight * weight for weight in weights)
                )
                // 2
                for weights in endpoint_neighbour_weights.values()
            )
            matching_component_contact_wedges[component] += sum(
                first_weight * second_weight
                for (
                    (first, first_weight),
                    (second, second_weight),
                ) in combinations(rows, 2)
                if (
                    (endpoints(first[0]) | endpoints(first[1]))
                    & (endpoints(second[0]) | endpoints(second[1]))
                )
            )
        assert (
            matching_endpoint_key_pair_mass**2
            <= matching_endpoint_key_support
            * (
                matching_endpoint_key_pair_mass
                + 2 * matching_endpoint_key_collisions
            )
        )
        assert (
            matching_endpoint_switch_pencil
            == 2 * matching_endpoint_key_collisions
        )
        assert (
            sum(matching_endpoint_metric_product_mass.values())
            == matching_endpoint_switch_pencil
        )
        assert all(
            matching_component_contact_wedges[component]
            <= matching_component_pencil_wedge_upper[component]
            for component in matching_component_vertices
        )
    if points is not None:
        for centre, neighbours in matching_adjacency.items():
            rows = list(neighbours.items())
            simple_neighbours = sorted(neighbours)
            for index, first in enumerate(simple_neighbours):
                for second in simple_neighbours[index + 1 :]:
                    matching_common_neighbours[first, second] += 1
                    matching_common_neighbour_lists[first, second].append(centre)
            for index, (first, first_weight) in enumerate(rows):
                matching_wedges["parallel"] += first_weight * (first_weight - 1) // 2
                first_potentials = mixed_potentials(first)
                for second, second_weight in rows[index + 1 :]:
                    weight = first_weight * second_weight
                    second_potentials = mixed_potentials(second)
                    if first_potentials is None or second_potentials is None:
                        matching_wedges["missing-potential"] += weight
                        continue
                    if first_potentials[0] == second_potentials[0]:
                        assert first_potentials[1] == second_potentials[1]
                        matching_wedges["repeated-potential"] += weight
                        continue
                    first_endpoints = endpoints(first[0]) | endpoints(first[1])
                    second_endpoints = endpoints(second[0]) | endpoints(second[1])
                    if first_endpoints.isdisjoint(second_endpoints):
                        matching_wedges["diffuse-twelve-distinct"] += weight
                    else:
                        matching_wedges["diffuse-neighbour-contact"] += weight

        for records in matching_records.values():
            for index, (_, first_fibre) in enumerate(records):
                first_base, first_sum = first_fibre
                for _, second_fibre in records[index + 1 :]:
                    second_base, second_sum = second_fibre
                    matching_wedge_fibres[
                        ("S" if first_sum == second_sum else "-")
                        + ("A" if first_base == second_base else "-")
                    ] += 1
        assert sum(matching_wedge_fibres.values()) == sum(matching_wedges.values())

    matching_c4_endpoints: Counter[tuple[int, int]] = Counter()
    matching_c4_data: dict[
        tuple[Edge, Edge, Edge, Edge],
        tuple[int, int, list[tuple[int, int]]],
    ] = {}
    if points is not None:
        for (first, second), centres in matching_common_neighbour_lists.items():
            component = cell_invariant(first)
            assert component == cell_invariant(second)
            displacement = subtract(second[0], first[0])
            linear_displacement = linear(displacement)
            pair_support: set[Point] = set()
            centre_supports: dict[Cell, set[Point]] = {}
            for centre in centres:
                first_edge = tuple(sorted((first, centre)))
                second_edge = tuple(sorted((second, centre)))
                local_support: set[Point] = set()
                for first_base, first_sum in occurrences[first_edge]:
                    for second_base, second_sum in occurrences[second_edge]:
                        sum_difference = subtract(first_sum, second_sum)
                        local_support.add(sum_difference)
                        pair_support.add(sum_difference)

                        # The common-neighbour extension simultaneously
                        # realizes three coupled D-D differences.
                        assert subtract(first_sum, centre[0]) in differences
                        assert subtract(second_sum, centre[0]) in differences
                        assert subtract(first_sum, first[0]) in differences
                        assert subtract(second_sum, second[0]) in differences
                        assert subtract(first_base, second_base) == rotate(
                            add(sum_difference, linear_displacement)
                        )

                        pair_key = first, second, sum_difference
                        cell_key = component, displacement, sum_difference
                        matching_pair_r_copies[pair_key] += 1
                        matching_zdr_copies[cell_key] += 1
                for sum_difference in local_support:
                    pair_key = first, second, sum_difference
                    cell_key = component, displacement, sum_difference
                    matching_pair_r_centres[pair_key] += 1
                    matching_zdr_centres[cell_key] += 1
                centre_supports[centre] = local_support
            matching_opposite_r_support[first, second] = len(pair_support)

            for index, third in enumerate(centres):
                for fourth in centres[index + 1 :]:
                    cells = (first, second, third, fourth)
                    assert len(set(cells)) == 4
                    physical = set()
                    alphas = set()
                    complete_potentials = True
                    for cell in cells:
                        physical.update(endpoints(cell[0]))
                        physical.update(endpoints(cell[1]))
                        cell_potentials = mixed_potentials(cell)
                        if cell_potentials is None:
                            complete_potentials = False
                        else:
                            alphas.add(cell_potentials[0])
                    cycle_key = tuple(
                        sorted(
                            (
                                tuple(sorted((first, third))),
                                tuple(sorted((first, fourth))),
                                tuple(sorted((second, third))),
                                tuple(sorted((second, fourth))),
                            )
                        )
                    )
                    endpoint_row = (
                        len(physical),
                        len(alphas) if complete_potentials else -1,
                    )
                    shared_r = len(
                        centre_supports[third] & centre_supports[fourth]
                    )
                    diagonal_contact = len(
                        (endpoints(first[0]) | endpoints(first[1]))
                        & (endpoints(second[0]) | endpoints(second[1]))
                    )
                    if cycle_key not in matching_c4_data:
                        matching_c4_data[cycle_key] = (
                            endpoint_row[0],
                            endpoint_row[1],
                            [(diagonal_contact, shared_r)],
                        )
                    else:
                        old_physical, old_potentials, diagonal_rows = (
                            matching_c4_data[cycle_key]
                        )
                        assert (old_physical, old_potentials) == endpoint_row
                        diagonal_rows.append((diagonal_contact, shared_r))

        for physical_count, potential_count, diagonal_rows in (
            matching_c4_data.values()
        ):
            # A simple four-cycle is encountered from each of its two
            # diagonals.  Keep the maximum common-r overlap, so the zero row
            # means neither diagonal admits a repeated-r realization.
            assert len(diagonal_rows) == 2
            if potential_count != -1:
                assert (
                    sum(row[0] for row in diagonal_rows)
                    == 16 - physical_count
                )
            overlaps = [row[1] for row in diagonal_rows]
            matching_c4_endpoints[physical_count, potential_count] += 1
            matching_c4_r_overlap[physical_count, max(overlaps)] += 1
            if potential_count == -1:
                matching_c4_missing_r_routes[bool(max(overlaps))] += 1
                continue
            contact_rows = [row for row in diagonal_rows if row[0]]
            clean_rows = [row for row in diagonal_rows if not row[0]]
            matching_c4_contact_r_routes[
                len(contact_rows),
                any(shared_r for _, shared_r in contact_rows),
                any(shared_r for _, shared_r in clean_rows),
            ] += 1

    assert matching_endpoint_switch_lambda <= 8 * matching_wedges["parallel"]
    summary = {
        "components": tuple(component_mass.most_common(8)),
        "shifts": tuple(shift_mass.most_common(8)),
        "fibres": tuple(fibre_mass.most_common(8)),
        "loads": tuple(Counter(loads.values()).most_common()),
        "endpoint_types": tuple(endpoint_types.most_common()),
        "potential_edges": tuple(potential_edge_types.most_common()),
        "potential_shifts": tuple(potential_shift_mass.most_common(8)),
        "potential_fibres": tuple(potential_fibres.most_common(8)),
        "matching_wedges": tuple(matching_wedges.most_common()),
        "matching_wedge_fibres": tuple(matching_wedge_fibres.most_common()),
        "matching_degree_profile": (
            ("vertices", len(matching_degrees)),
            ("edge_copies", sum(matching_degrees.values()) // 2),
            ("maximum", max(matching_degrees.values(), default=0)),
            ("second_moment", sum(value * value for value in matching_degrees.values())),
        ),
        "matching_c4_profile": (
            ("opposite_pairs", len(matching_common_neighbours)),
            (
                "maximum_codegree",
                max(matching_common_neighbours.values(), default=0),
            ),
            (
                "four_cycles",
                sum(
                    value * (value - 1) // 2
                    for value in matching_common_neighbours.values()
                )
                // 2,
            ),
            (
                "contact_pair_maximum_codegree",
                max(
                    (
                        value
                        for (first, second), value in (
                            matching_common_neighbours.items()
                        )
                        if (
                            (endpoints(first[0]) | endpoints(first[1]))
                            & (endpoints(second[0]) | endpoints(second[1]))
                        )
                    ),
                    default=0,
                ),
            ),
            (
                "clean_pair_maximum_codegree",
                max(
                    (
                        value
                        for (first, second), value in (
                            matching_common_neighbours.items()
                        )
                        if not (
                            (endpoints(first[0]) | endpoints(first[1]))
                            & (endpoints(second[0]) | endpoints(second[1]))
                        )
                    ),
                    default=0,
                ),
            ),
            (
                "contact_pair_two_paths",
                sum(
                    value
                    for (first, second), value in (
                        matching_common_neighbours.items()
                    )
                    if (
                        (endpoints(first[0]) | endpoints(first[1]))
                        & (endpoints(second[0]) | endpoints(second[1]))
                    )
                ),
            ),
            (
                "clean_pair_two_paths",
                sum(
                    value
                    for (first, second), value in (
                        matching_common_neighbours.items()
                    )
                    if not (
                        (endpoints(first[0]) | endpoints(first[1]))
                        & (endpoints(second[0]) | endpoints(second[1]))
                    )
                ),
            ),
        ),
        "matching_common_extension_profile": (
            (
                "copy_pairs",
                sum(matching_pair_r_copies.values()),
            ),
            (
                "fixed_opposite_r_copy_load",
                max(matching_pair_r_copies.values(), default=0),
            ),
            (
                "fixed_opposite_r_centre_load",
                max(matching_pair_r_centres.values(), default=0),
            ),
            (
                "fixed_zdr_copy_load",
                max(matching_zdr_copies.values(), default=0),
            ),
            (
                "fixed_zdr_centre_load",
                max(matching_zdr_centres.values(), default=0),
            ),
            (
                "maximum_opposite_r_support",
                max(matching_opposite_r_support.values(), default=0),
            ),
            (
                "contact_opposite_r_centre_load",
                max(
                    (
                        value
                        for (first, second, _), value in (
                            matching_pair_r_centres.items()
                        )
                        if (
                            (endpoints(first[0]) | endpoints(first[1]))
                            & (endpoints(second[0]) | endpoints(second[1]))
                        )
                    ),
                    default=0,
                ),
            ),
            (
                "clean_opposite_r_centre_load",
                max(
                    (
                        value
                        for (first, second, _), value in (
                            matching_pair_r_centres.items()
                        )
                        if not (
                            (endpoints(first[0]) | endpoints(first[1]))
                            & (endpoints(second[0]) | endpoints(second[1]))
                        )
                    ),
                    default=0,
                ),
            ),
        ),
        "matching_c4_endpoints": tuple(
            matching_c4_endpoints.most_common()
        ),
        "matching_c4_r_overlap": tuple(
            matching_c4_r_overlap.most_common()
        ),
        "matching_c4_contact_r_routes": tuple(
            matching_c4_contact_r_routes.most_common()
        ),
        "matching_c4_missing_r_routes": tuple(
            matching_c4_missing_r_routes.most_common()
        ),
        "matching_component_profile": (
            ("components", len(matching_component_vertices)),
            (
                "maximum_vertices",
                max(map(len, matching_component_vertices.values()), default=0),
            ),
            (
                "maximum_simple_edges",
                max(
                    (value // 2 for value in matching_component_edges.values()),
                    default=0,
                ),
            ),
            (
                "maximum_endpoint_pencil",
                max(matching_component_endpoint_pencils.values(), default=0),
            ),
            (
                "maximum_endpoint_pencil_vertex_product",
                max(
                    (
                        matching_component_endpoint_pencils[component]
                        * len(vertices)
                        for component, vertices in (
                            matching_component_vertices.items()
                        )
                    ),
                    default=0,
                ),
            ),
        ),
        "matching_weighted_endpoint_pencil_profile": (
            (
                "maximum_weighted_endpoint_pencil",
                max(
                    matching_component_weighted_endpoint_pencils.values(),
                    default=0,
                ),
            ),
            (
                "endpoint_contact_weighted_wedges",
                sum(matching_component_contact_wedges.values()),
            ),
            (
                "endpoint_pencil_wedge_upper",
                sum(matching_component_pencil_wedge_upper.values()),
            ),
            (
                "maximum_contact_pencil_ratio",
                (
                    max(
                        (row[0] for row in matching_contact_pencil_rows),
                        default=Fraction(0),
                    ).numerator,
                    max(
                        (row[0] for row in matching_contact_pencil_rows),
                        default=Fraction(0),
                    ).denominator,
                ),
            ),
        ),
        "matching_weighted_endpoint_pencils": tuple(
            (row, 1)
            for row in sorted(
                matching_weighted_endpoint_pencil_rows, reverse=True
            )[:8]
        ),
        "matching_contact_pencils": tuple(
            (
                (
                    row[0].numerator,
                    row[0].denominator,
                    *row[1:],
                ),
                1,
            )
            for row in sorted(
                matching_contact_pencil_rows, reverse=True
            )[:8]
        ),
        "matching_endpoint_pencil_copy_profiles": tuple(
            (row, 1)
            for row in sorted(
                matching_endpoint_pencil_copy_rows, reverse=True
            )[:8]
        ),
        "matching_endpoint_key_dichotomy": (
            ("pair_mass", matching_endpoint_key_pair_mass),
            ("support", matching_endpoint_key_support),
            ("collisions", matching_endpoint_key_collisions),
        ),
        "matching_endpoint_collision_switch": (
            ("switch_pencil", matching_endpoint_switch_pencil),
            ("switch_lambda", matching_endpoint_switch_lambda),
            (
                "maximum_switch_ratio",
                (
                    matching_endpoint_switch_theta.numerator,
                    matching_endpoint_switch_theta.denominator,
                ),
            ),
            ("maximum_switch_residual", matching_endpoint_switch_residual),
            (
                "switch_residual_product",
                matching_endpoint_switch_residual_product,
            ),
            ("parallel_wedges", matching_wedges["parallel"]),
        ),
        "matching_endpoint_collision_switch_cutoff": tuple(
            (
                switch_class,
                matching_endpoint_switch_class_pencil[switch_class],
                matching_endpoint_switch_class_lambda[switch_class],
                matching_endpoint_switch_class_residual[switch_class],
                matching_endpoint_switch_class_residual_product[
                    switch_class
                ],
            )
            for switch_class in ("nonpopular", "popular")
        ),
        "matching_endpoint_metric_product": (
            ("minimum", matching_endpoint_metric_product_minimum or 0),
            (
                "reciprocal_mass",
                matching_endpoint_metric_product_reciprocal,
            ),
            ("dyadic_mass", tuple(sorted(matching_endpoint_metric_product_mass.items()))),
            (
                "resonance_mass",
                tuple(sorted(matching_endpoint_metric_resonance_mass.items())),
            ),
        ),
        "matching_endpoint_reverse_cross_support": (
            (
                "maximum_record_square_to_cross_support",
                (
                    matching_endpoint_reverse_cross_support_ratio.numerator,
                    matching_endpoint_reverse_cross_support_ratio.denominator,
                ),
            ),
            ("maximizing_row", matching_endpoint_reverse_cross_support_row),
        ),
        "matching_resonant_decorated_footprint": (
            ("incidences", matching_resonant_footprint_incidences),
            (
                "diagonal_only_incidences",
                matching_resonant_diagonal_footprint_incidences,
            ),
            (
                "maximum_undecorated_depth",
                max(matching_resonant_footprint_depth.values(), default=0),
            ),
            (
                "maximum_decorated_load",
                int(bool(matching_resonant_footprint_owners)),
            ),
            (
                "maximum_completion_edge_reuse",
                max(
                    matching_resonant_footprint_edge_reuse.values(), default=0
                ),
            ),
            (
                "maximum_corner_degree_at_fixed_footprint",
                max(
                    matching_resonant_footprint_corner_degree.values(), default=0
                ),
            ),
            (
                "maximum_difference_degree_at_fixed_footprint",
                max(
                    matching_resonant_footprint_difference_degree.values(), default=0
                ),
            ),
            (
                "top_undecorated_depths",
                tuple(
                    sorted(
                        matching_resonant_footprint_depth.items(),
                        key=lambda item: (item[1], item[0]),
                        reverse=True,
                    )[:5]
                ),
            ),
            (
                "top_difference_degrees",
                tuple(
                    sorted(
                        matching_resonant_footprint_difference_degree.items(),
                        key=lambda item: (item[1], item[0]),
                        reverse=True,
                    )[:5]
                ),
            ),
            (
                "top_corner_degrees",
                tuple(
                    sorted(
                        matching_resonant_footprint_corner_degree.items(),
                        key=lambda item: (item[1], item[0]),
                        reverse=True,
                    )[:5]
                ),
            ),
        ),
        "matching_translate_profiles": tuple(
            (row, 1) for row in matching_translate_profiles
        ),
        "top_cells": tuple((row, 1) for row in top_cells[:8]),
    }
    core_profile = CoreProfile(
        vertices=len(loads),
        edge_copies=edge_copies,
        optimum_energy=energy,
        nested_mass=nested_mass,
        balance_mass=balance_mass,
        maximum_load=maximum_load,
        dyadic_level=dyadic_level,
        core_vertices=len(core),
        core_edge_copies=core_edge_copies,
        core_distinct_edges=len(core_edges),
        core_components=len(component_mass),
        maximum_component_edge_copies=max(component_mass.values(), default=0),
        maximum_parallel_multiplicity=max(core_edges.values(), default=0),
        distinct_shifts=len(shift_mass),
        maximum_shift_multiplicity=max(shift_mass.values(), default=0),
        distinct_fibres=len(fibre_mass),
        maximum_fibre_multiplicity=max(fibre_mass.values(), default=0),
    )
    return core_profile, summary, reversals


def transformed_costas(prime: int) -> tuple[list[Point], set[Point]]:
    matrix, _ = ROWS[prime]
    points = [apply(matrix, point) for point in welch(prime)]
    assert is_distance_sidon(points)
    return points, difference_set(points)


def main() -> None:
    costas_11 = transformed_costas(11)
    costas_17 = transformed_costas(17)
    families: list[tuple[str, set[Point], list[Point] | None]] = [
        ("closure-30", difference_set(POINTS[:30]), POINTS[:30]),
        ("Costas-11", costas_11[1], costas_11[0]),
        ("Costas-17", costas_17[1], costas_17[0]),
        ("radial-4", radial_set(4), None),
        ("radial-5", radial_set(5), None),
        ("radial-6", radial_set(6), None),
    ]
    if "--extended" in sys.argv:
        costas_23 = transformed_costas(23)
        families.extend(
            [
                ("closure-40", difference_set(POINTS[:40]), POINTS[:40]),
                ("Costas-23", costas_23[1], costas_23[0]),
                ("radial-8", radial_set(8), None),
            ]
        )
    if "--larger" in sys.argv:
        for prime in (29, 31, 37):
            points, differences = transformed_costas(prime)
            families.append((f"Costas-{prime}", differences, points))

    for name, differences, points in families:
        result, summary, reversals = profile(differences, points)
        print(name, result)
        print("  path-reversal units", reversals)
        for label, rows in summary.items():
            print(" ", label, rows)

    print("SWAP OPTIMAL NESTED-CORE ANALYZER: PASS")


if __name__ == "__main__":
    main()
