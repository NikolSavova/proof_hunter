#!/usr/bin/env python3
"""Exact probe for whole-hull (onion-layer) amortization.

If H is the global hull, h=|H|, and I=P-H, test

  h Z_I(1/2) + n (Z_P(1/2)-Z_I(1/2))
      <= 2 (Z_P(1)-Z_I(1)).

Together with HW2 on I, this inequality proves HW2 on P.
"""

from __future__ import annotations

import argparse
import random

from rooted_amortization_probe import audit as vertex_audit
from rooted_amortization_probe import hull, random_points, saved_examples
from link_half_weight_probe import is_convex_face


def audit(points):
    n = len(points)
    hull_set = set(hull(points))
    h = len(hull_set)
    interior_mask = sum(1 << i for i in range(n) if i not in hull_set)
    parent_v = interior_v = 0
    parent_w_scaled = interior_w_scaled = 0
    for mask in range(1 << n):
        if not is_convex_face(points, mask):
            continue
        weight = 1 << (n - mask.bit_count())
        parent_v += 1
        parent_w_scaled += weight
        if mask & ~interior_mask == 0:
            interior_v += 1
            interior_w_scaled += weight
    lhs = h * interior_w_scaled + n * (parent_w_scaled - interior_w_scaled)
    rhs = 2 * (parent_v - interior_v) * (1 << n)
    return lhs <= rhs, lhs, rhs, parent_v, interior_v, h


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

    worst = None
    for points, label in cases:
        record = audit(points)
        ratio = record[1] / record[2]
        if worst is None or ratio > worst[0]:
            worst = (ratio, label, len(points), record)
        if not record[0]:
            print(f"FAIL {label}: n={len(points)}, ratio={ratio:.12g}")
            print("record=", record)
            print("points=", points)
            raise SystemExit(1)
    print(f"PASS {len(cases)} configurations")
    print(
        f"worst ratio={worst[0]:.12g} at {worst[1]}, n={worst[2]}, "
        f"record={worst[3]}"
    )


if __name__ == "__main__":
    main()
