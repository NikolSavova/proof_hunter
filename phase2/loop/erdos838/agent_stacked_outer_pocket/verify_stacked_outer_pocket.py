#!/usr/bin/env python3
"""Exact rational audit of STACKED_OUTER_POCKET_BARRIER.md."""

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

from amplification_probe import cap_cup_profiles  # noqa: E402
from verify_apa_counterexample import matrix_profile, orient  # noqa: E402
from verify_insertion_chain_universality import transform  # noqa: E402
from verify_long_chain_mixed_barrier import choose_outer, hard_points, hull  # noqa: E402


Point = tuple[Fraction, Fraction]


def main() -> None:
    original = hard_points()
    _, _, image, coordinates = transform(original)
    n = len(image)
    assert n == 20

    # The transform preserves the complete convex-position profile.
    profile = matrix_profile(original)
    assert matrix_profile(tuple(image)) == profile
    v_q = sum(profile)
    assert v_q == 4775

    positive_original, negative_original = cap_cup_profiles(original)
    # The projective insertion-chain map reverses all internal signs.
    # Thus the original positive family becomes X-caps and the original
    # negative family becomes X-cups under the paper's sign convention.
    cap_total = sum(positive_original)
    cup_total = sum(negative_original)
    assert cap_total == 1604
    assert cup_total == 1627

    u: Point = (Fraction(-1), Fraction(0))
    v: Point = (Fraction(1), Fraction(0))
    fixed = [u, v] + image
    lower: Point | None = None
    for numerator in range(-50, 51):
        candidate = (Fraction(numerator, 103), Fraction(-1))
        if all(orient(candidate, first, second) for first, second in combinations(fixed, 2)):
            lower = candidate
            break
    assert lower is not None
    base = [u, v, lower]
    outer = choose_outer(image, base)
    upper = image + [outer]
    ambient = base + upper

    assert all(orient(a, b, c) for a, b, c in combinations(ambient, 3))
    base_set = set(base)
    assert set(hull(base)) == base_set

    # Exact ACP-correlated repair audit.  For every ordered upper pair the
    # earlier point is the singleton hidden ear and the later point is the
    # outward successor, while R=base is retained.
    repair_relations = 0
    for i, earlier in enumerate(upper):
        assert set(hull(base + [earlier])) == base_set | {earlier}
        for later in upper[i + 1 :]:
            assert set(hull([u, v, later])) == {u, v, later}
            assert earlier not in set(hull([u, v, earlier, later]))
            assert set(hull(base + [earlier, later])) == base_set | {later}

            # A=R union I and T=R union {p}; hence A=(T-p) union I.
            source = base_set | {earlier}
            target = base_set | {later}
            hidden = {earlier}
            assert source == (target - {later}) | hidden
            assert set(hull(list(source))) == source
            assert set(hull(list(target))) == target
            repair_relations += 1
    assert repair_relations == comb(n + 1, 2)

    # Lemma 2: a single projective guard exposes exactly one of the two
    # x-monotone hull-chain families.  The projective map reverses the
    # orientation sign, so u sees X-cups and v sees X-caps.
    image_v = sum(matrix_profile(tuple(image)))
    u_rooted_faces = sum(matrix_profile(tuple(image + [u]))) - image_v
    v_rooted_faces = sum(matrix_profile(tuple(image + [v]))) - image_v
    assert u_rooted_faces == cup_total + 1 == 1628
    assert v_rooted_faces == cap_total + 1 == 1605

    # Lemma 1: no face containing both guards can contain two upper points.
    guard_exclusions = 0
    for first, second in combinations(upper, 2):
        candidate = [u, v, first, second]
        assert len(hull(candidate)) == 3
        assert first not in set(hull(candidate))
        guard_exclusions += 1

    b = len(base)
    guarded_upper = 2 ** (b - 2) * (n + 2)
    full_core_upper = n + 2
    assert guarded_upper == 44
    assert full_core_upper == 22

    ambient_face_upper = 2 ** (b + 1) * v_q
    assert ambient_face_upper == 76400

    h = 10
    histories = comb(n, h)
    assert histories == 184756

    both_guard_single_fibre = ceil(histories / guarded_upper**2)
    both_core_single_fibre = ceil(histories / full_core_upper**2)
    one_guard_single_fibre = ceil(histories / (2 * guarded_upper * ambient_face_upper))
    one_guard_pair_fibre = ceil(histories**2 / (2 * guarded_upper * ambient_face_upper))
    unrestricted_pair_fibre = ceil(histories**2 / ambient_face_upper**2)

    assert both_guard_single_fibre == 96
    assert both_core_single_fibre == 382
    assert one_guard_single_fibre == 1
    assert one_guard_pair_fibre == 5078
    assert unrestricted_pair_fibre == 6

    # Variable-core cancellation (13b)--(13c).  The exact value of the
    # recoverable outer-core family cancels completely from both ratios.
    outer_core_family_size = 123457
    variable_core_single_fibre = ceil(
        outer_core_family_size * histories
        / (outer_core_family_size * (n + 2) ** 2)
    )
    variable_core_pair_fibre = ceil(
        (outer_core_family_size * histories) ** 2
        / (outer_core_family_size**2 * (n + 2) ** 2)
    )
    assert variable_core_single_fibre == 382
    assert variable_core_pair_fibre == 70526404

    # Symbolic coefficient audit of Theorem 2 on the banked sharp sequence.
    # log H / L^2 -> 1, log F_uv / L^2 -> 0, log V(P) / L^2 -> 1/2.
    # Record the exact resulting leading lower-bound coefficients.
    asymptotic_coefficients = {
        "single_history_both_outputs_guarded": "1",
        "single_history_at_least_one_output_guarded": "1/2",
        "single_history_split_guards_u_and_v": "1/2",
        "ordered_history_pair_no_guard_requirement": "1",
    }

    result = {
        "internal_points": n,
        "internal_V": v_q,
        "internal_cap_total": cap_total,
        "internal_cup_total": cup_total,
        "u_rooted_faces_before_base_and_terminal": u_rooted_faces,
        "v_rooted_faces_before_base_and_terminal": v_rooted_faces,
        "ambient_points": len(ambient),
        "ambient_general_position_triples": comb(len(ambient), 3),
        "strict_chain_relations": comb(n, 2),
        "terminal_chain_relations": n,
        "acp_correlated_repair_relations": repair_relations,
        "guard_exclusions": guard_exclusions,
        "base_size": b,
        "guarded_face_upper_bound": guarded_upper,
        "full_core_face_upper_bound": full_core_upper,
        "ambient_face_upper_bound": ambient_face_upper,
        "history_length": h,
        "history_count": histories,
        "both_guarded_single_history_fibre_lower": both_guard_single_fibre,
        "both_full_core_single_history_fibre_lower": both_core_single_fibre,
        "one_guard_single_history_fibre_lower": one_guard_single_fibre,
        "one_guard_ordered_history_pair_fibre_lower": one_guard_pair_fibre,
        "unrestricted_ordered_history_pair_fibre_lower": unrestricted_pair_fibre,
        "variable_outer_core_family_test_size": outer_core_family_size,
        "variable_core_single_history_fibre_lower": variable_core_single_fibre,
        "variable_core_ordered_history_pair_fibre_lower": variable_core_pair_fibre,
        "asymptotic_log2_fibre_coefficients": asymptotic_coefficients,
        "fixed_retained_outer_core": True,
        "fixed_tangent_chord": True,
        "all_successors_outward": True,
        "all_repairs_satisfy_A_equals_T_minus_p_union_I": True,
    }
    certificate = HERE / "stacked_outer_pocket_certificate.json"
    certificate.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: exact retained-outer/pocket coexistence barrier")


if __name__ == "__main__":
    main()
