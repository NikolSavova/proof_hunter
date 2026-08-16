#!/usr/bin/env python3
"""Exact audit for SOURCE_THIN_FOUR_LOCAL_BLOCKER_SHADOW_DICHOTOMY."""

from __future__ import annotations

import itertools
import sys
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))

from agent_shield_circuit_cover.verify_almost_full_word_mixed_bank_barrier import (  # noqa: E402
    central_child,
    is_convex,
    role_cells,
)


def subsets(mask):
    sub = mask
    while True:
        yield sub
        if sub == 0:
            return
        sub = (sub - 1) & mask


def minimalize(edges):
    edges = set(edges)
    return frozenset(
        edge for edge in edges
        if not any(other != edge and other & edge == other for other in edges)
    )


def independent(mask, hypergraph):
    return not any(edge & mask == edge for edge in hypergraph)


def min_vertex_cover(q, hypergraph):
    if not hypergraph:
        return 0, 0
    candidates = []
    for cover in range(1 << q):
        if all(cover & edge for edge in hypergraph):
            candidates.append(cover)
    size = min(mask.bit_count() for mask in candidates)
    return size, min(mask for mask in candidates if mask.bit_count() == size)


def maximum_matching(hypergraph):
    edges = sorted(hypergraph)
    best = ()
    for choice_mask in range(1 << len(edges)):
        chosen = tuple(
            edges[i] for i in range(len(edges)) if choice_mask >> i & 1
        )
        union = 0
        valid = True
        for edge in chosen:
            if union & edge:
                valid = False
                break
            union |= edge
        if valid and (len(chosen), tuple(chosen)) > (len(best), tuple(best)):
            best = chosen
    return best


def exhaustive_rank_three_hypergraphs():
    q = 4
    possible = [
        mask for mask in range(1, 1 << q) if mask.bit_count() <= 3
    ]
    seen = set()
    checked = 0
    for family_mask in range(1 << len(possible)):
        raw = [
            possible[i] for i in range(len(possible))
            if family_mask >> i & 1
        ]
        hypergraph = minimalize(raw)
        if hypergraph in seen:
            continue
        seen.add(hypergraph)

        compatible = {
            mask for mask in range(1 << q) if independent(mask, hypergraph)
        }
        # The independent-set description is hereditary and exact.
        assert all(sub in compatible for mask in compatible for sub in subsets(mask))

        almost_full = {
            i for i in range(q)
            if ((1 << q) - 1) ^ (1 << i) in compatible
        }
        if not hypergraph:
            assert almost_full == set(range(q))
            tau, cover = 0, 0
            matching = ()
        else:
            core = set(range(q))
            for edge in hypergraph:
                core &= {i for i in range(q) if edge >> i & 1}
            assert almost_full == core
            assert len(almost_full) <= 3
            tau, cover = min_vertex_cover(q, hypergraph)
            matching = maximum_matching(hypergraph)
            assert len(matching) <= tau <= 3 * len(matching)

        # Deleting a minimum cover, plus any one tag outside it, is good.
        for i in range(q):
            if not (cover >> i & 1):
                retained = ((1 << q) - 1) ^ (cover | (1 << i))
                assert retained in compatible

        # A representative root from every disjoint blocker gives distinct
        # codimension-one source masks.
        roots = [min(i for i in range(q) if edge >> i & 1) for edge in matching]
        assert len(roots) == len(set(roots))
        assert q - tau + 3 * len(matching) >= q
        checked += 1
    assert checked == len(seen)
    return checked


def maximum_child_and_pascal_models():
    rows = []
    for q in range(3, 11):
        for prefix in range(q + 1):
            hypergraph = frozenset(1 << i for i in range(prefix, q))
            tau, cover = min_vertex_cover(q, hypergraph)
            matching = maximum_matching(hypergraph)
            assert tau == q - prefix
            assert cover == sum(1 << i for i in range(prefix, q))
            assert len(matching) == q - prefix
            rows.append((q, prefix, tau))

        # The Pascal all-delete terminal is the prefix model with prefix 0.
        pascal = frozenset(1 << i for i in range(q))
        tau, _ = min_vertex_cover(q, pascal)
        matching = maximum_matching(pascal)
        assert tau == len(matching) == q
    return rows


def anti_aligned_geometry_and_loads():
    cells = role_cells()
    _, o, p, _, _ = central_child()
    word = [cell[0] for cell in cells]
    seam = [o, p]
    q = 6

    compatible = set()
    for mask in range(1 << q):
        trace = [word[i] for i in range(q) if mask >> i & 1]
        if is_convex(seam + trace):
            compatible.add(mask)
    expected = {
        mask for mask in range(1 << q)
        if not ((mask & 0b000111) and (mask & 0b111000))
    }
    assert compatible == expected

    hypergraph = minimalize(
        mask for mask in range(1, 1 << q)
        if mask not in compatible
    )
    assert hypergraph == frozenset(
        (1 << i) | (1 << j) for i in range(3) for j in range(3, 6)
    )
    tau, cover = min_vertex_cover(q, hypergraph)
    matching = maximum_matching(hypergraph)
    assert tau == len(matching) == 3
    assert cover in (0b000111, 0b111000)

    # Complete four-label role product.  The canonical matching roots are
    # three distinct roles.  Omitting a root from the ordinary source word
    # has exact completion load four.
    words = list(itertools.product(*cells))
    source_loads = Counter()
    cover_loads = Counter()
    roots = [min(i for i in range(q) if edge >> i & 1) for edge in matching]
    tags = [i for i in range(q) if not (cover >> i & 1)]
    for selected in words:
        for root in roots:
            output = frozenset(selected[i] for i in range(q) if i != root)
            assert is_convex(output)
            source_loads[output] += 1
        for tag in tags:
            deletion = cover | (1 << tag)
            output = frozenset(
                seam + [selected[i] for i in range(q) if not (deletion >> i & 1)]
            )
            assert is_convex(output)
            cover_loads[output] += 1

    mass = 4**6
    assert sum(source_loads.values()) == mass * 3
    assert len(source_loads) == mass * 3 // 4
    assert set(source_loads.values()) == {4}
    assert sum(cover_loads.values()) == mass * 3
    assert len(cover_loads) == mass * 3 // (4**4)
    assert set(cover_loads.values()) == {4**4}
    return (
        len(compatible), len(hypergraph), tau, len(matching),
        sum(source_loads.values()), len(source_loads),
        min(source_loads.values()),
        sum(cover_loads.values()), len(cover_loads),
        min(cover_loads.values()),
    )


def weighted_dichotomy_arithmetic():
    # Synthetic nonnegative weights verify the aggregate identity.  The
    # theorem itself is linear, so rational/integer weights suffice.
    q = 12
    rows = []
    total_weight = 0
    cover_incidence = 0
    blocker_incidence = 0
    for tau in range(q + 1):
        weight = (tau + 1) ** 2
        nu = (tau + 2) // 3
        assert 3 * nu >= tau
        total_weight += weight
        cover_incidence += weight * (q - tau)
        blocker_incidence += weight * nu
        rows.append((tau, weight, nu))
    assert cover_incidence + 3 * blocker_incidence >= q * total_weight
    assert cover_incidence >= q * total_weight / 2 or blocker_incidence >= q * total_weight / 6
    return total_weight, cover_incidence, blocker_incidence, rows


def main():
    hypergraphs = exhaustive_rank_three_hypergraphs()
    prefixes = maximum_child_and_pascal_models()
    anti = anti_aligned_geometry_and_loads()
    weighted = weighted_dichotomy_arithmetic()
    print(
        "PASS: source-thin blocker/shadow dichotomy; hypergraphs=%d; "
        "prefixes=%d; anti=%s; weighted=(%d,%d,%d)"
        % (
            hypergraphs, len(prefixes), anti,
            weighted[0], weighted[1], weighted[2],
        )
    )


if __name__ == "__main__":
    main()
