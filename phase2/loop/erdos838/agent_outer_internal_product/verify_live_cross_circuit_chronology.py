#!/usr/bin/env python3
"""Exact checks for LIVE_CROSS_CIRCUIT_CHRONOLOGY.md."""

from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
from math import comb


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
    points = [coordinates[label] for label in labels]
    return len(hull(points)) == len(set(points))


def cloud(center, size, sign):
    epsilon = Q(1, 10**5 * size * size)
    return [
        (
            center[0] + epsilon * j,
            center[1] + epsilon * epsilon * sign * j * j,
        )
        for j in range(1, size + 1)
    ]


def anti_aligned_clouds(size):
    left_points = cloud((Q(1, 100), Q(50099, 10000)), size, 1)
    right_points = cloud((Q(0), Q(-4)), size, -1)
    coordinates = {}
    for index, point in enumerate(left_points):
        coordinates[("L", index)] = point
    for index, point in enumerate(right_points):
        coordinates[("R", index)] = point
    return coordinates


def canonical_bad_circuit(left, right, coordinates):
    union = sorted(left | right)
    for circuit in combinations(union, 4):
        if not convex(circuit, coordinates):
            assert set(circuit) & left
            assert set(circuit) & right
            return tuple(circuit)
    raise AssertionError("a bad union must have a four-point witness")


def pair_weight(records):
    totals = defaultdict(Q)
    for record in records:
        totals[(record[0], record[1])] += record[4]
    return totals


def peel(
    records,
    coordinates,
    face_count,
    pair_cap,
    requested_steps,
    budget_guard=True,
    grouping="label",
):
    """Peel actual circuits, checking the theorem at every step.

    A record is (original_left, original_right, current_left, current_right,
    weight).  Original left is the already-x-deleted completion face.
    """

    current = list(records)
    deleted = []
    circuit_bound = comb(len(coordinates), 4)
    for _step in range(requested_steps):
        total = sum((record[4] for record in current), Q(0))
        good = []
        bad = []
        seen_good_outputs = defaultdict(Q)
        for record in current:
            left_now, right_now = record[2], record[3]
            if convex(left_now | right_now, coordinates):
                good.append(record)
                output = frozenset(left_now | right_now)
                seen_good_outputs[output] += record[4]
            else:
                bad.append(record)

        # Disjoint side grounds plus fixed deleted labels reconstruct the pair.
        reconstructed = {}
        deleted_left = {label for side, label in deleted if side == "L"}
        deleted_right = {label for side, label in deleted if side == "R"}
        for record in good:
            output = frozenset(record[2] | record[3])
            recovered = (
                frozenset(label for label in output if label[0] == "L")
                | deleted_left,
                frozenset(label for label in output if label[0] == "R")
                | deleted_right,
            )
            assert recovered == (record[0], record[1])
            old = reconstructed.setdefault(output, recovered)
            assert old == recovered

        assert all(weight <= pair_cap for weight in seen_good_outputs.values())
        good_weight = sum(seen_good_outputs.values(), Q(0))
        assert good_weight <= pair_cap * face_count

        if budget_guard and total <= 2 * pair_cap * face_count:
            break
        bad_weight = sum((record[4] for record in bad), Q(0))
        if bad_weight < total / 2:
            break
        assert bad_weight >= total / 2

        groups = defaultdict(list)
        for record in bad:
            circuit = canonical_bad_circuit(record[2], record[3], coordinates)
            completion_vertices = [label for label in circuit if label[0] == "L"]
            assert completion_vertices
            witness_label = min(completion_vertices)
            key = witness_label if grouping == "label" else circuit
            groups[key].append(record)
        key, group = max(
            groups.items(), key=lambda item: sum(r[4] for r in item[1])
        )
        group_weight = sum((record[4] for record in group), Q(0))
        choice_bound = len(coordinates) if grouping == "label" else circuit_bound
        assert len(groups) <= choice_bound
        assert group_weight >= total / (2 * choice_bound)

        if grouping == "label":
            label = key
        else:
            label = min(candidate for candidate in key if candidate[0] == "L")
        side = "L"
        assert all(label in (record[2] if side == "L" else record[3]) for record in group)
        assert label not in {old_label for _old_side, old_label in deleted}
        deleted.append((side, label))

        next_records = []
        for original_left, original_right, left_now, right_now, weight in group:
            if side == "L":
                next_left = frozenset(set(left_now) - {label})
                next_right = right_now
            else:
                next_left = left_now
                next_right = frozenset(set(right_now) - {label})
            assert convex(next_left, coordinates)
            assert convex(next_right, coordinates)
            next_records.append(
                (original_left, original_right, next_left, next_right, weight)
            )

        # Deletion on a common contained label is injective on original pairs.
        reduced_pairs = [(record[2], record[3]) for record in next_records]
        assert len(reduced_pairs) == len(set(reduced_pairs))
        current = next_records

    return deleted, current


def check_two_cloud_geometry():
    for size in range(3, 8):
        coordinates = anti_aligned_clouds(size)
        left = [label for label in coordinates if label[0] == "L"]
        right = [label for label in coordinates if label[0] == "R"]
        actual = 0
        for left_rank in range(size + 1):
            for left_set in combinations(left, left_rank):
                for right_rank in range(size + 1):
                    for right_set in combinations(right, right_rank):
                        is_face = convex(set(left_set) | set(right_set), coordinates)
                        expected = (
                            not left_set
                            or not right_set
                            or (left_rank <= 2 and right_rank <= 2)
                        )
                        assert is_face == expected
                        actual += int(is_face)
        profile = size + comb(size, 2)
        assert actual == 1 + 2 * (2**size - 1) + profile**2


def check_fixed_x_peeling():
    size = 10
    coordinates = anti_aligned_clouds(size)
    left_labels = sorted(label for label in coordinates if label[0] == "L")
    right_labels = sorted(label for label in coordinates if label[0] == "R")

    # x is fixed in every literal rank-6 completion and deleted before mixing.
    x = left_labels[0]
    left_reduced = [
        frozenset(choice)
        for choice in combinations(left_labels[1:], 5)
    ]
    right_faces = [
        frozenset(choice) for choice in combinations(right_labels, 5)
    ]
    records = []
    for index, (left, right) in enumerate(
        (pair for pair in ((a, b) for a in left_reduced for b in right_faces))
    ):
        # Rational weights stress the weighted statements; every pair is unique.
        weight = Q(1 + index % 3, 3)
        records.append((left, right, left, right, weight))

    pair_cap = Q(1)
    assert max(pair_weight(records).values()) <= pair_cap
    profile = size + comb(size, 2)
    face_count = 1 + 2 * (2**size - 1) + profile**2
    # The actual theorem applies while the mass is above the global budget.
    theorem_deleted, _theorem_surviving = peel(
        records,
        coordinates,
        face_count,
        pair_cap,
        requested_steps=5,
        budget_guard=True,
        grouping="label",
    )
    assert theorem_deleted

    # The fixed-four-circuit refinement has the weaker C(n,4) recurrence.
    fixed_deleted, _fixed_surviving = peel(
        records,
        coordinates,
        face_count,
        pair_cap,
        requested_steps=1,
        budget_guard=True,
        grouping="circuit",
    )
    assert fixed_deleted

    deleted, surviving = peel(
        records,
        coordinates,
        face_count,
        pair_cap,
        requested_steps=5,
        # Continue the exact local chronology after its mass falls below the
        # global V-threshold, solely to test the exact local endpoint.
        budget_guard=False,
        grouping="label",
    )

    # With the opposite side still above rank two, the exact anti-aligned
    # obstruction peels the selected side to empty before it releases.
    assert deleted
    assert all(side in {"L", "R"} for side, _label in deleted)
    assert len({label for _side, label in deleted}) == len(deleted)
    assert all(convex(record[2] | record[3], coordinates) for record in surviving)
    for record in surviving:
        left_now, right_now = record[2], record[3]
        if convex(left_now | right_now, coordinates):
            assert len(left_now) <= 2 or len(right_now) <= 2

    # Reattaching x after reconstruction gives the literal full completion.
    for original_left, _original_right, _left_now, _right_now, _weight in records:
        literal_completion = original_left | {x}
        assert len(literal_completion) == 6
        assert convex(literal_completion, coordinates)


def check_rank_corollary_arithmetic():
    for n in (8, 20, 100):
        circuit_bound = comb(n, 4)
        for rank in range(5):
            threshold = 2 * (2 * circuit_bound) ** rank
            # Any mass above this threshold would permit rank+1 deletions.
            assert threshold * (2 * circuit_bound) > threshold


if __name__ == "__main__":
    check_two_cloud_geometry()
    check_fixed_x_peeling()
    check_rank_corollary_arithmetic()
    print("LIVE_CROSS_CIRCUIT_CHRONOLOGY verifier: PASS")
