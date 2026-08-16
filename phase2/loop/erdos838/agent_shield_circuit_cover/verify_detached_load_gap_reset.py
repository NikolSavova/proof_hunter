#!/usr/bin/env python3
"""Exact checks for detached two-bank recovery and gap-reset regression."""

from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import sys


COMMON = Path(__file__).resolve().parents[1] / "agent_common_shield_mixing"
sys.path.insert(0, str(COMMON))
from verify_mixed_seam_vertex_cover_pi2 import convex, hull, orient  # noqa: E402


def point_on_edge(index, parameter, depth):
    """Point below edge P_i P_(i+1) of the parabola chain."""
    return (Q(index) + parameter,
            Q(index * index) + parameter * Q(2 * index + 1) - depth)


def gap_reset_regression(q=3, tail_size=3):
    core = [(Q(i), Q(i * i)) for i in range(2 * q + 2)]
    tail = [(Q(i), Q(i * i))
            for i in range(2 * q + 2, 2 * q + 2 + tail_size)]
    pocket = []
    pairs = []
    for role in range(q):
        edge = 2 * role
        x = point_on_edge(edge, Q(1, 2), Q(1, 10))
        a = point_on_edge(edge, Q(1, 4), Q(3, 100))
        b = point_on_edge(edge, Q(3, 4), Q(3, 100))
        pocket.append(x)
        pairs.append((a, b))

    universe = core + tail + pocket + [v for pair in pairs for v in pair]
    assert all(orient(*triple) for triple in combinations(universe, 3))
    assert convex(core + tail)
    assert convex(core + tail + pocket)

    contexts = []
    detached_records = []
    pair_records = []
    for mask in range(1 << tail_size):
        selected_tail = [tail[i] for i in range(tail_size) if mask >> i & 1]
        base = core + selected_tail
        released = base + pocket
        assert convex(base) and convex(released)
        boundary = hull(released)
        boundary_edges = {
            frozenset((boundary[i], boundary[(i + 1) % len(boundary)]))
            for i in range(len(boundary))
        }
        for role, (a, b) in enumerate(pairs):
            old_gap = frozenset((core[2 * role], core[2 * role + 1]))
            assert old_gap not in boundary_edges
            assert convex(base + [a]) and convex(base + [b])
            assert convex(base + [a, b])
            assert not convex(released + [a])
            assert not convex(released + [b])
            assert convex(pocket + [a]) and convex(pocket + [b])
            for endpoint in (a, b):
                detached = frozenset(pocket + [endpoint])
                released_key = frozenset(released)
                detached_records.append((detached, mask, role, endpoint))
                pair_records.append(((released_key, detached), mask,
                                     role, endpoint))
        contexts.append(frozenset(released))

    assert len(set(contexts)) == 2**tail_size
    detached_outputs = {record[0] for record in detached_records}
    assert len(detached_outputs) == 2 * q
    detached_load = max(sum(record[0] == output
                            for record in detached_records)
                        for output in detached_outputs)
    assert detached_load == 2**tail_size
    pair_outputs = {record[0] for record in pair_records}
    assert len(pair_outputs) == len(pair_records)
    return (len(universe), len(contexts), len(detached_records),
            len(detached_outputs), detached_load, len(pair_outputs))


def weighted_two_bank_audit():
    # Records (left face, right face, weight) deliberately collide.  The
    # exact pair load, rather than either marginal load, controls the total.
    records = []
    weights = (Q(1), Q(2, 3), Q(3, 5), Q(5, 7))
    for context, weight in enumerate(weights):
        for edge in range(5):
            left = (context % 3, edge % 2)
            right = ((context + edge) % 4, edge % 3)
            records.append((left, right, weight))
    left_faces = {row[0] for row in records}
    right_faces = {row[1] for row in records}
    pairs = {(row[0], row[1]) for row in records}
    total = sum(row[2] for row in records)
    pair_load = max(sum(row[2] for row in records
                        if (row[0], row[1]) == pair)
                    for pair in pairs)
    assert total <= pair_load * len(left_faces) * len(right_faces)
    return total, len(left_faces), len(right_faces), pair_load


def main():
    geometry = gap_reset_regression()
    total, left, right, load = weighted_two_bank_audit()
    print("PASS: gap-reset universe=%d contexts=%d records=%d "
          "detached=%d load=%d pair_outputs=%d; "
          "weighted total=%s banks=%dx%d pair_load=%s"
          % (*geometry, total, left, right, load))


if __name__ == "__main__":
    main()
