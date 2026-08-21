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
import heapq
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
    matching_endpoint_switch_role_pair_mass: Counter[tuple[int, int]] = Counter()
    matching_endpoint_switch_type_pair_mass: Counter[str] = Counter()
    matching_projected_key_pair_codegrees: Counter[
        tuple[tuple[object, ...], tuple[object, ...]]
    ] = Counter()
    matching_projected_key_pair_owner: dict[
        tuple[tuple[object, ...], tuple[object, ...]],
        tuple[Cell, Point, Point],
    ] = {}
    matching_projected_mixed_key_pair_groups: dict[
        tuple[tuple[object, ...], tuple[object, ...]],
        list[tuple[Cell, Point, Point]],
    ] = defaultdict(list)
    matching_projected_key_group_load: Counter[tuple[object, ...]] = Counter()
    matching_projected_full_same_pair_codegrees: dict[
        str,
        Counter[tuple[tuple[object, ...], tuple[object, ...]]],
    ] = {"V": Counter(), "W": Counter()}
    matching_projected_bundle_pair_codegrees: dict[
        str,
        Counter[tuple[tuple[object, ...], tuple[object, ...]]],
    ] = {"V": Counter(), "W": Counter()}
    matching_projected_group_count = 0
    matching_projected_mixed_group_incidence = 0
    matching_projected_same_centre_cross_second = 0
    matching_projected_same_centre_cross_third = 0
    matching_projected_same_centre_cross_maximum = 0
    matching_projected_same_centre_cross_load_histogram: Counter[int] = Counter()
    matching_projected_same_centre_mixed_second_pencil = 0
    matching_projected_same_centre_weighted_envelope = 0
    matching_projected_same_centre_cross_resonance: Counter[
        tuple[int, int, int]
    ] = Counter()
    matching_projected_same_centre_cross_rich_rows: list[tuple[object, ...]] = []
    matching_projected_same_centre_footprint_depth: Counter[Point] = Counter()
    matching_projected_same_centre_resonant_footprint_depth: Counter[
        Point
    ] = Counter()
    matching_projected_same_centre_transverse_footprint_depth: Counter[
        Point
    ] = Counter()
    matching_projected_same_centre_weighted_footprint_depth: Counter[
        Point
    ] = Counter()
    matching_projected_same_centre_resonant_weighted_footprint_depth: Counter[
        Point
    ] = Counter()
    matching_projected_same_centre_transverse_weighted_footprint_depth: Counter[
        Point
    ] = Counter()
    matching_projected_same_centre_physical_wedge_mass: Counter[
        tuple[object, ...]
    ] = Counter()
    matching_projected_same_centre_physical_wedge_cells: Counter[
        tuple[object, ...]
    ] = Counter()
    matching_projected_same_centre_physical_wedge_rows: dict[
        tuple[object, ...], list[tuple[object, ...]]
    ] = defaultdict(list)
    matching_projected_same_centre_physical_wedge_resonant_mass: Counter[
        tuple[object, ...]
    ] = Counter()
    matching_projected_same_centre_physical_wedge_transverse_mass: Counter[
        tuple[object, ...]
    ] = Counter()
    matching_projected_same_centre_physical_wedge_class_mass: Counter[
        str
    ] = Counter()
    matching_projected_same_centre_physical_wedge_triple_codegree: Counter[
        tuple[object, ...]
    ] = Counter()
    matching_projected_same_centre_physical_wedge_triple_owners: dict[
        tuple[object, ...], list[tuple[object, ...]]
    ] = defaultdict(list)

    def projected_physical_edge(key: tuple[object, ...]) -> Point:
        assert key[0] in ("V", "W")
        if key[0] == "V":
            return add(key[2], key[3])  # type: ignore[arg-type]
        return key[3]  # type: ignore[return-value]
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
                neighbour_roles: dict[Cell, int] = {}
                for copy in copies:
                    previous_role = neighbour_roles.setdefault(copy[0], copy[4])
                    assert previous_role == copy[4]
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

                v_neighbours = [
                    neighbour
                    for neighbour in q_fibres
                    if neighbour_roles[neighbour] < 2
                ]
                w_neighbours = [
                    neighbour
                    for neighbour in q_fibres
                    if neighbour_roles[neighbour] >= 2
                ]
                for v_neighbour in v_neighbours:
                    for w_neighbour in w_neighbours:
                        cross_load = Counter(
                            subtract(w_value, v_value)
                            for v_value in q_fibres[v_neighbour]
                            for w_value in q_fibres[w_neighbour]
                        )
                        matching_projected_same_centre_cross_second += sum(
                            load * (load - 1) // 2
                            for load in cross_load.values()
                        )
                        matching_projected_same_centre_cross_third += 3 * sum(
                            load * (load - 1) * (load - 2) // 6
                            for load in cross_load.values()
                        )
                        matching_projected_same_centre_cross_maximum = max(
                            matching_projected_same_centre_cross_maximum,
                            max(cross_load.values(), default=0),
                        )
                        matching_projected_same_centre_cross_load_histogram.update(
                            cross_load.values()
                        )
                        t_v = subtract(v_neighbour[0], centre[0])
                        t_w = subtract(w_neighbour[0], centre[0])
                        physical_delta = subtract(t_v, t_w)
                        for raw_difference, load in cross_load.items():
                            if load < 3:
                                continue
                            eta = (-raw_difference[0], -raw_difference[1])
                            shifts = (
                                eta,
                                rotate(add(eta, physical_delta)),
                                add(rotate(eta), linear(physical_delta)),
                            )
                            mass = load * (load - 1) * (load - 2) // 2
                            cell_pairs = tuple(
                                sorted(
                                    (
                                        v_value,
                                        add(v_value, raw_difference),
                                    )
                                    for v_value in q_fibres[v_neighbour]
                                    if add(v_value, raw_difference)
                                    in q_fibres[w_neighbour]
                                )
                            )
                            assert len(cell_pairs) == load
                            cell_values = {pair[0] for pair in cell_pairs}
                            c_value, ell_value = centre
                            footprint_offset = add(
                                add(c_value, ell_value), rotate(t_v)
                            )
                            footprint = {
                                add(
                                    footprint_offset,
                                    subtract(rotate(second), first),
                                )
                                for first in cell_values
                                for second in cell_values
                            }
                            footprint_counter = (
                                matching_projected_same_centre_resonant_footprint_depth
                                if any(shift == (0, 0) for shift in shifts)
                                else matching_projected_same_centre_transverse_footprint_depth
                            )
                            weighted_footprint_counter = (
                                matching_projected_same_centre_resonant_weighted_footprint_depth
                                if any(shift == (0, 0) for shift in shifts)
                                else matching_projected_same_centre_transverse_weighted_footprint_depth
                            )
                            footprint_weight = Fraction(mass, len(footprint))
                            physical_wedge = (
                                endpoint,
                                v_neighbour[0],
                                w_neighbour[1],
                                neighbour_roles[v_neighbour],
                                neighbour_roles[w_neighbour],
                            )
                            matching_projected_same_centre_physical_wedge_mass[
                                physical_wedge
                            ] += mass
                            matching_projected_same_centre_physical_wedge_cells[
                                physical_wedge
                            ] += 1
                            matching_projected_same_centre_physical_wedge_rows[
                                physical_wedge
                            ].append(
                                (
                                    mass,
                                    load,
                                    centre,
                                    t_v,
                                    t_w,
                                    eta,
                                    shifts,
                                )
                            )
                            physical_wedge_branch = (
                                matching_projected_same_centre_physical_wedge_resonant_mass
                                if any(shift == (0, 0) for shift in shifts)
                                else matching_projected_same_centre_physical_wedge_transverse_mass
                            )
                            physical_wedge_branch[physical_wedge] += mass
                            same_physical_edge = (
                                v_neighbour[0] == w_neighbour[1]
                                or v_neighbour[0]
                                == (
                                    -w_neighbour[1][0],
                                    -w_neighbour[1][1],
                                )
                            )
                            physical_wedge_class = (
                                "same_edge"
                                if same_physical_edge
                                else "one_endpoint"
                            )
                            matching_projected_same_centre_physical_wedge_class_mass[
                                physical_wedge_class
                            ] += mass
                            for triple in combinations(sorted(cell_values), 3):
                                wedge_triple = physical_wedge, triple
                                matching_projected_same_centre_physical_wedge_triple_codegree[
                                    wedge_triple
                                ] += 1
                                matching_projected_same_centre_physical_wedge_triple_owners[
                                    wedge_triple
                                ].append((centre, t_v, t_w, eta))
                            for footprint_value in footprint:
                                matching_projected_same_centre_footprint_depth[
                                    footprint_value
                                ] += 1
                                footprint_counter[footprint_value] += 1
                                matching_projected_same_centre_weighted_footprint_depth[
                                    footprint_value
                                ] += footprint_weight
                                weighted_footprint_counter[
                                    footprint_value
                                ] += footprint_weight
                            matching_projected_same_centre_cross_resonance[
                                sum(shift == (0, 0) for shift in shifts),
                                sum(shift in differences for shift in shifts),
                                sum(shift in adaptive_popular for shift in shifts),
                            ] += mass
                            matching_projected_same_centre_cross_rich_rows.append(
                                (
                                    load,
                                    mass,
                                    sum(shift == (0, 0) for shift in shifts),
                                    sum(shift in differences for shift in shifts),
                                    sum(shift in adaptive_popular for shift in shifts),
                                    centre,
                                    endpoint,
                                    t_v,
                                    t_w,
                                    eta,
                                    shifts,
                                    cell_pairs,
                                )
                            )
                for active_switch in active_switches:
                    lambda_v = sum(
                        fibre_internal_differences[neighbour][active_switch]
                        for neighbour in v_neighbours
                    )
                    lambda_w = sum(
                        fibre_internal_differences[neighbour][active_switch]
                        for neighbour in w_neighbours
                    )
                    weighted_v = sum(
                        max(0, len(q_fibres[neighbour]) - 2)
                        * fibre_internal_differences[neighbour][active_switch]
                        for neighbour in v_neighbours
                    )
                    weighted_w = sum(
                        max(0, len(q_fibres[neighbour]) - 2)
                        * fibre_internal_differences[neighbour][active_switch]
                        for neighbour in w_neighbours
                    )
                    matching_projected_same_centre_mixed_second_pencil += (
                        lambda_v * lambda_w
                    )
                    matching_projected_same_centre_weighted_envelope += min(
                        lambda_w * weighted_v,
                        lambda_v * weighted_w,
                    )
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
                    projected_keys: dict[Cell, tuple[tuple[object, ...], ...]] = {}
                    for neighbour, weight in active_neighbours:
                        role = neighbour_roles[neighbour]
                        displacement = subtract(neighbour[0], centre[0])
                        keys = []
                        for q_value in q_fibres[neighbour]:
                            if subtract(q_value, switch) not in q_fibres[neighbour]:
                                continue
                            if role < 2:
                                p_value = add(q_value, displacement)
                                key = (
                                    "V",
                                    role,
                                    subtract(p_value, switch),
                                    add(subtract(centre[0], q_value), switch),
                                )
                            else:
                                key = (
                                    "W",
                                    role,
                                    subtract(q_value, switch),
                                    neighbour[1],
                                )
                            keys.append(key)
                        assert len(keys) == weight
                        assert len(set(keys)) == weight
                        projected_keys[neighbour] = tuple(keys)

                    owner = centre, endpoint, switch
                    matching_projected_group_count += 1
                    owner_keys = {"V": set(), "W": set()}
                    owner_parts: dict[
                        str, dict[tuple[object, ...], Cell]
                    ] = {"V": {}, "W": {}}
                    for neighbour, keys in projected_keys.items():
                        for key in keys:
                            role_type = key[0]
                            assert role_type in owner_keys
                            assert key not in owner_keys[role_type]
                            owner_keys[role_type].add(key)
                            owner_parts[role_type][key] = neighbour
                    for role_type, part_map in owner_parts.items():
                        physical_parts: dict[Point, Cell] = {}
                        for key, neighbour in part_map.items():
                            physical_edge = projected_physical_edge(key)
                            previous_neighbour = physical_parts.setdefault(
                                physical_edge, neighbour
                            )
                            assert previous_neighbour == neighbour
                            if role_type == "V":
                                assert neighbour[0] == physical_edge
                            else:
                                assert neighbour[1] == physical_edge
                    matching_projected_mixed_group_incidence += (
                        len(owner_keys["V"]) * len(owner_keys["W"])
                    )
                    for role_type, keys in owner_keys.items():
                        matching_projected_key_group_load.update(keys)
                        for first_key, second_key in combinations(sorted(keys), 2):
                            key_pair = first_key, second_key
                            matching_projected_full_same_pair_codegrees[
                                role_type
                            ][key_pair] += 1
                            if (
                                projected_physical_edge(first_key)
                                == projected_physical_edge(second_key)
                            ):
                                matching_projected_bundle_pair_codegrees[
                                    role_type
                                ][key_pair] += 1

                    local_projected_pairs: set[
                        tuple[tuple[object, ...], tuple[object, ...]]
                    ] = set()
                    for first_index, (first_neighbour, first_weight) in enumerate(
                        active_neighbours
                    ):
                        for second_neighbour, second_weight in active_neighbours[
                            first_index + 1 :
                        ]:
                            for first_key in projected_keys[first_neighbour]:
                                for second_key in projected_keys[second_neighbour]:
                                    key_pair = tuple(sorted((first_key, second_key)))
                                    assert len(key_pair) == 2
                                    assert key_pair not in local_projected_pairs
                                    local_projected_pairs.add(key_pair)
                                    matching_projected_key_pair_codegrees[key_pair] += 1
                                    previous_owner = matching_projected_key_pair_owner.get(
                                        key_pair
                                    )
                                    if previous_owner is None or owner < previous_owner:
                                        matching_projected_key_pair_owner[key_pair] = owner
                                    if key_pair[0][0] != key_pair[1][0]:
                                        matching_projected_mixed_key_pair_groups[
                                            key_pair
                                        ].append(owner)
                            assert (
                                len(projected_keys[first_neighbour])
                                * len(projected_keys[second_neighbour])
                                == first_weight * second_weight
                            )
                    assert len(local_projected_pairs) == switch_pair

                    metric_edge_mass = 0
                    role_pair_mass: Counter[tuple[int, int]] = Counter()
                    type_pair_mass: Counter[str] = Counter()
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
                        role_pair = tuple(
                            sorted(
                                (
                                    neighbour_roles[first_neighbour],
                                    neighbour_roles[second_neighbour],
                                )
                            )
                        )
                        assert len(role_pair) == 2
                        role_pair_mass[role_pair] += weight
                        first_type = (
                            "V" if neighbour_roles[first_neighbour] < 2 else "W"
                        )
                        second_type = (
                            "V" if neighbour_roles[second_neighbour] < 2 else "W"
                        )
                        type_pair_mass["".join(sorted((first_type, second_type)))] += (
                            weight
                        )
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
                    assert sum(role_pair_mass.values()) == switch_pair
                    assert sum(type_pair_mass.values()) == switch_pair
                    matching_endpoint_switch_role_pair_mass.update(role_pair_mass)
                    matching_endpoint_switch_type_pair_mass.update(type_pair_mass)

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

    mixed_group_incidence = matching_projected_mixed_group_incidence
    mixed_pair_items = {
        key_pair: codegree
        for key_pair, codegree in matching_projected_key_pair_codegrees.items()
        if "".join(sorted((key_pair[0][0], key_pair[1][0]))) == "VW"
    }
    assert mixed_group_incidence == sum(mixed_pair_items.values())
    mixed_pair_collision = sum(
        codegree * (codegree - 1) // 2
        for codegree in mixed_pair_items.values()
    )
    assert {
        key_pair: len(groups)
        for key_pair, groups in matching_projected_mixed_key_pair_groups.items()
    } == mixed_pair_items

    def mixed_owner_difference(
        first: tuple[Cell, Point, Point],
        second: tuple[Cell, Point, Point],
    ) -> tuple[Point, Point, Point]:
        first_centre, first_endpoint, first_switch = first
        second_centre, second_endpoint, second_switch = second
        assert first_endpoint == second_endpoint
        h = subtract(first_centre[1], second_centre[1])
        s = rotate(subtract(first_switch, second_switch))
        a = subtract(first_centre[0], second_centre[0])
        assert h != (0, 0) or s != (0, 0) or a != (0, 0)
        return h, s, a

    mixed_group_pair_key_load: Counter[
        tuple[tuple[Cell, Point, Point], tuple[Cell, Point, Point]]
    ] = Counter()
    mixed_key_difference_load: Counter[
        tuple[
            tuple[tuple[object, ...], tuple[object, ...]],
            tuple[Point, Point, Point],
        ]
    ] = Counter()
    mixed_difference_mass: Counter[tuple[Point, Point, Point]] = Counter()
    mixed_difference_group_pairs: dict[
        tuple[Point, Point, Point],
        set[tuple[tuple[Cell, Point, Point], tuple[Cell, Point, Point]]],
    ] = defaultdict(set)
    for key_pair, groups in matching_projected_mixed_key_pair_groups.items():
        assert len(set(groups)) == len(groups)
        for first_owner, second_owner in combinations(sorted(groups), 2):
            owner_pair = first_owner, second_owner
            difference = mixed_owner_difference(first_owner, second_owner)
            mixed_group_pair_key_load[owner_pair] += 1
            mixed_key_difference_load[key_pair, difference] += 1
            mixed_difference_mass[difference] += 1
            mixed_difference_group_pairs[difference].add(owner_pair)
    assert sum(mixed_group_pair_key_load.values()) == mixed_pair_collision
    assert sum(mixed_key_difference_load.values()) == mixed_pair_collision
    assert sum(mixed_difference_mass.values()) == mixed_pair_collision

    difference_overlap: dict[Point, int] = {}

    def overlap(shift: Point) -> int:
        if shift not in difference_overlap:
            difference_overlap[shift] = sum(
                add(value, shift) in differences for value in differences
            )
        return difference_overlap[shift]

    def repeated_pair_upsilon(difference: tuple[Point, Point, Point]) -> int:
        h, s, a = difference
        lam = inverse_linear(h)
        js = rotate(s)
        products = (
            overlap(h) * overlap(s) * overlap(a),
            overlap(lam) * overlap(s) * overlap(a),
            overlap(h) * overlap(js) * overlap(add(a, js)),
            overlap(h) * overlap(s) * overlap(subtract(h, a)),
            overlap(h)
            * overlap(s)
            * overlap(subtract(h, linear(a))),
            overlap(a)
            * overlap(add(a, js))
            * overlap(subtract(a, lam)),
            overlap(subtract(h, a))
            * overlap(subtract(add(h, s), a))
            * overlap(a),
            overlap(subtract(h, a))
            * overlap(subtract(add(h, s), a))
            * overlap(subtract(h, linear(a))),
        )
        return min(products)

    mixed_difference_key_support: Counter[tuple[Point, Point, Point]] = Counter(
        difference for _, difference in mixed_key_difference_load
    )
    mixed_difference_upsilon = {
        difference: repeated_pair_upsilon(difference)
        for difference in mixed_difference_mass
    }
    mixed_difference_zero_pattern_mass: Counter[str] = Counter()
    mixed_difference_zero_pattern_support: Counter[str] = Counter()
    for (h, s, a), mass in mixed_difference_mass.items():
        pattern = (
            ("H" if h == (0, 0) else "-")
            + ("S" if s == (0, 0) else "-")
            + ("A" if a == (0, 0) else "-")
        )
        mixed_difference_zero_pattern_mass[pattern] += mass
        mixed_difference_zero_pattern_support[pattern] += 1
    assert (
        matching_projected_same_centre_cross_third
        == mixed_difference_zero_pattern_mass["H-A"]
    )
    assert (
        2 * matching_projected_same_centre_cross_third
        <= matching_projected_same_centre_weighted_envelope
    )
    assert all(
        load <= mixed_difference_upsilon[difference]
        for (_, difference), load in mixed_key_difference_load.items()
    )
    mixed_occupied_cell_upsilon_upper = sum(
        mixed_difference_key_support[difference] * upsilon
        for difference, upsilon in mixed_difference_upsilon.items()
    )
    single_key_reuse = {
        role_type: sum(
            load * (load - 1) // 2
            for key, load in matching_projected_key_group_load.items()
            if key[0] == role_type
        )
        for role_type in ("V", "W")
    }
    full_same_type_pair_collision = {
        role_type: sum(
            codegree * (codegree - 1) // 2
            for codegree in matching_projected_full_same_pair_codegrees[
                role_type
            ].values()
        )
        for role_type in ("V", "W")
    }
    physical_bundle_collision = {
        role_type: sum(
            codegree * (codegree - 1) // 2
            for codegree in matching_projected_bundle_pair_codegrees[
                role_type
            ].values()
        )
        for role_type in ("V", "W")
    }
    cross_part_pair_collision = {
        role_type: full_same_type_pair_collision[role_type]
        - physical_bundle_collision[role_type]
        for role_type in ("V", "W")
    }

    recorded_same_type_collision = {
        role_type * 2: sum(
            codegree * (codegree - 1) // 2
            for key_pair, codegree in matching_projected_key_pair_codegrees.items()
            if key_pair[0][0] == role_type and key_pair[1][0] == role_type
        )
        for role_type in ("V", "W")
    }
    assert cross_part_pair_collision == {
        role_type: recorded_same_type_collision[role_type * 2]
        for role_type in ("V", "W")
    }
    assert full_same_type_pair_collision == {
        role_type: cross_part_pair_collision[role_type]
        + physical_bundle_collision[role_type]
        for role_type in ("V", "W")
    }
    mixed_collision_upper = (
        min(single_key_reuse.values())
        + sum(full_same_type_pair_collision.values())
    )
    assert mixed_pair_collision <= mixed_collision_upper

    active_mixed_keys = set()
    mixed_support_min_owner_load = 0
    for first_key, second_key in mixed_pair_items:
        active_mixed_keys.add(first_key)
        active_mixed_keys.add(second_key)
        mixed_support_min_owner_load += min(
            matching_projected_key_group_load[first_key],
            matching_projected_key_group_load[second_key],
        )
    assert mixed_group_incidence <= mixed_support_min_owner_load

    def projected_pair_profile(role_types: str) -> tuple[object, ...]:
        items = [
            (key_pair, codegree)
            for key_pair, codegree in matching_projected_key_pair_codegrees.items()
            if "".join(sorted((key_pair[0][0], key_pair[1][0]))) == role_types
        ]
        degrees: Counter[tuple[object, ...]] = Counter()
        for (first_key, second_key), _ in items:
            degrees[first_key] += 1
            degrees[second_key] += 1
        pair_common_neighbours: Counter[
            tuple[tuple[object, ...], tuple[object, ...]]
        ] = Counter()
        rectangle_owner_types: Counter[int] = Counter()
        degeneracy = 0
        if role_types == "VW":
            adjacency: dict[
                tuple[object, ...], set[tuple[object, ...]]
            ] = defaultdict(set)
            for (first_key, second_key), _ in items:
                assert first_key[0] == "V" and second_key[0] == "W"
                adjacency[first_key].add(second_key)
                adjacency[second_key].add(first_key)
            live_degrees = {
                vertex: len(neighbours) for vertex, neighbours in adjacency.items()
            }
            heap = [(degree, vertex) for vertex, degree in live_degrees.items()]
            heapq.heapify(heap)
            removed: set[tuple[object, ...]] = set()
            while heap:
                degree, vertex = heapq.heappop(heap)
                if vertex in removed or degree != live_degrees[vertex]:
                    continue
                degeneracy = max(degeneracy, degree)
                removed.add(vertex)
                for neighbour in adjacency[vertex]:
                    if neighbour in removed:
                        continue
                    live_degrees[neighbour] -= 1
                    heapq.heappush(
                        heap,
                        (live_degrees[neighbour], neighbour),
                    )
            assert len(removed) == len(adjacency)
            left_adjacency = {
                vertex: neighbours
                for vertex, neighbours in adjacency.items()
                if vertex[0] == "V"
            }
            common_vertices: dict[
                tuple[tuple[object, ...], tuple[object, ...]],
                list[tuple[object, ...]],
            ] = defaultdict(list)
            for vertex, neighbours in left_adjacency.items():
                for first_key, second_key in combinations(sorted(neighbours), 2):
                    pair_common_neighbours[first_key, second_key] += 1
                    common_vertices[first_key, second_key].append(vertex)
            for vertex, neighbours in adjacency.items():
                if vertex[0] != "W":
                    continue
                for first_key, second_key in combinations(sorted(neighbours), 2):
                    pair_common_neighbours[first_key, second_key] += 1
            for (first_w, second_w), vertices in common_vertices.items():
                for first_v, second_v in combinations(sorted(vertices), 2):
                    edge_pairs = (
                        tuple(sorted((first_v, first_w))),
                        tuple(sorted((first_v, second_w))),
                        tuple(sorted((second_v, first_w))),
                        tuple(sorted((second_v, second_w))),
                    )
                    owners = tuple(
                        matching_projected_key_pair_owner[edge_pair]
                        for edge_pair in edge_pairs
                    )
                    cross_colour_vertices = sum(
                        owners[first_index] != owners[second_index]
                        for first_index, second_index in (
                            (0, 1),
                            (2, 3),
                            (0, 2),
                            (1, 3),
                        )
                    )
                    assert (len(set(owners)) == 1) == (
                        cross_colour_vertices == 0
                    )
                    rectangle_owner_types[cross_colour_vertices] += 1
            assert sum(rectangle_owner_types.values()) * 2 == sum(
                value * (value - 1) // 2
                for value in pair_common_neighbours.values()
            )
        return (
            role_types,
            sum(codegree for _, codegree in items),
            len(items),
            len(degrees),
            max(degrees.values(), default=0),
            sum(value * value for value in degrees.values()),
            degeneracy,
            max((codegree for _, codegree in items), default=0),
            sum(codegree * (codegree - 1) // 2 for _, codegree in items),
            max(pair_common_neighbours.values(), default=0),
            sum(
                value * (value - 1) // 2
                for value in pair_common_neighbours.values()
            )
            // 2,
            tuple(sorted(rectangle_owner_types.items())),
            tuple(sorted(Counter(codegree for _, codegree in items).items())),
        )

    difference_sum_loads = Counter(
        add(first, second) for first in differences for second in differences
    )
    assert all(
        value in difference_sum_loads
        for value in matching_projected_same_centre_weighted_footprint_depth
    )
    matching_projected_same_centre_footprint_representation_ratio = max(
        (
            weight / difference_sum_loads[value]
            for value, weight in (
                matching_projected_same_centre_weighted_footprint_depth.items()
            )
        ),
        default=Fraction(0),
    )

    matching_projected_same_centre_owner_offset_witnesses: Counter[
        tuple[object, ...]
    ] = Counter()
    for (physical_wedge, _), owners in (
        matching_projected_same_centre_physical_wedge_triple_owners.items()
    ):
        for first_owner, second_owner in combinations(sorted(owners), 2):
            first_centre, _, first_second_displacement, first_eta = first_owner
            second_centre, _, second_second_displacement, second_eta = second_owner
            owner_offset = (
                subtract(second_centre[0], first_centre[0]),
                subtract(second_second_displacement, first_second_displacement),
                subtract(second_eta, first_eta),
            )
            matching_projected_same_centre_owner_offset_witnesses[
                (physical_wedge, *owner_offset)
            ] += 1
    matching_projected_same_centre_owner_offset_zero_masks: Counter[
        tuple[int, ...]
    ] = Counter()
    for (_, centre_shift, second_shift, eta_shift), witness_count in (
        matching_projected_same_centre_owner_offset_witnesses.items()
    ):
        owner_directions = (
            centre_shift,
            (
                -linear(second_shift)[0] - rotate(centre_shift)[0],
                -linear(second_shift)[1] - rotate(centre_shift)[1],
            ),
            (
                -linear(add(centre_shift, second_shift))[0],
                -linear(add(centre_shift, second_shift))[1],
            ),
            add(centre_shift, eta_shift),
            (
                -second_shift[0] - rotate(eta_shift)[0],
                -second_shift[1] - rotate(eta_shift)[1],
            ),
            (-rotate(eta_shift)[0], -rotate(eta_shift)[1]),
        )
        zero_mask = tuple(
            index
            for index, direction in enumerate(owner_directions)
            if direction == (0, 0)
        )
        matching_projected_same_centre_owner_offset_zero_masks[
            zero_mask
        ] += witness_count

    # Every repeated mixed translate cell has one common physical endpoint,
    # one incident V edge, one incident W edge, and one orientation choice
    # for each edge.  The physical-wedge aggregation is therefore lossless.
    assert sum(
        matching_projected_same_centre_physical_wedge_mass.values()
    ) == matching_projected_same_centre_cross_third
    assert all(
        mass
        == matching_projected_same_centre_physical_wedge_resonant_mass[wedge]
        + matching_projected_same_centre_physical_wedge_transverse_mass[wedge]
        for wedge, mass in (
            matching_projected_same_centre_physical_wedge_mass.items()
        )
    )
    assert sum(
        matching_projected_same_centre_physical_wedge_class_mass.values()
    ) == matching_projected_same_centre_cross_third
    assert 3 * sum(
        matching_projected_same_centre_physical_wedge_triple_codegree.values()
    ) == matching_projected_same_centre_cross_third
    assert sum(
        matching_projected_same_centre_owner_offset_witnesses.values()
    ) == sum(
        value * (value - 1) // 2
        for value in (
            matching_projected_same_centre_physical_wedge_triple_codegree.values()
        )
    )
    if points is not None:
        point_count = len(points)
        assert len(
            matching_projected_same_centre_physical_wedge_mass
        ) <= 4 * point_count * (point_count - 1) ** 2

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
        "matching_endpoint_collision_role_pairs": (
            (
                "exact_roles",
                tuple(sorted(matching_endpoint_switch_role_pair_mass.items())),
            ),
            (
                "role_types",
                tuple(sorted(matching_endpoint_switch_type_pair_mass.items())),
            ),
            (
                "same_oriented_role",
                sum(
                    value
                    for (first_role, second_role), value in (
                        matching_endpoint_switch_role_pair_mass.items()
                    )
                    if first_role == second_role
                ),
            ),
            (
                "same_type_opposite_orientation",
                sum(
                    value
                    for (first_role, second_role), value in (
                        matching_endpoint_switch_role_pair_mass.items()
                    )
                    if first_role != second_role
                    and (first_role < 2) == (second_role < 2)
                ),
            ),
            (
                "mixed_VW",
                matching_endpoint_switch_type_pair_mass["VW"],
            ),
        ),
        "matching_projected_key_pair_codegrees": tuple(
            projected_pair_profile(role_types)
            for role_types in ("VV", "VW", "WW")
        ),
        "matching_projected_mixed_group_overlap": (
            ("groups", matching_projected_group_count),
            ("incidence", mixed_group_incidence),
            ("pair_collision", mixed_pair_collision),
            (
                "single_key_reuse",
                tuple(sorted(single_key_reuse.items())),
            ),
            (
                "full_same_type_pair_collision",
                tuple(sorted(full_same_type_pair_collision.items())),
            ),
            (
                "cross_part_pair_collision",
                tuple(sorted(cross_part_pair_collision.items())),
            ),
            (
                "physical_bundle_collision",
                tuple(sorted(physical_bundle_collision.items())),
            ),
            (
                "maximum_bundle_pair_group_codegree",
                tuple(
                    (
                        role_type,
                        max(codegrees.values(), default=0),
                    )
                    for role_type, codegrees in sorted(
                        matching_projected_bundle_pair_codegrees.items()
                    )
                ),
            ),
            ("collision_upper", mixed_collision_upper),
            ("active_keys", len(active_mixed_keys)),
            ("support_min_owner_load", mixed_support_min_owner_load),
        ),
        "matching_projected_mixed_repeated_pair_cells": (
            ("collision_mass", mixed_pair_collision),
            ("group_pairs", len(mixed_group_pair_key_load)),
            (
                "maximum_key_pairs_per_group_pair",
                max(mixed_group_pair_key_load.values(), default=0),
            ),
            ("difference_cells", len(mixed_difference_mass)),
            (
                "maximum_collision_mass_per_difference",
                max(mixed_difference_mass.values(), default=0),
            ),
            (
                "maximum_group_pairs_per_difference",
                max(
                    (len(value) for value in mixed_difference_group_pairs.values()),
                    default=0,
                ),
            ),
            (
                "key_difference_cells",
                len(mixed_key_difference_load),
            ),
            (
                "maximum_group_pairs_per_key_difference_cell",
                max(mixed_key_difference_load.values(), default=0),
            ),
            (
                "occupied_cell_upsilon_upper",
                mixed_occupied_cell_upsilon_upper,
            ),
            (
                "maximum_upsilon_on_occupied_difference",
                max(mixed_difference_upsilon.values(), default=0),
            ),
            (
                "group_pair_key_load_histogram",
                tuple(sorted(Counter(mixed_group_pair_key_load.values()).items())),
            ),
            (
                "key_difference_load_histogram",
                tuple(sorted(Counter(mixed_key_difference_load.values()).items())),
            ),
            (
                "top_difference_cells",
                tuple(
                    (
                        difference,
                        mass,
                        mixed_difference_key_support[difference],
                        len(mixed_difference_group_pairs[difference]),
                        mixed_difference_upsilon[difference],
                    )
                    for difference, mass in mixed_difference_mass.most_common(8)
                ),
            ),
            (
                "difference_zero_pattern_mass",
                tuple(sorted(mixed_difference_zero_pattern_mass.items())),
            ),
            (
                "difference_zero_pattern_support",
                tuple(sorted(mixed_difference_zero_pattern_support.items())),
            ),
            (
                "same_centre_cross_difference_energy",
                (
                    matching_projected_same_centre_cross_second,
                    matching_projected_same_centre_cross_third,
                    matching_projected_same_centre_cross_maximum,
                    matching_projected_same_centre_mixed_second_pencil,
                    matching_projected_same_centre_weighted_envelope,
                    tuple(
                        sorted(
                            matching_projected_same_centre_cross_load_histogram.items()
                        )
                    ),
                    (
                        len(matching_projected_same_centre_physical_wedge_mass),
                        max(
                            matching_projected_same_centre_physical_wedge_mass.values(),
                            default=0,
                        ),
                        tuple(
                            (
                                wedge,
                                mass,
                                matching_projected_same_centre_physical_wedge_cells[
                                    wedge
                                ],
                                matching_projected_same_centre_physical_wedge_resonant_mass[
                                    wedge
                                ],
                                matching_projected_same_centre_physical_wedge_transverse_mass[
                                    wedge
                                ],
                                tuple(
                                    sorted(
                                        matching_projected_same_centre_physical_wedge_rows[
                                            wedge
                                        ],
                                        reverse=True,
                                    )
                                ),
                            )
                            for wedge, mass in matching_projected_same_centre_physical_wedge_mass.most_common(
                                8
                            )
                        ),
                        tuple(
                            (
                                wedge_class,
                                matching_projected_same_centre_physical_wedge_class_mass[
                                    wedge_class
                                ],
                                max(
                                    (
                                        mass
                                        for wedge, mass in matching_projected_same_centre_physical_wedge_mass.items()
                                        if (
                                            wedge[1] == wedge[2]
                                            or wedge[1]
                                            == (-wedge[2][0], -wedge[2][1])
                                        )
                                        == (wedge_class == "same_edge")
                                    ),
                                    default=0,
                                ),
                            )
                            for wedge_class in ("same_edge", "one_endpoint")
                        ),
                        (
                            len(
                                matching_projected_same_centre_physical_wedge_triple_codegree
                            ),
                            max(
                                matching_projected_same_centre_physical_wedge_triple_codegree.values(),
                                default=0,
                            ),
                            sum(
                                value * (value - 1) // 2
                                for value in matching_projected_same_centre_physical_wedge_triple_codegree.values()
                            ),
                            tuple(
                                (
                                    wedge_triple,
                                    codegree,
                                    tuple(
                                        matching_projected_same_centre_physical_wedge_triple_owners[
                                            wedge_triple
                                        ]
                                    ),
                                )
                                for wedge_triple, codegree in matching_projected_same_centre_physical_wedge_triple_codegree.most_common(
                                    5
                                )
                            ),
                            (
                                len(
                                    matching_projected_same_centre_owner_offset_witnesses
                                ),
                                sum(
                                    matching_projected_same_centre_owner_offset_witnesses.values()
                                ),
                                max(
                                    matching_projected_same_centre_owner_offset_witnesses.values(),
                                    default=0,
                                ),
                                tuple(
                                    matching_projected_same_centre_owner_offset_witnesses.most_common(
                                        5
                                    )
                                ),
                                tuple(
                                    sorted(
                                        matching_projected_same_centre_owner_offset_zero_masks.items()
                                    )
                                ),
                            ),
                        ),
                    ),
                    tuple(
                        sorted(
                            matching_projected_same_centre_cross_resonance.items()
                        )
                    ),
                    (
                        sum(matching_projected_same_centre_footprint_depth.values()),
                        len(matching_projected_same_centre_footprint_depth),
                        max(
                            matching_projected_same_centre_footprint_depth.values(),
                            default=0,
                        ),
                        sum(
                            matching_projected_same_centre_resonant_footprint_depth.values()
                        ),
                        len(
                            matching_projected_same_centre_resonant_footprint_depth
                        ),
                        max(
                            matching_projected_same_centre_resonant_footprint_depth.values(),
                            default=0,
                        ),
                        sum(
                            matching_projected_same_centre_transverse_footprint_depth.values()
                        ),
                        len(
                            matching_projected_same_centre_transverse_footprint_depth
                        ),
                        max(
                            matching_projected_same_centre_transverse_footprint_depth.values(),
                            default=0,
                        ),
                        sum(
                            matching_projected_same_centre_weighted_footprint_depth.values(),
                            Fraction(0),
                        ),
                        max(
                            matching_projected_same_centre_weighted_footprint_depth.values(),
                            default=Fraction(0),
                        ),
                        max(
                            matching_projected_same_centre_resonant_weighted_footprint_depth.values(),
                            default=Fraction(0),
                        ),
                        max(
                            matching_projected_same_centre_transverse_weighted_footprint_depth.values(),
                            default=Fraction(0),
                        ),
                        tuple(
                            (
                                value,
                                weight,
                                matching_projected_same_centre_resonant_weighted_footprint_depth[
                                    value
                                ],
                                matching_projected_same_centre_transverse_weighted_footprint_depth[
                                    value
                                ],
                                matching_projected_same_centre_footprint_depth[value],
                            )
                            for value, weight in matching_projected_same_centre_weighted_footprint_depth.most_common(
                                8
                            )
                        ),
                        matching_projected_same_centre_footprint_representation_ratio,
                    ),
                    tuple(
                        sorted(
                            matching_projected_same_centre_cross_rich_rows,
                            reverse=True,
                        )[:8]
                    ),
                    tuple(
                        sorted(
                            (
                                row
                                for row in matching_projected_same_centre_cross_rich_rows
                                if row[2] == 0
                            ),
                            reverse=True,
                        )[:8]
                    ),
                ),
            ),
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
    large_costas_only = "--large-costas-only" in sys.argv
    families: list[tuple[str, set[Point], list[Point] | None]] = []
    if not large_costas_only:
        costas_11 = transformed_costas(11)
        costas_17 = transformed_costas(17)
        families.extend(
            [
                ("closure-30", difference_set(POINTS[:30]), POINTS[:30]),
                ("Costas-11", costas_11[1], costas_11[0]),
                ("Costas-17", costas_17[1], costas_17[0]),
                ("radial-4", radial_set(4), None),
                ("radial-5", radial_set(5), None),
                ("radial-6", radial_set(6), None),
            ]
        )
    if "--extended" in sys.argv:
        costas_23 = transformed_costas(23)
        families.extend(
            [
                ("closure-40", difference_set(POINTS[:40]), POINTS[:40]),
                ("Costas-23", costas_23[1], costas_23[0]),
                ("radial-8", radial_set(8), None),
            ]
        )
    if "--larger" in sys.argv or large_costas_only:
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
