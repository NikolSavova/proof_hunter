#!/usr/bin/env python3
"""Exact audit of the shelling-antimatroid formulation of HW2.

The script reconstructs all closed sets from an integer planar point set,
checks the Tutte/continuation specialization, and exhibits deletion minors
which violate HW2 even though the planar parent satisfies it.
"""

import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO_838 = HERE.parent
POINT_CERTIFICATE = (
    REPO_838 / "agent_lex_minimizer_search" / "direct_hull_certificates.json"
)


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull_index_set(points, selected):
    ordered = sorted(selected, key=lambda i: points[i])
    if len(ordered) <= 1:
        return ordered
    lower = []
    for i in ordered:
        while len(lower) >= 2 and orient(points[lower[-2]], points[lower[-1]], points[i]) <= 0:
            lower.pop()
        lower.append(i)
    upper = []
    for i in reversed(ordered):
        while len(upper) >= 2 and orient(points[upper[-2]], points[upper[-1]], points[i]) <= 0:
            upper.pop()
        upper.append(i)
    return lower[:-1] + upper[:-1]


def in_convex_polygon(points, polygon, point_index):
    return all(
        orient(points[polygon[i]], points[polygon[(i + 1) % len(polygon)]], points[point_index]) >= 0
        for i in range(len(polygon))
    )


def closed_set_records(points):
    """Return closed-set mask -> its unique extreme-set mask."""
    n = len(points)
    records = {}
    for extreme_mask in range(1 << n):
        selected = [i for i in range(n) if (extreme_mask >> i) & 1]
        polygon = hull_index_set(points, selected)
        if len(selected) >= 3 and len(polygon) != len(selected):
            continue
        if len(selected) <= 2:
            closed_mask = extreme_mask
        else:
            closed_mask = sum(
                1 << i
                for i in range(n)
                if in_convex_polygon(points, polygon, i)
            )
        # General position makes ext(cl(A))=A for convexly independent A.
        assert closed_mask not in records or records[closed_mask] == extreme_mask
        records[closed_mask] = extreme_mask
    return records


def profile(records, n):
    out = [0] * (n + 1)
    for extreme_mask in records.values():
        out[extreme_mask.bit_count()] += 1
    return out


def evaluate(poly, z):
    return sum((Q(coefficient) * z**degree for degree, coefficient in enumerate(poly)), Q(0))


def h_value(n, poly):
    return Q(n) * evaluate(poly, Q(1, 2)) / evaluate(poly, Q(1))


def antimatroid_f(records, t, z):
    """Feasible-set expansion, indexed equivalently by closed complements."""
    total = Q(0)
    for closed_mask, extreme_mask in records.items():
        closed_size = closed_mask.bit_count()
        continuation_size = extreme_mask.bit_count()
        total += t**closed_size * (z + 1) ** (closed_size - continuation_size)
    return total


def minor_profiles(records, n, extreme_element):
    """Profiles in the greedoid deletion and contraction by a feasible singleton."""
    deletion = [0] * n
    contraction = [0] * n
    for closed_mask, extreme_mask in records.items():
        k = extreme_mask.bit_count()
        if (closed_mask >> extreme_element) & 1:
            # A global hull point in a closed set is one of its extreme points.
            assert (extreme_mask >> extreme_element) & 1
            deletion[k - 1] += 1
        else:
            contraction[k] += 1
    return deletion, contraction


def main():
    source = json.loads(POINT_CERTIFICATE.read_text())["9"]
    points = [tuple(point) for point in source["coordinates"]]
    n = len(points)
    records = closed_set_records(points)
    parent = profile(records, n)
    assert parent == [1, 9, 36, 84, 36, 3, 0, 0, 0, 0]
    assert len(records) == source["empty_inclusive_count"] == 169

    # Z(s)=f(s,s^{-1}-1), and in particular the two HW2 evaluations are
    # f(1/2,1) and f(1,0).  The universal greedoid identity f(1,1)=2^n
    # is also checked directly.
    for s in (Q(1, 2), Q(1), Q(2, 3)):
        assert antimatroid_f(records, s, 1 / s - 1) == evaluate(parent, s)
    assert antimatroid_f(records, Q(1), Q(1)) == 2**n
    assert h_value(n, parent) < 2

    hull_vertices = set(hull_index_set(points, list(range(n))))
    assert hull_vertices == {0, 1, 8}
    for e in hull_vertices:
        deletion, contraction = minor_profiles(records, n, e)
        assert deletion == [1, 8, 28, 15, 2, 0, 0, 0, 0]
        assert contraction == [1, 8, 28, 56, 21, 1, 0, 0, 0]
        assert h_value(n - 1, deletion) == Q(56, 27) > 2

        # The specialized deletion-contraction recurrence is
        # Z_G(s)=s Z_(G-e)(s)+Z_(G/e)(s).
        for s in (Q(1, 2), Q(1), Q(2, 3)):
            assert evaluate(parent, s) == s * evaluate(deletion, s) + evaluate(contraction, s)

    print("shelling-antimatroid bridge: PASS")
    print(f"parent profile={parent}, H={h_value(n, parent)}")
    print(f"hull vertices={sorted(hull_vertices)}")
    print(f"every deletion-minor profile={deletion}, H={h_value(n-1, deletion)} > 2")
    print(f"every contraction profile={contraction}, H={h_value(n-1, contraction)}")
    print("Z(s)=f(s,s^-1-1), f(1,1)=2^n, and deletion-contraction all verified exactly")


if __name__ == "__main__":
    main()
