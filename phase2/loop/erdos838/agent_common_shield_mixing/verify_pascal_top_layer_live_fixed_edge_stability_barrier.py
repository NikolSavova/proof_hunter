#!/usr/bin/env python3
"""Exact audit for PASCAL_TOP_LAYER_LIVE_FIXED_EDGE_STABILITY_BARRIER.md."""

from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))
sys.path.insert(0, str(ERDOS / "agent_graded_supersat"))

import reflection_trace as rt  # noqa: E402
from graded_balanced import central_template, pascal_row, vertical_iterate  # noqa: E402


Point = tuple[Fraction, Fraction]
Affine = tuple[Fraction, Fraction]  # coefficient of beta, constant term


def affine_add(*terms: Affine) -> Affine:
    return sum((term[0] for term in terms), Fraction(0)), sum(
        (term[1] for term in terms), Fraction(0)
    )


def affine_scale(value: Affine, scalar: Fraction) -> Affine:
    return value[0] * scalar, value[1] * scalar


def formal_coefficient_audit() -> int:
    """Check (7) without numerically approximating beta."""
    cap: list[Affine] = [(Fraction(0), Fraction(0))]
    face: list[Affine] = [(Fraction(0), Fraction(0))]
    for depth in range(1, 33):
        new_cap = affine_add(
            cap[-1],
            (Fraction(1, 2), Fraction(0)),
            (Fraction(0), Fraction(depth - 1, 2)),
        )
        new_face = affine_add(
            affine_scale(cap[-1], Fraction(2)),
            (Fraction(1), Fraction(0)),
            (Fraction(0), Fraction(depth - 1)),
        )
        cap.append(new_cap)
        face.append(new_face)
        assert new_cap == (
            Fraction(depth, 2), Fraction(depth * (depth - 1), 4)
        )
        assert new_face == (
            Fraction(depth), Fraction(depth * (depth - 1), 2)
        )
        normalized = affine_scale(new_face, Fraction(1, depth * depth))
        target = (
            Fraction(1, depth), Fraction(depth - 1, 2 * depth)
        )
        assert normalized == target
        # target = 1/2 + (beta-1/2)/depth.
        assert affine_add(
            (Fraction(0), Fraction(1, 2)),
            (Fraction(1, depth), Fraction(-1, 2 * depth)),
        ) == target
    return 32


def max_rank(profile: list[int]) -> int:
    return max(index for index, value in enumerate(profile) if value)


def graded_pascal_audit() -> tuple[int, int, int]:
    checks = 0
    largest_seed = 0
    largest_iterate = 0
    for k in (4, 5, 6, 8, 10, 12, 16, 20, 24):
        template = central_template(k)
        size, caps, cups, faces = template
        top_rank = 2 * k - 4
        assert size == math.comb(2 * k - 4, k - 2)
        assert max_rank(caps) == max_rank(cups) == k - 1
        assert max_rank(faces) == top_rank
        assert sum(faces) < 32 * faces[top_rank]

        # The top face is literally top-cap(left) x top-cup(right).
        previous_row = pascal_row(2 * k - 5, 2 * k)
        left = previous_row[k - 3]
        right = previous_row[k - 2]
        assert max_rank(left[1]) == max_rank(right[2]) == k - 2
        assert faces[top_rank] == left[1][k - 2] * right[2][k - 2]
        largest_seed = faces[top_rank]
        checks += 1

    # Fixed-depth top-layer concentration, coefficient by coefficient.
    for k in (4, 6, 8, 10, 12):
        template = central_template(k)
        for depth in (1, 2, 3, 4):
            top_rank = depth * (2 * k - 4)
            _, _, _, faces = vertical_iterate(template, depth, top_rank)
            assert max_rank(faces) == top_rank
            assert sum(faces) < 32 * faces[top_rank]
            largest_iterate = faces[top_rank]
            checks += 1
    return checks, largest_seed.bit_length(), largest_iterate.bit_length()


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def exact_live_ledger() -> dict[str, int]:
    """A finite integer instance of (10)--(17), without coordinates."""
    k, depth, pocket_k = 12, 3, 24
    source_template = central_template(k)
    q = depth * (2 * k - 4)
    n_source, caps, cups, faces = vertical_iterate(
        source_template, depth, q
    )
    cap_total = sum(caps)
    face_total = sum(faces)
    top_total = faces[q]

    # Delta = ceil(log_2 log_2 N), calculated with integers.
    delta = 0
    while n_source > 1 << (1 << delta):
        delta += 1
    log_floor = n_source.bit_length() - 1
    rank = log_floor - delta
    assert 2 <= rank <= q

    directed_edges = n_source * (n_source - 1)
    edge_fibre = ceil_div(q * top_total, directed_edges)
    incidence = edge_fibre * math.comb(q - 2, rank - 2)
    maximum_multiplicity = math.comb(n_source - rank, q - rank)
    source_family = ceil_div(incidence, maximum_multiplicity)

    pocket = central_template(pocket_k)
    n_pocket, pocket_caps, pocket_cups, pocket_faces = pocket
    pocket_top_rank = 2 * pocket_k - 4
    pocket_top = pocket_faces[pocket_top_rank]
    pocket_face_total = sum(pocket_faces)
    pocket_cup_total = sum(pocket_cups)
    parent_faces = (
        face_total + pocket_face_total + cap_total * pocket_cup_total
    )

    # This one finite example already clears one L*Delta multiplier.
    target_multiplier = 1 << (log_floor * delta)
    assert source_family * pocket_top > parent_faces * target_multiplier
    assert n_pocket * 1_000 < n_source
    assert (pocket_k - 2) // 3 >= delta
    assert q - rank <= 3 * delta

    return {
        "N_bits": n_source.bit_length(),
        "q": q,
        "r": rank,
        "delta": delta,
        "pocket_rank": pocket_top_rank,
        "matching": (pocket_k - 2) // 3,
        "source_bits": source_family.bit_length(),
        "pocket_bits": pocket_top.bit_length(),
        "parent_bits": parent_faces.bit_length(),
        "surplus_bits_floor": (
            (source_family * pocket_top // parent_faces).bit_length() - 1
        ),
    }


def convex(points: list[Point]) -> bool:
    if len(points) <= 3:
        return True

    def half(sequence: list[Point]) -> list[Point]:
        output: list[Point] = []
        for point in sequence:
            while (
                len(output) >= 2
                and rt.determinant(output[-2], output[-1], point) <= 0
            ):
                output.pop()
            output.append(point)
        return output

    ordered = sorted(points)
    hull = half(ordered)[:-1] + half(list(reversed(ordered)))[:-1]
    return len(hull) == len(points)


def is_cup(points: list[Point]) -> bool:
    ordered = sorted(points)
    return all(
        rt.determinant(ordered[i], ordered[j], ordered[k]) > 0
        for i, j, k in itertools.combinations(range(len(ordered)), 3)
    )


def rational_geometry_audit() -> dict[str, int]:
    epsilon = Fraction(1, 97)
    left = sorted(rt.pascal_cell(4, 2, epsilon))
    right = sorted(rt.pascal_cell(6, 3, epsilon))
    outer_epsilon = Fraction(1, 1 << 100)
    parent = sorted(rt.strong_glue(left, right, outer_epsilon))
    assert len(left) == 6 and len(right) == 20 and len(parent) == 26
    assert parent[:6] == sorted(
        [(outer_epsilon**2 * x, outer_epsilon * y) for x, y in left]
    )

    left_profile = rt.evaluate(left)
    right_profile = rt.evaluate(right)
    parent_profile = rt.evaluate(parent)
    assert left_profile[:3] == (31, 31, 50)
    assert right_profile[:3] == (1281, 1281, 10951)
    assert parent_profile[2] == (
        left_profile[2] + right_profile[2]
        + left_profile[0] * right_profile[1]
    ) == 50712

    # Pigeonhole one literal directed edge and one common interior side.
    edge_candidates = []
    for u, v in itertools.combinations(range(6), 2):
        for sign in (-1, 1):
            sources = [
                (u, v, y)
                for y in range(6)
                if y not in (u, v)
                and (rt.determinant(left[u], left[v], left[y]) > 0)
                == (sign > 0)
            ]
            edge_candidates.append((len(sources), u, v, sign, sources))
    _, u, v, sign, sources = max(edge_candidates)
    assert len(sources) == 4
    assert all(
        (rt.determinant(left[u], left[v], left[y]) > 0) == (sign > 0)
        for _, _, y in sources
    )

    # Enumerate the entire top layer of T(6,3).
    pocket_top = [
        indices
        for indices in itertools.combinations(range(20), 6)
        if convex([right[index] for index in indices])
    ]
    assert len(pocket_top) == central_template(5)[3][6] == 2116
    assert all(not is_cup([right[index] for index in face]) for face in pocket_top)

    crossing_checks = 0
    singleton_trace_checks = 0
    for face in pocket_top:
        witness = next(
            triple
            for triple in itertools.combinations(face, 3)
            if rt.determinant(
                right[triple[0]], right[triple[1]], right[triple[2]]
            ) < 0
        )
        parent_face = tuple(6 + index for index in face)
        parent_witness = tuple(6 + index for index in witness)
        for source in sources:
            assert convex([parent[index] for index in source])
            assert not convex(
                [parent[index] for index in source + parent_face]
            )
            crossing_checks += 1
            for source_label in source:
                circuit = (source_label,) + parent_witness
                assert not convex([parent[index] for index in circuit])
                singleton_trace_checks += 1

    # Exhaust the trace clutter of one pair and see every source singleton.
    source = sources[0]
    face = pocket_top[0]
    union = source + tuple(6 + index for index in face)
    traces: set[frozenset[int]] = set()
    for four_set in itertools.combinations(union, 4):
        if not convex([parent[index] for index in four_set]):
            trace = frozenset(set(four_set) & set(source))
            assert trace
            traces.add(trace)
    assert all(frozenset((label,)) in traces for label in source)

    return {
        "sources": len(sources),
        "pocket_top": len(pocket_top),
        "crossing": crossing_checks,
        "singleton_traces": singleton_trace_checks,
        "trace_edges": len(traces),
        "parent_faces": parent_profile[2],
    }


def main() -> None:
    formal = formal_coefficient_audit()
    graded = graded_pascal_audit()
    ledger = exact_live_ledger()
    geometry = rational_geometry_audit()
    print(
        "PASS: Pascal top-layer live fixed-edge stability barrier; "
        f"formal={formal}; graded={graded}; ledger={ledger}; geometry={geometry}"
    )


if __name__ == "__main__":
    main()
