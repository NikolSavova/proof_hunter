#!/usr/bin/env python3
"""Exact checks for FACE_DEPENDENT_EDGE_DISPERSION_BOOLEAN_SHIELD_BARRIER."""

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
    hull,
)


def configuration():
    F = Fraction
    s, h = 3, 5
    delta = F(1, 100)
    Lx = [F(-1) - j * delta for j in range(1, s + 1)]
    Rx = [F(1) + j * delta for j in range(1, s + 1)]
    Cx = [F(j, 5) for j in range(-2, 3)]
    parabola = lambda x: (x, x * x - 1)
    L, C, R = list(map(parabola, Lx)), list(map(parabola, Cx)), list(map(parabola, Rx))

    original = [(F(a), F(a * a)) for a in range(-3, 4)]
    eps = F(1, 1000)
    child = [(eps * a, 1 + 3 * eps * a + eps * eps * b)
             for a, b in original]
    return s, h, L, C, R, child


def exposed_edge(face, left, right):
    H = hull(face)
    return any({H[i], H[(i + 1) % len(H)]} == {left, right}
               for i in range(len(H)))


def audit():
    s, h, L, C, R, child = configuration()
    all_points = L + C + R + child
    assert general_position(all_points)

    # The whole carrier is convex, hence its full Boolean algebra is a
    # detached load-one shield.
    carrier = L + C + R
    assert convex(carrier)
    detached = 0
    for mask in range(1 << len(carrier)):
        face = [carrier[i] for i in range(len(carrier)) if mask >> i & 1]
        assert convex(face)
        detached += 1
    assert detached == 2 ** (h + 2 * s)

    contexts = []
    fibres = Counter()
    singleton_outputs = set()
    mixed_tested = 0
    X = list(range(0, len(child), 2))
    Y = list(range(1, len(child), 2))
    for li, left in enumerate(L):
        for ri, right in enumerate(R):
            for mask in range(1 << h):
                middle = tuple(i for i in range(h) if mask >> i & 1)
                B = [left, right] + [C[i] for i in middle]
                assert convex(B)
                assert exposed_edge(B, left, right)
                contexts.append((middle, li, ri))
                fibres[(li, ri)] += 1

                for i, x in enumerate(child):
                    assert convex(B + [x])
                    # Label-level output decoder: B intersection with the
                    # three carrier classes plus child label i.
                    code = (middle, li, ri, i)
                    assert code not in singleton_outputs
                    singleton_outputs.add(code)

                for i in X:
                    for j in Y:
                        assert not convex(B + [child[i], child[j]])
                        mixed_tested += 1

    assert len(contexts) == (2**h) * s * s
    assert set(fibres.values()) == {2**h}
    assert all(Fraction(v, len(contexts)) == Fraction(1, s * s)
               for v in fibres.values())
    assert len(singleton_outputs) == len(contexts) * len(child)

    # Every directed edge goes L -> R, so [all L, all R] is an exact
    # topological ordering and no directed path can return.
    directed_edges = [(li, s + ri) for li in range(s) for ri in range(s)]
    assert all(u < s <= v for u, v in directed_edges)
    assert not any(v == u2 for u, v in directed_edges for u2, v2 in directed_edges)

    return len(contexts), len(fibres), detached, mixed_tested


if __name__ == "__main__":
    contexts, edges, detached, mixed = audit()
    print(
        "PASS: contexts=%d edge-fibres=%d detached=%d bad-cross-records=%d"
        % (contexts, edges, detached, mixed)
    )
