#!/usr/bin/env python3
"""Exact/small verification for the multiscale short-span report."""

from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


def orient(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    pts = sorted(points)
    if len(pts) <= 1:
        return pts
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
    return lower[:-1] + upper[:-1]


def deep_endpoint_counterfamily(max_m: int = 12) -> list[dict[str, int | str]]:
    rows: list[dict[str, int | str]] = []
    for m in range(1, max_m + 1):
        big = (m + 1) ** 2
        points = [(-1, -big)] + [(a, a * a) for a in range(1, m + 1)] + [
            (m + 1, -big)
        ]
        assert all(orient(*triple) != 0 for triple in itertools.combinations(points, 3))
        left_count = right_count = both_count = total = 0
        both_half = Fraction(0)
        for mask in range(1 << (m + 2)):
            chosen = [points[i] for i in range(m + 2) if mask >> i & 1]
            convex = len(chosen) <= 2 or len(hull(chosen)) == len(chosen)
            if not convex:
                continue
            total += 1
            has_left = bool(mask & 1)
            has_right = bool(mask >> (m + 1) & 1)
            left_count += has_left
            right_count += has_right
            both_count += has_left and has_right
            if has_left and has_right:
                both_half += Fraction(1, 2) ** len(chosen)
        a_count = 1 + m + math.comb(m, 2)
        assert left_count == right_count == 2 * a_count
        assert both_count == a_count
        assert total == 2**m + 3 * a_count
        expected_half = Fraction(1, 4) * (
            1 + Fraction(m, 2) + Fraction(math.comb(m, 2), 4)
        )
        assert both_half == expected_half
        rows.append(
            {
                "M": m,
                "A": a_count,
                "V": total,
                "L": left_count,
                "R": right_count,
                "E": left_count + right_count - both_count,
                "F_half": str(both_half),
            }
        )
    return rows


FI2_PERMUTATIONS = {
    16: [0, 3, 4, 5, 6, 7, 8, 9, 10, 2, 1, 12, 13, 14, 15, 11],
    20: [18, 0, 19, 3, 10, 17, 16, 9, 15, 8, 14, 7, 13, 5, 12, 4, 11, 2, 1, 6],
    24: [19, 23, 22, 21, 20, 3, 9, 18, 17, 8, 16, 15, 7, 14, 6, 13, 5, 11, 12, 10, 2, 1, 0, 4],
}


def fi2_root_score(permutation: list[int], scale: int = 10**6) -> dict[str, int | str | float]:
    """Exact reverse-product endpoint and total counts for an integral set."""
    n = len(permutation)
    points = [(i, scale * permutation[i] + i * i) for i in range(n)]
    assert all(orient(*triple) != 0 for triple in itertools.combinations(points, 3))
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            slope = Fraction(points[j][1] - points[i][1], j - i)
            edges.append((slope, i, j))
    edges.sort()

    def matrix(z: Fraction, reverse: bool = False) -> list[list[Fraction]]:
        mat = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
        ordered = reversed(edges) if reverse else edges
        for _, i, j in ordered:
            old = mat[j][:]
            mat[j] = [old[k] + z * mat[i][k] for k in range(n)]
        return mat

    a_one = matrix(Fraction(1))
    b_one = matrix(Fraction(1), True)
    a_half = matrix(Fraction(1, 2))
    b_half = matrix(Fraction(1, 2), True)
    v = 1 + n + sum(
        a_one[j][i] * b_one[j][i]
        for i in range(n)
        for j in range(i + 1, n)
    )
    f_half = a_half[n - 1][0] * b_half[n - 1][0]
    score = Fraction(n * n) * f_half / v
    return {
        "n": n,
        "scale": scale,
        "V": int(v),
        "F_half": str(f_half),
        "n2_F_half_over_V": str(score),
        "n2_F_half_over_V_float": float(score),
    }


def fi2_finite_certificates() -> list[dict[str, int | str | float]]:
    rows = [fi2_root_score(FI2_PERMUTATIONS[n]) for n in sorted(FI2_PERMUTATIONS)]
    assert rows[0]["n2_F_half_over_V_float"] > 1.5
    assert rows[-1]["n2_F_half_over_V_float"] > 1.9
    return rows


def is_downset(family: set[int]) -> bool:
    for face in family:
        sub = face
        while True:
            if sub not in family:
                return False
            if sub == 0:
                break
            sub = (sub - 1) & face
    return True


def exact_endpoints(face: int, n: int) -> tuple[int, int] | None:
    pts = [i for i in range(n) if face >> i & 1]
    if len(pts) < 2:
        return None
    return pts[0], pts[-1]


def marker_incidence_audit(n: int, family: set[int]) -> dict[str, int]:
    """Use a safe E: faces in I retaining its left or right marker.

    This is at least as transparent as the polynomial convention and proves
    the fixed-span incidence statement directly.
    """
    v = len(family)
    worst_sum = 0
    for s in range(2, n + 1):
        total_e = 0
        for i in range(n - s + 1):
            j = i + s - 1
            mask_i = ((1 << s) - 1) << i
            for face in family:
                if face == 0 or face & ~mask_i:
                    continue
                if (face >> i & 1) or (face >> j & 1):
                    total_e += 1
        # Each nonempty face has at most one left-marker and one right-marker
        # occurrence at a fixed interval length.
        assert total_e <= 2 * (v - 1)
        worst_sum = max(worst_sum, total_e)
    return {"V": v, "worst_fixed_span_E_sum": worst_sum}


def exhaustive_downsets(max_n: int = 4) -> dict[str, int]:
    checked = 0
    worst_slack = 10**9
    for n in range(1, max_n + 1):
        all_faces = 1 << n
        # Families themselves are masks on the Boolean lattice.  Force empty.
        for fam_mask in range(1 << all_faces):
            if not (fam_mask & 1):
                continue
            family = {f for f in range(all_faces) if fam_mask >> f & 1}
            if not is_downset(family):
                continue
            row = marker_incidence_audit(n, family)
            worst_slack = min(
                worst_slack,
                2 * (row["V"] - 1) - row["worst_fixed_span_E_sum"],
            )
            checked += 1
    return {"downsets_checked": checked, "minimum_incidence_slack": worst_slack}


def windows(n: int, m: int) -> list[tuple[int, int, int]]:
    out = []
    # q can start one block before [0,n), to cover its left boundary.
    for q in range(-1, (n + m - 1) // m + 1):
        lo = max(0, q * m)
        hi = min(n, (q + 2) * m)
        if lo < hi:
            out.append((q, lo, hi))
    return out


def dyadic_window_audit(max_n: int = 40) -> dict[str, int]:
    intervals_checked = 0
    for n in range(2, max_n + 1):
        for m in range(1, n + 1):
            ws = windows(n, m)
            for parity in (0, 1):
                same = [(lo, hi) for q, lo, hi in ws if q % 2 == parity]
                for (lo1, hi1), (lo2, hi2) in itertools.combinations(same, 2):
                    assert hi1 <= lo2 or hi2 <= lo1
            for lo in range(n):
                for hi in range(lo + 1, min(n, lo + m) + 1):
                    assert any(a <= lo and hi <= b for _, a, b in ws)
                    intervals_checked += 1
    return {"intervals_checked": intervals_checked}


def delta(c: Fraction, a: Fraction) -> float:
    if c <= a - 1:
        return math.sqrt(float(c * (a - 1)))
    return float(a - 1)


def exponent_table() -> list[dict[str, float | str]]:
    c = Fraction(1, 4)
    ans = []
    for a in (Fraction(3, 2), Fraction(5, 3), Fraction(2, 1), Fraction(3, 1)):
        d = delta(c, a)
        ans.append(
            {
                "a": str(a),
                "delta": d,
                "H_exponent": 1 - d,
                "one_pass_count_coefficient": d / 2,
                "bootstrap_fixed_point": float((a - 1) / 4),
                "perfect_rotation_H_exponent": 2 - float(a),
            }
        )
    return ans


def grid_optimum(c: float, a: float) -> dict[str, float]:
    best = (-1.0, 0.0)
    for q in range(1, 200001):
        theta = q / 200000
        value = min(theta * (a - 1), c / theta)
        if value > best[0]:
            best = (value, theta)
    exact = math.sqrt(c * (a - 1)) if c <= a - 1 else a - 1
    assert abs(best[0] - exact) < 1e-5
    return {"grid_delta": best[0], "grid_theta": best[1], "closed_delta": exact}


def smooth_jump_audit(c: float = 0.25) -> list[dict[str, float]]:
    rows = []
    for n in (100, 1000, 10000, 1000000):
        g_n = c * math.log2(n) ** 2
        g_prev = c * math.log2(n - 1) ** 2
        # Base-two increment times n ln(2) / log_2 n tends to 2c.
        normalized = (g_n - g_prev) * n * math.log(2) / math.log2(n)
        rows.append({"n": n, "normalized_increment": normalized})
    assert abs(rows[-1]["normalized_increment"] - 2 * c) < 1e-5
    return rows


def main() -> None:
    result = {
        "deep_endpoint_counterfamily": deep_endpoint_counterfamily(),
        "fi2_finite_certificates": fi2_finite_certificates(),
        "marker_incidence": exhaustive_downsets(),
        "two_grid_cover": dyadic_window_audit(),
        "exponents": exponent_table(),
        "optimizer_5_over_3": grid_optimum(0.25, 5 / 3),
        "smooth_jump": smooth_jump_audit(),
    }
    out = Path(__file__).with_name("certificate.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
