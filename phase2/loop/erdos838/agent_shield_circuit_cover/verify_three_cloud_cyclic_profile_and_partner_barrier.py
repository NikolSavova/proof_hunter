#!/usr/bin/env python3
"""Checks for THREE_CLOUD_CYCLIC_PROFILE_AND_PARTNER_BARRIER.md."""

from itertools import combinations, product
from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
mod = runpy.run_path(
    str(HERE / "verify_first_incoherent_sibling_nested_triangle_barrier.py")
)
convex_position = mod["convex_position"]
convex_hull = mod["convex_hull"]
in_general_position = mod["in_general_position"]
nested_triangles = mod["nested_triangles"]

CENTRAL = [(-3, -2), (3, -2), (4, 3), (-2, 4), (0, 1)]


def check_cyclic_algebra():
    checked = 0
    for A in product((3, 7, 19), repeat=3):
        for R in product((4, 11, 23), repeat=3):
            H = tuple(A[i] * R[i] - (i + 1) for i in range(3))
            B = (R[2] * A[1], R[0] * A[2], R[1] * A[0])
            assert B[0] * B[1] * B[2] == \
                   (A[0] * R[0]) * (A[1] * R[1]) * (A[2] * R[2])
            assert max(B) ** 3 >= H[0] * H[1] * H[2]
            checked += 1

    # Algebraic equality: no multiplier beyond the common H is forced.
    q = 10**6
    A = (q, q, q)
    R = (q, q, q)
    H = (q * q, q * q, q * q)
    B = (R[2] * A[1], R[0] * A[2], R[1] * A[0])
    assert B == H
    return checked


def hidden_point(points):
    hull = set(convex_hull(points))
    missing = [p for p in points if p not in hull]
    assert len(missing) == 1
    return missing[0]


def check_nested_partner_barrier(layers=10):
    triangles = nested_triangles(layers, CENTRAL)
    clouds = [[triangle[c] for triangle in triangles] for c in range(3)]
    all_points = [p for triangle in triangles for p in triangle] + CENTRAL
    assert in_general_position(all_points)

    # Pairwise edge modules are completely good: the obstruction begins at
    # signed 1+3 circuits, not at a hidden 2+2 edge pair.
    edge_pairs = 0
    for a, b in combinations(range(3), 2):
        for i, j in combinations(range(layers), 2):
            for k, ell in combinations(range(layers), 2):
                assert convex_position([
                    clouds[a][i], clouds[a][j],
                    clouds[b][k], clouds[b][ell],
                ])
                edge_pairs += 1

    records = 0
    for a in range(3):
        b, c = [color for color in range(3) if color != a]
        for i, j, k in combinations(range(layers), 3):
            triple = [clouds[a][i], clouds[a][j], clouds[a][k]]
            assert convex_position(triple)
            for t in range(layers):
                with_b = triple + [clouds[b][t]]
                with_c = triple + [clouds[c][t]]
                good_b = convex_position(with_b)
                good_c = convex_position(with_c)
                assert good_b != good_c
                bad = with_c if good_b else with_b
                assert hidden_point(bad) == clouds[a][j]

                # Delete the hidden middle A-label and insert the unused
                # same-layer partner.  The resulting 2+1+1 set is still bad.
                attempted_release = [
                    clouds[a][i], clouds[a][k],
                    clouds[b][t], clouds[c][t],
                ]
                assert not convex_position(attempted_release)
                records += 1

    expected = 3 * (layers * (layers - 1) * (layers - 2) // 6) * layers
    assert records == expected == 3600
    return edge_pairs, records


if __name__ == "__main__":
    algebra = check_cyclic_algebra()
    edge_pairs, records = check_nested_partner_barrier()
    print(
        "PASS: cyclic algebra cases="
        f"{algebra}; good 2+2 edge pairs={edge_pairs}; "
        f"anti-aligned 1+3 records={records}; third-partner repairs=0"
    )
