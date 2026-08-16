#!/usr/bin/env python3
"""Exact audits for the exterior-ear replacement lane of Erdos 838.

The script has two logically separate jobs.

1.  On exact integral point sets, enumerate every exterior blocked incidence
    (A,p), form I=(A+p) minus ext(A+p) and B=ext(A+p), and check the sharp
    multiplicity bounds for the pair (I,B).
2.  Certify a common-singleton-ear cloud in which arbitrarily many blockers
    can be placed while no three of them can replace the hidden vertex at
    once.  The finite instance here has eight blockers.  This is a local-map
    obstruction, not a counterexample to any global f-vector inequality.

Only integer orientation predicates are used.
"""

from __future__ import annotations

import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
Point = tuple[int, int]


def orient(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def hull_indices(points: tuple[Point, ...], labels: tuple[int, ...]) -> tuple[int, ...]:
    """Return the hull vertices in counterclockwise order, without repetition."""
    if len(labels) <= 2:
        return tuple(sorted(labels, key=lambda i: points[i]))
    ordered = sorted(labels, key=lambda i: points[i])

    def half(seq: list[int]) -> list[int]:
        out: list[int] = []
        for i in seq:
            while len(out) >= 2 and orient(points[out[-2]], points[out[-1]], points[i]) <= 0:
                out.pop()
            out.append(i)
        return out

    lower = half(ordered)
    upper = half(list(reversed(ordered)))
    return tuple(lower[:-1] + upper[:-1])


def convex(points: tuple[Point, ...], labels: tuple[int, ...]) -> bool:
    return len(labels) <= 3 or len(hull_indices(points, labels)) == len(labels)


def general_position(points: tuple[Point, ...]) -> bool:
    return all(
        orient(points[i], points[j], points[k]) != 0
        for i, j, k in itertools.combinations(range(len(points)), 3)
    )


def exterior_blocked_records(points: tuple[Point, ...]) -> list[dict[str, object]]:
    n = len(points)
    records: list[dict[str, object]] = []
    for mask in range(1 << n):
        labels = tuple(i for i in range(n) if mask >> i & 1)
        r = len(labels)
        if r < 4 or not convex(points, labels):
            continue
        hull_a = set(hull_indices(points, labels))
        assert hull_a == set(labels)
        for p in range(n):
            if mask >> p & 1:
                continue
            s = labels + (p,)
            hull_s = set(hull_indices(points, s))
            if p not in hull_s or len(hull_s) == len(s):
                continue
            hidden = tuple(sorted(set(labels) - hull_s))
            outer = tuple(sorted(hull_s))
            assert hidden
            assert set(hidden).isdisjoint(outer)
            assert set(hidden) | set(outer) == set(s)
            records.append(
                {
                    "rank": r,
                    "source": labels,
                    "root": p,
                    "hidden": hidden,
                    "outer": outer,
                }
            )
    return records


def audit_pair_multiplicity(points: tuple[Point, ...]) -> dict[str, object]:
    assert general_position(points)
    records = exterior_blocked_records(points)
    groups: dict[tuple[tuple[int, ...], tuple[int, ...]], list[int]] = defaultdict(list)
    by_hidden_size = Counter()
    for row in records:
        hidden = tuple(row["hidden"])
        outer = tuple(row["outer"])
        groups[(hidden, outer)].append(int(row["root"]))
        by_hidden_size[len(hidden)] += 1

    worst = 0
    worst_singleton = 0
    examples: list[dict[str, object]] = []
    for (hidden, outer), roots in groups.items():
        union = tuple(sorted(set(hidden) | set(outer)))
        repairs = [
            q
            for q in union
            if convex(points, tuple(x for x in union if x != q))
        ]
        assert set(roots).issubset(repairs)
        assert len(repairs) <= 3  # the general repair-degree theorem
        if len(hidden) == 1:
            assert hidden[0] in repairs
            assert len(roots) <= 2
            worst_singleton = max(worst_singleton, len(roots))
        # Exterior roots are hull vertices of the union.  Three of them
        # would force a triangular hull and at least two inner points; a
        # two-inner-point restriction then permits only one triangle-vertex
        # repair.  Hence the exterior-root bound is two for every hidden
        # size, not merely for singleton ears.
        assert len(roots) <= 2
        worst = max(worst, len(roots))
        if len(roots) >= 2 and len(examples) < 5:
            examples.append(
                {
                    "hidden": hidden,
                    "outer": outer,
                    "roots": sorted(roots),
                    "all_repairs": repairs,
                }
            )

    return {
        "n": len(points),
        "number_of_exterior_incidences": len(records),
        "number_of_distinct_pairs": len(groups),
        "hidden_size_histogram": dict(sorted(by_hidden_size.items())),
        "maximum_pair_multiplicity": worst,
        "maximum_singleton_pair_multiplicity": worst_singleton,
        "multiple_root_examples": examples,
    }


def audit_frame_rectangles(points: tuple[Point, ...]) -> dict[str, object]:
    """Exhaustively check fixed-root/tangent cross completion."""
    records = exterior_blocked_records(points)
    frames: dict[
        tuple[int, int, int, int, int],
        dict[str, set[tuple[int, ...]]],
    ] = defaultdict(lambda: {"hidden": set(), "retained": set(), "sources": set()})
    for row in records:
        p = int(row["root"])
        outer = tuple(row["outer"])
        order = hull_indices(points, outer)
        pos = order.index(p)
        x = order[(pos - 1) % len(order)]
        y = order[(pos + 1) % len(order)]
        hidden = tuple(row["hidden"])
        retained = tuple(sorted(set(outer) - {p}))
        frame = (p, min(x, y), max(x, y), int(row["rank"]), len(hidden))
        frames[frame]["hidden"].add(hidden)
        frames[frame]["retained"].add(retained)
        frames[frame]["sources"].add(tuple(row["source"]))

    total_products = 0
    root_rank_products: Counter[tuple[int, int]] = Counter()
    maximum_product = 0
    maximum_ratio = (0, 1)
    maximum_frame: dict[str, object] | None = None
    for frame, pools in frames.items():
        outputs: set[tuple[int, ...]] = set()
        for hidden in pools["hidden"]:
            for retained in pools["retained"]:
                labels = tuple(sorted(set(hidden) | set(retained)))
                assert len(labels) == frame[3]
                assert convex(points, labels)
                outputs.add(labels)
        product = len(pools["hidden"]) * len(pools["retained"])
        assert len(outputs) == product
        assert len(pools["sources"]) <= product
        total_products += product
        root_rank_products[(frame[0], frame[3])] += product
        if product > maximum_product:
            maximum_product = product
        ratio = (product, len(pools["sources"]))
        if ratio[0] * maximum_ratio[1] > maximum_ratio[0] * ratio[1]:
            maximum_ratio = ratio
            maximum_frame = {
                "frame_root_tangents_rank_hidden_size": frame,
                "hidden_pool": len(pools["hidden"]),
                "retained_pool": len(pools["retained"]),
                "source_edges": len(pools["sources"]),
                "completed_rectangle": product,
            }

    # Audit the sharpened Lemma 4 of AMORTIZED_RESET.md.  For fixed
    # (root, rank), a completed face C recovers its unique frame from the
    # repaired hull ext(C+root); rectangles from different frames are
    # therefore disjoint.
    face_counts: Counter[int] = Counter()
    for mask in range(1 << len(points)):
        labels = tuple(i for i in range(len(points)) if mask >> i & 1)
        if convex(points, labels):
            face_counts[len(labels)] += 1

    completed_by_root_rank: dict[
        tuple[int, int], set[tuple[int, ...]]
    ] = defaultdict(set)
    for frame, pools in frames.items():
        root, _, _, rank, _ = frame
        for hidden in pools["hidden"]:
            for retained in pools["retained"]:
                completed = tuple(sorted(set(hidden) | set(retained)))
                key = (root, rank)
                assert completed not in completed_by_root_rank[key]
                completed_by_root_rank[key].add(completed)

    aggregate_rows: list[dict[str, object]] = []
    maximum_aggregate_ratio = (0, 1)
    for (root, rank), product_sum in sorted(root_rank_products.items()):
        assert product_sum == len(completed_by_root_rank[(root, rank)])
        capacity = face_counts[rank]
        assert product_sum <= capacity
        if product_sum * maximum_aggregate_ratio[1] > (
            maximum_aggregate_ratio[0] * capacity
        ):
            maximum_aggregate_ratio = (product_sum, capacity)
        aggregate_rows.append(
            {
                "root": root,
                "rank": rank,
                "sum_of_rectangle_sizes": product_sum,
                "rank_faces": face_counts[rank],
                "disjoint_rectangle_capacity": capacity,
            }
        )

    return {
        "number_of_fixed_frames": len(frames),
        "sum_of_rectangle_sizes": total_products,
        "maximum_rectangle_size": maximum_product,
        "maximum_completion_ratio": f"{maximum_ratio[0]}/{maximum_ratio[1]}",
        "maximum_ratio_frame": maximum_frame,
        "aggregate_fixed_root_rank_rows": aggregate_rows,
        "maximum_aggregate_capacity_ratio": (
            f"{maximum_aggregate_ratio[0]}/{maximum_aggregate_ratio[1]}"
        ),
    }


def common_ear_points() -> tuple[Point, ...]:
    """A diamond source followed by an eight-point strict cap cloud.

    Labels 0,1,2,3 are x,a,y,z.  Each later point p is exterior to the
    diamond and hides exactly a.  The cloud lies on a strict concave
    parabola, so its points are all vertices of their own hull, while only
    its two extreme selected points can lie on the lower replacement chain.
    """
    source = ((-20, 0), (2, -10), (20, 0), (1, 100))
    ts = (-8, -6, -4, -2, 1, 3, 5, 7)
    cloud = tuple((t, -1000 - 3 * t * t) for t in ts)
    return source + cloud


def audit_common_ear() -> dict[str, object]:
    points = common_ear_points()
    assert general_position(points)
    source = (0, 1, 2, 3)
    retained = (0, 2, 3)
    cloud = tuple(range(4, len(points)))
    assert convex(points, source)
    rows = []
    for p in cloud:
        s = source + (p,)
        hs = set(hull_indices(points, s))
        assert hs == set(retained + (p,))
        rows.append({"root": p, "hidden": sorted(set(source) - hs)})

    # The cloud itself is in convex position, so all its subsets are faces.
    assert convex(points, cloud)

    replacement_histogram = Counter()
    replacement_examples: dict[int, tuple[int, ...]] = {}
    for size in range(len(cloud) + 1):
        for chosen in itertools.combinations(cloud, size):
            if convex(points, retained + chosen):
                replacement_histogram[size] += 1
                replacement_examples.setdefault(size, chosen)

    # Empty, singleton, and every pair attach.  No triple (and therefore no
    # larger subset) attaches while retaining x,y,z.
    assert replacement_histogram[0] == 1
    assert replacement_histogram[1] == len(cloud)
    assert replacement_histogram[2] == len(tuple(itertools.combinations(cloud, 2)))
    assert all(replacement_histogram[size] == 0 for size in range(3, len(cloud) + 1))

    return {
        "points": points,
        "source_labels": source,
        "retained_labels": retained,
        "cloud_labels": cloud,
        "blocker_checks": rows,
        "cloud_is_convex": True,
        "replacement_histogram": dict(sorted(replacement_histogram.items())),
        "interpretation": (
            "Each cloud point hides the same singleton.  Any two blockers can "
            "replace it, but no three can do so while the other source vertices "
            "are retained; the cloud itself supplies a large independent face."
        ),
    }


def audit_common_target_star() -> dict[str, object]:
    """Many singleton-ear sources whose raw hull replacement is identical."""
    outer = ((-20, 0), (0, -1000), (20, 0), (1, 100))
    ts = (-7, -5, -3, -1, 2, 4, 6, 8)
    inner = tuple(
        (t, -100 - 2 * t * t - (1 if t == -5 else 0)) for t in ts
    )
    points = outer + inner
    assert general_position(points)
    outer_labels = (0, 1, 2, 3)
    retained = (0, 2, 3)
    rows = []
    for q in range(4, len(points)):
        source = retained + (q,)
        assert convex(points, source)
        union = source + (1,)
        assert set(hull_indices(points, union)) == set(outer_labels)
        rows.append({"source": source, "root": 1, "repaired_hull": outer_labels})
    assert len({tuple(row["repaired_hull"]) for row in rows}) == 1
    return {
        "points": points,
        "number_of_sources": len(rows),
        "common_target": outer_labels,
        "rows": rows,
        "interpretation": (
            "The raw map (A,p) -> ext(A+p) has inverse multiplicity eight "
            "here, and the same construction admits arbitrarily many generic "
            "rational inner points.  Retaining the hidden face I removes this "
            "collapse."
        ),
    }


def main() -> None:
    # The ordinary-LC counterexample is an adversarial exact order type with
    # a rich mixture of interior and exterior repair incidences.
    ys = (
        -4015,
        2780,
        8170,
        5429,
        -4867,
        -2452,
        -5229,
        -5102,
        7389,
        -596,
        -8841,
        -8375,
        -8464,
        -8566,
    )
    lc_points = tuple((i, y) for i, y in enumerate(ys))
    output = {
        "pair_multiplicity_audit": audit_pair_multiplicity(lc_points),
        "fixed_frame_rectangle_audit": audit_frame_rectangles(lc_points),
        "common_ear_audit": audit_common_ear(),
        "common_target_star_audit": audit_common_target_star(),
    }
    path = HERE / "ear_map_certificate.json"
    path.write_text(json.dumps(output, indent=2) + "\n")
    print("wrote", path)
    print(json.dumps(output["pair_multiplicity_audit"], indent=2))
    print(json.dumps(output["common_ear_audit"]["replacement_histogram"], indent=2))


if __name__ == "__main__":
    main()
