#!/usr/bin/env python3
"""Exact audit for ONE_THREE_WRAPPER_APPLICABILITY_BARRIER.md."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent


def rooted_circuit_audit() -> dict[str, object]:
    sys.path.insert(0, str(HERE))
    try:
        import verify_dominance_cell_separated_one_gap as dominance

        inherited = dominance.rational_mixed_bank_counterexample()
    finally:
        sys.path.pop(0)

    u, v = (Q(-1), Q(0)), (Q(1), Q(0))
    q = (Q(-19, 20), Q(1, 20))
    x = (Q(-3, 40), Q(7, 8))
    w = (Q(0), Q(10, 11))
    z = (Q(3, 40), Q(7, 8))
    y = (Q(2, 15), Q(8, 9))
    points = (u, v, q, x, w, z, y)
    assert all(
        dominance.cross(*triple) != 0 for triple in combinations(points, 3)
    )

    interval = (x, z, y)
    assert dominance.convex(interval)
    assert not dominance.convex((q, *interval))
    assert dominance.convex((u, v, q, x, w, z))
    assert dominance.convex((u, v, q, x, w, y))
    assert not dominance.convex((u, v, q, *interval))

    weights = (Q(3, 230), Q(122, 575), Q(891, 1150))
    assert sum(weights) == 1
    assert tuple(
        weights[0] * q[i] + weights[1] * x[i] + weights[2] * y[i]
        for i in range(2)
    ) == z
    return {
        "inherited_dominance_audit": inherited,
        "interval_rank": len(interval),
        "interval_is_ordinary": True,
        "endpoint_plus_every_three_interval_labels_bad": True,
        "full_source_words_convex": 2,
        "one_gap_output_convex_without_root": False,
        "one_gap_output_convex_with_root": False,
        "hidden_label": "z",
        "barycentric_weights": [str(weight) for weight in weights],
    }


def conditional_wrapper_audit() -> dict[str, object]:
    wrapper_dir = HERE.parent / "agent_shield_circuit_cover"
    sys.path.insert(0, str(wrapper_dir))
    try:
        import verify_alternating_ferrers_planar_wrapper as wrapper

        coefficients = wrapper.coefficient_audit()
    finally:
        sys.path.pop(0)
    for record in coefficients["fixed_point_thresholds"]:
        threshold = Q(record["fixed_point_threshold"])
        assert threshold > Q(1, 2)
    return coefficients


def projective_universality_stress() -> dict[str, object]:
    universality_dir = HERE.parent / "agent_one_sided_reflection"
    sys.path.insert(0, str(universality_dir))
    try:
        import verify_singleton_reset_universality as universality

        source = universality.random_points(7, 838_153)
        result = universality.audit_source(source, "one_three_wrapper_random_child_n7")
    finally:
        sys.path.pop(0)
    assert result["rooted_coefficients"] == [1, 7, 0, 0, 0, 0, 0, 0]
    return result


def main() -> None:
    certificate = {
        "description": "rooted 1+3 atom versus lexicographic wrapper applicability",
        "rooted_rational_counterexample": rooted_circuit_audit(),
        "conditional_lexicographic_wrapper": conditional_wrapper_audit(),
        "projective_universality_stress": projective_universality_stress(),
        "claims": [
            "an exact endpoint-plus-three-label 1+3 atom can be the obstruction to the desired one-gap profile face",
            "strict reverse tangent dominance and convex full source words do not imply the omitted-cell splice",
            "under the additional lexicographic exposure hypothesis the recursive fixed-point threshold is strictly above one half",
            "arbitrary child face complexes survive projective singleton reset geometry",
        ],
    }
    output = Path(__file__).with_name("one_three_wrapper_applicability_certificate.json")
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
