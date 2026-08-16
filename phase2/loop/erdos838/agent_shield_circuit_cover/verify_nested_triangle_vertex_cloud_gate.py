#!/usr/bin/env python3
"""Exact checks for NESTED_TRIANGLE_VERTEX_CLOUD_FIXED_GAP_GATE.md."""

from itertools import combinations
from math import log2
from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
mod = runpy.run_path(
    str(HERE / "verify_first_incoherent_sibling_nested_triangle_barrier.py")
)
convex_position = mod["convex_position"]
nested_triangles = mod["nested_triangles"]

CENTRAL = [(-3, -2), (3, -2), (4, 3), (-2, 4), (0, 1)]


def masks(points):
    return [
        mask for mask in range(1, 1 << len(points))
        if convex_position([points[i] for i in range(len(points))
                            if mask >> i & 1])
    ]


def check_cloud_telescope(layers=6):
    triangles = nested_triangles(layers, CENTRAL)
    clouds = [[triangle[c] for triangle in triangles] for c in range(3)]
    face_families = [masks(cloud) for cloud in clouds]
    rows = []
    for c, (cloud, faces) in enumerate(zip(clouds, face_families)):
        increments = []
        for t in range(layers):
            count = 0
            for old_mask in range(1 << t):
                trace = [cloud[i] for i in range(t) if old_mask >> i & 1]
                trace.append(cloud[t])
                count += convex_position(trace)
            increments.append(count)
        assert sum(increments) == len(faces)
        rows.append((c, len(faces), tuple(increments)))
    assert rows == [
        (0, 56, (1, 2, 4, 7, 14, 28)),
        (1, 50, (1, 2, 4, 8, 13, 22)),
        (2, 54, (1, 2, 4, 8, 13, 26)),
    ]
    return triangles, clouds, face_families, rows


def has_cross_circuit(points_a, points_b):
    joined = [(p, 0) for p in points_a] + [(p, 1) for p in points_b]
    for choice in combinations(joined, 4):
        if {color for _, color in choice} != {0, 1}:
            continue
        if not convex_position([p for p, _ in choice]):
            return True
    return False


def check_face_rectangle():
    _triangles, clouds, families, rows = check_cloud_telescope()
    good_rows = []
    for i, j in combinations(range(3), 2):
        good = 0
        bad = 0
        outputs = set()
        for mask_i in families[i]:
            face_i = [clouds[i][a] for a in range(len(clouds[i]))
                      if mask_i >> a & 1]
            for mask_j in families[j]:
                face_j = [clouds[j][a] for a in range(len(clouds[j]))
                          if mask_j >> a & 1]
                if convex_position(face_i + face_j):
                    good += 1
                    output = (i, mask_i, j, mask_j)
                    assert output not in outputs
                    outputs.add(output)
                else:
                    bad += 1
                    assert has_cross_circuit(face_i, face_j)
        assert good + bad == len(families[i]) * len(families[j])
        good_rows.append((i, j, good, bad))
    assert good_rows == [
        (0, 1, 1230, 1570),
        (0, 2, 1120, 1904),
        (1, 2, 1036, 1664),
    ]
    return rows, good_rows


def phi(x, C=3):
    return x * x / 2 - C * x * log2(x)


def check_scale():
    a = log2(3)
    rows = []
    for L in (2**10, 2**12, 2**14, 2**16):
        # s=N/3 at leading order; the omitted central N/loglog N term is
        # lower order for this coefficient audit.
        ell = L - a
        deficit = phi(L) - phi(ell)
        assert abs(deficit / L - a) < 0.1
        log_bad_ratio = phi(L) - 2 * phi(ell)
        assert log_bad_ratio < -0.45 * L * L
        rows.append((L, round(deficit / L, 6),
                     round(log_bad_ratio / (L * L), 6)))
    return rows


if __name__ == "__main__":
    cloud_rows, good_rows = check_face_rectangle()
    scale_rows = check_scale()
    print("PASS")
    print(f"  cloud telescopes: {cloud_rows}")
    print(f"  mixed face rectangles: {good_rows}")
    print(f"  fixed-gap scale: {scale_rows}")
