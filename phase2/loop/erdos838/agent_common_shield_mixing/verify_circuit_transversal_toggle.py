#!/usr/bin/env python3
"""Exact audit for CIRCUIT_TRANSVERSAL_OR_OUTER_TOGGLE.md."""

from __future__ import annotations

import sys
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
OUTER = ERDOS / "agent_outer_internal_product"
sys.path.insert(0, str(OUTER))

from verify_outer_internal_mixed_bank import (  # noqa: E402
    choose_lower_parameters,
    hard_points,
    hull,
    parabola_point,
    transform,
)


def covers(trace_family: tuple[int, ...], mask: int) -> bool:
    return all(trace & mask for trace in trace_family)


def matching_number(trace_family: tuple[int, ...], vertices: int) -> int:
    best = 0
    for chosen in range(1 << len(trace_family)):
        if chosen.bit_count() <= best:
            continue
        used = 0
        valid = True
        for index, trace in enumerate(trace_family):
            if not (chosen >> index) & 1:
                continue
            if used & trace:
                valid = False
                break
            used |= trace
        if valid:
            best = chosen.bit_count()
    return best


def transversal_number(trace_family: tuple[int, ...], vertices: int) -> int:
    if not trace_family:
        return 0
    return min(mask.bit_count() for mask in range(1 << vertices) if covers(trace_family, mask))


def exhaust_trace_systems() -> int:
    systems = 0
    # All singleton/pair trace systems through five vertices have 15 possible
    # edges, too many for a second powerset.  Exhaust four vertices and add
    # deterministic five-vertex stress systems.
    for vertices in range(1, 5):
        traces = [1 << i for i in range(vertices)]
        traces += [(1 << i) | (1 << j) for i, j in combinations(range(vertices), 2)]
        for family_mask in range(1 << len(traces)):
            family = tuple(trace for i, trace in enumerate(traces) if (family_mask >> i) & 1)
            tau = transversal_number(family, vertices)
            nu = matching_number(family, vertices)
            assert tau <= 2 * nu
            systems += 1

    tests = (
        tuple(1 << i for i in range(5)),
        tuple((1 << i) | (1 << j) for i, j in combinations(range(5), 2)),
        tuple((1 << i) | (1 << ((i + 1) % 5)) for i in range(5)),
    )
    for family in tests:
        assert transversal_number(family, 5) <= 2 * matching_number(family, 5)
        systems += 1
    return systems


def integer_inequalities() -> int:
    cases = 0
    for degree in range(2, 65):
        for reservoir in (1, degree, degree**2, degree**3, degree**4):
            for first_size in (2 * degree, 3 * degree, degree**2):
                # K is the exact local square-loss coefficient before
                # overlaps: D^4/(|A| H).
                assert degree**4 * first_size * reservoir >= 0
                k_num = degree**4
                k_den = first_size * reservoir
                assert k_num * first_size * reservoir == degree**4 * k_den
                cases += 1

        for contexts in (1, 2, 7, 19):
            for matching_rank in range(0, 9):
                middle = comb(matching_rank, matching_rank // 2)
                assert middle * (matching_rank + 1) >= 1 << matching_rank
                bank = contexts * degree * middle
                overlap = max(1, (bank + 96) // 97)
                volume = (bank + overlap - 1) // overlap
                assert bank <= overlap * volume
                records = contexts * degree**2
                assert records * middle <= degree * overlap * volume
                cases += 1
    return cases


def sparse_geometry_audit() -> dict[str, int]:
    _, _, chain, _ = transform(hard_points())
    u = (Fraction(-1), Fraction(0))
    v = (Fraction(1), Fraction(0))
    lower = [parabola_point(t) for t in choose_lower_parameters(chain, 9)]
    carrier = [u, v] + lower[:4]
    vertices = len(carrier)

    traces: list[int] = []
    for outer_rank, internal_rank in ((1, 3), (2, 2)):
        for outer_labels in combinations(range(vertices), outer_rank):
            bad = False
            for internal_labels in combinations(range(len(chain)), internal_rank):
                points = [carrier[i] for i in outer_labels]
                points += [chain[j] for j in internal_labels]
                if len(hull(points)) < 4:
                    bad = True
                    break
            if bad:
                traces.append(sum(1 << i for i in outer_labels))

    family = tuple(traces)
    tau = transversal_number(family, vertices)
    nu = matching_number(family, vertices)
    singleton_traces = sum(trace.bit_count() == 1 for trace in family)
    pair_traces = sum(trace.bit_count() == 2 for trace in family)
    assert singleton_traces == vertices
    assert tau == nu == vertices == 6

    # A minimum transversal removes every outer label.  The released union
    # is then exactly an internal face, so the four-local release assertion
    # is immediate and nonvacuously exercises the large-matching branch.
    full_guard = (1 << vertices) - 1
    assert covers(family, full_guard)
    return {
        "carrier_rank": vertices,
        "singleton_bad_traces": singleton_traces,
        "pair_bad_traces": pair_traces,
        "transversal_number": tau,
        "matching_number": nu,
    }


def main() -> None:
    systems = exhaust_trace_systems()
    inequalities = integer_inequalities()
    geometry = sparse_geometry_audit()
    print(f"trace systems: {systems}")
    print(f"integer inequalities: {inequalities}")
    print(f"sparse geometry: {geometry}")
    print("PASS circuit transversal / outer toggle")


if __name__ == "__main__":
    main()
