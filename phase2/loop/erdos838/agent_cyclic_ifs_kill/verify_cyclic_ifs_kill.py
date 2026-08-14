#!/usr/bin/env python3
"""Exact certificate for the binary convex-chain subsystem of the cyclic IFS.

The all-depth argument is the elementary induction written in REPORT.md.  This
script checks every rational inequality used by that induction, including a
finite prefix plus a norm tail estimate for the only nonstationary vector (the
bridge between the two child chains).  It also enumerates the first eight
binary levels as an independent sanity check.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCE = ROOT / "agent_lex_minimizer_search" / "triangular_ifs_certificate.json"
EXPECTED_SOURCE_SHA256 = "c04c767c33c0d8a3947807170427fdee1bf5163efb352f940103dd7203e054c9"

Point = tuple[Q, Q]
Matrix = tuple[tuple[Q, Q], tuple[Q, Q]]


def add(x: Point, y: Point) -> Point:
    return x[0] + y[0], x[1] + y[1]


def sub(x: Point, y: Point) -> Point:
    return x[0] - y[0], x[1] - y[1]


def mv(a: Matrix, x: Point) -> Point:
    return tuple(sum(a[i][j] * x[j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def mm(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def det(a: Matrix) -> Q:
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def apply(affine: tuple[Matrix, Point], x: Point) -> Point:
    return add(mv(affine[0], x), affine[1])


def compose(f: tuple[Matrix, Point], g: tuple[Matrix, Point]):
    return mm(f[0], g[0]), add(mv(f[0], g[1]), f[1])


def fixed_point(f: tuple[Matrix, Point]) -> Point:
    a, t = f
    one_minus = ((1 - a[0][0], -a[0][1]), (-a[1][0], 1 - a[1][1]))
    delta = det(one_minus)
    assert delta != 0
    return (
        (one_minus[1][1] * t[0] - one_minus[0][1] * t[1]) / delta,
        (-one_minus[1][0] * t[0] + one_minus[0][0] * t[1]) / delta,
    )


def inf_norm_matrix(a: Matrix) -> Q:
    return max(sum(abs(x) for x in row) for row in a)


def inf_norm_vector(x: Point) -> Q:
    return max(abs(x[0]), abs(x[1]))


def slope_numerator(v: Point, lower: Q) -> Q:
    """Positive iff slope(v)>lower, assuming v.x>0."""
    return v[1] - lower * v[0]


def below_numerator(v: Point, upper: Q) -> Q:
    """Positive iff slope(v)<upper, assuming v.x>0."""
    return upper * v[0] - v[1]


def orient(a: Point, b: Point, c: Point) -> Q:
    u, v = sub(b, a), sub(c, a)
    return u[0] * v[1] - u[1] * v[0]


def main() -> None:
    raw = SOURCE.read_bytes()
    source_sha256 = hashlib.sha256(raw).hexdigest()
    assert source_sha256 == EXPECTED_SOURCE_SHA256, (
        "upstream fitted IFS changed; re-audit the exact cone certificate"
    )
    source = json.loads(raw)
    assert source["best_permutations"] == [[0, 1, 2], [2, 0, 1], [0, 2, 1]]
    macro = [tuple(map(Q, p)) for p in source["macro_centers"]]

    fs = []
    for center, row in zip(macro, source["best_maps"]):
        a: Matrix = tuple(tuple(Q(x) for x in r) for r in row["matrix"])  # type: ignore[assignment]
        deviation_t: Point = tuple(map(Q, row["translation"]))  # type: ignore[assignment]
        fs.append((a, add(center, deviation_t)))

    # Binary block maps corresponding to IFS words 00 and 01.
    t0 = compose(fs[0], fs[0])
    t1 = compose(fs[0], fs[1])
    a0, a1 = t0[0], t1[0]
    q = macro[0]
    d = sub(apply(t1, q), apply(t0, q))
    C_LO, C_HI = Q(1), Q(3)
    SEP_LO, SEP_HI = Q(243, 200), Q(13, 10)

    assert det(a0) > 0 and det(a1) > 0
    assert d[0] > 0 and slope_numerator(d, C_LO) > 0 and below_numerator(d, C_HI) > 0

    # Positive-determinant projective maps are increasing in slope.  These
    # endpoint tests therefore prove A_i(C) is contained in C.
    cone_vectors = ((Q(1), C_LO), (Q(1), C_HI))
    cone_images = {}
    for name, a in (("A0", a0), ("A1", a1)):
        images = [mv(a, v) for v in cone_vectors]
        assert all(v[0] > 0 for v in images)
        assert all(slope_numerator(v, C_LO) > 0 for v in images)
        assert all(below_numerator(v, C_HI) > 0 for v in images)
        cone_images[name] = images

    # Uniform slope gaps on the two sides of every recursive bridge.
    assert all(below_numerator(mv(a0, v), SEP_LO) > 0 for v in cone_vectors)
    assert all(slope_numerator(mv(a1, v), SEP_HI) > 0 for v in cone_vectors)

    p0, p1 = fixed_point(t0), fixed_point(t1)
    bridge_inf = sub(apply(t1, p0), apply(t0, p1))
    assert bridge_inf[0] > 12000
    assert slope_numerator(bridge_inf, SEP_LO) > Q(15, 2)
    assert below_numerator(bridge_inf, SEP_HI) > 1000
    assert inf_norm_matrix(a0) < Q(3, 5)
    assert inf_norm_matrix(a1) < Q(1, 10)
    assert inf_norm_vector(sub(q, p0)) < 40000
    assert inf_norm_vector(sub(q, p1)) < 2000

    # b_k = T1(T0^k q)-T0(T1^k q), k>=1.  Check k<14 exactly.
    left = right = q
    finite_bridge_margins = []
    for k in range(1, 14):
        left, right = apply(t0, left), apply(t1, right)
        bridge = sub(apply(t1, left), apply(t0, right))
        margins = (
            bridge[0],
            slope_numerator(bridge, SEP_LO),
            below_numerator(bridge, SEP_HI),
        )
        assert min(margins) > 0
        finite_bridge_margins.append(margins)

    # For k>=14, ||b_k-b_inf||_inf is at most the displayed E_k.
    tail_bound = 4000 * Q(3, 5) ** 14 + 1200 * Q(1, 10) ** 14
    assert tail_bound < Q(16, 5)
    assert bridge_inf[0] - tail_bound > 0
    assert slope_numerator(bridge_inf, SEP_LO) - (1 + SEP_LO) * tail_bound > 0
    assert below_numerator(bridge_inf, SEP_HI) - (1 + SEP_HI) * tail_bound > 0

    # Direct exact enumeration, not needed by the induction but useful against
    # implementation/indexing errors.
    def point(word: tuple[int, ...]) -> Point:
        x = q
        for bit in reversed(word):
            x = apply((t0, t1)[bit], x)
        return x

    enumerated = []
    for r in range(1, 9):
        pts = [point(bits) for bits in itertools.product((0, 1), repeat=r)]
        assert all(p[0] < z[0] for p, z in zip(pts, pts[1:]))
        turns = [orient(x, y, z) for x, y, z in zip(pts, pts[1:], pts[2:])]
        assert all(t > 0 for t in turns)
        enumerated.append({"r": r, "size": 2**r, "minimum_turn": str(min(turns)) if turns else None})

    out = {
        "mode": "exact_all_depth_binary_convex_chain_certificate",
        "source": str(SOURCE.relative_to(ROOT.parent.parent.parent.parent)),
        "source_sha256": source_sha256,
        "binary_blocks": [[0, 0], [0, 1]],
        "base_point_macro_digit": 0,
        "matrices": {
            "A0": [[str(x) for x in row] for row in a0],
            "A1": [[str(x) for x in row] for row in a1],
        },
        "determinants": {"A0": str(det(a0)), "A1": str(det(a1))},
        "common_edge_cone": [str(C_LO), str(C_HI)],
        "bridge_cone": [str(SEP_LO), str(SEP_HI)],
        "bridge_limit": [str(x) for x in bridge_inf],
        "bridge_limit_margins": {
            "x_minus_12000": str(bridge_inf[0] - 12000),
            "above_243_over_200_minus_15_over_2": str(slope_numerator(bridge_inf, SEP_LO) - Q(15, 2)),
            "below_13_over_10_minus_1000": str(below_numerator(bridge_inf, SEP_HI) - 1000),
        },
        "tail_start_k": 14,
        "tail_bound": str(tail_bound),
        "finite_bridge_minimum_margins": {
            "x": str(min(v[0] for v in finite_bridge_margins)),
            "above_243_over_200": str(min(v[1] for v in finite_bridge_margins)),
            "below_13_over_10": str(min(v[2] for v in finite_bridge_margins)),
        },
        "enumerated_levels": enumerated,
        "conclusion": "for every r>=1, the 2^r words over blocks 00,01 followed by macro digit 0 form a strict convex chain at IFS depth 2r+1",
    }
    target = HERE / "cyclic_ifs_kill_certificate.json"
    target.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("PASS: exact all-depth certificate")
    print("tail bound at k=14:", tail_bound, "=", float(tail_bound))
    print("bridge separation:", SEP_LO, "< slope(b_k) <", SEP_HI)
    print("binary convex-chain levels enumerated through r=8")


if __name__ == "__main__":
    main()
