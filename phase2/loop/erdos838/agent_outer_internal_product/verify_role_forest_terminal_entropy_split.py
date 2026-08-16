#!/usr/bin/env python3
"""Checks for ROLE_FOREST_TERMINAL_ENTROPY_SPLIT.md."""

from collections import defaultdict
from fractions import Fraction as Q
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "role_forest",
    HERE / "verify_role_monotone_mixed_face_forest.py",
)
ROLE_FOREST = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(ROLE_FOREST)


def terminal_data():
    role_count = 4
    alphabet_size = 3
    released_size = 7
    coordinates, roles = ROLE_FOREST.anti_aligned_role_cloud(
        role_count, alphabet_size, released_size
    )
    completions = [frozenset(choice) for choice in product(*roles)]
    released_labels = sorted(
        label for label in coordinates if label[0] == "U"
    )
    releases = [
        frozenset(choice) for choice in combinations(released_labels, 4)
    ]
    records = []
    index = 0
    for left in completions:
        for right in releases:
            weight = Q(1 + index % 4, 4)
            records.append((left, right, left, right, weight))
            index += 1
    terminals, _edges = ROLE_FOREST.build_forest(
        records,
        coordinates,
        [alphabet_size] * role_count,
    )
    return (
        coordinates,
        records,
        terminals,
        role_count,
        alphabet_size,
    )


def check_terminal_potential():
    (
        coordinates,
        records,
        terminals,
        role_count,
        alphabet_size,
    ) = terminal_data()
    initial_mass = sum((record[4] for record in records), Q(0))
    box_volume = alphabet_size**role_count

    output_weight = defaultdict(Q)
    output_cost = {}
    output_q = {}
    potential = Q(0)
    saw_all_deleted = False
    for record, history in terminals:
        output = record[2] | record[3]
        cost = 1
        deleted_roles = set()
        for role, _label, multiplicity in history:
            cost *= multiplicity
            deleted_roles.add(role)
        unspent = Q(box_volume, cost)
        factorized = Q(1)
        history_by_role = {
            role: multiplicity for role, _label, multiplicity in history
        }
        for role in range(role_count):
            if role in deleted_roles:
                factorized *= Q(alphabet_size, history_by_role[role])
            else:
                factorized *= alphabet_size
        assert factorized == unspent
        output_weight[output] += record[4]
        assert output_cost.setdefault(output, cost) == cost
        assert output_q.setdefault(output, unspent) == unspent
        potential += record[4] * cost
        if len(deleted_roles) == role_count:
            saw_all_deleted = True
            assert cost == box_volume
            assert unspent == 1
        assert ROLE_FOREST.convex(output, coordinates)

    assert potential >= initial_mass
    pair_cap = Q(1)
    assert all(weight <= pair_cap for weight in output_weight.values())
    assert saw_all_deleted

    # Check the threshold capacity inequality using the sharper number of
    # actually attained outputs (hence also with the ambient V bound).
    thresholds = sorted(set(output_q.values()))
    for threshold in thresholds:
        high_potential = sum(
            output_weight[output] * output_cost[output]
            for output in output_weight
            if output_q[output] >= threshold
        )
        high_outputs = sum(
            1 for output in output_weight if output_q[output] >= threshold
        )
        assert high_potential <= Q(
            pair_cap * high_outputs * box_volume, threshold
        )


def check_role_am_gm():
    examples = [
        [3, 3, 3, 3],
        [1, 2, 5, 9],
        [2, 7, 11],
        [1, 1, 1, 20],
    ]
    for sizes in examples:
        support = sum(sizes)
        rank = len(sizes)
        volume = 1
        for size in sizes:
            volume *= size
        # Exact integer form of prod d_i <= (N/s)^s.
        assert volume * rank**rank <= support**rank


if __name__ == "__main__":
    check_terminal_potential()
    check_role_am_gm()
    print("ROLE_FOREST_TERMINAL_ENTROPY_SPLIT verifier: PASS")
