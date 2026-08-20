#!/usr/bin/env python3
"""Audit LOCAL_COVOLUME_CORE_PARITY_LIFT_NO_GO.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import gcd
import sys

sys.path.insert(0, "phase2/loop/erdos1208")

from verify_ambient_centroid_endpoint_difference_hypergraph_gate import (  # noqa: E402
    coordinate_height,
    endpoint_hyperedges,
    is_distance_sidon,
    triple_cells,
)
from verify_closed_fibre_q_height_layered_barrier import (  # noqa: E402
    lifted_residue_parabola,
)

Point = tuple[int, int]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def lattice_covolume(points: list[Point]) -> int:
    assert len(points) >= 3
    origin = points[0]
    vectors = [(x - origin[0], y - origin[1]) for x, y in points[1:]]
    value = 0
    for first, second in combinations(vectors, 2):
        value = gcd(value, abs(determinant(first, second)))
    assert value > 0
    return value


def parity_core(prime: int) -> list[Point]:
    ambient = lifted_residue_parabola(prime)
    return [
        ambient[label]
        for label in range(prime)
        if (label * label % prime) % 2 == 0
    ]


def base_parity_core(prime: int) -> list[Point]:
    return [
        (label, label * label % prime)
        for label in range(prime)
        if (label * label % prime) % 2 == 0
    ]


def clean_energy_from_cells(points: list[Point]) -> tuple[int, int, int]:
    cells = triple_cells(points)
    triples = sum(len(entries) for entries in cells.values())
    ordered_collisions = sum(len(entries) * (len(entries) - 1) for entries in cells.values())
    blocks = ordered_collisions // 2
    return triples, ordered_collisions, blocks


def verify_parity_core(prime: int) -> tuple[int, ...]:
    assert prime % 4 == 1 and prime > 17
    base = base_parity_core(prime)
    points = parity_core(prime)
    size = (prime + 1) // 2
    assert len(base) == len(points) == size
    assert is_distance_sidon(points)

    base_covolume = lattice_covolume(base)
    lifted_covolume = lattice_covolume(points)
    assert base_covolume == lifted_covolume
    assert base_covolume % 2 == 0
    assert 16 % base_covolume == 0

    by_label = {point[0]: point for point in base}
    assert by_label[0] == (0, 0)
    assert by_label[2] == (2, 4)
    assert by_label[4] == (4, 16)
    assert determinant(by_label[2], by_label[4]) == 16

    triples, ordered_collisions, blocks = clean_energy_from_cells(points)
    assert triples == size * (size - 1) * (size - 2) // 6
    support_bound = (3 * prime - 2) ** 2
    cauchy_numerator = triples * triples - triples * support_bound
    assert ordered_collisions * support_bound >= cauchy_numerator

    hyperedges = endpoint_hyperedges(points)
    assert len(hyperedges) == 6 * ordered_collisions == 12 * blocks
    return (
        prime,
        size,
        coordinate_height(points),
        lifted_covolume,
        blocks,
        len(hyperedges),
    )


def block_key_covolume(points: list[Point], first: tuple[int, int, int], second: tuple[int, int, int]) -> int:
    labels = sorted(set(first) | set(second))
    assert len(labels) == 6
    return lattice_covolume([points[label] for label in labels])


def local_covolume_profiles(prime: int) -> tuple[Counter[int], Counter[int]]:
    points = lifted_residue_parabola(prime)
    block_profile: Counter[int] = Counter()
    centroid_profile: Counter[int] = Counter()
    for triples in triple_cells(points).values():
        if len(triples) < 2:
            continue
        union = sorted(set().union(*(set(triple) for triple in triples)))
        centroid_covolume = lattice_covolume([points[label] for label in union])
        centroid_profile[centroid_covolume] += len(triples) * (len(triples) - 1) // 2
        for first, second in combinations(triples, 2):
            block_profile[block_key_covolume(points, first, second)] += 1
    return block_profile, centroid_profile


def main() -> None:
    parity_profiles = {prime: verify_parity_core(prime) for prime in (29, 41, 61, 101)}
    expected_parity = {
        29: (29, 15, 829, 2, 32, 384),
        41: (41, 21, 1_672, 2, 163, 1_956),
        61: (61, 31, 3_710, 2, 1_116, 13_392),
        101: (101, 51, 10_191, 2, 10_385, 124_620),
    }
    assert parity_profiles == expected_parity

    expected_local = {
        23: (
            Counter({1: 583, 2: 107, 3: 21, 4: 8, 5: 2}),
            Counter({1: 640, 2: 61, 3: 16, 4: 4}),
        ),
        43: (
            Counter({
                1: 8_602, 2: 1_257, 3: 291, 4: 115, 5: 145,
                6: 72, 7: 33, 8: 28, 9: 2, 10: 10, 11: 10,
                12: 1, 15: 3, 19: 2,
            }),
            Counter({1: 10_246, 2: 222, 3: 55, 4: 17, 5: 7,
                     6: 10, 7: 2, 8: 8, 9: 1, 11: 3}),
        ),
    }
    actual_local = {prime: local_covolume_profiles(prime) for prime in (23, 43)}
    assert actual_local == expected_local

    print("local covolume core parity-lift no-go: PASS")
    print("parity cores:", parity_profiles)
    print(
        "local covolume-one block fractions:",
        {
            prime: round(blocks[1] / sum(blocks.values()), 6)
            for prime, (blocks, _) in actual_local.items()
        },
    )
    print(
        "centroid-core covolume-one mass fractions:",
        {
            prime: round(cells[1] / sum(cells.values()), 6)
            for prime, (_, cells) in actual_local.items()
        },
    )


if __name__ == "__main__":
    main()
