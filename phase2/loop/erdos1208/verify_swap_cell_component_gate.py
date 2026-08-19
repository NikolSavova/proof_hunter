#!/usr/bin/env python3
"""Exact verifier for the swap-cell component gate in Erdős 1208."""

from __future__ import annotations

from collections import Counter, defaultdict

from analyze_affine_costas_energy import is_distance_sidon, welch
from analyze_cross_endpoint_pair_charge import iter_records
from verify_determinant_prime_costas_resonance import ROWS, apply
from verify_orthogonal_two_support_gate import difference_set
from verify_radial_orthogonal_product_barrier import radial_set
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rotate,
    rich_fibres,
    subtract,
)
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Cell = tuple[Point, Point]
Edge = tuple[Cell, Cell]
Profile = tuple[int, int, int, int, int, int, int, int, int, int]


def cell_invariant(cell: Cell) -> Point:
    b_value, ell_value = cell
    return subtract(ell_value, linear(b_value))


def swap_profile(differences: set[Point]) -> Profile:
    edge_multiplicity: Counter[Edge] = Counter()
    edge_parameters: dict[Edge, set[Point]] = defaultdict(set)
    ordered_mass = 0

    for (base, ordinary_sum), q_forms, p_forms in iter_records(differences):
        w_value = subtract(ordinary_sum, base)
        q_value = subtract(q_forms[0], base)
        p_value = subtract(p_forms[0], base)
        t_value = subtract(p_value, q_value)
        e_value = rotate(p_value)

        first_cell = q_forms[0], p_forms[2]
        second_cell = p_forms[0], q_forms[2]
        assert first_cell != second_cell
        assert second_cell == (
            add(first_cell[0], t_value),
            add(first_cell[1], linear(t_value)),
        )
        assert cell_invariant(first_cell) == cell_invariant(second_cell)

        # For a fixed unordered swap edge, only e varies.  Its three moving
        # D-members are b+t+Je, ell+e, and ell+e+t.
        b_value, ell_value = first_cell
        moving = (
            add(add(b_value, t_value), rotate(e_value)),
            add(ell_value, e_value),
            add(add(ell_value, e_value), t_value),
        )
        assert moving == (base, p_forms[1], q_forms[1])
        assert all(value in differences for value in moving)

        edge = tuple(sorted((first_cell, second_cell)))
        if first_cell < second_cell:
            # The swapped ordered record supplies the other orientation, so
            # count the undirected edge exactly once.
            assert e_value not in edge_parameters[edge]
            edge_parameters[edge].add(e_value)
            edge_multiplicity[edge] += 1
        ordered_mass += 1

    assert ordered_mass == 2 * sum(edge_multiplicity.values())
    assert all(
        multiplicity == len(edge_parameters[edge])
        for edge, multiplicity in edge_multiplicity.items()
    )

    degrees: Counter[Cell] = Counter()
    component_vertices: dict[Point, set[Cell]] = defaultdict(set)
    component_multiplicities: dict[Point, list[int]] = defaultdict(list)
    for (first_cell, second_cell), multiplicity in edge_multiplicity.items():
        invariant = cell_invariant(first_cell)
        assert invariant == cell_invariant(second_cell)
        degrees[first_cell] += multiplicity
        degrees[second_cell] += multiplicity
        component_vertices[invariant].update((first_cell, second_cell))
        component_multiplicities[invariant].append(multiplicity)

    assert sum(degrees.values()) == ordered_mass
    degree_moment = sum(value * value for value in degrees.values())
    parallel_moment = sum(
        value * value for value in edge_multiplicity.values()
    )

    # For a vertex in a component of size h, Cauchy over its at most h-1
    # distinct neighbours gives d(v)^2 <= (h-1) sum_w m(v,w)^2.
    # Summing counts every undirected parallel class twice.
    component_envelope = 2 * sum(
        (len(component_vertices[invariant]) - 1)
        * sum(value * value for value in multiplicities)
        for invariant, multiplicities in component_multiplicities.items()
    )
    assert degree_moment <= component_envelope

    _, support, _ = rich_fibres(differences, adaptive=True)
    return (
        len(differences),
        support,
        ordered_mass,
        len(degrees),
        len(component_vertices),
        max((len(values) for values in component_vertices.values()), default=0),
        max(edge_multiplicity.values(), default=0),
        degree_moment,
        parallel_moment,
        component_envelope,
    )


def transformed_costas(prime: int) -> set[Point]:
    matrix, _ = ROWS[prime]
    points = [apply(matrix, point) for point in welch(prime)]
    assert is_distance_sidon(points)
    return difference_set(points)


def main() -> None:
    families: list[tuple[str, set[Point], Profile]] = [
        (
            "closure-30",
            difference_set(POINTS[:30]),
            (871, 62_273, 1_420, 1_382, 664, 4, 2, 1_496, 734, 1_732),
        ),
        (
            "closure-40",
            difference_set(POINTS[:40]),
            (
                1_561,
                156_057,
                370_516,
                216_909,
                41_293,
                47,
                6,
                1_139_274,
                212_806,
                5_602_992,
            ),
        ),
        (
            "Costas-11",
            transformed_costas(11),
            (91, 707, 2_264, 1_558, 648, 6, 4, 4_348, 1_432, 6_188),
        ),
        (
            "Costas-17",
            transformed_costas(17),
            (
                241,
                2_299,
                20_014,
                12_397,
                5_057,
                7,
                5,
                46_212,
                14_343,
                62_000,
            ),
        ),
        (
            "Costas-23",
            transformed_costas(23),
            (
                463,
                4_513,
                498_674,
                133_927,
                41_481,
                11,
                7,
                3_020_644,
                547_433,
                4_087_164,
            ),
        ),
        (
            "radial-4",
            radial_set(4),
            (29, 121, 8_330, 773, 177, 9, 6, 111_622, 15_213, 136_252),
        ),
        (
            "radial-5",
            radial_set(5),
            (39, 181, 24_716, 1_437, 283, 12, 9, 562_304, 56_274, 686_344),
        ),
        (
            "radial-6",
            radial_set(6),
            (
                53,
                253,
                93_290,
                2_715,
                423,
                16,
                12,
                4_120_768,
                304_937,
                4_861_720,
            ),
        ),
    ]

    for name, differences, expected in families:
        actual = swap_profile(differences)
        assert actual == expected, (name, actual, expected)
        number, support, mass, _, _, h_max, m_max, moment, _, envelope = actual
        adaptive_k = support / number
        print(
            name,
            actual,
            "moment/(K mass)",
            moment / (adaptive_k * mass) if mass else 0.0,
            "envelope/(K mass)",
            envelope / (adaptive_k * mass) if mass else 0.0,
            "hmax*mmax/K",
            h_max * m_max / adaptive_k if adaptive_k else 0.0,
        )

    print("SWAP-CELL COMPONENT GATE: PASS")


if __name__ == "__main__":
    main()
