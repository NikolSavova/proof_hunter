#!/usr/bin/env python3
"""Exact verifier for AMPLIFIED_TRANSVERSE_EQUAL_AREA_LOCAL_BRIDGE_BARRIER."""

from itertools import combinations


NAMES = (
    "S0 S1 T0 T1 x y z a b c d e f h i "
    "q1- q1+ q2- q2+ q0- q0+ M F1 P1a P1b F2 P2a P2b"
).split()

P = [
    (5066175, 12543305),
    (5069774, 12543343),
    (172515716, 98890592),
    (172519314, 98890629),
    (127510935, 99195760),
    (72339642, 163547160),
    (124703786, 121942283),
    (134857354, 41950986),
    (452256448, 351881630),
    (109296628, 189238304),
    (422645881, 268945712),
    (84732168, 4927769),
    (95359612, 140773953),
    (108740371, 61287538),
    (406250490, 257108757),
    (53567035, 165099095),
    (295645807, 361150490),
    (128005176, 52850030),
    (314912655, 313252825),
    (148192748, 86448880),
    (318148579, 207063954),
    (90887075, 154849249),
    (90887175, 154849650),
    (65451055, 0),
    (65451157, 401),
    (90887175, 154849856),
    (0, 171742885),
    (102, 171743492),
]


def add(u, v):
    return (u[0] + v[0], u[1] + v[1])


def sub(u, v):
    return (u[0] - v[0], u[1] - v[1])


def norm2(u):
    return u[0] * u[0] + u[1] * u[1]


def det(u, v):
    return u[0] * v[1] - u[1] * v[0]


def area(a, b, c):
    return det(sub(b, a), sub(c, a))


def sum_many(*points):
    out = (0, 0)
    for point in points:
        out = add(out, point)
    return out


assert len(NAMES) == len(P) == 28
assert len(set(P)) == 28
assert min(x for x, _ in P) == min(y for _, y in P) == 0
m = max(max(x, y) for x, y in P)
assert m == 452256448

# Global pair-sum and distance Sidonicity.
SUM_EDGE = {}
DIST_EDGE = {}
for edge in combinations(range(len(P)), 2):
    i, j = edge
    pair_sum = add(P[i], P[j])
    distance = norm2(sub(P[i], P[j]))
    assert pair_sum not in SUM_EDGE
    assert distance > 0 and distance not in DIST_EDGE
    SUM_EDGE[pair_sum] = edge
    DIST_EDGE[distance] = edge

assert len(SUM_EDGE) == len(DIST_EDGE) == 378

# Every nonzero directed difference has its unique ordered anchor.
DIFF_EDGE = {}
for i in range(len(P)):
    for j in range(len(P)):
        if i == j:
            continue
        difference = sub(P[i], P[j])
        assert difference not in DIFF_EDGE
        DIFF_EDGE[difference] = (i, j)


def H(q):
    """Clean starts for the oriented anchor difference q."""
    anchor = DIFF_EDGE[q]
    out = set()
    for start, edge_1 in SUM_EDGE.items():
        edge_2 = SUM_EDGE.get(add(start, q))
        if edge_2 is not None and len(set(anchor + edge_1 + edge_2)) == 6:
            out.add(start)
    return out


def edge_names(pair_sum):
    return {NAMES[j] for j in SUM_EDGE[pair_sum]}


s = add(P[0], P[1])
t = add(P[2], P[3])
q1 = sub(P[16], P[15])
q2 = sub(P[18], P[17])
q0 = sub(P[20], P[19])
g = sub(q2, q1)

assert q1 == sub(add(P[4], P[6]), s) == sub(add(P[7], P[8]), t)
assert q2 == sub(add(P[5], P[6]), s) == sub(add(P[9], P[10]), t)
assert q0 == sub(add(P[11], P[12]), s) == sub(add(P[13], P[14]), t)
assert g == sub(P[5], P[4]) == sub(add(P[9], P[10]), add(P[7], P[8]))

assert edge_names(add(s, q1)) == {"x", "z"}
assert edge_names(add(s, q2)) == {"y", "z"}
assert edge_names(add(t, q1)) == {"a", "b"}
assert edge_names(add(t, q2)) == {"c", "d"}
assert edge_names(add(s, q0)) == {"e", "f"}
assert edge_names(add(t, q0)) == {"h", "i"}

# All six planted rows are clean, and the source pair has exactly three
# common clean translations in the entire 28-point set.
for q in (q1, q2, q0):
    assert s in H(q) and t in H(q)

Q_p = [q for q in DIFF_EDGE if s in H(q) and t in H(q)]
assert set(Q_p) == {q1, q2, q0}
assert (len(H(q1)), len(H(q2)), len(H(q0))) == (3, 3, 2)

# One-role base and exact full transversality of q0.
good_1 = set(SUM_EDGE[add(s, q1)])
good_2 = set(SUM_EDGE[add(s, q2)])
bad_1 = set(SUM_EDGE[add(t, q1)])
bad_2 = set(SUM_EDGE[add(t, q2)])
good_0 = set(SUM_EDGE[add(s, q0)])
bad_0 = set(SUM_EDGE[add(t, q0)])
anchor_1 = set(DIFF_EDGE[q1])
anchor_2 = set(DIFF_EDGE[q2])
anchor_0 = set(DIFF_EDGE[q0])

assert len(good_1 & good_2) == 1
assert not (bad_1 & bad_2)
assert not (anchor_0 & (anchor_1 | anchor_2))
assert not (good_0 & (good_1 | good_2))
assert not (bad_0 & (bad_1 | bad_2))

# Literal reverse-switch record: v is in the good star P_g, w is in the
# clean part H_g of B_g, and both backward starts lie in both base fibres.
v_base = add(s, q1)
w_base = add(t, q1)
assert g in DIFF_EDGE
assert set(SUM_EDGE[v_base]) & set(SUM_EDGE[add(v_base, g)])
assert not (set(SUM_EDGE[w_base]) & set(SUM_EDGE[add(w_base, g)]))
assert w_base in H(g)
assert sub(v_base, q1) in H(q1) & H(add(q1, g))
assert sub(w_base, q1) in H(q1) & H(add(q1, g))

# The exact q/q0-preserving equal-centroid and four-sum identities.
assert sum_many(P[4], P[9], P[10]) == sum_many(P[5], P[7], P[8])
assert sum_many(P[11], P[12], P[7], P[8]) == sum_many(P[4], P[6], P[13], P[14])
assert sub(add(P[11], P[12]), add(P[4], P[6])) == sub(q0, q1)
assert sub(add(P[13], P[14]), add(P[7], P[8])) == sub(q0, q1)
assert sub(s, t) == sub(add(P[4], P[6]), add(P[7], P[8]))
assert sub(s, t) == sub(add(P[11], P[12]), add(P[13], P[14]))

# Every clean incidence has the canonical equal-centroid lift and satisfies
# the exact signed area-defect formula (2.9).  None has zero defect.
for q in (q1, q2, q0):
    A, B = DIFF_EDGE[q]
    for start in (s, t):
        C, D = SUM_EDGE[start]
        E, F = SUM_EDGE[add(start, q)]
        assert sum_many(P[A], P[C], P[D]) == sum_many(P[B], P[E], P[F])
        u = sub(P[C], P[D])
        v = sub(P[E], P[F])
        twice_defect = det(u, sub(start, add(P[A], P[A]))) - det(
            v, sub(add(start, q), add(P[B], P[B]))
        )
        defect = area(P[A], P[C], P[D]) - area(P[B], P[E], P[F])
        assert twice_defect == 2 * defect
        assert defect != 0

# Scalar weight: source gap 7272 gives r=-404.  At L=N/|H_q1|=126
# there are exactly two high-determinant representations, and their first
# endpoint edges make exactly one wedge.
source_gap = norm2(sub(P[1], P[0])) - norm2(sub(P[3], P[2]))
assert source_gap == 7272 and source_gap % 18 == 0
r = -source_gap // 18
N = len(SUM_EDGE)
L = N // len(H(q1))
assert (r, N, L) == (-404, 378, 126)

EDGE_BY_NORM = {
    norm2(sub(P[j], P[i])): (i, j, sub(P[j], P[i]))
    for i, j in combinations(range(len(P)), 2)
}
representations = []
for first_norm, (i, j, u) in EDGE_BY_NORM.items():
    partner = EDGE_BY_NORM.get(first_norm - r)
    if partner is None:
        continue
    i2, j2, v = partner
    doubled_det = 2 * det(u, v)
    if abs(doubled_det) > L:
        representations.append(((i, j), (i2, j2), doubled_det))

assert representations == [
    ((21, 22), (23, 24), -1604),
    ((21, 25), (26, 27), -2428),
]
degrees = {}
for first, _, _ in representations:
    for endpoint in first:
        degrees[endpoint] = degrees.get(endpoint, 0) + 1
W = sum(degree * (degree - 1) // 2 for degree in degrees.values())
assert W == 1

# Exhaustively check that every triangle is noncollinear and that no two
# triangles with six distinct endpoints have the same nonzero absolute area.
triangles_by_area = {}
triangle_count = 0
six_distinct_equal_area_pairs = 0
for triangle in combinations(range(len(P)), 3):
    doubled_area = abs(area(P[triangle[0]], P[triangle[1]], P[triangle[2]]))
    assert doubled_area != 0
    triangle_count += 1
    for previous in triangles_by_area.get(doubled_area, []):
        if not (set(triangle) & set(previous)):
            six_distinct_equal_area_pairs += 1
    triangles_by_area.setdefault(doubled_area, []).append(triangle)

assert triangle_count == 3276
assert six_distinct_equal_area_pairs == 0

print(
    "PASS",
    {
        "k": len(P),
        "N": N,
        "m": m,
        "Q_p": len(Q_p),
        "fibre_sizes": (len(H(q1)), len(H(q2)), len(H(q0))),
        "source_gap": source_gap,
        "target_gap": r,
        "cutoff": L,
        "target_representations": len(representations),
        "scalar_wedge_weight": W,
        "triangles": triangle_count,
        "six_distinct_equal_area_pairs": six_distinct_equal_area_pairs,
    },
)
