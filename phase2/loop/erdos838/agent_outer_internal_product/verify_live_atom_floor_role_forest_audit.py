#!/usr/bin/env python3
"""Checks LIVE_ATOM_FLOOR_ROLE_FOREST_AUDIT.md."""

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
    "atom_floor_forest", "verify_role_monotone_mixed_face_forest.py"
)
EFFECTIVE = load_module(
    "atom_floor_effective", "verify_effective_branching_role_forest.py"
)
PREFIX = load_module(
    "atom_floor_prefix", "verify_excess_rank_prefix_star_coherence_gate.py"
)


def check_atom_operations():
    n = 37
    weights = [Q(value, n) for value in [1, 2, 5, 11]]
    assert min(weights) == Q(1, n)
    restricted = weights[::2]
    duplicated = [(weight, tag) for weight in restricted for tag in range(3)]
    assert min(weight for weight, _tag in duplicated) >= Q(1, n)
    coalesced = defaultdict(Q)
    for weight, tag in duplicated:
        coalesced[tag] += weight
    assert min(coalesced.values()) >= Q(1, n)
    # Dyadic upper rounding: smallest power of two reciprocal above weight.
    rounded = []
    for weight in weights:
        candidate = Q(1)
        while candidate / 2 >= weight:
            candidate /= 2
        rounded.append(candidate)
        assert weight <= candidate < 2 * weight
    assert min(rounded) >= Q(1, n)


def check_mass_to_count():
    # Exact weights 2 and 3 lie in one factor-two bin [2,4).
    for class_count in range(1, 5):
        for counts in product(range(1, 6), repeat=class_count):
            for class_weights in product((2, 3), repeat=class_count):
                masses = [
                    count * weight
                    for count, weight in zip(counts, class_weights)
                ]
                chosen = max(range(class_count), key=lambda index: masses[index])
                total_count = sum(counts)
                max_count = max(counts)
                ratio = Q(sum(masses), masses[chosen])
                count_ratio = Q(total_count, max_count)
                assert ratio >= count_ratio / 2
                assert ratio <= 4 * count_ratio
                assert 2 * counts[chosen] >= max_count


def check_geometric_fibres():
    role_count = 4
    alphabet_size = 3
    n = 101
    coordinates, roles = FOREST.anti_aligned_role_cloud(role_count, alphabet_size, 7)
    completions = [frozenset(choice) for choice in product(*roles)]
    released = sorted(label for label in coordinates if label[0] == "U")
    releases = [frozenset(choice) for choice in combinations(released, 4)]
    box_volume = alphabet_size**role_count

    # Run independently in each fixed released-face fibre.
    for fibre_index, right in enumerate(releases[:5]):
        records = []
        for index, left in enumerate(completions):
            weight = Q(1 + (index + fibre_index) % 5, n)
            records.append((left, right, left, right, weight))
        fibre_mass = sum((record[4] for record in records), Q(0))
        terminals = EFFECTIVE.build_effective(records, coordinates)
        grouped_mass = defaultdict(Q)
        grouped_cost = {}
        for record, history in terminals:
            output = record[2] | record[3]
            cost = Q(1)
            for _role, _label, ratio in history:
                cost *= ratio
            grouped_mass[output] += record[4]
            assert grouped_cost.setdefault(output, cost) == cost
        for output, mass in grouped_mass.items():
            cost = grouped_cost[output]
            assert mass >= Q(1, n)
            assert cost <= fibre_mass / mass
            q_effective = Q(box_volume, 1) / cost
            assert q_effective >= Q(box_volume, 1) / (n * fibre_mass)


def check_rectangle_cancellation():
    s, k, d, released_count = 7, 2, 3, 11
    words = PREFIX.prefix_star(s, k, d)
    completion_count = len(words)
    box_volume = d**s
    total_records = completion_count * released_count

    # One identical zero-path forest per released column.
    for _released in range(released_count):
        survivors = set(words)
        cost = Q(1)
        for role in range(s):
            classes = {
                label: {word for word in survivors if word[role] == label}
                for label in range(d)
            }
            selected = classes[0]
            assert len(selected) == max(map(len, classes.values()))
            cost *= Q(len(survivors), len(selected))
            survivors = selected
        assert survivors == {(0,) * s}
        assert cost == completion_count
        assert Q(box_volume, 1) / cost == Q(box_volume, completion_count)

    terminal_face_count = released_count
    terminal_potential = released_count * completion_count
    assert terminal_potential == total_records
    # Exact degrees of K_{completion_count,released_count}.
    assert total_records // completion_count == released_count
    assert total_records // released_count == completion_count
    assert terminal_face_count == released_count


if __name__ == "__main__":
    check_atom_operations()
    check_mass_to_count()
    check_geometric_fibres()
    check_rectangle_cancellation()
    print("LIVE_ATOM_FLOOR_ROLE_FOREST_AUDIT verifier: PASS")
