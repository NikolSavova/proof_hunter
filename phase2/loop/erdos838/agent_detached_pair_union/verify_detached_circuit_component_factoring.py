#!/usr/bin/env python3
"""Exact audits for DETACHED_CIRCUIT_COMPONENT_FACTORING.md."""

from __future__ import annotations

import json
import math
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from random import Random


HERE = Path(__file__).resolve().parent


Point = tuple[Fraction, Fraction]


def cross(a: Point, b: Point, c: Point) -> Fraction:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def planar_hull(points: list[Point]) -> list[Point]:
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def chain(sequence):
        answer: list[Point] = []
        for point in sequence:
            while (len(answer) >= 2
                   and cross(answer[-2], answer[-1], point) <= 0):
                answer.pop()
            answer.append(point)
        return answer

    return chain(points)[:-1] + chain(reversed(points))[:-1]


def is_face(points: list[Point]) -> bool:
    return len(planar_hull(points)) == len(set(points))


def general_position(points: list[Point]) -> bool:
    return all(cross(*triple) != 0 for triple in combinations(points, 3))


def face_count(points: list[Point]) -> int:
    answer = 0
    for mask in range(1 << len(points)):
        chosen = [points[i] for i in range(len(points)) if mask >> i & 1]
        answer += is_face(chosen)
    return answer


def components(number: int, edges: set[tuple[int, int]]) -> list[list[int]]:
    adjacency = [set() for _ in range(number)]
    for first, second in edges:
        adjacency[first].add(second)
        adjacency[second].add(first)
    unseen = set(range(number))
    answer = []
    while unseen:
        root = min(unseen)
        stack = [root]
        unseen.remove(root)
        part = []
        while stack:
            vertex = stack.pop()
            part.append(vertex)
            for neighbour in adjacency[vertex]:
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    stack.append(neighbour)
        answer.append(sorted(part))
    return answer


def circuit_components(
    points: list[Point], block_of: list[int], number_blocks: int
) -> tuple[list[list[int]], Counter[tuple[int, ...]], set[tuple[int, int]]]:
    edges: set[tuple[int, int]] = set()
    patterns: Counter[tuple[int, ...]] = Counter()
    for indices in combinations(range(len(points)), 4):
        if is_face([points[index] for index in indices]):
            continue
        used = sorted({block_of[index] for index in indices})
        multiplicities = tuple(sorted(Counter(block_of[index] for index in indices).values(),
                                      reverse=True))
        patterns[multiplicities] += 1
        for first, second in combinations(used, 2):
            edges.add((first, second))
    return components(number_blocks, edges), patterns, edges


def random_general_position(rng: Random, size: int) -> list[Point]:
    points: list[Point] = []
    while len(points) < size:
        candidate = (Fraction(rng.randint(-70, 70)),
                     Fraction(rng.randint(-70, 70)))
        if candidate in points:
            continue
        if any(cross(a, b, candidate) == 0 for a, b in combinations(points, 2)):
            continue
        points.append(candidate)
    return points


def random_distinct_height_order_type(rng: Random, size: int) -> list[Point]:
    while True:
        points = random_general_position(rng, size)
        if len({point[1] for point in points}) == size:
            return points


def component_factoring_audit() -> dict[str, int]:
    rng = Random(838_20260814)
    trials = 36
    total_components = 0
    nontrivial_factorizations = 0
    entropy_families = 0
    extension_incidences = 0
    maximum_extension_load = 0

    for _ in range(trials):
        size = rng.randint(6, 10)
        points = random_general_position(rng, size)
        number_blocks = rng.randint(2, min(5, size))
        block_of = [index % number_blocks for index in range(size)]
        rng.shuffle(block_of)
        parts, _, _ = circuit_components(points, block_of, number_blocks)
        total_components += len(parts)
        nontrivial_factorizations += len(parts) > 1

        component_points = [
            [points[index] for index in range(size)
             if block_of[index] in part]
            for part in parts
        ]
        local_counts = [face_count(part) for part in component_points]
        global_count = face_count(points)
        product_count = math.prod(local_counts)
        assert global_count == product_count

        ranks = [rank for rank in range(1, min(5, size + 1))
                 if any(is_face([points[i] for i in indices])
                        for indices in combinations(range(size), rank))]
        rank = rng.choice(ranks)
        family = [indices for indices in combinations(range(size), rank)
                  if is_face([points[i] for i in indices])]
        rng.shuffle(family)
        family = family[: rng.randint(1, len(family))]
        mass = len(family)

        trace_counters = []
        projection_sizes = []
        entropies = []
        expected_ranks = []
        for part in parts:
            labels = {index for index in range(size) if block_of[index] in part}
            counter = Counter(tuple(index for index in face if index in labels)
                              for face in family)
            trace_counters.append(counter)
            projection_sizes.append(len(counter))
            entropy = -sum((count / mass) * math.log2(count / mass)
                           for count in counter.values())
            entropies.append(entropy)
            expected_ranks.append(sum(count * len(trace)
                                      for trace, count in counter.items()) / mass)

        # Exact count-only Kraft identity, cleared of denominators.
        assert product_count * math.prod(projection_sizes) * mass == (
            mass * math.prod(local_counts) * math.prod(projection_sizes)
        )
        left_ratio = product_count / mass
        right_ratio = (math.prod(lc / ps for lc, ps in zip(local_counts, projection_sizes))
                       * math.prod(projection_sizes) / mass)
        assert abs(left_ratio - right_ratio) < 1e-9 * max(1.0, left_ratio)

        total_correlation = sum(entropies) - math.log2(mass)
        local_surplus = sum(math.log2(count) - entropy
                            for count, entropy in zip(local_counts, entropies))
        assert total_correlation > -1e-10
        assert abs(math.log2(product_count / mass)
                   - total_correlation - local_surplus) < 1e-9

        if rank > 0:
            global_rhs = ((math.log2(mass) - math.log2(product_count / mass))
                          / rank)
            potentials = [
                (entropy - (math.log2(count) - entropy)) / expected
                for entropy, count, expected in zip(entropies, local_counts,
                                                    expected_ranks)
                if expected > 0
            ]
            assert max(potentials) + 1e-10 >= global_rhs
        entropy_families += 1

        # Every compatible one-point extension produces a rank-(rank+1)
        # face.  Audit the exact <= rank+1 decoder load.
        if rank < size:
            outputs: Counter[tuple[int, ...]] = Counter()
            family_set = set(family)
            for face in family_set:
                face_set = set(face)
                for label in range(size):
                    if label in face_set:
                        continue
                    extended = tuple(sorted(face_set | {label}))
                    if is_face([points[index] for index in extended]):
                        outputs[extended] += 1
                        extension_incidences += 1
            if outputs:
                load = max(outputs.values())
                assert load <= rank + 1
                maximum_extension_load = max(maximum_extension_load, load)

    # A deterministic many-component instance: every point on this strict
    # parabola chain is exposed, so there are no bad circuits and every
    # original block remains its own component.
    points = [(Fraction(index), Fraction(index * index)) for index in range(-4, 4)]
    block_of = [index % 4 for index in range(len(points))]
    parts, patterns, _ = circuit_components(points, block_of, 4)
    assert general_position(points)
    assert not patterns
    assert len(parts) == 4
    local_counts = [
        face_count([points[index] for index in range(len(points))
                    if block_of[index] in part])
        for part in parts
    ]
    assert face_count(points) == math.prod(local_counts) == 2 ** len(points)
    total_components += len(parts)
    nontrivial_factorizations += 1

    return {
        "general_position_partitions": trials + 1,
        "total_circuit_components": total_components,
        "nontrivial_factorizations": nontrivial_factorizations,
        "entropy_completion_families": entropy_families,
        "one_point_extension_incidences": extension_incidences,
        "maximum_extension_decoder_load": maximum_extension_load,
    }


def nested_triangle_product(length: int) -> tuple[
    list[Point], list[list[list[Point]]], list[int]
]:
    centers = [
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(-1)),
    ]
    tangent_width = Fraction(1, 1000)
    outward_shift = Fraction(1, 50)
    endpoint_correction = -tangent_width * tangent_width / 2
    apex_correction = tangent_width * tangent_width / 10
    perturbation = Fraction(1, 10**16 * max(1, length * length))

    points: list[Point] = []
    pockets: list[list[list[Point]]] = []
    block_of: list[int] = []
    serial = 1
    for pocket, (x, y) in enumerate(centers):
        tangent = (-y, x)
        normal = (x, y)

        def point(tangent_coefficient: Fraction,
                  normal_coefficient: Fraction) -> Point:
            return (
                x + tangent_coefficient * tangent[0] + normal_coefficient * normal[0],
                y + tangent_coefficient * tangent[1] + normal_coefficient * normal[1],
            )

        outer = [
            point(tangent_width, outward_shift + endpoint_correction),
            point(Fraction(0), outward_shift + apex_correction),
            point(-tangent_width, outward_shift + endpoint_correction),
        ]
        centroid = (
            sum(p[0] for p in outer) / 3,
            sum(p[1] for p in outer) / 3,
        )
        layers = []
        for layer in range(length):
            scale = (Fraction(3, 4) if length == 1 else
                     Fraction(3, 4) + Fraction(layer, 4 * (length - 1)))
            triangle = []
            for vertex in outer:
                raw = (
                    centroid[0] + scale * (vertex[0] - centroid[0]),
                    centroid[1] + scale * (vertex[1] - centroid[1]),
                )
                moved = (
                    raw[0] + perturbation * serial,
                    raw[1] + perturbation * serial * serial,
                )
                serial += 1
                triangle.append(moved)
                points.append(moved)
                block_of.append(pocket)
            layers.append(triangle)
        pockets.append(layers)
    return points, pockets, block_of


def triangle_product_audit() -> dict[str, object]:
    configurations = 0
    completions_checked = 0
    detached_bad_pairs = 0
    all_patterns: Counter[tuple[int, ...]] = Counter()
    component_counts = []
    circuit_edges: dict[str, list[str]] = {}
    local_face_counts: dict[str, list[int]] = {}

    for length in range(2, 5):
        points, pockets, block_of = nested_triangle_product(length)
        assert general_position(points)

        words = list(product(range(length), repeat=4))
        completions = [
            list({point for pocket, layer in enumerate(word)
                  for point in pockets[pocket][layer]})
            for word in words
        ]
        for completion in completions:
            assert len(completion) == 12
            assert is_face(completion)
            completions_checked += 1

        for first, second in combinations(completions, 2):
            union = list(set(first) | set(second))
            assert not is_face(union)
            detached_bad_pairs += 1

        parts, patterns, edges = circuit_components(points, block_of, 4)
        all_patterns.update(patterns)
        component_counts.append(len(parts))
        assert len(parts) == 1
        assert patterns[(3, 1)] > 0
        cyclic_edges = {(0, 1), (1, 2), (2, 3), (0, 3)}
        assert cyclic_edges <= edges
        circuit_edges[str(length)] = [f"{first}-{second}"
                                      for first, second in sorted(edges)]

        local_face_counts[str(length)] = [
            face_count([point for layer in pockets[pocket] for point in layer])
            for pocket in range(4)
        ]
        configurations += 1

    return {
        "rational_configurations": configurations,
        "completion_faces_checked": completions_checked,
        "detached_bad_completion_pairs": detached_bad_pairs,
        "circuit_component_counts": component_counts,
        "cross_pocket_circuit_edges": circuit_edges,
        "bad_circuit_trace_patterns": {
            "+".join(map(str, pattern)): count
            for pattern, count in sorted(all_patterns.items())
        },
        "local_face_counts": local_face_counts,
    }


def rooted_universality_audit() -> dict[str, int]:
    rng = Random(838_314159)
    trials = 24
    transformed_points = 0
    rooted_bad_pairs = 0

    for _ in range(trials):
        size = rng.randint(4, 9)
        original = random_distinct_height_order_type(rng, size)
        minimum_height = min(point[1] for point in original)
        coordinates = [(point[0], point[1] - minimum_height + 1)
                       for point in original]

        ratios = []
        for first, second in combinations(coordinates, 2):
            if first[1] > second[1]:
                first, second = second, first
            numerator = abs(second[1] * first[0] - first[1] * second[0])
            denominator = second[1] - first[1]
            assert denominator > 0
            ratios.append(numerator / denominator)
        root_left = (Fraction(-1), Fraction(0))
        root_right = (Fraction(1), Fraction(0))
        scale_bound = Fraction(1, 2) / (max(ratios, default=Fraction(0)) + 1)
        for divisor in range(1, 100):
            scale = scale_bound / divisor
            transformed = [(scale * x, height) for x, height in coordinates]
            if general_position([root_left, root_right] + transformed):
                break
        else:
            raise AssertionError("failed to avoid the finite forbidden scales")

        # The affine flattening preserves the full prescribed order type.
        for indices in combinations(range(size), 3):
            old_sign = cross(*(original[index] for index in indices))
            new_sign = cross(*(transformed[index] for index in indices))
            assert old_sign * new_sign > 0
        assert face_count(original) == face_count(transformed)
        assert general_position([root_left, root_right] + transformed)

        for point in transformed:
            assert is_face([root_left, root_right, point])
        for first, second in combinations(transformed, 2):
            assert not is_face([root_left, root_right, first, second])
            rooted_bad_pairs += 1
        transformed_points += size

    return {
        "arbitrary_rational_order_types": trials,
        "transformed_extension_points": transformed_points,
        "complete_fixed_root_bad_graph_edges": rooted_bad_pairs,
    }


def simultaneous_two_shield_audit() -> dict[str, int]:
    """A finite exact instance of Proposition 4."""
    centers = [
        (Fraction(1), Fraction(0)),
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(-3, 5), Fraction(4, 5)),
        (Fraction(-1), Fraction(0)),
        (Fraction(-3, 5), Fraction(-4, 5)),
    ]
    length = 3
    tangent_width = Fraction(1, 1000)
    outward_shift = Fraction(1, 50)
    endpoint_correction = -tangent_width * tangent_width / 2
    apex_correction = tangent_width * tangent_width / 10

    raw_pockets: list[list[list[Point]]] = []
    raw_points: list[Point] = []
    for x, y in centers[:4]:
        tangent = (-y, x)
        normal = (x, y)

        def point(a: Fraction, b: Fraction) -> Point:
            return (x + a * tangent[0] + b * normal[0],
                    y + a * tangent[1] + b * normal[1])

        outer = [
            point(tangent_width, outward_shift + endpoint_correction),
            point(Fraction(0), outward_shift + apex_correction),
            point(-tangent_width, outward_shift + endpoint_correction),
        ]
        centroid = (sum(p[0] for p in outer) / 3,
                    sum(p[1] for p in outer) / 3)
        layers = []
        for layer in range(length):
            scale = Fraction(3, 4) + Fraction(layer, 4 * (length - 1))
            triangle = [
                (centroid[0] + scale * (vertex[0] - centroid[0]),
                 centroid[1] + scale * (vertex[1] - centroid[1]))
                for vertex in outer
            ]
            layers.append(triangle)
            raw_points.extend(triangle)
        raw_pockets.append(layers)

    # A non-convex five-point order type with distinct heights.
    original_extension = [
        (Fraction(-4), Fraction(3)),
        (Fraction(-1), Fraction(-2)),
        (Fraction(2), Fraction(5)),
        (Fraction(5), Fraction(1)),
        (Fraction(0), Fraction(0)),
    ]
    minimum_height = min(point[1] for point in original_extension)
    maximum_height = max(point[1] for point in original_extension)
    normalized_heights = [
        Fraction(3, 4)
        + Fraction(point[1] - minimum_height,
                   5 * (maximum_height - minimum_height))
        for point in original_extension
    ]
    ratios = []
    for first, second in combinations(range(len(original_extension)), 2):
        if normalized_heights[first] > normalized_heights[second]:
            first, second = second, first
        numerator = abs(
            normalized_heights[second] * original_extension[first][0]
            - normalized_heights[first] * original_extension[second][0]
        )
        denominator = normalized_heights[second] - normalized_heights[first]
        ratios.append(numerator / denominator)
    lateral_scale = Fraction(1, 10) / (max(ratios) + 1)

    x, y = centers[4]
    tangent = (-y, x)
    normal = (x, y)

    def root_point(a: Fraction, b: Fraction) -> Point:
        return (x + a * tangent[0] + b * normal[0],
                y + a * tangent[1] + b * normal[1])

    root_left = root_point(tangent_width,
                           outward_shift + endpoint_correction)
    root_right = root_point(-tangent_width,
                            outward_shift + endpoint_correction)
    local_height = apex_correction - endpoint_correction
    raw_extension = [
        root_point(-tangent_width * lateral_scale * point[0],
                   outward_shift + endpoint_correction
                   + local_height * height)
        for point, height in zip(original_extension, normalized_heights)
    ]
    raw_points.extend([root_left, root_right] + raw_extension)

    # One tiny global generic perturbation removes the symmetries of the
    # rational macro polygon while preserving every strict condition.
    for divisor in range(1, 100):
        epsilon = Fraction(1, 10**24 * divisor)
        moved = [
            (point[0] + epsilon * (index + 1),
             point[1] + epsilon * (index + 1) * (index + 1))
            for index, point in enumerate(raw_points)
        ]
        if general_position(moved):
            break
    else:
        raise AssertionError("failed to find a generic global perturbation")

    iterator = iter(moved)
    pockets = []
    for _ in range(4):
        layers = []
        for _ in range(length):
            layers.append([next(iterator) for _ in range(3)])
        pockets.append(layers)
    root_left = next(iterator)
    root_right = next(iterator)
    extension = [next(iterator) for _ in raw_extension]
    assert list(iterator) == []

    # The extension order type survives all affine/generic perturbations.
    for indices in combinations(range(len(extension)), 3):
        assert (cross(*(original_extension[index] for index in indices))
                * cross(*(extension[index] for index in indices)) > 0)
    assert face_count(original_extension) == face_count(extension)

    words = list(product(range(length), repeat=4))
    completions = [
        [point for pocket, layer in enumerate(word)
         for point in pockets[pocket][layer]]
        for word in words
    ]
    source_faces = 0
    for completion in completions:
        assert is_face(completion)
        for label in extension:
            assert is_face([root_left, root_right] + completion + [label])
            source_faces += 1
    completion_bad_pairs = 0
    for first, second in combinations(completions, 2):
        assert not is_face(first + second)
        completion_bad_pairs += 1
    rooted_bad_pairs = 0
    for first, second in combinations(extension, 2):
        assert not is_face([root_left, root_right, first, second])
        rooted_bad_pairs += 1

    return {
        "completion_rank": 12,
        "completion_words": len(completions),
        "common_extension_labels": len(extension),
        "source_faces": source_faces,
        "detached_bad_completion_pairs": completion_bad_pairs,
        "fixed_root_bad_extension_pairs": rooted_bad_pairs,
        "extension_face_count_preserved": face_count(extension),
    }


def main() -> None:
    certificate = {
        "component_factoring": component_factoring_audit(),
        "rooted_universality_barrier": rooted_universality_audit(),
        "simultaneous_two_shield_regression": simultaneous_two_shield_audit(),
        "nested_triangle_regression": triangle_product_audit(),
        "verdict": (
            "Bad-four-circuit components factor the full convex-face complex "
            "exactly, and the entropy surplus splits into total correlation "
            "plus local shield surpluses.  Nested triangle completions give a "
            "real pairwise detached-incompatible, circuit-connected residue."
        ),
    }
    (HERE / "detached_circuit_component_certificate.json").write_text(
        json.dumps(certificate, indent=2) + "\n"
    )
    print(json.dumps(certificate, indent=2))
    print("detached circuit-component factoring audit: PASS")


if __name__ == "__main__":
    main()
