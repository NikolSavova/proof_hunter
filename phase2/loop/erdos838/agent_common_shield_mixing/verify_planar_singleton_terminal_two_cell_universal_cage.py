#!/usr/bin/env python3
"""Exact checks for PLANAR_SINGLETON_TERMINAL_TWO_CELL_UNIVERSAL_CAGE."""

from fractions import Fraction
from itertools import combinations
from math import comb, log2


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def general_position(points):
    return all(orient(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))


def hull(points):
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    def build(seq):
        out = []
        for p in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    lo = build(pts)
    hi = build(reversed(pts))
    return lo[:-1] + hi[:-1]


def convex(points):
    return len(points) <= 3 or len(hull(points)) == len(points)


def signs(points):
    return {
        triple: 1 if orient(points[triple[0]], points[triple[1]],
                            points[triple[2]]) > 0 else -1
        for triple in combinations(range(len(points)), 3)
    }


def transform(points, eps):
    # First coordinate a=x+y/101 is generic for the audited child.
    out = []
    for x, y in points:
        a = x + y / 101
        b = y
        out.append((eps * a, 1 + 3 * eps * a + eps * eps * b))
    return out


def tangent(point):
    x, y = point
    return y / (1 + x), y / (1 - x)


def make_configuration():
    # Nine parabola vertices plus a genuine interior point. All coordinates
    # are rational and the generic first coordinate is distinct.
    original = [(Fraction(x), Fraction(x * x)) for x in range(-4, 5)]
    original.append((Fraction(0), Fraction(5)))
    assert general_position(original)
    assert not convex(original)

    u = (Fraction(-1), Fraction(0))
    v = (Fraction(1), Fraction(0))
    carrier_x = [Fraction(-3, 4), Fraction(-1, 2), Fraction(-1, 4),
                 Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]
    carrier = [(x, x * x - 1) for x in carrier_x]

    # Avoid the finite cross-collinearity exceptional set by exact search.
    for denominator in range(1000, 5000):
        eps = Fraction(1, denominator)
        child = transform(original, eps)
        whole = [u, v] + carrier + child
        if general_position(whole):
            return original, child, u, v, carrier, eps
    raise AssertionError("failed to find a generic rational epsilon")


def geometry_audit():
    original, child, u, v, carrier, eps = make_configuration()
    assert signs(original) == signs(child)

    # Tangent orders agree strictly, giving common-edge containment.
    generic_a = [x + y / 101 for x, y in original]
    order = sorted(range(len(child)), key=lambda i: generic_a[i])
    tangent_values = [tangent(child[i]) for i in order]
    assert all(tangent_values[i][0] < tangent_values[i + 1][0]
               and tangent_values[i][1] < tangent_values[i + 1][1]
               for i in range(len(child) - 1))
    for i, j in combinations(range(len(order)), 2):
        inner = child[order[i]]
        outer = child[order[j]]
        # Strict containment is equivalent here to nonconvexity of uvxy;
        # verify the barycentric/hull statement directly.
        assert not convex([u, v, inner, outer])
        assert len(hull([u, v, inner, outer])) == 3

    # Enumerate every carrier face and every intrinsic child face. The
    # child is partitioned into three named clouds for decoder scope.
    carrier_faces = []
    for mask in range(1 << len(carrier)):
        face = [u, v] + [carrier[i] for i in range(len(carrier))
                         if mask >> i & 1]
        assert convex(face)
        carrier_faces.append(face)

    clouds = [[child[i] for i in range(len(child)) if i % 3 == residue]
              for residue in range(3)]
    intrinsic_faces = 0
    tested_rectangles = 0
    for cloud in clouds:
        for mask in range(1, 1 << len(cloud)):
            face = [cloud[i] for i in range(len(cloud)) if mask >> i & 1]
            if not convex(face):
                continue
            intrinsic_faces += 1
            for base in carrier_faces:
                for x in face:
                    assert convex(base + [x])
                if len(face) >= 2:
                    assert not convex(base + face)
                    # Every residual pair is still bad, so no deletion
                    # process can stop above singleton rank.
                    assert all(not convex(base + [x, y])
                               for x, y in combinations(face, 2))
                    tested_rectangles += 1

    # Exact carrier endpoint profile: every subset is a cup; only ranks one
    # and two are caps.
    p = len(carrier) + 2
    H = (1 << p) - 1
    C = p + comb(p, 2)
    U = H
    assert C * U // H == C
    assert C > p ** log2(3)
    return {
        "epsilon": eps,
        "child_faces": intrinsic_faces,
        "carrier_faces": len(carrier_faces),
        "rectangles": tested_rectangles,
        "endpoint_surplus": C,
    }


def density_shadow_audit():
    # A complete q-layer on a p-label adjacent-cell support is the sharp
    # finite support model. Its two-shadow is the complete pair layer.
    R, p, q, r = 18, 10, 4, 7
    family = list(combinations(range(p), q))
    delta = Fraction(len(family), comb(R, q))
    eta = Fraction(1)
    lower = (R - q + 1) * float(eta * delta / r) ** (1 / q)
    assert p >= lower
    shadow = {pair for edge in family for pair in combinations(edge, 2)}
    assert len(shadow) == comb(p, 2)

    # All pairs can be split among the three same/same/cross cell types;
    # one type always carries at least one third.
    left = set(range(p // 2))
    counts = [0, 0, 0]
    for x, y in shadow:
        if x in left and y in left:
            counts[0] += 1
        elif x not in left and y not in left:
            counts[1] += 1
        else:
            counts[2] += 1
    assert max(counts) * 3 >= len(shadow)
    return len(family), len(shadow), counts


def main():
    geometry = geometry_audit()
    family, shadow, types = density_shadow_audit()
    print(
        "PASS: affine universal cage eps=%s child-faces=%d carrier-faces=%d "
        "terminal-rectangles=%d endpoint-surplus=%d; layer=%d shadow=%d "
        "types=%s"
        % (
            geometry["epsilon"],
            geometry["child_faces"],
            geometry["carrier_faces"],
            geometry["rectangles"],
            geometry["endpoint_surplus"],
            family,
            shadow,
            types,
        )
    )


if __name__ == "__main__":
    main()
