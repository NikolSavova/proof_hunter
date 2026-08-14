#!/usr/bin/env python3
"""Exact probe of the cyclic three-cluster self-affine escape route.

The unique n=9 lex minimizer has a unique 3-decomposition into three triples.
Use the cluster centroids as a macro triangle and fit, at each vertex, an
affine map taking the macro triangle to that vertex's three observed deviation
vectors.  Shrinking all maps by an exact rational factor gives a genuine
three-map IFS.  We search the 6^3 possible identifications of micro vertices
at depth three, then iterate the best identification using exact rational
coordinates and the independent reflection-order evaluator.

Finite computations are certificates for the displayed depths only; the
report treats any asymptotic extrapolation explicitly as evidence.
"""

from __future__ import annotations

import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "agent_reflection_gate"))
import reflection_order_gate as gate  # noqa: E402

Point = tuple[Fraction, Fraction]


def add(a: Point, b: Point) -> Point:
    return a[0] + b[0], a[1] + b[1]


def sub(a: Point, b: Point) -> Point:
    return a[0] - b[0], a[1] - b[1]


def scale(t: Fraction, a: Point) -> Point:
    return t * a[0], t * a[1]


def centroid(points: list[Point]) -> Point:
    return (
        sum(p[0] for p in points) / len(points),
        sum(p[1] for p in points) / len(points),
    )


def affine_fit(domain: list[Point], target: list[Point]):
    """Return exact affine H with H(domain[j])=target[j]."""
    x0, x1, x2 = domain
    y0, y1, y2 = target
    u, v = sub(x1, x0), sub(x2, x0)
    r, s = sub(y1, y0), sub(y2, y0)
    det = u[0] * v[1] - u[1] * v[0]
    if det == 0:
        raise ValueError("macro domain is collinear")
    # A = [r s] [u v]^{-1}
    a00 = (r[0] * v[1] - s[0] * u[1]) / det
    a01 = (-r[0] * v[0] + s[0] * u[0]) / det
    a10 = (r[1] * v[1] - s[1] * u[1]) / det
    a11 = (-r[1] * v[0] + s[1] * u[0]) / det
    translation = (
        y0[0] - a00 * x0[0] - a01 * x0[1],
        y0[1] - a10 * x0[0] - a11 * x0[1],
    )

    def transform(p: Point) -> Point:
        return (
            a00 * p[0] + a01 * p[1] + translation[0],
            a10 * p[0] + a11 * p[1] + translation[1],
        )

    return transform, [[a00, a01], [a10, a11]], translation


def evaluation(points: list[Point]):
    points = sorted(points)
    n = len(points)
    slopes = sorted(
        ((points[j][1] - points[i][1]) / (points[j][0] - points[i][0]), i, j)
        for i in range(n)
        for j in range(i + 1, n)
    )
    roots = tuple((i, j) for _, i, j in slopes)
    word = gate.word_from_roots(n, roots)
    return gate.evaluate_word(n, word, graded=n <= 81)


def make_maps(macro, clusters, permutations, shrink):
    maps = []
    metadata = []
    for c in range(3):
        center = centroid(clusters[c])
        targets = [sub(clusters[c][permutations[c][j]], center) for j in range(3)]
        linear_deviation, matrix, translation = affine_fit(macro, targets)

        def f(point, c=c, linear_deviation=linear_deviation):
            return add(macro[c], scale(shrink, linear_deviation(point)))

        maps.append(f)
        metadata.append(
            {
                "matrix": [[str(x) for x in row] for row in matrix],
                "translation": [str(x) for x in translation],
            }
        )
    return maps, metadata


def expand(points, maps):
    return [f(point) for f in maps for point in points]


def main():
    data = json.loads((HERE / "exact_realizable_n9.json").read_text())
    points = sorted(tuple(map(Fraction, p)) for p in data["coordinates_as_stored"])
    groups = ((0, 1, 5), (2, 3, 4), (6, 7, 8))
    clusters = [[points[i] for i in group] for group in groups]
    macro = [centroid(cluster) for cluster in clusters]
    # shrink=1 reproduces the database n=9 set exactly at depth two.  The
    # fitted linear maps are already contractions in the relevant cluster
    # geometry; smaller common factors cross an order-type wall because the
    # observed clusters are not infinitesimal relative to their centroids.
    shrink = Fraction(1)

    base_eval = evaluation(macro)
    if base_eval.trace != 7:
        raise AssertionError("macro triangle should have seven nonempty subsets")
    permutation_options = list(itertools.permutations(range(3)))
    records = []
    best = None
    for permutations in itertools.product(permutation_options, repeat=3):
        maps, metadata = make_maps(macro, clusters, permutations, shrink)
        depth2 = expand(macro, maps)
        e2 = evaluation(depth2)
        if e2.trace != 168:
            raise AssertionError("shrunk n=9 order type changed")
        depth3 = expand(depth2, maps)
        e3 = evaluation(depth3)
        row = {
            "permutations": [list(p) for p in permutations],
            "depth3_n": 27,
            "depth3_trace": e3.trace,
            "depth3_first_moment": e3.first_moment,
            "depth3_mean_deficit": e3.mean_minus_log_n,
            "maps": metadata,
        }
        records.append(row)
        key = (e3.trace, e3.first_moment)
        if best is None or key < best[0]:
            best = (key, permutations, maps, metadata)
    assert best is not None

    _, best_permutations, maps, metadata = best
    depth_rows = []
    current = macro
    for depth in range(1, 6):
        if depth > 1:
            current = expand(current, maps)
        e = evaluation(current)
        depth_rows.append(
            {
                "depth": depth,
                "n": len(current),
                "trace": e.trace,
                "first_moment": e.first_moment,
                "mean_size": e.mean_size,
                "mean_minus_log2_n": e.mean_minus_log_n,
                "normalized_log_trace": e.normalized,
                "graded": list(e.graded) if e.graded is not None else None,
            }
        )
    output = {
        "mode": "exact_rational_cyclic_three_cluster_ifs_probe",
        "shrink": str(shrink),
        "macro_centers": [[str(x), str(y)] for x, y in macro],
        "mapping_count_depth3": len(records),
        "best_permutations": [list(p) for p in best_permutations],
        "best_maps": metadata,
        "depth_rows": depth_rows,
        "depth3_trace_range": [min(r["depth3_trace"] for r in records), max(r["depth3_trace"] for r in records)],
        "depth3_mean_deficit_range": [min(r["depth3_mean_deficit"] for r in records), max(r["depth3_mean_deficit"] for r in records)],
    }
    (HERE / "triangular_ifs_certificate.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    print("best permutations", best_permutations)
    for row in depth_rows:
        print(row)


if __name__ == "__main__":
    main()
