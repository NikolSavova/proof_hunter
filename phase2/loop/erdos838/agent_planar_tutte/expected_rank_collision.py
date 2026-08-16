#!/usr/bin/env python3
"""Find exact planar configurations with identical ER(p) but different Z(z).

Such a pair is a certificate that Gordon's one-variable expected-rank
polynomial, including its planar coefficient antisymmetry, does not determine
the half-weight quantity.  Coordinates and all polynomial coefficients are
integers.
"""

from __future__ import annotations

import argparse
import json
import math
import random
from pathlib import Path

from link_half_weight_probe import is_convex_face, is_general_position, closure_size


HERE = Path(__file__).resolve().parent


def invariants(points):
    n = len(points)
    profile = [0] * (n + 1)
    er = [0] * (n + 1)
    hull_interior = [[0] * (n + 1) for _ in range(n + 1)]
    closed_seen = set()
    for mask in range(1 << n):
        if not is_convex_face(points, mask):
            continue
        d = mask.bit_count()
        profile[d] += 1

        # Recover the closure mask, not just its size, to audit the bijection.
        if d <= 2:
            closed_mask = mask
        else:
            ids = [i for i in range(n) if mask >> i & 1]
            # A point is in cl(mask) iff adding it does not enlarge the closure
            # size.  The explicit orientation implementation is in the probe.
            target_size = closure_size(points, mask)
            closed_mask = mask
            for i in range(n):
                if mask >> i & 1:
                    continue
                if closure_size(points, mask | (1 << i)) == target_size:
                    closed_mask |= 1 << i
        assert closed_mask not in closed_seen
        closed_seen.add(closed_mask)

        feasible_size = n - closed_mask.bit_count()
        interior_size = closed_mask.bit_count() - d
        hull_interior[d][interior_size] += 1
        for j in range(d + 1):
            er[feasible_size + j] += feasible_size * (-1) ** j * math.comb(d, j)
    assert len(closed_seen) == sum(profile)
    return tuple(profile), tuple(er), tuple(tuple(row) for row in hull_interior)


def random_points(n, rng):
    while True:
        points = [(rng.randrange(1_000_000), rng.randrange(1_000_000)) for _ in range(n)]
        if len(set(points)) == n and is_general_position(points):
            return points


def half_weight_numerator(profile):
    n = len(profile) - 1
    return sum(value << (n - k) for k, value in enumerate(profile))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=8)
    parser.add_argument("--trials", type=int, default=100_000)
    parser.add_argument("--seed", type=int, default=838)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    rng = random.Random(args.seed)
    seen = {}

    for trial in range(args.trials):
        points = random_points(args.n, rng)
        profile, er, hull_interior = invariants(points)
        old = seen.get(er)
        if old is not None and old[1] != profile:
            old_points, old_profile, old_hull_interior = old
            certificate = {
                "n": args.n,
                "trial": trial,
                "expected_rank_coefficients": list(er),
                "first": {
                    "coordinates": old_points,
                    "convex_profile": list(old_profile),
                    "X_hull_vertices_by_interior_points": [list(row) for row in old_hull_interior],
                    "V": sum(old_profile),
                    "two_to_n_times_Z_half": half_weight_numerator(old_profile),
                },
                "second": {
                    "coordinates": points,
                    "convex_profile": list(profile),
                    "X_hull_vertices_by_interior_points": [list(row) for row in hull_interior],
                    "V": sum(profile),
                    "two_to_n_times_Z_half": half_weight_numerator(profile),
                },
            }
            print(json.dumps(certificate, indent=2))
            if args.write:
                (HERE / "expected_rank_collision_certificate.json").write_text(
                    json.dumps(certificate, indent=2) + "\n"
                )
            return
        seen[er] = (points, profile, hull_interior)
    raise SystemExit(f"no collision in {args.trials} trials")


if __name__ == "__main__":
    main()
