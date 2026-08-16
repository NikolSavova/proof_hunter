#!/usr/bin/env python3
"""Exact checks for TWO_ANCHOR_DOUBLE_CIRCUIT_ELIMINATION_GATE.md."""

from __future__ import annotations

import itertools
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))

import reflection_trace as rt  # noqa: E402


Point = tuple[Fraction, Fraction]


def is_convex(points: list[Point]) -> bool:
    if len(points) <= 3:
        return True
    points = sorted(points)

    def half(seq: list[Point]) -> list[Point]:
        out: list[Point] = []
        for point in seq:
            while len(out) >= 2 and rt.determinant(out[-2], out[-1], point) <= 0:
                out.pop()
            out.append(point)
        return out

    return len(half(points)[:-1] + half(list(reversed(points)))[:-1]) == len(points)


def is_chain(points: list[Point], sign: int) -> bool:
    points = sorted(points)
    return all(
        (rt.determinant(points[i], points[j], points[k]) > 0) == (sign > 0)
        for i, j, k in itertools.combinations(range(len(points)), 3)
    )


def families(points: list[Point]) -> tuple[list[int], list[int], list[int]]:
    faces: list[int] = []
    caps: list[int] = []
    cups: list[int] = []
    for mask in range(1, 1 << len(points)):
        subset = [points[i] for i in range(len(points)) if mask >> i & 1]
        if is_convex(subset):
            faces.append(mask)
        if is_chain(subset, -1):
            caps.append(mask)
        if is_chain(subset, +1):
            cups.append(mask)
    return faces, caps, cups


def circuit_sign(points: list[Point], labels: tuple[int, ...]) -> dict[int, int]:
    assert len(labels) == 4
    signs: dict[int, int] = {}
    for index, label in enumerate(labels):
        other = [points[labels[j]] for j in range(4) if j != index]
        value = ((-1) ** index) * rt.determinant(*other)
        signs[label] = 1 if value > 0 else -1
    return signs


def inner_label(signs: dict[int, int]) -> int | None:
    values = list(signs.values())
    for label, sign in signs.items():
        if values.count(sign) == 1:
            return label
    return None


def orient_at(signs: dict[int, int], label: int, target: int) -> dict[int, int]:
    if signs[label] == target:
        return signs
    return {item: -sign for item, sign in signs.items()}


def elimination_compatible(
    candidate: dict[int, int],
    first: dict[int, int],
    second: dict[int, int],
    eliminated: int,
) -> bool:
    for label, sign in candidate.items():
        if label == eliminated:
            return False
        allowed: list[int] = []
        if label in first:
            allowed.append(first[label])
        if label in second:
            allowed.append(second[label])
        if sign not in allowed:
            return False
    return True


def canonical_bad_sides(q: list[Point]):
    _, caps, cups = families(q)
    cap_set, cup_set = set(caps), set(cups)
    left = {}
    for cap in caps:
        labels = [i for i in range(6) if cap >> i & 1]
        for y in range(6):
            if (cap | (1 << y)) in cap_set:
                continue
            witnesses = [
                pair for pair in itertools.combinations(labels, 2)
                if not is_chain([q[pair[0]], q[pair[1]], q[y]], -1)
            ]
            if witnesses:
                left[cap, y] = min(witnesses)
    right = {}
    for cup in cups:
        labels = [i for i in range(6) if cup >> i & 1]
        for z in range(6):
            if (cup | (1 << z)) in cup_set:
                continue
            witnesses = [
                pair for pair in itertools.combinations(labels, 2)
                if not is_chain([q[z], q[pair[0]], q[pair[1]]], +1)
            ]
            if witnesses:
                right[cup, z] = min(witnesses)
    assert len(left) == len(right) == 60
    return left, right


def audit_pascal_and_elimination():
    q = sorted(rt.pascal_cell(4, 2, Fraction(1, 97)))
    points = sorted(rt.strong_glue(q, q, Fraction(1, 16384)))
    assert rt.evaluate(q)[:3] == (31, 31, 50)
    left, right = canonical_bad_sides(q)

    type_counts: Counter[tuple[str, str]] = Counter()
    representatives = {}
    seam_loads: Counter[tuple[int, ...]] = Counter()
    two_face_loads: Counter[tuple[tuple[int, ...], tuple[int, ...]]] = Counter()

    for (cap, y), a_pair in left.items():
        for (cup, z_local), b_pair in right.items():
            z = z_local + 6
            b_physical = (b_pair[0] + 6, b_pair[1] + 6)
            c_left = tuple(sorted(a_pair + (y, z)))
            c_right = tuple(sorted((y, z) + b_physical))
            assert not is_convex([points[i] for i in c_left])
            assert not is_convex([points[i] for i in c_right])
            inner_left = inner_label(circuit_sign(points, c_left))
            inner_right = inner_label(circuit_sign(points, c_right))
            kind = (
                "y" if inner_left == y else "A",
                "z" if inner_right == z else "B",
            )
            type_counts[kind] += 1
            representatives.setdefault(kind, (a_pair, y, b_physical, z))

            a = min(a_pair)
            b = min(b_physical)
            seam = tuple(sorted((a, y, z, b)))
            assert is_convex([points[i] for i in seam])
            seam_loads[seam] += 1

            detached = tuple(
                [i for i in range(6) if cap >> i & 1]
                + [i + 6 for i in range(6) if cup >> i & 1]
            )
            assert is_convex([points[i] for i in detached])
            assert not is_convex([points[i] for i in detached + (y,)])
            assert not is_convex([points[i] for i in detached + (z,)])
            two_face_loads[detached, seam] += 1

    assert type_counts == Counter({
        ("A", "B"): 1444,
        ("A", "z"): 836,
        ("y", "B"): 836,
        ("y", "z"): 484,
    })
    assert len(seam_loads) == 121
    assert max(seam_loads.values()) == 108
    assert len(two_face_loads) == 3600
    assert max(two_face_loads.values()) == 1

    expected = {
        ("A", "B"): {"opposite": True, "y": (2, 1), "z": (2, 1)},
        ("A", "z"): {"opposite": False, "y": (1, 1), "z": (0, 2)},
        ("y", "B"): {"opposite": False, "y": (0, 2), "z": (1, 1)},
        ("y", "z"): {"opposite": True, "y": (0, 2), "z": (0, 2)},
    }
    for kind, (a_pair, y, b_pair, z) in representatives.items():
        first_labels = tuple(sorted(a_pair + (y, z)))
        second_labels = tuple(sorted((y, z) + b_pair))
        first_y = orient_at(circuit_sign(points, first_labels), y, +1)
        second_y = orient_at(circuit_sign(points, second_labels), y, -1)
        assert (first_y[z] == -second_y[z]) == expected[kind]["opposite"]
        union = sorted(set(first_labels + second_labels))
        for eliminated, name in ((y, "y"), (z, "z")):
            first = orient_at(circuit_sign(points, first_labels), eliminated, +1)
            second = orient_at(circuit_sign(points, second_labels), eliminated, -1)
            convex_count = bad_count = 0
            for labels in itertools.combinations(
                [label for label in union if label != eliminated], 4
            ):
                candidate = circuit_sign(points, labels)
                reverse = {label: -sign for label, sign in candidate.items()}
                if (elimination_compatible(candidate, first, second, eliminated)
                        or elimination_compatible(reverse, first, second, eliminated)):
                    if is_convex([points[i] for i in labels]):
                        convex_count += 1
                    else:
                        bad_count += 1
            assert (convex_count, bad_count) == expected[kind][name]
    return type_counts, len(seam_loads), max(seam_loads.values())


def subset_counts(family: list[int], n: int) -> list[int]:
    values = [0] * (1 << n)
    for mask in family:
        values[mask] = 1
    for bit in range(n):
        for mask in range(1 << n):
            if mask >> bit & 1:
                values[mask] += values[mask ^ (1 << bit)]
    return values


def audit_partition_minimal_padding() -> tuple[int, int, int, int]:
    q = sorted(rt.pascal_cell(4, 2, Fraction(1, 97)))
    wrapper = sorted(rt.strong_glue(q, q, Fraction(1, 16384)))
    # First-row witness: A=(0,1), y=2, B=(6,7), z=9.
    carrier = [wrapper[i] for i in (0, 1, 2, 9, 6, 7)]
    padding = [
        (Fraction(89, 11), Fraction(-173, 11)),
        (Fraction(-116, 11), Fraction(49, 11)),
    ]
    points = sorted(carrier + padding)
    assert all(rt.determinant(points[i], points[j], points[k]) != 0
               for i, j, k in itertools.combinations(range(8), 3))
    faces, caps, cups = families(points)
    assert (len(caps), len(cups), len(faces)) == (77, 71, 121)

    # In sorted padded coordinates the two circuits are A=(1,2), y=3,
    # B=(4,5), z=6.
    assert not is_convex([points[i] for i in (1, 2, 3, 6)])
    assert not is_convex([points[i] for i in (3, 4, 5, 6)])
    assert is_convex([points[i] for i in (1, 2, 4, 5)])
    assert all(is_convex([points[i] for i in (a, 3, 6, b)])
               for a in (1, 2) for b in (4, 5))

    face_sub = subset_counts(faces, 8)
    cap_sub = subset_counts(caps, 8)
    cup_sub = subset_counts(cups, 8)
    full = (1 << 8) - 1
    mutations = [
        face_sub[red] + face_sub[full ^ red]
        + cap_sub[red] * cup_sub[full ^ red]
        for red in range(1 << 8)
    ]
    assert min(mutations) == len(faces) == 121
    z = 6
    blue = full ^ (1 << z)
    z_left = 1 + face_sub[blue] + cup_sub[blue]
    z_right = 1 + face_sub[blue] + cap_sub[blue]
    assert (z_left, z_right) == (123, 132)
    return len(faces), min(mutations), z_left, z_right


def main() -> None:
    type_counts, seams, seam_load = audit_pascal_and_elimination()
    value, mutation_min, z_left, z_right = audit_partition_minimal_padding()
    print(
        "PASS: sign types=%s; Pascal bad=3600 seams=%d maxload=%d pairload=1; "
        "padding V/min=%d/%d z-mutations=%d/%d"
        % (dict(type_counts), seams, seam_load,
           value, mutation_min, z_left, z_right)
    )


if __name__ == "__main__":
    main()
