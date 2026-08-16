#!/usr/bin/env python3
"""Exact verifier for RAW_RANK_MATCHED_ENDPOINT_DICHOTOMY.md."""

from __future__ import annotations

import importlib.util
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTER = HERE.parent / "agent_outer_internal_product"


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


TWO = load_module(
    "two_reference_for_rank_matching",
    OUTER / "verify_two_reference_hall_demand.py",
)
R = TWO.R


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


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


def convex(points):
    return len(points) == len(set(points)) == len(hull(points))


def enumerate_faces(points):
    result = []
    for mask in range(1 << len(points)):
        face = tuple(i for i in range(len(points)) if mask >> i & 1)
        if convex([points[i] for i in face]):
            result.append(face)
    return result


def rank_matching_audit():
    points = TWO.POINTS
    faces = TWO.enumerate_faces(points)
    face_set = set(faces)
    total = sum((Q(1, 1 << len(face)) for face in faces), Q())
    assert len(faces) == 449

    baseline = defaultdict(int)
    for face in faces:
        if len(face) >= 2:
            baseline[(face[0], face[-1], len(face))] += 1

    histories = []
    for face in faces:
        for depth in range(len(face) // 2):
            parent = face[depth : len(face) - depth]
            assert parent in face_set
            edge = (parent[0], parent[-1])
            histories.append((face, depth, edge, len(parent)))

    # The fixed literal tag is a genuine blocked ordinary face.
    fixed_tag = (1, 2, 3, 4, 5)
    assert fixed_tag in face_set
    selected = []
    for history in histories:
        _, _, edge, _ = history
        if not all(edge[0] < vertex < edge[1] for vertex in fixed_tag):
            continue
        tagged_union = tuple((edge[0], *fixed_tag, edge[1]))
        if tagged_union in face_set:
            continue
        selected.append(history)
    assert selected

    def audit_family(family):
        raw = defaultdict(int)
        for _, depth, edge, rank in family:
            raw[(depth, edge, rank)] += 1

        p_rank = {
            (edge, rank): Q(count, 1 << rank) / total
            for (left, right, rank), count in baseline.items()
            for edge in ((left, right),)
        }
        p_edge = defaultdict(Q)
        for (edge, _), mass in p_rank.items():
            p_edge[edge] += mass

        # Equations (1) and (2), exactly and cell by cell.
        by_depth_edge = defaultdict(list)
        for (depth, edge, rank), count in raw.items():
            completion_count = baseline[(edge[0], edge[1], rank)]
            assert completion_count > 0
            q = Q(count, (1 << rank) * (4**depth)) / total
            p = p_rank[(edge, rank)]
            density = Q(count, completion_count)
            assert density == (4**depth) * q / p
            by_depth_edge[(depth, edge)].append((rank, q, density))

        for (depth, edge), rows in by_depth_edge.items():
            h = sum((q for _, q, _ in rows), Q()) / p_edge[edge]
            average_density = sum(
                (p_rank[(edge, rank)] / p_edge[edge]) * density
                for rank, _, density in rows
            )
            # Ranks with no selected histories have density zero and are
            # absent from rows, so the equality still includes their zero.
            assert (4**depth) * h == average_density
            assert max(density for _, _, density in rows) >= (4**depth) * h

        maximum_depths = 1 + max(depth for depth, _, _ in raw)
        assert len(family) <= maximum_depths * len(faces)
        thresholds = sorted({Q(0), Q(1), Q(2)} | {
            Q(count, baseline[(edge[0], edge[1], rank)])
            for (depth, edge, rank), count in raw.items()
        })
        v2 = len(points) * (len(points) - 1) // 2
        for rho in thresholds:
            low_raw = Q()
            low_likelihood = Q()
            for (depth, edge, rank), count in raw.items():
                completion_count = baseline[(edge[0], edge[1], rank)]
                density = Q(count, completion_count)
                if density > rho:
                    continue
                low_raw += count
                q = Q(count, (1 << rank) * (4**depth)) / total
                low_likelihood += q / p_edge[edge]
            assert low_raw <= rho * maximum_depths * len(faces)
            assert low_likelihood <= Q(4, 3) * rho * v2
            assert low_likelihood <= Q(4, 3) * rho * len(faces)
        return len(raw), len(family), maximum_depths

    return audit_family(histories), audit_family(selected)


def varying_tag_obstruction_audit():
    named = {
        "L": (Q(-10), Q(0)),
        "R": (Q(10), Q(0)),
        "s0": (Q(-8), Q(-36)),
        "s1": (Q(-6), Q(-64)),
        "s2": (Q(6), Q(-64)),
        "s3": (Q(8), Q(-36)),
        "a": (Q(-3), Q(2)),
        "b": (Q(-2), Q(12)),
        "q1": (Q(1), Q(15)),
        "q2": (Q(5), Q(10)),
        "q3": (Q(4), Q(3)),
        "q4": (Q(0), Q(1)),
    }
    order = sorted(named, key=lambda name: named[name][0])
    points = [named[name] for name in order]
    index = {name: order.index(name) for name in order}
    assert all(orient(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))
    faces = enumerate_faces(points)
    face_set = set(faces)

    edge = (index["L"], index["R"])
    A = (index["a"], index["b"])
    circuit = tuple(sorted((*edge, *A)))
    assert not convex([points[i] for i in circuit])

    extras = [index[name] for name in ("q1", "q2", "q3", "q4")]
    tags = [tuple(sorted((*A, *choice))) for choice in combinations(extras, 2)]
    assert len(tags) == 6
    assert all(tag in face_set for tag in tags)
    assert all(all(edge[0] < vertex < edge[1] for vertex in tag) for tag in tags)
    assert all(tuple(sorted((*edge, *tag))) not in face_set for tag in tags)

    rank = 4
    bank = [face for face in faces
            if len(face) == rank and (face[0], face[-1]) == edge]
    assert len(bank) == 34
    assert all(tuple(sorted(set(tag) | set(output))) not in face_set
               for tag in tags for output in bank)

    total = sum((Q(1, 1 << len(face)) for face in faces), Q())
    p = Q(len(bank), 1 << rank) / total
    tagged_record_count = 0
    for tag in tags:
        histories = bank
        count = len(histories)
        q = Q(count, 1 << rank) / total
        assert count == len(bank)
        assert q / p == 1
        tagged_record_count += count
    assert tagged_record_count == 6 * 34 == 204
    return len(faces), len(tags), len(bank), tagged_record_count


def scarcity_audit(m=6):
    edge_points = [(Q(-2), Q(0)), (Q(2), Q(0))]
    left = [
        (Q(-4), Q(-4)),
        (Q(-407, 100), Q(-389, 100)),
        (Q(-391, 100), Q(-431, 100)),
    ]
    right = [
        (Q(79, 20), Q(-393, 100)),
        (Q(207, 50), Q(-211, 50)),
        (Q(403, 100), Q(-93, 25)),
    ]
    low = []
    for i in range(1, m + 1):
        x = Q(-1) + Q(2 * i, m + 1)
        low.append((x, Q(-100) - x * x))
    points = sorted(left + edge_points + low + right)
    assert all(orient(a, b, c) != 0 for a, b, c in combinations(points, 3))
    assert convex(low)

    e_left, e_right = edge_points
    assert all(e_left[0] < point[0] < e_right[0] for point in low)
    assert all(convex([e_left, e_right, *trace])
               for size in range(3) for trace in combinations(low, size))
    assert all(not convex([e_left, e_right, *trace])
               for size in range(3, m + 1) for trace in combinations(low, size))
    assert all(convex([root_left, e_left, e_right, root_right])
               for root_left in left for root_right in right)

    interval_half_weight = sum(
        (Q(1, 1 << size) for size in range(m + 1)
         for _ in combinations(low, size)), Q()
    )
    assert interval_half_weight == Q(3, 2) ** m
    compatible_half_weight = Q()
    compatible_count_by_rank = defaultdict(int)
    for size in range(m + 1):
        for trace in combinations(low, size):
            if not convex([e_left, e_right, *trace]):
                continue
            compatible_half_weight += Q(1, 1 << (size + 2))
            compatible_count_by_rank[size + 2] += 1
    quadratic = Q(1) + Q(m, 2) + Q(m * (m - 1), 8)
    assert compatible_half_weight == quadratic / 4
    assert compatible_count_by_rank[2] == 1

    raw_histories = len(left) * len(right)
    rank_resolved_ratio = Q(raw_histories, 4)
    aggregate_tilt = Q(raw_histories, 4 * quadratic)
    assert raw_histories == 9
    assert Q(raw_histories, compatible_count_by_rank[2]) == (
        4 * rank_resolved_ratio
    )
    assert aggregate_tilt == Q(raw_histories, 16) / compatible_half_weight
    common_tag = tuple(low[:3])
    assert convex(list(common_tag))
    assert not convex([e_left, e_right, *common_tag])
    return interval_half_weight, compatible_half_weight, raw_histories, aggregate_tilt


def main():
    full, fixed = rank_matching_audit()
    tags = varying_tag_obstruction_audit()
    scarcity = scarcity_audit()
    print("raw rank-matched endpoint dichotomy: PASS")
    print(f"rank audit full={full}, fixed-blocked-tag={fixed}")
    print(f"varying-tag obstruction faces/tags/bank/records={tags}")
    print(f"baseline scarcity interval/G/N/h={scarcity}")


if __name__ == "__main__":
    main()
