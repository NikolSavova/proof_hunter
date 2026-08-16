#!/usr/bin/env python3
"""Exact certificates for the weighted endpoint counterfamily.

All coordinates and orientation tests are integral.  Endpoint path
polynomials use one factor of z per edge, so the product of an upper and a
lower path has degree equal to the size of their convex union.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction


def orient(a, b, c):
    v = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    if not v:
        raise AssertionError((a, b, c))
    return 1 if v > 0 else -1


def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return out


def endpoint_poly(points, s, t, sign):
    """Polynomial for sign-monotone paths from s to t."""
    edge = {}
    for j in range(s + 1, t + 1):
        edge[(s, j)] = [0, 1]
    for i in range(s + 1, t):
        for j in range(i + 1, t + 1):
            p = [0]
            for h in range(s, i):
                if (h, i) in edge and orient(points[h], points[i], points[j]) == sign:
                    p = add(p, [0] + edge[(h, i)])
            if any(p):
                edge[(i, j)] = p
    ans = [0]
    for i in range(s, t):
        if (i, t) in edge:
            ans = add(ans, edge[(i, t)])
    return ans


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def value_and_mean(poly, z=Fraction(1, 2)):
    value = sum(Fraction(c) * z**k for k, c in enumerate(poly))
    moment = sum(Fraction(k * c) * z**k for k, c in enumerate(poly))
    return value, moment / value


def hull(points):
    if len(points) <= 1:
        return points
    points = sorted(points)
    def cross(a, b, c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo = []
    for p in points:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    hi = []
    for p in reversed(points):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    return lo[:-1] + hi[:-1]


def profile(points):
    n = len(points)
    ans = [0] * (n + 1)
    for mask in range(1 << n):
        subset = [points[i] for i in range(n) if mask >> i & 1]
        if len(subset) <= 3 or len(hull(subset)) == len(subset):
            ans[len(subset)] += 1
    return ans


def parabola_chord(n):
    """0, n-2 parabola points, then a point back on the x-axis."""
    assert n >= 3
    return [(0, 0)] + [(k, k * k) for k in range(1, n - 1)] + [(n - 1, 0)]


def visible_pocket(m):
    # The certificate from agent_visible_flip_hw, sorted by x-coordinate.
    L = m + 1
    return [(-1, (L + 1) ** 2)] + [(i, i * (L - i)) for i in range(L + 1)]


def record(points, s, t, brute=False):
    cup = endpoint_poly(points, s, t, +1)
    cap = endpoint_poly(points, s, t, -1)
    product = mul(cup, cap)
    half, mean = value_and_mean(product)
    out = {
        "n": len(points),
        "endpoint": [s, t],
        "span": t - s + 1,
        "cup": cup,
        "cap": cap,
        "product": product,
        "product_at_half": str(half),
        "half_activity_mean": str(mean),
        "mean_minus_log2_span": float(mean) - math.log2(t - s + 1),
        "endpoint_ratio_one_over_half": float(sum(product) / half),
    }
    if brute:
        prof = profile(points)
        zhalf = sum(Fraction(c, 2**k) for k, c in enumerate(prof))
        out.update({
            "profile": prof,
            "Z_one": sum(prof),
            "Z_half": str(zhalf),
            "H": float(len(points) * zhalf / sum(prof)),
            "local_compensation_score": math.log2(float(Fraction(sum(prof), 1) / half))
                - math.log2(t - s + 1),
        })
    return out


def main():
    records = []
    for n in range(3, 15):
        pts = parabola_chord(n)
        rec = record(pts, 0, n - 1, brute=n <= 13)
        expected_cap = [0, 1, n - 2]
        assert rec["cup"] == [0, 1]
        assert rec["cap"] == expected_cap
        assert rec["half_activity_mean"] == str(Fraction(3 * n - 2, n))
        # Deleting the last point leaves n-1 points on a strict convex chain.
        if n <= 13:
            assert sum(profile(pts[:-1])) == 2 ** (n - 1)
            expected_profile = [0] * (n + 1)
            expected_profile[0] = 1
            expected_profile[1] = n
            expected_profile[2] = math.comb(n, 2)
            expected_profile[3] = math.comb(n, 3)
            for k in range(4, n + 1):
                expected_profile[k] = math.comb(n - 1, k)
            assert rec["profile"] == expected_profile
        records.append({"family": "parabola_chord", **rec})

    for m in (2, 4, 6, 8):
        pts = visible_pocket(m)
        # q_0 and q_L are positions 1 and len(points)-1.
        rec = record(pts, 1, len(pts) - 1, brute=len(pts) <= 13)
        # The q_i form a cap chain; every subset of the m internal points is
        # an endpoint cap and the endpoint cup is direct.
        expected_cap = [0, 1]
        for _ in range(m):
            expected_cap = mul(expected_cap, [1, 1])
        assert rec["cap"] == expected_cap
        assert rec["cup"] == [0, 1]
        records.append({"family": "visible_pocket", "m": m, **rec})

    result = {
        "description": "exact weighted cup-cap endpoint and localization stress tests",
        "records": records,
    }
    with open("phase2/loop/erdos838/agent_weighted_cupcap/certificate.json", "w") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
