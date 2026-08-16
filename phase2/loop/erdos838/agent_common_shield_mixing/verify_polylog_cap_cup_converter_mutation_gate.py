#!/usr/bin/env python3
"""Exact verifier for POLYLOG_CAP_CUP_CONVERTER_MUTATION_GATE.md."""

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


def is_convex(points: list[Point]) -> bool:
    if len(points) <= 3:
        return True
    pts = sorted(points)

    def half(seq: list[Point]) -> list[Point]:
        out: list[Point] = []
        for p in seq:
            while len(out) >= 2 and rt.determinant(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    return len(half(pts)[:-1] + half(list(reversed(pts)))[:-1]) == len(pts)


def is_chain(points: list[Point], sign: int) -> bool:
    pts = sorted(points)
    return all(
        (rt.determinant(pts[i], pts[j], pts[k]) > 0) == (sign > 0)
        for i, j, k in itertools.combinations(range(len(pts)), 3)
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


def subset_counts(family: list[int], n: int) -> list[int]:
    counts = [0] * (1 << n)
    for ambient in range(1 << n):
        counts[ambient] = sum(mask & ~ambient == 0 for mask in family)
    return counts


def main() -> None:
    q = sorted(rt.pascal_cell(4, 2, Fraction(1, 97)))
    p = sorted(rt.strong_glue(q, q, Fraction(1, 16384)))
    assert rt.evaluate(q)[:3] == (31, 31, 50)
    assert rt.evaluate(p)[:3] == (248, 248, 1061)

    faces, caps, cups = families(p)
    assert (len(caps), len(cups), len(faces)) == (248, 248, 1061)

    # Exact quadratic all-pairs load lower bound.
    assert len(caps) * len(cups) * 3 >= (len(q) + 2) ** 2 * len(faces)
    load_ratio = Fraction(len(caps) * len(cups), len(faces))

    n = len(p)
    full = (1 << n) - 1
    face_counts = subset_counts(faces, n)
    cap_counts = subset_counts(caps, n)
    cup_counts = subset_counts(cups, n)

    mutations: list[int] = []
    for red in range(1 << n):
        blue = full ^ red
        mutations.append(
            face_counts[red]
            + face_counts[blue]
            + cap_counts[red] * cup_counts[blue]
        )
    assert min(mutations) == 688
    assert sum(value < len(faces) for value in mutations) == 2249

    face_gibbs = sum(
        Fraction(2, 1 << mask.bit_count()) for mask in faces
    )
    cross_gibbs = sum(
        Fraction(1, 1 << (a.bit_count() + b.bit_count()))
        for a in caps
        for b in cups
        if a & b == 0
    )
    average_mutation = Fraction(sum(mutations), 1 << n)
    assert face_gibbs == Fraction(669, 4)
    assert cross_gibbs == Fraction(61057, 64)
    assert average_mutation == face_gibbs + cross_gibbs
    assert average_mutation == Fraction(71761, 64)
    assert cross_gibbs >= Fraction(len(faces) - n, 2)

    # Direct all-delete/common-triple audit on the two six-point children.
    q_faces, q_caps, q_cups = families(q)
    noncaps = [mask for mask in q_faces if mask not in set(q_caps)]
    noncups = [mask for mask in q_faces if mask not in set(q_cups)]
    assert len(noncaps) == len(noncups) == 19

    spanning_caps = [
        cap | (1 << (6 + z)) for cap in q_caps for z in range(6)
    ]
    spanning_cups = [
        (1 << y) | (cup << 6) for y in range(6) for cup in q_cups
    ]
    good_spanning = 0
    spanning_outputs: dict[int, int] = {}
    for cap in spanning_caps:
        for cup in spanning_cups:
            union = cap | cup
            if is_convex([p[i] for i in range(12) if union >> i & 1]):
                good_spanning += 1
                spanning_outputs[union] = spanning_outputs.get(union, 0) + 1
    assert (len(spanning_caps), len(spanning_cups)) == (186, 186)
    assert good_spanning == 15876
    cap_extension_mass = 2 * sum(mask.bit_count() for mask in q_caps) - 6
    cup_extension_mass = 2 * sum(mask.bit_count() for mask in q_cups) - 6
    assert cap_extension_mass == cup_extension_mass == 126
    assert good_spanning == cap_extension_mass * cup_extension_mass
    assert len(spanning_outputs) == 31 * 31
    assert max(spanning_outputs.values()) == 36

    delete_checks = 0
    for dmask in noncaps:
        d_indices = [i for i in range(6) if dmask >> i & 1]
        witness = next(
            triple
            for triple in itertools.combinations(d_indices, 3)
            if rt.determinant(q[triple[0]], q[triple[1]], q[triple[2]]) > 0
        )
        for z in range(6, 12):
            assert not is_convex([p[i] for i in witness] + [p[z]])
        for hmask in noncups:
            hpoints = [p[6 + i] for i in range(6) if hmask >> i & 1]
            sub = dmask
            while sub:
                union = [p[i] for i in range(6) if sub >> i & 1] + hpoints
                assert not is_convex(union)
                delete_checks += 1
                sub = (sub - 1) & dmask

    print(
        "PASS: P12 (C,U,W)=(248,248,1061), all-pair ratio=%s; "
        "mutations min=688 smaller=2249 average=%s; Gibbs=(%s,%s); "
        "spanning good/output/load=%d/%d/%d; all-delete checks=%d"
        % (
            load_ratio,
            average_mutation,
            face_gibbs,
            cross_gibbs,
            good_spanning,
            len(spanning_outputs),
            max(spanning_outputs.values()),
            delete_checks,
        )
    )


if __name__ == "__main__":
    main()
