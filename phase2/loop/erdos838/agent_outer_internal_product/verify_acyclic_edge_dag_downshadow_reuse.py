#!/usr/bin/env python3
"""Exact checks for ACYCLIC_EDGE_DAG_DOWNSHADOW_AND_REUSE_GATE."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import sys

COMMON = Path(__file__).resolve().parents[1] / "agent_common_shield_mixing"
sys.path.insert(0, str(COMMON))
from verify_planar_singleton_terminal_two_cell_universal_cage import (  # noqa: E402
    convex,
    general_position,
)

from verify_face_dependent_edge_dispersion_barrier import configuration


def weighted_decoder_check():
    # Abstract labelled carrier faces on six endpoint labels plus private
    # internal labels. The first three labels are L, the next three R.
    weights = [Fraction(1), Fraction(2), Fraction(3), Fraction(5)]
    contexts = []
    for li in range(3):
        for ri in range(3):
            for j, w in enumerate(weights):
                edge = (li, 3 + ri)
                internal = frozenset({6 + j, 10 + (li + ri + j) % 3})
                contexts.append((edge, internal, w))

    W = sum(w for _, _, w in contexts)
    fibres = Counter()
    for edge, _, w in contexts:
        fibres[edge] += w
    delta = max(fibres.values()) / W
    assert delta == Fraction(1, 9)

    loads = defaultdict(Fraction)
    generated = Fraction(0)
    for edge, internal, w in contexts:
        items = tuple(internal)
        for mask in range(1 << len(items)):
            F = frozenset(items[i] for i in range(len(items)) if mask >> i & 1)
            out = frozenset(edge) | F
            assert out & frozenset(range(6)) == frozenset(edge)
            loads[out] += w
            generated += w
    assert max(loads.values()) <= delta * W
    union_size = len(loads)
    assert union_size * delta * W >= generated
    return len(contexts), union_size


def geometry_source_reuse_check():
    s, _, L, _, R, child = configuration()
    assert general_position(L + R + child)
    # The transformed seven-point parabola is convex, so all nontrivial
    # subsets are actual source faces.
    assert convex(child)
    source_faces = []
    q = len(child)
    for mask in range(1 << q):
        A = [i for i in range(q) if mask >> i & 1]
        if len(A) >= 2:
            assert convex([child[i] for i in A])
            source_faces.append(tuple(A))

    edge_load = Counter()
    singleton_load = Counter()
    records = 0
    for li, left in enumerate(L):
        for ri, right in enumerate(R):
            B = [left, right]
            for A in source_faces:
                records += 1
                edge_load[(li, ri)] += 1
                for i in A:
                    assert convex(B + [child[i]])
                    singleton_load[(li, ri, i)] += 1
                for i, j in combinations(A, 2):
                    assert not convex(B + [child[i], child[j]])

    T = len(source_faces)
    assert records == T * s * s
    assert set(edge_load.values()) == {T}
    assert Fraction(max(edge_load.values()), records) == Fraction(1, s * s)
    # In the Boolean q-child, every label belongs to 2^(q-1)-1 source
    # faces of rank at least two.
    assert set(singleton_load.values()) == {2 ** (q - 1) - 1}
    assert all(u < s <= v for u, v in
               [(li, s + ri) for li in range(s) for ri in range(s)])
    return T, records, max(singleton_load.values())


if __name__ == "__main__":
    contexts, outputs = weighted_decoder_check()
    source_faces, records, load = geometry_source_reuse_check()
    print(
        "PASS: abstract-contexts=%d outputs=%d; source-faces=%d "
        "records=%d singleton-load=%d"
        % (contexts, outputs, source_faces, records, load)
    )
