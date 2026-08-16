#!/usr/bin/env python3
"""Exact checks for MASK_CASCADE_ENTROPY_DICHOTOMY.md."""

from fractions import Fraction
from itertools import product
from math import prod


def exhaustive_masks() -> int:
    checked = 0
    # Abstract cells: each pair is assigned a deletion mask.  The theorem
    # uses only mask counts and the exact maximum forgotten alphabet.
    for q in range(2, 5):
        g = 0
        masks = list(range(1 << (q - 1)))
        for sizes in product(range(1, 4), repeat=q):
            mg = sizes[g]
            costs = []
            for mask in masks:
                costs.append(prod(sizes[i + 1] for i in range(q - 1)
                                  if mask & (1 << i)))
            # Exhaust all small multiplicity vectors with entries 0,1,2.
            for counts in product(range(3), repeat=len(masks)):
                total = sum(counts)
                if not total:
                    continue
                for T in sorted(set(costs)):
                    low = sum(c for c, k in zip(counts, costs) if k <= T)
                    if 2 * low < total:
                        continue
                    best_outputs = max(
                        (Fraction(c, mg * k) for c, k in zip(counts, costs)
                         if k <= T), default=Fraction(0))
                    claimed = Fraction(total, 2 * len(masks) * mg * T)
                    assert best_outputs >= claimed
                    checked += 1
    return checked


def coefficient_rows():
    rows = []
    a = Fraction(1, 4)
    c = Fraction(1, 8)
    eps = Fraction(1, 64)
    for d in (64, 128, 256, 512):
        q = d // 4
        source = a * d * d
        reservoir = c * d * d
        threshold = (c - eps) * d * d
        mask_and_g_loss = q + d
        bank = source + reservoir - threshold - mask_and_g_loss - 1
        # Leading term is (a+eps)d^2; the displayed finite row includes
        # the exact linear mask and deleted-coordinate-description loss.
        assert bank == (a + eps) * d * d - mask_and_g_loss - 1
        rows.append({
            "log_D": d,
            "source_bits": int(source),
            "reservoir_bits": int(reservoir),
            "erased_threshold_bits": int(threshold),
            "bank_lower_bits": int(bank),
        })
    return rows


def main():
    checked = exhaustive_masks()
    rows = coefficient_rows()
    print({"exhaustive_weighted_systems": checked,
           "coefficient_rows": rows,
           "live_erased_fraction": "1/2"})
    print("PASS: mask-cascade entropy dichotomy verified")


if __name__ == "__main__":
    main()
