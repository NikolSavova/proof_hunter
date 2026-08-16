#!/usr/bin/env python3
"""Exact audit for FIXED_ANCHOR_RELOCATION_CANCELLATION_GATE."""

from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))

import reflection_trace as rt  # noqa: E402


Point = tuple[Fraction, Fraction]


def convex(points: list[Point]) -> bool:
    if len(points) <= 3:
        return True
    ordered = sorted(points)

    def chain(sequence: list[Point]) -> list[Point]:
        result: list[Point] = []
        for point in sequence:
            while (len(result) >= 2
                   and rt.determinant(result[-2], result[-1], point) <= 0):
                result.pop()
            result.append(point)
        return result

    return len(chain(ordered)[:-1]
               + chain(list(reversed(ordered)))[:-1]) == len(points)


def chain(points: list[Point], sign: int) -> bool:
    ordered = sorted(points)
    return all((rt.determinant(ordered[i], ordered[j], ordered[k]) > 0)
               == (sign > 0)
               for i, j, k in itertools.combinations(range(len(ordered)), 3))


def families(points: list[Point]):
    faces = []
    caps = []
    cups = []
    for mask in range(1, 1 << len(points)):
        subset = [points[i] for i in range(len(points)) if mask >> i & 1]
        if convex(subset):
            faces.append(mask)
        if chain(subset, -1):
            caps.append(mask)
        if chain(subset, 1):
            cups.append(mask)
    return faces, caps, cups


def rank_profile(points: list[Point]):
    profile = {}
    for mask in range(1, 1 << len(points)):
        if convex([points[i] for i in range(len(points)) if mask >> i & 1]):
            profile[mask.bit_count()] = profile.get(mask.bit_count(), 0) + 1
    return profile


def anchor_erasure_checks():
    q = sorted(rt.pascal_cell(4, 2, Fraction(1, 97)))
    positions = [
        (Fraction(-20), Fraction(-7)),
        (Fraction(0), Fraction(20)),
        (Fraction(21), Fraction(8)),
    ]
    q_profile = rank_profile(q)
    vq = sum(q_profile.values())
    assert vq == 50
    values = []
    for point in positions:
        profile = rank_profile(q + [point])
        # Coefficientwise: each base face has at most two anchor masks.
        for rank, count in profile.items():
            base_same = 1 if rank == 0 else q_profile.get(rank, 0)
            base_previous = (1 if rank - 1 == 0
                             else q_profile.get(rank - 1, 0))
            assert count <= base_same + base_previous
        values.append(sum(profile.values()))
        assert values[-1] + 1 <= 2 * (vq + 1)
    return values


def wrapper_checks():
    q = sorted(rt.pascal_cell(4, 2, Fraction(1, 97)))
    p = sorted(rt.strong_glue(q, q, Fraction(1, 16384)))
    faces, caps, cups = families(p)
    q_faces, q_caps, q_cups = families(q)
    assert (len(q_caps), len(q_cups), len(q_faces)) == (31, 31, 50)
    assert (len(caps), len(cups), len(faces)) == (248, 248, 1061)

    n = len(q)
    cap_inc = set()
    cup_inc = set()
    for a in q_caps:
        for y in range(n):
            subset = [q[i] for i in range(n) if (a | (1 << y)) >> i & 1]
            if chain(subset, -1):
                cap_inc.add((a, y))
    for b in q_cups:
        for z in range(n):
            subset = [q[i] for i in range(n) if (b | (1 << z)) >> i & 1]
            if chain(subset, 1):
                cup_inc.add((b, z))
    assert len(cap_inc) == len(cup_inc) == 126
    rank_bound = max(
        max(mask.bit_count() for mask in q_caps),
        max(mask.bit_count() for mask in q_cups),
    )
    assert rank_bound == 3
    assert len(cap_inc) <= 2 * rank_bound * len(q_caps)
    assert len(cup_inc) <= 2 * rank_bound * len(q_cups)

    good = 0
    for a in q_caps:
        for z in range(n):
            left_record = a | (1 << (n + z))
            for y in range(n):
                for b in q_cups:
                    right_record = (1 << y) | (b << n)
                    actual = convex([p[i] for i in range(2 * n)
                                     if (left_record | right_record) >> i & 1])
                    expected = ((a, y) in cap_inc and (b, z) in cup_inc)
                    assert actual == expected
                    good += int(actual)
    assert good == 126 ** 2 == 15876

    # Exact ceiling after selecting k anchors on each side. We grant that
    # every incidence using a selected anchor becomes repairable.
    best_by_k = []
    for k in range(n + 1):
        best_cap = 0
        best_cup = 0
        for selected in itertools.combinations(range(n), k):
            selected = set(selected)
            cap_covered = sum((a, y) in cap_inc or y in selected
                              for a in q_caps for y in range(n))
            cup_covered = sum((b, z) in cup_inc or z in selected
                              for b in q_cups for z in range(n))
            best_cap = max(best_cap, cap_covered)
            best_cup = max(best_cup, cup_covered)
        assert best_cap <= len(cap_inc) + k * len(q_caps)
        assert best_cup <= len(cup_inc) + k * len(q_cups)
        assert (best_cap * best_cup * n * n
                <= ((2 * rank_bound + k) ** 2
                    * (n * len(q_caps)) ** 2))
        best_by_k.append(best_cap * best_cup)
    assert best_by_k[0] == good
    assert best_by_k[-1] == (n * len(q_caps)) ** 2
    return best_by_k


def five_point_minimizer_check():
    p = [
        (Fraction(6), Fraction(15)),
        (Fraction(18), Fraction(22)),
        (Fraction(13), Fraction(4)),
        (Fraction(12), Fraction(17)),
        (Fraction(20), Fraction(29)),
    ]
    faces, _, _ = families(p)
    assert len(faces) == 26
    extension_counts = []
    for deleted in range(5):
        q = p[:deleted] + p[deleted + 1:]
        q_faces, _, _ = families(q)
        extension_counts.append(len(faces) - len(q_faces))
        # Every general-position five-point configuration has at least the
        # 25 rank-at-most-three faces and one convex four-set. Hence 26 is
        # the global lower bound, certifying the actual extension cell.
        assert len(faces) == 25 + 1
    return extension_counts


def main():
    relocations = anchor_erasure_checks()
    coverage = wrapper_checks()
    extensions = five_point_minimizer_check()
    print("PASS: fixed-anchor cancellation; relocation V=%s; "
          "wrapper coverage k=0,1,6=%d,%d,%d; minimizer extensions=%s"
          % (relocations, coverage[0], coverage[1], coverage[6], extensions))


if __name__ == "__main__":
    main()
