#!/usr/bin/env python3
"""Search nongeneric endpoint identifications in abelian corner cores.

This is a conflict-directed search over either Q(i) or a split finite field.
A state is a partition of the formal endpoint labels.  The Gaussian equations
force further point coalescences and, whenever two distinct point-pairs have
the same universal squared-norm form, distance-Sidonicity gives three
possible repairs: identify the pairs in either orientation, or collapse both
pairs to zero.  Every repair is propagated before the next branch.

The default Q(i) mode is the mathematical certificate.  The finite-field
mode is retained as a faster development oracle.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import combinations

from search_edge_disjoint_translation_core import translation_matchings
from search_full_eight_corner_core import (
    I,
    I_MOD,
    MODULUS,
    ONE,
    ZERO,
    difference as exact_difference,
    gi_add,
    gi_negate,
    modular_nullspace,
    norm_signature as exact_norm_signature,
    relation_tuples,
    rref_nullspace,
)


Partition = tuple[int, ...]


def canonical_partition(labels: list[int] | tuple[int, ...]) -> Partition:
    names: dict[int, int] = {}
    return tuple(names.setdefault(value, len(names)) for value in labels)


def merge_partition(state: Partition, pairs: tuple[tuple[int, int], ...]) -> Partition:
    parent = list(range(max(state) + 1))

    def root(value: int) -> int:
        while parent[value] != value:
            parent[value] = parent[parent[value]]
            value = parent[value]
        return value

    for left, right in pairs:
        left_root = root(state[left])
        right_root = root(state[right])
        if left_root != right_root:
            parent[right_root] = left_root
    return canonical_partition([root(value) for value in state])


def matrix_for(
    relations: tuple[tuple[int, ...], ...], variables: int, root: int
) -> list[list[int]]:
    coefficients = (1, -1, -1, 1, -root, root)
    matrix: list[list[int]] = []
    for relation in relations:
        row = [0] * variables
        for variable, coefficient in zip(relation, coefficients):
            row[variable] = (row[variable] + coefficient) % MODULUS
        matrix.append(row)
    return matrix


def difference(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a - b) % MODULUS for a, b in zip(left, right))


def modular_norm_signature(
    plus: tuple[int, ...], minus: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(
        (minus[row] * plus[column]) % MODULUS
        for row in range(len(plus))
        for column in range(row, len(plus))
    )


def dot_signature(
    plus_left: tuple[int, ...],
    minus_left: tuple[int, ...],
    plus_right: tuple[int, ...],
    minus_right: tuple[int, ...],
) -> tuple[int, ...]:
    return tuple(
        (
            minus_left[row] * plus_right[column]
            + minus_right[row] * plus_left[column]
        )
        % MODULUS
        for row in range(len(plus_left))
        for column in range(len(plus_left))
    )


def violates_corner_linearity(relations: tuple[tuple[int, ...], ...]) -> bool:
    keys = [
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
    for left, right in combinations(keys, 2):
        if sum(a == b for a, b in zip(left, right)) >= 2:
            return True
    return False


class PartitionSearch:
    def __init__(
        self,
        relations: tuple[tuple[int, ...], ...],
        variables: int,
        *,
        exact: bool = True,
    ):
        self.formal_relations = relations
        self.variables = variables
        self.exact = exact
        self.memo: set[Partition] = set()
        self.nodes = 0
        self.reasons: defaultdict[str, int] = defaultdict(int)

    def run(self, node_limit: int) -> Partition | None:
        self.node_limit = node_limit
        return self.visit(tuple(range(self.variables)))

    def visit(self, state: Partition) -> Partition | None:
        state = canonical_partition(state)
        if state in self.memo:
            return None
        self.memo.add(state)
        self.nodes += 1
        if self.nodes > self.node_limit:
            raise RuntimeError(("node-limit", self.node_limit, dict(self.reasons)))

        relations = tuple(
            tuple(state[variable] for variable in relation)
            for relation in self.formal_relations
        )
        if any(
            relation[0] == relation[1]
            or relation[2] == relation[3]
            or relation[4] == relation[5]
            for relation in relations
        ):
            self.reasons["zero-relation-edge"] += 1
            return None
        if len(set(relations)) != len(relations):
            self.reasons["record-collapse"] += 1
            return None
        if violates_corner_linearity(relations):
            self.reasons["corner-nonlinearity"] += 1
            return None

        count = max(state) + 1
        if self.exact:
            coefficients = (
                ONE,
                gi_negate(ONE),
                gi_negate(ONE),
                ONE,
                gi_negate(I),
                I,
            )
            exact_matrix = []
            for relation in relations:
                row = [ZERO] * count
                for variable, coefficient in zip(relation, coefficients):
                    row[variable] = gi_add(row[variable], coefficient)
                exact_matrix.append(row)
            basis = rref_nullspace(exact_matrix)
            if not basis:
                self.reasons["rank-mismatch"] += 1
                return None
            forms = [
                tuple(vector[variable] for vector in basis)
                for variable in range(count)
            ]
        else:
            plus_basis, plus_pivots = modular_nullspace(
                matrix_for(relations, count, I_MOD)
            )
            minus_basis, minus_pivots = modular_nullspace(
                matrix_for(relations, count, (-I_MOD) % MODULUS)
            )
            if plus_pivots != minus_pivots or not plus_basis:
                self.reasons["rank-mismatch"] += 1
                return None
            plus_forms = [
                tuple(vector[variable] for vector in plus_basis)
                for variable in range(count)
            ]
            minus_forms = [
                tuple(vector[variable] for vector in minus_basis)
                for variable in range(count)
            ]

        forced: list[tuple[int, int]] = []
        by_form: dict[object, int] = {}
        representatives = [state.index(variable) for variable in range(count)]
        form_keys = forms if self.exact else list(zip(plus_forms, minus_forms))
        for variable, key in enumerate(form_keys):
            if key in by_form:
                forced.append((representatives[variable], representatives[by_form[key]]))
            else:
                by_form[key] = variable
        if forced:
            next_state = merge_partition(state, tuple(forced))
            if next_state == state:
                raise AssertionError(forced)
            self.reasons["forced-point-coalescence"] += 1
            return self.visit(next_state)

        # The finite-field oracle can cheaply reject an identically
        # nontransverse branch.  The exact proof does not need this rejection:
        # retaining additional branches only strengthens an exhaustion result.
        if not self.exact:
            for relation in relations:
                d_plus = difference(plus_forms[relation[0]], plus_forms[relation[1]])
                d_minus = difference(minus_forms[relation[0]], minus_forms[relation[1]])
                e_plus = difference(plus_forms[relation[4]], plus_forms[relation[5]])
                e_minus = difference(minus_forms[relation[4]], minus_forms[relation[5]])
                if not any(dot_signature(d_plus, d_minus, e_plus, e_minus)):
                    self.reasons["forced-nontransverse"] += 1
                    return None

        pair_by_signature: dict[object, tuple[int, int]] = {}
        conflict: tuple[tuple[int, int], tuple[int, int]] | None = None
        for left, right in combinations(range(count), 2):
            if self.exact:
                signature = exact_norm_signature(
                    exact_difference(forms[left], forms[right])
                )
            else:
                plus = difference(plus_forms[left], plus_forms[right])
                minus = difference(minus_forms[left], minus_forms[right])
                signature = modular_norm_signature(plus, minus)
            pair = representatives[left], representatives[right]
            if signature in pair_by_signature:
                conflict = pair_by_signature[signature], pair
                break
            pair_by_signature[signature] = pair
        if conflict is None:
            self.reasons["survivor"] += 1
            return state

        (a, b), (c, d) = conflict
        branches = (
            ((a, c), (b, d)),
            ((a, d), (b, c)),
            ((a, b), (c, d)),
        )
        self.reasons["norm-conflict"] += 1
        for pairs in branches:
            next_state = merge_partition(state, pairs)
            if next_state == state:
                continue
            answer = self.visit(next_state)
            if answer is not None:
                return answer
        return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dimension", type=int, default=8)
    parser.add_argument(
        "--shifts", default="1,2,4,8,16,32,64,128",
        help="comma-separated nonzero translation shifts",
    )
    parser.add_argument("--node-limit", type=int, default=1_000_000)
    parser.add_argument("--modular", action="store_true")
    args = parser.parse_args()
    shifts = tuple(int(value) for value in args.shifts.split(","))
    matchings = translation_matchings(args.dimension, shifts)
    data = relation_tuples(matchings)
    if data is None:
        raise SystemExit("record collapse before search")
    formal_relations, variables = data
    search = PartitionSearch(
        tuple(formal_relations), variables, exact=not args.modular
    )
    answer = search.run(args.node_limit)
    print("nodes", search.nodes)
    print("reasons", dict(search.reasons))
    print("survivor", answer)


if __name__ == "__main__":
    main()
