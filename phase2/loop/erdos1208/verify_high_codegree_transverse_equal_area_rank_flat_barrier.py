#!/usr/bin/env python3
"""Verify the literal high-codegree scalar/equal-area rank-flat barrier."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations

from verify_dilated_internal_pair_sum_charge import transformed_parabola_43
from verify_high_codegree_replacement_completion import add, tables


SELECTED_Q = [
    (-148, 14), (289, -27), (117, -11), (-741, 71), (1657, -159),
    (944, -90), (-29, 3), (-149, 15), (-18, 2), (139, -13),
    (-554, 54), (726, -70), (1340, -128), (-292, 28), (245, -23),
    (-517, 49), (-97, 9), (-88, 8), (1210, -116), (-772, 74),
    (-555, 53), (-526, 50), (100, -10), (-311, 29), (411, -39),
    (-178, 18), (555, -53), (160, -16), (-467, 45), (-308, 30),
    (445, -43), (-315, 31), (247, -23), (942, -90), (-20, 2),
    (843, -81), (-111, 11), (-398, 38), (-695, 67), (-694, 66),
    (-244, 24), (681, -65), (528, -50), (154, -14), (283, -27),
    (438, -42), (-328, 32), (-416, 40), (-49, 5),
]

CORE = [
    (1215871044, 38128236), (1239849372, 82124640),
    (1146504096, 33773772), (1098137052, 44496912),
    (1039113540, 41125476), (1016029236, 63236484),
    (838064676, -12985236), (985594116, 8639388),
    (888546996, 16974120), (780843408, 11214276),
    (901005708, 58639644), (720956748, 19606536),
    (819806112, 38842752), (618444216, -28379508),
    (700582908, 30752028), (665397996, -2463708),
    (487701396, -38801112), (644537820, 56299392),
    (633018204, 53968512), (610842120, 37543056),
    (526977132, 1938912), (590155248, 35577000),
    (540612024, 44952288), (531444768, 45317112),
    (460588608, 26503248), (434710680, 66763392),
    (342541584, 19760376), (244318284, 26747256),
    (369358608, 18834876), (249822372, -2367396),
    (226296804, 40588452), (217302852, -19775880),
    (121431912, -10093296), (253426860, 52774500),
    (-8313516, 583392), (89225424, -14390232),
    (138218532, 1109724), (-6332484, 8403900),
    (21347688, -4285296), (-3622020, -2561616),
    (-1691544, -8947056), (-1378512, 4164492),
    (-11721948, 3181464),
]

EXTRA = [
    (18209765733449837023, 59480478233554644551),
    (18216024718535674524, 59841218603479725328),
    (18212895225992755772, 59581744478939231956),
    (18216024718535674526, 59841218603479725328),
    (18212895225992755776, 59581744478939231956),
]


def sub(left, right):
    return left[0] - right[0], left[1] - right[1]


def norm2(vector):
    return vector[0] * vector[0] + vector[1] * vector[1]


def det(left, right):
    return left[0] * right[1] - left[1] * right[0]


def sum_many(*points):
    answer = (0, 0)
    for point in points:
        answer = add(answer, point)
    return answer


def exact_rank(rows):
    basis = {}
    for raw_row in rows:
        row = [Fraction(value) for value in raw_row]
        for pivot, old_row in sorted(basis.items()):
            if row[pivot]:
                factor = row[pivot]
                row = [x - factor * y for x, y in zip(row, old_row)]
        pivot = next((index for index, value in enumerate(row) if value), None)
        if pivot is None:
            continue
        factor = row[pivot]
        row = [value / factor for value in row]
        for old_pivot, old_row in list(basis.items()):
            if old_row[pivot]:
                factor = old_row[pivot]
                basis[old_pivot] = [
                    x - factor * y for x, y in zip(old_row, row)
                ]
        basis[pivot] = row
    return len(basis)


# Translate into a nonnegative box.  Translation preserves every difference,
# clean-row identity, distance, and triangle area.
RAW_POINTS = CORE + EXTRA
shift = (-min(x for x, _ in RAW_POINTS), -min(y for _, y in RAW_POINTS))
POINTS = [add(point, shift) for point in RAW_POINTS]
k = len(POINTS)
assert len(CORE) == 43 and len(EXTRA) == 5 and k == 48
assert len(set(POINTS)) == k
assert min(x for x, _ in POINTS) == min(y for _, y in POINTS) == 0
m = max(max(point) for point in POINTS)

# Recover the 43-label incidence template and its rank-flat rows.
template = transformed_parabola_43()
template_sum_edge, _, template_anchor = tables(template)
template_s = add(template[0], template[37])
template_t = add(template[5], template[39])
relation_rows = []
for q in SELECTED_Q:
    anchor_head, anchor_tail = template_anchor[q]
    for start in (template_s, template_t):
        source = template_sum_edge[start]
        target = template_sum_edge[add(start, q)]
        row = [0] * 43
        for endpoint in (anchor_head, *source):
            row[endpoint] += 1
        for endpoint in (anchor_tail, *target):
            row[endpoint] -= 1
        relation_rows.append(row)
        for coordinate in (0, 1):
            assert sum(
                row[index] * CORE[index][coordinate] for index in range(43)
            ) == 0

assert len(SELECTED_Q) == 49
assert len(relation_rows) == 98
assert exact_rank(relation_rows) == 36

# Global distance and pair-sum Sidonicity.
SUM_EDGE = {}
DIST_EDGE = {}
for edge in combinations(range(k), 2):
    first, second = edge
    pair_sum = add(POINTS[first], POINTS[second])
    distance = norm2(sub(POINTS[first], POINTS[second]))
    assert pair_sum not in SUM_EDGE
    assert distance > 0 and distance not in DIST_EDGE
    SUM_EDGE[pair_sum] = edge
    DIST_EDGE[distance] = edge

assert len(SUM_EDGE) == len(DIST_EDGE) == 1128

DIFF_EDGE = {}
for first in range(k):
    for second in range(k):
        if first == second:
            continue
        difference = sub(POINTS[first], POINTS[second])
        assert difference not in DIFF_EDGE
        DIFF_EDGE[difference] = (first, second)


def clean(q, start):
    source = SUM_EDGE.get(start)
    target = SUM_EDGE.get(add(start, q))
    anchor = DIFF_EDGE.get(q)
    return (
        source is not None
        and target is not None
        and anchor is not None
        and len(set(source + target + anchor)) == 6
    )


def fibre(q):
    return {start for start in SUM_EDGE if clean(q, start)}


source_s = add(POINTS[0], POINTS[37])
source_t = add(POINTS[5], POINTS[39])
Q_p = [q for q in DIFF_EDGE if clean(q, source_s) and clean(q, source_t)]

new_q = {
    old_q: sub(
        POINTS[template_anchor[old_q][0]],
        POINTS[template_anchor[old_q][1]],
    )
    for old_q in SELECTED_Q
}
assert len(set(new_q.values())) == 49
assert set(Q_p) == set(new_q.values())
assert len(Q_p) == 49 >= k

# Verify the two-translation four-sum identities with all q/r endpoint data.
target_s = {
    old_q: SUM_EDGE[add(source_s, new_q[old_q])] for old_q in SELECTED_Q
}
target_t = {
    old_q: SUM_EDGE[add(source_t, new_q[old_q])] for old_q in SELECTED_Q
}
for old_q, old_r in combinations(SELECTED_Q, 2):
    q, r = new_q[old_q], new_q[old_r]
    Aq, Bq = DIFF_EDGE[q]
    Ar, Br = DIFF_EDGE[r]
    Eq, Fq = target_s[old_q]
    Er, Fr = target_s[old_r]
    Iq, Jq = target_t[old_q]
    Ir, Jr = target_t[old_r]
    assert sub(add(POINTS[Eq], POINTS[Fq]), add(POINTS[Er], POINTS[Fr])) == sub(q, r)
    assert sub(add(POINTS[Iq], POINTS[Jq]), add(POINTS[Ir], POINTS[Jr])) == sub(q, r)
    assert sum_many(POINTS[Eq], POINTS[Fq], POINTS[Ir], POINTS[Jr]) == sum_many(
        POINTS[Er], POINTS[Fr], POINTS[Iq], POINTS[Jq]
    )
    assert sum_many(POINTS[Eq], POINTS[Fq], POINTS[Bq], POINTS[Ar]) == sum_many(
        POINTS[Er], POINTS[Fr], POINTS[Aq], POINTS[Br]
    )

# Literal one-role base.  The template identifiers merely name its two
# endpoint patterns; new_q retains the actual deformed anchor differences.
base_q1_old = (100, -10)
base_q2_old = (-694, 66)
base_q1 = new_q[base_q1_old]
base_q2 = new_q[base_q2_old]
assert (len(fibre(base_q1)), len(fibre(base_q2))) == (42, 40)

first_edges = {old_q: set(target_s[old_q]) for old_q in SELECTED_Q}
second_edges = {old_q: set(target_t[old_q]) for old_q in SELECTED_Q}
assert not (first_edges[base_q1_old] & first_edges[base_q2_old])
assert second_edges[base_q1_old] & second_edges[base_q2_old]

good_edges = second_edges
bad_edges = first_edges
base_anchor_union = set(
    template_anchor[base_q1_old] + template_anchor[base_q2_old]
)
good_union = good_edges[base_q1_old] | good_edges[base_q2_old]
bad_union = bad_edges[base_q1_old] | bad_edges[base_q2_old]
transverse = [
    old_q
    for old_q in SELECTED_Q
    if not (
        set(template_anchor[old_q]) & base_anchor_union
        or good_edges[old_q] & good_union
        or bad_edges[old_q] & bad_union
    )
]
assert len(transverse) == 36

# Exhaustive six-distinct geometric equal-area energy.
triangles_by_area = defaultdict(list)
area_pairs = []
triangle_count = 0
for triangle in combinations(range(k), 3):
    first, second, third = triangle
    doubled_area = abs(
        det(
            sub(POINTS[second], POINTS[first]),
            sub(POINTS[third], POINTS[first]),
        )
    )
    assert doubled_area != 0
    triangle_count += 1
    for old_triangle in triangles_by_area[doubled_area]:
        if not (set(triangle) & set(old_triangle)):
            area_pairs.append((old_triangle, triangle, doubled_area))
    triangles_by_area[doubled_area].append(triangle)

assert triangle_count == 17296
assert len(area_pairs) == 24
assert all(max(first + second) < 43 for first, second, _ in area_pairs)
assert 18 * len(area_pairs) == 432  # equal-signed ordered energy

# Scalar source gap and both determinant-qualified wedge orientations.
source_gap = norm2(sub(POINTS[37], POINTS[0])) - norm2(
    sub(POINTS[39], POINTS[5])
)
assert source_gap == 450646926180300144
assert source_gap % 18 == 0
metric_gap = -source_gap // 18
N = len(SUM_EDGE)
cutoff = max(N // len(fibre(base_q1)), N // len(fibre(base_q2)))
assert (metric_gap, N, cutoff) == (-25035940343350008, 1128, 28)

EDGE_BY_NORM = {
    norm2(sub(POINTS[second], POINTS[first])): (
        first,
        second,
        sub(POINTS[second], POINTS[first]),
    )
    for first, second in combinations(range(k), 2)
}


def metric_representations(gap):
    output = []
    for first_norm, (a, b, u) in EDGE_BY_NORM.items():
        partner = EDGE_BY_NORM.get(first_norm - gap)
        if partner is None:
            continue
        c, d, v = partner
        doubled_determinant = 2 * det(u, v)
        if abs(doubled_determinant) > cutoff:
            output.append(((a, b), (c, d), doubled_determinant))
    return output


negative_representations = metric_representations(metric_gap)
positive_representations = metric_representations(-metric_gap)
assert negative_representations == [
    ((43, 44), (43, 46), -1442961479700323108),
    ((43, 45), (43, 47), -810129963076699240),
]
assert positive_representations == [
    ((43, 46), (43, 44), 1442961479700323108),
    ((43, 47), (43, 45), 810129963076699240),
]


def wedge_count(representations):
    degrees = Counter()
    for first_edge, _, _ in representations:
        degrees.update(first_edge)
    return sum(degree * (degree - 1) // 2 for degree in degrees.values())


assert wedge_count(negative_representations) == 1
assert wedge_count(positive_representations) == 1

# Individual and pairwise local exposure of the 24 global area pairs.
metric_endpoints = set(range(43, 48))
source_endpoints = {0, 37, 5, 39}
base_endpoints = source_endpoints | metric_endpoints | base_anchor_union
for old_q in (base_q1_old, base_q2_old):
    base_endpoints |= first_edges[old_q] | second_edges[old_q]


def exposed_count(old_translations):
    endpoints = set(base_endpoints)
    for old_q in old_translations:
        endpoints |= set(template_anchor[old_q])
        endpoints |= first_edges[old_q] | second_edges[old_q]
    return sum(
        set(first + second) <= endpoints for first, second, _ in area_pairs
    )


single_profile = Counter(exposed_count([old_q]) for old_q in transverse)
pair_profile = Counter(
    exposed_count([old_q, old_r]) for old_q, old_r in combinations(transverse, 2)
)
assert single_profile == {0: 31, 1: 5}
assert pair_profile == {0: 404, 1: 153, 2: 55, 3: 16, 4: 2}

print(
    "PASS",
    {
        "k": k,
        "N": N,
        "m": m,
        "relation_rank": exact_rank(relation_rows),
        "codegree": len(Q_p),
        "base_fibres": (len(fibre(base_q1)), len(fibre(base_q2))),
        "transverse": len(transverse),
        "metric_gap": metric_gap,
        "cutoff": cutoff,
        "weights": (
            wedge_count(negative_representations),
            wedge_count(positive_representations),
        ),
        "geometric_area_pairs": len(area_pairs),
        "ordered_area_energy": 18 * len(area_pairs),
        "single_exposure": dict(single_profile),
        "pair_exposure": dict(pair_profile),
    },
)
