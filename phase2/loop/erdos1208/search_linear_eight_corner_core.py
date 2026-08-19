#!/usr/bin/env python3
"""Search linear F_2 models of an exact full eight-corner relation core.

Records are x in F_2^m.  Each of the six endpoint roles is a linear quotient
with row space U_s.  Every mixed corner has fibre size two when the span of
the three selected row spaces has rank m-1.  Fourier decomposition gives the
complete Gaussian-linear solution space of the relation equation; we test
whether its formal point labels can be generically distance-Sidon.
"""

from __future__ import annotations

import argparse
import random
from itertools import combinations, product

from search_four_corner_core import Form, difference, norm_signature


Gaussian = tuple[int, int]


def gf2_rank(vectors: list[int]) -> int:
    basis: dict[int, int] = {}
    for value in vectors:
        while value:
            pivot = value.bit_length() - 1
            if pivot in basis:
                value ^= basis[pivot]
            else:
                basis[pivot] = value
                break
    return len(basis)


def canonical_basis(vectors: list[int]) -> tuple[int, ...]:
    pivots: dict[int, int] = {}
    for value in vectors:
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                for old_pivot, old in list(pivots.items()):
                    if (old >> pivot) & 1:
                        pivots[old_pivot] = old ^ value
                pivots[pivot] = value
                break
    return tuple(pivots[pivot] for pivot in sorted(pivots))


def subspace(basis: tuple[int, ...]) -> frozenset[int]:
    values = []
    for mask in range(1 << len(basis)):
        value = 0
        for index, vector in enumerate(basis):
            if (mask >> index) & 1:
                value ^= vector
        values.append(value)
    return frozenset(values)


def all_subspaces(m: int, dimension: int) -> list[tuple[tuple[int, ...], frozenset[int]]]:
    found: dict[frozenset[int], tuple[int, ...]] = {}
    for generators in combinations(range(1, 1 << m), dimension):
        basis = canonical_basis(list(generators))
        if len(basis) != dimension:
            continue
        space = subspace(basis)
        found.setdefault(space, basis)
    return [(basis, space) for space, basis in found.items()]


def gaussian_negate(value: Gaussian) -> Gaussian:
    return -value[0], -value[1]


def gaussian_multiply(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def gaussian_divide_unit(left: Gaussian, right: Gaussian) -> Gaussian:
    # All coefficients used here are Gaussian units.
    return gaussian_multiply(left, (right[0], -right[1]))


def build_point_forms(
    m: int,
    choices: tuple[tuple[tuple[int, ...], frozenset[int]], ...],
) -> tuple[list[Form], list[tuple[int, int]]]:
    signs: tuple[Gaussian, ...] = ((1, 0), (-1, 0), (-1, 0), (1, 0), (0, -1), (0, 1))
    spaces = [choice[1] for choice in choices]
    parameters: list[tuple[int, int, Gaussian]] = []
    # Entry (role, character, coefficient of the independent parameter).
    parameter_columns: list[list[tuple[int, int, Gaussian]]] = []
    for character in range(1 << m):
        roles = [role for role, space in enumerate(spaces) if character in space]
        if len(roles) < 2:
            continue
        pivot = roles[-1]
        for role in roles[:-1]:
            pivot_coefficient = gaussian_negate(gaussian_divide_unit(signs[role], signs[pivot]))
            parameter_columns.append(
                [(role, character, (1, 0)), (pivot, character, pivot_coefficient)]
            )
    dimension = len(parameter_columns)
    role_character_coefficients: dict[tuple[int, int], list[Gaussian]] = {}
    for column, entries in enumerate(parameter_columns):
        for role, character, coefficient in entries:
            vector = role_character_coefficients.setdefault(
                (role, character), [(0, 0)] * dimension
            )
            vector[column] = coefficient

    point_forms: list[Form] = []
    point_labels: list[tuple[int, int]] = []
    for role, (basis, _) in enumerate(choices):
        labels: dict[tuple[int, ...], int] = {}
        for x in range(1 << m):
            label = tuple((vector & x).bit_count() & 1 for vector in basis)
            labels.setdefault(label, x)
        for label, representative in sorted(labels.items()):
            form = [(0, 0)] * dimension
            for character in spaces[role]:
                coefficient_vector = role_character_coefficients.get((role, character))
                if coefficient_vector is None:
                    continue
                parity = -1 if ((character & representative).bit_count() & 1) else 1
                for column, (real, imag) in enumerate(coefficient_vector):
                    form[column] = form[column][0] + parity * real, form[column][1] + parity * imag
            point_forms.append(tuple(form))
            point_labels.append((role, sum(bit << index for index, bit in enumerate(label))))
    return point_forms, point_labels


def repeated_norm_count(points: list[Form]) -> int:
    seen: set[tuple[Gaussian, ...]] = set()
    repeats = 0
    for first, second in combinations(range(len(points)), 2):
        signature = norm_signature(difference(points[first], points[second]))
        if signature in seen:
            repeats += 1
        else:
            seen.add(signature)
    return repeats


def search(m: int, dimension: int, trials: int, seed: int) -> None:
    rng = random.Random(seed)
    candidates = all_subspaces(m, dimension)
    print("subspaces", len(candidates))
    best: tuple[int, tuple[tuple[tuple[int, ...], frozenset[int]], ...]] | None = None
    accepted = 0
    for trial in range(trials):
        choices = tuple(rng.choice(candidates) for _ in range(6))
        good = True
        for i, j, k in product((0, 1), repeat=3):
            vectors = list(choices[i][0] + choices[2 + j][0] + choices[4 + k][0])
            if gf2_rank(vectors) != m - 1:
                good = False
                break
        if not good:
            continue
        points, labels = build_point_forms(m, choices)
        if len(set(points)) != len(points):
            continue
        accepted += 1
        repeats = repeated_norm_count(points)
        if best is None or repeats < best[0]:
            best = repeats, choices
            print("best", trial, "accepted", accepted, "points", len(points), "repeats", repeats)
            print("bases", tuple(choice[0] for choice in choices))
        if not repeats:
            print("GENERIC FULL-CORE COUNTEREXAMPLE")
            return
    print("complete", "accepted", accepted, "best", None if best is None else best[0])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, default=5)
    parser.add_argument("--dimension", type=int, default=2)
    parser.add_argument("--trials", type=int, default=100_000)
    parser.add_argument("--seed", type=int, default=1208)
    args = parser.parse_args()
    search(args.m, args.dimension, args.trials, args.seed)


if __name__ == "__main__":
    main()
