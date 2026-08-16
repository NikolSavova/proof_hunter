#!/usr/bin/env python3
"""Exact audits for the capped source-projection/first-divergence theorem."""

from __future__ import annotations

from collections import defaultdict
from itertools import product
from math import comb, floor, log2
from random import Random


def prefixes(word: tuple[int, ...]):
    return [word[:i] for i in range(len(word) + 1)]


def first_divergence(x: tuple[int, ...], y: tuple[int, ...]):
    assert x != y and len(x) == len(y)
    for i, (a, b) in enumerate(zip(x, y)):
        if a != b:
            return x[:i]
    raise AssertionError("distinct fixed-depth leaves must diverge")


def audit(words, weights, sources, cap):
    """Check (7), and realize every w_s as first-divergence pair mass."""
    assert len(words) == len(weights) == len(sources)
    depth = len(words[0])
    assert all(len(w) == depth for w in words)
    assert len(set(words)) == len(words)

    source_mass = defaultdict(int)
    for a, s in zip(weights, sources):
        assert a >= 0
        source_mass[s] += a
    assert max(source_mass.values(), default=0) <= cap

    e = defaultdict(int)
    for word, a in zip(words, weights):
        for p in prefixes(word):
            e[p] += a

    w_node = {}
    for level in range(depth):
        for node in [p for p in e if len(p) == level]:
            children = [node + (bit,) for bit in (0, 1) if node + (bit,) in e]
            w_node[node] = e[node] ** 2 - sum(e[c] ** 2 for c in children)
            assert w_node[node] >= 0

    lhs = sum(w_node.values())
    rhs = e[()] ** 2 - sum(a * a for a in weights)
    assert lhs == rhs

    by_node = defaultdict(int)
    by_source_pair = defaultdict(int)
    for i, x in enumerate(words):
        for j, y in enumerate(words):
            if i == j:
                continue
            mass = weights[i] * weights[j]
            by_node[first_divergence(x, y)] += mass
            by_source_pair[(sources[i], sources[j])] += mass

    assert dict(by_node) == {k: v for k, v in w_node.items() if v}
    assert sum(by_source_pair.values()) == lhs
    assert max(by_source_pair.values(), default=0) <= cap * cap
    assert lhs <= cap * cap * len(set(sources)) ** 2
    return lhs, max(by_source_pair.values(), default=0)


def exhaustive_small():
    # Eight depth-three leaves, every 3-source assignment with cap <= 4.
    words = list(product((0, 1), repeat=3))
    checked = 0
    for sources in product(range(3), repeat=len(words)):
        counts = [sources.count(s) for s in range(3)]
        cap = max(counts)
        if cap > 4:
            continue
        audit(words, [1] * len(words), list(sources), cap)
        checked += 1
    return checked


def random_weighted():
    rng = Random(838)
    checked = 0
    words_all = list(product((0, 1), repeat=6))
    for _ in range(1000):
        rng.shuffle(words_all)
        m = rng.randint(2, 32)
        words = sorted(words_all[:m])
        cap = rng.randint(2, 12)
        weights = []
        sources = []
        remaining = defaultdict(lambda: cap)
        source_count = rng.randint(1, 12)
        for _word in words:
            available = [s for s in range(source_count) if remaining[s] > 0]
            if not available:
                break
            s = rng.choice(available)
            a = rng.randint(1, remaining[s])
            remaining[s] -= a
            sources.append(s)
            weights.append(a)
        words = words[: len(weights)]
        if len(words) >= 2:
            audit(words, weights, sources, cap)
            checked += 1
    return checked


def top_window_arithmetic():
    rows = []
    for ell in (16, 32, 64, 128, 256, 512, 1024):
        for C in (1, 2, 3, 4):
            g = min(ell - 1, floor(C * log2(ell)))
            r = ell - g
            d = 1 << g
            assert d <= ell**C
            assert d * d <= ell ** (2 * C)
            # n=2^ell makes n/2^r exactly 2^g.
            assert (1 << ell) // (1 << r) == d
            rows.append((ell, C, r, d))
    return rows


def history_audit():
    rows = []
    for L in (8, 12, 16, 20, 24):
        N = 1 << L
        h = L
        d = 1 << (2 * (L.bit_length() - 1))  # <= L^2, a polylog cap.
        histories = comb(N, h)
        capped = d * N
        assert histories > capped
        # Report exact bit gap.  It tends to L^2-O(L log L).
        gap = histories.bit_length() - capped.bit_length()
        rows.append((L, h, d, gap))
    return rows


def main():
    exhaustive = exhaustive_small()
    random_trials = random_weighted()
    top_rows = top_window_arithmetic()
    history_rows = history_audit()
    print("PASS capped guard-release telescope")
    print(f"  exhaustive capped source assignments: {exhaustive}")
    print(f"  random integer-weighted trees: {random_trials}")
    print(f"  exact top-window arithmetic rows: {len(top_rows)}")
    print("  universal-chain (L,h,d,history/cap bit gap):")
    for row in history_rows:
        print("   ", row)


if __name__ == "__main__":
    main()
