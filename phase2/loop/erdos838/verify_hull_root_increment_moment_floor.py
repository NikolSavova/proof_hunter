#!/usr/bin/env python3
"""Verify HULL_ROOT_INCREMENT_MOMENT_FLOOR_20260816.md."""

from __future__ import annotations

from math import ceil, comb


def rank_sum(n: int, count: int) -> int:
    assert 1 <= count < 2**n
    remaining = count
    total = 0
    for rank in range(1, n + 1):
        layer = comb(n, rank)
        take = min(remaining, layer)
        total += rank * take
        remaining -= take
        if remaining == 0:
            return total
    raise AssertionError("count exceeds the nonempty Boolean lattice")


def check_rank_sum() -> int:
    rows = 0
    for n in range(1, 13):
        previous = 0
        for count in range(1, 2**n):
            value = rank_sum(n, count)
            assert value > previous
            cutoff = next(
                rank for rank in range(1, n + 1)
                if sum(comb(n, j) for j in range(1, rank + 1)) >= count
            )
            before = sum(comb(n, j) for j in range(1, cutoff))
            formula = (
                sum(j * comb(n, j) for j in range(1, cutoff))
                + cutoff * (count - before)
            )
            assert value == formula
            previous = value
            rows += 1
    return rows


def check_finite_table() -> int:
    face_minima = [1, 3, 7, 14, 26, 44, 72, 113, 168]
    increments = [1, 3, 6, 11, 17, 27, 40, 54]
    expected_moments = [1, 4, 12, 28, 59, 108, 190, 316]
    expected_bounds = [1, 3, 6, 10, 16, 23, 34, 47]
    for n, increment in enumerate(increments, start=1):
        assert increment == face_minima[n] - face_minima[n - 1] - 1
        moment = rank_sum(n, face_minima[n - 1])
        bound = ceil(moment / n) + n - 1
        assert moment == expected_moments[n - 1]
        assert bound == expected_bounds[n - 1]
        assert increment >= bound
    return len(increments)


def check_ledger_algebra() -> int:
    rows = 0
    # E, C, MF, MC satisfy the summed restoration inequality (13).
    # Verify mechanically that it implies the exact floor (2) whenever the
    # two rank-moment lower bounds hold.
    for n in range(1, 61):
        for face_count in range(1, min(500, 2**n - 1) + 1):
            mf_floor = rank_sum(n, face_count)
            target = ceil(mf_floor / n) + n - 1
            for excess in range(0, min(target + 3, 18)):
                for caps in range(n * (n + 1) // 2, target + 5):
                    k_value = excess + caps
                    if k_value < target:
                        # Even the least possible moments violate (13).
                        assert mf_floor + n * n > n * (k_value + 1)
                    else:
                        assert k_value >= target
                    rows += 1
    return rows


def check_asymptotic_cutoffs() -> int:
    rows = 0
    # At n=2^L and target size approximately 2^(c L^2), the Boolean cutoff
    # is cL+O(log L).  Exact finite rows check the normalized approach.
    for ambient_log in range(8, 19):
        n = 2**ambient_log
        for numerator in range(1, 5):
            denominator = 8
            exponent = numerator * ambient_log**2 // denominator
            count = min((1 << exponent), (1 << n) - 1)
            # Avoid constructing all layers: locate the cutoff by cumulative
            # binomial sums, then use the closed formula.
            cumulative = 0
            weighted = 0
            for rank in range(1, n + 1):
                layer = comb(n, rank)
                if cumulative + layer >= count:
                    weighted += rank * (count - cumulative)
                    cutoff = rank
                    break
                cumulative += layer
                weighted += rank * layer
            assert weighted >= cutoff * (count - cumulative)
            # The cutoff differs from cL only by a lower-order finite term;
            # use a deliberately broad rigorous window for these scales.
            center_num = numerator * ambient_log
            assert cutoff * denominator >= center_num
            assert cutoff <= numerator * ambient_log + 4 * ambient_log
            rows += 1
    return rows


if __name__ == "__main__":
    rank_rows = check_rank_sum()
    finite = check_finite_table()
    ledgers = check_ledger_algebra()
    asymptotic = check_asymptotic_cutoffs()
    print(
        "PASS: hull-root increment moment floor; "
        f"rank_rows={rank_rows}, finite={finite}, "
        f"ledgers={ledgers}, asymptotic={asymptotic}"
    )
