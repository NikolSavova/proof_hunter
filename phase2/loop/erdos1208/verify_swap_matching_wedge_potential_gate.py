#!/usr/bin/env python3
"""Exact checks for SWAP_MATCHING_WEDGE_POTENTIAL_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product

from analyze_affine_costas_energy import is_distance_sidon
from analyze_swap_optimal_nested_cores import profile, transformed_costas
from verify_seven_incidence_opposite_endpoint_charge import linear, subtract


Point = tuple[int, int]
Cell = tuple[Point, Point]


PLANTED = [
    (-47, -42),
    (33, -1),
    (21, 21),
    (31, -55),
    (12, -1),
    (-15, 30),
    (39, 121),
    (-48, -72),
]


def endpoint_map(points: list[Point]) -> dict[Point, tuple[Point, Point]]:
    output: dict[Point, tuple[Point, Point]] = {}
    for head in points:
        for tail in points:
            if head == tail:
                continue
            value = subtract(head, tail)
            assert value not in output
            output[value] = head, tail
    return output


def invariant(cell: Cell) -> Point:
    return subtract(cell[1], linear(cell[0]))


def potential(
    cell: Cell,
    endpoints: dict[Point, tuple[Point, Point]],
) -> tuple[Point, Point]:
    x_b, y_b = endpoints[cell[0]]
    x_ell, y_ell = endpoints[cell[1]]
    alpha = subtract(x_ell, linear(x_b))
    beta = subtract(y_ell, linear(y_b))
    assert subtract(alpha, beta) == invariant(cell)
    return alpha, beta


def verify_clean_potential_injection(points: list[Point]) -> tuple[int, int, int]:
    """Exhaustively verify the ordered clean-pair injection."""

    assert is_distance_sidon(points)
    endpoints = endpoint_map(points)
    cells = list(product(endpoints, repeat=2))
    fibres: dict[tuple[Point, Point], list[Cell]] = defaultdict(list)
    for cell in cells:
        alpha, _ = potential(cell, endpoints)
        fibres[invariant(cell), alpha].append(cell)

    p_linear = {value for value in endpoints if linear(value) in endpoints}
    images: dict[tuple[Point, Point], tuple[Cell, Cell]] = {}
    clean_pairs = 0
    for fibre in fibres.values():
        for first in fibre:
            for second in fibre:
                if first == second:
                    continue
                physical = (
                    endpoints[first[0]]
                    + endpoints[first[1]]
                    + endpoints[second[0]]
                    + endpoints[second[1]]
                )
                if len(set(physical)) != 8:
                    continue

                first_alpha, first_beta = potential(first, endpoints)
                second_alpha, second_beta = potential(second, endpoints)
                assert first_alpha == second_alpha
                assert first_beta == second_beta

                d_x = subtract(endpoints[second[0]][0], endpoints[first[0]][0])
                d_y = subtract(endpoints[second[0]][1], endpoints[first[0]][1])
                assert d_x in p_linear and d_y in p_linear
                image = d_x, d_y
                previous = images.setdefault(image, (first, second))
                assert previous == (first, second)
                clean_pairs += 1

    assert clean_pairs == len(images)
    assert clean_pairs <= len(p_linear) ** 2
    return len(p_linear), clean_pairs, max(map(len, fibres.values()), default=0)


def verify_wedge_inequality() -> None:
    # A loopless multigraph with edge-copy multiplicities 3, 2, 1.
    edges = {(0, 1): 3, (0, 2): 2, (1, 2): 1}
    degrees = Counter()
    edge_mass = 0
    for (first, second), multiplicity in edges.items():
        degrees[first] += multiplicity
        degrees[second] += multiplicity
        edge_mass += multiplicity
    wedges = sum(value * (value - 1) // 2 for value in degrees.values())
    vertices = len(degrees)
    assert (edge_mass, tuple(degrees[index] for index in range(3)), wedges) == (
        6,
        (5, 4, 3),
        19,
    )
    assert wedges >= 2 * edge_mass * edge_mass / vertices - edge_mass

    # This is the only graph-theoretic input used in the sufficient wedge
    # reduction: |U_t| <= E/t.
    level = 4
    orientation_mass = 20
    assert level * vertices <= orientation_mass
    assert wedges >= 2 * level * edge_mass * edge_mass / orientation_mass - edge_mass


def verify_genuine_profiles() -> None:
    expected = {
        11: (("parallel", 4),),
        17: (
            ("parallel", 428),
            ("diffuse-neighbour-contact", 120),
            ("diffuse-twelve-distinct", 10),
            ("missing-potential", 6),
            ("repeated-potential", 3),
        ),
    }
    for prime, target in expected.items():
        points, differences = transformed_costas(prime)
        _, summary, _ = profile(differences, points)
        assert summary["matching_wedges"] == target


def main() -> None:
    p_size, clean_pairs, maximum_fibre = verify_clean_potential_injection(PLANTED)
    assert (p_size, clean_pairs, maximum_fibre) == (4, 8, 4)
    verify_wedge_inequality()
    verify_genuine_profiles()
    print(
        "SWAP MATCHING-WEDGE POTENTIAL GATE: PASS",
        (p_size, clean_pairs, maximum_fibre),
    )


if __name__ == "__main__":
    main()
