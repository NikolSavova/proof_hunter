#!/usr/bin/env python3
"""Audit NORMALIZED_LONG_EDGE_QUOTA_AND_BLOCK_SATURATION.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import gcd, isqrt
import sys

sys.path.insert(0, "phase2/loop/erdos1208")

from verify_ambient_centroid_endpoint_difference_hypergraph_gate import (  # noqa: E402
    coordinate_height,
    endpoint_hyperedges,
    is_distance_sidon,
    norm2,
    sub,
)
from verify_closed_fibre_q_height_layered_barrier import (  # noqa: E402
    lifted_residue_parabola,
)
from verify_low_common_scale_normalized_gaussian_product import (  # noqa: E402
    determinant,
    normalized_cell,
)
from verify_transverse_closure_witness import POINTS  # noqa: E402

Point = tuple[int, int]
Edge = tuple[int, int]
Hyperedge = frozenset[Edge]


def content(vector: Point) -> int:
    return gcd(abs(vector[0]), abs(vector[1]))


def divisors(number: int) -> list[int]:
    output: list[int] = []
    for candidate in range(1, isqrt(number) + 1):
        if number % candidate:
            continue
        output.append(candidate)
        if candidate * candidate != number:
            output.append(number // candidate)
    return output


def unordered_edges(points: list[Point]) -> list[tuple[int, int]]:
    return list(combinations(range(len(points)), 2))


def edge_scale_counts(points: list[Point]) -> Counter[int]:
    counts: Counter[int] = Counter()
    for source, target in unordered_edges(points):
        vector = sub(points[target], points[source])
        for divisor in divisors(content(vector)):
            counts[divisor] += 1
    return counts


def exact_scale_and_minimum(points: list[Point], hyperedge: Hyperedge) -> tuple[int, int]:
    vectors = [sub(points[target], points[source]) for source, target in hyperedge]
    common = 0
    for vector in vectors:
        common = gcd(common, content(vector))
    assert common >= 1
    lengths = [norm2(vector) for vector in vectors]
    assert all(length % (common * common) == 0 for length in lengths)
    return common, min(lengths) // (common * common)


def matching_block(hyperedge: Hyperedge) -> frozenset[frozenset[int]]:
    source = frozenset(edge[0] for edge in hyperedge)
    target = frozenset(edge[1] for edge in hyperedge)
    assert len(source) == len(target) == 3
    assert source.isdisjoint(target)
    return frozenset((source, target))


def block_cross_edges(block: frozenset[frozenset[int]]) -> list[frozenset[int]]:
    first, second = tuple(block)
    return [frozenset((left, right)) for left in first for right in second]


def verify_quota_family(points: list[Point]) -> tuple[int, ...]:
    assert is_distance_sidon(points)
    k = len(points)
    height = coordinate_height(points)
    target = k**3 + height**2
    quota = (target + k * k - 1) // (k * k)
    scale_counts = edge_scale_counts(points)
    divisor_incidence = sum(scale_counts.values())
    direct_divisor_incidence = sum(
        len(divisors(content(sub(points[target_index], points[source_index]))))
        for source_index, target_index in unordered_edges(points)
    )
    assert divisor_incidence == direct_divisor_incidence

    hyperedges = endpoint_hyperedges(points)
    short: set[Hyperedge] = set()
    exact_scale_load: Counter[int] = Counter()
    for hyperedge in hyperedges:
        common, minimum = exact_scale_and_minimum(points, hyperedge)
        exact_scale_load[common] += 1
        if minimum <= quota:
            short.add(hyperedge)

    short_rhs = 4 * quota * divisor_incidence
    assert len(short) <= short_rhs

    sparse_mass = sum(
        load for common, load in exact_scale_load.items() if scale_counts[common] <= quota
    )
    sparse_rhs = 2 * quota * divisor_incidence
    assert sparse_mass <= sparse_rhs
    for common, load in exact_scale_load.items():
        assert load < 2 * scale_counts[common] ** 2

    blocks: defaultdict[frozenset[frozenset[int]], list[Hyperedge]] = defaultdict(list)
    for hyperedge in hyperedges:
        blocks[matching_block(hyperedge)].append(hyperedge)
    assert all(len(records) == 12 for records in blocks.values())

    saturated_blocks = {matching_block(hyperedge) for hyperedge in short}
    saturated_mass = sum(len(blocks[block]) for block in saturated_blocks)
    assert saturated_mass <= 12 * len(short)

    unsaturated = 0
    for block, records in blocks.items():
        if block in saturated_blocks:
            continue
        unsaturated += len(records)
        for edge in block_cross_edges(block):
            first, second = tuple(edge)
            assert norm2(sub(points[first], points[second])) > quota
        for hyperedge in records:
            _, minimum = exact_scale_and_minimum(points, hyperedge)
            assert minimum > quota

    return (
        k,
        height,
        len(hyperedges),
        quota,
        len(short),
        sparse_mass,
        len(blocks),
        saturated_mass,
        unsaturated,
    )


def deep_profile(prime: int) -> tuple[int, ...]:
    points = lifted_residue_parabola(prime)
    assert is_distance_sidon(points)
    height = coordinate_height(points)
    target = prime**3 + height**2
    hyperedges = endpoint_hyperedges(points)
    noncollinear = 0
    residual_core = 0
    deep = 0

    for hyperedge in hyperedges:
        cell = normalized_cell(points, hyperedge)
        if cell is None:
            continue
        noncollinear += 1
        common, area, dot = cell
        vectors = [sub(points[target_index], points[source_index]) for source_index, target_index in hyperedge]
        minimum = min(norm2(vector) // (common * common) for vector in vectors)
        in_core = (
            common**3 * target < height**4
            and (area * abs(dot)) ** 3 > height**4
            and minimum * prime**2 > target
        )
        residual_core += int(in_core)

        vertical_differences = [
            abs(points[target_index][1] - points[source_index][1])
            for source_index, target_index in hyperedge
        ]
        absolute_determinant = abs(determinant(vectors[0], vectors[1]))
        in_deep_core = (
            min(vertical_differences) ** 10 >= prime
            and absolute_determinant**10 > prime**9
            and common**20 <= prime
            and common**3 * target < height**4
            and minimum * prime**2 > target
            and (area * abs(dot)) ** 3 > height**4
        )
        deep += int(in_deep_core)

    return (
        prime,
        height,
        len(hyperedges),
        noncollinear,
        residual_core,
        deep,
    )


def main() -> None:
    quota_profiles = {
        "closure-20": verify_quota_family(list(POINTS[:20])),
        "modular-23": verify_quota_family(lifted_residue_parabola(23)),
    }
    deep_profiles = {prime: deep_profile(prime) for prime in (23, 43)}
    expected_deep = {
        23: (23, 429, 8_652, 8_588, 6_580, 3_940),
        43: (43, 1_790, 126_852, 126_462, 106_096, 80_952),
    }
    assert deep_profiles == expected_deep

    print("normalized long-edge quota and block saturation: PASS")
    print("quota profiles:", quota_profiles)
    print("deep lifted-parabola profiles:", deep_profiles)


if __name__ == "__main__":
    main()
