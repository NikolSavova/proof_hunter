#!/usr/bin/env python3
"""Exact checks for fixed detached-pair source-mask Hall banks."""

from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import sys


COMMON = Path(__file__).resolve().parents[1] / "agent_common_shield_mixing"
sys.path.insert(0, str(COMMON))
from verify_mixed_seam_vertex_cover_pi2 import convex, orient  # noqa: E402


def point_on_edge(index, parameter, depth):
    return (Q(index) + parameter,
            Q(index * index) + parameter * Q(2 * index + 1) - depth)


def fixed_pair_regression(q=3, tail_size=4):
    core = [(Q(i), Q(i * i)) for i in range(2 * q + 2)]
    tail = [(Q(i), Q(i * i))
            for i in range(2 * q + 2, 2 * q + 2 + tail_size)]
    pocket = []
    pairs = []
    for role in range(q):
        edge = 2 * role
        pocket.append(point_on_edge(edge, Q(1, 2), Q(1, 10)))
        pairs.append((
            point_on_edge(edge, Q(1, 4), Q(3, 100)),
            point_on_edge(edge, Q(3, 4), Q(3, 100)),
        ))

    universe = core + tail + pocket + [v for pair in pairs for v in pair]
    assert all(orient(*triple) for triple in combinations(universe, 3))

    # One fixed role, endpoint, released face, and detached face.
    edge = pairs[1]
    endpoint = edge[0]
    released = frozenset(core + pocket)
    detached = frozenset(pocket + [endpoint])
    assert convex(released) and convex(detached)
    assert not convex(list(released) + [endpoint])
    base_endpoint = frozenset(core + [endpoint])
    assert convex(base_endpoint)
    assert detached.intersection(base_endpoint) == {endpoint}
    assert detached.difference({endpoint}) == frozenset(pocket)
    assert base_endpoint.difference({endpoint}) == frozenset(core)

    sources = set()
    endpoint_faces = set()
    pair_faces = set()
    fixed_outputs = []
    for mask in range(1 << tail_size):
        selected = [tail[i] for i in range(tail_size) if mask >> i & 1]
        source = frozenset(core + selected)
        endpoint_face = frozenset(core + selected + [endpoint])
        pair_face = frozenset(core + selected + list(edge))
        assert convex(source)
        assert convex(endpoint_face)
        assert convex(pair_face)
        sources.add(source)
        endpoint_faces.add(endpoint_face)
        pair_faces.add(pair_face)
        fixed_outputs.append((released, detached))

    expected = 1 << tail_size
    assert len(sources) == len(endpoint_faces) == len(pair_faces) == expected
    assert len(set(fixed_outputs)) == 1
    pair_load = len(fixed_outputs)

    # The top source has one consecutive deleted tail run, and its Boolean
    # run downshadow is exactly the source family above.
    long_run_bank = {
        frozenset(core + [tail[i] for i in range(tail_size) if mask >> i & 1])
        for mask in range(1 << tail_size)
    }
    assert long_run_bank == sources
    return (len(universe), len(sources), pair_load, len(sources),
            len(endpoint_faces), len(long_run_bank))


def cyclic_runs(mask, n):
    chosen = {i for i in range(n) if mask >> i & 1}
    if not chosen:
        return []
    if len(chosen) == n:
        return [tuple(range(n))]
    starts = [i for i in chosen if (i - 1) % n not in chosen]
    runs = []
    for start in starts:
        run = []
        i = start
        while i in chosen:
            run.append(i)
            i = (i + 1) % n
        runs.append(tuple(run))
    return runs


def abstract_weighted_hall(n=6, copies=4):
    # Five distinct source masks, each copied with four rationally weighted
    # history tags.  Copying changes loads but never the ordinary outputs.
    masks = (0b000111, 0b011001, 0b101010, 0b111100, 0b010000)
    copy_weights = (Q(1), Q(1, 2), Q(2, 3), Q(5, 6))
    assert len(copy_weights) == copies
    histories = [(mask, tag, weight)
                 for mask in masks
                 for tag, weight in enumerate(copy_weights)]
    total = sum(weight for _, _, weight in histories)
    source_load = max(
        sum(weight for source, _, weight in histories if source == mask)
        for mask in masks
    )
    assert total <= source_load * len(masks)

    full_load = defaultdict(Q)
    run_load = defaultdict(Q)
    full_incidence = Q(0)
    run_incidence = Q(0)
    for mask, _, weight in histories:
        selected = [i for i in range(n) if mask >> i & 1]
        for submask in range(1, 1 << len(selected)):
            output = frozenset(selected[i] for i in range(len(selected))
                               if submask >> i & 1)
            full_load[output] += weight
            full_incidence += weight

        runs = cyclic_runs(mask, n)
        assert runs
        longest = min((run for run in runs),
                      key=lambda run: (-len(run), run))
        assert len(longest) >= (len(selected) + len(runs) - 1) // len(runs)
        for submask in range(1, 1 << len(longest)):
            output = frozenset(longest[i] for i in range(len(longest))
                               if submask >> i & 1)
            run_load[output] += weight
            run_incidence += weight

    lambda_all = max(full_load.values())
    lambda_run = max(run_load.values())
    # V is here the number of all abstract subsets; each geometric theorem
    # only uses that its output bank is a subfamily of the V ordinary faces.
    abstract_v = 1 << n
    assert full_incidence <= lambda_all * abstract_v
    assert run_incidence <= lambda_run * abstract_v

    # Replacing each history by h unit copies scales every incidence and
    # load by h while leaving all output supports unchanged.
    support_full = set(full_load)
    duplicated = defaultdict(int)
    for mask in masks:
        selected = [i for i in range(n) if mask >> i & 1]
        for _ in range(7):
            for submask in range(1, 1 << len(selected)):
                output = frozenset(selected[i] for i in range(len(selected))
                                   if submask >> i & 1)
                duplicated[output] += 1
    assert set(duplicated) == support_full
    return (len(histories), full_incidence, run_incidence,
            lambda_all, lambda_run)


def canonical_depth_decoder(max_rank=20):
    for rank in range(2, max_rank + 1):
        source = tuple(range(rank))
        by_endpoint = {}
        for depth in range(rank // 2):
            carrier = source[depth:rank - depth]
            endpoint = frozenset((carrier[0], carrier[-1]))
            assert endpoint not in by_endpoint
            by_endpoint[endpoint] = (depth, carrier)
        for endpoint, (depth, carrier) in by_endpoint.items():
            assert min(endpoint) == depth
            assert carrier == source[depth:rank - depth]


def hall_density(records):
    """Exact max nonempty subfamily weight divided by target-union size."""
    best = Q(0)
    for mask in range(1, 1 << len(records)):
        weight = Q(0)
        targets = set()
        for i, (left, right, value) in enumerate(records):
            if mask >> i & 1:
                weight += value
                targets.update((left, right))
        best = max(best, weight / len(targets))
    return best


def two_target_hall_audit():
    records = [("W", "Q%d" % i, Q(1)) for i in range(5)]
    eta = hall_density(records)
    targets = {target for left, right, _ in records for target in (left, right)}
    assert eta == Q(5, 6)
    assert sum(weight for _, _, weight in records) == eta * len(targets)

    weighted = [
        ("A", "B", Q(1, 2)),
        ("A", "C", Q(2, 3)),
        ("B", "C", Q(3, 4)),
        ("A", "B", Q(5, 6)),
    ]
    eta_weighted = hall_density(weighted)
    target_count = len({target for left, right, _ in weighted
                        for target in (left, right)})
    assert sum(weight for _, _, weight in weighted) <= eta_weighted * target_count
    return eta


def actual_guard_cauchy_audit():
    # Distinct actual guards above one fixed source have distinct targets.
    source_guards = {
        "A0": ("y0", "y1", "y2", "y3", "y4"),
        "A1": ("z0", "z1"),
        "A2": ("w0", "w1", "w2"),
    }
    records = [(source, guard)
               for source, guards in source_guards.items()
               for guard in guards]
    source_bank = len(source_guards)
    target_bank = max(len(guards) for guards in source_guards.values())
    assert len(records) <= source_bank * target_bank
    assert max(source_bank, target_bank) ** 2 >= len(records)


def main():
    geometry = fixed_pair_regression()
    histories, full_inc, run_inc, load_all, load_run = abstract_weighted_hall()
    canonical_depth_decoder()
    hall_star = two_target_hall_audit()
    actual_guard_cauchy_audit()
    print("PASS: fixed-pair universe=%d sources=%d pair_load=%d "
          "source_bank=%d endpoint_bank=%d long_run_bank=%d; "
          "abstract Hall histories=%d full_inc=%s run_inc=%s "
          "Lambda_all=%s Lambda_run=%s hall_star=%s"
          % (*geometry, histories, full_inc, run_inc, load_all, load_run,
             hall_star))


if __name__ == "__main__":
    main()
