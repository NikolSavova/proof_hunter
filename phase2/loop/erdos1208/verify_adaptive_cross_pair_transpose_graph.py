#!/usr/bin/env python3
"""Exact verifier for the adaptive cross-pair transpose graph.

The fixed D^2 charge (u+q,w-(I+J)p) has a seven-point normal form.
Transposing a record to the fibre/primary-shift key (s,s-q) produces a
simple bipartite graph.  This script checks the normal form, the inverse
map, the exact degree moments, and the affine parallelogram forced by every
four-cycle.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
import sys

from analyze_affine_costas_energy import is_distance_sidon, welch
from analyze_cross_endpoint_pair_charge import iter_records
from verify_adaptive_cross_pair_d2_charge import inverse_linear
from verify_determinant_prime_costas_resonance import ROWS, apply
from verify_orthogonal_two_support_gate import difference_set
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    subtract,
)
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Left = tuple[Point, Point]
Right = tuple[Point, Point]
Record = tuple[Point, Point, Point, Point]
GraphProfile = tuple[int, int, int, int, int, int, int]
C4Profile = tuple[int, int, int, tuple[int, int, int, int], int, int]


def neg(value: Point) -> Point:
    return -value[0], -value[1]


def scale(coefficient: int, value: Point) -> Point:
    return coefficient * value[0], coefficient * value[1]


def quarter_turn(value: Point) -> Point:
    return -value[1], value[0]


def build_graph(
    differences: set[Point],
) -> tuple[dict[tuple[Left, Right], Record], dict[Left, list[Right]], dict[Right, list[Left]]]:
    """Build and verify the simple transpose graph.

    An edge stores (u,s,q,p), has left endpoint
        (b,ell)=(u+q,w-(I+J)p),
    and right endpoint
        (s,r)=(s,s-q).
    """
    edges: dict[tuple[Left, Right], Record] = {}
    left_adjacency: dict[Left, list[Right]] = defaultdict(list)
    right_adjacency: dict[Right, list[Left]] = defaultdict(list)

    for (base, ordinary_sum), q_forms, p_forms in iter_records(differences):
        w_value = subtract(ordinary_sum, base)
        q_value = subtract(q_forms[0], base)
        p_value = subtract(p_forms[0], base)
        b_value = q_forms[0]
        ell_value = p_forms[2]

        # Fixed-cell coordinates t=p-q and e=Jp give the seven D forms
        # b,b+t,b+t+Je, ell,ell+e,ell+e+t,ell+(I+J)t.
        t_value = subtract(p_value, q_value)
        e_value = quarter_turn(p_value)
        normal_forms = (
            b_value,
            add(b_value, t_value),
            add(add(b_value, t_value), quarter_turn(e_value)),
            ell_value,
            add(ell_value, e_value),
            add(add(ell_value, e_value), t_value),
            add(ell_value, linear(t_value)),
        )
        original_forms = (
            q_forms[0],
            p_forms[0],
            base,
            p_forms[2],
            p_forms[1],
            q_forms[1],
            q_forms[2],
        )
        assert normal_forms == original_forms
        assert all(value in differences for value in normal_forms)
        assert p_value == neg(quarter_turn(e_value))
        assert q_value == subtract(neg(quarter_turn(e_value)), t_value)
        assert q_value != p_value

        r_value = subtract(ordinary_sum, q_value)
        left = b_value, ell_value
        right = ordinary_sum, r_value

        # The edge endpoints recover the complete record.
        recovered_q = subtract(ordinary_sum, r_value)
        recovered_base = add(subtract(b_value, ordinary_sum), r_value)
        recovered_w = subtract(
            subtract(scale(2, ordinary_sum), b_value), r_value
        )
        recovered_p = inverse_linear(subtract(recovered_w, ell_value))
        assert (recovered_base, ordinary_sum, recovered_q, recovered_p) == (
            base,
            ordinary_sum,
            q_value,
            p_value,
        )

        edge = left, right
        assert edge not in edges
        edges[edge] = base, ordinary_sum, q_value, p_value
        left_adjacency[left].append(right)
        right_adjacency[right].append(left)

    return edges, left_adjacency, right_adjacency


def graph_profile(differences: set[Point]) -> tuple[
    GraphProfile,
    dict[tuple[Left, Right], Record],
    dict[Left, list[Right]],
    dict[Right, list[Left]],
]:
    edges, left_adjacency, right_adjacency = build_graph(differences)
    profile = (
        len(differences),
        len(edges),
        len(left_adjacency),
        len(right_adjacency),
        sum(len(values) ** 2 for values in left_adjacency.values()),
        sum(len(values) ** 2 for values in right_adjacency.values()),
        max((len(values) for values in right_adjacency.values()), default=0),
    )
    return profile, edges, left_adjacency, right_adjacency


def pair_codegrees(
    adjacency: dict[tuple[Point, Point], list[tuple[Point, Point]]],
) -> dict[tuple[tuple[Point, Point], tuple[Point, Point]], list[tuple[Point, Point]]]:
    common: dict[
        tuple[tuple[Point, Point], tuple[Point, Point]],
        list[tuple[Point, Point]],
    ] = defaultdict(list)
    for vertex, neighbours in adjacency.items():
        for pair in combinations(sorted(neighbours), 2):
            common[pair].append(vertex)
    return common


def c4_profile(
    edges: dict[tuple[Left, Right], Record],
    left_adjacency: dict[Left, list[Right]],
    right_adjacency: dict[Right, list[Left]],
) -> C4Profile:
    # A pair of left vertices is indexed by all of its common right vertices.
    left_pair_common_rights = pair_codegrees(right_adjacency)
    right_pair_common_lefts = pair_codegrees(left_adjacency)

    c4_count = 0
    degeneracies: Counter[tuple[bool, bool]] = Counter()
    p_quads: Counter[tuple[Point, Point, Point, Point]] = Counter()

    for (left_zero, left_one), common_rights in left_pair_common_rights.items():
        b_zero, ell_zero = left_zero
        b_one, ell_one = left_one
        beta = subtract(b_one, b_zero)
        ell_delta = subtract(ell_one, ell_zero)
        alpha = inverse_linear(neg(add(beta, ell_delta)))

        for right_zero, right_one in combinations(sorted(common_rights), 2):
            c4_count += 1
            s_zero, r_zero = right_zero
            s_one, r_one = right_one
            sigma = subtract(s_one, s_zero)
            rho = subtract(r_one, r_zero)
            eta = inverse_linear(subtract(scale(2, sigma), rho))
            p_zero = edges[left_zero, right_zero][3]

            p_values: list[Point] = []
            for i_value, left in enumerate((left_zero, left_one)):
                for j_value, right in enumerate((right_zero, right_one)):
                    base, ordinary_sum, q_value, p_value = edges[left, right]
                    expected_p = add(
                        p_zero,
                        add(scale(i_value, alpha), scale(j_value, eta)),
                    )
                    assert p_value == expected_p

                    # The right vertex fixes the primary popular shift q.
                    assert q_value == subtract(right[0], right[1])
                    # The left/right inverse remains exact at every corner.
                    assert base == add(subtract(left[0], right[0]), right[1])
                    assert ordinary_sum == right[0]
                    p_values.append(p_value)

            degeneracies[alpha == (0, 0), eta == (0, 0)] += 1
            p_quads[tuple(sorted(p_values))] += 1

    assert c4_count == sum(
        len(values) * (len(values) - 1) // 2
        for values in left_pair_common_rights.values()
    )
    degeneracy_tuple = (
        degeneracies[False, False],
        degeneracies[True, False],
        degeneracies[False, True],
        degeneracies[True, True],
    )
    return (
        c4_count,
        max((len(values) for values in left_pair_common_rights.values()), default=0),
        max((len(values) for values in right_pair_common_lefts.values()), default=0),
        degeneracy_tuple,
        len(p_quads),
        max(p_quads.values(), default=0),
    )


def transformed_costas(prime: int) -> list[Point]:
    matrix, _ = ROWS[prime]
    points = [apply(matrix, point) for point in welch(prime)]
    assert is_distance_sidon(points)
    return points


def main() -> None:
    families: list[tuple[str, set[Point], GraphProfile, C4Profile]] = [
        (
            "closure-30",
            difference_set(POINTS[:30]),
            (871, 1_420, 1_382, 1_294, 1_496, 1_724, 4),
            (0, 1, 1, (0, 0, 0, 0), 0, 0),
        ),
        (
            "closure-40",
            difference_set(POINTS[:40]),
            (1_561, 370_516, 216_909, 219_180, 1_139_274, 1_443_180, 156),
            (22_980, 7, 19, (10_512, 1_601, 10_491, 376), 3_229, 172),
        ),
        (
            "Costas-11",
            difference_set(transformed_costas(11)),
            (91, 2_264, 1_558, 1_340, 4_348, 6_612, 18),
            (61, 3, 3, (34, 23, 2, 2), 42, 8),
        ),
        (
            "Costas-17",
            difference_set(transformed_costas(17)),
            (241, 20_014, 12_397, 7_750, 46_212, 96_798, 33),
            (2_100, 6, 7, (1_320, 396, 302, 82), 305, 50),
        ),
    ]
    if "--extended" in sys.argv:
        families.append(
            (
                "Costas-23",
                difference_set(transformed_costas(23)),
                (463, 498_674, 133_927, 62_350, 3_020_644, 11_782_418, 230),
                (676_822, 12, 53, (547_140, 55_340, 67_846, 6_496), 9_712, 1_959),
            )
        )

    for name, differences, expected_graph, expected_c4 in families:
        actual_graph, edges, left_adjacency, right_adjacency = graph_profile(
            differences
        )
        assert actual_graph == expected_graph, (name, actual_graph, expected_graph)
        actual_c4 = c4_profile(edges, left_adjacency, right_adjacency)
        assert actual_c4 == expected_c4, (name, actual_c4, expected_c4)
        print(name, "graph", actual_graph, "C4", actual_c4)

    print("ADAPTIVE CROSS-PAIR TRANSPOSE GRAPH: PASS")


if __name__ == "__main__":
    main()
