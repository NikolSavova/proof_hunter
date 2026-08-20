#!/usr/bin/env python3
"""Verify LOW_COMMON_SCALE_NORMALIZED_GAUSSIAN_PRODUCT_GATE.md."""

from __future__ import annotations

from collections import Counter
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
from verify_global_directional_short_compensator_no_go import (  # noqa: E402
    balanced_transform,
)
from verify_transverse_closure_witness import POINTS  # noqa: E402

Point = tuple[int, int]
Edge = tuple[int, int]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def content(vector: Point) -> int:
    return gcd(abs(vector[0]), abs(vector[1]))


def divisor_count(number: int) -> int:
    output = 1
    prime = 2
    residue = number
    while prime * prime <= residue:
        if residue % prime:
            prime += 1
            continue
        exponent = 0
        while residue % prime == 0:
            residue //= prime
            exponent += 1
        output *= exponent + 1
        prime += 1
    if residue > 1:
        output *= 2
    return output


def normalized_cell(
    points: list[Point], hyperedge: frozenset[Edge]
) -> tuple[int, int, int] | None:
    vectors = [sub(points[target], points[source]) for source, target in hyperedge]
    assert (
        sum(vector[0] for vector in vectors),
        sum(vector[1] for vector in vectors),
    ) == (0, 0)
    area = abs(determinant(vectors[0], vectors[1]))
    if not area:
        return None

    vectors.sort(key=norm2)
    lengths = [norm2(vector) for vector in vectors]
    assert lengths[0] < lengths[1] < lengths[2]
    contents = [content(vector) for vector in vectors]
    common = gcd(gcd(contents[0], contents[1]), contents[2])
    assert area % (common * common) == 0

    dot = (
        vectors[0][0] * vectors[1][0]
        + vectors[0][1] * vectors[1][1]
    )
    assert dot % (common * common) == 0
    normalized_area = area // (common * common)
    normalized_dot = dot // (common * common)
    first_length = lengths[0] // (common * common)
    second_length = lengths[1] // (common * common)
    assert (
        first_length * second_length
        == normalized_dot * normalized_dot
        + normalized_area * normalized_area
    )
    return common, normalized_area, normalized_dot


def profile(points: list[Point]) -> tuple[int, ...]:
    assert is_distance_sidon(points)
    primitive_area: Counter[tuple[int, int]] = Counter()
    gaussian: Counter[tuple[int, int, int]] = Counter()
    low_product = 0
    height = coordinate_height(points)

    for hyperedge in endpoint_hyperedges(points):
        cell = normalized_cell(points, hyperedge)
        if cell is None:
            continue
        common, area, dot = cell
        primitive_area[(common, area)] += 1
        gaussian[cell] += 1
        if (area * abs(dot)) ** 3 <= height**4:
            low_product += 1

    for (common, area, dot), load in gaussian.items():
        assert load <= 24 * divisor_count(dot * dot + area * area)
        assert area <= 2 * height * height // (common * common)
        assert abs(dot) <= 2 * height * height // (common * common)

    mass = sum(gaussian.values())
    return (
        len(points),
        height,
        mass,
        len(primitive_area),
        max(primitive_area.values(), default=0),
        len(gaussian),
        max(gaussian.values(), default=0),
        sum(load * load for load in gaussian.values()),
        low_product,
    )


def verify_product_cell_count() -> None:
    # Direct finite audit of the counting argument for moderate boxes.
    for height in (8, 15, 30, 60):
        threshold = height ** (4 / 3)
        cells = 0
        zero_dot = 0
        for common in range(1, isqrt(2) * height + 2):
            maximum = 2 * height * height // (common * common)
            zero_dot += maximum
            for area in range(1, maximum + 1):
                bound = min(maximum, int(threshold // area))
                cells += 2 * bound
        cells += zero_dot
        # The proof gives an absolute-constant O(m^2+mY^(3/4)) bound.
        assert cells <= 100 * height * height


def main() -> None:
    families = {
        "closure-20": list(POINTS[:20]),
        "closure-40": list(POINTS[:40]),
        "modular-23": lifted_residue_parabola(23),
        "modular-43": lifted_residue_parabola(43),
        "balanced-23": balanced_transform(
            [(x, (x * x) % 23) for x in range(23)], 20
        ),
    }
    expected = {
        "closure-20": (20, 75, 432, 187, 6, 215, 4, 872, 54),
        "closure-40": (40, 223, 8_274, 2_752, 24, 4_130, 4, 16_604, 346),
        "modular-23": (23, 429, 8_588, 278, 156, 4_211, 4, 17_840, 402),
        "modular-43": (
            43,
            1_790,
            126_462,
            1_412,
            664,
            62_005,
            8,
            262_940,
            2_656,
        ),
        "balanced-23": (23, 439, 8_588, 278, 156, 4_216, 4, 17_800, 0),
    }
    actual = {name: profile(points) for name, points in families.items()}
    assert actual == expected
    verify_product_cell_count()

    print("low-common-scale normalized Gaussian product gate: PASS")
    print(
        "profiles:",
        {
            name: {
                "mass": row[2],
                "primitive_area_max": row[4],
                "gaussian_max": row[6],
                "normalized_energy": round(row[7] / row[2], 6),
                "low_product": row[8],
            }
            for name, row in actual.items()
        },
    )


if __name__ == "__main__":
    main()
