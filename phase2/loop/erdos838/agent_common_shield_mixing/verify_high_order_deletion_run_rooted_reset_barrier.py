#!/usr/bin/env python3
"""Exact checks for HIGH_ORDER_DELETION_RUN_ROOTED_RESET_BARRIER."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb, log2
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from verify_critical_edge_dispersion_rechart_ledger import (  # noqa: E402
    configuration,
    convex,
)

sys.path.insert(0, str(ROOT / "agent_outer_internal_product"))
from verify_opposite_singleton_return_rooted_antialignment import (  # noqa: E402
    profile,
    construction,
    rooted_convex,
)


def role_face_data():
    left, right, ys, ws, lowers, roots = configuration()
    roles = [[left], ys, ws, [right], lowers, roots]
    points = [point for role in roles for point in role]
    point_role = {
        point: role_index
        for role_index, role in enumerate(roles)
        for point in role
    }
    faces = []
    for mask in range(1 << len(points)):
        face = tuple(points[i] for i in range(len(points)) if mask >> i & 1)
        if convex(face):
            occupied = frozenset(point_role[point] for point in face)
            empty = frozenset(range(len(roles))) - occupied
            faces.append((face, empty))
    return roles, faces


def deletion_transform_audit():
    roles, faces = role_face_data()
    q = len(roles)
    checked = 0

    # Every order-t transform.
    for t in range(q + 1):
        masks = [frozenset(mask) for mask in combinations(range(q), t)]
        lhs = 0
        for deleted in masks:
            lhs += sum(deleted <= empty for _, empty in faces)
        rhs = sum(comb(len(empty), t) for _, empty in faces)
        assert lhs == rhs
        checked += len(masks)

    # Every cyclic interval length, with repetitions retained at k=q.
    interval_checks = 0
    for k in range(1, q + 1):
        intervals = [
            frozenset((start + offset) % q for offset in range(k))
            for start in range(q)
        ]
        lhs = sum(
            sum(interval <= empty for _, empty in faces)
            for interval in intervals
        )
        rhs = sum(
            sum(interval <= empty for interval in intervals)
            for _, empty in faces
        )
        assert lhs == rhs
        interval_checks += len(intervals)
    return len(faces), checked, interval_checks


def parabola_point(index):
    return (Fraction(index), Fraction(index * index))


def cyclic_interval(start, length, q):
    return frozenset((start + offset) % q for offset in range(length))


def run_erasure_audit():
    cases = 0
    for q in range(3, 7):
        for d in range(2, 5):
            # Tags and labels are all rational points on one parabola, so
            # every selected record and partial output is an ordinary face.
            tags = [parabola_point(i) for i in range(q)]
            roles = [
                [parabola_point(q + i * d + value) for value in range(d)]
                for i in range(q)
            ]
            all_points = tags + [point for role in roles for point in role]
            assert convex(all_points)

            for k in range(1, q):
                outputs = Counter()
                records = 0
                for start in range(q):
                    deleted = cyclic_interval(start, k, q)
                    # A proper cyclic interval has exactly one cyclic run.
                    boundaries = sum(
                        ((i in deleted) != ((i + 1) % q in deleted))
                        for i in range(q)
                    )
                    assert boundaries == 2
                    for word in product(range(d), repeat=q):
                        full_face = [tags[start]] + [
                            roles[i][word[i]] for i in range(q)
                        ]
                        assert convex(full_face)
                        output_face = [tags[start]] + [
                            roles[i][word[i]] for i in range(q)
                            if i not in deleted
                        ]
                        assert convex(output_face)
                        key = (start,) + tuple(
                            None if i in deleted else word[i]
                            for i in range(q)
                        )
                        outputs[key] += 1
                        records += 1

                assert records == q * d**q
                assert len(outputs) == q * d ** (q - k)
                assert set(outputs.values()) == {d**k}

                # Literal atom weight 1/n: the physical load scales exactly.
                n = len(all_points)
                weighted_total = Fraction(records, n)
                weighted_load = Fraction(d**k, n)
                assert Fraction(weighted_total, weighted_load) == len(outputs)
                cases += 1
    return cases


def phi(length, correction):
    return Fraction(1, 2) * length * length - correction * length * log2(length)


def scale_audit():
    rows = []
    correction = 8.0
    kappa = 0.25
    for power in (10, 12, 14, 16, 18):
        length = float(2**power)
        level2 = log2(length)
        level3 = log2(level2)
        run_fraction = 1.0 / level2
        complement_log = length + log2(1.0 - run_fraction)
        child_log = length - level3

        deletion_deficit = phi(length, correction) - phi(
            complement_log, correction
        )
        child_deficit = phi(length, correction) - phi(
            child_log, correction
        )
        erased_log = (kappa * length / level2) * (
            length - log2(kappa * length)
        )

        expected_deletion = length * log2(2.718281828459045) / level2
        assert 0.75 < deletion_deficit / expected_deletion < 1.25
        assert 0.65 < child_deficit / (length * level3) < 1.05
        assert erased_log > 4.0 * child_deficit
        rows.append((power, deletion_deficit, child_deficit, erased_log))
    return rows


def rooted_profile_audit():
    m = 14
    block, a, b, root = construction(m)
    assert profile(block, (), rooted_convex) == 2**m
    cap = profile(block, (a, root), rooted_convex)
    cup = profile(block, (b, root), rooted_convex)
    assert (cap, cup) == (86, 106)
    assert cap * cup == 9116 < 2**m
    return cap, cup


def main():
    faces, masks, intervals = deletion_transform_audit()
    erasure_cases = run_erasure_audit()
    rows = scale_audit()
    cap, cup = rooted_profile_audit()
    print(
        "PASS: faces=%d deletion-masks=%d intervals=%d erasure-cases=%d "
        "scale-L=2^%d rooted=(%d,%d)<2^14"
        % (faces, masks, intervals, erasure_cases, rows[-1][0], cap, cup)
    )


if __name__ == "__main__":
    main()
