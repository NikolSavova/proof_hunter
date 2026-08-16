#!/usr/bin/env python3
"""Exact checks for ALMOST_FULL_WORD_MIXED_BANK_BARRIER.md."""

from fractions import Fraction as F
from itertools import combinations, product
from math import comb


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lo = []
    for p in points:
        while len(lo) >= 2 and orient(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    up = []
    for p in reversed(points):
        while len(up) >= 2 and orient(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def is_convex(points):
    return len(hull(points)) == len(set(points))


def role_cells():
    # Six roles, four labels per role.  The fourth raw label is interior to
    # the first three, so the local role order type is already non-Boolean.
    raw = [
        (F(-2), F(-1)),
        (F(2), F(-1)),
        (F(0), F(2)),
        (F(0), F(0)),
    ]
    eps = F(1, 10000)
    indices = [-3, -2, -1, 1, 2, 3]
    cells = []
    for idx, i in enumerate(indices):
        a = F(idx + 3, 100)
        b = F(2 * idx + 1, 100)
        cell = [
            (
                F(i) + eps * (rx + a * ry),
                F(i * i) + eps * (b * rx + ry),
            )
            for rx, ry in raw
        ]
        cells.append(cell)
    return cells


def central_child():
    # A six-point non-Boolean order type.  We choose the pair of maximum
    # ordinary-coface degree, then apply an exact affine map which sends it
    # to a short upward vertical segment near (1/101,-1).
    raw = [
        (F(-3), F(-1)),
        (F(3), F(-1)),
        (F(0), F(4)),
        (F(-1), F(0)),
        (F(1), F(0)),
        (F(0), F(1)),
    ]
    faces = []
    for mask in range(1 << len(raw)):
        face = frozenset(raw[j] for j in range(len(raw)) if mask >> j & 1)
        if is_convex(face):
            faces.append(face)
    degree, o0, p0 = max(
        (
            sum(frozenset((a, b)) <= face for face in faces),
            a,
            b,
        )
        for a, b in combinations(raw, 2)
    )

    dx, dy = p0[0] - o0[0], p0[1] - o0[1]
    den = dx * dx + dy * dy
    eta = F(1, 10000)
    x0 = F(1, 101)

    def transform(z):
        ux, uy = z[0] - o0[0], z[1] - o0[1]
        across = -dy * ux + dx * uy
        along = dx * ux + dy * uy
        return (x0 + eta * across / den, F(-1) + eta * along / den)

    image = list(map(transform, raw))
    o, p = transform(o0), transform(p0)
    image_faces = [frozenset(transform(z) for z in face) for face in faces]
    star = [face for face in image_faces if frozenset((o, p)) <= face]
    assert len(star) == degree
    return image, o, p, image_faces, star


def check_geometry():
    cells = role_cells()
    child, o, p, child_faces, star = central_child()
    role_points = [point for cell in cells for point in cell]
    all_points = role_points + child
    assert len(all_points) == len(set(all_points))
    assert all(orient(*triple) != 0 for triple in combinations(all_points, 3))

    # Each local role is non-Boolean but all one-per-role words are convex.
    assert all(len(hull(cell)) == 3 for cell in cells)
    words = list(product(*cells))
    assert len(words) == 4**6 == 4096
    assert all(is_convex(word) for word in words)

    # Exact child rank data and the pair-star averaging inequality.
    rank_vector = [sum(len(face) == r for face in child_faces) for r in range(7)]
    assert rank_vector == [1, 6, 15, 20, 3, 0, 0]
    assert len(child_faces) == 45
    assert len(star) == 7
    assert len(star) * comb(len(child), 2) >= len(child_faces) - len(child) - 1

    left = [point for cell in cells[:3] for point in cell]
    right = [point for cell in cells[3:] for point in cell]
    for a in left:
        for b in right:
            # The four-set has hull {o,a,b}; p is strictly hidden.
            assert not is_convex([o, p, a, b])
            assert p not in hull([o, p, a, b])

    # The same fixed circuit kills every pair-star face with any two-sided
    # partial transversal.  It suffices to test all singleton side choices;
    # adding further labels cannot make p extreme again.
    for face in star:
        for a in left:
            for b in right:
                assert not is_convex(list(face) + [a, b])
    return len(words), len(child_faces), len(star)


def check_masks():
    q, D = 6, 4
    full_words = D**q
    distinct_partial = (D + 1) ** q
    incidence_sum = 0
    for t in range(q + 1):
        count = comb(q, t) * D**t
        load = D ** (q - t)
        incidence_sum += count * load
        assert load == D ** (q - t)
    assert incidence_sum == full_words * 2**q
    assert distinct_partial == sum(comb(q, t) * D**t for t in range(q + 1))

    k = q // 2
    one_sided = 2 * (D + 1) ** k - 1
    assert one_sided == 249

    # Any support of rank >q/2 necessarily meets both three-role sides.
    for mask in range(1 << q):
        rank = mask.bit_count()
        if rank > k:
            assert (mask & ((1 << k) - 1)) != 0
            assert (mask >> k) != 0
    return full_words, distinct_partial, one_sided


if __name__ == "__main__":
    words, total_faces, star = check_geometry()
    full_words, partial, one_sided = check_masks()
    assert words == full_words
    print(
        f"PASS: {words} convex words, central pair-star {star}/{total_faces}, "
        f"all {star} two-sided profile unions bad, and exact mask loads "
        f"partial={partial} one_sided={one_sided}"
    )
