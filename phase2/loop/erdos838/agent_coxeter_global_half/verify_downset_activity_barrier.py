#!/usr/bin/env python3
"""Exact finite checks for DOWNSET_ACTIVITY_BARRIER.md."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
N58_CERTIFICATE = (
    HERE.parent
    / "agent_cyclic_stem_hw"
    / "reflection_counter"
    / "certificate.json"
)
ALPHA = math.log2(1.5)


def partition_numbers(limit: int) -> list[int]:
    """p[m] is the exact number of integer partitions of m."""
    p = [0] * (limit + 1)
    p[0] = 1
    for part in range(1, limit + 1):
        for total in range(part, limit + 1):
            p[total] += p[total - part]
    return p


def minimum_total_area(number: int, p: list[int]) -> tuple[int, int]:
    """Return exact minimum area and largest used area for `number` diagrams."""
    remaining = number
    total = 0
    largest = 0
    for area, multiplicity in enumerate(p):
        take = min(remaining, multiplicity)
        total += area * take
        if take:
            largest = area
        remaining -= take
        if remaining == 0:
            return total, largest
    raise AssertionError("partition table too short")


def distinct_part_construction(rank: int) -> None:
    """Every subset of [rank] gives a distinct partition of bounded area."""
    areas = []
    for mask in range(1 << rank):
        area = sum(j + 1 for j in range(rank) if mask & (1 << j))
        areas.append(area)
    assert len(areas) == 1 << rank
    assert max(areas) == rank * (rank + 1) // 2


def exhaustive_boolean_downsets(rank: int = 4) -> tuple[int, float]:
    """Exhaust Theorem 2 on every downset of a small Boolean lattice."""
    subsets = 1 << rank
    submasks = []
    for subset in range(subsets):
        mask = 0
        child = subset
        while True:
            mask |= 1 << child
            if child == 0:
                break
            child = (child - 1) & subset
        submasks.append(mask)

    number_downsets = 0
    minimum_log_slack = float("inf")
    h = Fraction(1, 2)
    for family in range(1 << subsets):
        if any(
            family & (1 << subset) and family & submasks[subset] != submasks[subset]
            for subset in range(subsets)
        ):
            continue
        number_downsets += 1
        size = family.bit_count()
        if size == 0:
            continue
        weighted = sum(
            (
                h ** subset.bit_count()
                for subset in range(subsets)
                if family & (1 << subset)
            ),
            Fraction(0),
        )
        slack = math.log2(float(weighted)) - ALPHA * math.log2(size)
        assert slack >= -1e-12
        minimum_log_slack = min(minimum_log_slack, slack)
    assert number_downsets == 168
    return number_downsets, minimum_log_slack


def root_sequence(n: int, word: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    """Validate a reduced word for w0 and return its positive-root order."""
    wires = list(range(n))
    roots = []
    for generator in word:
        assert 0 <= generator < n - 1
        left, right = wires[generator : generator + 2]
        assert left < right
        roots.append((left, right))
        wires[generator], wires[generator + 1] = right, left
    assert len(word) == n * (n - 1) // 2
    assert wires == list(reversed(range(n)))
    assert set(roots) == set(combinations(range(n), 2))
    return tuple(roots)


def product_one(
    n: int, roots: tuple[tuple[int, int], ...]
) -> list[list[int]]:
    matrix = [[int(i == j) for j in range(n)] for i in range(n)]
    for i, j in roots:
        matrix[j] = [left + right for left, right in zip(matrix[j], matrix[i])]
    return matrix


def product_half_scaled(
    n: int, roots: tuple[tuple[int, int], ...]
) -> tuple[int, list[list[int]]]:
    scale = 1 << n
    matrix = [[scale * int(i == j) for j in range(n)] for i in range(n)]
    for i, j in roots:
        assert all(value % 2 == 0 for value in matrix[i])
        matrix[j] = [left + right // 2 for left, right in zip(matrix[j], matrix[i])]
    return scale, matrix


def rectangle_union_area(rectangles: list[tuple[int, int]]) -> int:
    """Area of the union of integer rectangles [width] x [height]."""
    area = 0
    current_height = 0
    for width, height in sorted(rectangles, reverse=True):
        if height > current_height:
            area += width * (height - current_height)
            current_height = height
    return area


def n58_reflection_regression() -> dict[str, float | int]:
    """Replay the path and vertex inequalities on the certified hard word."""
    saved = json.loads(N58_CERTIFICATE.read_text())["finite_braid_record"]
    n = int(saved["n"])
    roots = root_sequence(n, tuple(map(int, saved["word_zero_based"])))

    forward_one = product_one(n, roots)
    backward_one = product_one(n, tuple(reversed(roots)))
    scale, forward_half = product_half_scaled(n, roots)
    other_scale, backward_half = product_half_scaled(n, tuple(reversed(roots)))
    assert scale == other_scale

    min_path_slack = float("inf")
    min_cell_slack = float("inf")
    min_vertex_slack = float("inf")
    for v in range(1, n):
        rectangles = []
        vertex_half = Fraction(0)
        for u in range(v):
            r_one = forward_one[v][u]
            b_one = backward_one[v][u]
            r_half = Fraction(forward_half[v][u], scale)
            b_half = Fraction(backward_half[v][u], scale)
            assert r_one >= 1 and b_one >= 1

            for half_value, one_value in ((r_half, r_one), (b_half, b_one)):
                slack = math.log2(float(2 * half_value)) - ALPHA * math.log2(
                    one_value
                )
                assert slack >= -1e-10
                min_path_slack = min(min_path_slack, slack)

            g_half = r_half * b_half
            x_one = r_one * b_one
            cell_slack = math.log2(float(4 * g_half)) - ALPHA * math.log2(
                x_one
            )
            assert cell_slack >= -1e-10
            min_cell_slack = min(min_cell_slack, cell_slack)
            rectangles.append((r_one, b_one))
            vertex_half += g_half

        area = rectangle_union_area(rectangles)
        vertex_slack = math.log2(float(4 * vertex_half)) - ALPHA * math.log2(
            area
        )
        assert vertex_slack >= -1e-10
        min_vertex_slack = min(min_vertex_slack, vertex_slack)

    return {
        "n": n,
        "minimum_path_slack_bits": min_path_slack,
        "minimum_cell_slack_bits": min_cell_slack,
        "minimum_vertex_slack_bits": min_vertex_slack,
    }


def dyadic_collapse(number: int) -> tuple[Fraction, Fraction]:
    h = Fraction(1, 2)
    delta = Fraction(1, 1 << number)

    rectangle_sum = sum(
        ((h + j * delta) * h for j in range(1, number + 1)), Fraction(0)
    )
    expected_rectangles = (
        number * h * h + h * delta * number * (number + 1) / 2
    )
    assert rectangle_sum == expected_rectangles

    polynomial_sum = sum(
        (((h + j * h**number) * h) for j in range(1, number + 1)),
        Fraction(0),
    )
    expected_polynomials = Fraction(number, 4) + Fraction(
        number * (number + 1), 1 << (number + 2)
    )
    assert polynomial_sum == expected_polynomials

    # At activity one, P_j(1)=j+1 gives pairwise distinct integer states.
    assert len({1 + j for j in range(1, number + 1)}) == number
    return rectangle_sum, polynomial_sum


def main() -> None:
    p = partition_numbers(256)
    assert p[:11] == [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]

    rows = []
    for number in (16, 64, 256, 1024, 4096):
        total, largest = minimum_total_area(number, p)
        rows.append((number, total, largest))

    for rank in range(1, 13):
        distinct_part_construction(rank)

    number_downsets, downset_slack = exhaustive_boolean_downsets()
    n58 = n58_reflection_regression()

    rectangle_sum, polynomial_sum = dyadic_collapse(32)
    assert rectangle_sum > Fraction(32, 4)
    assert polynomial_sum > Fraction(32, 4)
    assert rectangle_sum - Fraction(32, 4) < Fraction(1, 1 << 20)
    assert polynomial_sum - Fraction(32, 4) < Fraction(1, 1 << 20)

    print("downset activity barrier: PASS")
    for number, total, largest in rows:
        print(
            f"N={number:4d} exact_min_total_area={total:6d} "
            f"largest_used_area={largest:2d}"
        )
    print("dyadic rectangles N=32 total area=", rectangle_sum)
    print("path-polynomial rectangles N=32 total area=", polynomial_sum)
    print(
        f"Boolean B4 downsets={number_downsets} "
        f"minimum interpolation slack={downset_slack:.12f} bits"
    )
    print(
        "n58 reflection regression:",
        f"path={n58['minimum_path_slack_bits']:.12f}",
        f"cell={n58['minimum_cell_slack_bits']:.12f}",
        f"vertex={n58['minimum_vertex_slack_bits']:.12f}",
        "bits",
    )


if __name__ == "__main__":
    main()
