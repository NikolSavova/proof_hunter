#!/usr/bin/env python3
"""Quantitative and dependency audit for END_TO_END_QUASIPOLY_GATE_AUDIT.md."""

from fractions import Fraction as Q
from math import comb, log2


def deletion_identity_audit(maximum_n=40):
    # Abstract downsets: enumerate all subfaces of one rank-r maximum face.
    systems = 0
    for n in range(3, maximum_n + 1):
        for rank in range(n + 1):
            faces_by_size = [comb(rank, k) for k in range(rank + 1)]
            face_count = sum(faces_by_size)
            rank_sum = sum(k * faces_by_size[k] for k in range(rank + 1))
            deletion_sum = sum((n - k) * faces_by_size[k]
                               for k in range(rank + 1))
            assert deletion_sum == n * face_count - rank_sum
            assert face_count == 2 ** rank
            systems += 1
    return systems


def fixed_gap_mean_audit():
    systems = 0
    for n in [16, 32, 64, 128, 256, 512, 1024, 4096]:
        current_log = log2(n)
        previous_log = log2(n - 1)
        for c in [0.20, 0.25, 0.40, 0.49]:
            exponent_gap = c * (current_log ** 2 - previous_log ** 2)
            mean_upper = n * (1 - 2 ** (-exponent_gap))
            analytic_upper = 2 * c * current_log * n / (n - 1)
            assert mean_upper <= analytic_upper + 1e-12
            assert analytic_upper <= 4 * c * current_log
            systems += 1
    return systems


def pocket_and_recovery_audit():
    systems = 0
    for log_n in range(20, 101, 5):
        n = 2 ** log_n
        mean_rank = 2 * log_n
        maximum_rank = Q(1, 2) * log_n * log_n
        pocket = Q(n - 2 * mean_rank, 1) / (
            8 * (maximum_rank - 2) * mean_rank
        )
        assert pocket > Q(n, 20 * log_n ** 3)
        pocket_log_lower = log_n - log2(20 * log_n ** 3)
        coefficient = Q(49, 100)
        loss = float(coefficient) * (
            log_n * log_n - pocket_log_lower * pocket_log_lower
        )
        assert loss > 0
        assert loss < 20 * log_n * log2(log_n)
        systems += 1
    return systems


def terminal_scale_audit():
    systems = 0
    # If kappa_A <= n^C, the terminal theorem costs exponent C+3/2+o(1).
    for description_exponent in range(0, 11):
        for sigma_num in range(1, 6):
            sigma = Q(sigma_num, 10)
            threshold = Q(2 * description_exponent + 4, 2 * sigma)
            # Any loglog n beyond this threshold dominates the polynomial.
            loglog_n = int(threshold) + 2
            recovery_exponent = sigma * loglog_n
            polynomial_exponent = Q(2 * description_exponent + 3, 2)
            assert recovery_exponent > polynomial_exponent
            systems += 1
    return systems


def dependency_ledger_audit():
    status = {
        "fixed_gap_minimizer": "proved",
        "rank_safe_marked_pocket": "proved",
        "large_guard_matching": "proved",
        "complete_product_promotion": "open",
        "blocker_cover_local": "proved",
        "mixed_seam_reset_conditional_chart": "proved",
        "bad_pair_classification": "proved",
        "endpoint_hall_reductions": "proved",
        "rooted_to_dense_context_promotion": "open",
        "polynomial_description_load": "open",
        "source_triangle_terminal": "proved",
        "half_theorem": "open",
    }
    prerequisites = {
        "half_theorem": [
            "fixed_gap_minimizer",
            "rank_safe_marked_pocket",
            "large_guard_matching",
            "complete_product_promotion",
            "blocker_cover_local",
            "mixed_seam_reset_conditional_chart",
            "bad_pair_classification",
            "endpoint_hall_reductions",
            "rooted_to_dense_context_promotion",
            "polynomial_description_load",
            "source_triangle_terminal",
        ]
    }
    assert status["source_triangle_terminal"] == "proved"
    unresolved = [node for node in prerequisites["half_theorem"]
                  if status[node] != "proved"]
    assert unresolved == [
        "complete_product_promotion",
        "rooted_to_dense_context_promotion",
        "polynomial_description_load",
    ]
    assert status["half_theorem"] == "open"
    return tuple(unresolved)


def main():
    deletion = deletion_identity_audit()
    means = fixed_gap_mean_audit()
    pockets = pocket_and_recovery_audit()
    scales = terminal_scale_audit()
    unresolved = dependency_ledger_audit()
    print(
        "PASS: deletion=%d mean=%d pocket=%d scale=%d unresolved=%s"
        % (deletion, means, pockets, scales, unresolved)
    )


if __name__ == "__main__":
    main()
