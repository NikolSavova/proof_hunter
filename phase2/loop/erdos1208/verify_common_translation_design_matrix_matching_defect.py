#!/usr/bin/env python3
"""Exact design-rank and matching-defect audit for one clean fibre."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import comb

from verify_metric_scalar_universal_matrix_and_ruler_stress import (
    add,
    clean_fibres,
    distance_sidon,
    finite_field_parabola,
    lex_transform,
    sub,
)


def rank_mod(matrix: list[list[int]], prime: int = 1_000_003) -> int:
    rows = [[entry % prime for entry in row] for row in matrix]
    if not rows:
        return 0
    row_count, column_count = len(rows), len(rows[0])
    rank = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(rank, row_count) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], prime - 2, prime)
        rows[rank] = [(entry * inverse) % prime for entry in rows[rank]]
        for row in range(row_count):
            if row == rank or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                (left - factor * right) % prime
                for left, right in zip(rows[row], rows[rank])
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def profile(p: int) -> tuple[int, ...]:
    points = finite_field_parabola(p)
    fibres, pair_by_sum, _ = clean_fibres(points)
    q_value = max(fibres, key=lambda q: len(fibres[q]))
    starts = fibres[q_value]

    transformed = [lex_transform(p, point) for point in points]
    assert distance_sidon(transformed)
    transformed_q = sub(
        lex_transform(p, q_value), lex_transform(p, (0, 0))
    )

    active = sorted({
        vertex
        for start in starts
        for vertex in pair_by_sum[start] + pair_by_sum[add(start, q_value)]
    })
    position = {vertex: index for index, vertex in enumerate(active)}
    n = len(active)

    role_rows: list[list[int]] = []
    merged_rows: list[list[int]] = []
    signed_codegrees: Counter[tuple[str, int, str, int]] = Counter()
    merged_codegrees: Counter[tuple[int, int]] = Counter()

    for start in starts:
        source = pair_by_sum[start]
        target = pair_by_sum[add(start, q_value)]
        assert set(source).isdisjoint(target)

        role_row = [0] * (2 * n)
        merged_row = [0] * n
        for vertex in source:
            role_row[position[vertex]] = -1
            merged_row[position[vertex]] = -1
        for vertex in target:
            role_row[n + position[vertex]] = 1
            merged_row[position[vertex]] = 1
        role_rows.append(role_row)
        merged_rows.append(merged_row)

        signed_codegrees[("-", min(source), "-", max(source))] += 1
        signed_codegrees[("+", min(target), "+", max(target))] += 1
        for source_vertex in source:
            for target_vertex in target:
                signed_codegrees[
                    ("-", source_vertex, "+", target_vertex)
                ] += 1
        for first, second in combinations(source + target, 2):
            merged_codegrees[tuple(sorted((first, second)))] += 1

        # The integral transformed realization satisfies the same row.
        lhs = [0, 0]
        for coefficient, vertex in zip(merged_row, active):
            lhs[0] += coefficient * transformed[vertex][0]
            lhs[1] += coefficient * transformed[vertex][1]
        assert tuple(lhs) == transformed_q

    assert max(signed_codegrees.values()) == 1
    assert max(merged_codegrees.values()) <= 4

    centered_role = [
        [left - right for left, right in zip(row, role_rows[0])]
        for row in role_rows[1:]
    ]
    centered_merged = [
        [left - right for left, right in zip(row, merged_rows[0])]
        for row in merged_rows[1:]
    ]
    ranks = (
        rank_mod(role_rows),
        rank_mod(centered_role),
        rank_mod(merged_rows),
        rank_mod(centered_merged),
    )

    # On odd n, the colour (i+j)/2 mod n partitions K_n into matchings.
    assert n % 2 == 1
    inverse_two = pow(2, -1, n)
    blocks: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for start in starts:
        first, second = map(position.__getitem__, pair_by_sum[start])
        blocks[((first + second) * inverse_two) % n].append(start)

    total_discrepancy = 0
    total_wedges = 0
    total_escapes = 0
    minimum_discrepancy = None
    maximum_block = 0
    for block in blocks.values():
        source_vertices: set[int] = set()
        target_degrees: Counter[int] = Counter()
        for start in block:
            source = pair_by_sum[start]
            assert source_vertices.isdisjoint(source)
            source_vertices.update(source)
            target_degrees.update(pair_by_sum[add(start, q_value)])

        discrepancy = {
            vertex: target_degrees[vertex] - int(vertex in source_vertices)
            for vertex in active
        }
        assert sum(discrepancy.values()) == 0
        lhs = [
            sum(discrepancy[v] * transformed[v][coordinate] for v in active)
            for coordinate in (0, 1)
        ]
        assert tuple(lhs) == (
            len(block) * transformed_q[0],
            len(block) * transformed_q[1],
        )
        norm_squared = sum(value * value for value in discrepancy.values())
        wedges = sum(comb(target_degrees[v], 2) for v in active)
        escapes = sum(
            target_degrees[v] for v in active if v not in source_vertices
        )
        assert norm_squared == 2 * (wedges + escapes)
        assert norm_squared > 0

        total_discrepancy += norm_squared
        total_wedges += wedges
        total_escapes += escapes
        minimum_discrepancy = (
            norm_squared if minimum_discrepancy is None
            else min(minimum_discrepancy, norm_squared)
        )
        maximum_block = max(maximum_block, len(block))

    return (
        p,
        len(starts),
        n,
        max(signed_codegrees.values()),
        max(merged_codegrees.values()),
        *ranks,
        len(blocks),
        maximum_block,
        total_discrepancy,
        total_wedges,
        total_escapes,
        minimum_discrepancy or 0,
    )


def main() -> None:
    expected = {
        31: (31, 86, 29, 1, 4, 55, 54, 27, 26, 28, 6, 272, 0, 136, 4),
        43: (43, 171, 41, 1, 4, 79, 78, 39, 38, 41, 12, 562, 12, 269, 4),
        61: (61, 336, 59, 1, 4, 115, 114, 57, 56, 59, 11, 1090, 0, 545, 8),
    }
    for p, wanted in expected.items():
        actual = profile(p)
        assert actual == wanted, (p, actual, wanted)
        print(actual)
    print("common-translation design and matching-defect audit: PASS")


if __name__ == "__main__":
    main()
