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
from math import ceil, log2
import sys

from analyze_affine_costas_energy import is_distance_sidon, welch
from verify_determinant_prime_costas_resonance import ROWS, apply
from verify_orthogonal_two_support_gate import difference_set
from verify_radial_orthogonal_product_barrier import radial_set
from verify_seven_incidence_opposite_endpoint_charge import linear, subtract
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

    summary = {
        "components": tuple(component_mass.most_common(8)),
        "shifts": tuple(shift_mass.most_common(8)),
        "fibres": tuple(fibre_mass.most_common(8)),
        "loads": tuple(Counter(loads.values()).most_common()),
        "endpoint_types": tuple(endpoint_types.most_common()),
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
