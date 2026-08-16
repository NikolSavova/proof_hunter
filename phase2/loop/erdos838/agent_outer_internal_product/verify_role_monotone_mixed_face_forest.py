#!/usr/bin/env python3
"""Exact checks for ROLE_MONOTONE_MIXED_FACE_FOREST.md."""

from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, product


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (
        b[1] - a[1]
    ) * (c[0] - a[0])


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for point in points:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and orient(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def convex(labels, coordinates):
    return len(hull([coordinates[label] for label in labels])) == len(labels)


def cloud(center, size, sign):
    epsilon = Q(1, 10**5 * size * size)
    return [
        (
            center[0] + epsilon * j,
            center[1] + epsilon * epsilon * sign * j * j,
        )
        for j in range(1, size + 1)
    ]


def anti_aligned_role_cloud(role_count, alphabet_size, released_size):
    completion_size = role_count * alphabet_size
    left = cloud(
        (Q(1, 100), Q(50099, 10000)), completion_size, 1
    )
    right = cloud((Q(0), Q(-4)), released_size, -1)
    coordinates = {}
    roles = []
    cursor = 0
    for role in range(role_count):
        support = []
        for value in range(alphabet_size):
            label = ("A", role, value)
            coordinates[label] = left[cursor]
            cursor += 1
            support.append(label)
        roles.append(tuple(support))
    for index, point in enumerate(right):
        coordinates[("U", index)] = point
    return coordinates, roles


def bad_circuits(left, right, coordinates):
    return [
        frozenset(circuit)
        for circuit in combinations(sorted(left | right), 4)
        if not convex(frozenset(circuit), coordinates)
    ]


def minimum_eligible_role(left, right, coordinates):
    circuits = bad_circuits(left, right, coordinates)
    assert circuits
    roles = [
        label[1]
        for circuit in circuits
        for label in circuit
        if label[0] == "A"
    ]
    assert roles
    return min(roles)


def build_forest(records, coordinates, role_sizes, history=()):
    """Return terminal records and every selected child edge."""
    good = []
    bad_by_role_value = defaultdict(list)
    for record in records:
        original_left, original_right, left_now, right_now, weight = record
        if convex(left_now | right_now, coordinates):
            good.append((record, history))
            continue
        role = minimum_eligible_role(left_now, right_now, coordinates)
        label = next(label for label in left_now if label[1] == role)
        bad_by_role_value[(role, label)].append(record)

    by_role = defaultdict(dict)
    for (role, label), group in bad_by_role_value.items():
        by_role[role][label] = group

    children = []
    for role, label_groups in by_role.items():
        label, group = max(
            label_groups.items(),
            key=lambda item: sum(record[4] for record in item[1]),
        )
        role_mass = sum(
            (record[4] for groups in label_groups.values() for record in groups),
            Q(0),
        )
        child_mass = sum((record[4] for record in group), Q(0))
        assert child_mass >= role_mass / role_sizes[role]
        assert not history or role > history[-1][0]
        multiplicity = len(label_groups)
        child_records = []
        for original_left, original_right, left_now, right_now, weight in group:
            assert label in left_now
            next_left = frozenset(set(left_now) - {label})
            assert convex(next_left, coordinates)
            child_records.append(
                (original_left, original_right, next_left, right_now, weight)
            )
        child_history = history + ((role, label, multiplicity),)
        terminal, descendant_edges = build_forest(
            child_records, coordinates, role_sizes, child_history
        )
        good.extend(terminal)
        children.append((history, child_history, child_mass))
        children.extend(descendant_edges)
    return good, children


def check_forest():
    role_count = 4
    alphabet_size = 2
    released_size = 6
    coordinates, roles = anti_aligned_role_cloud(
        role_count, alphabet_size, released_size
    )
    completions = [
        frozenset(choice) for choice in product(*roles)
    ]
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
            weight = Q(1 + index % 3, 3)
            records.append((left, right, left, right, weight))
            index += 1

    initial_mass = sum((record[4] for record in records), Q(0))
    terminals, edges = build_forest(
        records, coordinates, [alphabet_size] * role_count
    )
    terminal_mass = sum((record[0][4] for record in terminals), Q(0))
    box_volume = alphabet_size**role_count
    assert terminal_mass >= initial_mass / box_volume

    # Every history is strictly role-increasing, and every terminal is good.
    for record, history in terminals:
        assert all(history[i][0] < history[i + 1][0] for i in range(len(history) - 1))
        assert convex(record[2] | record[3], coordinates)
    assert all(
        parent == child[: len(parent)] and len(child) == len(parent) + 1
        for parent, child, _mass in edges
    )

    # The mixed face determines missing roles, hence the unique stored path
    # and the literal original endpoint pair.
    output_weight = defaultdict(Q)
    output_pair = {}
    histories_by_roles = {
        tuple(role for role, _label, _multiplicity in history): history
        for _record, history in terminals
    }
    for record, history in terminals:
        original_left, original_right, left_now, right_now, weight = record
        output = left_now | right_now
        missing_roles = tuple(
            role
            for role in range(role_count)
            if not any(label[0] == "A" and label[1] == role for label in output)
        )
        assert missing_roles == tuple(
            role for role, _label, _multiplicity in history
        )
        # Histories with the same role word are identical because the forest
        # selected one fixed physical label on every child edge.
        stored_history = histories_by_roles[missing_roles]
        recovered_left = frozenset(
            set(label for label in output if label[0] == "A")
            | {label for _role, label, _multiplicity in stored_history}
        )
        recovered_right = frozenset(label for label in output if label[0] == "U")
        recovered = (recovered_left, recovered_right)
        assert recovered == (original_left, original_right)
        assert output_pair.setdefault(output, recovered) == recovered
        output_weight[output] += weight

    pair_cap = Q(1)
    assert all(weight <= pair_cap for weight in output_weight.values())

    # In this anti-aligned instance the opposite trace has rank four, so a
    # selected completion side can remain incompatible until it is empty.
    assert any(len(history) == role_count for _record, history in terminals)


if __name__ == "__main__":
    check_forest()
    print("ROLE_MONOTONE_MIXED_FACE_FOREST verifier: PASS")
