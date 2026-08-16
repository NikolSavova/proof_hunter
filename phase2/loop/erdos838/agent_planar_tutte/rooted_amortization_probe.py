#!/usr/bin/env python3
"""Probe a two-state hull-vertex induction sufficient for HW2.

For a hull vertex e, let Z0 be the convex-subset polynomial of P-e and let
R_e be the link polynomial (convex subsets containing e, with e removed).
The rooted amortization inequality

    2 Z0(1/2) + n R_e(1/2) <= 4 R_e(1)

for at least one hull vertex, together with HW2 for P-e, implies HW2 for P.
This program searches exact configurations for a failure at every hull
vertex.
"""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

from link_half_weight_probe import is_convex_face, is_general_position


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    ids = sorted(range(len(points)), key=lambda i: points[i])
    lower = []
    for i in ids:
        while len(lower) >= 2 and orient(points[lower[-2]], points[lower[-1]], points[i]) <= 0:
            lower.pop()
        lower.append(i)
    upper = []
    for i in reversed(ids):
        while len(upper) >= 2 and orient(points[upper[-2]], points[upper[-1]], points[i]) <= 0:
            upper.pop()
        upper.append(i)
    return lower[:-1] + upper[:-1]


def audit(points):
    n = len(points)
    faces = [mask for mask in range(1 << n) if is_convex_face(points, mask)]
    # Work at denominator 2^n.  For e absent the contribution is 2^(n-|A|).
    # For the link term it is 2^n * 2^{-(|A|-1)}.
    records = []
    for e in hull(points):
        absent_scaled = sum(1 << (n - mask.bit_count()) for mask in faces if not mask >> e & 1)
        link_scaled = sum(1 << (n - mask.bit_count() + 1) for mask in faces if mask >> e & 1)
        link_count = sum(1 for mask in faces if mask >> e & 1)
        lhs = 2 * absent_scaled + n * link_scaled
        rhs = 4 * link_count * (1 << n)
        records.append((lhs <= rhs, lhs, rhs, e, absent_scaled, link_scaled, link_count))
    return records, len(faces)


def random_points(n, rng):
    while True:
        points = [(rng.randrange(1_000_000), rng.randrange(1_000_000)) for _ in range(n)]
        if len(set(points)) == n and is_general_position(points):
            return points


def saved_examples():
    direct = json.loads(
        (ROOT / "agent_lex_minimizer_search" / "direct_hull_certificates.json").read_text()
    )
    for key, item in direct.items():
        yield [tuple(p) for p in item["coordinates"]], f"direct-{key}"
    collision = json.loads((HERE / "expected_rank_collision_certificate.json").read_text())
    for key in ("first", "second"):
        yield [tuple(p) for p in collision[key]["coordinates"]], f"collision-{key}"

    chain_points = 12
    length = chain_points - 1
    yield (
        [(-1, chain_points**2)]
        + [(i, i * (length - i)) for i in range(chain_points)],
        "apex-concave-chain-n13",
    )

    middle = 11
    deep = (middle + 2) ** 3
    yield (
        [(-1, -deep)]
        + [(i, i * i) for i in range(1, middle + 1)]
        + [(middle + 1, -deep)],
        "two-deep-endpoint-wrapper-n13",
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--random", type=int, default=1000)
    parser.add_argument("--max-n", type=int, default=14)
    parser.add_argument("--seed", type=int, default=838)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    cases = list(saved_examples())
    for trial in range(args.random):
        n = rng.randrange(4, args.max_n + 1)
        cases.append((random_points(n, rng), f"random-{trial}-n{n}"))

    worst_best = None
    individual_failures = []
    for points, label in cases:
        records, face_count = audit(points)
        best = min(records, key=lambda row: row[1] / row[2])
        ratio = best[1] / best[2]
        if worst_best is None or ratio > worst_best[0]:
            worst_best = (ratio, label, len(points), face_count, best, records)
        for row in records:
            if not row[0]:
                individual_failures.append((label, row[3], row[1] / row[2]))
        if not any(row[0] for row in records):
            print(f"FAIL {label}: n={len(points)}, V={face_count}")
            print("points=", points)
            for row in records:
                print("e, ratio, link_count=", row[3], row[1] / row[2], row[6])
            raise SystemExit(1)

    ratio, label, n, face_count, best, records = worst_best
    print(f"PASS {len(cases)} configurations")
    print(
        f"worst best-vertex ratio={ratio:.12g} at {label}, n={n}, V={face_count}, "
        f"best_e={best[3]}, hull_size={len(records)}"
    )
    print(f"individual hull-vertex failures={len(individual_failures)}")
    for item in individual_failures[:8]:
        print("  ", item)


if __name__ == "__main__":
    main()
