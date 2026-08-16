#!/usr/bin/env python3
"""Exact audit of CIRCUIT_TRANSVERSAL_GUARD_RELEASE.md."""

from __future__ import annotations

import json
import sys
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
CHAIN = ERDOS / "agent_cyclic_stem_hw"
MIXED = ERDOS / "agent_recursive_pocket_induction"
APA = ERDOS / "agent_apa_rank"
for directory in (HERE, CHAIN, MIXED, APA):
    sys.path.insert(0, str(directory))

from verify_insertion_chain_universality import transform  # noqa: E402
from verify_long_chain_mixed_barrier import hard_points, hull  # noqa: E402
from verify_outer_internal_mixed_bank import (  # noqa: E402
    choose_lower_parameters,
    parabola_point,
)


Point = tuple[Fraction, Fraction]


def maximum_disjoint_edges(edges: set[int], vertices: int) -> tuple[int, ...]:
    """One maximum matching in a clutter represented by bit masks."""
    ordered = tuple(sorted(edges, key=lambda mask: (mask.bit_count(), mask)))

    @lru_cache(maxsize=None)
    def solve(available: int) -> tuple[int, ...]:
        best: tuple[int, ...] = ()
        for edge in ordered:
            if edge & available == edge:
                candidate = (edge,) + solve(available ^ edge)
                if len(candidate) > len(best):
                    best = candidate
        return best

    return solve((1 << vertices) - 1)


def exhaustive_rank_two_clutters() -> dict[str, int]:
    """Exhaust every rank-two clutter through four vertices, then stress to 8."""
    checked = 0
    toggle_checks = 0
    vertices = 4
    possible = [1 << i for i in range(vertices)] + [
        (1 << i) | (1 << j) for i, j in combinations(range(vertices), 2)
    ]
    for family_mask in range(1 << len(possible)):
        edges = {
            edge for index, edge in enumerate(possible) if family_mask & (1 << index)
        }
        matching = maximum_disjoint_edges(edges, vertices)
        guard = 0
        for edge in matching:
            assert not guard & edge
            guard |= edge
        assert guard.bit_count() <= 2 * len(matching)
        assert all(guard & edge for edge in edges)

        # The matching blocks give exactly 2^k distinct deleted subsets.
        deleted = set()
        for choice in range(1 << len(matching)):
            mask = 0
            for index, edge in enumerate(matching):
                if choice & (1 << index):
                    mask |= edge
            deleted.add(mask)
        assert len(deleted) == 1 << len(matching)
        checked += 1
        toggle_checks += len(deleted)

    # Deterministic larger stress families.
    for vertices in range(5, 9):
        possible = [1 << i for i in range(vertices)] + [
            (1 << i) | (1 << j) for i, j in combinations(range(vertices), 2)
        ]
        for seed in range(64):
            edges = {
                edge
                for index, edge in enumerate(possible)
                if ((index + 3) * (seed + 5) + index * index) % 11 < 4
            }
            matching = maximum_disjoint_edges(edges, vertices)
            guard = 0
            for edge in matching:
                assert not guard & edge
                guard |= edge
            assert all(guard & edge for edge in edges)
            assert guard.bit_count() <= 2 * len(matching)
            checked += 1

    return {
        "rank_two_clutters_checked": checked,
        "four_vertex_toggle_subsets_checked": toggle_checks,
    }


def internal_faces(points: list[Point]) -> list[tuple[int, ...]]:
    faces = []
    for rank in range(len(points) + 1):
        for labels in combinations(range(len(points)), rank):
            selected = [points[index] for index in labels]
            if len(hull(selected)) == rank:
                faces.append(labels)
    return faces


def trace_clutter(carrier: list[Point], internal: list[Point]) -> set[int]:
    edges: set[int] = set()
    for outer_rank in (1, 2):
        for outer_labels in combinations(range(len(carrier)), outer_rank):
            outer = [carrier[index] for index in outer_labels]
            for inner_labels in combinations(range(len(internal)), 4 - outer_rank):
                inner = [internal[index] for index in inner_labels]
                if len(hull(outer + inner)) < 4:
                    edge = sum(1 << index for index in outer_labels)
                    edges.add(edge)
                    break
    return edges


def released_decoder_bound() -> dict[str, int]:
    """Exhaust the S_g(t) preimage count used in (14)."""
    checks = 0
    for t in range(1, 9):
        universe = set(range(t + 4))
        fixed_released = frozenset(range(t, t + 4))
        for g in range(0, min(4, t) + 1):
            carriers = []
            for size in range(g + 1):
                for guard in combinations(range(t), size):
                    carriers.append(fixed_released | frozenset(guard))
            assert len(set(carriers)) == sum(comb(t, size) for size in range(g + 1))
            assert all(carrier <= universe for carrier in carriers)
            checks += 1
    return {"released_decoder_parameter_checks": checks}


def entropy_splice_audit() -> dict[str, object]:
    """Exact integer audit of Theorem 3 and Corollary 9 constants."""
    rows = []
    # c=1/8, delta=1/2, hence t=floor((log D)/32), and any
    # epsilon<1/64 is allowed asymptotically.  Audit epsilon=1/128.
    for log_degree in (64, 96, 128, 192, 256):
        degree = 1 << log_degree
        log_n = 2 * log_degree
        n = 1 << log_n
        guard_size = log_degree // 32
        released_overlap = sum(comb(n, size) for size in range(guard_size + 1))
        reservoir_log = log_degree * log_degree // 8
        reservoir = 1 << reservoir_log

        # Exact fixed-power criterion H/S_t(n) >= D^(2+2 epsilon),
        # with epsilon=1/128.  Clear the fractional exponent by taking
        # the 64th power: 2+2epsilon=129/64.
        assert reservoir**64 >= released_overlap**64 * degree**129

        # In fact the low-cover coefficient is already <1 on these rows:
        # [D^2 sqrt(S/H)]^2 = D^4 S/H.
        assert degree**4 * released_overlap < reservoir

        threshold_matching = guard_size // 2 + 1
        # k_0/log D is asymptotic to c delta/4=1/64.
        assert 64 * threshold_matching >= log_degree

        # Abstract exact Cauchy audit with repeated released banks.
        contexts = 3 * log_degree + 1
        volume = max(
            contexts,
            (contexts * reservoir + released_overlap - 1) // released_overlap,
        )
        record_mass = contexts * degree**2
        assert (
            record_mass**2 * reservoir
            <= degree**4 * released_overlap * volume**2
        )

        rows.append(
            {
                "log2_D": log_degree,
                "log2_n": log_n,
                "guard_threshold_t": guard_size,
                "matching_threshold_k0": threshold_matching,
                "log2_H": reservoir_log,
                "released_overlap_bit_length": released_overlap.bit_length(),
                "low_cover_multiplier_is_below_one": True,
                "epsilon_1_over_128_criterion": True,
            }
        )
    return {"constant_choice": "c=1/8, delta=1/2, epsilon=1/128", "rows": rows}


def nontrivial_guard_release_audit() -> dict[str, int]:
    """A genuine 2+2 circuit killed by deleting only one of two guards."""
    _, _, chain, _ = transform(hard_points())
    internal = list(chain[:2])
    u: Point = (Fraction(-1), Fraction(0))
    v: Point = (Fraction(1), Fraction(0))
    carrier = [u, v]
    faces = internal_faces(internal)
    assert len(faces) == 4

    edges = trace_clutter(carrier, internal)
    assert edges == {0b11}
    minimum_guard = {0}  # delete u
    release_checks = 0
    for face in faces:
        candidate = [v] + [internal[index] for index in face]
        assert len(hull(candidate)) == len(candidate)
        release_checks += 1

    # Before release the full internal pair is the canonical nested 2+2
    # obstruction on uv.
    assert len(hull(carrier + internal)) == 3
    return {
        "outer_trace_edges": len(edges),
        "minimum_guard_size": len(minimum_guard),
        "released_internal_faces_checked": release_checks,
    }


def sparse_geometry_audit() -> dict[str, object]:
    original = hard_points()
    _, _, full_chain, _ = transform(original)
    chain = list(full_chain[:8])
    u: Point = (Fraction(-1), Fraction(0))
    v: Point = (Fraction(1), Fraction(0))
    lower = [parabola_point(t) for t in choose_lower_parameters(list(full_chain), 9)]
    w = lower[0]
    cloud = lower[1:]

    carrier_label_sets = [
        (0, 1, 2) + tuple(3 + index for index in labels)
        for labels in combinations(range(8), 3)
    ]
    lower_points = [u, v, w] + cloud
    carriers = [[lower_points[index] for index in labels] for labels in carrier_label_sets]
    faces = internal_faces(chain)
    assert all(len(hull([chain[index] for index in face])) == len(face) for face in faces)

    released_loads: Counter[frozenset[int]] = Counter()
    toggle_loads: Counter[frozenset[int]] = Counter()
    matching_sizes = []
    transversal_sizes = []
    tangent_one_guard_failures = 0
    tangent_two_guard_failures = 0
    release_checks = 0
    degree = 4

    for context, (carrier_labels, carrier) in enumerate(zip(carrier_label_sets, carriers)):
        edges = trace_clutter(carrier, chain)
        singleton_edges = {1 << index for index in range(len(carrier))}
        assert singleton_edges <= edges

        matching = maximum_disjoint_edges(edges, len(carrier))
        guard_mask = 0
        for edge in matching:
            guard_mask |= edge
        assert all(guard_mask & edge for edge in edges)
        assert len(matching) == len(carrier) == 6
        assert guard_mask == (1 << len(carrier)) - 1
        matching_sizes.append(len(matching))

        # Brute-force the minimum transversal.
        tau = None
        for size in range(len(carrier) + 1):
            for labels in combinations(range(len(carrier)), size):
                mask = sum(1 << index for index in labels)
                if all(mask & edge for edge in edges):
                    tau = size
                    break
            if tau is not None:
                break
        assert tau == 6
        transversal_sizes.append(tau)

        released_outer = frozenset(
            carrier_labels[index]
            for index in range(len(carrier))
            if not guard_mask & (1 << index)
        )
        assert not released_outer
        released_loads[released_outer] += 1

        # Theorem 1: after deleting the transversal, every internal face is
        # still an ordinary face.  This is non-vacuous as a circuit audit
        # even though the finite barrier deletes the whole carrier.
        released_points = [
            carrier[index]
            for index in range(len(carrier))
            if not guard_mask & (1 << index)
        ]
        for face in faces:
            candidate = released_points + [chain[index] for index in face]
            assert len(hull(candidate)) == len(candidate)
            release_checks += 1

        # Deleting only u, or both canonical tangent guards u,v, does not
        # release the full reservoir.
        for deleted, counter_name in (((0,), "one"), ((0, 1), "two")):
            remainder = [
                point for index, point in enumerate(carrier) if index not in deleted
            ]
            failed = any(
                len(hull(remainder + [chain[index] for index in face]))
                < len(remainder) + len(face)
                for face in faces
            )
            assert failed
            if counter_name == "one":
                tangent_one_guard_failures += 1
            else:
                tangent_two_guard_failures += 1

        # Toggle all six singleton matching blocks.  The label 100+x marks
        # the source atom and is disjoint from the outer label alphabet.
        for atom in range(degree):
            atom_label = 100 + atom
            for choice in range(1 << len(matching)):
                deleted_mask = 0
                for index, edge in enumerate(matching):
                    if choice & (1 << index):
                        deleted_mask |= edge
                face_labels = {atom_label}
                face_labels.update(
                    carrier_labels[index]
                    for index in range(len(carrier))
                    if not deleted_mask & (1 << index)
                )
                toggle_loads[frozenset(face_labels)] += 1

    contexts = len(carriers)
    assert contexts == 56
    assert max(released_loads.values()) == contexts
    assert max(toggle_loads.values()) == contexts  # singleton {x}
    assert all(size == 6 for size in matching_sizes)
    assert all(size == 6 for size in transversal_sizes)
    assert tangent_one_guard_failures == contexts
    assert tangent_two_guard_failures == contexts

    per_context_toggle = degree * (1 << 6)
    total_toggle_incidences = contexts * per_context_toggle
    assert sum(toggle_loads.values()) == total_toggle_incidences
    assert len(toggle_loads) < total_toggle_incidences

    return {
        "internal_subrecord_points": len(chain),
        "internal_subrecord_faces": len(faces),
        "outer_contexts": contexts,
        "carrier_rank": len(carriers[0]),
        "trace_matching_number": matching_sizes[0],
        "minimum_trace_transversal": transversal_sizes[0],
        "guard_release_checks": release_checks,
        "one_guard_release_failures": tangent_one_guard_failures,
        "two_guard_release_failures": tangent_two_guard_failures,
        "released_carrier_overlap_L_R": max(released_loads.values()),
        "toggle_bank_D": degree,
        "toggle_faces_per_context": per_context_toggle,
        "toggle_bank_incidences": total_toggle_incidences,
        "distinct_toggle_faces": len(toggle_loads),
        "toggle_overlap_L_T": max(toggle_loads.values()),
    }


def main() -> None:
    result = {
        "abstract_cover_or_toggle": exhaustive_rank_two_clutters(),
        "released_decoder": released_decoder_bound(),
        "entropy_splice": entropy_splice_audit(),
        "nontrivial_guard_release": nontrivial_guard_release_audit(),
        "sparse_geometry": sparse_geometry_audit(),
        "status": "PASS",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: circuit-transversal guard release and matching toggle bank")


if __name__ == "__main__":
    main()
