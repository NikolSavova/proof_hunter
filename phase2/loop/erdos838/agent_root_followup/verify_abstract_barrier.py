#!/usr/bin/env python3
"""Exact verifier for ABSTRACT_LATTICE_BARRIER.md."""

from itertools import combinations
from math import comb


def bits(mask, n):
    return [i for i in range(n) if mask >> i & 1]


def family(n):
    out = set()
    for k in range(n + 1):
        prefix = (1 << k) - 1
        tail = list(range(k, n))
        for b in range(3):
            for choice in combinations(tail, b):
                mask = prefix
                for i in choice:
                    mask |= 1 << i
                out.add(mask)
    return out


def closure(mask, closed, n):
    supers = [c for c in closed if c & mask == mask]
    ans = (1 << n) - 1
    for c in supers:
        ans &= c
    return ans


def verify(n):
    closed = family(n)
    full = (1 << n) - 1

    assert len(closed) == 1 + n + comb(n, 2) + comb(n, 3)
    assert 0 in closed and full in closed
    for a in closed:
        for b in closed:
            assert a & b in closed
        if a != full:
            assert any(a | (1 << x) in closed for x in range(n) if not (a >> x & 1))

    # Direct anti-exchange check.
    for a in closed:
        outside = [x for x in range(n) if not (a >> x & 1)]
        for x, y in combinations(outside, 2):
            cx = closure(a | (1 << x), closed, n)
            cy = closure(a | (1 << y), closed, n)
            assert not ((cx >> y & 1) and (cy >> x & 1))

    extreme_profile = [0] * (n + 1)
    for c in closed:
        ext = 0
        for x in bits(c, n):
            if not (closure(c & ~(1 << x), closed, n) >> x & 1):
                ext |= 1 << x
        k = ext.bit_count()
        assert k <= 3
        assert closure(ext, closed, n) == c
        extreme_profile[k] += 1

        # Every point in cl(S) is witnessed by a subset of S of size <= 3.
        for y in bits(c, n):
            witnesses = bits(ext, n)
            assert any(
                closure(sum(1 << x for x in q), closed, n) >> y & 1
                for r in range(min(3, len(witnesses)) + 1)
                for q in combinations(witnesses, r)
            )

    expected = [1, n, comb(n, 2), comb(n, 3)] + [0] * max(0, n - 3)
    assert extreme_profile == expected[: n + 1]
    return len(closed), extreme_profile


def main():
    for n in range(1, 13):
        size, profile = verify(n)
        print(n, size, profile)
    print("PASS")


if __name__ == "__main__":
    main()
