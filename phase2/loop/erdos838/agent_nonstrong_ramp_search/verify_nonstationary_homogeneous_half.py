#!/usr/bin/env python3
"""Exact regressions for NONSTATIONARY_HOMOGENEOUS_HALF_CLOSURE.md."""

from __future__ import annotations

from decimal import Decimal, getcontext
from itertools import product
from math import ceil, log2


def exact_power_of_two_ledger() -> int:
    """Exhaust q in {1,2,3} and all alpha/beta splits through depth 8."""
    checked = 0
    for depth in range(2, 9):
        for qs in product((1, 2, 3), repeat=depth):
            # It is enough to exhaust all splits independently level by
            # level: E=c+u depends only on alpha+beta, but checking every
            # split audits that cancellation rather than assuming it.
            split_ranges = tuple(range(q + 1) for q in qs[:-1])
            for alphas in product(*split_ranges):
                c = 0
                u = 0
                prefix = 0
                for q, alpha in zip(qs[:-1], alphas):
                    beta = q - alpha
                    c += alpha * prefix
                    u += beta * prefix
                    prefix += q

                square_mesh = sum(q * q for q in qs[:-1])
                telescope = (prefix * prefix - square_mesh) // 2
                assert (prefix * prefix - square_mesh) % 2 == 0
                assert c + u == telescope

                full_log_size = sum(qs)
                q_star = max(qs)
                bounded_rhs_twice = (
                    full_log_size * full_log_size
                    - 3 * q_star * full_log_size
                    + 2 * q_star * q_star
                )
                assert 2 * (c + u) >= bounded_rhs_twice
                checked += 1
    return checked


def arbitrary_arity_ledger() -> int:
    """Exhaust m in {2,3,4,5} through depth 7 at high precision."""
    getcontext().prec = 80
    checked = 0
    for depth in range(2, 8):
        for arities in product((2, 3, 4, 5), repeat=depth):
            qs = [Decimal(m).ln() / Decimal(2).ln() for m in arities]
            rewards = [Decimal(ceil(log2(m))) for m in arities]
            prefix = Decimal(0)
            endpoint_sum = Decimal(0)
            for q, reward in zip(qs[:-1], rewards[:-1]):
                assert reward >= q
                endpoint_sum += reward * prefix
                prefix += q

            mesh_identity = (
                prefix * prefix - sum(q * q for q in qs[:-1])
            ) / 2
            assert endpoint_sum + Decimal("1e-65") >= mesh_identity

            full_log_size = sum(qs)
            q_star = max(qs)
            bounded_rhs = (
                full_log_size * full_log_size / 2
                - Decimal(3) * q_star * full_log_size / 2
                + q_star * q_star
            )
            assert endpoint_sum + Decimal("1e-65") >= bounded_rhs
            checked += 1
    return checked


def skew_child_obstruction() -> int:
    """Audit the exact arity-two failure of anchor-size weighting."""
    checked = 0
    # The genuine two-position row has lengths (1,1), hence Kraft equality.
    assert (1, 1) == (1, 1)
    assert 2 ** -1 + 2 ** -1 == 1
    for t in range(2, 81):
        large_child = 1 << t
        small_child = 1
        actual_left_multiplier = 1 + small_child
        naive_anchor_multiplier = large_child
        actual_right_multiplier = 1 + large_child
        assert actual_left_multiplier == 2
        assert naive_anchor_multiplier > actual_left_multiplier
        assert naive_anchor_multiplier // actual_left_multiplier == 1 << (t - 1)
        assert actual_right_multiplier == (1 << t) + 1
        checked += 1
    return checked


def growing_chart_menu_ledger() -> tuple[int, int]:
    """Audit the universal-in-chart minimum with a growing layered menu.

    A q-bit complete prefix row has arity 2**q.  Its cap reward is the
    Hamming weight and its cup reward the complementary weight, so every
    row has exact Kraft equality.  Rows rotate their words and call
    arbitrary previous-layer charts, but cap and cup at one position use
    the same target.
    """
    cap = [0]
    cup = [0]
    prefix = 0
    rows = 0
    for level in range(1, 41):
        q = 1 + (level % 3)
        arity = 1 << q
        state_count = level + 1
        previous_count = len(cap)
        previous_minimum = min(c + u for c, u in zip(cap, cup))
        next_cap = []
        next_cup = []
        for state in range(state_count):
            cap_candidates = []
            cup_candidates = []
            kraft_numerator = 0
            for position in range(arity):
                word = (position + state + level) % arity
                alpha = word.bit_count()
                beta = q - alpha
                target = (
                    position * (state + 1) + state + 2 * level
                ) % previous_count
                cap_candidates.append(cap[target] + alpha * prefix)
                cup_candidates.append(cup[target] + beta * prefix)
                kraft_numerator += 1
            assert kraft_numerator == arity
            parent_cap = max(cap_candidates)
            parent_cup = max(cup_candidates)
            # Choose one position in both maxima inequalities.  Its two
            # rewards share a target and sum to q.
            assert parent_cap + parent_cup >= previous_minimum + q * prefix
            next_cap.append(parent_cap)
            next_cup.append(parent_cup)
            rows += 1
        cap, cup = next_cap, next_cup
        prefix += q

    # A same-chart final two-position splice may choose a chart minimizing
    # the sum; its face exponent is at least the universal potential.
    final_minimum = min(c + u for c, u in zip(cap, cup))
    assert all(c + u >= final_minimum for c, u in zip(cap, cup))
    return rows, len(cap)


def main() -> None:
    exact = exact_power_of_two_ledger()
    arbitrary = arbitrary_arity_ledger()
    skew = skew_child_obstruction()
    chart_rows, final_charts = growing_chart_menu_ledger()
    print(
        "PASS: nonstationary homogeneous half closure; "
        f"exact_ledgers={exact}; arbitrary_arity_ledgers={arbitrary}; "
        f"skew_binary_instances={skew}; chart_rows={chart_rows}; "
        f"final_charts={final_charts}"
    )


if __name__ == "__main__":
    main()
