#!/usr/bin/env python3
"""Checks TERMINAL_WEIGHT_FLOOR_EXCESS_RANK_GATE.md."""

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
    "terminal_floor_base_forest", "verify_role_monotone_mixed_face_forest.py"
)
EFFECTIVE = load_module(
    "terminal_floor_effective", "verify_effective_branching_role_forest.py"
)
PREFIX = load_module(
    "terminal_floor_prefix", "verify_excess_rank_prefix_star_coherence_gate.py"
)


def check_geometric_path_upper():
    role_count = 4
    alphabet_size = 3
    coordinates, roles = FOREST.anti_aligned_role_cloud(role_count, alphabet_size, 7)
    completions = [frozenset(choice) for choice in product(*roles)]
    released = sorted(label for label in coordinates if label[0] == "U")
    releases = [frozenset(choice) for choice in combinations(released, 4)]
    records = []
    index = 0
    for left in completions:
        for right in releases:
            weight = Q(1 + index % 7, 7)
            records.append((left, right, left, right, weight))
            index += 1
    root_mass = sum((record[4] for record in records), Q(0))
    terminals = EFFECTIVE.build_effective(records, coordinates)

    grouped_mass = defaultdict(Q)
    grouped_cost = {}
    box_volume = alphabet_size**role_count
    for record, history in terminals:
        output = record[2] | record[3]
        cost = Q(1)
        for _role, _label, ratio in history:
            cost *= ratio
        grouped_mass[output] += record[4]
        assert grouped_cost.setdefault(output, cost) == cost

    for output, mass in grouped_mass.items():
        cost = grouped_cost[output]
        assert mass * cost <= root_mass
        q_value = Q(box_volume, 1) / cost
        assert mass <= root_mass * q_value / box_volume


def check_kraft_equality():
    for s, k, d in [(5, 1, 2), (7, 2, 3), (9, 3, 2), (10, 4, 4)]:
        records = PREFIX.weighted_prefix_star(s, k, d)
        survivors = dict(records)
        root_mass = sum(survivors.values(), Q(0))
        assert root_mass == d**k
        cost = Q(1)
        for role in range(s):
            classes = {
                label: {
                    word: weight
                    for word, weight in survivors.items()
                    if word[role] == label
                }
                for label in range(d)
            }
            masses = {
                label: sum(fibre.values(), Q(0))
                for label, fibre in classes.items()
            }
            assert len(set(masses.values())) == 1
            ratio = sum(masses.values(), Q(0)) / masses[0]
            assert ratio == d
            cost *= ratio
            survivors = classes[0]
        terminal_mass = sum(survivors.values(), Q(0))
        assert terminal_mass == Q(1, d ** (s - k))
        assert terminal_mass * cost == root_mass
        assert Q(d**s, 1) / cost == 1


if __name__ == "__main__":
    check_geometric_path_upper()
    check_kraft_equality()
    print("TERMINAL_WEIGHT_FLOOR_EXCESS_RANK_GATE verifier: PASS")
