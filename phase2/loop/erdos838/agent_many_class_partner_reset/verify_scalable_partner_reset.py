#!/usr/bin/env python3
"""Exact rational verifier for the scalable stretchable partner reset.

The construction has t classes of size g=2m and requires m >= t-1.
Every class pair receives a label-disjoint matching of m nonconvex 2+2
circuits.  At each class, different neighbours use different physical
pairs, although every physical label occurs against every neighbour.

Only Fraction arithmetic is used.  The small perturbation and optional
common-uv projective nesting are found by finite exact searches whose
termination is proved in the companion markdown artifact.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations
from math import comb


Point = tuple[Q, Q]
Label = tuple[int, str, int]


def orient(a: Point, b: Point, c: Point) -> Q:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points: list[Point]) -> list[Point]:
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def half(seq: list[Point]) -> list[Point]:
        out: list[Point] = []
        for p in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    return half(points)[:-1] + half(list(reversed(points)))[:-1]


def is_convex(points: list[Point]) -> bool:
    return len(points) <= 3 or len(hull(points)) == len(points)


def vandermonde_x(a: Point, b: Point, c: Point) -> Q:
    x1, x2, x3 = a[0], b[0], c[0]
    return (x2 - x1) * (x3 - x1) * (x3 - x2)


def all_labels(t: int, m: int) -> list[Label]:
    return [(i, side, a)
            for i in range(t) for side in ("L", "R") for a in range(m)]


def skeleton(t: int, m: int) -> dict[Label, Point]:
    """Points on the tangent lines y=2ix-i^2 before perturbation."""
    denominator = 8 * (m + 1)
    far = t + 1
    out: dict[Label, Point] = {}
    for i in range(t):
        for a in range(m):
            small = Q(a + 1, denominator)
            for side, s in (("L", small), ("R", Q(far) + small)):
                x = Q(i) + s
                out[(i, side, a)] = (x, Q(i * i) + 2 * i * s)
    assert len({p[0] for p in out.values()}) == 2 * m * t
    return out


def lift(base: dict[Label, Point], delta: Q) -> dict[Label, Point]:
    return {label: (x, y + delta * x * x)
            for label, (x, y) in base.items()}


def class_labels(t: int, m: int, i: int) -> list[Label]:
    del t
    return [(i, side, a) for side in ("L", "R") for a in range(m)]


def neighbour_rank(i: int, j: int) -> int:
    assert i != j
    return j if j < i else j - 1


def factor(t: int, m: int, i: int, j: int) -> list[tuple[Label, Label]]:
    shift = neighbour_rank(i, j)
    assert 0 <= shift < m
    return [((i, "L", a), (i, "R", (a + shift) % m))
            for a in range(m)]


def selected_circuits(t: int, m: int):
    for i, j in combinations(range(t), 2):
        fi, fj = factor(t, m, i, j), factor(t, m, j, i)
        for a in range(m):
            yield i, j, a, fi[a] + fj[a]


def stability_radius(t: int, m: int, base: dict[Label, Point]) -> Q:
    """A radius preserving every two-class 2+1 triple orientation."""
    ratios: list[Q] = []
    for i, j in combinations(range(t), 2):
        ci, cj = class_labels(t, m, i), class_labels(t, m, j)
        triples = (
            (pair + (z,) for pair in combinations(ci, 2) for z in cj),
            (pair + (z,) for pair in combinations(cj, 2) for z in ci),
        )
        for family in triples:
            for labels in family:
                pts = [base[x] for x in labels]
                d0 = orient(*pts)
                v = vandermonde_x(*pts)
                assert d0 != 0 and v != 0
                ratios.append(abs(d0 / v))
    return min(ratios) / 4


def general_position(points: dict[Label, Point]) -> bool:
    return all(orient(points[a], points[b], points[c]) != 0
               for a, b, c in combinations(points, 3))


def construct(t: int, m: int) -> tuple[dict[Label, Point], Q, int]:
    assert t >= 2 and m >= t - 1
    base = skeleton(t, m)
    delta = stability_radius(t, m, base)
    halvings = 0
    while True:
        points = lift(base, delta)
        if general_position(points):
            return points, delta, halvings
        delta /= 2
        halvings += 1
        assert halvings < 512


def interior_label(quad: tuple[Label, ...], points: dict[Label, Point]) -> Label:
    hull_points = set(hull([points[x] for x in quad]))
    inside = [x for x in quad if points[x] not in hull_points]
    assert len(inside) == 1
    return inside[0]


def circuit_audit(t: int, m: int, points: dict[Label, Point]) -> dict[str, int]:
    owner: dict[tuple[int, tuple[Label, Label]], int] = {}
    pair_graph_degree: Counter[tuple[int, tuple[Label, Label]]] = Counter()
    label_load: Counter[Label] = Counter()
    hidden_classes: Counter[tuple[int, int]] = Counter()
    edges = 0

    for i in range(t):
        for j in range(t):
            if i == j:
                continue
            f = factor(t, m, i, j)
            assert len({x for pair in f for x in pair}) == 2 * m
            for pair in f:
                node = (i, tuple(sorted(pair)))
                assert node not in owner
                owner[node] = j

    for i, j, a, quad in selected_circuits(t, m):
        assert not is_convex([points[x] for x in quad])
        hidden = interior_label(quad, points)
        assert hidden == (j, "L", a)
        hidden_classes[(i, j)] += 1
        pi = (i, tuple(sorted(quad[:2])))
        pj = (j, tuple(sorted(quad[2:])))
        pair_graph_degree[pi] += 1
        pair_graph_degree[pj] += 1
        label_load.update(quad)
        edges += 1

    assert set(pair_graph_degree.values()) == {1}
    assert set(label_load.values()) == {t - 1}
    assert set(hidden_classes.values()) == {m}
    assert edges == comb(t, 2) * m
    return {
        "selected_circuit_edges": edges,
        "label_load": t - 1,
        "pair_node_max_degree": max(pair_graph_degree.values()),
        "pair_node_triangles": 0,
    }


def class_face_audit(t: int, m: int, points: dict[Label, Point]) -> int:
    for i in range(t):
        pts = [points[x] for x in class_labels(t, m, i)]
        assert len(hull(pts)) == 2 * m
    return t * ((1 << (2 * m)) - 1)


def cross_quad_audit(t: int, m: int, points: dict[Label, Point]) -> dict[str, int]:
    convex = bad = 0
    expected_convex_per_pair = m * m * (m - 1) * (2 * m - 1)
    expected_bad_per_pair = m * m * comb(2 * m, 2)
    for i, j in combinations(range(t), 2):
        pair_convex = pair_bad = 0
        for pi in combinations(class_labels(t, m, i), 2):
            for pj in combinations(class_labels(t, m, j), 2):
                if is_convex([points[x] for x in pi + pj]):
                    pair_convex += 1
                else:
                    pair_bad += 1
        assert pair_convex == expected_convex_per_pair
        assert pair_bad == expected_bad_per_pair
        convex += pair_convex
        bad += pair_bad
    assert convex + bad == comb(t, 2) * comb(2 * m, 2) ** 2
    return {
        "convex_2+2_quads": convex,
        "nonconvex_2+2_quads": bad,
    }


def canonical_release(quad: tuple[Label, ...], y: Label,
                      points: dict[Label, Point]) -> frozenset[Label]:
    for z in sorted(quad):
        candidate = [x for x in quad if x != z] + [y]
        if is_convex([points[x] for x in candidate]):
            return frozenset(candidate)
    raise AssertionError("ES(4)=5 release was not found")


def es5_audit(t: int, m: int, points: dict[Label, Point]) -> dict[str, int]:
    outputs: defaultdict[frozenset[Label], list[tuple[int, int, int, Label]]] = defaultdict(list)
    records = 0
    for i, j, a, quad in selected_circuits(t, m):
        for k in range(t):
            if k in (i, j):
                continue
            for y in class_labels(t, m, k):
                out = canonical_release(quad, y, points)
                assert len({x[0] for x in out}) == 3
                outputs[out].append((i, j, a, y))
                records += 1
    max_load = max(map(len, outputs.values()), default=0)
    assert records == comb(t, 2) * m * (t - 2) * 2 * m
    assert max_load <= 3
    assert 3 * len(outputs) >= records
    return {
        "es5_records": records,
        "es5_distinct_faces": len(outputs),
        "es5_max_decoder_load": max_load,
    }


def projective_image(p: Point, scale: Q, epsilon: Q) -> Point:
    f, h = p[0] / scale, p[1] / scale
    denominator = 2 + epsilon * f
    return (epsilon * epsilon * h / denominator, -1 / denominator)


def nest_in_common_uv(points: dict[Label, Point]):
    scale = 1 + max(max(abs(x), abs(y)) for x, y in points.values())
    raw_order = sorted(points, key=lambda z: points[z][0])
    epsilon = Q(1, 16)
    u, v, outside = (Q(-1), Q(0)), (Q(1), Q(0)), (Q(1, 7), Q(1))

    for halvings in range(512):
        image = {label: projective_image(p, scale, epsilon)
                 for label, p in points.items()}
        tangents = []
        for label in raw_order:
            f, h = points[label][0] / scale, points[label][1] / scale
            tangents.append((2 + epsilon * f + epsilon * epsilon * h,
                             2 + epsilon * f - epsilon * epsilon * h))
        monotone = all(tangents[k][0] < tangents[k + 1][0]
                       and tangents[k][1] < tangents[k + 1][1]
                       for k in range(len(tangents) - 1))
        caged = all(not is_convex([u, v, image[a], image[b]])
                    for a, b in combinations(image, 2))
        compatible = all(is_convex([u, v, outside, image[a]]) for a in image)
        augmented = [u, v, outside] + list(image.values())
        gp = all(orient(*triple) != 0 for triple in combinations(augmented, 3))
        if monotone and caged and compatible and gp:
            # The displayed formula is one projective map.  Check its
            # chirotope preservation up to the single global sign.
            sign = None
            labels = list(points)
            for a, b, c in combinations(labels, 3):
                before = orient(points[a], points[b], points[c])
                after = orient(image[a], image[b], image[c])
                ratio_sign = 1 if before * after > 0 else -1
                sign = ratio_sign if sign is None else sign
                assert ratio_sign == sign
            return image, epsilon, halvings
        epsilon /= 2
    raise AssertionError("common-uv nesting search did not terminate")


def exhaustive_face_count(points: dict[Label, Point]) -> int:
    labels = list(points)
    total = 0
    for size in range(1, len(labels) + 1):
        for subset in combinations(labels, size):
            total += is_convex([points[x] for x in subset])
    return total


def run(t: int, m: int, small_regression: bool) -> dict[str, object]:
    points, delta, delta_halvings = construct(t, m)
    circuits = circuit_audit(t, m, points)
    internal_faces = class_face_audit(t, m, points)
    quads = cross_quad_audit(t, m, points)
    es5 = es5_audit(t, m, points)
    nested, epsilon, nesting_halvings = nest_in_common_uv(points)

    # Projectivity preserves every selected signed circuit and face bank.
    assert circuit_audit(t, m, nested) == circuits
    assert class_face_audit(t, m, nested) == internal_faces
    assert cross_quad_audit(t, m, nested) == quads

    disjoint_bank_lower = (internal_faces + quads["convex_2+2_quads"]
                           + es5["es5_distinct_faces"])
    result: dict[str, object] = {
        "parameters": {"t": t, "m": m, "g": 2 * m, "n": 2 * m * t},
        "delta": str(delta),
        "delta_halvings": delta_halvings,
        "common_uv_epsilon": str(epsilon),
        "nesting_halvings": nesting_halvings,
        **circuits,
        "internal_boolean_faces": internal_faces,
        **quads,
        **es5,
        "certified_disjoint_face_bank_lower_bound": disjoint_bank_lower,
    }

    if small_regression:
        small, _, _ = construct(3, 2)
        small_internal = class_face_audit(3, 2, small)
        small_quads = cross_quad_audit(3, 2, small)["convex_2+2_quads"]
        small_es5 = es5_audit(3, 2, small)["es5_distinct_faces"]
        small_total = exhaustive_face_count(small)
        assert small_total >= small_internal + small_quads + small_es5
        result["small_t3_m2_exact_total_faces"] = small_total

    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", type=int, default=6)
    parser.add_argument("--m", type=int, default=6)
    parser.add_argument("--no-small-regression", action="store_true")
    args = parser.parse_args()
    result = run(args.t, args.m, not args.no_small_regression)
    print("PASS")
    for key, value in result.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
