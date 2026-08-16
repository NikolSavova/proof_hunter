#!/usr/bin/env python3
"""Direct-hull deletion-path probes on standard planar families (n <= 16)."""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path[:0] = [
    str(ROOT / "agent_planar_lattice_mean"),
    str(ROOT / "agent_graded_supersat"),
    str(ROOT / "agent_upper_multitype"),
]

from planar_lattice_mean import is_convex  # noqa: E402
from mean_size_probe import dyadic_horton  # noqa: E402
from nested_cage_search import nested_triangles  # noqa: E402


def direct_path(points: list[tuple[object, object]]) -> dict[str, float | int]:
    n = len(points)
    count = 1 << n
    z1 = [0] * count
    zh = [0] * count  # 2^n Z(1/2)
    m1 = [0] * count
    mh = [0] * count
    for mask in range(count):
        face = [i for i in range(n) if mask >> i & 1]
        if is_convex(points, face):
            k = len(face)
            z1[mask] = 1
            zh[mask] = 1 << (n - k)
            m1[mask] = k
            mh[mask] = k << (n - k)
    for i in range(n):
        bit = 1 << i
        for mask in range(count):
            if mask & bit:
                child = mask ^ bit
                z1[mask] += z1[child]
                zh[mask] += zh[child]
                m1[mask] += m1[child]
                mh[mask] += mh[child]
    mean_r = [0.0] * count
    mean_kl = [0.0] * count
    min_r = [0.0] * count
    for mask in range(1, count):
        size = mask.bit_count()
        mu1 = Fraction(m1[mask], z1[mask])
        muh = Fraction(mh[mask], zh[mask])
        local_r = math.log(float((size - muh) / (size - mu1)))
        s1 = sh = 0
        children = []
        bits = mask
        while bits:
            bit = bits & -bits
            child = mask ^ bit
            children.append(child)
            s1 += z1[child]
            sh += zh[child]
            bits -= bit
        er = ek = d = 0.0
        best = math.inf
        for child in children:
            q1 = z1[child] / s1
            qh = zh[child] / sh
            er += qh * mean_r[child]
            ek += qh * mean_kl[child]
            d += qh * math.log(qh / q1)
            best = min(best, min_r[child])
        mean_r[mask] = local_r + er
        mean_kl[mask] = d + ek
        min_r[mask] = local_r + best
    full = count - 1
    L = math.log(z1[full] / (zh[full] / (1 << n)))
    if abs(mean_r[full] + mean_kl[full] - L) > 3e-11:
        raise AssertionError("path decomposition")
    return {
        "n": n,
        "V": z1[full],
        "L": L,
        "path_integrated_variance": mean_r[full],
        "path_KL": mean_kl[full],
        "minimum_path_sum": min_r[full],
        "target_log_n_over_2": math.log(n / 2),
        "expected_path_slack": mean_r[full] - math.log(n / 2),
    }


def generic_x(points: list[tuple[Fraction, Fraction]]) -> list[tuple[Fraction, Fraction]]:
    for shear in range(1, 1000):
        result = sorted((x + shear * y, y) for x, y in points)
        if len({x for x, _ in result}) == len(result):
            return result
    raise AssertionError("no generic shear")


def main() -> None:
    cases: dict[str, list[tuple[object, object]]] = {}
    for level in (2, 3, 4):
        cases[f"dyadic_horton_n{1 << level}"] = dyadic_horton(level)
    for depth in (2, 3, 4, 5):
        cages = nested_triangles(depth, 838 + 1000 * depth)
        cases[f"nested_triangles_n{3 * depth}"] = generic_x(
            [point for cage in cages for point in cage]
        )
    cases["parabola_n16"] = [(i, i * i) for i in range(16)]
    rows = {name: direct_path(points) for name, points in cases.items()}
    for name, row in rows.items():
        if row["expected_path_slack"] < -3e-11:
            raise AssertionError((name, row))
        print(
            name,
            f"R={row['path_integrated_variance']:.12f}",
            f"target={row['target_log_n_over_2']:.12f}",
            f"minPath={row['minimum_path_sum']:.12f}",
        )
    output = {
        "mode": "direct_hull_family_path_probe",
        "scope": "exact face decisions and integer zeta transforms; floating logs only",
        "cases": rows,
        "parabola_all_n_formula": {
            "local_r": "log(4/3)",
            "path_integrated_variance": "n log(4/3)",
            "path_KL": 0,
        },
    }
    path = HERE / "family_certificate.json"
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
