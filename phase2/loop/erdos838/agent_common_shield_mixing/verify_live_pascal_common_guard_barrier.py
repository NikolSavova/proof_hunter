#!/usr/bin/env python3
"""Exact verifier for LIVE_PASCAL_COMMON_GUARD_MULTIPLICATION_BARRIER.md.

The geometric audit uses the independent rational realization in
agent_geometry/audit_geometry.py.  The asymptotic theorem is proved in the
report; the DP loop here is a finite regression of its exact recurrences and
normalization envelope.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations
from math import ceil, comb, log2
from pathlib import Path
import importlib.util
import sys


ROOT = Path(__file__).resolve().parent.parent
GEOMETRY = ROOT / "agent_geometry" / "audit_geometry.py"


def load_geometry():
    spec = importlib.util.spec_from_file_location("pascal_audit_geometry", GEOMETRY)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def all_nonempty_subsets(indices: tuple[int, ...]):
    for r in range(1, len(indices) + 1):
        yield from combinations(indices, r)


def exact_geometry_audit(g) -> dict[str, int]:
    # T(6,3)=T(5,2) prec T(5,3), with ten rational points in each child.
    n, i = 6, 3
    points = g.cell(n, i)
    left_size = comb(n - 1, i - 1)
    assert len(points) == comb(n, i) == 20
    assert left_size == 10

    left = tuple(range(left_size))
    right = tuple(range(left_size, len(points)))
    orient = g.orient_table(points)

    left_faces = [a for a in all_nonempty_subsets(left)
                  if g.is_convex(a, orient)]
    right_faces = [b for b in all_nonempty_subsets(right)
                   if g.is_convex(b, orient)]
    sources = [a for a in left_faces if not g.is_cap(a, orient)]
    pockets = [b for b in right_faces if not g.is_cup(b, orient)]

    assert len(left_faces) == len(right_faces) == 375
    assert len(sources) == len(pockets) == 274

    # Exhaust the exact strong-glue mixed-face classification, not merely the
    # selected rectangle.
    mixed_checks = 0
    for a in left_faces:
        for b in right_faces:
            got = g.is_convex(a + b, orient)
            want = g.is_cap(a, orient) and g.is_cup(b, orient)
            assert got == want, (a, b, got, want)
            mixed_checks += 1

    # Canonical first noncap triple and exact rank bucketing.
    buckets: dict[tuple[tuple[int, ...], int], list[tuple[int, ...]]] = defaultdict(list)
    for d in sources:
        bad_triples = [t for t in combinations(d, 3)
                       if not g.is_cap(t, orient)]
        assert bad_triples
        buckets[(min(bad_triples), len(d))].append(d)

    key = max(buckets, key=lambda k: len(buckets[k]))
    root, rank = key
    fibre = buckets[key]
    assert len(root) == 3 and len(fibre) == 6 and rank == 5
    assert all(set(root).issubset(d) for d in fibre)
    fixed_x = root[0]
    assert all(fixed_x in d for d in fibre)

    # The fixed root blocks every physical point of the opposite child.
    root_checks = 0
    for z in right:
        assert not g.is_convex(root + (z,), orient)
        root_checks += 1

    # Exhaust every record and every possible deleted guard subset.  The full
    # source is the unique guard that releases the right face.
    record_checks = 0
    guard_checks = 0
    for d in fibre:
        dset = set(d)
        for u in pockets:
            assert not g.is_convex(d + u, orient)
            record_checks += 1
            for k in range(len(d) + 1):
                for guard in combinations(d, k):
                    remaining = tuple(sorted(dset.difference(guard)))
                    released = g.is_convex(remaining + u, orient)
                    assert released == (k == len(d)), (d, u, guard)
                    guard_checks += 1

    # Explicit finite rank formulas in both children.
    for child, child_i in ((left, 2), (right, 3)):
        cap_rank = max(len(a) for a in all_nonempty_subsets(child)
                       if g.is_cap(a, orient))
        cup_rank = max(len(a) for a in all_nonempty_subsets(child)
                       if g.is_cup(a, orient))
        face_rank = max(len(a) for a in all_nonempty_subsets(child)
                        if g.is_convex(a, orient))
        assert cap_rank == child_i + 1
        assert cup_rank == (n - 1) - child_i + 1
        assert face_rank == n - 1

    return {
        "left_faces": len(left_faces),
        "right_faces": len(right_faces),
        "sources": len(sources),
        "pockets": len(pockets),
        "fibre": len(fibre),
        "rank": rank,
        "mixed_checks": mixed_checks,
        "root_checks": root_checks,
        "record_checks": record_checks,
        "guard_checks": guard_checks,
    }


def exact_dp_audit(g, nmax: int = 96) -> dict[str, float | int]:
    caps, cups = g.dp_counts(nmax)
    faces = g.dp_convex_counts(nmax, caps, cups)

    worst_scaled_gap = 0.0
    checked = 0
    for n in range(6, nmax + 1, 2):
        h = n // 2
        parent = faces[n][h]
        left = faces[n - 1][h - 1]
        right = faces[n - 1][h]
        cap = caps[n - 1][h - 1]
        cup = cups[n - 1][h]

        assert left == right
        assert cap == cup
        assert parent == left + right + cap * cup

        source_nonprofile = left - cap
        pocket_nonprofile = right - cup
        assert source_nonprofile == pocket_nonprofile > 0
        # From n=6 onward the nonprofile complement already retains at least
        # half the exact child bank.
        assert 2 * source_nonprofile >= left

        # Exact integer check of a deliberately loose O(n log n) envelope.
        exponent = ceil(4 * n * log2(n + 2))
        assert parent <= left * (1 << exponent)

        gap = log2(parent) - log2(left)
        worst_scaled_gap = max(worst_scaled_gap,
                               gap / (n * log2(n + 2)))
        checked += 1

    return {
        "central_splits": checked,
        "nmax": nmax,
        "worst_gap_over_nlogn": worst_scaled_gap,
    }


def main() -> None:
    g = load_geometry()
    geometry = exact_geometry_audit(g)
    dp = exact_dp_audit(g)
    print("PASS: live Pascal common-guard multiplication barrier")
    print("geometry:", geometry)
    print("DP:", dp)


if __name__ == "__main__":
    main()
