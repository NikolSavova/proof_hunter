#!/usr/bin/env python3
"""Exact verifier for MINIMIZER_ALL_LOOP_ENDPOINT_POTENTIAL_GATE.md."""

from __future__ import annotations

from itertools import product
from math import log2
from pathlib import Path
import importlib.util
import sys


ROOT = Path(__file__).resolve().parent.parent
GEOMETRY = ROOT / "agent_geometry" / "audit_geometry.py"


def load_geometry():
    spec = importlib.util.spec_from_file_location("endpoint_potential_geometry",
                                                  GEOMETRY)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def reflection_minimum_audit() -> int:
    checks = 0
    for cy, uy, cz, uz in product(range(1, 7), repeat=4):
        products = (cy * uz, uy * uz, cy * cz, uy * cz)
        is_minimal = products[0] == min(products)
        criterion = cy <= uy and uz <= cz
        assert is_minimal == criterion
        checks += 1
    return checks


def pascal_endpoint_audit(g, nmax: int = 96) -> tuple[int, float]:
    caps, cups = g.dp_counts(nmax)
    faces = g.dp_convex_counts(nmax, caps, cups)
    checks = 0
    max_normalized_imbalance = 0.0

    for n in range(2, nmax + 1):
        for i in range(n + 1):
            # Universal endpoint injection V <= C U.
            assert faces[n][i] <= caps[n][i] * cups[n][i]
            checks += 1

    for n in range(6, nmax + 1, 2):
        h = n // 2
        cy = caps[n - 1][h - 1]
        uy = cups[n - 1][h - 1]
        cz = caps[n - 1][h]
        uz = cups[n - 1][h]
        parent = faces[n][h]
        child = faces[n - 1][h - 1]
        assert child == faces[n - 1][h]
        assert parent == 2 * child + cy * uz
        assert cy == uz and uy == cz
        imbalance = abs(log2(uy) - log2(cy)) / (n * n)
        max_normalized_imbalance = max(max_normalized_imbalance, imbalance)

    return checks, max_normalized_imbalance


def cycle_telescope_audit() -> int:
    checks = 0
    # Work with integer base logarithms.  An edge i -> j has exponent
    # cap_i + cup_j + span_i.  Around a cycle, every cap and cup occurs once.
    for k in range(2, 6):
        for caps in product(range(1, 4), repeat=k):
            for cups in product(range(1, 4), repeat=k):
                for spans in product(range(3), repeat=k):
                    lhs = 0
                    for i in range(k):
                        j = (i + 1) % k
                        lhs += caps[i] + cups[j] + spans[i]
                    rhs = sum(caps) + sum(cups) + sum(spans)
                    assert lhs == rhs
                    checks += 1
    return checks


def quarter_ramp_audit() -> int:
    checks = 0
    for q in range(2, 80):
        for i in range(q):
            for j in range(i + 1, q):
                cap_i = i + 2
                cup_j = q + 1 - j
                span = j - i - 1
                assert cap_i + cup_j + span == q + 2
                checks += 1
    return checks


def main() -> None:
    g = load_geometry()
    reflection = reflection_minimum_audit()
    endpoint, imbalance = pascal_endpoint_audit(g)
    cycles = cycle_telescope_audit()
    ramps = quarter_ramp_audit()
    print("PASS: minimizer all-loop endpoint-potential gate")
    print({
        "reflection_profiles": reflection,
        "pascal_endpoint_cells": endpoint,
        "cycle_exponent_words": cycles,
        "quarter_ramp_intervals": ramps,
        "max_pascal_imbalance_over_n2": imbalance,
    })


if __name__ == "__main__":
    main()
