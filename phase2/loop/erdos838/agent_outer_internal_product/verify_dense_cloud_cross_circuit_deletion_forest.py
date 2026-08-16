#!/usr/bin/env python3
"""Exact verifier for the dense-cloud cross-circuit deletion forest."""

from collections import defaultdict
from itertools import combinations
from math import comb
from pathlib import Path
import random
import sys


ROOT = Path(__file__).resolve().parents[1]
COMMON = ROOT / "agent_common_shield_mixing"
sys.path.insert(0, str(COMMON))
import verify_dense_hall_two_cloud_profile_barrier as dense  # noqa: E402


def canonical_bad_four(left, right):
    """Return the lexicographically first cross bad four-subset."""
    union = tuple(sorted(left | right))
    for part in combinations(union, 4):
        part = frozenset(part)
        if not (part & left) or not (part & right):
            continue
        if not dense.convex(tuple(part)):
            return part
    raise AssertionError("bad union without a cross four-circuit")


def route_pair(left, right):
    """Canonical X-side deletion route."""
    original = frozenset(left)
    residual = set(left)
    deleted = set()
    witnesses = []
    while not dense.convex(tuple(residual | set(right))):
        circuit = canonical_bad_four(frozenset(residual), frozenset(right))
        x = min(circuit & residual)
        witnesses.append((circuit, x))
        residual.remove(x)
        deleted.add(x)
    assert frozenset(residual) == original - deleted
    return frozenset(deleted), frozenset(residual), tuple(witnesses)


def audit_forest(points_x, points_y, family_a, family_b):
    groups = defaultdict(list)
    routed = 0
    x_ground, y_ground = frozenset(points_x), frozenset(points_y)
    for left in family_a:
        for right in family_b:
            mask, residual, witnesses = route_pair(left, right)
            output = frozenset(residual | right)
            assert dense.convex(tuple(output))
            for circuit, x in witnesses:
                assert x in circuit
                assert circuit & x_ground and circuit & y_ground
                assert not dense.convex(tuple(circuit))
            groups[mask].append((output, frozenset(left), frozenset(right)))
            routed += 1

    # Fixed-mask output is a physical load-one decoder.
    for mask, records in groups.items():
        decoded = {}
        for output, left, right in records:
            assert output not in decoded
            recovered_right = output & y_ground
            recovered_left = (output & x_ground) | mask
            assert recovered_left == left and recovered_right == right
            decoded[output] = (left, right)

    max_rank = max(map(len, family_a), default=0)
    mask_bound = sum(comb(len(points_x), t)
                     for t in range(max_rank + 1))
    assert len(groups) <= mask_bound
    assert max(map(len, groups.values()), default=0) * mask_bound >= routed

    # Refined terminal-survival inequality.
    for survivors in range(max_rank + 1):
        selected = {
            mask: [record for record in records
                   if len(record[1] - mask) >= survivors]
            for mask, records in groups.items()
        }
        selected = {mask: records for mask, records in selected.items()
                    if records}
        mass = sum(map(len, selected.values()))
        depth_bound = sum(comb(len(points_x), t)
                          for t in range(max_rank - survivors + 1))
        assert len(selected) <= depth_bound
        if mass:
            assert max(map(len, selected.values())) * depth_bound >= mass
    return groups


def arbitrary_geometry_audit():
    rng = random.Random(8381517)
    points = []
    while len(points) < 10:
        p = (rng.randrange(-100, 101), rng.randrange(-100, 101))
        if p in points:
            continue
        if any(dense.orient(a, b, p) == 0
               for a, b in combinations(points, 2)):
            continue
        points.append(p)
    x, y = points[:5], points[5:]
    faces_x = [frozenset(part)
               for rank in range(1, 4)
               for part in combinations(x, rank)
               if dense.convex(part)]
    faces_y = [frozenset(part)
               for rank in range(1, 4)
               for part in combinations(y, rank)
               if dense.convex(part)]
    groups = audit_forest(x, y, faces_x, faces_y)
    return len(faces_x), len(faces_y), len(groups)


def parabolic_saturation():
    size, rank = 7, 3
    x = dense.parabolic_cloud(dense.G0, size, 1)
    y = dense.parabolic_cloud(dense.X0, size, -1)
    family_a = [frozenset(part) for part in combinations(x, rank)]
    family_b = [frozenset(part) for part in combinations(y, rank)]
    assert all(dense.convex(tuple(face)) for face in family_a + family_b)

    groups = audit_forest(x, y, family_a, family_b)
    alphabet = comb(size, rank)
    assert len(groups) == alphabet
    assert set(groups) == set(family_a)
    assert all(len(records) == alphabet for records in groups.values())

    for left in family_a:
        for right in family_b:
            assert not dense.convex(tuple(left | right))
            for subrank in range(1, rank + 1):
                for residual in combinations(left, subrank):
                    assert not dense.convex(tuple(residual) + tuple(right))
    return alphabet, alphabet * alphabet


def binomial_survival_audit():
    checks = 0
    for support in range(20, 81):
        for rank in range(3, min(10, support // 3)):
            for survivors in range(1, min(4, rank) + 1):
                shadow = sum(comb(support, t)
                             for t in range(rank - survivors + 1))
                exact_layer = comb(support, rank)
                product_ratio = 1.0
                for i in range(survivors):
                    product_ratio *= ((support - rank + i + 1)
                                      / (rank - i))
                lower = product_ratio / (rank + 1)
                assert exact_layer / shadow + 1e-12 >= lower
                checks += 1
    return checks


def main():
    arbitrary = arbitrary_geometry_audit()
    saturation = parabolic_saturation()
    checks = binomial_survival_audit()
    print("PASS: deletion forest",
          f"arbitrary={arbitrary}",
          f"parabolic alphabet={saturation[0]} bad={saturation[1]}",
          f"binomial_checks={checks}")


if __name__ == "__main__":
    main()
