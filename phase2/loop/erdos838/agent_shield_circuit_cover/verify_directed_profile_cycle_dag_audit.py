#!/usr/bin/env python3
"""Exact checks for the directed-profile cycle/DAG audit.

The checker has three independent parts.

* It exhausts every orientation of every simple graph through five
  vertices and checks the source/sink alternative for acyclic digraphs.
* It checks that pairwise convex unions around a directed 3-cycle need not
  have convex total union.
* It checks the exact 2-by-2-per-role nested-shell product used in the
  one-chamber regression, including all 256 row/column records and the
  actual decoder loads.
"""

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def half(sequence):
        answer = []
        for point in sequence:
            while (len(answer) >= 2
                   and orient(answer[-2], answer[-1], point) <= 0):
                answer.pop()
            answer.append(point)
        return answer

    return half(points)[:-1] + half(points[::-1])[:-1]


def convex(points):
    return len(points) <= 2 or len(hull(points)) == len(points)


def acyclic_and_degrees(n, arcs):
    outgoing = [[] for _ in range(n)]
    incoming = [[] for _ in range(n)]
    for u, v in arcs:
        outgoing[u].append(v)
        incoming[v].append(u)
    indegree = [len(part) for part in incoming]
    stack = [v for v in range(n) if indegree[v] == 0]
    order = []
    while stack:
        v = stack.pop()
        order.append(v)
        for w in outgoing[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                stack.append(w)
    if len(order) != n:
        return False, None
    undirected_degree = [len(outgoing[v]) + len(incoming[v])
                         for v in range(n)]
    sources = [v for v in range(n) if not incoming[v]]
    sinks = [v for v in range(n) if not outgoing[v]]
    return True, (outgoing, incoming, undirected_degree, sources, sinks)


def graph_audit():
    tested = 0
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        # State 0 omits the edge; 1 directs low-to-high; 2 high-to-low.
        for states in product(range(3), repeat=len(pairs)):
            arcs = []
            for state, (u, v) in zip(states, pairs):
                if state == 1:
                    arcs.append((u, v))
                elif state == 2:
                    arcs.append((v, u))
            is_dag, data = acyclic_and_degrees(n, arcs)
            if not is_dag:
                continue
            outgoing, incoming, degrees, sources, sinks = data
            delta = min(degrees)
            assert sources and sinks
            assert any(len(outgoing[v]) >= delta for v in sources)
            assert any(len(incoming[v]) >= delta for v in sinks)
            tested += 1

    # Weighted peeling: deleted edge weight is charged exactly once, at
    # the first endpoint removed.  These exhaustive small integer examples
    # check the strict-average core statement used in the report.
    weighted = 0
    n = 4
    pairs = list(combinations(range(n), 2))
    for weights in product(range(3), repeat=len(pairs)):
        total = sum(weights)
        if not total:
            continue
        threshold = Q(total, n)
        active = set(range(n))
        while active:
            degrees = {
                v: sum(weight for weight, (x, y) in zip(weights, pairs)
                       if weight and v in (x, y) and x in active and y in active)
                for v in active
            }
            light = [v for v in active if degrees[v] < threshold]
            if not light:
                break
            active.remove(min(light))
        assert active
        assert all(
            sum(weight for weight, (x, y) in zip(weights, pairs)
                if weight and v in (x, y) and x in active and y in active)
            >= threshold for v in active)
        weighted += 1
    return tested, weighted


def directed_cycle_counterexample():
    base = [(Q(-5), Q(1)), (Q(-1), Q(11)),
            (Q(2), Q(9)), (Q(11), Q(1))]
    pocket = [(Q(2), Q(-10)), (Q(9), Q(-4))]
    endpoint = [(Q(5), Q(-6))]
    blocks = [base, pocket, endpoint]
    assert all(convex(blocks[i] + blocks[(i + 1) % 3])
               for i in range(3))
    assert not convex(base + pocket + endpoint)
    assert endpoint[0] not in hull(base + pocket + endpoint)
    # The abstract profile graph may orient the three compatible pairs as
    # 0 -> 1 -> 2 -> 0.  Its cycle is therefore insufficient for gluing.
    return len(base + pocket + endpoint)


OUTER_ROLES = [
    [(-99988, 17), (-100000, 17)],
    [(-2, -100016), (12, -99992)],
    [(100016, 5), (100019, -3)],
    [(-3, 100010), (1, 99995)],
]

INNER_ROLES = [
    [(-60020, -29988), (-59992, -29983)],
    [(-29983, -60020), (-30014, -60013)],
    [(-7, -30005), (-9, -29994)],
    [(-30010, 13), (-29980, -12)],
]


def bad_circuits(points):
    return [part for part in combinations(range(len(points)), 4)
            if not convex([points[index] for index in part])]


def canonical_release(points):
    for size in range(len(points) + 1):
        for deleted in combinations(range(len(points)), size):
            deleted_set = set(deleted)
            remaining = tuple(point for index, point in enumerate(points)
                              if index not in deleted_set)
            if convex(remaining):
                return deleted, remaining
    raise AssertionError("no release")


def nested_shell_product():
    outer_roles = [[(Q(x, 10000), Q(y, 10000)) for x, y in role]
                   for role in OUTER_ROLES]
    inner_roles = [[(Q(x, 10000), Q(y, 10000)) for x, y in role]
                   for role in INNER_ROLES]
    base = (Q(5), Q(7))
    endpoint = (Q(4), Q(7))
    ambient = ([point for role in outer_roles for point in role]
               + [point for role in inner_roles for point in role]
               + [base, endpoint])
    assert all(orient(*triple) for triple in combinations(ambient, 3))
    rank_vector = Counter()
    for mask in range(1 << len(ambient)):
        subset = [ambient[index] for index in range(len(ambient))
                  if mask >> index & 1]
        if convex(subset):
            rank_vector[len(subset)] += 1
    assert [rank_vector[rank] for rank in range(9)] == [
        1, 18, 153, 816, 1880, 2008, 966, 177, 4]
    assert sum(rank_vector.values()) == 6023

    outer_words = [tuple(word) for word in product(*outer_roles)]
    inner_words = [tuple(word) for word in product(*inner_roles)]
    records = []
    mark_outputs = []
    release_outputs = []
    release_downfaces = []
    shield_outputs = []
    targets = set()

    for outer in outer_words:
        assert convex(outer)
        assert convex(outer + (base,))
        assert convex(outer + (endpoint,))
        assert not convex(outer + (base, endpoint))
        assert endpoint not in hull(outer + (base, endpoint))
        for inner in inner_words:
            assert convex(inner)
            assert convex(inner + (base,))
            # Every selected inner point is strictly inside every selected
            # outer quadrilateral.  Thus all 256 trace unions are bad in
            # one common containment chamber.
            assert all(point not in hull(outer + (point,))
                       for point in inner)
            trace = inner + outer
            assert not convex(trace)

            circuits = bad_circuits(trace)
            assert circuits
            deleted, released = canonical_release(trace)
            assert len(deleted) == 3
            assert deleted == (0, 2, 4)

            # There are two disjoint bad four-circuits, hence the maximum
            # circuit matching has size two on this eight-label trace.  Its
            # union is the whole trace; the canonical tie chooses the
            # four-label inner side as shield.
            assert any(set(left).isdisjoint(right)
                       for left, right in combinations(circuits, 2))
            shield = frozenset(inner)

            records.append((inner, outer))
            mark_outputs.append(frozenset((inner[0], outer[0])))
            release_outputs.append(frozenset(released))
            shield_outputs.append(shield)
            for size in range(1, len(released) + 1):
                release_downfaces.extend(
                    frozenset(face) for face in combinations(released, size))

            source = frozenset(inner + (base,))
            column = frozenset(outer + (base,))
            detached = frozenset(outer + (endpoint,))
            common = frozenset((base, endpoint))
            assert all(convex(tuple(face))
                       for face in (source, column, detached, common))
            targets.update((source, column, detached, common))

    assert len(records) == 256
    assert len(targets) == 49
    mark_load = max(Counter(mark_outputs).values())
    release_load = max(Counter(release_outputs).values())
    downface_load = max(Counter(release_downfaces).values())
    shield_load = max(Counter(shield_outputs).values())
    assert (mark_load, release_load, downface_load, shield_load) == (
        64, 8, 128, 16)

    hall_load = max(Q(rows * columns, rows + 2 * columns + 1)
                    for rows in range(1, 17)
                    for columns in range(1, 17))
    assert hall_load == Q(256, 49)

    # The 16 literal full outer transversals are a load-one bank.  We do
    # deliberately *not* infer an endpoint-profile multiplier from the
    # three local faces of each two-point support: strong separation alone
    # does not justify that splice.
    full_outer_bank = len(outer_words)
    assert full_outer_bank == 16
    return (len(inner_words), len(outer_words), len(records),
            sum(rank_vector.values()), hall_load,
            mark_load, release_load, downface_load, shield_load,
            full_outer_bank)


def main():
    dags, weighted = graph_audit()
    cycle_points = directed_cycle_counterexample()
    data = nested_shell_product()
    print(
        "PASS: dags=%d weighted_cores=%d cycle_points=%d; "
        "nested rows=%d cols=%d records=%d V=%d hall=%s mark=%d release=%d "
        "downface=%d shield=%d full_outer=%d"
        % ((dags, weighted, cycle_points) + data)
    )


if __name__ == "__main__":
    main()
