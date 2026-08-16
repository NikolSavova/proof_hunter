#!/usr/bin/env python3
"""Checks for DETACHED_BOOLEAN_SHIELD_CONTEXT_REUSE_GATE.md."""

from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from math import comb
from pathlib import Path


def weighted_two_bank_check():
    # Each tuple is (weight, old-source count, shield count, demand).
    contexts = [
        (F(1, 2), 3, 12, 6),
        (F(2, 3), 5, 20, 10),
        (F(3, 5), 7, 28, 14),
        (F(4, 7), 11, 44, 22),
    ]
    Gamma = F(1)
    assert all(e * e <= Gamma * a * s for _, a, s, e in contexts)
    lhs = sum(w * e for w, _, _, e in contexts)
    sa = sum(w * a for w, a, _, _ in contexts)
    ss = sum(w * s for w, _, s, _ in contexts)
    assert lhs * lhs <= Gamma * sa * ss
    return lhs, sa, ss


def rank_budget_check():
    # Formal leading exponents: m=n^(tau loglog n), k=c loglog n.
    # Local one-shield Cauchy needs c>=3 tau; the terminal bound needs
    # c<2 sigma.  There is no solution once tau>=sigma.
    for sigma_num in range(1, 9):
        sigma = F(sigma_num, 4)
        for tau_num in range(sigma_num, 13):
            tau = F(tau_num, 4)
            feasible = [
                F(c_num, 8)
                for c_num in range(0, 200)
                if F(c_num, 8) >= 3 * tau
                and F(c_num, 8) < 2 * sigma
            ]
            assert not feasible

            # The same obstruction for one source and b low-rank tags.
            for b in range(1, 8):
                local = (F(2) + F(1, b)) * tau
                global_upper = (F(1) + F(1, b)) * sigma
                assert local > global_upper

    # A finite Boolean-support sanity check: full shield eventually has the
    # local cardinality while modest low-rank pieces do not.
    p, r, k = 50, 3, 5
    m = comb(p, r)
    low = sum(comb(p, j) for j in range(k + 1))
    full = 2**p
    assert low < m**3 < full
    return p, m, low, full


def decoder_threshold_check():
    for q in range(2, 13):
        for D in (2, 3, 5, 11):
            M = D**q
            for h in range(q + 1):
                states = sum(comb(q, s) * D**s for s in range(h + 1))
                coarse_den = (q + 1) * 2**q * D**h
                assert states <= coarse_den
                exact_pigeonhole = F(M, states)
                coarse = F(D ** (q - h), (q + 1) * 2**q)
                assert exact_pigeonhole >= coarse


def exact_geometry_check():
    sibling = (
        Path(__file__).resolve().parents[1]
        / "agent_outer_internal_product"
        / "verify_quadratic_base_word_reuse.py"
    )
    spec = spec_from_file_location("quadratic_reuse", sibling)
    module = module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    module.check_geometry()
    module.check_decoder_bound()


if __name__ == "__main__":
    weighted = weighted_two_bank_check()
    rank = rank_budget_check()
    decoder_threshold_check()
    exact_geometry_check()
    print(
        "PASS: weighted two-bank Cauchy, rank-budget incompatibility, "
        "quadratic-context geometry, and decoder thresholds; "
        f"weighted={weighted} finite_rank={(rank[0], rank[1], rank[2])}"
    )
