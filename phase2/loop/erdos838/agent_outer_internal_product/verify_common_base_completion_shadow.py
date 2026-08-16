#!/usr/bin/env python3
"""Audits COMMON_BASE_COMPLETION_SHADOW.md.

Only finite combinatorics and integer inequalities are checked here.  The
geometric input is the standard planar four-point certificate.
"""

from collections import Counter
from itertools import combinations
from math import comb, e, log2
from random import Random


def subsets_of_size(items, size):
    return [frozenset(x) for x in combinations(items, size)]


def audit_central_shadows():
    families = 0
    fibres = 0
    for m in range(2, 6):
        ground = tuple(range(m))
        for q in range(1, m + 1):
            layer = subsets_of_size(ground, q)
            # Exhaust all families when feasible.
            for mask in range(1, 1 << len(layer)):
                family = [layer[j] for j in range(len(layer)) if mask >> j & 1]
                for s in range(q + 1):
                    loads = Counter()
                    for Q in family:
                        for S in combinations(Q, s):
                            loads[frozenset(S)] += 1
                    assert sum(loads.values()) == len(family) * comb(q, s)
                    assert len(loads) == len({frozenset(S)
                                              for Q in family
                                              for S in combinations(Q, s)})
                    # A heavy output leaves distinct, uniform residuals.
                    for S, load in loads.items():
                        residuals = [Q - S for Q in family if S <= Q]
                        assert len(residuals) == load
                        assert len(set(residuals)) == load
                        assert all(len(T) == q - s for T in residuals)
                        fibres += 1
                families += 1
    return families, fibres


def audit_hybrid_cauchy():
    rng = Random(83820260814)
    trials = 600
    for _ in range(trials):
        number = rng.randint(1, 30)
        D = rng.randint(2, 12)
        b = rng.randint(1, 8)
        s = b // 2
        a = comb(b, s)
        H = rng.randint(1, 25)

        # Abstract ordinary-face labels.  The A and J universes are made
        # disjoint, which can only increase the available V.
        ua = rng.randint(D * a, D * a + 35)
        uj = rng.randint(H, H + 35)
        A_banks = []
        J_banks = []
        for _cell in range(number):
            A_banks.append(set(rng.sample(range(ua), D * a)))
            J_banks.append(set(rng.sample(range(uj), H)))
        load_a = Counter(x for bank in A_banks for x in bank)
        load_j = Counter(x for bank in J_banks for x in bank)
        LA = max(load_a.values())
        LJ = max(load_j.values())
        V = len(load_a) + len(load_j)

        # Square (11) and clear its denominator.  This is exact integer
        # arithmetic, with E = number * D^2.
        lhs = (number * D * D) ** 2 * a * H
        rhs = D ** 3 * LA * LJ * V * V
        assert lhs <= rhs
    return trials


def audit_dense_four_cover():
    cases = 0
    for m in range(4, 9):
        ground = tuple(range(m))
        fours = subsets_of_size(ground, 4)
        for q in range(4, m + 1):
            layer = subsets_of_size(ground, q)
            threshold = comb(m - 4, q - 4)
            # Exhaust every missing family below the sharp integer
            # threshold when the layer is small; otherwise sample all
            # initial missing segments (the proof itself is counting-only).
            missing_sets = []
            for z in range(threshold):
                if comb(len(layer), z) <= 5000:
                    missing_sets.extend(combinations(layer, z))
                else:
                    missing_sets.append(tuple(layer[:z]))
                    missing_sets.append(tuple(layer[-z:]) if z else tuple())
            for missing_tuple in missing_sets:
                missing = set(missing_tuple)
                present = [Q for Q in layer if Q not in missing]
                for T in fours:
                    assert any(T <= Q for Q in present)
                cases += 1
    return cases


def audit_explicit_dichotomy():
    # The report uses the elementary sufficient condition
    # d/8 >= 2 + 4 log_2(4 e d).  Its left-minus-right derivative is
    # positive from d=404 onward.
    d0 = 404
    margin = d0 / 8 - 2 - 4 * log2(4 * e * d0)
    derivative = 1 / 8 - 4 * log2(e) / d0
    assert margin > 0
    assert derivative > 0

    # Direct finite cross-check well below the conservative analytic
    # threshold.  Once m > 2q, 2^m/C(m,q) is increasing, so stopping after
    # a safe margin covers the tail.
    scans = 0
    for d in (48, 64, 80, 96):
        D = 1 << d
        H = 1 << (d * d // 8)
        m_stop = 2000
        for q in range(4, d // 2 + 1):
            for m in range(q, m_stop + 1):
                assert max(1 << m, H) >= D * D * comb(m, q)
                scans += 1
            assert m_stop > 2 * q
            assert (1 << m_stop) >= D * D * comb(m_stop, q)
    return margin, scans


def audit_obstructions():
    # Complete middle layer: the full downclosure expands by at most q+1.
    middle = []
    for q in range(1, 31):
        M = comb(2 * q, q)
        down = sum(comb(2 * q, i) for i in range(q + 1))
        assert down <= (q + 1) * M
        middle.append((q, down, M))

    # Two stars: both separate maximum degrees are k+1, while every
    # (A,J) codegree is one.
    star_cases = 0
    for k in range(1, 101):
        contexts = [("a*", "j*")]
        contexts += [("a*", f"j{i}") for i in range(k)]
        contexts += [(f"a{i}", "j*") for i in range(k)]
        da = Counter(a for a, _ in contexts)
        dj = Counter(j for _, j in contexts)
        pair = Counter(contexts)
        assert max(da.values()) == k + 1
        assert max(dj.values()) == k + 1
        assert max(pair.values()) == 1
        star_cases += 1
    return len(middle), star_cases


def audit_compatible_union_load():
    cases = 0
    for m in range(2, 8):
        ground = tuple(range(m))
        for q in range(1, m + 1):
            layer = subsets_of_size(ground, q)
            loads = Counter()
            for Q in layer:
                for R in layer:
                    if Q != R:
                        loads[Q | R] += 1
            if loads:
                assert max(loads.values()) <= 3 ** (2 * q)
                assert sum(loads.values()) == len(layer) * (len(layer) - 1)
            cases += 1
    return cases


def main():
    families, fibres = audit_central_shadows()
    cauchy = audit_hybrid_cauchy()
    covers = audit_dense_four_cover()
    margin, scans = audit_explicit_dichotomy()
    middle, stars = audit_obstructions()
    union_cases = audit_compatible_union_load()
    print("PASS: common-base completion-shadow audit")
    print(f"  uniform families: {families}; heavy fibres: {fibres}")
    print(f"  exact hybrid-Cauchy trials: {cauchy}")
    print(f"  dense four-cover cases: {covers}")
    print(f"  shield/source-cloud scans: {scans}; d=404 margin: {margin:.6f}")
    print(f"  middle-layer barriers: {middle}; two-star barriers: {stars}")
    print(f"  compatible-pair union banks: {union_cases}")


if __name__ == "__main__":
    main()
