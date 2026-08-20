#!/usr/bin/env python3
"""Verify the radial Schur-triple endpoint-cocycle barrier."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import ceil
from random import Random


Point = tuple[int, int]


def norm2(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def add(first: Point, second: Point) -> Point:
    return first[0] + second[0], first[1] + second[1]


def negate(point: Point) -> Point:
    return -point[0], -point[1]


def lifted_residue_parabola(prime: int) -> list[Point]:
    return [
        (x + prime * ((x * x) % prime), (x * x) % prime)
        for x in range(prime)
    ]


def genuine_difference_profile(points: list[Point]) -> tuple[int, int, int, int]:
    by_vector: dict[Point, tuple[int, int]] = {}
    by_radius: dict[int, tuple[int, int]] = {}
    for first, a in enumerate(points):
        for second in range(first + 1, len(points)):
            b = points[second]
            radius = (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
            assert radius not in by_radius
            by_radius[radius] = (first, second)
        for second, b in enumerate(points):
            if first == second:
                continue
            vector = b[0] - a[0], b[1] - a[1]
            assert vector not in by_vector
            by_vector[vector] = (first, second)

    vectors = set(by_vector)
    total = 0
    clean = 0
    for first in vectors:
        for second in vectors:
            third = negate(add(first, second))
            if third not in vectors:
                continue
            total += 1
            clean += len(set(by_vector[first] + by_vector[second] + by_vector[third])) == 6
    return len(vectors), total, clean, total - clean


def radial_representatives(side: int, seed: int) -> dict[int, Point]:
    classes: defaultdict[int, list[Point]] = defaultdict(list)
    for first in range(-side, side + 1):
        for second in range(-side, side + 1):
            if (first, second) == (0, 0):
                continue
            if first < 0 or (first == 0 and second < 0):
                continue
            classes[first * first + second * second].append((first, second))
    rng = Random(seed)
    return {radius: rng.choice(vectors) for radius, vectors in classes.items()}


def radial_set(representatives: dict[int, Point], radii: set[int]) -> set[Point]:
    output: set[Point] = set()
    for radius in radii:
        vector = representatives[radius]
        output.add(vector)
        output.add(negate(vector))
    return output


def distinct_radius_triples(
    vectors: set[Point],
) -> list[tuple[Point, Point, Point, tuple[int, int, int]]]:
    output = []
    for first in vectors:
        for second in vectors:
            third = negate(add(first, second))
            if third not in vectors:
                continue
            radii = norm2(first), norm2(second), norm2(third)
            if len(set(radii)) == 3:
                output.append((first, second, third, radii))
    return output


def verify_radial_profiles() -> None:
    expected = {
        (12, 2): (164, 4104, 4068),
        (20, 3): (394, 21378, 21240),
        (30, 1): (814, 83784, 83604),
        (40, 2): (1372, 221016, 220716),
    }
    for (side, seed), row in expected.items():
        representatives = radial_representatives(side, seed)
        vectors = radial_set(representatives, set(representatives))
        labels = Counter(norm2(vector) for vector in vectors)
        assert set(labels.values()) == {2}
        triples = distinct_radius_triples(vectors)
        total = sum(
            negate(add(first, second)) in vectors
            for first in vectors
            for second in vectors
        )
        assert (len(vectors), total, len(triples)) == row


def trimmed_formal_certificate() -> tuple[int, int, int, int, int]:
    side = 30
    representatives = radial_representatives(side, 1)
    radii = set(representatives)
    vectors = radial_set(representatives, radii)
    triples = distinct_radius_triples(vectors)
    assert (len(radii), len(vectors), len(triples)) == (407, 814, 83604)

    degree: Counter[int] = Counter()
    for _first, _second, _third, triple_radii in triples:
        degree.update(triple_radii)
    removed = min(radii, key=lambda radius: degree[radius])
    assert removed == 1682
    radii.remove(removed)

    k = 29
    assert len(radii) == k * (k - 1) // 2 == 406
    vectors = radial_set(representatives, radii)
    triples = distinct_radius_triples(vectors)
    assert len(vectors) == k * (k - 1) == 812
    assert len(triples) == 83496

    endpoint_edges = list(combinations(range(k), 2))
    Random(2).shuffle(endpoint_edges)
    labels = dict(zip(sorted(radii), endpoint_edges))
    clean = 0
    for _first, _second, _third, triple_radii in triples:
        edges = [labels[radius] for radius in triple_radii]
        clean += len(set(edges[0] + edges[1] + edges[2])) == 6
    assert clean == 54720

    displacement: dict[tuple[int, int], Point] = {}
    for radius, (first, second) in labels.items():
        vector = representatives[radius]
        displacement[first, second] = vector
        displacement[second, first] = negate(vector)
    assert len(displacement) == k * (k - 1)

    cocycles = 0
    for first, second, third in permutations(range(k), 3):
        left = add(displacement[first, second], displacement[second, third])
        cocycles += left == displacement[first, third]
    assert cocycles == 6

    ambient_side = ceil(side**1.5)
    assert ambient_side == 165
    assert clean > k**3 + ambient_side**2 == 51614
    return k, len(vectors), len(triples), clean, cocycles


def main() -> None:
    genuine = genuine_difference_profile(lifted_residue_parabola(7))
    assert genuine == (42, 654, 144, 510)
    assert genuine[3] <= 15 * 7**3
    verify_radial_profiles()
    formal = trimmed_formal_certificate()
    print(
        "PASS",
        {
            "genuine_p7": genuine,
            "formal_radial_L30": formal,
            "ambient_side": 165,
            "formal_target": 51614,
            "load_bearing_property": "global endpoint cocycle",
        },
    )


if __name__ == "__main__":
    main()
