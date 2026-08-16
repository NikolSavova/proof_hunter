#!/usr/bin/env python3
"""Exact checks for FIXED_EDGE_CARRIER_ENDPOINT_DILUTION_GATE."""

from fractions import Fraction
from itertools import combinations, product
from math import log2


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    def build(seq):
        out = []
        for point in seq:
            while (len(out) >= 2
                   and orient(out[-2], out[-1], point) <= 0):
                out.pop()
            out.append(point)
        return out

    lower = build(pts)
    upper = build(reversed(pts))
    return lower[:-1] + upper[:-1]


def convex(points):
    return len(points) <= 3 or len(hull(points)) == len(points)


def general_position(points):
    return all(orient(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))


def directional_sign(points):
    """Return the common x-ordered triple sign, or zero if not a chain."""
    ordered = sorted(points)
    values = {1 if orient(*triple) > 0 else -1
              for triple in combinations(ordered, 3)}
    return next(iter(values)) if len(values) == 1 else 0


def project(point, lam):
    x, y = point
    denominator = 1 - lam * y
    assert denominator > 0
    return x / denominator, y / denominator


def endpoint_counts(points):
    caps = cups = ordinary = 0
    for mask in range(1, 1 << len(points)):
        subset = [points[i] for i in range(len(points)) if mask >> i & 1]
        if convex(subset):
            ordinary += 1
        sign = directional_sign(subset)
        if len(subset) <= 2 or sign > 0:
            caps += 1
        if len(subset) <= 2 or sign < 0:
            cups += 1
    return ordinary, caps, cups


def projective_audit():
    f = Fraction
    u, v = (f(-1), f(0)), (f(1), f(0))
    xs = [-4, -3, -2, 0, 2, 3, 4]
    carrier = [(f(x), f(-x * x - 5) + f(x ** 3, 97)) for x in xs]
    points = [u, v] + carrier
    assert general_position(points)
    assert all(y < 0 for _, y in carrier)

    lam = f(10)
    image = [project(point, lam) for point in points]
    assert general_position(image)
    assert image[:2] == [u, v]
    assert all(-1 < x < 1 for x, _ in image[2:])
    assert all(
        (orient(points[i], points[j], points[k]) > 0)
        == (orient(image[i], image[j], image[k]) > 0)
        for i, j, k in combinations(range(len(points)), 3)
    )

    fixed_faces = []
    fixed_signs = set()
    for mask in range(1 << len(carrier)):
        subset = [u, v] + [carrier[i] for i in range(len(carrier))
                            if mask >> i & 1]
        if convex(subset):
            fixed_faces.append(mask)
            transformed = [u, v] + [image[2 + i] for i in range(len(carrier))
                                      if mask >> i & 1]
            if len(transformed) >= 3:
                fixed_signs.add(directional_sign(transformed))
    assert len(fixed_signs) == 1 and 0 not in fixed_signs

    ordinary, caps, cups = endpoint_counts(image)
    h = len(fixed_faces)
    p = len(points)
    fixed_profile = caps if next(iter(fixed_signs)) > 0 else cups
    assert fixed_profile >= h
    assert min(caps, cups) >= p + p * (p - 1) // 2
    assert caps * cups >= h * (p * (p - 1) // 2)
    assert caps * cups / ordinary >= h * (p * (p - 1) // 2) / ordinary
    return p, h, ordinary, caps, cups


def insertion_edge(base, point):
    enlarged = hull(base + [point])
    if len(enlarged) != len(base) + 1:
        return None
    for index in range(len(base)):
        a, b = base[index], base[(index + 1) % len(base)]
        still_edge = any(
            {enlarged[j], enlarged[(j + 1) % len(enlarged)]} == {a, b}
            for j in range(len(enlarged))
        )
        if not still_edge:
            return index
    raise AssertionError("no replaced edge")


def adjacent_release_audit():
    base = [(-4, 0), (-2, -3), (2, -3), (4, 0), (0, 5)]
    assert convex(base) and general_position(base)
    cells = {index: [] for index in range(len(base))}
    for point in product(range(-10, 11), repeat=2):
        if point in base:
            continue
        edge = insertion_edge(base, point)
        if edge is not None:
            cells[edge].append(point)

    tested = bad = 0
    for left_edge in range(len(base)):
        right_edge = (left_edge + 1) % len(base)
        shared = base[right_edge]
        outputs = set()
        for x in cells[left_edge]:
            for y in cells[right_edge]:
                tested += 1
                released = tuple(sorted([point for point in base
                                         if point != shared] + [x, y]))
                assert convex(list(released))
                if not convex(base + [x, y]):
                    bad += 1
                    assert released not in outputs
                    outputs.add(released)
    assert tested > 1000 and bad > 100
    return tested, bad


def exponent_audit():
    a = log2(3)
    theta = 2 - a
    assert abs((2 - theta) - a) < 1e-15
    for p in [16, 64, 256, 1024]:
        epsilon = 0.1
        lower = p ** (-theta + epsilon) * (p * (p - 1) / 2)
        asserted = p ** (a + epsilon) / 3
        assert lower >= asserted


def main():
    p, h, ordinary, caps, cups = projective_audit()
    tested, bad = adjacent_release_audit()
    exponent_audit()
    print(
        "PASS: projective common-edge normalization p=%d H=%d V=%d "
        "C=%d U=%d surplus=%.6f; adjacent-tests=%d bad-releases=%d"
        % (p, h, ordinary, caps, cups, caps * cups / ordinary,
           tested, bad)
    )


if __name__ == "__main__":
    main()
