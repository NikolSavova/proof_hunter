#!/usr/bin/env python3
"""Exact rational check for HIGH_TRANSVERSAL_COMMON_POCKET_ENDPOINT_PRODUCT."""

from fractions import Fraction as F
from itertools import combinations, product


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
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


def is_face(points):
    return len(points) == len(set(points)) and len(hull(points)) == len(points)


def strict_inside(p, tri):
    signs = [orient(tri[i], tri[(i + 1) % 3], p) for i in range(3)]
    return all(s > 0 for s in signs) or all(s < 0 for s in signs)


# Canonical ear over (-100,0)--(100,0), exterior above the edge.
U = (F(-100), F(0))
V = (F(100), F(0))
TRIS = [
    ((F(-50), F(100)), (F(0), F(150)), (F(50), F(100))),
    ((F(-55), F(94)), (F(2), F(146)), (F(56), F(96))),
    ((F(-44), F(106)), (F(-2), F(153)), (F(46), F(104))),
]
SOURCES = [(F(-2), F(119)), (F(0), F(121)), (F(2), F(120))]


def top(p):
    return (p[0], p[1] + F(300))


def bottom(p):
    # Orientation-preserving half-turn plus a generic rational shear.
    return (-p[0] + p[1] / F(997), -F(300) - p[1])


BASE = [(F(-100), F(-300)), (F(100), F(-300)),
        (F(100), F(300)), (F(-100), F(300))]

roles = []
for mapping in (top, bottom):
    roles.append({
        "sources": [mapping(p) for p in SOURCES],
        "tris": [tuple(mapping(p) for p in tri) for tri in TRIS],
    })

# A labelled infinitesimal rational perturbation removes accidental
# collinearities between different ear alternatives.  All hypotheses below
# are strict and are rechecked after the perturbation.
eps = F(1, 10**12)
tag = 1
for role in roles:
    fresh_sources = []
    for x, y in role["sources"]:
        fresh_sources.append((x + eps * tag**2, y + eps * tag**3))
        tag += 1
    role["sources"] = fresh_sources
    fresh_tris = []
    for tri in role["tris"]:
        fresh_tri = []
        for x, y in tri:
            fresh_tri.append((x + eps * tag**2, y + eps * tag**3))
            tag += 1
        fresh_tris.append(tuple(fresh_tri))
    role["tris"] = fresh_tris


all_points = BASE[:]
for role in roles:
    all_points.extend(role["sources"])
    for tri in role["tris"]:
        all_points.extend(tri)

assert len(all_points) == 28
assert len(set(all_points)) == 28

# Exact general position.
for a, b, c in combinations(all_points, 3):
    assert orient(a, b, c) != 0

# Local hypotheses: every source is strictly inside every target triangle,
# and each singleton/triangle is an admissible ear with the carrier.
for ridx, role in enumerate(roles):
    edge = [top(U), top(V)] if ridx == 0 else [bottom(U), bottom(V)]
    for x in role["sources"]:
        assert is_face(edge + [x])
        for tri in role["tris"]:
            assert strict_inside(x, tri)
    for tri in role["tris"]:
        assert is_face(edge + list(tri))

# Every full source word and every full target word is ordinary.
source_words = {}
target_words = {}
for a0, a1 in product(range(3), repeat=2):
    word = BASE + [roles[0]["sources"][a0], roles[1]["sources"][a1]]
    assert is_face(word)
    source_words[(a0, a1)] = tuple(word)

for b0, b1 in product(range(3), repeat=2):
    word = BASE + list(roles[0]["tris"][b0]) + list(roles[1]["tris"][b1])
    assert is_face(word)
    target_words[(b0, b1)] = tuple(word)

# All 81 records are bad, with a literal hidden singleton in both roles.
bad_records = 0
for avec, bvec in product(source_words, target_words):
    union = list(dict.fromkeys(source_words[avec] + target_words[bvec]))
    assert not is_face(union)
    for i in range(2):
        assert strict_inside(roles[i]["sources"][avec[i]], roles[i]["tris"][bvec[i]])
    bad_records += 1
assert bad_records == 3 ** 4

# The released traces are physically disjoint.  At either chronology level
# every one of the three traces has record load 3^3, hence h=3.
trace_vertices = []
for role in roles:
    for tri in role["tris"]:
        trace_vertices.extend(tri)
assert len(trace_vertices) == len(set(trace_vertices)) == 18

stage_mass = 3 ** 4
trace_load = 3 ** 3
dispersions = []
for _ in range(2):
    dispersions.append(stage_mass // trace_load)
    stage_mass //= 3
    trace_load //= 3
assert dispersions == [3, 3]

# Complete crossed left-endpoint x right-endpoint product.  The output
# itself recovers both label words, hence decoder load one.
bank = {}
for left_word in product(range(3), repeat=2):
    for right_word in product(range(3), repeat=2):
        out = BASE[:]
        for i in range(2):
            out.append(roles[i]["tris"][left_word[i]][0])
            out.append(roles[i]["tris"][right_word[i]][2])
        assert is_face(out)
        key = frozenset(out)
        assert key not in bank
        bank[key] = (left_word, right_word)

assert len(bank) == 3 ** 4 == bad_records

# The stronger source-primitive bank uses the actual hidden source mark and
# only one triangle endpoint.  It directly recovers the original record.
mixed_bank = {}
for source_word in product(range(3), repeat=2):
    for target_word in product(range(3), repeat=2):
        out = BASE[:]
        for i in range(2):
            out.append(roles[i]["sources"][source_word[i]])
            out.append(roles[i]["tris"][target_word[i]][0])
        assert is_face(out)
        key = frozenset(out)
        assert key not in mixed_bank
        mixed_bank[key] = (source_word, target_word)
assert len(mixed_bank) == bad_records

# Root-retaining endpoint modules: for every physical source mark, choose
# the left endpoint of one containing triangle and the right endpoint of a
# second.  Tangent dominance through the common source makes all 3^6 global
# choices ordinary.
rooted_module_bank = {}
for source_word in product(range(3), repeat=2):
    for left_word in product(range(3), repeat=2):
        for right_word in product(range(3), repeat=2):
            out = BASE[:]
            for i in range(2):
                out.append(roles[i]["tris"][left_word[i]][0])
                out.append(roles[i]["sources"][source_word[i]])
                out.append(roles[i]["tris"][right_word[i]][2])
            assert is_face(out)
            key = frozenset(out)
            assert key not in rooted_module_bank
            rooted_module_bank[key] = (source_word, left_word, right_word)
assert len(rooted_module_bank) == 3 ** 6

# Context-retaining Hall form at equality m_K=b_K^2.  The two physical
# marked gaps are recovered from their disjoint local endpoint grounds, so
# the global output load is one even though both contexts retain BASE.
context_bank = {}
for i in range(2):
    for source_name in range(3):
        for target_name in range(3):
            out = BASE + [
                roles[i]["tris"][source_name][0],
                roles[i]["tris"][target_name][2],
            ]
            assert is_face(out)
            key = frozenset(out)
            assert key not in context_bank
            context_bank[key] = (i, source_name, target_name)
assert len(context_bank) == 2 * 3**2

mixed_context_bank = {}
for i in range(2):
    for source_name in range(3):
        for target_name in range(3):
            out = BASE + [
                roles[i]["sources"][source_name],
                roles[i]["tris"][target_name][0],
            ]
            assert is_face(out)
            key = frozenset(out)
            assert key not in mixed_context_bank
            mixed_context_bank[key] = (i, source_name, target_name)
assert len(mixed_context_bank) == 2 * 3**2

rooted_context_bank = {}
for i in range(2):
    for source_name in range(3):
        for left_name in range(3):
            for right_name in range(3):
                out = BASE + [
                    roles[i]["tris"][left_name][0],
                    roles[i]["sources"][source_name],
                    roles[i]["tris"][right_name][2],
                ]
                assert is_face(out)
                key = frozenset(out)
                assert key not in rooted_context_bank
                rooted_context_bank[key] = (
                    i,
                    source_name,
                    left_name,
                    right_name,
                )
assert len(rooted_context_bank) == 2 * 3**3

print(
    "PASS: diffuse disjoint-triangle roots have exact common-pocket "
    "endpoint product; records=%d, endpoint_bank=%d, mixed_bank=%d, "
    "rooted_bank=%d, context_banks=(%d,%d,%d), "
    "dispersions=%s, points=%d"
    % (
        bad_records,
        len(bank),
        len(mixed_bank),
        len(rooted_module_bank),
        len(context_bank),
        len(mixed_context_bank),
        len(rooted_context_bank),
        dispersions,
        len(all_points),
    )
)
