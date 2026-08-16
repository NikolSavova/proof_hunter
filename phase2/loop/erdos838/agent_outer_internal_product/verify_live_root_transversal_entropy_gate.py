#!/usr/bin/env python3
"""Checks for LIVE_ROOT_TRANSVERSAL_ENTROPY_GATE.md."""

from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations


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


def anti_aligned_clouds(size):
    coordinates = {}
    for index, point in enumerate(
        cloud((Q(1, 100), Q(50099, 10000)), size, 1)
    ):
        coordinates[("A", index)] = point
    for index, point in enumerate(cloud((Q(0), Q(-4)), size, -1)):
        coordinates[("U", index)] = point
    return coordinates


def canonical_circuit(left, right, coordinates):
    for circuit in combinations(sorted(left | right), 4):
        if not convex(frozenset(circuit), coordinates):
            assert set(circuit) & left and set(circuit) & right
            return frozenset(circuit)
    raise AssertionError("bad union without four-circuit")


def minimum_transversal(edges):
    ground = sorted(set().union(*edges))
    for rank in range(1, len(ground) + 1):
        for choice in combinations(ground, rank):
            chosen = frozenset(choice)
            if all(chosen & edge for edge in edges):
                return chosen
    raise AssertionError("nonempty-edge hypergraph has a transversal")


def matching_number(edges):
    edges = list(dict.fromkeys(edges))
    best = 0
    for mask in range(1 << len(edges)):
        chosen = [edge for i, edge in enumerate(edges) if mask >> i & 1]
        if all(not a & b for i, a in enumerate(chosen) for b in chosen[i + 1 :]):
            best = max(best, len(chosen))
    return best


def weighted_dispersion(edges, weights):
    total = sum(weights, Q(0))
    loads = defaultdict(Q)
    for edge, weight in zip(edges, weights):
        for vertex in edge:
            loads[vertex] += weight
    return total / max(loads.values()), loads


def descend(records, coordinates, face_count, pair_cap, budget_guard):
    """Released-side adaptive transversal descent."""
    current = list(records)
    deleted = []
    transcript = []
    while current:
        total = sum((record[4] for record in current), Q(0))
        good = []
        bad = []
        traces = []
        for record in current:
            left_now, right_now = record[2], record[3]
            if convex(left_now | right_now, coordinates):
                good.append(record)
            else:
                circuit = canonical_circuit(left_now, right_now, coordinates)
                trace = frozenset(label for label in circuit if label[0] == "U")
                assert trace
                bad.append(record)
                traces.append(trace)

        # A good output recovers both reduced grounds and the fixed deletions.
        output_weights = defaultdict(Q)
        output_pairs = {}
        deleted_set = frozenset(deleted)
        for record in good:
            output = record[2] | record[3]
            output_weights[output] += record[4]
            recovered = (
                frozenset(label for label in output if label[0] == "A"),
                frozenset(label for label in output if label[0] == "U")
                | deleted_set,
            )
            assert recovered == (record[0], record[1])
            assert output_pairs.setdefault(output, recovered) == recovered
        assert all(weight <= pair_cap for weight in output_weights.values())
        assert sum(output_weights.values(), Q(0)) <= pair_cap * face_count

        if not bad:
            break
        if budget_guard and total <= 2 * pair_cap * face_count:
            break
        bad_weight = sum((record[4] for record in bad), Q(0))
        if bad_weight < total / 2:
            break

        bad_weights = [record[4] for record in bad]
        dispersion, loads = weighted_dispersion(traces, bad_weights)
        root = max(loads, key=loads.get)
        group = [record for record, trace in zip(bad, traces) if root in trace]
        retained_weight = sum((record[4] for record in group), Q(0))
        assert retained_weight == loads[root]
        assert retained_weight >= total / (2 * dispersion)
        assert root not in deleted
        deleted.append(root)
        transcript.append(
            (dispersion, traces, bad_weights, retained_weight, total)
        )

        next_records = []
        for original_left, original_right, left_now, right_now, weight in group:
            assert root in right_now
            next_right = frozenset(set(right_now) - {root})
            assert convex(next_right, coordinates)
            next_records.append(
                (original_left, original_right, left_now, next_right, weight)
            )
        current = next_records
    return deleted, current, transcript


def check_hypergraph_matching_bound():
    examples = [
        [{0}, {1}, {2}],
        [{0, 1, 2}, {2, 3}, {3, 4, 5}, {5, 6}],
        [{0, 1}, {0, 2}, {0, 3}],
        [{0, 1, 2}, {3, 4, 5}, {1, 4, 6}],
    ]
    for raw_edges in examples:
        edges = [frozenset(edge) for edge in raw_edges]
        tau = len(minimum_transversal(edges))
        nu = matching_number(edges)
        weights = [Q(1 + index % 3, 3) for index in range(len(edges))]
        dispersion, _loads = weighted_dispersion(edges, weights)
        assert tau <= 3 * nu
        assert dispersion <= 3 * nu


def make_records(size, left_rank, right_faces):
    coordinates = anti_aligned_clouds(size)
    left_labels = sorted(label for label in coordinates if label[0] == "A")
    left_sets = [frozenset(choice) for choice in combinations(left_labels, left_rank)]
    records = []
    index = 0
    for left in left_sets:
        for right in right_faces:
            weight = Q(1 + index % 2, 2)
            records.append((left, right, left, right, weight))
            index += 1
    return coordinates, records


def check_stationary_and_spread():
    size = 8
    all_coordinates = anti_aligned_clouds(size)
    right_labels = sorted(label for label in all_coordinates if label[0] == "U")

    # The released endpoint is one fixed triangle.  Its successive canonical
    # traces have singleton covers until the root is exhausted.
    root = frozenset(right_labels[:3])
    stationary_right = [root]
    coordinates, records = make_records(size, 4, stationary_right)
    profile = size + size * (size - 1) // 2
    face_count = 1 + 2 * (2**size - 1) + profile**2
    deleted, surviving, transcript = descend(
        records, coordinates, face_count, Q(1), budget_guard=False
    )
    assert transcript
    assert all(
        dispersion <= 3
        for dispersion, _traces, _weights, _kept, _total in transcript
    )
    assert len(deleted) == 3
    assert all(convex(record[2] | record[3], coordinates) for record in surviving)

    # The full rank layer has genuinely spread canonical released roots.
    spread_right = [frozenset(choice) for choice in combinations(right_labels, 5)]
    coordinates, records = make_records(size, 4, spread_right)
    _deleted, _surviving, spread_transcript = descend(
        records, coordinates, face_count, Q(1), budget_guard=False
    )
    assert spread_transcript
    assert max(
        dispersion
        for dispersion, _traces, _weights, _kept, _total in spread_transcript
    ) > 1


if __name__ == "__main__":
    check_hypergraph_matching_bound()
    check_stationary_and_spread()
    print("LIVE_ROOT_TRANSVERSAL_ENTROPY_GATE verifier: PASS")
