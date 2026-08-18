#!/usr/bin/env python3
"""Exact finite certificate for the foreign-shift averaging barrier.

The asymptotic argument in FOREIGN_SHIFT_AVERAGING_BARRIER.md uses two
parabola Sidon sets.  This p=127, q=7 instance checks every combinatorial
ingredient, the exact third-moment identity, and one explicit metric lift to
a 117-point distance-Sidon set in general position.
"""

from collections import Counter
from itertools import permutations
from math import comb, gcd


CORE_PRIME = 127
ANCHOR_PRIME = 7
SHEAR = 30_730
STRETCH = 71_498
TRANSLATION = (1_428_002_731_496, 1_536_127_443_481)


def add(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] + y[0], x[1] + y[1]


def sub(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] - y[0], x[1] - y[1]


def quarter_turn(x: tuple[int, int]) -> tuple[int, int]:
    return -x[1], x[0]


def transform(x: tuple[int, int]) -> tuple[int, int]:
    return x[0] + SHEAR * x[1], STRETCH * x[1]


def norm2(x: tuple[int, int]) -> int:
    return x[0] * x[0] + x[1] * x[1]


def determinant(u: tuple[int, int], v: tuple[int, int]) -> int:
    return u[0] * v[1] - u[1] * v[0]


def canonical(v: tuple[int, int]) -> tuple[int, int]:
    negative = (-v[0], -v[1])
    return max(v, negative)


def difference_set(points: list[tuple[int, int]]) -> set[tuple[int, int]]:
    return {sub(x, y) for x in points for y in points if x != y}


def assert_vector_sidon(points: list[tuple[int, int]]) -> None:
    differences = difference_set(points)
    assert len(differences) == len(points) * (len(points) - 1)


def assert_distance_sidon(points: list[tuple[int, int]]) -> None:
    assert len(set(points)) == len(points)
    distances = {
        norm2(sub(points[i], points[j]))
        for i in range(len(points))
        for j in range(i)
    }
    assert 0 not in distances
    assert len(distances) == comb(len(points), 2)


def maximum_collinearity(points: list[tuple[int, int]]) -> int:
    best = 1
    for i, x in enumerate(points):
        directions: Counter[tuple[int, int]] = Counter()
        for j, y in enumerate(points):
            if i == j:
                continue
            dx, dy = sub(y, x)
            divisor = gcd(abs(dx), abs(dy))
            dx //= divisor
            dy //= divisor
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            directions[(dx, dy)] += 1
        best = max(best, 1 + max(directions.values(), default=0))
    return best


def parabola(prime: int) -> list[tuple[int, int]]:
    return [(x, x * x % prime) for x in range(prime)]


def triple_correlation(
    differences: set[tuple[int, int]],
    u: tuple[int, int],
    v: tuple[int, int],
) -> int:
    return sum(
        add(x, u) in differences and add(x, v) in differences
        for x in differences
    )


def build_instance() -> tuple[
    list[tuple[int, int]],
    list[tuple[int, int]],
    list[tuple[int, int]],
]:
    original_core = parabola(CORE_PRIME)
    anchors_parameters = parabola(ANCHOR_PRIME)
    assert_vector_sidon(original_core)
    assert_vector_sidon(anchors_parameters)
    assert maximum_collinearity(original_core) == 2
    assert maximum_collinearity(anchors_parameters) == 2

    # Every common undirected difference labels a unique core edge.  Choosing
    # one endpoint from each such edge leaves disjoint difference spectra.
    core_edge_by_difference = {
        canonical(sub(original_core[i], original_core[j])): (i, j)
        for i in range(len(original_core))
        for j in range(i)
    }
    anchor_undirected_differences = {
        canonical(sub(anchors_parameters[i], anchors_parameters[j]))
        for i in range(len(anchors_parameters))
        for j in range(i)
    }
    overlap = sorted(anchor_undirected_differences & core_edge_by_difference.keys())
    deleted = {core_edge_by_difference[vector][0] for vector in overlap}
    core_parameters = [
        point for index, point in enumerate(original_core) if index not in deleted
    ]
    assert len(overlap) == 21
    assert len(deleted) == 17
    assert len(core_parameters) == 110

    # Explicit instance of the algebraic metric lift.
    core = [transform(point) for point in core_parameters]
    anchors = [
        add(TRANSLATION, tuple(-coordinate for coordinate in quarter_turn(transform(u))))
        for u in anchors_parameters
    ]
    points = core + anchors
    return core_parameters, anchors_parameters, points


def main() -> None:
    core_parameters, anchors_parameters, points = build_instance()
    original_core = parabola(CORE_PRIME)
    core_differences = difference_set(core_parameters)

    assert len(original_core) == 127
    assert_vector_sidon(original_core)
    assert_vector_sidon(anchors_parameters)
    assert maximum_collinearity(original_core) == 2
    assert maximum_collinearity(anchors_parameters) == 2
    assert len(core_parameters) == 110
    assert len(core_differences) == 110 * 109
    assert not (core_differences & difference_set(anchors_parameters))

    direct_total = 0
    distinct_total = 0
    distinct_values: list[int] = []
    for u0 in anchors_parameters:
        for u1 in anchors_parameters:
            for u2 in anchors_parameters:
                value = triple_correlation(
                    core_differences, sub(u1, u0), sub(u2, u0)
                )
                direct_total += value
                if len({u0, u1, u2}) == 3:
                    assert determinant(sub(u1, u0), sub(u2, u0)) != 0
                    distinct_total += value
                    distinct_values.append(value)

    translate_occupancy: Counter[tuple[int, int]] = Counter(
        sub(difference, anchor)
        for difference in core_differences
        for anchor in anchors_parameters
    )
    occupancy_total = sum(value**3 for value in translate_occupancy.values())
    assert sum(translate_occupancy.values()) == len(core_differences) * 7
    assert direct_total == occupancy_total == 880_874
    assert len(distinct_values) == 7 * 6 * 5
    assert distinct_total == 317_592
    assert min(distinct_values) == 1_386
    assert max(distinct_values) == 1_591

    assert len(points) == 117
    assert_distance_sidon(points)
    assert maximum_collinearity(points) == 2

    core = points[: len(core_parameters)]
    anchors = points[len(core_parameters) :]

    # Check that every ordered anchor triangle contributes its advertised
    # number of distinct fibres after the lift.
    lifted_total = 0
    for i, j, k in permutations(range(len(anchors_parameters)), 3):
        u0 = anchors_parameters[i]
        first_shift = sub(anchors_parameters[j], u0)
        second_shift = sub(anchors_parameters[k], u0)
        witnesses = {
            difference
            for difference in core_differences
            if add(difference, first_shift) in core_differences
            and add(difference, second_shift) in core_differences
        }
        outputs = {
            add(anchors[i], quarter_turn(transform(difference)))
            for difference in witnesses
        }
        assert len(outputs) == len(witnesses)
        lifted_total += len(outputs)
    assert lifted_total == distinct_total

    print("original/deleted/core points", 127, 17, len(core_parameters))
    print("anchor points", len(anchors_parameters))
    print("all/distinct anchor moment", direct_total, distinct_total)
    print("minimum/maximum distinct codegree", min(distinct_values), max(distinct_values))
    print("lifted points", len(points))
    print("unordered distances", comb(len(points), 2))
    print("maximum collinearity", maximum_collinearity(points))
    print("distinct anchor contribution / points^3", distinct_total / len(points) ** 3)


if __name__ == "__main__":
    main()
