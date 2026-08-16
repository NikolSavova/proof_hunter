#!/usr/bin/env python3
"""Exact checks for pairwise-convex triple circuit cover and regression."""

from fractions import Fraction as Q
from itertools import combinations
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
    raise AssertionError("finite hypergraph has no transversal")


def matching_number(edges):
    best = 0
    for mask in range(1 << len(edges)):
        used = set()
        count = 0
        valid = True
        for i, edge in enumerate(edges):
            if mask >> i & 1:
                if used.intersection(edge):
                    valid = False
                    break
                used.update(edge)
                count += 1
        if valid:
            best = max(best, count)
    return best


def base_configuration():
    base = [(Q(-5), Q(1)), (Q(-1), Q(11)),
            (Q(2), Q(9)), (Q(11), Q(1))]
    x = (Q(2), Q(-10))
    z = (Q(9), Q(-4))
    endpoint = (Q(5), Q(-6))
    return base, [x, z], endpoint


def tangent_and_transversal_audit():
    base, pocket, endpoint = base_configuration()
    universe = base + pocket + [endpoint]
    assert all(orient(*triple) for triple in combinations(universe, 3))
    assert convex(base + pocket)
    assert convex(base + [endpoint])
    assert convex(pocket + [endpoint])
    assert not convex(universe)

    circuits = bad_circuits(universe)
    traces = []
    for circuit in circuits:
        assert endpoint in circuit
        assert circuit.intersection(base)
        assert circuit.intersection(pocket)
        split = (len(circuit.intersection(base)),
                 len(circuit.intersection(pocket)))
        assert split in ((2, 1), (1, 2))
        traces.append(frozenset(circuit.difference({endpoint})))

    vertices = base + pocket
    covers = minimum_transversals(vertices, traces)
    tau = len(covers[0])
    nu = matching_number(traces)
    assert nu <= tau <= 3 * nu

    # Release iff every surviving bad circuit is hit.
    for mask in range(1 << len(vertices)):
        deleted = {vertices[i] for i in range(len(vertices)) if mask >> i & 1}
        hits = all(deleted.intersection(trace) for trace in traces)
        released = convex([point for point in universe if point not in deleted])
        assert hits == released

    x = pocket[0]
    assert covers == [frozenset({x})]
    q_hull = hull(base + [endpoint])
    place = q_hull.index(endpoint)
    tangents = {q_hull[place - 1], q_hull[(place + 1) % len(q_hull)]}
    witness = frozenset((base[1], pocket[0], pocket[1], endpoint))
    assert witness in circuits
    assert not witness.intersection(tangents)
    return len(circuits), tau, nu


def rectangle(m=7):
    base, _, endpoint = base_configuration()
    root = base[1]
    guards = []
    pockets = []
    for i in range(1, m + 1):
        parameter = Q(i, 10000 * m)
        guards.append((parameter,
                       Q(-12) + 3 * parameter + 7 * parameter * parameter))
    for j in range(1, m + 1):
        parameter = Q(j, 10000 * m)
        x = (Q(2) + parameter,
             Q(-10) + 2 * parameter + 3 * parameter * parameter)
        z = (Q(9) - 2 * parameter,
             Q(-4) + parameter + 5 * parameter * parameter)
        pockets.append((x, z))

    universe = base + [endpoint] + guards + [p for pair in pockets for p in pair]
    assert all(orient(*triple) for triple in combinations(universe, 3))
    q_face = frozenset(base + [endpoint])
    assert convex(q_face)

    sources = []
    released = []
    detached = []
    canonical_releases = []
    for guard in guards:
        source = frozenset(base + [guard])
        assert convex(source)
        sources.append(source)
    for x, z in pockets:
        c_face = frozenset(base + [x, z])
        w_face = frozenset((x, z, endpoint))
        whole = base + [x, z, endpoint]
        assert convex(c_face) and convex(w_face) and not convex(whole)
        witness = [root, x, z, endpoint]
        assert not convex(witness) and endpoint not in hull(witness)

        circuits = bad_circuits(whole)
        traces = [frozenset(circuit.difference({endpoint}))
                  for circuit in circuits]
        covers = minimum_transversals(base + [x, z], traces)
        assert covers == [frozenset({x})]
        release = frozenset(base + [z, endpoint])
        assert convex(release)
        released.append(c_face)
        detached.append(w_face)
        canonical_releases.append(release)

    mixed_release_outputs = set()
    mark_pairs = set()
    records = []
    for i, guard in enumerate(guards):
        for j, (x, z) in enumerate(pockets):
            assert not convex(base + [guard, z, endpoint])
            assert not convex(base + [guard, x, z])
            mark_pair = frozenset((guard, x))
            assert convex(mark_pair)
            mark_pairs.add(mark_pair)
            records.append((i, j))
            # Deliberately empty: the proposed full mixed release is bad.
            if convex(base + [guard, z, endpoint]):
                mixed_release_outputs.add(frozenset(base + [guard, z, endpoint]))

    assert not mixed_release_outputs
    assert len(mark_pairs) == m * m
    assert len(set(sources)) == len(set(released)) == len(set(detached)) == m
    assert len(set(canonical_releases)) == m

    # Any subfamily using a rows and c columns has at most ac edges and at
    # least a+2c+1 actual four-target faces.  Exhaust the possible counts.
    hall4 = Q(0)
    for rows in range(1, m + 1):
        for columns in range(1, m + 1):
            hall4 = max(hall4, Q(rows * columns, rows + 2 * columns + 1))
    assert hall4 == Q(m * m, 3 * m + 1)
    return len(records), hall4, m, m, 1


def main():
    circuits, tau, nu = tangent_and_transversal_audit()
    records, hall4, circuit_load, release_load, mark_load = rectangle()
    print("PASS: tangent counterexample circuits=%d tau=%d nu=%d; "
          "rectangle m=7 records=%d hall4=%s circuit_load=%d "
          "release_load=%d mark_pair_load=%d"
          % (circuits, tau, nu, records, hall4, circuit_load,
             release_load, mark_load))


if __name__ == "__main__":
    main()
