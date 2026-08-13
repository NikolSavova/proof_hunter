#!/usr/bin/env python3
"""Macro predicate including the exact H-S-T0 carry triangle."""

from __future__ import annotations

from typed_predicate import coverage_bits as phased_coverage_bits
from typed_predicate import prefix_length, sum_bits


def coverage_bits(p: dict[str, set[int]], limit: int) -> int:
    ordinary = phased_coverage_bits(p, limit)
    hs = sum_bits(p["J"], p["K"], limit)
    ht = sum_bits(p["J"], p["L0"], limit)
    st = sum_bits(p["K"], p["L0"], limit)
    # Two exact carry orientations:
    #   HS,HT at q and ST at q-1; or
    #   HS,HT at q-1 and ST at q.
    triangle = (hs & ht & (st << 1)) | ((hs << 1) & (ht << 1) & st)
    return ordinary | triangle
