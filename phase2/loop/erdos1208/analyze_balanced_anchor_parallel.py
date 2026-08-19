#!/usr/bin/env python3
"""Exact diagnostics for parallel edges in the balanced-anchor graphs.

This is exploratory evidence for HANDOFF_20260819.md, not a proof of the
balanced-anchor theorem.
"""

from __future__ import annotations

from collections import Counter
import heapq
import sys

from analyze_affine_costas_energy import welch
from verify_determinant_prime_costas_resonance import ROWS, apply
from verify_endpoint_switched_two_moment_charge import midpoint_table, negate
from verify_orthogonal_two_support_gate import difference_set
from verify_seven_incidence_opposite_endpoint_charge import (
    POINTS,
    add,
    linear,
    rich_fibres,
    rotate,
    subtract,
)

from verify_hybrid_endpoint_opposite_charge import antipodal_sign


Point = tuple[int, int]
Omega = tuple[int, Point]
Edge = tuple[Omega, Point, Point]


def graph_degeneracy(
    edge_weights: Counter[tuple[Point, Point]], weighted: bool
) -> int:
    """Return the (possibly multiplicity-weighted) bipartite degeneracy."""
    adjacency: dict[
        tuple[int, Point], dict[tuple[int, Point], int]
    ] = {}
    for (left, right), multiplicity in edge_weights.items():
        left_vertex = 0, left
        right_vertex = 1, right
        adjacency.setdefault(left_vertex, {})[right_vertex] = multiplicity
        adjacency.setdefault(right_vertex, {})[left_vertex] = multiplicity

    degrees = {
        vertex: sum(
            value if weighted else 1 for value in neighbours.values()
        )
        for vertex, neighbours in adjacency.items()
    }
    queue = [(degree, vertex) for vertex, degree in degrees.items()]
    heapq.heapify(queue)
    alive = set(adjacency)
    answer = 0
    while queue:
        degree, vertex = heapq.heappop(queue)
        if vertex not in alive or degrees[vertex] != degree:
            continue
        answer = max(answer, degree)
        alive.remove(vertex)
        for neighbour, multiplicity in adjacency[vertex].items():
            if neighbour not in alive:
                continue
            degrees[neighbour] -= multiplicity if weighted else 1
            heapq.heappush(queue, (degrees[neighbour], neighbour))
    return answer


def profile(points: list[Point], cores: bool = False) -> tuple[int, ...]:
    differences = difference_set(points)
    midpoints = midpoint_table(points)
    fibres, _, _ = rich_fibres(differences, adaptive=True)

    edges: Counter[Edge] = Counter()
    endpoint_layers: dict[
        tuple[Omega, Point], Counter[tuple[Point, Point]]
    ] = {}
    left_degrees: Counter[tuple[Omega, Point]] = Counter()
    right_degrees: Counter[tuple[Omega, Point]] = Counter()
    normal_mass = 0

    for (base, ordinary_sum), fibre in fibres.items():
        w_value = subtract(ordinary_sum, base)
        for q_value in fibre:
            left = subtract(w_value, linear(q_value))
            right = subtract(w_value, q_value)
            assert q_value == negate(rotate(subtract(right, left)))
            for p_value in fibre:
                if q_value == p_value:
                    continue
                c_value = add(base, p_value)
                h_value = subtract(midpoints[base], midpoints[c_value])
                displacement = subtract(base, c_value)
                if h_value in (displacement, negate(displacement)):
                    continue

                omega = int(antipodal_sign(c_value)), h_value
                edge = omega, left, right
                edges[edge] += 1
                if cores:
                    endpoint_layers.setdefault(
                        (omega, p_value), Counter()
                    )[(left, right)] += 1
                left_degrees[(omega, left)] += 1
                right_degrees[(omega, right)] += 1
                normal_mass += 1

    parallel_second = sum(value * value for value in edges.values())
    balanced_moment = sum(
        multiplicity
        * min(left_degrees[(omega, left)], right_degrees[(omega, right)])
        for (omega, left, right), multiplicity in edges.items()
    )
    parallel_excess = parallel_second - normal_mass
    transverse_excess = balanced_moment - parallel_second
    multiplicity_histogram = Counter(edges.values())

    max_simple_degeneracy = 0
    max_weighted_degeneracy = 0
    max_layer_simple_degeneracy = 0
    max_layer_weighted_degeneracy = 0
    if cores:
        omega_edges: dict[Omega, Counter[tuple[Point, Point]]] = {}
        for (omega, left, right), multiplicity in edges.items():
            omega_edges.setdefault(omega, Counter())[(left, right)] = (
                multiplicity
            )
        for edge_weights in omega_edges.values():
            max_simple_degeneracy = max(
                max_simple_degeneracy,
                graph_degeneracy(edge_weights, weighted=False),
            )
            max_weighted_degeneracy = max(
                max_weighted_degeneracy,
                graph_degeneracy(edge_weights, weighted=True),
            )
        for edge_weights in endpoint_layers.values():
            max_layer_simple_degeneracy = max(
                max_layer_simple_degeneracy,
                graph_degeneracy(edge_weights, weighted=False),
            )
            max_layer_weighted_degeneracy = max(
                max_layer_weighted_degeneracy,
                graph_degeneracy(edge_weights, weighted=True),
            )

    assert parallel_second <= balanced_moment
    assert parallel_excess >= 0 and transverse_excess >= 0
    assert sum(
        multiplicity * count
        for multiplicity, count in multiplicity_histogram.items()
    ) == normal_mass

    return (
        normal_mass,
        len(edges),
        parallel_second,
        max(edges.values(), default=0),
        balanced_moment,
        parallel_excess,
        transverse_excess,
        max_simple_degeneracy,
        max_weighted_degeneracy,
        max_layer_simple_degeneracy,
        max_layer_weighted_degeneracy,
    )


def main() -> None:
    expected_prefix: dict[str, tuple[int, ...]] = {
        "closure-30": (984, 984, 984, 1, 984, 0, 0),
        "closure-40": (301_640, 301_384, 302_152, 2, 313_937, 512, 11_785),
        "closure-80": (303_490, 303_444, 303_582, 2, 304_560, 92, 978),
        "Costas-11": (2_100, 2_090, 2_120, 2, 2_172, 20, 52),
        "Costas-17": (16_336, 16_255, 16_498, 2, 17_349, 162, 851),
        "Costas-23": (458_872, 455_385, 465_854, 3, 584_338, 6_982, 118_484),
        "Costas-31": (731_126, 725_308, 742_794, 3, 946_578, 11_668, 203_784),
        "Costas-37": (2_853_770, 2_824_830, 2_912_002, 3, 3_808_250, 58_232, 896_248),
        "Costas-41": (4_445_470, 4_402_368, 4_532_186, 4, 6_240_597, 86_716, 1_708_411),
        "Costas-43": (8_250_792, 8_171_268, 8_410_596, 4, 11_901_168, 159_804, 3_490_572),
    }
    expected_cores: dict[str, tuple[int, ...]] = {
        "closure-30": (1, 1, 1, 1),
        "closure-40": (2, 2, 2, 2),
        "closure-80": (1, 2, 1, 1),
        "Costas-11": (1, 2, 1, 1),
        "Costas-17": (2, 2, 1, 1),
        "Costas-23": (3, 3, 2, 2),
        "Costas-31": (3, 3, 3, 3),
        "Costas-37": (3, 4, 3, 3),
        "Costas-41": (4, 5, 3, 3),
    }
    families: list[tuple[str, list[Point]]] = [
        ("closure-30", POINTS[:30]),
        ("closure-40", POINTS[:40]),
    ]
    primes = [11, 17, 23, 31]
    if "--extended" in sys.argv:
        families.append(("closure-80", POINTS[:80]))
        primes += [37, 41, 43]

    for prime in primes:
        matrix, _ = ROWS[prime]
        points = [apply(matrix, point) for point in welch(prime)]
        families.append((f"Costas-{prime}", points))

    for name, points in families:
        compute_cores = "--cores" in sys.argv and (
            name != "Costas-43" or "--p43-core" in sys.argv
        )
        values = profile(points, cores=compute_cores)
        assert values[:7] == expected_prefix[name]
        if compute_cores:
            assert values[7:] == expected_cores[name]
        print(
            name,
            values,
            "parallel-load",
            values[2] / values[0] if values[0] else 0.0,
            "balanced-load",
            values[4] / values[0] if values[0] else 0.0,
        )

    print("BALANCED ANCHOR PARALLEL/CORE DIAGNOSTICS: PASS")


if __name__ == "__main__":
    main()
