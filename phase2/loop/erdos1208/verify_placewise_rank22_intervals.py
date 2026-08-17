#!/usr/bin/env python3
"""Exact rational-log envelope certificate for the rank-22 target 0.498."""

from __future__ import annotations

import verify_placewise_rank20_intervals as core
from verify_placewise_rank22 import ALPHA, SPLIT_PRIMES, W0, exact_checks


def main() -> None:
    # Reuse the generic rational interval machinery with the rank-22 data.
    core.ALPHA = ALPHA
    core.SPLIT_PRIMES = SPLIT_PRIMES
    core.W0 = W0
    discriminant_bound = exact_checks()
    items, cost_logs, gain_logs, values = core.build_items()

    right_target = 2 * ALPHA * (2 * W0)
    right_position, _, _, _ = core.locate_endpoint(
        items, cost_logs, right_target
    )
    used_depth = [0] * len(SPLIT_PRIMES)
    previous_efficiency = None
    for _, prime_index, depth in items[: right_position + 1]:
        assert depth == used_depth[prime_index] + 1
        used_depth[prime_index] = depth
        q = SPLIT_PRIMES[prime_index]
        efficiency = core.ratio_bounds_positive(
            gain_logs[(prime_index, depth)], cost_logs[q]
        )
        if previous_efficiency is not None:
            assert previous_efficiency[0] >= efficiency[1]
        previous_efficiency = efficiency

    left = core.certify_endpoint(
        items, cost_logs, gain_logs, values, discriminant_bound, W0
    )
    right = core.certify_endpoint(
        items, cost_logs, gain_logs, values, discriminant_bound, 2 * W0
    )
    print("exact arithmetic tower checks: PASS")
    print("certified monotone frontier items:", right_position + 1)
    print("left segment:", left[:3], "margin lower:", core.as_decimal(left[3]))
    print("right segment:", right[:3], "margin lower:", core.as_decimal(right[3]))
    print("rank-22 target F_2(n) << n^0.498: CERTIFIED")


if __name__ == "__main__":
    main()
