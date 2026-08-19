#!/usr/bin/env python3
"""Search exact full eight-corner cores through doubled four-core trades.

Four c_0-colour matchings act separately on two copies of the certified
sixteen-record trade.  Four c_1-colour matchings join the copies through
edge-disjoint permutations.  Endpoint labels are the connected components
of the appropriate four matching colours.  Exact Q(i) elimination then
tests whether the universal relation system has a generic distance-Sidon
specialization.
"""

from __future__ import annotations

import argparse
import random
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations

from verify_four_corner_stopping_set_barrier import MATCHINGS as BASE_MATCHINGS


GI = tuple[Fraction, Fraction]
Matching = tuple[int, ...]


ZERO: GI = Fraction(0), Fraction(0)
ONE: GI = Fraction(1), Fraction(0)
I: GI = Fraction(0), Fraction(1)
MODULUS = 998_244_353
I_MOD = pow(3, (MODULUS - 1) // 4, MODULUS)


def gi_add(left: GI, right: GI) -> GI:
    return left[0] + right[0], left[1] + right[1]


def gi_negate(value: GI) -> GI:
    return -value[0], -value[1]


def gi_subtract(left: GI, right: GI) -> GI:
    return gi_add(left, gi_negate(right))


def gi_multiply(left: GI, right: GI) -> GI:
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def gi_conjugate(value: GI) -> GI:
    return value[0], -value[1]


def gi_divide(left: GI, right: GI) -> GI:
    denominator = right[0] * right[0] + right[1] * right[1]
    numerator = gi_multiply(left, gi_conjugate(right))
    return numerator[0] / denominator, numerator[1] / denominator


def components(matchings: tuple[Matching, ...]) -> tuple[int, ...]:
    n = len(matchings[0])
    labels = [-1] * n
    component = 0
    for root in range(n):
        if labels[root] >= 0:
            continue
        labels[root] = component
        stack = [root]
        while stack:
            vertex = stack.pop()
            for matching in matchings:
                neighbour = matching[vertex]
                if labels[neighbour] < 0:
                    labels[neighbour] = component
                    stack.append(neighbour)
        component += 1
    return tuple(labels)


def rref_nullspace(matrix: list[list[GI]]) -> list[list[GI]]:
    if not matrix:
        return []
    rows = len(matrix)
    columns = len(matrix[0])
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows) if matrix[row][column] != ZERO), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [gi_divide(value, scale) for value in matrix[pivot_row]]
        for row in range(rows):
            if row == pivot_row or matrix[row][column] == ZERO:
                continue
            factor = matrix[row][column]
            matrix[row] = [
                gi_subtract(matrix[row][entry], gi_multiply(factor, matrix[pivot_row][entry]))
                for entry in range(columns)
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    free_columns = [column for column in range(columns) if column not in set(pivot_columns)]
    basis: list[list[GI]] = []
    for free in free_columns:
        vector = [ZERO] * columns
        vector[free] = ONE
        for row, pivot in enumerate(pivot_columns):
            vector[pivot] = gi_negate(matrix[row][free])
        basis.append(vector)
    return basis


def norm_signature(form: tuple[GI, ...]) -> tuple[GI, ...]:
    return tuple(
        gi_multiply(gi_conjugate(form[row]), form[column])
        for row in range(len(form))
        for column in range(row, len(form))
    )


def difference(left: tuple[GI, ...], right: tuple[GI, ...]) -> tuple[GI, ...]:
    return tuple(gi_subtract(a, b) for a, b in zip(left, right))


def modular_nullspace(matrix: list[list[int]], modulus: int = MODULUS) -> tuple[list[list[int]], tuple[int, ...]]:
    if not matrix:
        return [], ()
    rows = len(matrix)
    columns = len(matrix[0])
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows) if matrix[row][column] % modulus), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column] % modulus, modulus - 2, modulus)
        matrix[pivot_row] = [(value * inverse) % modulus for value in matrix[pivot_row]]
        for row in range(rows):
            factor = matrix[row][column] % modulus
            if row == pivot_row or factor == 0:
                continue
            matrix[row] = [
                (matrix[row][entry] - factor * matrix[pivot_row][entry]) % modulus
                for entry in range(columns)
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    pivot_set = set(pivot_columns)
    free_columns = [column for column in range(columns) if column not in pivot_set]
    basis: list[list[int]] = []
    for free in free_columns:
        vector = [0] * columns
        vector[free] = 1
        for row, pivot in enumerate(pivot_columns):
            vector[pivot] = (-matrix[row][free]) % modulus
        basis.append(vector)
    return basis, tuple(pivot_columns)


def relation_tuples(matchings: tuple[Matching, ...]) -> tuple[list[tuple[int, ...]], int] | None:
    maps = []
    for role in range(3):
        for bit in range(2):
            selected = tuple(
                matchings[mask] for mask in range(8) if ((mask >> role) & 1) == bit
            )
            maps.append(components(selected))
    counts = [max(mapping) + 1 for mapping in maps]
    offsets = []
    running = 0
    for count in counts:
        offsets.append(running)
        running += count
    tuples = [
        tuple(offsets[role] + maps[role][record] for role in range(6))
        for record in range(len(matchings[0]))
    ]
    if len(set(tuples)) != len(tuples):
        return None
    return tuples, running


def analyze_mod(matchings: tuple[Matching, ...]) -> tuple[int, int, int, int] | None:
    data = relation_tuples(matchings)
    if data is None:
        return None
    tuples, variables = data

    def matrix_for(root: int) -> list[list[int]]:
        coefficients = (1, -1, -1, 1, -root, root)
        matrix = []
        for relation in tuples:
            row = [0] * variables
            for variable, coefficient in zip(relation, coefficients):
                row[variable] = (row[variable] + coefficient) % MODULUS
            matrix.append(row)
        return matrix

    plus_basis, plus_pivots = modular_nullspace(matrix_for(I_MOD))
    minus_basis, minus_pivots = modular_nullspace(matrix_for((-I_MOD) % MODULUS))
    if plus_pivots != minus_pivots or not plus_basis:
        return None
    plus_forms = [tuple(vector[variable] for vector in plus_basis) for variable in range(variables)]
    minus_forms = [tuple(vector[variable] for vector in minus_basis) for variable in range(variables)]
    if len(set(plus_forms)) != variables:
        return None
    seen: set[tuple[int, ...]] = set()
    repeats = 0
    for first, second in combinations(range(variables), 2):
        plus = tuple((a - b) % MODULUS for a, b in zip(plus_forms[first], plus_forms[second]))
        minus = tuple((a - b) % MODULUS for a, b in zip(minus_forms[first], minus_forms[second]))
        signature = tuple(
            (minus[row] * plus[column]) % MODULUS
            for row in range(len(plus))
            for column in range(row, len(plus))
        )
        if signature in seen:
            repeats += 1
        else:
            seen.add(signature)
    return variables, len(plus_basis), repeats, len(tuples)


def peel_full_corner_core(relations: list[tuple[int, ...]]) -> int:
    """Return the size of the simultaneous eight-projection two-core."""
    relation_keys = [
        tuple(
            (
                relation[mask & 1],
                relation[2 + ((mask >> 1) & 1)],
                relation[4 + ((mask >> 2) & 1)],
            )
            for mask in range(8)
        )
        for relation in relations
    ]
    fibres: list[dict[tuple[int, int, int], set[int]]] = [dict() for _ in range(8)]
    for index, keys in enumerate(relation_keys):
        for mask, key in enumerate(keys):
            fibres[mask].setdefault(key, set()).add(index)
    alive = [True] * len(relations)
    queue = deque(
        (mask, key)
        for mask in range(8)
        for key, members in fibres[mask].items()
        if len(members) < 2
    )
    while queue:
        mask, key = queue.popleft()
        members = fibres[mask][key]
        if len(members) >= 2:
            continue
        for index in tuple(members):
            if not alive[index]:
                continue
            alive[index] = False
            for other_mask, other_key in enumerate(relation_keys[index]):
                other_members = fibres[other_mask][other_key]
                other_members.discard(index)
                if len(other_members) < 2:
                    queue.append((other_mask, other_key))
    return sum(alive)


def analyze_mod_coalesced(
    matchings: tuple[Matching, ...]
) -> tuple[int, int, int, int, int, int] | None:
    """Analyze after identifying point variables forced equal by the equations.

    Returns (formal variables, geometric points, nullity, norm repetitions,
    distinct relation records, full-core size).
    """
    data = relation_tuples(matchings)
    if data is None:
        return None
    tuples, variables = data

    def matrix_for(root: int) -> list[list[int]]:
        coefficients = (1, -1, -1, 1, -root, root)
        matrix = []
        for relation in tuples:
            row = [0] * variables
            for variable, coefficient in zip(relation, coefficients):
                row[variable] = (row[variable] + coefficient) % MODULUS
            matrix.append(row)
        return matrix

    plus_basis, plus_pivots = modular_nullspace(matrix_for(I_MOD))
    minus_basis, minus_pivots = modular_nullspace(matrix_for((-I_MOD) % MODULUS))
    if plus_pivots != minus_pivots or not plus_basis:
        return None
    plus_forms = [tuple(vector[variable] for vector in plus_basis) for variable in range(variables)]
    minus_forms = [tuple(vector[variable] for vector in minus_basis) for variable in range(variables)]
    form_keys = [(plus_forms[index], minus_forms[index]) for index in range(variables)]
    unique_keys = {key: index for index, key in enumerate(dict.fromkeys(form_keys))}
    classes = [unique_keys[key] for key in form_keys]
    coalesced_relations = sorted(
        set(tuple(classes[variable] for variable in relation) for relation in tuples)
    )
    unique_variables = tuple(dict.fromkeys(classes))
    representatives = [classes.index(variable) for variable in unique_variables]
    seen: set[tuple[int, ...]] = set()
    repeats = 0
    for first, second in combinations(representatives, 2):
        plus = tuple((a - b) % MODULUS for a, b in zip(plus_forms[first], plus_forms[second]))
        minus = tuple((a - b) % MODULUS for a, b in zip(minus_forms[first], minus_forms[second]))
        signature = tuple(
            (minus[row] * plus[column]) % MODULUS
            for row in range(len(plus))
            for column in range(row, len(plus))
        )
        if signature in seen:
            repeats += 1
        else:
            seen.add(signature)
    return (
        variables,
        len(representatives),
        len(plus_basis),
        repeats,
        len(coalesced_relations),
        peel_full_corner_core(coalesced_relations),
    )


def analyze(matchings: tuple[Matching, ...]) -> tuple[int, int, int, int] | None:
    assert len(matchings) == 8
    data = relation_tuples(matchings)
    if data is None:
        return None
    tuples, running = data

    coefficients: tuple[GI, ...] = (ONE, gi_negate(ONE), gi_negate(ONE), ONE, gi_negate(I), I)
    matrix: list[list[GI]] = []
    for relation in tuples:
        row = [ZERO] * running
        for variable, coefficient in zip(relation, coefficients):
            row[variable] = gi_add(row[variable], coefficient)
        matrix.append(row)
    nullspace = rref_nullspace(matrix)
    if not nullspace:
        return None
    forms = [tuple(vector[variable] for vector in nullspace) for variable in range(running)]
    if len(set(forms)) != len(forms):
        return None
    seen: set[tuple[GI, ...]] = set()
    repeats = 0
    for first, second in combinations(range(len(forms)), 2):
        signature = norm_signature(difference(forms[first], forms[second]))
        if signature in seen:
            repeats += 1
        else:
            seen.add(signature)
    return running, len(nullspace), repeats, len(tuples)


def doubled_matchings(permutations: tuple[tuple[int, ...], ...]) -> tuple[Matching, ...]:
    base_size = len(BASE_MATCHINGS[0])
    total = 2 * base_size
    result: list[Matching] = []
    for base in BASE_MATCHINGS:
        result.append(tuple(base[index] + layer * base_size for layer in range(2) for index in range(base_size)))
    for permutation in permutations:
        inverse = [0] * base_size
        for index, value in enumerate(permutation):
            inverse[value] = index
        matching = [0] * total
        for index, value in enumerate(permutation):
            matching[index] = base_size + value
            matching[base_size + value] = index
        result.append(tuple(matching))
    # The four base colours are masks 0--3 (c bit zero), followed by the
    # four cross-layer colours 4--7 (c bit one).
    return tuple(result)


def random_permutations(size: int, rng: random.Random) -> tuple[tuple[int, ...], ...]:
    permutations: list[tuple[int, ...]] = []
    used_by_row = [set() for _ in range(size)]
    for _ in range(4):
        for _attempt in range(1000):
            candidate = list(range(size))
            rng.shuffle(candidate)
            if all(candidate[row] not in used_by_row[row] for row in range(size)):
                permutation = tuple(candidate)
                permutations.append(permutation)
                for row, value in enumerate(permutation):
                    used_by_row[row].add(value)
                break
        else:
            return random_permutations(size, rng)
    return tuple(permutations)


def search(trials: int, seed: int) -> None:
    rng = random.Random(seed)
    best: tuple[int, tuple[tuple[int, ...], ...], tuple[int, int, int, int]] | None = None
    accepted = 0
    for trial in range(trials):
        permutations = random_permutations(16, rng)
        matchings = doubled_matchings(permutations)
        profile = analyze_mod(matchings)
        if profile is None:
            continue
        accepted += 1
        repeats = profile[2]
        if best is None or repeats < best[0]:
            best = repeats, permutations, profile
            print("best", trial, "accepted", accepted, "profile", profile)
            print("permutations", permutations)
        if repeats == 0:
            exact_profile = analyze(matchings)
            print("GENERIC FULL EIGHT-CORNER COUNTEREXAMPLE", exact_profile)
            return
    print("complete", accepted, None if best is None else best[2])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=1208)
    args = parser.parse_args()
    search(args.trials, args.seed)


if __name__ == "__main__":
    main()
