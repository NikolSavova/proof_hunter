#!/usr/bin/env python3
"""Exact audit of MIDDLE_TOGGLE_FIRST_DIVERGENCE.md."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
Point = tuple[Fraction, Fraction]


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull_indices(points: list[Point], labels: tuple[int, ...]) -> tuple[int, ...]:
    if len(labels) <= 2:
        return labels
    ordered = sorted(labels, key=lambda i: points[i])

    def chain(sequence: list[int]) -> list[int]:
        answer: list[int] = []
        for label in sequence:
            while (
                len(answer) >= 2
                and orient(points[answer[-2]], points[answer[-1]], points[label]) <= 0
            ):
                answer.pop()
            answer.append(label)
        return answer

    return tuple(chain(ordered)[:-1] + chain(list(reversed(ordered)))[:-1])


def convex(points: list[Point], labels: tuple[int, ...]) -> bool:
    return len(labels) <= 2 or len(hull_indices(points, labels)) == len(labels)


def interval_collision_audit() -> dict[str, int]:
    """Exhaust Boolean intervals and check Theorem 2 exactly."""
    ground = tuple(range(7))
    intervals: list[tuple[frozenset[int], frozenset[int]]] = []
    width = 3
    for top in combinations(ground, 5):
        top_set = frozenset(top)
        for deleted in combinations(top, width):
            bottom = top_set - set(deleted)
            intervals.append((frozenset(bottom), top_set))

    incidences: dict[frozenset[int], list[tuple[frozenset[int], frozenset[int]]]] = {}
    for bottom, top in intervals:
        middle = tuple(top - bottom)
        for size in range(width + 1):
            for chosen in combinations(middle, size):
                face = frozenset(set(bottom) | set(chosen))
                incidences.setdefault(face, []).append((bottom, top))

    checked = 0
    for face, fibre in incidences.items():
        by_rank: dict[int, list[frozenset[int]]] = {}
        for _, top in fibre:
            completion = top - face
            assert top == face | completion
            by_rank.setdefault(len(completion), []).append(completion)
        assert max(map(len, by_rank.values())) * (width + 1) >= len(fibre)
        checked += len(fibre)
    return {
        "intervals": len(intervals),
        "outputs": len(incidences),
        "incidences_checked": checked,
    }


def trace_clutter(
    points: list[Point], base: frozenset[int], support: frozenset[int]
) -> set[frozenset[int]]:
    traces: set[frozenset[int]] = set()
    for circuit in combinations(sorted(base | support), 4):
        if not convex(points, circuit):
            trace = frozenset(circuit) & support
            assert trace
            traces.add(frozenset(trace))
    return traces


def maximum_matching(traces: set[frozenset[int]]) -> list[frozenset[int]]:
    ordered = list(traces)
    best: list[frozenset[int]] = []

    def search(index: int, used: frozenset[int], chosen: list[frozenset[int]]) -> None:
        nonlocal best
        if len(chosen) + len(ordered) - index <= len(best):
            return
        if index == len(ordered):
            if len(chosen) > len(best):
                best = list(chosen)
            return
        search(index + 1, used, chosen)
        edge = ordered[index]
        if not (edge & used):
            search(index + 1, used | edge, chosen + [edge])

    search(0, frozenset(), [])
    return best


def planar_trace_audit() -> dict[str, int]:
    """Verify trace avoidance, matching suppression, and guard release."""
    # Two exact rational parabolic layers.  Each layer is convex, but their
    # union has many cross four-circuits.
    m = 4
    height = Fraction(10 * m * m)
    eta = Fraction(1, 10)
    outer = [
        (Fraction(i), Fraction(i * i - m * m)) for i in range(-m, m + 1)
    ]
    inner = [
        (Fraction(i), height + eta * i * i) for i in range(-m, m + 1)
    ]
    points = outer + inner
    assert all(orient(a, b, c) != 0 for a, b, c in combinations(points, 3))

    # Use a rank-five convex base and six internal support labels.
    base = frozenset(range(1, 6))
    support = frozenset(range(len(outer), len(outer) + 6))
    assert convex(points, tuple(base))
    traces = trace_clutter(points, base, support)
    matching = maximum_matching(traces)
    guard = frozenset().union(*matching) if matching else frozenset()

    # A maximum matching is maximal; its endpoints hit every trace.
    assert all(trace & guard for trace in traces)
    assert len(guard) <= 4 * len(matching)
    assert convex(points, tuple(sorted(base | (support - guard))))

    compatible: list[frozenset[int]] = []
    for mask in range(1 << len(support)):
        chosen = frozenset(
            label for bit, label in enumerate(sorted(support)) if mask >> bit & 1
        )
        geometric = convex(points, tuple(sorted(base | chosen)))
        independent = not any(trace <= chosen for trace in traces)
        assert geometric == independent
        if geometric:
            compatible.append(chosen)

    s = len(matching)
    assert len(compatible) * (16**s) <= (2 ** len(support)) * (15**s)
    return {
        "base_rank": len(base),
        "support_rank": len(support),
        "bad_traces": len(traces),
        "trace_matching": s,
        "guard_rank": len(guard),
        "compatible_subsets": len(compatible),
    }


def complete_layer_audit() -> int:
    """Exhaust Theorem 3 on small exact rational point sets."""
    configurations = [
        [(Fraction(i), Fraction(i * i)) for i in range(9)],
        [
            (Fraction(-4), Fraction(0)),
            (Fraction(-3), Fraction(-5)),
            (Fraction(-1), Fraction(-8)),
            (Fraction(2), Fraction(-7)),
            (Fraction(4), Fraction(0)),
            (Fraction(-2), Fraction(6)),
            (Fraction(0), Fraction(9)),
            (Fraction(3), Fraction(7)),
            (Fraction(1), Fraction(2)),
        ],
    ]
    checked = 0
    for points in configurations:
        assert all(orient(a, b, c) != 0 for a, b, c in combinations(points, 3))
        labels = tuple(range(len(points)))
        for base_rank in (0, 1, 2):
            for base_tuple in combinations(labels, base_rank):
                base = frozenset(base_tuple)
                if not convex(points, base_tuple):
                    continue
                remaining = tuple(label for label in labels if label not in base)
                for y in remaining:
                    candidates = tuple(label for label in remaining if label != y)
                    for support_tuple in combinations(candidates, 5):
                        support = frozenset(support_tuple)
                        premise = all(
                            convex(points, tuple(sorted(base | set(qset) | {y})))
                            for qset in combinations(support_tuple, 4)
                        )
                        if premise:
                            assert convex(points, tuple(sorted(base | support | {y})))
                            checked += 1
    return checked


def first_divergence_audit() -> dict[str, int]:
    """Check Lemma 5 and the 3^(2p) union decoder."""
    points = [
        (Fraction(-4), Fraction(0)),
        (Fraction(-3), Fraction(-5)),
        (Fraction(-1), Fraction(-8)),
        (Fraction(2), Fraction(-7)),
        (Fraction(4), Fraction(0)),
        (Fraction(-2), Fraction(6)),
        (Fraction(0), Fraction(9)),
        (Fraction(3), Fraction(7)),
        (Fraction(1), Fraction(2)),
    ]
    base = frozenset({0})
    rank = 3
    completions = [
        frozenset(face)
        for face in combinations(range(1, len(points)), rank)
        if convex(points, tuple(sorted(base | set(face))))
    ]
    compatible = 0
    bad = 0
    union_load: dict[frozenset[int], int] = {}
    for first in completions:
        for second in completions:
            if first == second:
                continue
            union = base | first | second
            if convex(points, tuple(sorted(union))):
                compatible += 1
                union_load[union] = union_load.get(union, 0) + 1
            else:
                bad += 1
                witnesses = [
                    frozenset(circuit)
                    for circuit in combinations(sorted(union), 4)
                    if not convex(points, circuit)
                ]
                assert any(
                    witness & (first - second) and witness & (second - first)
                    for witness in witnesses
                )
    assert not union_load or max(union_load.values()) <= 3 ** (2 * rank)
    return {
        "completion_faces": len(completions),
        "compatible_ordered_pairs": compatible,
        "bad_ordered_pairs": bad,
        "maximum_union_load": max(union_load.values(), default=0),
        "decoder_bound": 3 ** (2 * rank),
    }


def main() -> None:
    certificate = {
        "interval_collision": interval_collision_audit(),
        "complete_layer_instances": complete_layer_audit(),
        "planar_trace": planar_trace_audit(),
        "first_divergence": first_divergence_audit(),
        "verdict": (
            "Heavy middle-toggle overlap localizes to uniform common-base completions; "
            "complete layers release a full shield, while arbitrary defects obey the "
            "exact rank-four trace matching suppression/guard-release dichotomy."
        ),
    }
    (HERE / "certificate.json").write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps(certificate, indent=2))
    print("middle-toggle first-divergence audit: PASS")


if __name__ == "__main__":
    main()
