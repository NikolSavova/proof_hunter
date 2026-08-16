#!/usr/bin/env python3
"""Exact finite audit for HEAVY_PREFIX_ROTATION_DESCENT.md."""

from fractions import Fraction
from itertools import combinations, product
from math import comb


def powerset(items):
    items = tuple(items)
    for mask in range(1 << len(items)):
        yield frozenset(items[i] for i in range(len(items)) if mask >> i & 1)


def audit_toggle_banks():
    checked = 0
    # Exhaust all nonempty r-uniform families for the small cases and all
    # choices of an s-prefix inside every source.
    for n, r, s in ((4, 2, 1), (5, 2, 1), (5, 3, 1), (5, 3, 2)):
        layer = [frozenset(x) for x in combinations(range(n), r)]
        # Full family enumeration is already 2^10 for n=5,r=2.  For each
        # family, audit canonical splits plus all splits when the family is
        # small enough.
        for fam_mask in range(1, 1 << len(layer)):
            fam = [layer[i] for i in range(len(layer)) if fam_mask >> i & 1]
            options = [list(combinations(sorted(a), s)) for a in fam]
            split_vectors = product(*options) if len(fam) <= 4 else [tuple(o[0] for o in options)]
            for qs in split_vectors:
                banks = {}
                decomp = {}
                downclosure = set()
                for a, q0 in zip(fam, qs):
                    q = frozenset(q0)
                    rr = a - q
                    decomp[a] = (q, rr)
                    downclosure.update(powerset(a))
                    for b in powerset(q):
                        f = rr | b
                        banks.setdefault(f, []).append(a)
                kappa = max(map(len, banks.values()))
                assert (1 << s) * len(fam) == sum(map(len, banks.values()))
                assert (1 << s) * len(fam) <= kappa * len(downclosure)
                for f, sources in banks.items():
                    child = set()
                    residuals = []
                    for a in sources:
                        m = a - f
                        assert len(m) <= s and f <= a
                        residuals.append(m)
                        for b in powerset(f):
                            out = b | m
                            assert out <= a
                            child.add(out)
                    assert len(set(residuals)) == len(sources)
                    assert len(child) == (1 << len(f)) * len(sources)
                    assert len(f) >= r - s
                checked += 1
    return checked


def audit_exponents():
    checked = 0
    # Rational exponent audit.  For alpha>=1/2,
    # alpha/2 >= (1-alpha)/2, and delta<1/2 leaves saving 1/2-delta.
    for num in range(50, 100):
        alpha = Fraction(num, 100)
        assert alpha / 2 >= (1 - alpha) / 2
        for dnum in (0, 5, 10, 20, 24, 25, 40, 49):
            delta = Fraction(dnum, 100)
            assert Fraction(1, 2) - delta > 0
            # exponent in kappa*D/2^s is at most
            # (delta+1)(1-alpha)-alpha/2.
            lhs = (1 + delta) * (1 - alpha) - alpha / 2
            rhs = (1 - (Fraction(1, 2) - delta)) * (1 - alpha)
            assert lhs <= rhs
            checked += 1
    return checked


def audit_codegrees_and_marked_downsets():
    checked = 0
    # Exhaust all left-D-regular incidence graphs for small (sources,labels).
    for source_count, label_count, D in ((3, 3, 1), (3, 3, 2), (4, 3, 2), (3, 4, 2)):
        neighborhoods = [frozenset(c) for c in combinations(range(label_count), D)]
        for choice in product(neighborhoods, repeat=source_count):
            q = {}
            for a in range(source_count):
                for b in range(source_count):
                    if a != b:
                        q[a, b] = len(choice[a] & choice[b])
            q2 = sum(v * v for v in q.values())
            c = {}
            for p in range(label_count):
                for z in range(label_count):
                    c[p, z] = sum(p in choice[a] and z in choice[a] for a in range(source_count))
            mt = {}
            for p in range(label_count):
                direct = sum(q[a, b] for a in range(source_count) for b in range(source_count)
                             if a != b and p in choice[a] and p in choice[b])
                moment = sum(c[p, z] * (c[p, z] - 1) for z in range(label_count))
                assert direct == moment
                mt[p] = direct
            assert sum(mt.values()) == q2

            # Treat every quadruple (a,b,p,z) as incompatible.  Give source a
            # an abstract rank-3 target with mark p; private labels prevent
            # accidental target equality but downfaces may overlap on marks.
            occurrences = []
            targets = {}
            next_private = label_count
            for a in range(source_count):
                for p in choice[a]:
                    targets[a, p] = frozenset((p, next_private, next_private + 1))
                    next_private += 2
            for a in range(source_count):
                for b in range(source_count):
                    if a == b:
                        continue
                    common = choice[a] & choice[b]
                    for p in common:
                        for z in common:
                            occurrences.append((a, b, p, z))
            if occurrences:
                mp = {p: 0 for p in range(label_count)}
                face_load = {}
                complex_faces = set()
                for a, b, p, z in occurrences:
                    mp[p] += 1
                    target = targets[a, p]
                    complex_faces.update(powerset(target))
                    for f in powerset(target):
                        if p in f:
                            face_load[f] = face_load.get(f, 0) + 1
                M = max(mp.values())
                total_inc = sum(face_load.values())
                assert total_inc == len(occurrences) * (1 << (3 - 1))
                assert max(face_load.values()) <= 3 * M
                assert len(occurrences) * (1 << (3 - 1)) <= 3 * M * len(complex_faces)
            checked += 1
    return checked


def main():
    a = audit_toggle_banks()
    b = audit_exponents()
    c = audit_codegrees_and_marked_downsets()
    print(f"PASS toggle={a} exponent={b} codegree={c}")


if __name__ == "__main__":
    main()
