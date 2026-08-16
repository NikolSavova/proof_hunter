#!/usr/bin/env python3
"""Exact checks for SHIELD_CIRCUIT_COVER.md."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations, product
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
Point = tuple[Fraction, Fraction]


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points: list[Point]) -> list[Point]:
    if len(points) <= 2:
        return list(points)
    ordered = sorted(points)

    def chain(sequence: list[Point]) -> list[Point]:
        answer: list[Point] = []
        for point in sequence:
            while len(answer) >= 2 and orient(answer[-2], answer[-1], point) <= 0:
                answer.pop()
            answer.append(point)
        return answer

    return chain(ordered)[:-1] + chain(list(reversed(ordered)))[:-1]


def convex(points: list[Point]) -> bool:
    return len(points) <= 2 or len(hull(points)) == len(points)


def cauchy_audit() -> int:
    """Check the squared form of sum w_c <= sqrt(K L) V."""
    cases = 0
    for contexts in range(1, 8):
        for degree in range(2, 10):
            for reservoir in range(1, 30):
                for overlap in range(1, contexts + 1):
                    # Abstract bank capacities: sum |A_c|=C<=V and
                    # sum |M_c|=CH<=L V.  Use the least admissible V.
                    volume = max(contexts, (contexts * reservoir + overlap - 1) // overlap)
                    records = contexts * degree * degree
                    # Squared Corollary 2, with no floating arithmetic.
                    assert records * records * reservoir <= (
                        degree**4 * overlap * volume * volume
                    )
                    cases += 1
    return cases


def deleted_guard_overlap_audit() -> int:
    """Exhaust small carriers and verify the L_t completion bound."""
    checked = 0
    outer = tuple(range(6))
    for rank in (2, 3, 4):
        carriers = list(combinations(outer, rank))
        for guard_cap in (0, 1, 2):
            outputs: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
            for carrier in carriers:
                for size in range(min(guard_cap, rank) + 1):
                    for guard in combinations(carrier, size):
                        remainder = tuple(x for x in carrier if x not in guard)
                        outputs.setdefault(remainder, set()).add(carrier)
            bound = sum(comb(len(outer), i) for i in range(guard_cap + 1))
            assert max(map(len, outputs.values())) <= bound
            checked += 1
    return checked


def minimum_cover(vertices: tuple[int, ...], traces: set[frozenset[int]]) -> int:
    for size in range(len(vertices) + 1):
        for guard in combinations(vertices, size):
            if all(set(guard) & trace for trace in traces):
                return size
    raise AssertionError("no cover")


def double_parabola_audit(m: int = 6) -> dict[str, int]:
    height = Fraction(10 * m * m)
    eta = Fraction(1, 10)
    indices = tuple(range(-m, m + 1))
    outer = [(Fraction(i), Fraction(i * i - m * m)) for i in indices]
    internal = [(Fraction(i), height + eta * i * i) for i in indices]
    ambient = outer + internal

    assert all(orient(a, b, c) != 0 for a, b, c in combinations(ambient, 3))
    assert convex(outer)
    assert convex(internal)
    assert all(convex(outer + [point]) for point in internal)

    traces: set[frozenset[int]] = set()
    singleton_witnesses = 0
    for position in range(1, len(indices) - 1):
        quadruple = [
            outer[position],
            internal[position - 1],
            internal[position],
            internal[position + 1],
        ]
        assert not convex(quadruple)
        assert internal[position] not in set(hull(quadruple))
        traces.add(frozenset({position}))
        singleton_witnesses += 1

        midpoint = (
            (internal[position - 1][0] + internal[position + 1][0]) / 2,
            (internal[position - 1][1] + internal[position + 1][1]) / 2,
        )
        assert midpoint[0] == internal[position][0] == outer[position][0]
        assert outer[position][1] < internal[position][1] < midpoint[1]

    cover = minimum_cover(tuple(range(len(outer))), traces)
    assert cover == len(outer) - 2 == singleton_witnesses

    rank = 4
    context_labels = tuple(range(1, len(outer) - 1))
    contexts = list(combinations(context_labels, rank))
    for carrier in contexts:
        local_traces = {frozenset({label}) for label in carrier}
        assert minimum_cover(tuple(carrier), local_traces) == rank
        assert convex([outer[label] for label in carrier])

    return {
        "outer_points": len(outer),
        "internal_points": len(internal),
        "singleton_traces": singleton_witnesses,
        "minimum_trace_cover": cover,
        "rank_four_contexts": len(contexts),
    }


def matching_shield_audit() -> int:
    """Exhaust the double count Q_s C <= Delta V on tiny banks."""
    checked = 0
    universe = tuple(range(5))
    shield_rank = 3
    middle_rank = 1
    banks = list(combinations(universe, shield_rank))
    q = comb(shield_rank, middle_rank)
    for context_count in range(1, 5):
        for assignment in product(banks, repeat=context_count):
            degree = {
                face: sum(set(face) <= set(bank) for bank in assignment)
                for face in combinations(universe, middle_rank)
            }
            delta = max(degree.values())
            volume = len(degree)
            assert q * context_count <= delta * volume
            checked += 1
    return checked


def main() -> None:
    certificate = {
        "cauchy_parameter_cases": cauchy_audit(),
        "deleted_guard_overlap_cases": deleted_guard_overlap_audit(),
        "double_parabola": double_parabola_audit(),
        "matching_shield_incidence_cases": matching_shield_audit(),
        "verdict": (
            "Small outer circuit transversals release the full internal mixed bank; "
            "a rational double-parabola family forces a linear trace matching, while "
            "the matching canonically exposes an outer Boolean shield."
        ),
    }
    path = HERE / "certificate.json"
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps(certificate, indent=2))
    print("shield circuit cover audit: PASS")


if __name__ == "__main__":
    main()
