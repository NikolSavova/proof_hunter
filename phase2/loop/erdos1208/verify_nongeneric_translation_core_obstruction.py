#!/usr/bin/env python3
"""Exact exhaustion of nongeneric abelian eight-corner cores.

The earlier Fourier audit leaves 27,389 systems with a forced record kernel
and 581 systems with a universal squared-distance collision.  This verifier
checks the former kernel obstruction and runs the Q(i) partition closure on
every latter system.
"""

from __future__ import annotations

from collections import Counter

from search_edge_disjoint_translation_core import (
    annihilator,
    coalesced_translation_obstruction,
    face_spaces,
    intersection,
    translation_matchings,
)
from search_full_eight_corner_core import relation_tuples
from search_nongeneric_translation_core import PartitionSearch
from verify_edge_disjoint_translation_core_obstruction import (
    columns,
    gaussian_binomial,
    rref_subspaces,
)


def record_kernel_size(dimension: int, shifts: tuple[int, ...]) -> int:
    spaces = face_spaces(shifts)
    annihilators = tuple(annihilator(dimension, space) for space in spaces)
    multiplicity = Counter(
        character for characters in annihilators for character in characters
    )
    active_by_role = tuple(
        tuple(
            character
            for character in characters
            if character and multiplicity[character] >= 2
        )
        for characters in annihilators
    )
    coalesced_spaces = tuple(
        frozenset(
            direction
            for direction in range(1 << dimension)
            if all(
                (character & direction).bit_count() % 2 == 0
                for character in active
            )
        )
        for active in active_by_role
    )
    return len(intersection(coalesced_spaces))


def main() -> None:
    totals: Counter[str] = Counter()
    kernel_histogram: Counter[int] = Counter()
    maximum_nodes = 0
    maximum_example: tuple[int, tuple[int, ...]] | None = None

    for dimension in range(1, 9):
        dimension_count = 0
        for rows in rref_subspaces(8, dimension):
            dimension_count += 1
            totals["subspaces"] += 1
            shifts = columns(rows)
            if 0 in shifts or len(set(shifts)) != 8:
                continue
            totals["simple"] += 1
            spaces = face_spaces(shifts)
            if intersection(spaces) != frozenset({0}):
                totals["record-collapse"] += 1
                continue
            totals["formal-full-core"] += 1
            outcome, _ = coalesced_translation_obstruction(dimension, shifts)
            totals[outcome] += 1

            if outcome == "empty-core":
                kernel = record_kernel_size(dimension, shifts)
                assert kernel > 1
                kernel_histogram[kernel] += 1
                continue

            assert outcome == "translation-collision"
            data = relation_tuples(translation_matchings(dimension, shifts))
            assert data is not None
            relations, variables = data
            search = PartitionSearch(tuple(relations), variables, exact=True)
            survivor = search.run(1_000_000)
            assert survivor is None
            totals["partition-systems"] += 1
            totals["partition-nodes"] += search.nodes
            for reason, count in search.reasons.items():
                totals[f"state:{reason}"] += count
            if search.nodes > maximum_nodes:
                maximum_nodes = search.nodes
                maximum_example = dimension, shifts
        assert dimension_count == gaussian_binomial(8, dimension)

    assert totals == Counter(
        {
            "subspaces": 417_198,
            "simple": 50_864,
            "record-collapse": 22_894,
            "formal-full-core": 27_970,
            "empty-core": 27_389,
            "translation-collision": 581,
            "partition-systems": 581,
            "partition-nodes": 793,
            "state:forced-point-coalescence": 107,
            "state:record-collapse": 42,
            "state:corner-nonlinearity": 609,
            "state:norm-conflict": 35,
        }
    )
    assert kernel_histogram == Counter(
        {2: 1_400, 4: 3_880, 8: 7_996, 16: 10_169, 32: 3_925, 64: 19}
    )
    assert maximum_nodes == 5
    assert maximum_example is not None
    print("totals", dict(totals))
    print("record kernels", dict(sorted(kernel_histogram.items())))
    print("maximum partition nodes", maximum_nodes, maximum_example)
    print("nongeneric translation-core obstruction: PASS")


if __name__ == "__main__":
    main()
