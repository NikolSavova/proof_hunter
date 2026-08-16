#!/usr/bin/env python3
"""Exact audit for SEAM_JET_INTERVAL_COMPLEMENT_DICHOTOMY.md."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
import json
from pathlib import Path


Point = tuple[Q, Q]


def cross(a: Point, b: Point, c: Point) -> Q:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def strict_hull(points: list[Point] | tuple[Point, ...]) -> list[Point]:
    ordered = sorted(set(points))
    if len(ordered) <= 2:
        return ordered
    lower: list[Point] = []
    upper: list[Point] = []
    for point in ordered:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    for point in reversed(ordered):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def convex(points: list[Point] | tuple[Point, ...]) -> bool:
    return len(strict_hull(points)) == len(set(points))


def enumerate_faces(points: tuple[Point, ...]) -> tuple[tuple[int, ...], ...]:
    result = []
    for mask in range(1 << len(points)):
        face = tuple(i for i in range(len(points)) if mask >> i & 1)
        if convex(tuple(points[i] for i in face)):
            result.append(face)
    return tuple(result)


def first_bad_four(union: tuple[int, ...], points: tuple[Point, ...]) -> tuple[int, ...]:
    for candidate in combinations(union, 4):
        if not convex(tuple(points[i] for i in candidate)):
            return candidate
    raise AssertionError("nonconvex union has no bad four-subset")


def positive_two_plus_two_audit() -> dict[str, object]:
    # A slightly perturbed diamond.  Left and right singleton ears replace
    # adjacent lower edges and fail only at the lower seam vertex.
    w = (
        (Q(-2), Q(0)),
        (Q(-1, 10), Q(-2)),
        (Q(1, 10), Q(2)),
        (Q(2), Q(0)),
    )
    count = 4
    epsilon = Q(1, 10_000)
    left = tuple(
        (Q(-3) - i * epsilon, Q(-3) - i * i * epsilon**2 - i * epsilon**3)
        for i in range(1, count + 1)
    )
    right = tuple(
        (Q(3) + i * epsilon, Q(-3) - 2 * i * i * epsilon**2 - i * epsilon**3)
        for i in range(1, count + 1)
    )
    points = tuple(sorted((*left, *w, *right)))
    assert all(cross(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))
    index = {point: i for i, point in enumerate(points)}
    w_ids = tuple(index[point] for point in w)
    left_ids = tuple(index[point] for point in left)
    right_ids = tuple(index[point] for point in right)
    assert tuple(sorted(w_ids)) == w_ids
    assert convex(w)

    internal_trace = None
    outputs = set()
    endpoint_pairs = []
    for ell in left_ids:
        for r in right_ids:
            edge = (ell, r)
            full = tuple(sorted((*w_ids, *edge)))
            assert convex(tuple(points[i] for i in (*w_ids, ell)))
            assert convex(tuple(points[i] for i in (*w_ids, r)))
            assert not convex(tuple(points[i] for i in full))
            circuit = first_bad_four(full, points)
            trace = tuple(i for i in circuit if i in w_ids)
            external = tuple(i for i in circuit if i in edge)
            assert len(trace) == 2 and external == edge
            if internal_trace is None:
                internal_trace = trace
            assert trace == internal_trace
            endpoint_pairs.append(edge)

    assert internal_trace is not None
    assert len(endpoint_pairs) == count**2

    # Let W vary while the two-label trace stays fixed.  The output recovers
    # C=W-A and hence W, so all records remain distinct.
    base_complement = tuple(i for i in w_ids if i not in internal_trace)
    records = []
    for edge in endpoint_pairs:
        for mask in range(1 << len(base_complement)):
            complement = tuple(
                base_complement[i]
                for i in range(len(base_complement))
                if mask >> i & 1
            )
            variable_w = tuple(sorted((*internal_trace, *complement)))
            assert convex(tuple(points[i] for i in (*variable_w, edge[0])))
            assert convex(tuple(points[i] for i in (*variable_w, edge[1])))
            assert not convex(tuple(points[i] for i in (*variable_w, *edge)))
            circuit = first_bad_four(tuple(sorted((*variable_w, *edge))), points)
            trace = tuple(i for i in circuit if i in variable_w)
            assert trace == internal_trace
            output = tuple(sorted((*complement, *edge)))
            assert convex(tuple(points[i] for i in output))
            assert (output[0], output[-1]) == edge
            outputs.add(output)
            records.append((variable_w, edge))
    assert len(outputs) == len(records) == count**2 * (1 << len(base_complement))

    # Literal aggregate radial tilts eta_e=sum_j h_(j,e), computed from all
    # ordinary source faces of this same rational configuration.
    faces = enumerate_faces(points)
    cells: defaultdict[tuple[int, int], Q] = defaultdict(Q)
    for face in faces:
        if len(face) >= 2:
            cells[face[0], face[-1]] += Q(1, 1 << len(face))
    max_depth = max(map(len, faces)) // 2
    eta = {edge: Q() for edge in endpoint_pairs}
    for depth in range(max_depth):
        numerators: defaultdict[tuple[int, int], Q] = defaultdict(Q)
        for face in faces:
            if len(face) >= 2 * depth + 2:
                edge = (face[depth], face[-1 - depth])
                numerators[edge] += Q(1, 1 << len(face))
        for edge in endpoint_pairs:
            if cells[edge]:
                eta[edge] += numerators[edge] / cells[edge]
    assert all(value > 0 for value in eta.values())
    interval_variants = 1 << len(base_complement)
    total_tilt = interval_variants * sum(eta.values(), Q())
    maximum_tilt = max(eta.values())
    assert total_tilt <= maximum_tilt * len(outputs)

    return {
        "points": len(points),
        "ordinary_faces": len(faces),
        "interval_rank": len(w),
        "endpoint_pairs": len(endpoint_pairs),
        "varying_interval_records": len(records),
        "fixed_two_plus_two_trace": list(internal_trace),
        "complement_outputs": len(outputs),
        "literal_total_aggregate_tilt": str(total_tilt),
        "literal_maximum_endpoint_tilt": str(maximum_tilt),
        "weighted_hall_inequality_verified": True,
    }


def one_plus_three_instance(m: int, count: int = 3) -> dict[str, object]:
    epsilon = Q(1, 1_000_000)
    w = tuple((Q(i), Q(i * i)) for i in range(m))
    left = tuple(
        (Q(-1) - a * epsilon,
         Q(-m * m) - a * a * epsilon**2 - a * epsilon**3)
        for a in range(1, count + 1)
    )
    right = tuple(
        (Q(m) + b * epsilon,
         Q(-m * m) - 2 * b * b * epsilon**2 - b * epsilon**3)
        for b in range(1, count + 1)
    )
    points = tuple(sorted((*left, *w, *right)))
    assert all(cross(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))
    index = {point: i for i, point in enumerate(points)}
    w_ids = tuple(index[point] for point in w)
    left_ids = tuple(index[point] for point in left)
    right_ids = tuple(index[point] for point in right)
    assert convex(w)

    expected_trace = w_ids[:3]
    complement = w_ids[3:]
    assert len(complement) >= 3
    pairs = 0
    for ell in left_ids:
        # Every retained triple already obstructs the individual left ear.
        for triple in combinations(w_ids, 3):
            assert not convex(tuple(points[i] for i in (ell, *triple)))
        for r in right_ids:
            for triple in combinations(w_ids, 3):
                assert not convex(tuple(points[i] for i in (r, *triple)))
            full = tuple(sorted((ell, *w_ids, r)))
            circuit = first_bad_four(full, points)
            internal = tuple(i for i in circuit if i in w_ids)
            external = tuple(i for i in circuit if i in (ell, r))
            assert internal == expected_trace
            assert external == (ell,)
            repaired = tuple(sorted((ell, *complement, r)))
            assert not convex(tuple(points[i] for i in repaired))
            pairs += 1

    return {
        "m": m,
        "points": len(points),
        "endpoint_pairs": pairs,
        "fixed_one_plus_three_trace": list(expected_trace),
        "discarded_complement_rank": len(complement),
        "minimum_interval_deletions_for_one_endpoint_ear": m - 2,
        "all_complement_reattachments_fail": True,
    }


def main() -> None:
    certificate = {
        "description": "2+2 interval-complement repair and scalable 1+3 seam-jet obstruction",
        "positive_two_plus_two": positive_two_plus_two_audit(),
        "one_plus_three_regressions": [
            one_plus_three_instance(m) for m in (6, 9, 12)
        ],
        "claims": [
            "a 2+2 circuit between individually compatible endpoint ears is repaired by adjoining the complement to both endpoints",
            "the complement output recovers the endpoint pair and fixed interval tag",
            "literal aggregate radial tilt obeys the heavy-endpoint-or-output-bank inequality",
            "a fixed 1+3 trace can coexist with quadratically many endpoint pairs for which complement reattachment always fails",
            "the 1+3 regression requires deletion of all but two interval labels before the seam theorem applies",
        ],
    }
    output = Path(__file__).with_name("seam_jet_interval_complement_certificate.json")
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
