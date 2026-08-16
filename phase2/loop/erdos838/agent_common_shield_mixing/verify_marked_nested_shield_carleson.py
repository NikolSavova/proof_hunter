#!/usr/bin/env python3
"""Exact checks for MARKED_NESTED_SHIELD_CARLESON.md."""

from collections import Counter, defaultdict, deque
from fractions import Fraction as F
from itertools import combinations, product
from math import ceil, comb


def cross(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def convex(points):
    return len(points) == len(set(points)) == len(hull(points))


def all_face_indices(points):
    return [S for r in range(len(points) + 1)
            for S in combinations(range(len(points)), r)
            if convex([points[i] for i in S])]


def configuration():
    active = [
        [(F(-2), F(-2)), (F(-9, 5), F(-3, 2))],
        [(F(2), F(-2)), (F(17, 10), F(-9, 5))],
        [(F(2), F(2)), (F(9, 5), F(17, 10))],
        [(F(-2), F(2)), (F(-17, 10), F(9, 5))],
    ]
    repairs = [
        (F(0), F(-16, 7)),
        (F(-1, 295), F(-134, 59)),
        (F(1, 150), F(-34, 15)),
        (F(-3, 160), F(-9, 4)),
    ]
    return active, repairs


def check_geometry():
    active, repairs = configuration()
    points = sum(active, []) + repairs
    blocks = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4]
    assert all(cross(*triple) != 0 for triple in combinations(points, 3))

    completions = [tuple(active[i][bits[i]] for i in range(4))
                   for bits in product(range(2), repeat=4)]
    M, D = len(completions), len(repairs)
    assert (M, D) == (16, 4)
    assert all(convex(q) for q in completions)
    assert all(not convex(list(dict.fromkeys(q + r)))
               for q, r in combinations(completions, 2))

    stars = [q + (p,) for q in completions for p in repairs]
    assert len(stars) == len(set(stars)) == M * D == 64
    assert all(convex(s) for s in stars)
    assert all(all(x in s or not convex(s + (x,)) for x in points)
               for s in stars)
    assert all(not convex(tuple(dict.fromkeys(s + t)))
               for s, t in combinations(stars, 2))

    # Y realizes a nonconvex four-point order type: repair 1 is internal.
    assert not convex(repairs)
    others = [repairs[i] for i in (0, 2, 3)]
    signs = (cross(others[0], others[1], repairs[1]),
             cross(others[1], others[2], repairs[1]),
             cross(others[2], others[0], repairs[1]))
    assert all(x > 0 for x in signs) or all(x < 0 for x in signs)

    shield_faces = all_face_indices(repairs)
    assert len(shield_faces) == 15
    marked_bins = [(p, face) for face in shield_faces for p in face]
    assert len(marked_bins) == 28

    # Every marked shield bin occurs once for every completion, so retaining
    # the mark leaves exact overlap M.
    loads = Counter()
    for qi in range(M):
        for p, face in marked_bins:
            loads[p, face] += 1
            shield = tuple(repairs[i] for i in face)
            star = completions[qi] + (repairs[p],)
            if face != (p,):
                assert not convex(tuple(dict.fromkeys(star + shield)))
    assert len(loads) == 28
    assert set(loads.values()) == {M}
    assert sum(loads.values()) == M * 28 == 448

    profile = Counter()
    masks = Counter()
    faces_P = all_face_indices(points)
    for S in faces_P:
        profile[len(S)] += 1
        mask = 0
        for i in S:
            mask |= 1 << blocks[i]
        masks[mask] += 1
    expected = (1, 12, 66, 220, 318, 168, 0, 0, 0, 0, 0, 0, 0)
    assert tuple(profile[i] for i in range(13)) == expected
    assert len(faces_P) == 785
    assert masks[0b11111] == M * D == 64

    # Bad-four-circuit graph on the five blocks is connected.
    graph = defaultdict(set)
    for C in combinations(range(len(points)), 4):
        if convex([points[i] for i in C]):
            continue
        used = set(blocks[i] for i in C)
        for a, b in combinations(used, 2):
            graph[a].add(b)
            graph[b].add(a)
    seen = {0}
    queue = deque([0])
    while queue:
        a = queue.popleft()
        for b in graph[a] - seen:
            seen.add(b)
            queue.append(b)
    assert seen == set(range(5))

    # Unit-weight Carleson identity on the actual common-alphabet family.
    incidence = M * len(marked_bins)
    Lambda = M
    h = max(map(len, shield_faces))
    assert h == 3
    assert incidence == sum(loads.values())
    assert incidence <= Lambda * h * len(faces_P)
    # On the induced repair shield the exact number of marked bins is J=28.
    assert incidence == Lambda * len(marked_bins)
    return M, D, len(stars), len(shield_faces), len(marked_bins), incidence, len(faces_P)


def check_weighted_carleson():
    # Abstract nonuniform histories and subfamilies on actual shield faces.
    _, repairs = configuration()
    shield_faces = all_face_indices(repairs)
    bins = [(p, face) for face in shield_faces for p in face]
    histories = []
    for e in range(11):
        weight = F((e % 4) + 1, 3)
        family = [z for j, z in enumerate(bins) if (j + 2 * e) % 5 != 0]
        histories.append((weight, family))
    degrees = defaultdict(F)
    I = F(0)
    for weight, family in histories:
        I += weight * len(family)
        for z in family:
            degrees[z] += weight
    assert I == sum(degrees.values(), F(0))
    Lambda = max(degrees.values())
    h = 3
    # Here V can be replaced by the 15 induced shield faces.
    assert I <= Lambda * h * len(shield_faces)
    for T in (F(1), F(2), F(5)):
        tail = sum((d for d in degrees.values() if d >= T), F(0))
        second = sum((d * d for d in degrees.values()), F(0))
        assert tail <= second / T
    return len(histories), I, Lambda


def check_marked_collision_quadratic():
    # Finite exact enumeration of (13).  There are m marked bins and the
    # only geometric input is m<=hV.
    tests = 0
    for V in range(1, 7):
        for h in range(1, 5):
            for m in range(1, min(h * V, 5) + 1):
                for degrees in product(range(5), repeat=m):
                    I = sum(degrees)
                    if I == 0:
                        continue
                    collisions = sum(comb(d, 2) for d in degrees)
                    for good in range(collisions + 1):
                        L = ceil(F(good, V))
                        for theta in (F(1), F(1, 2), F(1, 3)):
                            for beta in range(3):
                                if F(good) < theta * collisions - beta * I:
                                    continue
                                x = F(I, V)
                                a = F(1) + F(2 * beta) / theta
                                assert x * x - h * a * x - F(2 * h * L) / theta <= 0
                                tests += 1
    return tests


def main():
    geometry = check_geometry()
    weighted = check_weighted_carleson()
    quadratics = check_marked_collision_quadratic()
    print(
        "marked nested shield: PASS; "
        f"geometry(M,D,stars,H,J,occ,V)={geometry}; "
        f"weighted(histories,I,Lambda)={weighted}; "
        f"collision_quadratics={quadratics}"
    )


if __name__ == "__main__":
    main()

