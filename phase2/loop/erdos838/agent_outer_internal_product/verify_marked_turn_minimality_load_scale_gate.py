#!/usr/bin/env python3
"""Exact/numerical checks for MARKED_TURN_MINIMALITY_LOAD_SCALE_GATE."""

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import comb, e, expm1, log, log1p, log2, sqrt
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PASCAL_VERIFIER = (
    ROOT / "agent_common_shield_mixing"
    / "verify_canonical_source_role_deletion_pascal_density_barrier.py"
)


def load_pascal_verifier():
    spec = spec_from_file_location("marked_turn_pascal_verifier", PASCAL_VERIFIER)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def minimality_scale_audit():
    rows = []
    c = Fraction(2, 5)
    A = 14
    for L in (24, 32, 48, 64, 96, 128, 256, 512):
        n = 1 << L
        decrement = -log1p(-2.0 ** (-L)) / log(2)
        log_previous = L - decrement
        window = float(c) * (2 * L * decrement - decrement * decrement)
        assert 0 < window < 4 * float(c) * L / n

        load_log = float(c) * log_previous * log_previous - A * L
        assert load_log < float(c) * L * L
        rows.append((L, window, load_log / (L * L)))
    assert rows[-1][2] > float(c) - 0.03
    return rows


def source_capacity_audit():
    rows = []
    c = 0.4
    epsilon = 0.05
    A = 14
    for L in (48, 64, 96, 128, 256, 512):
        n = 1 << L
        r = int((c + epsilon) * L)
        load_log = c * log2(n - 1) ** 2 - A * L
        source_log = log2(comb(n, r))
        assert source_log > load_log
        relative_mass = 2 ** (-A * L)
        mean_contribution = r * relative_mass
        assert mean_contribution < 1
        rows.append((L, r, source_log / L**2, load_log / L**2))
    return rows


def support_rank_audit():
    checked = 0
    for s in range(4, 120):
        for r in range(1, s // 2 + 1):
            downset = sum(comb(s, i) for i in range(r + 1))
            upper = (e * s / r) ** r
            assert downset <= upper * (1 + 1e-12)
            checked += 1
    return checked


def fixed_gap_audit():
    rows = []
    for delta in (0.05, 0.1, 0.2):
        alpha = sqrt(1 - 2 * delta) + delta / 3
        allowance = 0.5 * alpha**2 - (0.5 - delta)
        g = allowance / 4
        kappa_sigma = allowance / 2
        assert g + kappa_sigma < allowance
        rows.append((delta, alpha, allowance, g + kappa_sigma))
    return rows


def mean_rank_constant_audit():
    rows = []
    for delta in (0.01, 0.05, 0.1, 0.2, 0.25):
        c = 0.5 - delta
        assert 4 * c >= 1 > delta
        for L in (24, 32, 48):
            n = 1 << L
            decrement = -log1p(-2.0 ** (-L)) / log(2)
            exponent_gap = c * (2 * L * decrement - decrement**2)
            one_minus_ratio = -expm1(-log(2) * exponent_gap)
            mean_bound = n * one_minus_ratio
            assert mean_bound / L < 2 * c + 1e-5
        rows.append((delta, 2 * c, 4 * c))
    return rows


def pascal_geometry_audit():
    verifier = load_pascal_verifier()
    geometry_module = verifier.load_geometry()
    result = verifier.exact_geometry_audit(geometry_module)
    assert result["terminal_load"] == result["retained_weight"]
    assert result["retained_weight"] >= Fraction(1, 2)
    assert result["rank"] <= result["max_rank"]
    dp_checks = verifier.exact_dp_audit(geometry_module, nmax=36)
    return result, dp_checks


def main():
    scales = minimality_scale_audit()
    sources = source_capacity_audit()
    downsets = support_rank_audit()
    gaps = fixed_gap_audit()
    means = mean_rank_constant_audit()
    pascal, dp_checks = pascal_geometry_audit()
    print("PASS: marked-turn minimality load scale gate")
    print("  scale rows:", [(L, f"{w:.3e}", round(c, 6))
                            for L, w, c in scales])
    print("  source rows:", [(L, r, round(a, 6), round(b, 6))
                             for L, r, a, b in sources])
    print("  downset checks:", downsets)
    print("  gap rows:", [(d, round(a, 6), round(x, 8), round(y, 8))
                          for d, a, x, y in gaps])
    print("  mean/rank constants:", means)
    print("  Pascal terminal:", pascal["terminal_load"], "DP:", dp_checks)


if __name__ == "__main__":
    main()
