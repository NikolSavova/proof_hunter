#!/usr/bin/env python3
"""Exact checks for LARGE_DETERMINANT_CLOSED_FIBRE_ENERGY_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from math import comb, gcd
import sys

sys.path.insert(0, "phase2/loop/erdos1208")

from verify_ambient_centroid_endpoint_difference_hypergraph_gate import (  # noqa: E402
    centroid_matching_determinant_profile,
    directed_edges,
    primitive_unoriented,
    residue_parabola,
    shear,
)

Point = tuple[int, int]
Direction = tuple[int, int]
Edge = tuple[int, int]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def extended_gcd_nonnegative(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    divisor, x, y = extended_gcd_nonnegative(b, a % b)
    return divisor, y, x - (a // b) * y


def unimodular_partner(direction: Direction) -> Point:
    """Return v with det(direction, v)=1."""
    x, y = direction
    divisor, coefficient_x, coefficient_y = extended_gcd_nonnegative(
        abs(x), abs(y)
    )
    assert divisor == 1
    if x < 0:
        coefficient_x = -coefficient_x
    if y < 0:
        coefficient_y = -coefficient_y
    partner = (-coefficient_y, coefficient_x)
    assert determinant(direction, partner) == 1
    return partner


def direction_fibres(
    points: list[Point],
) -> tuple[
    dict[Point, Edge],
    dict[Direction, set[int]],
    dict[Direction, Point],
    dict[Direction, dict[int, set[int]]],
]:
    _, by_vector = directed_edges(points)
    differences = set(by_vector)
    contents: dict[Direction, set[int]] = defaultdict(set)
    for vector in differences:
        direction = primitive_unoriented(vector)
        content = gcd(abs(vector[0]), abs(vector[1]))
        contents[direction].add(content)

    partners: dict[Direction, Point] = {}
    fibres: dict[Direction, dict[int, set[int]]] = {}
    for direction in contents:
        partner = unimodular_partner(direction)
        partners[direction] = partner
        direction_fibre: dict[int, set[int]] = defaultdict(set)
        for vector in differences:
            residue = determinant(direction, vector)
            longitudinal = determinant(vector, partner)
            rebuilt = (
                longitudinal * direction[0] + residue * partner[0],
                longitudinal * direction[1] + residue * partner[1],
            )
            assert rebuilt == vector
            direction_fibre[residue].add(longitudinal)

        assert sum(map(len, direction_fibre.values())) == len(differences)
        for residue, fibre in direction_fibre.items():
            assert direction_fibre[-residue] == {-value for value in fibre}
        assert direction_fibre[0] == {
            sign * content
            for content in contents[direction]
            for sign in (-1, 1)
        }
        fibres[direction] = direction_fibre

    return by_vector, contents, partners, fibres


def fibre_band_statistics(
    points: list[Point],
) -> tuple[dict[int, tuple[int, int, int, int]], int]:
    by_vector, contents, partners, fibres = direction_fibres(points)
    determinant_profile = centroid_matching_determinant_profile(points)
    N = len(by_vector)

    # Include bands that contribute only to the relaxed fibre functional.
    # Stopping at the largest clean determinant omitted a terminal Q-only
    # band in the p=43 stress.
    maximum_scale = max(
        content * abs(residue)
        for direction, direction_contents in contents.items()
        for residue in fibres[direction]
        if residue
        for content in direction_contents
    )
    cutoffs: list[int] = []
    cutoff = 1
    while cutoff <= maximum_scale:
        cutoffs.append(cutoff)
        cutoff *= 2

    output: dict[int, tuple[int, int, int, int]] = {}
    for cutoff in cutoffs:
        hyperedges = sum(
            load
            for value, load in determinant_profile.items()
            if cutoff <= value < 2 * cutoff
        )
        clean_closure = 0
        unrestricted_closure = 0
        minimum_relaxation = 0

        for direction, direction_contents in contents.items():
            partner = partners[direction]
            for residue, fibre in fibres[direction].items():
                selected_contents = [
                    content
                    for content in direction_contents
                    if cutoff <= content * abs(residue) < 2 * cutoff
                ]
                fibre_size = len(fibre)
                minimum_relaxation += min(
                    comb(fibre_size, 2),
                    fibre_size * len(selected_contents),
                )

                for content in selected_contents:
                    first = (
                        content * direction[0],
                        content * direction[1],
                    )
                    for longitudinal in fibre:
                        if longitudinal + content not in fibre:
                            continue
                        unrestricted_closure += 1
                        second = (
                            longitudinal * direction[0]
                            + residue * partner[0],
                            longitudinal * direction[1]
                            + residue * partner[1],
                        )
                        third = (
                            -first[0] - second[0],
                            -first[1] - second[1],
                        )
                        assert first in by_vector
                        assert second in by_vector
                        assert third in by_vector
                        endpoints = (
                            by_vector[first]
                            + by_vector[second]
                            + by_vector[third]
                        )
                        clean_closure += len(set(endpoints)) == 6

        # Positive first-vector orientations contribute exactly half of
        # all six ordered choices, after pairing every hyperedge with its
        # reversal.
        assert clean_closure == 3 * hyperedges
        assert clean_closure <= unrestricted_closure <= minimum_relaxation

        # The two endpoint universal estimates in the note.
        assert 3 * hyperedges * hyperedges <= 2 * cutoff * N**3
        assert 6 * hyperedges <= N * (N - 1)

        output[cutoff] = (
            hyperedges,
            clean_closure,
            unrestricted_closure,
            minimum_relaxation,
        )

    return output, N


def main() -> None:
    small, small_N = fibre_band_statistics(shear(residue_parabola(7), 4))
    assert small_N == 42
    assert small == {
        1: (0, 0, 36, 54),
        2: (6, 18, 72, 124),
        4: (6, 18, 96, 158),
        8: (12, 36, 102, 138),
        16: (0, 0, 12, 14),
    }

    stress, N = fibre_band_statistics(shear(residue_parabola(43), 28))
    assert N == 1_806
    assert stress == {
        1: (446, 1_338, 1_590, 2_468),
        2: (1_006, 3_018, 4_008, 6_848),
        4: (2_034, 6_102, 8_028, 14_526),
        8: (4_258, 12_774, 16_236, 29_534),
        16: (8_648, 25_944, 32_826, 58_962),
        32: (15_514, 46_542, 59_628, 110_770),
        64: (25_066, 75_198, 97_872, 189_372),
        128: (31_370, 94_110, 121_980, 250_432),
        256: (27_520, 82_560, 107_742, 222_504),
        512: (10_236, 30_708, 42_708, 94_340),
        1_024: (364, 1_092, 2_796, 8_564),
        2_048: (0, 0, 0, 8),
    }

    print("large determinant closed fibre energy gate: PASS")
    print("p=7:", small)
    print("p=43:", stress)


if __name__ == "__main__":
    main()
