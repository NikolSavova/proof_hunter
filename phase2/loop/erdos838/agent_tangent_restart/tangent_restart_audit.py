#!/usr/bin/env python3
"""Exact audits for the dynamic two-tangent restart lane.

The main search tests whether convex replacement chains supported on
nonadjacent edge pockets remain compatible in arbitrary multiplicity.  This
is the natural all-orders strengthening of the proved pair-locality lemma.
All predicates use exact integer determinants.
"""

from __future__ import annotations

import itertools
import json
import math
import random
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "agent_tilted_switch"))

from tilted_switch_audit import face_table, orient  # noqa: E402


Point = tuple[int, int]


def hull_order(points: list[Point], mask: int) -> list[int]:
    ids = [i for i in range(len(points)) if mask >> i & 1]
    if len(ids) <= 2:
        return ids
    ids.sort(key=lambda i: points[i])
    lo: list[int] = []
    for i in ids:
        while len(lo) >= 2 and orient(points[lo[-2]], points[lo[-1]], points[i]) <= 0:
            lo.pop()
        lo.append(i)
    hi: list[int] = []
    for i in reversed(ids):
        while len(hi) >= 2 and orient(points[hi[-2]], points[hi[-1]], points[i]) <= 0:
            hi.pop()
        hi.append(i)
    return lo[:-1] + hi[:-1]


def pocket(points: list[Point], base: int, q: int) -> int | None:
    hull = hull_order(points, base)
    bad = [
        i
        for i in range(len(hull))
        if orient(points[hull[i]], points[hull[(i + 1) % len(hull)]], points[q]) < 0
    ]
    return bad[0] if len(bad) == 1 else None


def random_points(seed: int, n: int) -> list[Point]:
    rng = random.Random(seed)
    while True:
        points = [(i, rng.randrange(-10**9, 10**9)) for i in range(n)]
        if all(
            orient(points[i], points[j], points[k])
            for i, j, k in itertools.combinations(range(n), 3)
        ):
            return points


def nonadjacent_chain_search(records: int = 80, n: int = 12) -> dict[str, object]:
    checked = 0
    rooted_equivalences = 0
    for seed in range(records):
        points = random_points(seed, n)
        faces = face_table(points)
        for base, good in enumerate(faces):
            r = base.bit_count()
            if not good or r < 4:
                continue
            groups: list[list[int]] = [[] for _ in range(r)]
            for q in range(n):
                if base >> q & 1 or not faces[base | (1 << q)]:
                    continue
                i = pocket(points, base, q)
                assert i is not None
                groups[i].append(q)
            hull = hull_order(points, base)
            for i, group in enumerate(groups):
                endpoints = (1 << hull[i]) | (1 << hull[(i + 1) % r])
                for cm in range(1 << len(group)):
                    C = sum(1 << group[t] for t in range(len(group)) if cm >> t & 1)
                    assert faces[base | C] == faces[endpoints | C]
                    rooted_equivalences += 1
            for i in range(r):
                for j in range(i + 1, r):
                    if (i - j) % r in (1, r - 1):
                        continue
                    left = groups[i]
                    right = groups[j]
                    for lm in range(1, 1 << len(left)):
                        L = sum(1 << left[t] for t in range(len(left)) if lm >> t & 1)
                        if not faces[base | L]:
                            continue
                        for rm in range(1, 1 << len(right)):
                            R = sum(1 << right[t] for t in range(len(right)) if rm >> t & 1)
                            if not faces[base | R]:
                                continue
                            checked += 1
                            if not faces[base | L | R]:
                                return {
                                    "status": "counterexample",
                                    "seed": seed,
                                    "points": points,
                                    "base": [q for q in range(n) if base >> q & 1],
                                    "pocket_indices": [i, j],
                                    "left_chain": [q for q in left if L >> q & 1],
                                    "right_chain": [q for q in right if R >> q & 1],
                                    "checked_before_failure": checked,
                                }
    return {
        "status": "pass",
        "records": records,
        "n": n,
        "two_pocket_chain_products_checked": checked,
        "single_pocket_rooted_equivalences_checked": rooted_equivalences,
    }


def matching_chain_search(records: int = 40, n: int = 13) -> dict[str, object]:
    checked = 0
    for seed in range(10_000, 10_000 + records):
        points = random_points(seed, n)
        faces = face_table(points)
        for base, good in enumerate(faces):
            r = base.bit_count()
            if not good or r < 6:
                continue
            groups: list[list[int]] = [[] for _ in range(r)]
            for q in range(n):
                if base >> q & 1 or not faces[base | (1 << q)]:
                    continue
                i = pocket(points, base, q)
                assert i is not None
                groups[i].append(q)
            chain_masks: list[list[int]] = []
            for group in groups:
                masks = []
                for cm in range(1, 1 << len(group)):
                    C = sum(1 << group[t] for t in range(len(group)) if cm >> t & 1)
                    if faces[base | C]:
                        masks.append(C)
                chain_masks.append(masks)
            for im in range(1, 1 << r):
                chosen = [i for i in range(r) if im >> i & 1]
                if len(chosen) < 3 or any((im >> i & 1) and (im >> ((i + 1) % r) & 1) for i in range(r)):
                    continue
                pools = [chain_masks[i] for i in chosen]
                if any(not pool for pool in pools):
                    continue
                for choices in itertools.product(*pools):
                    checked += 1
                    union = base
                    for C in choices:
                        union |= C
                    if not faces[union]:
                        return {
                            "status": "counterexample",
                            "seed": seed,
                            "points": points,
                            "base": [q for q in range(n) if base >> q & 1],
                            "pocket_indices": chosen,
                            "chains": [[q for q in range(n) if C >> q & 1] for C in choices],
                            "checked_before_failure": checked,
                        }
    return {"status": "pass", "records": records, "n": n, "checked": checked}


def pascal_block_regression() -> dict[str, object]:
    graded = ROOT / "agent_graded_supersat"
    sys.path.insert(0, str(graded))
    from graded_balanced import central_template, vertical_iterate

    rows = []
    for h in (4, 6, 8, 10, 12):
        depth = 8
        period = 2 * h - 4
        template = central_template(h)
        log_n = depth * math.log2(template[0])
        cutoff = math.floor(0.9 * log_n) + period + 4
        n, _, _, values = vertical_iterate(template, depth, cutoff)
        p = {
            r: (r + 1) * values[r + 1] / ((n - r) * values[r])
            for r in range(3, cutoff)
            if values[r] and values[r + 1]
        }
        credits = []
        for start in range(3, math.floor(0.9 * log_n) - period + 1, period):
            if all(r in p and r + 1 in p for r in range(start, start + period)):
                product = math.prod(p[r + 1] / p[r] for r in range(start, start + period))
                credits.append(math.log2(product) + period)
        assert credits and min(credits) > 0
        rows.append(
            {
                "h": h,
                "depth": depth,
                "period": period,
                "log2_n": log_n,
                "blocks": len(credits),
                "minimum_credit_over_2_to_minus_period": min(credits),
                "last_credit": credits[-1],
            }
        )
    return {"status": "pass", "rows": rows}


def polynomial_add(a: list[int], b: list[int]) -> list[int]:
    out = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return out


def polynomial_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def rooted_profile(u: Point, v: Point, Q: list[Point]) -> list[int]:
    values = [0] * (len(Q) + 1)
    for mask in range(1 << len(Q)):
        chosen = [Q[i] for i in range(len(Q)) if mask >> i & 1]
        points = [u, v] + chosen
        if len(hull_order(points, (1 << len(points)) - 1)) == len(points):
            values[len(chosen)] += 1
    while len(values) > 1 and not values[-1]:
        values.pop()
    return values


def pivot_parts(u: Point, v: Point, Q: list[Point]) -> tuple[Point, list[Point], list[Point], list[Point]]:
    side = 1 if orient(u, v, Q[0]) > 0 else -1
    assert all(side * orient(u, v, q) > 0 for q in Q)
    # Signed distance to uv has the common positive scale |uv|, so maximizing
    # the exact determinant chooses the outermost point without division.
    x = max(Q, key=lambda q: side * orient(u, v, q))
    left: list[Point] = []
    right: list[Point] = []
    blocked: list[Point] = []
    sxv = orient(u, x, v)
    svu = orient(x, v, u)
    for q in Q:
        if q == x:
            continue
        beyond_left = orient(u, x, q) * sxv < 0
        beyond_right = orient(x, v, q) * svu < 0
        assert not (beyond_left and beyond_right)
        if beyond_left:
            left.append(q)
        elif beyond_right:
            right.append(q)
        else:
            blocked.append(q)
    return x, left, right, blocked


def rooted_pivot_audit(records: int = 120, m: int = 10) -> dict[str, object]:
    checked_subsets = 0
    max_blocked = 0
    for seed in range(20_000, 20_000 + records):
        rng = random.Random(seed)
        u, v = (0, 0), (1000, 0)
        while True:
            Q = [(rng.randrange(-500, 1501), rng.randrange(1, 2001)) for _ in range(m)]
            points = [u, v] + Q
            if len(set(points)) == len(points) and all(
                orient(points[i], points[j], points[k])
                for i, j, k in itertools.combinations(range(len(points)), 3)
            ):
                break
        x, left, right, blocked = pivot_parts(u, v, Q)
        full = rooted_profile(u, v, Q)
        without = rooted_profile(u, v, [q for q in Q if q != x])
        selected = [0] + polynomial_mul(rooted_profile(u, x, left), rooted_profile(x, v, right))
        predicted = polynomial_add(without, selected)
        assert full == predicted, (seed, full, predicted, x, left, right, blocked)
        checked_subsets += 1 << m
        max_blocked = max(max_blocked, len(blocked))
    return {
        "status": "pass",
        "records": records,
        "points_per_record": m + 2,
        "rooted_subsets_checked": checked_subsets,
        "maximum_discarded_middle_pocket": max_blocked,
    }


def main() -> None:
    result = {
        "nonadjacent_chain_search": nonadjacent_chain_search(),
        "matching_chain_search": matching_chain_search(),
        "pascal_block_regression": pascal_block_regression(),
        "rooted_pivot_recurrence": rooted_pivot_audit(),
    }
    HERE.mkdir(parents=True, exist_ok=True)
    (HERE / "certificate.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
