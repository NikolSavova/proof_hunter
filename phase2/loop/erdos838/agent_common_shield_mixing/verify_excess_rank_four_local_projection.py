#!/usr/bin/env python3
"""Finite checks for EXCESS_RANK_FOUR_LOCAL_PROJECTION_DICHOTOMY.md."""

from itertools import combinations, product
from math import comb, factorial, log2


def entropy(probs):
    return -sum(p * log2(p) for p in probs if p)


def projection(word, i):
    return word[:i] + word[i+1:]


def audit_projection_entropy():
    r = 4
    cube = tuple(product(range(2), repeat=r))
    systems = 0
    # Exhaust every nonempty selected family.  Test three ambient ordinary
    # supersets: selected only, full cube, and a deterministic parity thickening.
    for mask in range(1, 1 << len(cube)):
        selected = {cube[j] for j in range(len(cube)) if mask >> j & 1}
        ambient_sets = (
            selected,
            set(cube),
            selected | {w for w in cube if sum(w) % 2 == 0},
        )
        weight_schemes = (
            {w: 1.0 for w in selected},
            {w: 1.0 / (1 + ((sum((j + 1) * x for j, x in enumerate(w))
                                + mask.bit_count()) % 3)) for w in selected},
        )
        for weights in weight_schemes:
            W = sum(weights.values())
            probs = [weights[w] / W for w in selected]
            Rw = r - entropy(probs)
            for good in ambient_sets:
                G = 0.0
                B = 0.0
                Dsum = 0
                for i in range(r):
                    fibres = {}
                    for w in selected:
                        fibres.setdefault(projection(w, i), []).append(
                            (w[i], weights[w]))
                    gi = 0.0
                    bi = 0.0
                    Di = 0
                    for v, vals in fibres.items():
                        a = sum(weight for _, weight in vals)
                        cond = [weight / a for _, weight in vals]
                        h = entropy(cond)
                        d = sum(v[:i] + (x,) + v[i:] in good
                                for x in range(2))
                        assert len(vals) <= d <= 2
                        assert h + 1e-12 >= log2(a)
                        p_v = a / W
                        gi += p_v * (log2(d) - h)
                        bi += p_v * log2(2 / d)
                        Di += d
                    assert Di + 1e-10 >= W * 2**gi
                    G += gi
                    B += bi
                    Dsum += Di
                assert Rw <= G + B + 1e-10
                assert len(good) + 1e-10 >= Dsum / r
                assert len(good) / W + 1e-10 >= 2**(G / r)
                systems += 1
    return systems


def audit_injective_colouring():
    labels = tuple(range(6))
    s = 3
    sources = tuple(combinations(labels, s))
    weights = {a: 1.0 / (1 + sum(a) % 3) for a in sources}
    total = sum(weights.values())
    best = 0.0
    for colouring in product(range(s), repeat=len(labels)):
        kept = sum(weights[a] for a in sources
                   if len({colouring[x] for x in a}) == s)
        best = max(best, kept)
    target = factorial(s) / s**s * total
    assert best + 1e-12 >= target
    return len(sources), best, target


def audit_four_local_union_bound():
    # Abstract rooted role box.  Patterns may use one to four variable roles
    # and the remaining fixed root labels.
    s, t, q = 4, 3, 8
    words = tuple(product(range(q), repeat=s))
    bad_sets = {}
    beta_sum = 0.0
    for ksize in range(t + 1):
        jsize = 4 - ksize
        if not 1 <= jsize <= s:
            continue
        for J in combinations(range(s), jsize):
            for K in combinations(range(t), ksize):
                # A single bad tuple makes the union bound non-vacuous while
                # exercising every possible number of variable roles.
                bad = {tuple((sum(K) + z) % q for z in range(jsize))}
                bad_sets[(J, K)] = bad
                beta_sum += len(bad) / q**jsize
    bad_full = 0
    for w in words:
        if any(tuple(w[i] for i in J) in bad
               for (J, _K), bad in bad_sets.items()):
            bad_full += 1
    good = len(words) - bad_full
    assert good >= len(words) * (1 - beta_sum) - 1e-12
    return good, beta_sum


def audit_dense_layer():
    n, r = 8, 5
    layer = set(combinations(range(n), r))
    covered4 = {q for edge in layer for q in combinations(edge, 4)}
    assert len(covered4) == comb(n, 4)
    # Remove all extensions of one four-set: the missing fraction is exact.
    q0 = (0, 1, 2, 3)
    reduced = {edge for edge in layer if not set(q0) <= set(edge)}
    missing_fraction = 1 - len(reduced) / len(layer)
    exact = comb(n - 4, r - 4) / comb(n, r)
    assert abs(missing_fraction - exact) < 1e-12
    assert exact >= ((r - 3) / n) ** 4
    return len(layer), len(covered4)


def rs_code(p=5):
    # Length 5, dimension 4.  Evaluation of cubics at 0,...,4.
    words = set()
    for coeff in product(range(p), repeat=4):
        word = tuple(sum(coeff[j] * pow(x, j, p) for j in range(4)) % p
                     for x in range(5))
        words.add(word)
    return words


def audit_mds_strength_four():
    p = 5
    code = rs_code(p)
    assert len(code) == p**4
    for k in range(1, 5):
        for I in combinations(range(5), k):
            projection_set = {tuple(w[i] for i in I) for w in code}
            assert len(projection_set) == p**k
    ambient = p**5
    redundancy_gain = ambient // len(code)
    assert redundancy_gain == p
    return len(code), ambient


def main():
    colour_sources, colour_best, colour_target = audit_injective_colouring()
    systems = audit_projection_entropy()
    good, beta = audit_four_local_union_bound()
    layer, shadow4 = audit_dense_layer()
    code, ambient = audit_mds_strength_four()
    print('PASS: colouring-sources=%d best=%.3f target=%.3f; '
          'projection-systems=%d fourlocal-good=%d beta-sum=%.3f; '
          'dense-layer=%d shadow4=%d; MDS=%d ambient=%d' %
          (colour_sources, colour_best, colour_target, systems, good, beta,
           layer, shadow4, code, ambient))


if __name__ == '__main__':
    main()
