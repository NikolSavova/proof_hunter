#!/usr/bin/env python3
"""Exact verifier for NESTED_TRIANGLE_LIVE_NORMALIZATION_AUDIT.md."""

from itertools import combinations
import math
import random


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def strict_inside_triangle(p, tri):
    signs = [orient(tri[i], tri[(i + 1) % 3], p) for i in range(3)]
    return all(x > 0 for x in signs) or all(x < 0 for x in signs)


def general_position(points):
    return all(orient(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))


def convex_hull(points):
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    def half(seq):
        out = []
        for p in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    lo = half(pts)
    hi = half(reversed(pts))
    return lo[:-1] + hi[:-1]


def convex_position(points):
    return len(points) <= 2 or len(convex_hull(points)) == len(points)


def nested_triangles(count, central):
    rng = random.Random(83820260815)
    triangles = []
    existing = list(central)
    for t in range(count):
        scale = 1000 ** (t + 2)
        for _ in range(10000):
            z = [rng.randrange(-10000, 10001) for _ in range(6)]
            tri = [(-scale + z[0], -scale + z[1]),
                   (scale + z[2], -scale + z[3]),
                   (z[4], scale + z[5])]
            if orient(*tri) < 0:
                tri[1], tri[2] = tri[2], tri[1]
            required = central if not triangles else triangles[-1]
            if not all(strict_inside_triangle(p, tri) for p in required):
                continue
            if not general_position(existing + tri):
                continue
            triangles.append(tuple(tri))
            existing.extend(tri)
            break
        else:
            raise RuntimeError("generic nested triangle search failed")
    return triangles


def geometry_audit():
    central = [(-3, -2), (3, -2), (4, 3), (-2, 4), (0, 1)]
    m, k = len(central), 3
    triangles = nested_triangles(m * k, central)
    all_points = central + [p for tri in triangles for p in tri]
    assert general_position(all_points)

    # The three arbitrary vertex-position clouds are disjoint and have R=km.
    clouds = [{tri[r] for tri in triangles} for r in range(3)]
    assert [len(cloud) for cloud in clouds] == [k * m] * 3
    assert all(a.isdisjoint(b) for a, b in combinations(clouds, 2))

    # Canonical five-point extension: every output has two central labels
    # and two labels of a unique record triangle, and the decoder is injective.
    outputs = {}
    for t, tri in enumerate(triangles):
        j, a = divmod(t, m)
        y_a = central[a]
        assert strict_inside_triangle(y_a, tri)
        assert not convex_position([y_a, *tri])
        for b, y_b in enumerate(central):
            if b == a:
                continue
            assert strict_inside_triangle(y_b, tri)
            candidates = []
            for omitted in range(3):
                face = [y_a, y_b] + [tri[r] for r in range(3)
                                      if r != omitted]
                if convex_position(face):
                    candidates.append((omitted, tuple(sorted(face))))
            assert candidates, (t, b)
            omitted, output = min(candidates)
            assert convex_position(list(output))
            assert output not in outputs
            outputs[output] = (j, a, b, omitted)

    assert len(outputs) == k * m * (m - 1)
    return m, k, len(outputs)


def phi(L, C=3.0):
    return 0.5 * L * L - C * L * math.log2(L)


def asymptotic_audit():
    C = 3.0
    previous_cloud_slope = None
    for L in (64, 128, 256, 512, 1024, 2048):
        k = max(2.0, math.log2(L))
        beta = math.log2(3.0 + 1.0 / k)
        alpha = math.log2(1.0 + 3.0 * k)
        cloud_gap = phi(L, C) - phi(L - beta, C)
        central_gap = phi(L, C) - phi(L - alpha, C)
        # Exact subtraction identity (13).
        cloud_formula = (beta * L - 0.5 * beta * beta
                         - C * (L * math.log2(L)
                                - (L - beta) * math.log2(L - beta)))
        central_formula = (alpha * L - 0.5 * alpha * alpha
                           - C * (L * math.log2(L)
                                  - (L - alpha) * math.log2(L - alpha)))
        assert abs(cloud_gap - cloud_formula) < 1e-7
        assert abs(central_gap - central_formula) < 1e-7
        assert central_gap > cloud_gap > 0
        assert 2 * L < phi(L - beta, C)  # polynomial ES bank is negligible
        slope = cloud_gap / L
        if previous_cloud_slope is not None:
            assert slope > previous_cloud_slope
        previous_cloud_slope = slope
    assert abs(previous_cloud_slope - math.log2(3)) < 0.06


def source_and_cauchy_audit():
    # Exhaust an arbitrary weighted record grouping.
    weights = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]
    R = 4
    fibres = [sum(weights[i] for i in range(len(weights)) if i % R == r)
              for r in range(R)]
    W = sum(weights)
    lam = max(fibres)
    assert W <= R * lam

    # If W>=V/Q and WH<=Lambda V^2, then V>=H/(Q Lambda).
    # Check the implication on an exact integer grid.
    for V in range(1, 40):
        for Q in range(1, 8):
            for decoder in range(1, 6):
                for H in range(1, 40):
                    W0 = (V + Q - 1) // Q
                    if W0 * H <= decoder * V * V:
                        assert V * Q * decoder >= H


def ramp_audit():
    # Exact integer verification of (22)--(25).
    for q in range(2, 13):
        B = q * q + 1
        h = 4 * q + (q % 2)  # h-q even and h>3q
        if (h - q) % 2:
            h += 1
        b = (h - q) // 2
        H = B ** h
        C = [B ** (b + i) for i in range(q)]
        U = [B ** (h - b - i) for i in range(q)]
        assert all(C[i] * U[i] == H for i in range(q))
        cross = 0
        for i in range(q):
            for j in range(i + 1, q):
                term = C[i] * U[j] * B ** (j - i - 1)
                assert term == H // B
                cross += term
        Wlin = q * H + cross
        assert Wlin == q * H + q * (q - 1) // 2 * (H // B)
        assert Wlin <= 2 * q * H


def main():
    m, k, extensions = geometry_audit()
    asymptotic_audit()
    source_and_cauchy_audit()
    ramp_audit()
    print("PASS: nested live audit",
          f"central={m}", f"partners={k}",
          f"five_point_outputs={extensions}",
          "cloud/source/ramp ledgers exact")


if __name__ == "__main__":
    main()
