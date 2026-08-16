#!/usr/bin/env python3
"""Checks EFFECTIVE_BRANCHING_ROLE_FOREST.md."""

from collections import defaultdict
from fractions import Fraction as Q
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_module(name, filename):
    spec = spec_from_file_location(name, HERE / filename)
    module = module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


FOREST = load_module(
    "role_forest_effective_base", "verify_role_monotone_mixed_face_forest.py"
)
PREFIX = load_module(
    "prefix_star_effective_base",
    "verify_excess_rank_prefix_star_coherence_gate.py",
)


def build_effective(records, coordinates, history=()):
    terminals = []
    bad_by_role_value = defaultdict(list)
    for record in records:
        original_left, original_right, left_now, right_now, weight = record
        if FOREST.convex(left_now | right_now, coordinates):
            terminals.append((record, history))
            continue
        role = FOREST.minimum_eligible_role(left_now, right_now, coordinates)
        label = next(label for label in left_now if label[1] == role)
        bad_by_role_value[(role, label)].append(record)

    by_role = defaultdict(dict)
    for (role, label), group in bad_by_role_value.items():
        by_role[role][label] = group

    for role, label_groups in by_role.items():
        mass_by_label = {
            label: sum((record[4] for record in group), Q(0))
            for label, group in label_groups.items()
        }
        label = max(mass_by_label, key=mass_by_label.get)
        group = label_groups[label]
        total_mass = sum(mass_by_label.values(), Q(0))
        child_mass = mass_by_label[label]
        ratio = total_mass / child_mass
        child_records = []
        for original_left, original_right, left_now, right_now, weight in group:
            next_left = frozenset(set(left_now) - {label})
            child_records.append(
                (original_left, original_right, next_left, right_now, weight)
            )
        terminals.extend(
            build_effective(
                child_records,
                coordinates,
                history + ((role, label, ratio),),
            )
        )
    return terminals


def check_geometric_forest():
    role_count = 4
    alphabet_size = 3
    released_size = 7
    coordinates, roles = FOREST.anti_aligned_role_cloud(
        role_count, alphabet_size, released_size
    )
    completions = [frozenset(choice) for choice in product(*roles)]
    released_labels = sorted(label for label in coordinates if label[0] == "U")
    releases = [frozenset(choice) for choice in combinations(released_labels, 4)]

    records = []
    index = 0
    for left in completions:
        for right in releases:
            weight = Q(1 + index % 5, 5)
            records.append((left, right, left, right, weight))
            index += 1

    initial_mass = sum((record[4] for record in records), Q(0))
    terminals = build_effective(records, coordinates)
    box_volume = alphabet_size**role_count
    potential = Q(0)
    output_mass = defaultdict(Q)
    output_cost = {}
    output_q = {}

    for record, history in terminals:
        cost = Q(1)
        deleted = set()
        for role, _label, ratio in history:
            cost *= ratio
            deleted.add(role)
        unspent = Q(box_volume, 1) / cost
        factorized = Q(1)
        history_ratio = {role: ratio for role, _label, ratio in history}
        for role in range(role_count):
            if role in deleted:
                factorized *= Q(alphabet_size, 1) / history_ratio[role]
            else:
                factorized *= alphabet_size
        assert factorized == unspent

        output = record[2] | record[3]
        assert FOREST.convex(output, coordinates)
        output_mass[output] += record[4]
        assert output_cost.setdefault(output, cost) == cost
        assert output_q.setdefault(output, unspent) == unspent
        potential += record[4] * cost

    assert potential >= initial_mass
    pair_load = Q(1)
    assert all(mass <= pair_load for mass in output_mass.values())

    for threshold in sorted(set(output_q.values())):
        high = sum(
            output_mass[output] * output_cost[output]
            for output in output_mass
            if output_q[output] >= threshold
        )
        count = sum(output_q[output] >= threshold for output in output_mass)
        assert high <= pair_load * count * box_volume / threshold


def check_prefix_telescope():
    for s, k, d in [(5, 1, 2), (7, 2, 3), (9, 3, 2), (10, 4, 4)]:
        words = PREFIX.prefix_star(s, k, d)
        survivors = set(words)
        cost = Q(1)
        for role in range(s):
            classes = {
                label: {word for word in survivors if word[role] == label}
                for label in range(d)
            }
            nonempty = {label: fibre for label, fibre in classes.items() if fibre}
            assert len(nonempty) == d
            selected = nonempty[0]
            assert len(selected) == max(map(len, nonempty.values()))
            ratio = Q(len(survivors), len(selected))
            cost *= ratio
            survivors = selected
        assert survivors == {(0,) * s}
        assert cost == len(words)
        assert Q(d**s, 1) / cost == Q(d**s, len(words))


if __name__ == "__main__":
    check_geometric_forest()
    check_prefix_telescope()
    print("EFFECTIVE_BRANCHING_ROLE_FOREST verifier: PASS")
