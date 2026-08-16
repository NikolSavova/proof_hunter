#!/usr/bin/env python3
"""Exact audit for ORDERED_HYPERGRAPH_PROMOTION_AUDIT.md."""

from __future__ import annotations

import json
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb, factorial


Point = tuple[Q, Q]


def cross(a: Point, b: Point, c: Point) -> Q:
    return (b[0] - a[0]) * (c[1] - a[1]) - (
        b[1] - a[1]
    ) * (c[0] - a[0])


def convex_hull(points: list[Point]) -> list[Point]:
    ordered = sorted(set(points))
    if len(ordered) <= 1:
        return ordered

    def half(sequence) -> list[Point]:
        output: list[Point] = []
        for point in sequence:
            while (
                len(output) >= 2
                and cross(output[-2], output[-1], point) <= 0
            ):
                output.pop()
            output.append(point)
        return output

    return half(ordered)[:-1] + half(reversed(ordered))[:-1]


def convex(points: list[Point]) -> bool:
    return len(points) == len(set(points)) == len(convex_hull(points))


def tangent_point(left: int | Q, right: int | Q) -> Point:
    left, right = Q(left), Q(right)
    return ((left - right) / (left + right), Q(-2) / (left + right))


def within_power(value: Q, exponent: int) -> bool:
    return Q(1, 1 << exponent) <= value <= Q(1 << exponent)


def parameter_audit() -> dict[str, object]:
    rows = []
    for log_n in (16, 32, 64, 128):
        k = log_n // 4
        r = 2 * k
        n = 1 << log_n
        alpha = k
        constant_sum = sum(
            comb(2 * k - 2, j) for j in range(k, min(r, 2 * k - 2) + 1)
        )
        component_prefactor = Q(constant_sum, factorial(k - 1))
        # alpha=k makes 1-2^(k-1-alpha)=1/2 exactly.
        extraction_constant = Q(factorial(k - 1), 2 * constant_sum)
        double_factor = extraction_constant**2 / r**alpha

        total_component_bound = component_prefactor * sum(
            1 << (scale * (k - 1)) for scale in range(log_n + 1)
        )
        family = n**alpha
        average = Q(family) / total_component_bound
        subquadratic_budget = log_n * (log_n.bit_length() + 2)

        assert total_component_bound < family
        assert average >= (1 << (log_n // 2))
        assert average <= (1 << subquadratic_budget)
        assert within_power(extraction_constant, subquadratic_budget)
        assert within_power(double_factor, subquadratic_budget)

        rows.append(
            {
                "log_n": log_n,
                "k": k,
                "r": r,
                "constant_sum_bits": constant_sum.bit_length(),
                "factorial_bits": factorial(k - 1).bit_length(),
                "component_average_num_bits": average.numerator.bit_length(),
                "component_average_den_bits": average.denominator.bit_length(),
                "double_factor_num_bits": double_factor.numerator.bit_length(),
                "double_factor_den_bits": double_factor.denominator.bit_length(),
                "subquadratic_budget": subquadratic_budget,
            }
        )
    return {"scales": rows}


def interval_r_threshold_audit() -> dict[str, object]:
    rows = []
    for log_n in (32, 64, 128):
        n = 1 << log_n
        r = log_n // 2
        assert factorial(r) > n
        assert comb(n, r) < n ** (r - 1)
        rows.append(
            {
                "log_n": log_n,
                "r": r,
                "factorial_bits": factorial(r).bit_length(),
                "n_bits": n.bit_length(),
            }
        )
    return {"scales": rows}


def cup_cap_counterexample_audit() -> dict[str, object]:
    u, v = (Q(-1), Q(0)), (Q(1), Q(0))
    left_coordinates = ((2, 22), (9, 13), (17, 4))
    right_coordinates = ((3, 23), (10, 14), (18, 5))
    first = tuple(tangent_point(*pair) for pair in left_coordinates)
    second = tuple(tangent_point(*pair) for pair in right_coordinates)
    ambient = [u, v, *first, *second]

    assert len(set(ambient)) == 8
    assert all(cross(*triple) != 0 for triple in combinations(ambient, 3))
    assert convex([u, *first, v])
    assert convex([u, *second, v])

    # Each indexed cell is strictly before the next in L and strictly after
    # it in R, for both available points.
    cells = [
        (left_coordinates[index], right_coordinates[index]) for index in range(3)
    ]
    for earlier, later in zip(cells, cells[1:]):
        assert max(pair[0] for pair in earlier) < min(pair[0] for pair in later)
        assert min(pair[1] for pair in earlier) > max(pair[1] for pair in later)

    convex_words = []
    for bits in product((0, 1), repeat=3):
        transversal = [
            (first[index], second[index])[bit] for index, bit in enumerate(bits)
        ]
        if convex([u, *transversal, v]):
            convex_words.append(bits)

    mixed = (0, 1, 0)
    assert mixed not in convex_words
    assert (0, 0, 0) in convex_words and (1, 1, 1) in convex_words
    assert len(convex_words) == 5
    return {
        "ambient_points": len(ambient),
        "general_position_triples": comb(len(ambient), 3),
        "ambient_transversals": 8,
        "convex_transversals": len(convex_words),
        "nonconvex_mixed_word": mixed,
    }


def rational_circle_point(parameter: Q) -> Point:
    # tangent coordinates (t,1/t) give the rational lower unit circle.
    return tangent_point(parameter, 1 / parameter)


def erased_component_audit() -> dict[str, object]:
    # A literal small planar realization of the finest-scale construction.
    n, k = 16, 4
    points = [rational_circle_point(Q(index + 1)) for index in range(n)]
    fixed_output = frozenset((0,))
    edges = []
    for chosen_pairs in combinations(range(1, n // 2), k - 2):
        edge = frozenset((0, 1, *(2 * pair for pair in chosen_pairs)))
        assert len(edge) == k
        parent_pairs = {vertex // 2 for vertex in edge}
        assert len(parent_pairs) == k - 1
        assert convex([points[vertex] for vertex in edge])
        edges.append(edge)
    assert len(edges) == len(set(edges)) == comb(n // 2 - 1, k - 2) == 21
    assert all(fixed_output <= edge for edge in edges)

    scales = []
    for log_n in (16, 32, 64):
        n_large = 1 << log_n
        k_large = log_n // 4
        reuse = comb(n_large // 2 - 1, k_large - 2)
        assert reuse >= comb(n_large // 4, k_large - 2)
        scales.append(
            {
                "log_n": log_n,
                "k": k_large,
                "component_reuse_bits": reuse.bit_length(),
            }
        )
    return {
        "small_n": n,
        "small_k": k,
        "components_reusing_single_face": len(edges),
        "scales": scales,
    }


def multiply_occupied_residual_audit() -> dict[str, object]:
    # Small rooted planar model: eight variable points in one tangent cell,
    # then two later anchors, all on the same lower rational circle.
    variable_count, k = 8, 3
    variables_t = [Q(1) + Q(index + 1, variable_count + 1) for index in range(variable_count)]
    anchors_t = [Q(3), Q(4)]
    u, v = (Q(-1), Q(0)), (Q(1), Q(0))
    support = [rational_circle_point(t) for t in (*variables_t, *anchors_t)]
    assert convex([u, *support, v])

    sources = []
    for choice in combinations(range(variable_count), k):
        source = frozenset((*choice, variable_count, variable_count + 1))
        assert len(source) == 2 * k - 1
        assert convex([u, *(support[index] for index in source), v])
        sources.append(source)
    assert len(sources) == comb(variable_count, k) == 56
    projections = {
        frozenset((index, variable_count, variable_count + 1))
        for index in range(variable_count)
    }
    assert len(projections) == variable_count == 8

    scales = []
    for log_n in (16, 32, 64):
        alphabet = 1 << log_n
        macro_parts = log_n // 4
        family = comb(alphabet, macro_parts)
        host = alphabet + macro_parts + 1
        assert host ** (macro_parts - 1) < family < host**macro_parts
        projection_loss = family // alphabet
        assert projection_loss >= alphabet ** (macro_parts - 2)
        scales.append(
            {
                "log_alphabet": log_n,
                "macro_parts": macro_parts,
                "rank": 2 * macro_parts - 1,
                "host_vertices": host,
                "family_bits": family.bit_length(),
                "one_per_part_projection_bits": alphabet.bit_length(),
                "projection_loss_bits": projection_loss.bit_length(),
            }
        )
    return {
        "small_sources": len(sources),
        "small_projections": len(projections),
        "small_rank": 2 * k - 1,
        "scales": scales,
    }


def main() -> None:
    result = {
        "parameters": parameter_audit(),
        "interval_r_threshold": interval_r_threshold_audit(),
        "cup_cap_counterexample": cup_cap_counterexample_audit(),
        "erased_component_reuse": erased_component_audit(),
        "multiply_occupied_residual": multiply_occupied_residual_audit(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: ordered-hypergraph promotion constants and exact barriers verified")


if __name__ == "__main__":
    main()
