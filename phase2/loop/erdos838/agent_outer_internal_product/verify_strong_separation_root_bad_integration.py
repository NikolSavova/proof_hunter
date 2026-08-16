#!/usr/bin/env python3
"""Exact checks for STRONG_SEPARATION_ROOT_BAD_INTEGRATION_AUDIT.md."""

from fractions import Fraction as F
from itertools import combinations, product
from math import prod


def orient(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def convex_hull(points):
    """Andrew monotone chain; exact rational arithmetic."""
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

    return half(pts)[:-1] + half(reversed(pts))[:-1]


def signature(word):
    return tuple(1 if orient(word[i], word[j], word[k]) > 0 else -1
                 for i, j, k in combinations(range(len(word)), 3))


# Section 2: all singleton transversals convex, but their type changes.
p = (F(2), F(-2))
q = (F(-3), F(2))
a = (F(0), F(0))
b = (F(4), F(0))
c = (F(0), F(4))
all_five = [p, q, a, b, c]
for triple in combinations(all_five, 3):
    assert orient(*triple) != 0
assert len(convex_hull([p, a, b, c])) == 4
assert len(convex_hull([q, a, b, c])) == 4
assert orient(p, a, b) == -8
assert orient(q, a, b) == 8
assert signature([p, a, b, c]) != signature([q, a, b, c])


# Section 3: same fixed cyclic type, but a two-point local face is not an
# arbitrary endpoint profile after the adjacent fourth role is omitted.
u = (F(2), F(-2))
v = (F(2), F(-1))
b = (F(4), F(0))
c = (F(0), F(4))
a = (F(0), F(0))
all_five = [u, v, b, c, a]
for triple in combinations(all_five, 3):
    assert orient(*triple) != 0
words = [[x, b, c, a] for x in (u, v)]
assert all(len(convex_hull(w)) == 4 for w in words)
assert signature(words[0]) == signature(words[1]) == (1, 1, 1, 1)

# v = 3/4 u + 1/8 b + 1/8 c, so {u,v,b,c} is nonconvex.
weights = (F(3, 4), F(1, 8), F(1, 8))
rhs = tuple(weights[0] * u[j] + weights[1] * b[j] + weights[2] * c[j]
            for j in range(2))
assert sum(weights) == 1 and all(x > 0 for x in weights)
assert rhs == v
assert len(convex_hull([u, v, b, c])) == 3


# Section 3.1: scalable same-type support whose two omitted-gap endpoint
# profile families are both too small to factor its full local reservoir.
m = 14
delta = F(1, 100 * m * m)
curve = [(F(2) - delta * t * t, -F(1, 5) + delta * t)
         for t in range(1, m + 1)]
b = (F(4), F(0))
c = (F(0), F(4))
a = (F(0), F(0))

# Every singleton transversal has the positive cyclic type.
curve_words = [[x, b, c, a] for x in curve]
assert all(len(convex_hull(word)) == 4 for word in curve_words)
assert all(signature(word) == (1, 1, 1, 1) for word in curve_words)

# The curve is in convex position, so all 2^m-1 nonempty subsets are local
# faces.  The complete ambient configuration is in general position.
assert len(convex_hull(curve)) == m
ambient = curve + [b, c, a]
assert all(orient(*triple) != 0 for triple in combinations(ambient, 3))
local_faces = (1 << m) - 1

# Every middle curve point is strictly inside the triangle made by the
# two outer curve points and c.  Check both the closed formula and the
# exact barycentric signs for all C(m,3) triples.
for i0, j0, k0 in combinations(range(m), 3):
    i, j, k = i0 + 1, j0 + 1, k0 + 1
    pi, pj, pk = curve[i0], curve[j0], curve[k0]
    denominator = orient(pi, pk, c)
    formula_d = delta * (k - i) * (
        F(2) - F(21, 5) * (i + k) + delta * i * k
    )
    numerator_c = orient(pi, pk, pj)
    formula_n = delta * delta * (k - i) * (j - i) * (j - k)
    assert denominator == formula_d < 0
    assert numerator_c == formula_n < 0
    lambdas = (
        orient(pj, pk, c) / denominator,
        orient(pi, pj, c) / denominator,
        numerator_c / denominator,
    )
    assert all(x > 0 for x in lambdas)
    assert sum(lambdas) == 1
    reconstructed = tuple(
        lambdas[0] * pi[d] + lambdas[1] * pk[d] + lambdas[2] * c[d]
        for d in range(2)
    )
    assert reconstructed == pj

# Exhaust all local traces.  Anything of rank >=3 is nonconvex with c;
# hence both adjacent omitted-gap profile alphabets have rank at most 2.
safe_bc = []
safe_ca = []
for mask in range(1, 1 << m):
    trace = [curve[i] for i in range(m) if mask >> i & 1]
    assert len(convex_hull(trace)) == len(trace)
    if len(convex_hull(trace + [b, c])) == len(trace) + 2:
        safe_bc.append(mask)
    if len(convex_hull(trace + [c, a])) == len(trace) + 2:
        safe_ca.append(mask)
assert all(mask.bit_count() <= 2 for mask in safe_bc)
assert all(mask.bit_count() <= 2 for mask in safe_ca)
profile_cap = m + m * (m - 1) // 2
assert len(safe_bc) <= profile_cap
assert len(safe_ca) <= profile_cap
assert profile_cap == 105
assert profile_cap * profile_cap == 11025 < local_faces == 16383


# Section 4: exact cyclic product identity for arbitrary positive integers.
Ls = [2, 3, 5, 7, 11]
As = [13, 17, 19, 23, 29]
Rs = [31, 37, 41, 43, 47]
qrank = len(Ls)
p0 = prod(Ls)
banks = []
for j in range(qrank):
    bank = Rs[(j - 1) % qrank] * As[(j + 1) % qrank]
    for i in range(qrank):
        if i not in {(j - 1) % qrank, j, (j + 1) % qrank}:
            bank *= Ls[i]
    banks.append(bank)
lhs_num = prod(banks)
rhs_num = p0 ** qrank * prod(As[i] * Rs[i] for i in range(qrank))
rhs_den = prod(Ls[i] ** 3 for i in range(qrank))
assert lhs_num * rhs_den == rhs_num


# Coefficients in (23).
acoef = F(1, 4)
kappa = F(1, 4)
assert acoef + F(1, 4) * (acoef / kappa) ** 2 == F(1, 2)
assert acoef + F(1, 8) * (acoef / kappa) ** 2 == F(3, 8)


# Section 5: K contexts reusing one B-face bank have overlap exactly K.
K = 17
Bsize = 31
contexts = range(K)
bank = set(range(Bsize))
incidences = [(ctx, face) for ctx in contexts for face in bank]
loads = {face: sum(1 for _, f in incidences if f == face) for face in bank}
assert len(incidences) == K * Bsize
assert max(loads.values()) == K
assert len(incidences) // max(loads.values()) == Bsize


print("STRONG_SEPARATION_ROOT_BAD_INTEGRATION_AUDIT verifier: PASS")
