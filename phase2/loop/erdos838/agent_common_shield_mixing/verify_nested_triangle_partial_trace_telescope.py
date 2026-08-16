#!/usr/bin/env python3
"""Exact checks for NESTED_TRIANGLE_PARTIAL_TRACE_TELESCOPE.md."""

from fractions import Fraction
from itertools import combinations
from math import comb, log2
from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
SHIELD = HERE.parent / "agent_shield_circuit_cover"
mod = runpy.run_path(
    str(SHIELD / "verify_first_incoherent_sibling_nested_triangle_barrier.py")
)
convex_position = mod["convex_position"]
in_general_position = mod["in_general_position"]
nested_triangles = mod["nested_triangles"]


CENTRAL = [(-3, -2), (3, -2), (4, 3), (-2, 4), (0, 1)]


def face_masks(points):
    return {
        mask for mask in range(1 << len(points))
        if convex_position([
            points[i] for i in range(len(points)) if mask >> i & 1
        ])
    }


def check_exact_telescope():
    triangles = nested_triangles(4, CENTRAL)
    points = list(CENTRAL)
    previous_faces = face_masks(points)
    rows = []
    all_outputs = set()

    for t, triangle in enumerate(triangles, 1):
        old_n = len(points)
        traces = [
            tuple(choice)
            for rank in (1, 2)
            for choice in combinations(range(3), rank)
        ]
        incidence = 0
        outputs = set()
        profile = []
        for trace in traces:
            trace_mask = sum(1 << (old_n + i) for i in trace)
            compatible = 0
            for old_mask in previous_faces:
                face = [
                    points[i] for i in range(old_n) if old_mask >> i & 1
                ]
                face += [triangle[i] for i in trace]
                if convex_position(face):
                    compatible += 1
                    output = old_mask | trace_mask
                    assert output not in outputs
                    outputs.add(output)
            profile.append(compatible)
            incidence += compatible

        points.extend(triangle)
        current_faces = face_masks(points)
        full_triangle_mask = sum(1 << (old_n + i) for i in range(3))
        predicted_new = outputs | {full_triangle_mask}
        actual_new = current_faces - previous_faces
        assert actual_new == predicted_new
        assert len(current_faces) == len(previous_faces) + incidence + 1

        # Across layers, the largest triangle label in the output recovers
        # t, and deleting its trace recovers the old face.
        tagged = {(t, output) for output in outputs}
        assert not (tagged & all_outputs)
        all_outputs |= tagged

        old_count = len(previous_faces)
        rho = Fraction(incidence + 1, old_count)
        assert Fraction(len(current_faces), old_count) == 1 + rho
        rows.append((t, old_count, tuple(profile), incidence,
                     len(current_faces), rho))
        previous_faces = current_faces

    telescoped = Fraction(rows[-1][4], len(face_masks(CENTRAL)))
    product_ratio = Fraction(1, 1)
    for row in rows:
        product_ratio *= 1 + row[-1]
    assert telescoped == product_ratio
    return rows, telescoped


def check_low_rank_baseline():
    rows, _ = check_exact_telescope()
    for t, _old_count, profile, _incidence, _new, _rho in rows:
        old_n = len(CENTRAL) + 3 * (t - 1)
        singleton_floor = sum(comb(old_n, rank) for rank in range(3))
        edge_floor = 1 + old_n
        assert all(value >= singleton_floor for value in profile[:3])
        assert all(value >= edge_floor for value in profile[3:])
    return len(rows)


def check_central_zero_profile():
    triangles = nested_triangles(15, CENTRAL)
    # Mask 11 is the central triangle with labels 0,1,3.
    central_face = [CENTRAL[i] for i in (0, 1, 3)]
    assert convex_position(central_face)
    checked = 0
    for triangle in triangles:
        for rank in (1, 2):
            for trace in combinations(triangle, rank):
                assert not convex_position(central_face + list(trace))
                checked += 1
    assert checked == 15 * 6
    return checked


def phi(L, C):
    return L * L / 2 - C * L * log2(L)


def check_fixed_gap_scale():
    C = 3
    rows = []
    for L in (2**10, 2**12, 2**14, 2**16):
        L2 = log2(L)
        L3 = log2(L2)
        # Ambient N=2^L, k~L2, central m=N/(3k).
        lm = L - log2(3 * L2)
        deficit = phi(L, C) - phi(lm, C)
        ratio = deficit / (L * L3)
        assert 0.5 < ratio < 2

        # Even six load-one first-order traces for every one of s=N/3
        # layers give only O(N) copies of the original central bank.
        log_first_order_multiplier = L + log2(2)
        assert log_first_order_multiplier < deficit / 2
        rows.append((L, round(lm, 6), round(ratio, 6),
                     round(deficit / L, 6)))
    return rows


if __name__ == "__main__":
    rows, ratio = check_exact_telescope()
    baseline = check_low_rank_baseline()
    zero = check_central_zero_profile()
    scales = check_fixed_gap_scale()
    print("PASS")
    print("  exact telescope rows:")
    for row in rows:
        print(f"    {row}")
    print(f"  exact final/central ratio: {ratio}")
    print(f"  low-rank baseline layers: {baseline}")
    print(f"  central zero-profile incidences: {zero}")
    print(f"  fixed-gap rows: {scales}")
