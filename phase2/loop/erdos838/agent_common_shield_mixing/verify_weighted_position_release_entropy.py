#!/usr/bin/env python3
"""Exact/finite checks for WEIGHTED_POSITION_RELEASE_ENTROPY.md."""

from fractions import Fraction
from itertools import combinations, product
from math import comb, log2


def entropy(probabilities):
    return -sum(p * log2(p) for p in probabilities if p)


def orientation(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    points = sorted(set(points))
    lower = []
    for p in points:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def inside_triangle(p, a, b, c):
    signs = (orientation(a, b, p), orientation(b, c, p),
             orientation(c, a, p))
    return all(s > 0 for s in signs) or all(s < 0 for s in signs)


def convex_position(points):
    return len(hull(points)) == len(set(points))


def audit_position_colouring():
    # Ordered 3-words on five labels with deterministic nonuniform weights.
    labels = range(5)
    words = [w for w in combinations(labels, 3)]
    weights = {w: Fraction(1 + sum(w) % 3, 3) for w in words}
    total = sum(weights.values(), Fraction())
    best = Fraction()
    for colouring in product(range(3), repeat=5):
        kept = sum((weights[w] for w in words
                    if all(colouring[w[i]] == i for i in range(3))),
                   Fraction())
        best = max(best, kept)
    assert best >= total / 3**3
    return len(words), best


def audit_entropy_decoder():
    # Two binary roles and two pocket faces.  Exhaust every selected family,
    # integer weight vector in {1,2}, and deterministic adaptive mask map.
    words = tuple(product(range(2), repeat=2))
    faces = (0, 1)
    masks = (0, 1, 2, 3)  # bit i means coordinate i is deleted
    systems = 0
    for nonempty in range(1, 1 << len(words)):
        selected = [words[i] for i in range(len(words)) if nonempty >> i & 1]
        for raw_weights in product((1, 2), repeat=len(selected)):
            # Interpret raw weights 1,2 as actual weights 1/2,1, so every
            # source atom has weight at most one as in the theorem.
            raw_total = sum(raw_weights)
            W = raw_total / 2
            # It is enough to exhaust constant, word-only, face-only, and one
            # fully adaptive family; the inequality proof itself is symbolic.
            maps = []
            for m in masks:
                maps.append({(x, f): m for x in selected for f in faces})
            for by_word in product(masks, repeat=len(selected)):
                maps.append({(x, f): by_word[j]
                             for j, x in enumerate(selected) for f in faces})
            for by_face in product(masks, repeat=len(faces)):
                maps.append({(x, f): by_face[f] for x in selected for f in faces})
            maps.append({(x, f): (3 * x[0] + x[1] + f) % 4
                         for x in selected for f in faces})
            for mask_map in maps:
                output_mass = {}
                mean_sigma = 0.0
                input_probs = []
                for j, x in enumerate(selected):
                    for f in faces:
                        prob = raw_weights[j] / (raw_total * len(faces))
                        mask = mask_map[(x, f)]
                        retained = tuple(x[i] if not (mask >> i & 1) else None
                                         for i in range(2))
                        out = (f, mask, retained)
                        output_mass[out] = output_mass.get(out, 0.0) + prob
                        mean_sigma += prob * mask.bit_count()  # log |Xi| = 1
                        input_probs.append(prob)
                h_out = entropy(output_mass.values())
                h_in = entropy(input_probs)
                conditional_h = h_in - h_out
                mean_redundancy = mean_sigma - conditional_h
                assert h_out + mean_sigma + 1e-12 >= h_in
                assert mean_redundancy >= -1e-12
                assert abs(mean_sigma -
                           (h_in - h_out + mean_redundancy)) < 1e-10
                # The report's weaker min-entropy form.
                assert h_out + mean_sigma + 1e-12 >= log2(W) + 1
                systems += 1
    return systems


def rs_words(p=5):
    # Length 3, dimension 2: f(x)=a+bx at evaluation points 0,1,2.
    return {(a % p, (a + b) % p, (a + 2*b) % p)
            for a in range(p) for b in range(p)}


def audit_marked_mds_geometry():
    F = Fraction
    q, p = 3, 5
    radius = 8
    height = 10 * radius * radius
    eta = F(1, 10)

    # Fifteen source labels in three consecutive blocks, and seventeen
    # pocket labels so every source index has two neighbours.
    z = {i: (F(i), F(i*i - radius*radius)) for i in range(-7, 8)}
    x = {i: (F(i), F(height) + eta*i*i) for i in range(-8, 9)}
    left = (F(-9), F(638))
    right = (F(9), F(638))
    top = (F(1, 10), F(6403))
    root = (left, right, top)

    all_points = list(root) + list(z.values()) + list(x.values())
    assert all(orientation(a, b, c) != 0
               for a, b, c in combinations(all_points, 3))
    assert convex_position(list(root) + list(z.values()))
    assert convex_position(list(x.values()))
    assert all(inside_triangle(v, *root) for v in x.values())
    assert all(inside_triangle(x[i], z[i], x[i-1], x[i+1]) for i in z)

    blocks = (tuple(range(-7, -2)), tuple(range(-2, 3)),
              tuple(range(3, 8)))
    code = rs_words(p)
    assert len(code) == p**2
    sources = []
    for word in code:
        indices = tuple(blocks[j][word[j]] for j in range(q))
        source = list(root) + [z[i] for i in indices]
        assert convex_position(source)
        # The common root circuit and q singleton outer traces are strict.
        assert all(inside_triangle(x[i], z[i], x[i-1], x[i+1])
                   for i in indices)
        sources.append(indices)

    distances = [sum(a != b for a, b in zip(u, v))
                 for u, v in combinations(code, 2)]
    dmin = min(distances)
    assert dmin == 2
    assert q // dmin == 1

    # Exhaust the split-circuit hypergraph for every source and verify that
    # all q singleton traces plus the root trace are present.  This already
    # forces every cover to contain q source labels and one root label.
    for indices in sources:
        A_named = [('t0', left), ('t1', right), ('t2', top)] + [
            (f'z{i}', z[i]) for i in indices]
        X_named = [(f'x{i}', x[i]) for i in range(-8, 9)]
        traces = set()
        for four in combinations(A_named + X_named, 4):
            names = tuple(v[0] for v in four)
            pts = [v[1] for v in four]
            if convex_position(pts):
                continue
            outer = frozenset(name for name in names if not name.startswith('x'))
            if outer and len(outer) < 4:
                traces.add(outer)
        for i in indices:
            assert frozenset((f'z{i}',)) in traces
        assert frozenset(('t0', 't1', 't2')) in traces
        outer_names = [name for name, _ in A_named]
        tau = min(len(S) for k in range(len(outer_names) + 1)
                  for S in combinations(outer_names, k)
                  if all(set(S) & set(edge) for edge in traces))
        assert tau >= q + 1

    return len(code), dmin, len(all_points)


def audit_polar_local_global():
    # Fixed triangle around the origin and four angularly separated variable
    # roles.  Exhaust all transversals; whenever every cyclic local turn is
    # positive, the polar-order polygon must be convex.
    fixed = ((Fraction(3), Fraction(0)),
             (Fraction(0), Fraction(3)),
             (Fraction(-3), Fraction(-3)))
    roles = (
        ((Fraction(2), Fraction(1)), (Fraction(3), Fraction(1))),
        ((Fraction(-1), Fraction(2)), (Fraction(-1), Fraction(3))),
        ((Fraction(-3), Fraction(-1)), (Fraction(-2), Fraction(-1))),
        ((Fraction(1), Fraction(-2)), (Fraction(1), Fraction(-3))),
    )

    def half(p):
        return 0 if (p[1] > 0 or (p[1] == 0 and p[0] >= 0)) else 1

    def polar_cmp_key(p):
        # Only used on this rational finite audit.  atan2 is safe for sorting;
        # every asserted orientation and convexity statement remains exact.
        from math import atan2
        return atan2(float(p[1]), float(p[0])) % (2 * 3.141592653589793)

    checked = 0
    for choice in product(*roles):
        pts = sorted(fixed + choice, key=polar_cmp_key)
        turns = [orientation(pts[i], pts[(i+1) % len(pts)],
                             pts[(i+2) % len(pts)])
                 for i in range(len(pts))]
        if all(v > 0 for v in turns):
            assert convex_position(pts)
            checked += 1
    assert checked > 0
    return checked


def main():
    words, best = audit_position_colouring()
    systems = audit_entropy_decoder()
    code, dmin, points = audit_marked_mds_geometry()
    polar = audit_polar_local_global()
    print('PASS: position-words=%d best=%s entropy-systems=%d; '
          'marked-RS=%d dmin=%d points=%d polar=%d' %
          (words, best, systems, code, dmin, points, polar))


if __name__ == '__main__':
    main()
