#!/usr/bin/env python3
"""Exact checks for SOURCE_REUSE_BALANCED_ONE_ENDED_PROFILE_BARRIER."""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import sys

COMMON = Path(__file__).resolve().parents[1] / "agent_common_shield_mixing"
sys.path.insert(0, str(COMMON))
from verify_planar_singleton_terminal_two_cell_universal_cage import (  # noqa: E402
    convex,
    general_position,
    signs,
)


def circle(t):
    return ((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))


def configuration():
    F = Fraction
    q, s = 8, 2
    parameters = []
    for i in range(1, q // 2 + 1):
        parameters.extend([F(i), -F(1, i)])
    original = [circle(t) for t in parameters]
    lam, eps = F(1, 50), F(1, 1000)
    source = []
    for x, y in original:
        a, b = x + lam * y, y
        source.append((eps * a, 1 + 3 * eps * a + eps * eps * b))
    delta = F(1, 100)
    parabola = lambda x: (x, x * x - 1)
    L = [parabola(F(-1) - j * delta) for j in range(1, s + 1)]
    R = [parabola(F(1) + j * delta) for j in range(1, s + 1)]
    return original, source, L, R


def audit():
    original, Q, L, R = configuration()
    q, s = len(Q), len(L)
    whole = L + R + Q
    assert general_position(whole)
    assert convex(original) and convex(Q)
    assert signs(original) == signs(Q)

    # Universal full-edge obstruction, simultaneously over every edge.
    for left in L:
        for right in R:
            for i, j in combinations(range(q), 2):
                assert convex([left, right, Q[i]])
                assert convex([left, right, Q[j]])
                assert not convex([left, right, Q[i], Q[j]])

    profiles = []
    for endpoint in L + R:
        count = 0
        for mask in range(1 << q):
            A = [Q[i] for i in range(q) if mask >> i & 1]
            count += int(convex(A + [endpoint]))
        profiles.append(count)
    assert profiles == [82, 82, 82, 82]
    P_L, P_R = max(profiles[:s]), max(profiles[s:])

    V = 0
    for mask in range(1 << len(whole)):
        face = [whole[i] for i in range(len(whole)) if mask >> i & 1]
        V += int(convex(face))
    H = 1 << q
    upper = H + (2**s - 1) * (P_L + P_R) + (q + 1) * 2 ** (2 * s)
    assert V == 829
    assert V <= upper

    # Every source gets total weight one across the s^2 edges.
    T = H - q - 1
    weight = Fraction(1, s * s)
    edge_load = Counter()
    singleton_load = Counter()
    source_triangle_pairs = set()
    for mask in range(1 << q):
        A = tuple(i for i in range(q) if mask >> i & 1)
        if len(A) < 2:
            continue
        assert sum(weight for _ in L for _ in R) == 1
        for li, _ in enumerate(L):
            for ri, _ in enumerate(R):
                edge_load[(li, ri)] += weight
                for x in A:
                    singleton_load[(li, ri, x)] += weight
                    assert convex([L[li], R[ri], Q[x]])
                    source_triangle_pairs.add((mask, li, ri, x))

    W = Fraction(T)
    assert set(edge_load.values()) == {Fraction(T, s * s)}
    assert all(v / W == Fraction(1, s * s) for v in edge_load.values())
    assert set(singleton_load.values()) == {Fraction(2 ** (q - 1) - 1, s * s)}
    assert len(source_triangle_pairs) == s * s * (q * 2 ** (q - 1) - q)
    assert V * V >= len(source_triangle_pairs)
    return V, H, T, profiles[0], next(iter(singleton_load.values()))


if __name__ == "__main__":
    V, H, W, profile, load = audit()
    print(
        "PASS: V=%d H=%d W=%d one-ended-profile=%d singleton-load=%s"
        % (V, H, W, profile, load)
    )
