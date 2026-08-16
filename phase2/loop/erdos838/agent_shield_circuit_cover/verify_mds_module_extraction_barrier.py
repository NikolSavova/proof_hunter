#!/usr/bin/env python3
"""Exact checks for MDS_MODULE_EXTRACTION_BARRIER.md."""

from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
CERT = HERE / "mds_module_extraction_barrier_certificate.json"


def eval_poly(coeffs, x, p):
    value = 0
    for a in reversed(coeffs):
        value = (value * x + a) % p
    return value


def rs_code(p, q, k):
    points = tuple(range(1, q + 1))
    return {
        tuple(eval_poly(coeffs, x, p) for x in points)
        for coeffs in itertools.product(range(p), repeat=k)
    }


def rs_audit():
    p, q, k = 17, 6, 4
    code = rs_code(p, q, k)
    assert len(code) == p**k
    nonzero_weights = [sum(x != 0 for x in word) for word in code if any(word)]
    dmin = min(nonzero_weights)
    assert dmin == q - k + 1 == 3
    left = {word[: q // 2] for word in code}
    right = {word[q // 2 :] for word in code}
    assert len(left) == len(right) == p ** (q // 2)
    rectangle = len(left) * len(right)
    assert rectangle // len(code) == p ** (q - k)
    module_bound = q // dmin
    assert module_bound == 2
    return {
        "field_prime": p,
        "length_q": q,
        "dimension_k": k,
        "codewords": len(code),
        "minimum_distance": dmin,
        "left_projection": len(left),
        "right_projection": len(right),
        "tangent_rectangle": rectangle,
        "rectangle_to_selected_ratio": rectangle // len(code),
        "maximum_disjoint_variable_modules": module_bound,
    }


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def half(seq):
        out = []
        for point in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], point) <= 0:
                out.pop()
            out.append(point)
        return out

    return half(points)[:-1] + half(reversed(points))[:-1]


def convex(points, labels):
    labels = tuple(labels)
    return len(labels) <= 2 or len(hull([points[x] for x in labels])) == len(labels)


def planar_audit():
    p, q, k = 5, 4, 3
    code = rs_code(p, q, k)
    assert len(code) == 125
    assert min(sum(x != 0 for x in w) for w in code if any(w)) == 2

    points = {}
    T = []
    for x in (-2, -1, 0, 1, 2):
        label = f"t{x:+d}"
        points[label] = (Q(x), Q(-x * x))
        T.append(label)
    centres = (Q(-4), Q(-3), Q(3), Q(4))
    clusters = []
    for i, centre in enumerate(centres):
        block = []
        for value in range(p):
            x = centre + Q(value - 2, 25)
            label = f"X{i}_{value}"
            points[label] = (x, -(x * x))
            block.append(label)
        clusters.append(tuple(block))
    Z = []
    for i, x in enumerate((Q(-3, 5), Q(-3, 10), Q(0), Q(3, 10), Q(3, 5))):
        label = f"z{i}"
        points[label] = (x, Q(-100) - x * x)
        Z.append(label)

    for triple in itertools.combinations(points, 3):
        assert orient(*(points[x] for x in triple)) != 0

    sources = []
    for word in code:
        petal = tuple(clusters[i][word[i]] for i in range(q))
        U = tuple(sorted(tuple(T) + petal, key=lambda x: points[x][0]))
        assert convex(points, U)
        assert tuple(U[2:-2]) == tuple(T)
        sources.append(U)
    assert len(set(sources)) == len(code)

    W = (Z[0], Z[2], Z[4])
    e = (T[0], T[-1])
    assert convex(points, W)
    assert not convex(points, e + W)
    mark = T[2]
    for U in sources:
        ordered = tuple(sorted(U, key=lambda x: points[x][0]))
        pos = ordered.index(mark)
        assert ordered[pos - 2 : pos + 3] == tuple(T)
        assert convex(points, tuple(x for x in U if x != mark))

    # Every unselected transversal is also geometrically available.
    all_transversals = 0
    for word in itertools.product(range(p), repeat=q):
        petal = tuple(clusters[i][word[i]] for i in range(q))
        assert convex(points, tuple(T) + petal)
        all_transversals += 1
    assert all_transversals == p**q

    left = {w[:2] for w in code}
    right = {w[2:] for w in code}
    assert len(left) == len(right) == p**2
    return {
        "field_prime": p,
        "length_q": q,
        "dimension_k": k,
        "ambient_points": len(points),
        "selected_sources": len(sources),
        "available_transversals": all_transversals,
        "left_projection": len(left),
        "right_projection": len(right),
        "rectangle_surplus_factor": all_transversals // len(sources),
        "common_parent": list(T),
        "common_W": list(W),
        "W_union_endpoint_convex": False,
        "fixed_mark": mark,
        "fixed_tangent_tuple": list(T),
    }


def asymptotic_audit():
    rows = []
    for L in (64, 128, 256, 512):
        q = L // 4
        c = math.ceil(q / math.log2(L))
        k = q - c
        selected_log = k * L
        rectangle_log = q * L
        surplus_log = c * L
        dmin = c + 1
        modules = q // dmin
        assert surplus_log / (L * L) <= 1 / math.log2(L) + 1 / L
        assert modules <= math.ceil(math.log2(L))
        rows.append({
            "L": L,
            "q": q,
            "codimension_c": c,
            "dimension_k": k,
            "minimum_distance": dmin,
            "selected_log2": selected_log,
            "selected_coefficient": selected_log / (L * L),
            "rectangle_surplus_log2": surplus_log,
            "surplus_coefficient": surplus_log / (L * L),
            "maximum_disjoint_modules": modules,
            "one_gap_coefficient_lower_bound": q / L + 1 / 8,
        })
    assert rows[-1]["selected_coefficient"] > 0.2
    assert rows[-1]["one_gap_coefficient_lower_bound"] == 0.375
    return rows


def main():
    cert = {
        "exact_rs_code": rs_audit(),
        "planar_fixed_tuple": planar_audit(),
        "asymptotic_scaling": asymptotic_audit(),
    }
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print("PASS verify_mds_module_extraction_barrier")
    print(json.dumps(cert, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
