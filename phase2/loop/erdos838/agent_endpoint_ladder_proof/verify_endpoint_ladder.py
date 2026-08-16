#!/usr/bin/env python3
"""Exact audit for the two-deep-endpoint obstruction.

The script uses only integer coordinates, integer determinants, and
``fractions.Fraction``.  It independently checks the endpoint path
polynomials by dynamic programming and, for the smaller instances, checks
the entire convex-subset profile by brute-force hull enumeration.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent


def orient(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def points(middle: int) -> list[tuple[int, int]]:
    """Return l,q_1,...,q_M,r in increasing x-order."""
    B = (middle + 2) ** 3
    return ([(-1, -B)]
            + [(a, a * a) for a in range(1, middle + 1)]
            + [(middle + 1, -B)])


def add_poly(a: list[int], b: list[int]) -> list[int]:
    ans = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        ans[i] += value
    for i, value in enumerate(b):
        ans[i] += value
    while len(ans) > 1 and ans[-1] == 0:
        ans.pop()
    return ans


def endpoint_path_poly(
    pts: list[tuple[int, int]], left: int, right: int, sign: int
) -> list[int]:
    """Count sign-monotone paths, with z to the number of path edges."""
    edge: dict[tuple[int, int], list[int]] = {}
    for j in range(left + 1, right + 1):
        edge[left, j] = [0, 1]
    for i in range(left + 1, right):
        for j in range(i + 1, right + 1):
            poly = [0]
            for h in range(left, i):
                if ((h, i) in edge
                        and (orient(pts[h], pts[i], pts[j]) > 0) == (sign > 0)):
                    poly = add_poly(poly, [0] + edge[h, i])
            if any(poly):
                edge[i, j] = poly
    ans = [0]
    for i in range(left, right):
        if (i, right) in edge:
            ans = add_poly(ans, edge[i, right])
    return ans


def mul_poly(a: list[int], b: list[int]) -> list[int]:
    ans = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            ans[i + j] += x * y
    return ans


def poly_value(poly: list[int], z: Fraction) -> Fraction:
    return sum((Fraction(a) * z**k for k, a in enumerate(poly)), Fraction())


def hull_size(pts: list[tuple[int, int]]) -> int:
    if len(pts) <= 1:
        return len(pts)
    pts = sorted(pts)
    lower: list[tuple[int, int]] = []
    for p in pts:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper: list[tuple[int, int]] = []
    for p in reversed(pts):
        while len(upper) >= 2 and orient(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return len(lower) + len(upper) - 2


def brute_profile(pts: list[tuple[int, int]]) -> list[int]:
    n = len(pts)
    profile = [0] * (n + 1)
    for mask in range(1 << n):
        chosen = [pts[i] for i in range(n) if (mask >> i) & 1]
        if len(chosen) <= 3 or hull_size(chosen) == len(chosen):
            profile[len(chosen)] += 1
    return profile


def expected_profile(M: int) -> list[int]:
    n = M + 2
    answer = [0] * (n + 1)
    for k in range(n + 1):
        # Choose t of the two deep endpoints.  If t>0, at most two of the
        # middle parabola points may be retained.
        for t in range(3):
            q = k - t
            if 0 <= q <= M and (t == 0 or q <= 2):
                answer[k] += math.comb(2, t) * math.comb(M, q)
    return answer


def exact_record(M: int) -> dict[str, object]:
    pts = points(M)
    n = M + 2
    B = (M + 2) ** 3

    # Exhaust all orientations and check the four formulas used in the proof.
    for i, j, k in combinations(range(n), 3):
        assert orient(pts[i], pts[j], pts[k]) != 0
    for a, b in combinations(range(1, M + 1), 2):
        qa, qb = pts[a], pts[b]
        assert orient(pts[0], qa, qb) == (b - a) * (a * b + a + b - B) < 0
        assert orient(qa, qb, pts[-1]) < 0
    for a in range(1, M + 1):
        assert orient(pts[0], pts[a], pts[-1]) == -(M + 2) * (a * a + B) < 0
    for a, b, c in combinations(range(1, M + 1), 3):
        assert orient(pts[a], pts[b], pts[c]) == (b-a) * (c-b) * (c-a) > 0

    cup = endpoint_path_poly(pts, 0, n - 1, +1)
    cap = endpoint_path_poly(pts, 0, n - 1, -1)
    endpoint = mul_poly(cup, cap)
    expected_endpoint = [0, 0, 1, M, math.comb(M, 2)]
    assert cup == [0, 1]
    assert cap == [0, 1, M, math.comb(M, 2)]
    assert endpoint == expected_endpoint

    A = 1 + M + math.comb(M, 2)
    L = R = 2 * A
    E = 3 * A
    F_half = poly_value(endpoint, Fraction(1, 2))
    assert F_half == Fraction(M * M + 3 * M + 8, 32)
    Z_one = 2**M + 3 * A

    # Independently sum all exact-left and exact-right endpoint products.
    left_mass = 1
    right_mass = 1
    for b in range(1, n):
        left_mass += sum(mul_poly(endpoint_path_poly(pts, 0, b, +1),
                                  endpoint_path_poly(pts, 0, b, -1)))
    for a in range(n - 1):
        right_mass += sum(mul_poly(endpoint_path_poly(pts, a, n - 1, +1),
                                   endpoint_path_poly(pts, a, n - 1, -1)))
    assert left_mass == L
    assert right_mass == R

    brute = None
    if M <= 10:
        brute = brute_profile(pts)
        assert brute == expected_profile(M)
        assert sum(brute) == Z_one

    return {
        "middle_points": M,
        "total_points_and_span": n,
        "B": B,
        "coordinates": pts,
        "root_cup_polynomial": cup,
        "root_cap_polynomial": cap,
        "root_product_polynomial": endpoint,
        "F_root_at_half": str(F_half),
        "Z_interval_at_one": Z_one,
        "left_marker_mass": L,
        "right_marker_mass": R,
        "either_marker_mass": E,
        "Fhalf_over_one_marker": str(F_half / L),
        "Fhalf_over_either_marker": str(F_half / E),
        "span2_full_ratio": float(Fraction(n * n) * F_half / Z_one),
        "span_3_over_2_one_marker_ratio": float(
            (n ** Fraction(3, 2)) * F_half / L
        ),
        "span_5_over_3_either_marker_ratio": float(
            (n ** Fraction(5, 3)) * F_half / E
        ),
        "brute_profile": brute,
    }


def main() -> None:
    records = [exact_record(M) for M in range(2, 13)]
    certificate = {
        "description": "exact two-deep-endpoint obstruction to marker localization",
        "limiting_ratios": {
            "Fhalf_over_one_marker": "1/32",
            "Fhalf_over_either_marker": "1/48",
            "consequence": "every positive span power against L/R/E is impossible",
        },
        "records": records,
    }
    target = HERE / "certificate.json"
    target.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps(certificate, indent=2))


if __name__ == "__main__":
    main()
