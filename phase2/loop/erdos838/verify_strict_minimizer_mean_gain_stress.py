#!/usr/bin/env python3
"""Exact stress checks for the strict minimizer mean-gain route.

The expensive rows enumerate every convex face of the certified 44- and
58-point configurations from their exact slope orders.  Closure sizes are
then recovered by intersecting precomputed exact half-plane masks.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
APA = HERE / "agent_apa_rank"
LATTICE = HERE / "agent_planar_lattice_mean"
LEX = HERE / "agent_lex_minimizer_search"
UNIT = HERE / "agent_unit_matrix_asymptotic"
for directory in (APA, LATTICE, UNIT):
    sys.path.insert(0, str(directory))

import verify_apa_counterexample as n44_source  # noqa: E402
import verify_half_weight_counterexample as n58_source  # noqa: E402
from planar_lattice_mean import closure_mask, is_convex  # noqa: E402
from verify_endpoint_span_localization import temporal_paths  # noqa: E402


def summary(n: int, v: int, moment: int, interior: int) -> dict[str, object]:
    mu = Q(moment, v)
    mean_interior = Q(interior, v)
    mean_blocked = Q(n) - mean_interior - 2 * mu
    return {
        "n": n,
        "V": v,
        "moment": moment,
        "interior_total": interior,
        "mu": mu,
        "mean_interior": mean_interior,
        "mean_blocked": mean_blocked,
        "blocked_over_mu_squared": mean_blocked / (mu * mu),
    }


def brute_small(path: Path) -> dict[str, object]:
    record = json.loads(path.read_text())
    points = tuple(tuple(point) for point in record["coordinates_as_stored"])
    n = len(points)
    v = moment = interior = 0
    for mask in range(1 << n):
        face = [label for label in range(n) if (mask >> label) & 1]
        if not is_convex(points, face):
            continue
        v += 1
        moment += len(face)
        interior += closure_mask(points, face).bit_count() - len(face)
    return summary(n, v, moment, interior)


def exact_large(source) -> dict[str, object]:
    points = tuple(sorted(source.points()))
    n = len(points)
    roots = tuple(
        (i, j)
        for _, i, j in sorted(
            (
                (points[j][1] - points[i][1])
                / (points[j][0] - points[i][0]),
                i,
                j,
            )
            for i in range(n)
            for j in range(i + 1, n)
        )
    )
    forward = temporal_paths(n, roots)
    backward = temporal_paths(n, tuple(reversed(roots)))

    all_labels = (1 << n) - 1
    left_masks: dict[tuple[int, int], int] = {}
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            mask = (1 << i) | (1 << j)
            for k in range(n):
                if k not in (i, j) and source.orient(
                    points[i], points[j], points[k]
                ) > 0:
                    mask |= 1 << k
            left_masks[i, j] = mask

    profile = [0] * (n + 1)
    profile[0] = 1
    profile[1] = n
    v = 1 + n
    moment = n
    interior = 0
    for i, j in combinations(range(n), 2):
        for lower in forward[i, j]:
            for upper in backward[i, j]:
                cycle = lower + tuple(reversed(upper[1:-1]))
                rank = len(cycle)
                profile[rank] += 1
                v += 1
                moment += rank
                if rank < 3:
                    continue
                sign = source.orient(
                    points[cycle[0]], points[cycle[1]], points[cycle[2]]
                )
                closed = all_labels
                for first, second in zip(cycle, cycle[1:] + cycle[:1]):
                    closed &= (
                        left_masks[first, second]
                        if sign > 0
                        else left_masks[second, first]
                    )
                face_mask = sum(1 << label for label in cycle)
                assert closed & face_mask == face_mask
                interior += closed.bit_count() - rank

    expected = tuple(source.EXPECTED_PROFILE)
    assert tuple(profile[: len(expected)]) == expected
    assert not any(profile[len(expected) :])
    assert v == sum(expected)
    return summary(n, v, moment, interior)


def stored_rows() -> list[dict[str, object]]:
    certificate = json.loads(
        (LATTICE / "CERTIFICATE.json").read_text()
    )
    rows = []
    for record in certificate["results"]:
        n = int(record["n"])
        v = int(record["V"])
        moment = int(record["M1"])
        interior = sum(
            int(key.split(",")[1]) * int(value)
            for key, value in record["joint_h_i"].items()
        )
        row = summary(n, v, moment, interior)
        assert row["mu"] == Q(record["mu"])
        assert row["mean_interior"] == Q(record["mean_interior"])
        assert row["mean_blocked"] == Q(record["mean_blocked_exterior"])
        rows.append(row)
    return rows


def main() -> None:
    n8 = brute_small(LEX / "exact_realizable_n8_independent.json")
    n9 = brute_small(LEX / "exact_realizable_n9.json")
    assert (n8["V"], n8["moment"], n8["interior_total"]) == (114, 316, 63)
    assert (n9["V"], n9["moment"], n9["interior_total"]) == (169, 492, 111)

    stored = stored_rows()
    by_n = {row["n"]: row for row in stored}
    assert by_n[17]["interior_total"] == 5765
    assert by_n[20]["interior_total"] == 16325

    n44 = exact_large(n44_source)
    n58 = exact_large(n58_source)
    assert (n44["V"], n44["moment"], n44["interior_total"]) == (
        237229,
        1150674,
        1995795,
    )
    assert (n58["V"], n58["moment"], n58["interior_total"]) == (
        1061907,
        5515707,
        11878530,
    )

    # The minimizer rows survive the proposed strict factor, while the large
    # nonminimizers rigorously kill its universal version.
    assert n8["blocked_over_mu_squared"] < 1
    assert n9["blocked_over_mu_squared"] < 1
    assert by_n[17]["blocked_over_mu_squared"] < 1
    assert by_n[20]["blocked_over_mu_squared"] < 1
    assert n44["blocked_over_mu_squared"] > 1
    assert n58["blocked_over_mu_squared"] > 1

    rows = [n8, n9, by_n[17], by_n[20], n44, n58]
    display = [
        (
            row["n"],
            row["V"],
            f"{float(row['mu']):.6f}",
            f"{float(row['blocked_over_mu_squared']):.6f}",
        )
        for row in rows
    ]
    print(f"PASS: strict minimizer mean stress; rows={display}")


if __name__ == "__main__":
    main()
