#!/usr/bin/env python3
"""Applicability checks for the quasipolynomial source--triangle closure."""

from itertools import combinations, product
from math import comb
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
OUTER = ROOT / "agent_outer_internal_product"
sys.path.insert(0, str(OUTER))
import verify_full_word_triangle_reuse as stationary  # noqa: E402


def stationary_mapping():
    q, alphabet, cloud_size = 2, 2, 6
    anchors, endpoint, partner, cells, guards, pockets = (
        stationary.stationary_construction(q, alphabet, cloud_size)
    )
    del endpoint, partner
    words = list(product(range(alphabet), repeat=q))
    contexts = []
    all_sources = set()
    tags = set()
    raw_triangle_load = {}

    for word in words:
        base = frozenset(
            anchors + [cells[index][choice]
                       for index, choice in enumerate(word)]
        )
        sources = {
            frozenset(set(base) | {guard}) for guard in guards
        }
        assert len(sources) == cloud_size
        assert all(stationary.is_convex(list(source)) for source in sources)
        canonical_source = min(sources, key=lambda face: tuple(sorted(face)))
        triangles = {frozenset(triple)
                     for triple in combinations(guards, 3)}
        assert len(triangles) == comb(cloud_size, 3)
        for triangle in triangles:
            tags.add((canonical_source, triangle))
            raw_triangle_load[triangle] = (
                raw_triangle_load.get(triangle, 0) + 1
            )
        contexts.append((sources, triangles))
        all_sources.update(sources)

    context_count = alphabet**q
    assert len(contexts) == context_count
    assert len(all_sources) == context_count * cloud_size
    assert max(raw_triangle_load.values()) == context_count
    assert len(tags) == context_count * comb(cloud_size, 3)

    rows = columns = cloud_size
    edges = rows * columns
    triangles = comb(max(rows, columns), 3)
    assert 5 * edges * edges <= 54 * rows * triangles
    # Equality is attained at rows=columns=6.
    assert 5 * edges * edges == 54 * rows * triangles
    return context_count, len(all_sources), len(tags), max(
        raw_triangle_load.values())


def face_alphabet_scope_barrier():
    # Put q labels in convex position.  All nonempty subsets are actual
    # ordinary source faces, but they are a face alphabet rather than a
    # physical point cloud of the same size.
    q = 8
    source_faces = (1 << q) - 1
    physical_triangles = comb(q, 3)
    formal_face_triples = comb(source_faces, 3)
    assert physical_triangles == 56
    assert formal_face_triples > 2_000_000

    # If one falsely substitutes a=number of source faces into the local
    # triangle inequality while retaining only actual ambient triangles,
    # the inequality fails by orders of magnitude.
    rows = columns = source_faces
    edges = rows * columns
    assert 5 * edges * edges > 54 * rows * physical_triangles

    # Choosing one representative point from each source cannot repair the
    # mismatch: there are at most q distinct representatives.
    representative_support = q
    assert representative_support < source_faces
    return source_faces, physical_triangles, formal_face_triples


def context_coalescing_audit():
    # Repeating one source in K separately named equal-weight contexts
    # gives source load K, not one.  It may be compressed only if the
    # contexts coalesce into one product layer, or K is charged to the
    # certified description load.
    copies = 37
    unit_weight = 1
    split_load = copies * unit_weight
    coalesced_occurrences = unit_weight
    assert split_load == 37
    assert coalesced_occurrences == 1
    return split_load, coalesced_occurrences


def main():
    mapped = stationary_mapping()
    scope = face_alphabet_scope_barrier()
    coalescing = context_coalescing_audit()
    print(
        "PASS: stationary contexts=%d sources=%d tags=%d raw_T_load=%d; "
        "face-alphabet sources=%d physical_T=%d formal_face_triples=%d; "
        "context_loads=%s"
        % (mapped + scope + (coalescing,))
    )


if __name__ == "__main__":
    main()
