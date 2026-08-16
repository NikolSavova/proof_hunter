#!/usr/bin/env python3
"""Exact audits for the circuit-localized attack on Erdos 838.

The script checks four facts used in REPORT.md.

1. Edge-pocket factorization of a link is false, even for six integer points.
2. Pair conflicts between individually addable points are confined to equal or
   adjacent edge pockets.
3. Repairable nonfaces have the asserted ear-replacement structure, and the
   exact two-extension moment identity holds on the saved twenty-point record.
4. Pointwise half-curvature is asymptotically false on a realizable iterated
   strong-glue family; the failures occur in periodic blocks.
"""

from __future__ import annotations

import itertools
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
TILTED = ROOT / "agent_tilted_switch"
GRADED = ROOT / "agent_graded_supersat"
sys.path[:0] = [str(TILTED), str(GRADED)]

from tilted_switch_audit import face_table, orient, profile, repair_degree  # noqa: E402
from graded_balanced import central_template, vertical_iterate  # noqa: E402


Point = tuple[int, int]


def hull_order(points: list[Point], mask: int) -> list[int]:
    ids = [i for i in range(len(points)) if mask >> i & 1]
    if len(ids) <= 2:
        return ids
    ids.sort(key=lambda i: points[i])
    lower: list[int] = []
    for i in ids:
        while len(lower) >= 2 and orient(
            points[lower[-2]], points[lower[-1]], points[i]
        ) <= 0:
            lower.pop()
        lower.append(i)
    upper: list[int] = []
    for i in reversed(ids):
        while len(upper) >= 2 and orient(
            points[upper[-2]], points[upper[-1]], points[i]
        ) <= 0:
            upper.pop()
        upper.append(i)
    return lower[:-1] + upper[:-1]


def mask_of(ids: list[int]) -> int:
    return sum(1 << i for i in ids)


def edge_pocket(points: list[Point], face: int, point: int) -> int:
    """Unique support edge violated by an individually addable point."""
    hull = hull_order(points, face)
    violated = [
        i
        for i in range(len(hull))
        if orient(points[hull[i]], points[hull[(i + 1) % len(hull)]], points[point]) < 0
    ]
    if len(violated) != 1:
        raise AssertionError((face, point, hull, violated))
    return violated[0]


def in_open_triangle(p: Point, a: Point, b: Point, c: Point) -> bool:
    s = orient(a, b, c)
    return all(
        s * value > 0
        for value in (orient(a, b, p), orient(b, c, p), orient(c, a, p))
    )


def factorization_counterexample() -> dict[str, object]:
    points = [(0, 0), (3, 0), (3, 3), (0, 3), (1, -10), (-10, 1)]
    assert all(orient(points[i], points[j], points[k]) for i, j, k in itertools.combinations(range(6), 3))
    faces = face_table(points)
    base = mask_of([0, 1, 2, 3])
    q, x = 4, 5
    assert faces[base] and faces[base | (1 << q)] and faces[base | (1 << x)]
    assert not faces[base | (1 << q) | (1 << x)]
    iq, ix = edge_pocket(points, base, q), edge_pocket(points, base, x)
    assert (iq - ix) % 4 in (1, 3)  # adjacent edge pockets
    return {
        "points": points,
        "base_indices": [0, 1, 2, 3],
        "individual_additions": [q, x],
        "edge_pockets": [iq, ix],
        "base_plus_each_is_convex": True,
        "base_plus_both_is_convex": False,
    }


def random_pair_locality_audit() -> dict[str, int]:
    checked_faces = checked_pairs = 0
    for seed in range(20):
        rng = random.Random(seed)
        n = 12
        while True:
            points = [(i, rng.randrange(-10**8, 10**8)) for i in range(n)]
            if all(
                orient(points[i], points[j], points[k])
                for i, j, k in itertools.combinations(range(n), 3)
            ):
                break
        faces = face_table(points)
        for base, good in enumerate(faces):
            r = base.bit_count()
            if not good or r < 4:
                continue
            addable = [
                q for q in range(n) if not (base >> q & 1) and faces[base | (1 << q)]
            ]
            pockets = {q: edge_pocket(points, base, q) for q in addable}
            checked_faces += 1
            for q, x in itertools.combinations(addable, 2):
                i, j = pockets[q], pockets[x]
                if (i - j) % r not in (0, 1, r - 1):
                    assert faces[base | (1 << q) | (1 << x)]
                    checked_pairs += 1
    return {"random_integer_records": 20, "faces_checked": checked_faces, "nonadjacent_pairs_checked": checked_pairs}


def saved_twenty_audit() -> dict[str, object]:
    records = json.loads(
        (ROOT / "agent_dual_number_amortization" / "half_weight_search_records.json").read_text()
    )["exact_records"]
    ys = list(map(int, records["20"]["y_at_x_0_through_19"]))
    points = list(enumerate(ys))
    n = len(points)
    faces = face_table(points)
    values = profile(faces, n)
    full = (1 << n) - 1

    maximal = [0] * (n + 1)
    universal_from_parents = [0] * (n + 1)
    for base, good in enumerate(faces):
        if not good:
            continue
        r = base.bit_count()
        addable = [
            q for q in range(n) if not (base >> q & 1) and faces[base | (1 << q)]
        ]
        if not addable:
            maximal[r] += 1
        if r < 3:
            continue
        for q in addable:
            if all(
                x == q or not faces[base | (1 << q) | (1 << x)]
                for x in addable
            ):
                universal_from_parents[r + 1] += 1
    for r in range(4, n + 1):
        assert universal_from_parents[r] == r * maximal[r]

    # Ear classification of every repair incidence.
    interior_repairs = hull_repairs = 0
    repair_hist: Counter[int] = Counter()
    depth_two = [0] * (n + 1)
    repairable = [0] * (n + 1)
    for mask, good in enumerate(faces):
        if good or mask.bit_count() < 4:
            continue
        hull = hull_order(points, mask)
        hull_mask = mask_of(hull)
        inner = mask ^ hull_mask
        if faces[inner]:
            depth_two[mask.bit_count()] += 1
        repairs = [i for i in range(n) if mask >> i & 1 and faces[mask ^ (1 << i)]]
        if repairs:
            repairable[mask.bit_count()] += 1
            repair_hist[len(repairs)] += 1
        for x in repairs:
            if inner >> x & 1:
                assert inner == 1 << x
                interior_repairs += 1
                continue
            hull_repairs += 1
            pos = hull.index(x)
            left, right = hull[pos - 1], hull[(pos + 1) % len(hull)]
            inner_ids = [i for i in range(n) if inner >> i & 1]
            assert inner_ids
            assert all(
                in_open_triangle(points[y], points[left], points[x], points[right])
                for y in inner_ids
            )
            # The hidden interior set is precisely a convex replacement chain
            # between the two neighbours of the repaired hull vertex.
            chain = inner | (1 << left) | (1 << right)
            assert faces[chain]

    # Exact two-extension identity and the planar error bound E_r <= B_(r+1).
    double_rows = []
    for r in range(3, n - 1):
        lhs = 0
        boundary_next = 0
        repair_error = 0
        for mask, good in enumerate(faces):
            k = mask.bit_count()
            if good and k == r:
                outside = full ^ mask
                u = sum(faces[mask | (1 << q)] for q in range(n) if outside >> q & 1)
                lhs += math.comb(u, 2)
            elif not good and k == r + 2:
                d = repair_degree(mask, faces)
                repair_error += math.comb(d, 2)
                boundary_next += d
        successful = math.comb(r + 2, 2) * values[r + 2]
        assert lhs == successful + repair_error
        assert repair_error <= boundary_next
        double_rows.append(
            {
                "r": r,
                "sum_faces_choose_u_2": lhs,
                "successful_two_extensions": successful,
                "repair_error": repair_error,
                "boundary_B_r_plus_1": boundary_next,
            }
        )

    nested_rows = []
    for k in range(4, n + 1):
        if depth_two[k] or repairable[k]:
            denominator = k * values[k] * 2 ** (k - 1) if values[k] else 0
            nested_rows.append(
                {
                    "k": k,
                    "v_k": values[k],
                    "all_depth_two_subsets": depth_two[k],
                    "repairable_nonfaces": repairable[k],
                    "all_depth_two_over_2_to_k_minus_1_k_v_k": (
                        depth_two[k] / denominator if denominator else None
                    ),
                    "repairable_over_2_to_k_minus_1_k_v_k": (
                        repairable[k] / denominator if denominator else None
                    ),
                }
            )
    return {
        "n": n,
        "profile": values,
        "repair_degree_histogram": dict(sorted(repair_hist.items())),
        "interior_repair_incidences": interior_repairs,
        "hull_ear_repair_incidences": hull_repairs,
        "maximal_face_counts": maximal,
        "universal_conflict_vertices_from_rank_below": universal_from_parents,
        "two_extension_rows": double_rows,
        "nested_pair_overcount_rows": nested_rows,
    }


def curvature_countertest() -> dict[str, object]:
    h, depth = 10, 12
    template = central_template(h)
    log_n = depth * math.log2(template[0])
    cutoff = math.ceil(log_n) + 2
    n, _, _, convex = vertical_iterate(template, depth, cutoff)
    probabilities: list[tuple[int, float]] = []
    for r in range(3, math.floor(log_n) + 1):
        if convex[r] and convex[r + 1]:
            probabilities.append(
                (r, (r + 1) * convex[r + 1] / ((n - r) * convex[r]))
            )
    ratios = [
        (r, q / p, max(0.0, -math.log2(q / p) - 1))
        for (r, p), (s, q) in zip(probabilities, probabilities[1:])
        if s == r + 1
    ]
    bad = [(r, ratio, excess) for r, ratio, excess in ratios if ratio < 0.5]
    interior = [row for row in ratios if row[0] <= 0.9 * log_n]
    assert len(bad) >= 20
    return {
        "family": "vertical_iterate(central_template(h=10), depth=12)",
        "log2_n": log_n,
        "bad_ratio_rows": [
            {"r": r, "p_r_plus_1_over_p_r": ratio, "excess_bits_beyond_halving": excess}
            for r, ratio, excess in bad
        ],
        "cumulative_excess_bits_through_0.9_log2_n": sum(row[2] for row in interior),
        "cumulative_excess_divided_by_log2_n": sum(row[2] for row in interior) / log_n,
    }


def main() -> None:
    output = {
        "mode": "circuit_hardcore_localization_audit",
        "factorization_counterexample": factorization_counterexample(),
        "pair_locality_random_audit": random_pair_locality_audit(),
        "saved_twenty_point_audit": saved_twenty_audit(),
        "curvature_countertest": curvature_countertest(),
    }
    HERE.mkdir(parents=True, exist_ok=True)
    path = HERE / "certificate.json"
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(f"wrote {path}")
    print(json.dumps(output["pair_locality_random_audit"], sort_keys=True))
    curve = output["curvature_countertest"]
    print(
        "curvature",
        f"log2n={curve['log2_n']:.6f}",
        f"bad_rows={len(curve['bad_ratio_rows'])}",
        f"excess/log2n={curve['cumulative_excess_divided_by_log2_n']:.6f}",
    )


if __name__ == "__main__":
    main()
