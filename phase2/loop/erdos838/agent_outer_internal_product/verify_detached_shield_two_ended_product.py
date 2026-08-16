#!/usr/bin/env python3
"""Exact audit for DETACHED_SHIELD_TWO_ENDED_PRODUCT.md."""

import importlib.util
import sys
from fractions import Fraction
from itertools import combinations, product
from math import ceil, comb
from pathlib import Path
from random import Random


HERE = Path(__file__).resolve().parent
REGRESSION = HERE / "verify_pairwise_incompatible_completion_regression.py"
SPEC = importlib.util.spec_from_file_location("nested_regression", REGRESSION)
NESTED = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(NESTED)

GEOMETRY_PATH = HERE.parent / "agent_geometry" / "audit_geometry.py"
GEOMETRY_SPEC = importlib.util.spec_from_file_location("strong_geometry",
                                                       GEOMETRY_PATH)
GEOMETRY = importlib.util.module_from_spec(GEOMETRY_SPEC)
sys.modules[GEOMETRY_SPEC.name] = GEOMETRY
GEOMETRY_SPEC.loader.exec_module(GEOMETRY)


def audit_rational_two_ended_banks():
    models = 0
    faces = 0
    for q in range(2, 6):
        for L in range(2, 6):
            _base, active, _labels, _completions = NESTED.build(q, L, 3)
            expected = comb(L, 2) ** 2 * L ** (q - 2)
            for i in range(q):
                j = (i + 1) % q
                rest = [k for k in range(q) if k not in (i, j)]
                outputs = set()
                for left in combinations(active[i], 2):
                    for right in combinations(active[j], 2):
                        for middle in product(*[active[k] for k in rest]):
                            face = frozenset(left + right + middle)
                            assert NESTED.is_convex_set(list(face))
                            outputs.add(face)
                assert len(outputs) == expected
                faces += len(outputs)
            models += 1
    return models, faces


def audit_elementary_inequality():
    rng = Random(83808142026)
    trials = 1000
    for _ in range(trials):
        q = rng.randint(2, 12)
        sizes = [rng.randint(2, 30) for _ in range(q)]
        P0 = 1
        for size in sizes:
            P0 *= size
        banks = []
        for i in range(q):
            j = (i + 1) % q
            bank = comb(sizes[i], 2) * comb(sizes[j], 2)
            for k, size in enumerate(sizes):
                if k not in (i, j):
                    bank *= size
            banks.append(bank)
        # Clear the q-th root in max B >= P0^(1+2/q)/16.
        assert (16 * max(banks)) ** q >= P0 ** (q + 2)
    return trials


def audit_profile_alignment():
    rng = Random(83820260814)
    trials = 1000
    for _ in range(trials):
        q = rng.randint(2, 15)
        sizes = [rng.randint(2, 50) for _ in range(q)]
        left = [rng.randint(1, 200) for _ in range(q)]
        right = [rng.randint(1, 200) for _ in range(q)]
        # Clear denominators and q-th roots in (15):
        # max_i (R_i A_{i+1}/(L_i L_{i+1}))^q
        # >= product_i(A_i R_i/L_i^2).
        ratios = [Fraction(right[i] * left[(i + 1) % q],
                           sizes[i] * sizes[(i + 1) % q])
                  for i in range(q)]
        rhs = Fraction(1)
        for i in range(q):
            rhs *= Fraction(left[i] * right[i], sizes[i] ** 2)
        assert max(ratios) ** q >= rhs
    return trials


def audit_uniform_record_payment():
    cases = 0
    for D in range(4, 80):
        for q in range(2, 10):
            M = D ** q
            bank = comb(D, 2) ** 2 * D ** (q - 2)
            assert D * D * M <= Fraction(4 * D * D, (D - 1) ** 2) * bank
            cases += 1
    return cases


def audit_full_strong_glue_recurrence():
    templates = [(3, 1), (3, 2), (2, 1)]
    audits = 0
    for length in range(2, 5):
        for choices in product(range(len(templates)), repeat=length):
            blocks = []
            profiles = []
            for block_id, choice in enumerate(choices):
                n, i = templates[choice]
                raw = GEOMETRY.cell(n, i)
                block = tuple(GEOMETRY.Point(p.x, p.y, p.word, block_id)
                              for p in raw)
                blocks.append(block)
                profiles.append(GEOMETRY.cap_cup_counts(block))
            joined = blocks[0]
            for block in blocks[1:]:
                joined = GEOMETRY.glue(joined, block)
            _caps, _cups, actual = GEOMETRY.cap_cup_counts(joined)

            expected = sum(profile[2] for profile in profiles)
            for i in range(length):
                for j in range(i + 1, length):
                    term = profiles[i][0] * profiles[j][1]
                    for k in range(i + 1, j):
                        term *= 1 + len(blocks[k])
                    expected += term
            assert actual == expected
            assert all(caps * cups >= convex
                       for caps, cups, convex in profiles)
            audits += 1
    return audits


def audit_global_hybrid_cauchy():
    rng = Random(83820260815)
    trials = 800
    for _ in range(trials):
        cells = rng.randint(1, 30)
        D = rng.randint(2, 15)
        q = rng.randint(2, 8)
        M0 = rng.randint(2, 10)
        Ms = [rng.randint(M0, M0 + 25) for _ in range(cells)]

        # Realize abstract source and detached banks with their guaranteed
        # minimum sizes, in disjoint face namespaces.
        src_banks = []
        det_banks = []
        src_universe = D * max(Ms) + 40
        det_sizes = [ceil(M ** (1 + 2 / q) / 16) for M in Ms]
        det_universe = max(det_sizes) + 40
        for M, det_size in zip(Ms, det_sizes):
            src_banks.append(set(rng.sample(range(src_universe), D * M)))
            det_banks.append(set(rng.sample(range(det_universe), det_size)))
        src_load = {}
        det_load = {}
        for bank in src_banks:
            for face in bank:
                src_load[face] = src_load.get(face, 0) + 1
        for bank in det_banks:
            for face in bank:
                det_load[face] = det_load.get(face, 0) + 1
        LS = max(src_load.values())
        LD = max(det_load.values())
        V = len(src_load) + len(det_load)

        # Square (26), then raise to q to avoid fractional exponents:
        # E <= 4 D^(3/2) M0^(-1/q) sqrt(LS LD) V.
        E = sum(D * D * M for M in Ms)
        assert E ** (2 * q) * M0 ** 2 <= (
            16 * D ** 3 * LS * LD * V * V) ** q
    return trials


def main():
    models, faces = audit_rational_two_ended_banks()
    elementary = audit_elementary_inequality()
    profiles = audit_profile_alignment()
    payments = audit_uniform_record_payment()
    recurrences = audit_full_strong_glue_recurrence()
    hybrid = audit_global_hybrid_cauchy()
    print("PASS: detached-shield two-ended product")
    print(f"  rational cyclic models: {models}; bank faces: {faces}")
    print(f"  elementary entropy inequalities: {elementary}")
    print(f"  cyclic profile/Kraft identities: {profiles}")
    print(f"  uniform record payments: {payments}")
    print(f"  exact strong-glue recurrences: {recurrences}")
    print(f"  global source/detached Cauchy trials: {hybrid}")


if __name__ == "__main__":
    main()
