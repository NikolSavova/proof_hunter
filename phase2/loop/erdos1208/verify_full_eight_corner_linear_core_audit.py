#!/usr/bin/env python3
"""Exact checks for the F_2-linear full eight-corner core audit."""

from __future__ import annotations

from collections import Counter
from itertools import product

from search_linear_eight_corner_core import (
    build_point_forms,
    gf2_rank,
    repeated_norm_count,
    subspace,
)


Basis = tuple[int, ...]


VALID_BASES: tuple[Basis, ...] = (
    (15, 20),
    (8, 20),
    (13, 20),
    (1, 20),
    (13, 21),
    (7, 8),
)


COLLAPSED_BASES: tuple[Basis, ...] = (
    (3, 24, 36, 65),
    (5, 27, 33, 73),
    (3, 8, 16, 101),
    (14, 16, 39, 68),
    (6, 19, 41, 74),
    (6, 24, 34, 65),
)


def choices_from_bases(bases: tuple[Basis, ...]):
    return tuple((basis, subspace(basis)) for basis in bases)


def relation_indices(m: int, bases: tuple[Basis, ...], labels: list[tuple[int, int]]) -> list[tuple[int, ...]]:
    lookup = {label: index for index, label in enumerate(labels)}
    relations = []
    for record in range(1 << m):
        relation = []
        for role, basis in enumerate(bases):
            label = sum(
                (((vector & record).bit_count() & 1) << index)
                for index, vector in enumerate(basis)
            )
            relation.append(lookup[(role, label)])
        relations.append(tuple(relation))
    return relations


def verify_relation_equations(forms, relations) -> None:
    for relation in relations:
        a0, a1, b0, b1, c0, c1 = (forms[index] for index in relation)
        for coordinate in range(len(a0)):
            # a0-a1-b0+b1-i*c0+i*c1
            real = (
                a0[coordinate][0]
                - a1[coordinate][0]
                - b0[coordinate][0]
                + b1[coordinate][0]
                + c0[coordinate][1]
                - c1[coordinate][1]
            )
            imag = (
                a0[coordinate][1]
                - a1[coordinate][1]
                - b0[coordinate][1]
                + b1[coordinate][1]
                - c0[coordinate][0]
                + c1[coordinate][0]
            )
            assert (real, imag) == (0, 0)


def corner_profile(relations: list[tuple[int, ...]]) -> tuple[int, ...]:
    profile = []
    for mask in range(8):
        keys = Counter(
            (
                relation[mask & 1],
                relation[2 + ((mask >> 1) & 1)],
                relation[4 + ((mask >> 2) & 1)],
            )
            for relation in relations
        )
        assert set(keys.values()) == {2}
        profile.append(len(keys))
    return tuple(profile)


def verify_valid_core() -> None:
    choices = choices_from_bases(VALID_BASES)
    mixed_ranks = tuple(
        gf2_rank(list(choices[i][0] + choices[2 + j][0] + choices[4 + k][0]))
        for i, j, k in product((0, 1), repeat=3)
    )
    total_rank = gf2_rank([vector for basis in VALID_BASES for vector in basis])
    assert mixed_ranks == (4,) * 8
    assert total_rank == 5
    forms, labels = build_point_forms(5, choices)
    relations = relation_indices(5, VALID_BASES, labels)
    assert len(set(relations)) == len(relations) == 32
    assert len(forms) == len(set(forms)) == 24
    assert corner_profile(relations) == (16,) * 8
    verify_relation_equations(forms, relations)
    assert repeated_norm_count(forms) == 16
    print("valid linear core", len(relations), len(forms), repeated_norm_count(forms))


def verify_canonical_cube() -> None:
    bases: list[Basis] = []
    for role in range(3):
        for bit in range(2):
            bases.append(
                tuple(
                    1 << mask
                    for mask in range(8)
                    if ((mask >> role) & 1) != bit
                )
            )
    bases_tuple = tuple(bases)
    choices = choices_from_bases(bases_tuple)
    forms, labels = build_point_forms(8, choices)
    relations = relation_indices(8, bases_tuple, labels)
    assert len(set(relations)) == len(relations) == 256
    assert len(forms) == len(set(forms)) == 96
    assert corner_profile(relations) == (128,) * 8
    verify_relation_equations(forms, relations)
    assert repeated_norm_count(forms) == 96
    print("canonical cube", len(relations), len(forms), repeated_norm_count(forms))


def verify_collapsed_regression() -> None:
    choices = choices_from_bases(COLLAPSED_BASES)
    mixed_ranks = tuple(
        gf2_rank(list(choices[i][0] + choices[2 + j][0] + choices[4 + k][0]))
        for i, j, k in product((0, 1), repeat=3)
    )
    total_rank = gf2_rank([vector for basis in COLLAPSED_BASES for vector in basis])
    forms, labels = build_point_forms(7, choices)
    relations = relation_indices(7, COLLAPSED_BASES, labels)
    assert mixed_ranks == (6,) * 8
    assert total_rank == 6
    assert len(relations) == 128
    assert len(set(relations)) == 64
    assert len(forms) == len(set(forms)) == 96
    assert repeated_norm_count(forms) == 0
    print("collapsed regression", len(relations), len(set(relations)), total_rank)


def main() -> None:
    verify_valid_core()
    verify_canonical_cube()
    verify_collapsed_regression()
    print("full eight-corner linear core audit: PASS")


if __name__ == "__main__":
    main()
