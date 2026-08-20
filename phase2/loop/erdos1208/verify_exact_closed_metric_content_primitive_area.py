#!/usr/bin/env python3
"""Verify EXACT_CLOSED_METRIC_CONTENT_PRIMITIVE_AREA_GATE.md."""

from __future__ import annotations

from collections import Counter
from math import gcd, pi
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


def primitive(vector: Point) -> Point:
    divisor = content(vector)
    return vector[0] // divisor, vector[1] // divisor


def triple_data(points: list[Point], hyperedge: frozenset[Edge]):
    vectors = [sub(points[target], points[source]) for source, target in hyperedge]
    assert (
        sum(vector[0] for vector in vectors),
        sum(vector[1] for vector in vectors),
    ) == (0, 0)

    contents = [content(vector) for vector in vectors]
    lengths = [norm2(vector) for vector in vectors]
    area = abs(determinant(vectors[0], vectors[1]))
    assert area
    common_scale = gcd(gcd(contents[0], contents[1]), contents[2])
    assert area % (common_scale * common_scale) == 0

    for index in range(3):
        other = (index + 1) % 3
        last = (index + 2) % 3
        assert (lengths[other] - lengths[last]) % contents[index] == 0
        assert area % (contents[index] * contents[other]) == 0

    heron = 2 * (
        lengths[0] * lengths[1]
        + lengths[1] * lengths[2]
        + lengths[2] * lengths[0]
    ) - sum(length * length for length in lengths)
    assert heron == 4 * area * area

    directions = [primitive(vector) for vector in vectors]
    minors = [
        determinant(directions[1], directions[2]),
        determinant(directions[2], directions[0]),
        determinant(directions[0], directions[1]),
    ]
    minor_gcd = gcd(gcd(abs(minors[0]), abs(minors[1])), abs(minors[2]))
    assert minor_gcd
    primitive_kernel = [value // minor_gcd for value in minors]
    signed_contents = []
    for index in range(3):
        assert primitive_kernel[index]
        quotient = contents[index] // abs(primitive_kernel[index])
        assert quotient == common_scale
        signed_contents.append(
            common_scale * primitive_kernel[index]
        )
    assert (
        sum(signed_contents[i] * directions[i][0] for i in range(3)),
        sum(signed_contents[i] * directions[i][1] for i in range(3)),
    ) == (0, 0)

    return common_scale, area // (common_scale * common_scale)


def profile(points: list[Point]):
    assert is_distance_sidon(points)
    hyperedges = []
    for hyperedge in endpoint_hyperedges(points):
        edges = list(hyperedge)
        first = sub(points[edges[0][1]], points[edges[0][0]])
        second = sub(points[edges[1][1]], points[edges[1][0]])
        if determinant(first, second):
            hyperedges.append(hyperedge)
    charges: Counter[tuple[int, int]] = Counter()
    scales: Counter[int] = Counter()
    for hyperedge in hyperedges:
        charge = triple_data(points, hyperedge)
        charges[charge] += 1
        scales[charge[0]] += 1

    height = coordinate_height(points)
    range_bound = sum(
        2 * height * height // (scale * scale)
        for scale in range(1, int((2**0.5) * height) + 1)
    )
    assert len(charges) <= range_bound
    assert range_bound <= (pi * pi / 3) * height * height

    directed = [
        sub(points[target], points[source])
        for source in range(len(points))
        for target in range(len(points))
        if source != target
    ]
    directed_contents = [content(vector) for vector in directed]
    maximum_scale = max(scales, default=0)
    for threshold in range(1, maximum_scale + 2):
        actual = sum(load for scale, load in scales.items() if scale >= threshold)
        envelope = 0
        for divisor in range(threshold, 2 * height + 1):
            divisible = sum(value % divisor == 0 for value in directed_contents)
            radius_bound = 4 * height * height // (divisor * divisor)
            assert divisible <= min(len(directed), radius_bound)
            envelope += divisible * divisible
        assert actual <= envelope

    return (
        len(points),
        height,
        len(hyperedges),
        len(charges),
        max(charges.values(), default=0),
        sum(load * load for load in charges.values()),
        maximum_scale,
    )


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
        "closure-20": (20, 75, 432, 187, 6, 1_128, 4),
        "closure-40": (40, 223, 8_274, 2_752, 24, 36_044, 11),
        "modular-23": (23, 429, 8_588, 278, 156, 624_344, 5),
        "modular-43": (43, 1_790, 126_462, 1_412, 664, 36_074_756, 15),
        "balanced-23": (23, 439, 8_588, 278, 156, 624_344, 5),
    }

    actual = {name: profile(points) for name, points in families.items()}
    assert actual == expected
    base_23 = [(x, (x * x) % 23) for x in range(23)]
    assert all(
        content(sub(families["balanced-23"][right], families["balanced-23"][left]))
        == content(sub(base_23[right], base_23[left]))
        for left in range(23)
        for right in range(left + 1, 23)
    )

    print("exact closed metric-content primitive-area gate: PASS")
    print(
        "profiles:",
        {
            name: {
                "hyperedges": row[2],
                "keys": row[3],
                "max_load": row[4],
                "normalized_energy": round(row[5] / row[2], 6),
            }
            for name, row in actual.items()
        },
    )


if __name__ == "__main__":
    main()
