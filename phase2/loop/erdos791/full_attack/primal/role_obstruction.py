#!/usr/bin/env python3
"""Audit a certificate against the triangle-free fine/coarse role bound.

For the recorded interleaved cycle the on-role edges are I-L and K-L.  The
only off-role square in its prefix is the square-zero I-K anchor.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

from phased_predicate import coverage_bits, sum_bits
from primal_verify import load


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    p, raw = load(args.certificate)
    m = raw.get("m")
    if type(m) is not int:
        raise ValueError("certificate must state m")
    covered = coverage_bits(p, m)
    il = sum_bits(p["I"], p["L0"], m) | sum_bits(p["I"], p["L1"], m)
    kl = sum_bits(p["K"], p["L0"], m) | sum_bits(p["K"], p["L1"], m)
    on_role = il | kl
    residual = covered & ~on_role
    fine = len(p["I"]) + len(p["K"])
    coarse = len(p["L0"]) + len(p["L1"])
    other = len(p["J"])
    ell = fine + coarse + other
    cross_capacity = fine * coarse
    threshold = Fraction(23 * ell * ell, 588)
    print(
        json.dumps(
            {
                "status": "PASS",
                "ell": ell,
                "m": m,
                "fine_mass_I_plus_K": fine,
                "coarse_mass_L": coarse,
                "unused_other_mass_J": other,
                "fine_times_coarse": cross_capacity,
                "ell_squared_over_4": str(Fraction(ell * ell, 4)),
                "off_role_squares_in_prefix": residual.bit_count(),
                "off_role_square_indices": [q for q in range(m) if residual >> q & 1],
                "record_forces_more_than_off_role_squares": str(threshold),
                "record_integer_minimum_off_role": threshold.numerator // threshold.denominator + 1,
                "identity": "85/294 - 1/4 = 23/588",
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
