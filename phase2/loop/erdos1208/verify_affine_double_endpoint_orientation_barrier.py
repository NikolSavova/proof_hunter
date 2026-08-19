#!/usr/bin/env python3
"""Exact checks for AFFINE_DOUBLE_ENDPOINT_ORIENTATION_BARRIER.md."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations


Cell = tuple[int, int]
Line = tuple[int, int]


def ordered_edge(left: Cell, right: Cell) -> tuple[Cell, Cell]:
    return (left, right) if left < right else (right, left)


def verify_prime(prime: int) -> None:
    cells = [
        (i, j)
        for i in range(1, prime)
        for j in range(1, prime)
        if i != j
    ]
    lines = [
        (slope, intercept)
        for slope in range(1, prime)
        for intercept in range(prime)
    ]
    block_size = prime - 1

    blocks: dict[Cell, set[Line]] = {
        (i, j): {
            (slope, (j - slope * i) % prime)
            for slope in range(1, prime)
        }
        for i, j in cells
    }
    assert all(len(block) == block_size for block in blocks.values())

    all_pencils: dict[Line, set[Cell]] = {
        (slope, intercept): {
            (i, (slope * i + intercept) % prime)
            for i in range(1, prime)
            if (i, (slope * i + intercept) % prime) in cells
        }
        for slope, intercept in lines
    }
    assert Counter(map(len, all_pencils.values())) == {
        0: 1,
        block_size: block_size - 1,
        block_size - 1: block_size,
        block_size - 2: block_size * (block_size - 1),
    }
    pencils = {line: pencil for line, pencil in all_pencils.items() if pencil}

    full_diagonal_pencils = 0
    for (slope, intercept), pencil in pencils.items():
        if intercept != 0 or slope == 1:
            continue
        assert len(pencil) == block_size
        for i, j in pencil:
            incidence_label = (i * slope) % prime
            assert incidence_label == j
        full_diagonal_pencils += 1
    assert full_diagonal_pencils == block_size - 1

    edge_centre: dict[tuple[Cell, Cell], Line] = {}
    for line, pencil in pencils.items():
        assert len({i for i, _ in pencil}) == len(pencil)
        assert len({j for _, j in pencil}) == len(pencil)
        incidence_labels = {
            (i * line[0]) % prime for i, _ in pencil
        }
        assert len(incidence_labels) == len(pencil)
        for left, right in combinations(sorted(pencil), 2):
            edge = ordered_edge(left, right)
            assert edge not in edge_centre
            edge_centre[edge] = line

    for left, right in combinations(cells, 2):
        intersection = blocks[left].intersection(blocks[right])
        should_meet = left[0] != right[0] and left[1] != right[1]
        assert len(intersection) == int(should_meet)
        assert (ordered_edge(left, right) in edge_centre) == should_meet
        if should_meet:
            assert intersection == {edge_centre[ordered_edge(left, right)]}

    # Equal first or second endpoint labels are independent sets.
    for coordinate in (0, 1):
        for value in range(1, prime):
            colour_class = [cell for cell in cells if cell[coordinate] == value]
            assert all(
                ordered_edge(left, right) not in edge_centre
                for left, right in combinations(colour_class, 2)
            )

    intersection_count = len(edge_centre)
    expected_edges = (
        (block_size - 1) * block_size * (block_size - 1) // 2
        + block_size * (block_size - 1) * (block_size - 2) // 2
        + block_size
        * (block_size - 1)
        * (block_size - 2)
        * (block_size - 3)
        // 2
    )
    assert intersection_count == expected_edges

    # Lexicographically orient every edge and compute its outgoing pencil
    # cut.  The lower bound below applies to every orientation, not only this
    # convenient exact stress.
    outdegree: Counter[Cell] = Counter(tail for tail, _ in edge_centre)
    pencil_outcut: dict[Line, int] = {}
    for line, pencil in pencils.items():
        internal = len(pencil) * (len(pencil) - 1) // 2
        direct = sum(
            1
            for tail, head in edge_centre
            if tail in pencil and head not in pencil
        )
        predicted = sum(outdegree[cell] for cell in pencil) - internal
        assert direct == predicted
        pencil_outcut[line] = direct

    total = sum(pencil_outcut.values())
    assert total == (block_size - 1) * intersection_count
    cost = sum(value * value for value in pencil_outcut.values())
    # The isolated zero block contributes k further support points, all with
    # pencil load zero.
    support_size = len(pencils) + block_size
    assert support_size == block_size**2 + 2 * block_size - 1
    cauchy_lower = Fraction(total * total, support_size)
    assert cost >= cauchy_lower

    normalized_universal_lower = Fraction(
        block_size * (block_size - 1) ** 2,
        support_size,
    )
    assert (
        Fraction(block_size, intersection_count**2) * cauchy_lower
        == normalized_universal_lower
    )
    print(
        prime,
        "affine double-endpoint profile",
        (
            block_size,
            len(cells) + 1,
            support_size,
            intersection_count,
            cost,
            normalized_universal_lower,
        ),
    )


def main() -> None:
    for prime in (5, 7, 11, 13):
        verify_prime(prime)
    print("affine double-endpoint orientation barrier: PASS")


if __name__ == "__main__":
    main()
