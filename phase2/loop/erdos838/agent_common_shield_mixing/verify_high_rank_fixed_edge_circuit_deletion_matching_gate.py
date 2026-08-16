#!/usr/bin/env python3
"""Exact checks for HIGH_RANK_FIXED_EDGE_CIRCUIT_DELETION_MATCHING_GATE.md."""

from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction
from functools import lru_cache
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))

from agent_common_shield_mixing.verify_dense_hall_two_cloud_profile_barrier import (  # noqa: E402
    G0,
    X0,
    convex,
    hull,
    parabolic_cloud,
)


def masks_of_size_at_most(n: int, d: int):
    for k in range(min(n, d) + 1):
        for subset in itertools.combinations(range(n), k):
            yield sum(1 << i for i in subset)


def transversal_number(edges: tuple[int, ...], n: int) -> int:
    if not edges:
        return 0
    for d in range(n + 1):
        for mask in masks_of_size_at_most(n, d):
            if all(mask & edge for edge in edges):
                return d
    raise AssertionError("no transversal")


def matching_number(edges: tuple[int, ...]) -> int:
    edges = tuple(sorted(set(edges)))

    @lru_cache(None)
    def search(used: int, start: int = 0) -> int:
        answer = 0
        for index in range(start, len(edges)):
            edge = edges[index]
            if not edge & used:
                answer = max(answer, 1 + search(used | edge, index + 1))
        return answer

    return search(0, 0)


def bad_circuits(source, pocket):
    points = tuple(source) + tuple(pocket)
    r = len(source)
    full = []
    source_traces = []
    for indices in itertools.combinations(range(len(points)), 4):
        if convex([points[i] for i in indices]):
            continue
        full_mask = sum(1 << i for i in indices)
        trace = full_mask & ((1 << r) - 1)
        assert trace and trace != full_mask
        full.append(full_mask)
        source_traces.append(trace)
    return tuple(sorted(set(full))), tuple(sorted(set(source_traces)))


def ordinary_after_mask(source, pocket, deleted: int) -> bool:
    points = tuple(source) + tuple(pocket)
    kept = [point for i, point in enumerate(points) if not (deleted >> i) & 1]
    return convex(kept)


def adjacent_on_hull(points, a, b):
    boundary = hull(points)
    ia = boundary.index(a)
    ib = boundary.index(b)
    return (ia - ib) % len(boundary) in (1, len(boundary) - 1)


def exact_planar_deletion_audit():
    outer = parabolic_cloud(G0, 8, 1)
    inner = parabolic_cloud(X0, 7, -1)
    summaries = []
    checked_masks = 0

    for r, q in ((4, 3), (5, 4), (6, 6)):
        source = tuple(outer[:r])
        pocket = tuple(inner[:q])
        assert convex(source) and convex(pocket)
        assert adjacent_on_hull(list(source), source[0], source[1])
        full, traces = bad_circuits(source, pocket)
        tau_y = transversal_number(traces, r)
        nu_y = matching_number(traces)
        tau_full = transversal_number(full, r + q)
        nu_full = matching_number(full)
        assert tau_y == r
        assert tau_y <= 3 * nu_y
        assert tau_full == r + q - max(r, q, 4)
        assert tau_full <= 4 * nu_full

        # Theorem 1: source deletion releases iff it hits every source trace.
        for deleted_y in range(1 << r):
            hits = all(deleted_y & edge for edge in traces)
            actual = ordinary_after_mask(source, pocket, deleted_y)
            assert actual == hits
            checked_masks += 1

        # Symmetric full-circuit version.
        for deleted in range(1 << (r + q)):
            hits = all(deleted & edge for edge in full)
            actual = ordinary_after_mask(source, pocket, deleted)
            assert actual == hits
            checked_masks += 1

        summaries.append((r, q, len(full), tau_y, nu_y, tau_full, nu_full))
    return summaries, checked_masks


def common_edge_toggle_audit():
    outer = parabolic_cloud(G0, 8, 1)
    inner = parabolic_cloud(X0, 7, -1)
    source = tuple(outer[:6])
    pocket = tuple(inner[:6])
    _, traces = bad_circuits(source, pocket)

    # Every singleton source trace occurs in the anti-aligned regression.
    singleton_masks = [1 << i for i in range(6)]
    assert all(mask in traces for mask in singleton_masks)
    safe = singleton_masks[2:]  # preserve the common exposed edge 0,1
    outputs = set()
    for choice in range(1 << len(safe)):
        deleted = 0
        for i, trace in enumerate(safe):
            if (choice >> i) & 1:
                deleted |= trace
        kept = tuple(i for i in range(6) if not (deleted >> i) & 1)
        assert 0 in kept and 1 in kept
        face = [source[i] for i in kept]
        assert convex(face)
        if len(face) >= 3:
            assert adjacent_on_hull(face, source[0], source[1])
        outputs.add(kept)
    assert len(outputs) == 16
    return len(outputs)


def decoder_load_audit():
    # Exhaust the literal low-deletion decoder on a small labelled universe.
    # The output R and guessed deleted set G recover A=R union G.
    n = 9
    d = 2
    sources = list(itertools.combinations(range(6), 4))
    pockets = list(itertools.combinations(range(6, 9), 2))
    fibres = {}
    for source in sources:
        for pocket in pockets:
            for deleted in itertools.chain(
                itertools.combinations(source, 0),
                itertools.combinations(source, 1),
                itertools.combinations(source, 2),
            ):
                output = (frozenset(set(source) - set(deleted)), frozenset(pocket))
                fibres.setdefault(output, set()).add((source, pocket, tuple(deleted)))
    bound = sum(comb(n, i) for i in range(d + 1))
    maximum = max(len(records) for records in fibres.values())
    assert maximum <= bound
    # In fact the rank constraint makes this toy fibre much smaller.
    assert maximum == comb(6 - 2, 2)
    return len(fibres), maximum, bound


def kk_shadow_audit():
    checked = 0
    for x in range(9, 24):
        for r in range(4, min(9, x) + 1):
            for j in range(1, min(4, r) + 1):
                lhs = comb(x, r - j) * comb(x, r)
                product_num = 1
                product_den = 1
                for h in range(j):
                    product_num *= r - h
                    product_den *= x - r + h + 1
                assert comb(x, r - j) * product_den == comb(x, r) * product_num
                assert lhs > 0
                checked += 1
    return checked


def mixed_capacity_audit():
    # Exact identity: pure-Y and pure-X face banks intersect only in empty.
    outer = parabolic_cloud(G0, 5, 1)
    inner = parabolic_cloud(X0, 4, -1)
    all_points = tuple(outer) + tuple(inner)

    def faces(points):
        answer = set()
        for mask in range(1 << len(points)):
            chosen = [points[i] for i in range(len(points)) if (mask >> i) & 1]
            if convex(chosen):
                answer.add(mask)
        return answer

    ambient = faces(all_points)
    left = faces(tuple(outer))
    right = faces(tuple(inner))
    mixed = {
        mask for mask in ambient
        if mask & ((1 << len(outer)) - 1)
        and mask >> len(outer)
    }
    assert len(mixed) == len(ambient) - len(left) - len(right) + 1
    return len(ambient), len(left), len(right), len(mixed)


def log2_binomial_sum(n: int, d: int) -> float:
    return math.log2(sum(comb(n, i) for i in range(d + 1)))


def live_scale_audit():
    rows = []
    sigma = 1 / 3
    for level in (128, 192, 256, 384, 512):
        n = 1 << level
        # A representative quasipolynomial slack.  Delta=o(L) and grows.
        delta = max(12, int(4 * math.log2(level)))
        d = int(sigma * delta / 2)
        load = log2_binomial_sum(n, d)
        surplus = sigma * level * delta
        assert load < 0.6 * surplus
        source_matching = d // 3
        full_matching = d // 4
        assert source_matching >= 1 and full_matching >= 1
        # If p=n/L^A with A>1, the induced Y-bank reduces mixed capacity
        # only by O(L/s), i.e. O(log L) bits rather than Theta(L log L).
        exponent = 3
        s = level**exponent
        eta = -math.log2(1 - 1 / s)
        phi_drop = 0.5 * level**2 - 0.5 * (level - eta) ** 2
        assert phi_drop <= 2 * level / (s * math.log(2))
        mixed_bit_saving = -math.log2(max(phi_drop * math.log(2), 1e-300))
        assert mixed_bit_saving < 2 * exponent * math.log2(level)
        rows.append((level, delta, d, load / (level * delta), mixed_bit_saving))
    return rows


def fixed_circuit_localization_audit():
    """Exact constant ledger for (24a)--(24c)."""
    sigma = Fraction(1, 3)
    rows = []
    for delta in (960, 1920, 3840, 7680):
        s = (sigma.numerator * delta) // (32 * sigma.denominator)
        d = 8 * s
        assert d <= sigma * delta / 4
        assert 4 * s <= sigma * delta / 8
        # After fixing the ordered four-label descriptions, the advertised
        # 5 sigma / 8 exponent leaves explicit slack (the raw ledger leaves
        # 7 sigma / 8, before lower-order terms).
        assert sigma * delta - 4 * s >= 5 * sigma * delta / 8
        assert d // 4 >= 2 * s
        rows.append((delta, s, d))
    return rows


def main():
    planar, masks = exact_planar_deletion_audit()
    toggles = common_edge_toggle_audit()
    decoder = decoder_load_audit()
    mixed = mixed_capacity_audit()
    kk = kk_shadow_audit()
    live = live_scale_audit()
    localization = fixed_circuit_localization_audit()
    print(
        "PASS: high-rank fixed-edge circuit deletion/matching gate; "
        f"planar={planar}; deletion-masks={masks}; toggles={toggles}; "
        f"decoder={decoder}; mixed={mixed}; KK={kk}; live-ledger={live}; "
        f"fixed-circuits={localization}"
    )


if __name__ == "__main__":
    main()
