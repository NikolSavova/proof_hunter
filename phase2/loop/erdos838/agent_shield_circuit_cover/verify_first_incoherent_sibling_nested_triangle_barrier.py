#!/usr/bin/env python3
"""Exact finite verifier for FIRST_INCOHERENT_SIBLING_NESTED_TRIANGLE_BARRIER.md."""

from itertools import combinations
import random


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - \
           (b[1] - a[1]) * (c[0] - a[0])


def strict_inside_triangle(p, tri):
    signs = [orient(tri[i], tri[(i + 1) % 3], p) for i in range(3)]
    return all(s > 0 for s in signs) or all(s < 0 for s in signs)


def in_general_position(points):
    return all(orient(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))


def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def half(seq):
        out = []
        for p in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    lo = half(points)
    hi = half(reversed(points))
    return lo[:-1] + hi[:-1]


def convex_position(points):
    return len(points) <= 2 or len(convex_hull(points)) == len(points)


def nested_triangles(count, central):
    """Deterministic seeded exact-integer construction with strict nesting."""
    rng = random.Random(83820260815)
    triangles = []
    existing = list(central)
    for t in range(count):
        scale = 1000 ** (t + 2)
        for _ in range(10000):
            offsets = [rng.randrange(-10000, 10001) for _ in range(6)]
            tri = [(-scale + offsets[0], -scale + offsets[1]),
                   (scale + offsets[2], -scale + offsets[3]),
                   (offsets[4], scale + offsets[5])]
            if orient(*tri) < 0:
                tri[1], tri[2] = tri[2], tri[1]
            required = central if not triangles else triangles[-1]
            if not all(strict_inside_triangle(p, tri) for p in required):
                continue
            if not in_general_position(existing + tri):
                continue
            triangles.append(tuple(tri))
            existing.extend(tri)
            break
        else:
            raise RuntimeError("failed to find a generic containing triangle")
    return triangles


def main():
    # Four hull vertices and one genuine interior point: the construction
    # does not rely on the central child itself being in convex position.
    central = [(-3, -2), (3, -2), (4, 3), (-2, 4), (0, 1)]
    m = len(central)
    k = 3
    triangles = nested_triangles(m * k, central)
    points = central + [p for tri in triangles for p in tri]
    assert in_general_position(points)

    # Strict total nesting and containment of the whole central child.
    assert all(strict_inside_triangle(y, triangles[0]) for y in central)
    for inner, outer in zip(triangles, triangles[1:]):
        assert all(strict_inside_triangle(p, outer) for p in inner)
    assert all(all(strict_inside_triangle(y, tri) for y in central)
               for tri in triangles)

    # Index t=j*m+a.  For each j the circuit supports form a matching.
    records = []
    for j in range(k):
        supports = []
        for a, y in enumerate(central):
            t = j * m + a
            tri = triangles[t]
            assert strict_inside_triangle(y, tri)
            assert convex_position(tri)
            assert not convex_position([y, *tri])
            support = {("Y", a)} | {("T", t, z) for z in range(3)}
            supports.append(support)
            records.append((j, a, support))
        assert all(supports[a].isdisjoint(supports[b])
                   for a, b in combinations(range(m), 2))

    # Independent central indices give disjoint circuits; equal indices in
    # different partner classes share only their hidden singleton.
    for (j, a, s), (ell, b, t) in combinations(records, 2):
        if j == ell:
            continue
        expected = set() if a != b else {("Y", a)}
        assert s & t == expected

    # No two full releases coexist, and no nonempty central trace coexists
    # with a full release.  Exhaust the small central face complex exactly.
    for inner, outer in combinations(triangles, 2):
        assert not convex_position([*inner, *outer])
    central_faces = []
    for mask in range(1, 1 << m):
        face = [central[a] for a in range(m) if mask >> a & 1]
        if convex_position(face):
            central_faces.append(face)
            for tri in triangles:
                assert not convex_position([*face, *tri])

    # Released triangle labels recover (j,a) with load one.
    decoded = {tri: divmod(t, m) for t, tri in enumerate(triangles)}
    assert len(decoded) == k * m
    assert set(decoded.values()) == {(j, a) for j in range(k)
                                     for a in range(m)}

    print(
        "PASS: nested 1+3 array "
        f"central={m}, partners={k}, records={len(records)}, "
        f"central_faces={len(central_faces)}, released_load=1"
    )


if __name__ == "__main__":
    main()
