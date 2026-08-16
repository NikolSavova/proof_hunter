#!/usr/bin/env python3
"""Exact verifier for the common-core mark-C4 face/circuit dichotomy."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path

import verify_rooted_hull_kraft_reset as kraft


HERE = Path(__file__).resolve().parent
Point = tuple[Fraction, Fraction]


def tangent_point(a_value: int, b_value: int) -> Point:
    assert a_value > b_value
    gap = a_value - b_value
    return (Fraction(a_value, gap), Fraction(-1, gap))


def audit_record(points: list[Point], core: set[int], ear: int, blocker: int) -> None:
    source = core | {ear}
    target = core | {blocker}
    assert kraft.convex(points, source)
    assert kraft.convex(points, target)
    assert not kraft.convex(points, source | {blocker})
    assert kraft.hull_vertices(points, source | {blocker}) == target


def one_rectangle(parameters: list[tuple[int, int]], good: bool) -> dict:
    roots_and_core = [
        (Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0)),
        (Fraction(1, 2), Fraction(1)),
    ]
    points = roots_and_core + [tangent_point(*pair) for pair in parameters]
    assert kraft.general_position(points)
    core = {0, 1, 2}
    x_labels = [3, 4]
    p_labels = [5, 6]
    for ear in x_labels:
        for blocker in p_labels:
            audit_record(points, core, ear, blocker)

    x_face = core | set(x_labels)
    p_face = core | set(p_labels)
    assert kraft.convex(points, x_face) is good
    assert kraft.convex(points, p_face) is good
    if good:
        assert x_face & p_face == core
        assert x_face - p_face == set(x_labels)
        assert p_face - x_face == set(p_labels)
        circuit = None
    else:
        # The first member of each parameter pair is the inner point.
        assert kraft.hull_vertices(points, {0, 1, 3, 4}) == {0, 1, 4}
        assert kraft.hull_vertices(points, {0, 1, 5, 6}) == {0, 1, 6}
        circuit = {"root": [0, 1], "inner": 3, "outer": 4}
    return {
        "kind": "good" if good else "bad",
        "records": 4,
        "common_root_edge": [0, 1],
        "x_pair_convex": kraft.convex(points, x_face),
        "p_pair_convex": kraft.convex(points, p_face),
        "canonical_circuit": circuit,
    }


def tensor_regression() -> dict:
    cap_size = 4
    u = (Fraction(0), Fraction(0))
    v = (Fraction(1), Fraction(0))
    cap = []
    for index in range(1, cap_size + 1):
        parameter = Fraction(index, cap_size + 1)
        cap.append((parameter, parameter * (1 - parameter)))
    # Two nested X marks followed by two nested Y marks.
    # Scalable template A_i=m+1-i, B_i=-A_i^2 at m=4.
    mark_parameters = [(4, -16), (3, -9), (2, -4), (1, -1)]
    marks = [tangent_point(*pair) for pair in mark_parameters]
    points = [u, v, *cap, *marks]
    assert kraft.general_position(points)
    x_labels = [2 + cap_size, 3 + cap_size]
    p_labels = [4 + cap_size, 5 + cap_size]

    cores = []
    records = []
    pair_core_degree = Counter()
    source_projection = set()
    target_projection = set()
    mark_projection = set()
    source_target_faces = set()
    bad_rectangles = 0
    for bits in range(1 << cap_size):
        core = {0, 1} | {
            2 + index for index in range(cap_size) if bits >> index & 1
        }
        assert kraft.convex(points, core)
        cores.append(core)
        for ear in x_labels:
            for blocker in p_labels:
                audit_record(points, core, ear, blocker)
                records.append((bits, ear, blocker))
                source_projection.add((bits, ear))
                target_projection.add((bits, blocker))
                mark_projection.add((ear, blocker))
                pair_core_degree[(ear, blocker)] += 1
                source_target_faces.add(tuple(sorted(core | {ear})))
                source_target_faces.add(tuple(sorted(core | {blocker})))
        assert not kraft.convex(points, core | set(x_labels))
        assert not kraft.convex(points, core | set(p_labels))
        assert kraft.hull_vertices(points, {0, 1, *x_labels}) == {0, 1, x_labels[1]}
        assert kraft.hull_vertices(points, {0, 1, *p_labels}) == {0, 1, p_labels[1]}
        bad_rectangles += 1

    assert len(records) == (1 << cap_size) * len(x_labels) * len(p_labels)
    assert set(pair_core_degree.values()) == {1 << cap_size}
    assert bad_rectangles == 1 << cap_size
    projection_product = (
        len(source_projection) * len(target_projection) * len(mark_projection)
    )
    assert len(records) ** 2 == projection_product

    mark_points = [points[index] for index in x_labels + p_labels]
    detached_mark_faces = sum(
        kraft.convex(
            mark_points,
            {index for index in range(len(mark_points)) if bits >> index & 1},
        )
        for bits in range(1 << len(mark_points))
    )
    assert detached_mark_faces == 1 << len(mark_points)

    total_faces = sum(
        kraft.convex(
            points,
            {index for index in range(len(points)) if bits >> index & 1},
        )
        for bits in range(1 << len(points))
    )
    return {
        "upper_cap_size": cap_size,
        "core_count": len(cores),
        "mark_alphabet_sizes": [len(x_labels), len(p_labels)],
        "actual_record_count": len(records),
        "source_projection_size": len(source_projection),
        "target_projection_size": len(target_projection),
        "mark_projection_size": len(mark_projection),
        "loomis_whitney_left": len(records) ** 2,
        "loomis_whitney_right": projection_product,
        "loomis_whitney_equality": len(records) ** 2 == projection_product,
        "pair_core_degree": next(iter(pair_core_degree.values())),
        "common_core_rectangles": bad_rectangles,
        "good_rectangles": 0,
        "bad_rooted_circuits": bad_rectangles,
        "distinct_source_target_faces": len(source_target_faces),
        "detached_upper_cap_faces": 1 << cap_size,
        "detached_mark_faces": detached_mark_faces,
        "total_convex_subsets": total_faces,
    }


def rectangle_count_identity() -> dict:
    # A synthetic graph checks sum_{p<q} binom(codeg(p,q),2).
    left = range(5)
    right = range(4)
    edges = {
        (x, p)
        for x in left
        for p in right
        if (2 * x + p) % 3 != 0
    }
    direct = 0
    for x_1, x_2 in combinations(left, 2):
        for p_1, p_2 in combinations(right, 2):
            direct += all(
                (x, p) in edges
                for x in (x_1, x_2)
                for p in (p_1, p_2)
            )
    codegree = 0
    for p_1, p_2 in combinations(right, 2):
        common = sum((x, p_1) in edges and (x, p_2) in edges for x in left)
        codegree += common * (common - 1) // 2
    assert direct == codegree
    return {
        "left_vertices": len(left),
        "right_vertices": len(right),
        "edges": len(edges),
        "rectangles": direct,
        "codegree_formula": codegree,
    }


def main() -> None:
    certificate = {
        "description": "common-core mark C4 face-or-rooted-circuit dichotomy",
        "arithmetic": "fractions.Fraction for every geometric assertion",
        "good_rectangle": one_rectangle(
            [(10, -5), (9, -6), (6, -1), (5, -2)], good=True
        ),
        "bad_rectangle": one_rectangle(
            [(12, -8), (10, -5), (6, -2), (4, -1)], good=False
        ),
        "all_bad_tensor": tensor_regression(),
        "rectangle_count_identity": rectangle_count_identity(),
        "assertions": [
            "every repair edge gives the same insertion edge to its ear and blocker",
            "a common-core K2,2 uses one root edge",
            "incomparable same-side pairs give two mixed ordinary faces",
            "a comparable same-side pair gives a canonical rooted 1+3 circuit",
            "the full planar ACP tensor attains equality in discrete Loomis-Whitney",
            "the Boolean-core complete tensor makes every rectangle bad",
            "the explicit tensor exposes both upper-core and detached-mark Boolean shields",
        ],
    }
    output = HERE / "mark_c4_root_circuit_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    tensor = certificate["all_bad_tensor"]
    print(
        "tensor records="
        f"{tensor['actual_record_count']} bad rectangles={tensor['bad_rooted_circuits']}"
    )
    print(
        "detached shields="
        f"{tensor['detached_upper_cap_faces']}x{tensor['detached_mark_faces']} (separate banks)"
    )
    print(f"PASS: wrote {output}")


if __name__ == "__main__":
    main()
