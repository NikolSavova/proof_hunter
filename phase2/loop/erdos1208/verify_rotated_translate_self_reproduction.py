#!/usr/bin/env python3
"""Exact checks for the rotated-translate self-reproduction gate."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations

from analyze_affine_costas_energy import is_distance_sidon, welch
from verify_determinant_prime_costas_resonance import ROWS, apply


Point = tuple[int, int]


EXPECTED = {
    # prime: (k, |D|, |U|, max fibre, shadow edges)
    11: (10, 91, 876, 2, 4_095),
    17: (16, 241, 3_704, 3, 28_920),
    23: (22, 463, 9_618, 3, 106_953),
}


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def quarter_turn(point: Point) -> Point:
    return -point[1], point[0]


def ordered_edge(left: Point, right: Point) -> tuple[Point, Point]:
    return (left, right) if left < right else (right, left)


def verify_row(prime: int) -> tuple[int, int, int, int, int]:
    matrix, _ = ROWS[prime]
    points = [apply(matrix, point) for point in welch(prime)]
    assert is_distance_sidon(points)
    k = len(points)

    differences = {
        subtract(left, right) for left in points for right in points
    }
    assert len(differences) == k * (k - 1) + 1
    endpoint_of_difference = {
        subtract(left, right): (left, right)
        for left in points
        for right in points
        if left != right
    }
    assert len(endpoint_of_difference) == k * (k - 1)

    blocks: dict[Point, set[Point]] = {}
    fibres: dict[Point, list[tuple[Point, Point]]] = defaultdict(list)
    for difference in differences:
        rotated = quarter_turn(difference)
        block = {add(point, rotated) for point in points}
        assert len(block) == k
        blocks[difference] = block
        for endpoint in points:
            fibres[add(endpoint, rotated)].append((endpoint, difference))

    support = set(fibres)
    assert support == set().union(*blocks.values())
    assert sum(map(len, fibres.values())) == k * len(differences)

    shadow_edges: set[tuple[Point, Point]] = set()
    for block in blocks.values():
        local_edges = {
            ordered_edge(left, right) for left, right in combinations(block, 2)
        }
        assert not shadow_edges.intersection(local_edges)
        shadow_edges.update(local_edges)
    assert len(shadow_edges) == len(differences) * k * (k - 1) // 2

    degrees: dict[Point, int] = defaultdict(int)
    for left, right in shadow_edges:
        degrees[left] += 1
        degrees[right] += 1

    neighborhoods: dict[Point, set[Point]] = {}
    endpoint_sets: dict[Point, set[Point]] = {}
    incident_blocks: dict[Point, set[Point]] = {}
    for output, representations in fibres.items():
        endpoints = {endpoint for endpoint, _ in representations}
        incident_differences = {
            difference for _, difference in representations
        }
        assert len(endpoints) == len(representations)
        assert len(incident_differences) == len(representations)

        block_neighborhood = set().union(
            *(blocks[difference] for difference in incident_differences)
        )
        star_neighborhood = {
            add(output, subtract(point, endpoint))
            for point in points
            for endpoint in endpoints
        }
        expected_size = 1 + (k - 1) * len(representations)
        assert block_neighborhood == star_neighborhood
        assert len(block_neighborhood) == expected_size
        assert degrees[output] == expected_size - 1
        neighborhoods[output] = block_neighborhood
        endpoint_sets[output] = endpoints
        incident_blocks[output] = incident_differences

    assert sum(degrees.values()) == 2 * len(shadow_edges)
    assert sum(
        (k - 1) * len(representations)
        for representations in fibres.values()
    ) == 2 * len(shadow_edges)

    # Directly stress block linearity as a separate assertion.
    block_items = list(blocks.items())
    for index, (difference, block) in enumerate(block_items):
        for other_difference, other_block in block_items[index + 1 :]:
            assert difference != other_difference
            assert len(block.intersection(other_block)) <= 1

    # Check every adjacent pair, and either every or a deterministic sample
    # of nonadjacent pairs, against the transverse endpoint normal form.
    outputs = sorted(support)
    pairs_to_check = set(shadow_edges)
    if len(outputs) <= 1_000:
        pairs_to_check.update(combinations(outputs, 2))
    else:
        target_nonadjacent = 20_000
        for left_index, left in enumerate(outputs):
            if not target_nonadjacent:
                break
            for right in outputs[left_index + 1 :]:
                pair = (left, right)
                if pair in pairs_to_check:
                    continue
                pairs_to_check.add(pair)
                target_nonadjacent -= 1
                if not target_nonadjacent:
                    break

    for left, right in pairs_to_check:
        delta = subtract(right, left)
        common_blocks = incident_blocks[left].intersection(
            incident_blocks[right]
        )
        assert len(common_blocks) <= 1
        baseline = (
            blocks[next(iter(common_blocks))] if common_blocks else set()
        )

        transverse_points: set[Point] = set()
        transverse_count = 0
        for first_endpoint in endpoint_sets[left]:
            for second_endpoint in endpoint_sets[right]:
                shifted = add(
                    delta,
                    subtract(first_endpoint, second_endpoint),
                )
                endpoint_pair = endpoint_of_difference.get(shifted)
                if endpoint_pair is None:
                    continue
                first, second = endpoint_pair
                if first == first_endpoint or second == second_endpoint:
                    continue
                common = add(left, subtract(first, first_endpoint))
                assert common == add(
                    right, subtract(second, second_endpoint)
                )
                assert common not in (left, right)
                assert common not in baseline
                assert common in neighborhoods[left]
                assert common in neighborhoods[right]
                transverse_count += 1
                transverse_points.add(common)

        assert len(transverse_points) == transverse_count
        actual_intersection = neighborhoods[left].intersection(
            neighborhoods[right]
        )
        assert actual_intersection == baseline.union(transverse_points)
        assert len(actual_intersection) == (
            (k if common_blocks else 0) + transverse_count
        )

    return (
        k,
        len(differences),
        len(support),
        max(map(len, fibres.values())),
        len(shadow_edges),
    )


def main() -> None:
    for prime in EXPECTED:
        profile = verify_row(prime)
        assert profile == EXPECTED[prime], (prime, profile, EXPECTED[prime])
        print(prime, "self-reproduction profile", profile)
    print("rotated-translate self-reproduction gate: PASS")


if __name__ == "__main__":
    main()
