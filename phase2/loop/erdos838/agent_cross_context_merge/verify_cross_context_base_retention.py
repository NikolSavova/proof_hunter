#!/usr/bin/env python3
"""Exact audit of CROSS_CONTEXT_BASE_RETENTION_BARRIER.md."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from itertools import combinations
from math import ceil, comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
CHAIN = ERDOS / "agent_cyclic_stem_hw"
MIXED = ERDOS / "agent_recursive_pocket_induction"
APA = ERDOS / "agent_apa_rank"
for directory in (CHAIN, MIXED, APA):
    sys.path.insert(0, str(directory))

from verify_apa_counterexample import matrix_profile, orient  # noqa: E402
from verify_insertion_chain_universality import transform  # noqa: E402
from verify_long_chain_mixed_barrier import hard_points, hull  # noqa: E402


Point = tuple[Fraction, Fraction]


def choose_lower(points: list[Point]) -> Point:
    fixed = [(Fraction(-1), Fraction(0)), (Fraction(1), Fraction(0))] + points
    for numerator in range(-100, 101):
        candidate = (Fraction(numerator, 211), Fraction(-1))
        if all(orient(candidate, first, second) for first, second in combinations(fixed, 2)):
            return candidate
    raise AssertionError("no generic rational lower vertex found")


def main() -> None:
    original = hard_points()
    _, _, chain, tangent_coordinates = transform(original)
    assert len(chain) == 20

    u: Point = (Fraction(-1), Fraction(0))
    v: Point = (Fraction(1), Fraction(0))
    lower = choose_lower(chain)
    base = [u, v, lower]
    base_set = set(base)
    ambient = base + chain

    assert all(orient(a, b, c) for a, b, c in combinations(ambient, 3))
    assert set(hull(base)) == base_set

    # The projective coordinates certify strict fixed-edge nesting exactly.
    strict_nesting = 0
    for i, earlier in enumerate(chain):
        left_i, right_i = tangent_coordinates[i]
        for j in range(i + 1, len(chain)):
            later = chain[j]
            left_j, right_j = tangent_coordinates[j]
            height_i = earlier[1]
            barycentric = (
                height_i * (right_i - right_j) / 2,
                height_i * (left_i - left_j) / 2,
                height_i * (left_j + right_j) / 2,
            )
            assert all(value > 0 for value in barycentric)
            assert sum(barycentric) == 1
            assert earlier not in set(hull([u, v, earlier, later]))
            assert set(hull(base + [earlier, later])) == base_set | {later}
            strict_nesting += 1
    assert strict_nesting == comb(20, 2)

    # Ten source atoms, each with the ten later tips as selected blockers.
    d = 10
    sources = chain[:d]
    blockers = chain[d:]
    repair_relations = 0
    nonaddable_checks = 0
    for i, source_tip in enumerate(sources):
        source = base + [source_tip]
        assert set(hull(source)) == base_set | {source_tip}

        # Every other chain point is nonaddable: an earlier point is already
        # interior, while a later point hides the source tip.
        for k, other in enumerate(chain):
            if other == source_tip:
                continue
            candidate = source + [other]
            assert len(hull(candidate)) < len(candidate)
            if k < i:
                assert other not in set(hull(candidate))
            elif k > i:
                assert source_tip not in set(hull(candidate))
            nonaddable_checks += 1

        for blocker in blockers:
            assert set(hull(source + [blocker])) == base_set | {blocker}
            repair_relations += 1
    assert repair_relations == d * d
    assert nonaddable_checks == d * (len(chain) - 1)

    # A face containing the complete base has zero or one chain tip.
    for tip in chain:
        assert set(hull(base + [tip])) == base_set | {tip}
    guard_exclusions = 0
    for first, second in combinations(chain, 2):
        candidate = base + [first, second]
        assert len(hull(candidate)) == len(base) + 1
        guard_exclusions += 1
    base_retaining_faces = len(chain) + 1
    assert base_retaining_faces == 2 * d + 1

    beta = [d] * d
    mass = sum(beta)
    root_square = mass * mass
    child_square = sum(value * value for value in beta)
    cross_atom_square = root_square - child_square
    assert mass == d * d
    assert child_square == d**3
    assert cross_atom_square == d**3 * (d - 1)

    cross_pair_fibre = ceil(cross_atom_square / base_retaining_faces**2)
    all_pair_fibre = ceil(root_square / base_retaining_faces**2)
    assert cross_pair_fibre == 21
    assert all_pair_fibre == 23

    # Theorem 2: after one bank releases the base, the exact internal face
    # reservoir pays many contexts with balanced overlap.
    internal_faces = sum(matrix_profile(tuple(chain)))
    assert internal_faces == 4775
    first_bank = 2 * d
    released_bank_per_context = ceil(d**4 / first_bank)
    assert released_bank_per_context == 500

    released_allocations: list[dict[str, int]] = []
    for contexts, expected_overlap in ((9, 1), (10, 2), (37, 4)):
        loads = [0] * internal_faces
        for context in range(contexts):
            start = context * released_bank_per_context
            block = {
                (start + offset) % internal_faces
                for offset in range(released_bank_per_context)
            }
            assert len(block) == released_bank_per_context
            for face_index in block:
                loads[face_index] += 1
        overlap = max(loads)
        assert overlap == ceil(contexts * released_bank_per_context / internal_faces)
        assert overlap == expected_overlap
        assert first_bank * released_bank_per_context >= d**4
        released_allocations.append({
            "contexts": contexts,
            "released_faces_per_context": released_bank_per_context,
            "maximum_released_face_overlap": overlap,
        })

    # Exact symbolic seam audit.  Here D=2^r, n=2^(2r), |B|=r-1,
    # and the remaining points can be padded inside conv(B).
    seam_rows: list[dict[str, int]] = []
    for rank in range(4, 65):
        cap = 1 << rank
        n = 1 << (2 * rank)
        chain_points = 2 * cap
        padding = n - (rank - 1) - chain_points
        assert padding > 0
        assert n // (1 << rank) == cap

        bank = chain_points + 1
        symbolic_mass = cap * cap
        symbolic_root_square = symbolic_mass**2
        symbolic_child_square = cap**3
        symbolic_cross = symbolic_root_square - symbolic_child_square
        cauchy_product_numerator = symbolic_root_square
        cauchy_product_denominator = bank**2

        # (17) and (15), without floating point.
        assert 9 * cauchy_product_numerator >= cap**2 * cauchy_product_denominator
        assert 18 * symbolic_cross >= cap**2 * bank**2

        if rank in (4, 8, 16, 32, 64):
            seam_rows.append({
                "rank": rank,
                "ambient_n": n,
                "selected_cap_D": cap,
                "chain_points": chain_points,
                "interior_padding_points": padding,
                "base_retaining_faces": bank,
                "record_mass": symbolic_mass,
                "child_square": symbolic_child_square,
                "cross_atom_square": symbolic_cross,
            })

    result = {
        "finite_chain_points": len(chain),
        "finite_base_size": len(base),
        "finite_general_position_triples": comb(len(ambient), 3),
        "finite_strict_nesting_relations": strict_nesting,
        "finite_selected_degree_D": d,
        "finite_sources": len(sources),
        "finite_repair_records": repair_relations,
        "finite_nonaddable_chain_checks": nonaddable_checks,
        "finite_full_base_face_count": base_retaining_faces,
        "finite_guard_exclusions": guard_exclusions,
        "finite_atom_weights": beta,
        "finite_parent_square": root_square,
        "finite_sum_child_squares": child_square,
        "finite_cross_atom_square": cross_atom_square,
        "finite_cross_pair_fibre_lower": cross_pair_fibre,
        "finite_all_pair_fibre_lower": all_pair_fibre,
        "finite_released_internal_face_reservoir": internal_faces,
        "finite_released_first_bank_size": first_bank,
        "finite_released_faces_needed_per_context": released_bank_per_context,
        "finite_released_balanced_allocations": released_allocations,
        "symbolic_seam_rows": seam_rows,
        "symbolic_cauchy_product_lower": "D^4/(2D+1)^2 >= D^2/9",
        "symbolic_cross_pair_fibre_lower": "D^3(D-1)/(2D+1)^2 >= D^2/18",
        "is_counterexample_to_base_retaining_two_bank_telescope": True,
        "is_counterexample_to_fixed_power_EIC_prime": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: exact cross-context base-retention barrier")


if __name__ == "__main__":
    main()
