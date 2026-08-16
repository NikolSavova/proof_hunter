#!/usr/bin/env python3
"""Exact weighted path-DAG audits for the one-sided convex-chain route."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from itertools import combinations
from math import comb, log2
from pathlib import Path

sys.set_int_max_str_digits(0)

Point = tuple[int, int]


def frac(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def orient(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def in_triangle_strict(p: Point, a: Point, b: Point, c: Point) -> bool:
    values = (orient(a, b, p), orient(b, c, p), orient(c, a, p))
    return all(value > 0 for value in values) or all(value < 0 for value in values)


def nested_parabola_fan(log_population: int) -> dict:
    population = 1 << log_population
    scale = 100 * population * population
    u = (0, 0)
    v = (scale, 0)
    z = [
        (scale // 2 + j * j, -scale * (1 << (j + 1)))
        for j in range(population)
    ]
    for i in range(population):
        for j in range(i + 1, population):
            assert in_triangle_strict(z[i], u, v, z[j])

    # The internal path for label j is the singleton state z_j; common roots
    # u,v are deliberately excluded from bottleneck statistics.
    disjoint = Fraction(population - 1, population)
    max_internal_vertex = Fraction(1, population)
    return {
        "log2_population": log_population,
        "path_count": population,
        "coordinates": {
            "u": list(u),
            "v": list(v),
            "z": [list(point) for point in z],
        },
        "internal_path_length": 1,
        "internally_vertex_disjoint_pair_probability": frac(disjoint),
        "geometrically_nonnested_pair_probability": "0",
        "maximum_internal_vertex_mass": frac(max_internal_vertex),
        "maximum_nonroot_edge_mass": frac(max_internal_vertex),
        "compressed_common_tangent_cell_mass": "1",
    }


def normalize_projective(vector: tuple[int, int, int], prime: int) -> tuple[int, int, int]:
    for entry in vector:
        if entry % prime:
            inverse = pow(entry, -1, prime)
            return tuple((inverse * value) % prime for value in vector)
    raise ValueError("zero projective vector")


def projective_plane_paths(prime: int) -> dict:
    assert prime >= 2
    points = sorted(
        {
            normalize_projective((x, y, z), prime)
            for x in range(prime)
            for y in range(prime)
            for z in range(prime)
            if (x, y, z) != (0, 0, 0)
        }
    )
    lines = points.copy()
    expected = prime * prime + prime + 1
    assert len(points) == len(lines) == expected
    incidence_paths = []
    vertex_degree = [0] * expected
    edge_degree: dict[tuple[int, int], int] = {}
    for line in lines:
        path = [
            index
            for index, point in enumerate(points)
            if sum(a * b for a, b in zip(line, point)) % prime == 0
        ]
        assert len(path) == prime + 1
        incidence_paths.append(path)
        for vertex in path:
            vertex_degree[vertex] += 1
        for edge in zip(path, path[1:]):
            edge_degree[edge] = edge_degree.get(edge, 0) + 1
    assert set(vertex_degree) == {prime + 1}
    assert set(edge_degree.values()) == {1}
    for first, second in combinations(incidence_paths, 2):
        assert len(set(first) & set(second)) == 1

    path_count = expected
    path_length = prime + 1
    max_vertex = Fraction(prime + 1, expected)
    theorem_lower = Fraction(1, path_length)
    assert max_vertex >= theorem_lower
    # State i is realized by (i,i^2); every incidence path is an increasing
    # subset of this strict parabolic convex chain.
    planar_states = [(index, index * index) for index in range(expected)]
    return {
        "prime_order": prime,
        "path_count": path_count,
        "internal_states_per_path": path_length,
        "all_path_pairs_intersect": True,
        "maximum_vertex_mass": frac(max_vertex),
        "weighted_intersection_lower_bound_1_over_r": frac(theorem_lower),
        "maximum_edge_mass": frac(Fraction(1, path_count)),
        "planar_parabola_state_coordinates": [list(point) for point in planar_states],
    }


def product_pair_identity(sizes: list[int]) -> tuple[int, int]:
    total = 1
    for size in sizes:
        total *= size
    prefix = 1
    suffix = total
    different = 0
    for size in sizes:
        suffix //= size
        different += prefix * size * (size - 1) * suffix * suffix
        prefix *= size
    assert total * total == different + total
    return total, different


def product_trie_stats(name: str, sizes: list[int]) -> dict:
    total, first_difference_pairs = product_pair_identity(sizes)
    coordinatewise_increasing = 1
    for size in sizes:
        coordinatewise_increasing *= size * (size + 1) // 2
    nonforward = 2 * coordinatewise_increasing - total
    assert 0 <= nonforward <= total * total
    internal_intersection = Fraction(1, sizes[0])
    internally_disjoint = 1 - internal_intersection
    max_vertex = internal_intersection
    nonnested = Fraction(total * total - nonforward, total * total)
    conditional_rows = []
    prefix = 1
    for depth, size in enumerate(sizes, start=1):
        prefix *= size
        conditional_rows.append(
            {
                "depth": depth,
                "alphabet": size,
                "conditional_divergence_probability": frac(Fraction(size - 1, size)),
                "conditional_child_bottleneck_mass": frac(Fraction(1, size)),
                "unconditional_max_prefix_cell_mass": frac(Fraction(1, prefix)),
            }
        )
    return {
        "name": name,
        "coordinate_count": len(sizes),
        "sizes": sizes,
        "path_count": total,
        "first_difference_ordered_pairs": first_difference_pairs,
        "diagonal_pairs": total,
        "internally_disjoint_pair_probability_after_root": frac(internally_disjoint),
        "maximum_nonroot_vertex_mass": frac(max_vertex),
        "nonnested_forward_pair_probability": frac(nonnested),
        "log2_nonforward_upper_bound": 1 + len(sizes) * log2(0.75),
        "first_four_conditional_rows": conditional_rows[:4],
        "last_conditional_row": conditional_rows[-1],
    }


def ramp_sizes(h: int) -> list[int]:
    length = 1 << h
    ramp = [1 << j for j in range(h)]
    exponents = ramp + [length] * (length // 2) + list(reversed(ramp))
    return [1 << exponent for exponent in exponents]


def intersecting_subsets_edge_obstruction(rank: int) -> dict:
    # All rank-subsets of a (2r-1)-set pairwise intersect.  Insert a unique
    # connector between consecutive selected ground states, making every DAG
    # edge path-specific while retaining the shared ground-state vertices.
    path_count = comb(2 * rank - 1, rank)
    vertex_mass = Fraction(rank, 2 * rank - 1)
    edge_mass = Fraction(1, path_count)
    assert path_count * rank == (2 * rank - 1) * comb(2 * rank - 2, rank - 1)
    return {
        "rank": rank,
        "path_count": path_count,
        "internal_path_length_after_unique_connectors": 2 * rank - 1,
        "all_pairs_vertex_intersect": True,
        "maximum_ground_vertex_mass": frac(vertex_mass),
        "maximum_edge_mass": frac(edge_mass),
        "log2_inverse_max_edge_mass": log2(path_count),
        "realization": (
            "ground states and path-specific connector states are placed in topological "
            "order on y=x^2; every path is a one-sided convex chain"
        ),
    }


def weighted_intersection_lemma_audits() -> list[dict]:
    # Exact finite weighted path systems, represented only by their internal
    # vertex sets and rational weights.
    systems = [
        ([{0, 1}, {1, 2}, {2, 3}], [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]),
        ([{0, 2, 4}, {1, 2}, {1, 3, 4}, {0, 3}], [Fraction(1, 5)] * 3 + [Fraction(2, 5)]),
    ]
    rows = []
    for paths, weights in systems:
        assert sum(weights) == 1
        vertices = sorted(set().union(*paths))
        masses = {vertex: sum(weight for path, weight in zip(paths, weights) if vertex in path) for vertex in vertices}
        intersection = sum(
            weights[i] * weights[j]
            for i in range(len(paths))
            for j in range(len(paths))
            if paths[i] & paths[j]
        )
        union_bound = sum(mass * mass for mass in masses.values())
        max_length = max(map(len, paths))
        max_mass = max(masses.values())
        assert intersection <= union_bound <= max_length * max_mass
        rows.append(
            {
                "paths": [sorted(path) for path in paths],
                "weights": [frac(weight) for weight in weights],
                "intersection_probability": frac(intersection),
                "sum_squared_vertex_masses": frac(union_bound),
                "max_path_length_times_max_vertex_mass": frac(max_length * max_mass),
            }
        )
    return rows


def main() -> None:
    result = {
        "dichotomies_tested": {
            "vertex_intersection": (
                "For paths with at most r internal vertices, either internally disjoint "
                "ordered-pair mass is at least delta or some internal vertex has path "
                "mass at least (1-delta)/r."
            ),
            "strong_nonnested": (
                "Replace internally disjoint by geometrically nonnested while refusing "
                "to count the common tangent cell/core as a bottleneck."
            ),
        },
        "weighted_intersection_lemma_audits": weighted_intersection_lemma_audits(),
        "nested_parabola_fans": [nested_parabola_fan(value) for value in (4, 6, 8)],
        "projective_plane_sharpness": [projective_plane_paths(prime) for prime in (3, 5, 7, 11)],
        "product_endpoint_tries": [
            product_trie_stats("homogeneous_endpoint_blocks", [16] * 8),
            product_trie_stats("Proposition26_product", [256] * 17),
            product_trie_stats("ramp_plateau_h6", ramp_sizes(6)),
        ],
        "edge_only_obstructions": [
            intersecting_subsets_edge_obstruction(rank) for rank in (4, 6, 8, 10, 16)
        ],
    }
    output = Path(__file__).with_name("path_dag_menger_certificate.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print("path-DAG Menger audit: PASS")
    for row in result["nested_parabola_fans"]:
        print(
            f"nested N={row['path_count']}: disjoint={row['internally_vertex_disjoint_pair_probability']}, "
            f"nonnested=0, max internal mass={row['maximum_internal_vertex_mass']}"
        )
    for row in result["projective_plane_sharpness"]:
        print(
            f"PG(2,{row['prime_order']}): paths={row['path_count']}, max vertex mass={row['maximum_vertex_mass']}"
        )
    for row in result["product_endpoint_tries"]:
        print(
            f"{row['name']}: disjoint={row['internally_disjoint_pair_probability_after_root']}, "
            f"log2(nonforward upper)={row['log2_nonforward_upper_bound']:.3f}"
        )


if __name__ == "__main__":
    main()
