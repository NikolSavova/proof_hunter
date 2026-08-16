#!/usr/bin/env python3
"""Deterministic exact verification of the planar-Tutte barriers."""

from __future__ import annotations

import json
import math
from pathlib import Path

from expected_rank_collision import half_weight_numerator, invariants
from link_half_weight_probe import closure_size, is_convex_face, is_general_position


HERE = Path(__file__).resolve().parent


def add_poly(out, coefficient, shift, power):
    for j in range(power + 1):
        out[shift + j] += coefficient * math.comb(power, j)


def verify_collision():
    cert = json.loads((HERE / "expected_rank_collision_certificate.json").read_text())
    n = cert["n"]
    recovered = []
    for key in ("first", "second"):
        item = cert[key]
        points = [tuple(p) for p in item["coordinates"]]
        assert len(points) == n and is_general_position(points)
        profile, er, table = invariants(points)
        assert list(profile) == item["convex_profile"]
        assert [list(row) for row in table] == item["X_hull_vertices_by_interior_points"]
        assert list(er) == cert["expected_rank_coefficients"]
        assert sum(profile) == item["V"]
        assert half_weight_numerator(profile) == item["two_to_n_times_Z_half"]

        # Exact Boolean-interval / weighted-polygon identity.
        lhs = [0] * (n + 1)
        for hull_vertices, row in enumerate(table):
            for interior_points, count in enumerate(row):
                if count:
                    add_poly(lhs, count, hull_vertices, interior_points)
        assert lhs == [math.comb(n, j) for j in range(n + 1)]
        recovered.append((profile, er))

    first, second = cert["first"], cert["second"]
    assert first["V"] == second["V"] == 133
    assert recovered[0][1] == recovered[1][1]
    assert recovered[0][0] != recovered[1][0]
    assert first["two_to_n_times_Z_half"] == 5444
    assert second["two_to_n_times_Z_half"] == 5448

    er = cert["expected_rank_coefficients"]
    assert er[1] == er[n] == 4
    assert all(er[j] == -er[n + 1 - j] for j in range(2, n))


def verify_link_counterfamily():
    # T is an empty triangle.  Every other point lies in the opposite cone at
    # (0,0), so adding any one of them hides (0,0).  Thus link(T)={empty}.
    points = [(0, 0), (1000, 0), (0, 1000)] + [(-t, -t * t) for t in range(1, 18)]
    assert len(points) == 20 and is_general_position(points)
    triangle = 0b111
    assert is_convex_face(points, triangle)
    assert closure_size(points, triangle) == 3
    for i in range(3, len(points)):
        assert not is_convex_face(points, triangle | (1 << i))

    # Heredity now gives Z_link(1)=Z_link(1/2)=1.  Both the uncorrected link
    # strengthening and its closure-corrected repair fail:
    #   (n-|cl T|) * 1 = 17 > 2^(|T|+1) * 1 = 16.
    assert len(points) - closure_size(points, triangle) == 17 > 2 ** (3 + 1)


def main():
    verify_collision()
    verify_link_counterfamily()
    print("planar Tutte barriers: PASS")
    print("same ER(p), same V=133, but 2^8 Z(1/2)=5444 versus 5448")
    print("closure-corrected all-links HW2 fails exactly: 17 > 16")


if __name__ == "__main__":
    main()
