#!/usr/bin/env python3
"""Exact checks for quadratic trace rectangle-or-shield."""

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import sys


COMMON = Path(__file__).resolve().parents[1] / "agent_common_shield_mixing"
sys.path.insert(0, str(COMMON))
from verify_mixed_seam_vertex_cover_pi2 import convex, hull, orient  # noqa: E402


def bad_circuits(points):
    return [frozenset(part) for part in combinations(points, 4)
            if not convex(part)]


def minimum_transversals(vertices, edges):
    for size in range(len(vertices) + 1):
        covers = [frozenset(part) for part in combinations(vertices, size)
                  if all(set(part).intersection(edge) for edge in edges)]
        if covers:
            return covers
    raise AssertionError("no transversal")


def matching_number(edges):
    best = 0
    for mask in range(1 << len(edges)):
        used = set()
        count = 0
        for index, edge in enumerate(edges):
            if mask >> index & 1:
                if used.intersection(edge):
                    break
                used.update(edge)
                count += 1
        else:
            best = max(best, count)
    return best


def bad_trace_audit():
    row = [(Q(0), Q(0)), (Q(4), Q(0))]
    column = [(Q(0), Q(4)), (Q(1), Q(1))]
    universe = row + column
    assert convex(row) and convex(column) and not convex(universe)
    circuits = bad_circuits(universe)
    assert len(circuits) == 1
    for circuit in circuits:
        split = (len(circuit.intersection(row)),
                 len(circuit.intersection(column)))
        assert split in ((1, 3), (2, 2), (3, 1))

    covers = minimum_transversals(universe, circuits)
    tau = len(covers[0])
    nu = matching_number(circuits)
    assert nu <= tau <= 4 * nu
    for mask in range(1 << len(universe)):
        deleted = {universe[i] for i in range(len(universe)) if mask >> i & 1}
        hits = all(deleted.intersection(circuit) for circuit in circuits)
        released = convex([point for point in universe if point not in deleted])
        assert hits == released

    rank = len(universe)
    release_size = (1 << (rank - tau)) - 1
    # The one matched circuit has two labels on each side, so the selected
    # one-side Boolean shield has three nonempty faces.
    shield_size = (1 << 2) - 1
    local_bank = max(release_size, shield_size)
    assert local_bank >= 2 ** (rank / 3) - 1
    return len(circuits), tau, nu, local_bank


def explicit_lift():
    base = [(Q(-5), Q(1)), (Q(-1), Q(11)),
            (Q(2), Q(9)), (Q(11), Q(1))]
    endpoint = (Q(5), Q(-6))
    x = (Q(2), Q(-10))
    z = (Q(9), Q(-4))
    root = base[1]
    centers = [
        (Q(-961, 1000), Q(-12977, 1000)),
        (Q(1613, 1000), Q(-11482, 1000)),
        (Q(2574, 1000), Q(-10802, 1000)),
        (Q(8545, 1000), Q(-4552, 1000)),
    ]
    epsilon = Q(1, 100000)
    roles = []
    for role, (cx, cy) in enumerate(centers, 1):
        roles.append([
            (cx + epsilon * (choice + 1) * (2 * role + 1),
             cy + epsilon * (choice + 1) *
             (3 * role * role + 2 * choice + 1))
            for choice in range(2)
        ])

    ambient = (base + [endpoint, x, z]
               + [point for support in roles for point in support])
    assert all(orient(*triple) for triple in combinations(ambient, 3))
    assert convex(base + [endpoint])
    assert not convex([root, x, z, endpoint])
    assert endpoint not in hull([root, x, z, endpoint])

    rows = {}
    columns = {}
    records = []
    mark_outputs = []
    trace_outputs = []
    target_sets = []
    for choices in product(range(2), repeat=4):
        row_word = (roles[0][choices[0]], roles[1][choices[1]])
        column_word = (roles[2][choices[2]], roles[3][choices[3]])
        row_key = choices[:2]
        column_key = choices[2:]
        row_trace = list(row_word)
        column_trace = [x, *column_word, z]
        source = frozenset(base + row_trace)
        released = frozenset(base + column_trace)
        detached = frozenset(column_trace + [endpoint])
        trace = frozenset(row_trace + column_trace)

        assert convex(row_trace) and convex(column_trace)
        assert convex(source) and convex(released) and convex(detached)
        assert convex(trace)
        assert not convex(base + column_trace + [endpoint])

        rows[row_key] = source
        columns[column_key] = (released, detached)
        records.append((row_key, column_key))
        mark_outputs.append(frozenset((row_word[0], column_word[0])))
        trace_outputs.append(trace)
        target_sets.extend((source, released, detached,
                            frozenset(base + [endpoint])))

    assert len(rows) == len(columns) == 4 and len(records) == 16
    mark_load = max(Counter(mark_outputs).values())
    trace_load = max(Counter(trace_outputs).values())
    assert len(set(trace_outputs)) == len(records)
    assert mark_load == 4 and trace_load == 1

    # A subrectangle with a rows and c columns has ac records and
    # a+2c+1 distinct four-target faces; maximize exactly.
    hall4 = max(Q(a * c, a + 2 * c + 1)
                for a in range(1, 5) for c in range(1, 5))
    assert hall4 == Q(16, 13)
    return len(rows), len(columns), len(records), hall4, mark_load, trace_load


def main():
    circuits, tau, nu, local_bank = bad_trace_audit()
    rows, columns, records, hall4, mark_load, trace_load = explicit_lift()
    print("PASS: bad-trace circuits=%d tau=%d nu=%d local_bank=%d; "
          "lift rows=%d cols=%d records=%d hall4=%s mark_load=%d "
          "trace_load=%d"
          % (circuits, tau, nu, local_bank, rows, columns, records,
             hall4, mark_load, trace_load))


if __name__ == "__main__":
    main()
