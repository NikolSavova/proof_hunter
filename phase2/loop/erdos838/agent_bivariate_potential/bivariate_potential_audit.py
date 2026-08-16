#!/usr/bin/env python3
"""Exact audits for the bivariate QuickHull/APA lane of Erdos 838.

The script checks four facts used in REPORT.md:

* the mixed cap/cup polynomial specializes to the convex-face polynomial;
* its elementary four-corner interaction is nonnegative;
* a tempting scalar use of the mixed corners already fails on an exact
  stretchable twenty-point record;
* the rooted QuickHull slack has the stated excluded-pivot recurrence.

All geometric predicates and all displayed ratios are exact.
"""

from __future__ import annotations

import itertools
import json
import random
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "agent_reflection_gate"))
sys.path.insert(0, str(ROOT / "agent_tangent_restart"))
sys.path.insert(0, str(ROOT / "agent_tilted_switch"))

import reflection_order_gate as gate  # noqa: E402
from tangent_restart_audit import pivot_parts, rooted_profile  # noqa: E402
from tilted_switch_audit import face_table, orient  # noqa: E402


def matrix_value(n: int, roots, z: Q) -> list[list[Q]]:
    matrix = [[Q(i == j) for j in range(n)] for i in range(n)]
    for i, j in roots:
        matrix[j] = [a + z * b for a, b in zip(matrix[j], matrix[i])]
    return matrix


def matrix_value_derivative(n: int, roots, z: Q):
    matrix = [[Q(i == j) for j in range(n)] for i in range(n)]
    derivative = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i, j in roots:
        old_row = matrix[j]
        old_derivative = derivative[j]
        matrix[j] = [a + z * b for a, b in zip(old_row, matrix[i])]
        derivative[j] = [
            a + b + z * c
            for a, b, c in zip(old_derivative, matrix[i], derivative[i])
        ]
    return matrix, derivative


def inner(left, right) -> Q:
    return sum(
        (left[i][j] * right[i][j] for i in range(len(left)) for j in range(len(left))),
        Q(0),
    )


def mixed_corners(n: int, roots):
    forward_one = matrix_value(n, roots, Q(1))
    forward_half = matrix_value(n, roots, Q(1, 2))
    backward_one = matrix_value(n, tuple(reversed(roots)), Q(1))
    backward_half = matrix_value(n, tuple(reversed(roots)), Q(1, 2))

    # Subtract the n diagonal empty-path pairs.  What remains starts with the
    # universal two-point term xy * binom(n,2).
    k11 = inner(backward_one, forward_one) - n
    k1h = inner(backward_one, forward_half) - n
    kh1 = inner(backward_half, forward_one) - n
    khh = inner(backward_half, forward_half) - n
    interaction = k11 + khh - k1h - kh1
    direct_interaction = sum(
        (
            (backward_one[i][j] - backward_half[i][j])
            * (forward_one[i][j] - forward_half[i][j])
            for i in range(n)
            for j in range(n)
        ),
        Q(0),
    )
    assert interaction == direct_interaction and interaction >= 0
    return k11, k1h, kh1, khh, interaction


def z_and_derivative(n: int, roots, z: Q) -> tuple[Q, Q]:
    forward, dforward = matrix_value_derivative(n, roots, z)
    backward, dbackward = matrix_value_derivative(n, tuple(reversed(roots)), z)
    product = inner(backward, forward)
    derivative = inner(dbackward, forward) + inner(backward, dforward)
    return 1 + n * z + product - n, n + derivative


def planar_twenty_corner_barrier() -> dict[str, object]:
    source = ROOT / "agent_coxeter_half_weight" / "planar_seed_n20.json"
    raw = json.loads(source.read_text())
    n = int(raw["n"])
    word = tuple(map(int, raw["word_zero_based"]))
    roots = gate.root_sequence(n, word)
    k11, k1h, kh1, khh, interaction = mixed_corners(n, roots)

    z1, dz1 = z_and_derivative(n, roots, Q(1))
    zh, dzh = z_and_derivative(n, roots, Q(1, 2))
    assert z1 == 1 + n + k11
    assert zh == 1 + Q(n, 2) + khh

    # This was the simplest way to turn the positive interaction into a
    # tangent payment.  It is false even in the stretchable class.
    proposed_lhs = n * khh
    proposed_rhs = 2 * (k1h + kh1)
    assert proposed_lhs > proposed_rhs

    apa_lhs = n * zh + Q(n - 1, 2) * dzh
    apa_rhs = 2 * dz1
    assert apa_lhs < apa_rhs

    # Independently certify that this saved word is the exact slope order of
    # the stored integer-coordinate record.
    records = json.loads(
        (ROOT / "agent_dual_number_amortization" / "half_weight_search_records.json").read_text()
    )
    ys = tuple(map(int, records["exact_records"][str(n)][f"y_at_x_0_through_{n-1}"]))
    slopes = sorted(
        (Q(ys[j] - ys[i], j - i), i, j)
        for i in range(n)
        for j in range(i + 1, n)
    )
    coordinate_roots = tuple((i, j) for _, i, j in slopes)
    assert gate.word_from_roots(n, coordinate_roots) == word

    return {
        "n": n,
        "stretchable_fixed_x_integer_certificate": True,
        "K_11": str(k11),
        "K_1h": str(k1h),
        "K_h1": str(kh1),
        "K_hh": str(khh),
        "four_corner_interaction": str(interaction),
        "false_mixed_payment_rhs_over_lhs": str(proposed_rhs / proposed_lhs),
        "APA_ratio": str(apa_lhs / apa_rhs),
    }


def polynomial_value(profile: list[int], z: Q) -> Q:
    return sum((Q(value) * z**degree for degree, value in enumerate(profile)), Q(0))


def compatibility_graph_barrier() -> dict[str, object]:
    """Kill the claim that rooted chains are graph cliques."""
    u, v = (0, 0), (100_000, 0)
    points = [(110_597, 138_659), (16_176, 148_701), (87_080, 127_172)]
    all_points = [u, v] + points
    assert all(
        orient(all_points[i], all_points[j], all_points[k])
        for i, j, k in itertools.combinations(range(5), 3)
    )
    profile = rooted_profile(u, v, points)
    # Empty, all three singletons, all three pairs, but not the triple.
    assert profile == [1, 3, 3]
    return {
        "roots": [list(u), list(v)],
        "pocket_points": [list(point) for point in points],
        "rooted_profile": profile,
        "all_pair_compatibilities": True,
        "three_clique_is_not_a_rooted_chain": True,
    }


def local_pivot_barrier() -> dict[str, object]:
    """Exact visible-chain counterexample to pointwise slack monotonicity."""
    chain_size = 12
    last = chain_size - 1
    chain = [(i, i * (last - i)) for i in range(chain_size)]
    apex = (-1, chain_size * chain_size)
    u, v = chain[0], chain[-1]
    points = [apex] + chain[1:-1]
    m = len(points)
    x, left, right, discarded = pivot_parts(u, v, points)
    assert x == apex and not left and not right and set(discarded) == set(chain[1:-1])

    without = chain[1:-1]
    r_zero_half = polynomial_value(rooted_profile(u, v, without), Q(1, 2))
    delta_v = Q(sum(face_table(points)) - sum(face_table(without)))
    a_one = a_half = Q(1)
    local_margin = delta_v + a_one - r_zero_half - Q(m, 2) * a_half
    assert delta_v == 56
    assert r_zero_half == Q(59049, 1024)
    assert local_margin == Q(-6313, 1024)

    full_profile = rooted_profile(u, v, points)
    r_one = polynomial_value(full_profile, Q(1))
    r_half = polynomial_value(full_profile, Q(1, 2))
    v_one = Q(sum(face_table(points)))
    rooted_ratio = m * r_half / (r_one + v_one)
    assert rooted_ratio < 1
    return {
        "chain_size": chain_size,
        "rooted_points_m": m,
        "Delta_V": str(delta_v),
        "R_zero_half": str(r_zero_half),
        "pointwise_pivot_margin": str(local_margin),
        "pointwise_pivot_inequality": False,
        "global_rooted_ratio": str(rooted_ratio),
        "global_rooted_inequality_still_passes": True,
    }


def random_upper_instance(seed: int, m: int):
    rng = random.Random(seed)
    u, v = (0, 0), (100_000, 0)
    while True:
        points = [
            (rng.randrange(-50_000, 150_001), rng.randrange(1, 200_001))
            for _ in range(m)
        ]
        all_points = [u, v] + points
        if len(set(all_points)) == len(all_points) and all(
            orient(all_points[i], all_points[j], all_points[k])
            for i, j, k in itertools.combinations(range(m + 2), 3)
        ):
            return u, v, points


def rooted_slack_audit(records_per_size: int = 20, max_m: int = 12) -> dict[str, object]:
    maximum_ratio = Q(0)
    maximum_record = None
    recurrence_checks = 0
    for m in range(3, max_m + 1):
        for offset in range(records_per_size):
            seed = 50_000 + 1_000 * m + offset
            u, v, points = random_upper_instance(seed, m)
            profile = rooted_profile(u, v, points)
            r_one = polynomial_value(profile, Q(1))
            r_half = polynomial_value(profile, Q(1, 2))
            v_one = Q(sum(face_table(points)))
            ratio = m * r_half / (r_one + v_one)
            if ratio > maximum_ratio:
                maximum_ratio = ratio
                maximum_record = {
                    "m": m,
                    "seed": seed,
                    "rooted_profile": profile,
                    "V": int(v_one),
                }

            x, left, right, _discarded = pivot_parts(u, v, points)
            without = [q for q in points if q != x]
            profile_zero = rooted_profile(u, v, without)
            profile_left = rooted_profile(u, x, left)
            profile_right = rooted_profile(x, v, right)
            zero_half = polynomial_value(profile_zero, Q(1, 2))
            left_one = polynomial_value(profile_left, Q(1))
            right_one = polynomial_value(profile_right, Q(1))
            left_half = polynomial_value(profile_left, Q(1, 2))
            right_half = polynomial_value(profile_right, Q(1, 2))
            v_without = Q(sum(face_table(without)))
            delta_v = v_one - v_without

            slack = r_one + v_one - m * r_half
            old_slack = (
                polynomial_value(profile_zero, Q(1))
                + v_without
                - (m - 1) * zero_half
            )
            recurrence_rhs = (
                old_slack
                - zero_half
                + left_one * right_one
                - Q(m, 2) * left_half * right_half
                + delta_v
            )
            assert slack == recurrence_rhs
            assert delta_v >= left_one * right_one
            recurrence_checks += 1

    # This is finite evidence for the C=1 rooted conjecture, not a proof.
    assert maximum_ratio < 1
    return {
        "status": "finite_pass_only",
        "records": recurrence_checks,
        "maximum_m": max_m,
        "maximum_m_Rh_over_R1_plus_V": str(maximum_ratio),
        "maximum_record": maximum_record,
    }


def apa_boundary_identity() -> dict[str, object]:
    source = ROOT / "agent_coxeter_half_weight" / "planar_seed_n20.json"
    raw = json.loads(source.read_text())
    n = int(raw["n"])
    word = tuple(map(int, raw["word_zero_based"]))
    evaluation = gate.evaluate_word(n, word, graded=True)
    assert evaluation.graded is not None
    profile = [1] + list(evaluation.graded[1:])
    profile.extend([0] * (n + 1 - len(profile)))
    zh = polynomial_value(profile, Q(1, 2))
    dzh = sum((Q(k * value, 2 ** (k - 1)) for k, value in enumerate(profile) if k), Q(0))
    dz1 = sum(Q(k * value) for k, value in enumerate(profile))
    apa_lhs = n * zh + Q(n - 1, 2) * dzh
    apa_rhs = 2 * dz1

    boundaries = []
    for r in range(n + 1):
        next_value = profile[r + 1] if r + 1 < len(profile) else 0
        boundaries.append((n - r) * profile[r] - (r + 1) * next_value)
    boundary_lhs = sum((Q(value, 2**r) for r, value in enumerate(boundaries)), Q(0))
    boundary_rhs = 2 * dz1 - Q(n + 2, 2) * dzh
    assert apa_rhs - apa_lhs == boundary_rhs - boundary_lhs
    return {
        "n": n,
        "profile": profile,
        "APA_ratio": str(apa_lhs / apa_rhs),
        "weighted_boundary": str(boundary_lhs),
        "available_derivative_credit": str(boundary_rhs),
        "identity_checked": True,
    }


def main() -> None:
    result = {
        "planar_twenty_corner_barrier": planar_twenty_corner_barrier(),
        "compatibility_graph_barrier": compatibility_graph_barrier(),
        "local_pivot_barrier": local_pivot_barrier(),
        "rooted_slack": rooted_slack_audit(),
        "APA_boundary_identity": apa_boundary_identity(),
    }
    (HERE / "certificate.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
