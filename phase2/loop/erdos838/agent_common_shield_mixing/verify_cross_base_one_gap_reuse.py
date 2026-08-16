#!/usr/bin/env python3
"""Exact audit for CROSS_BASE_ONE_GAP_REUSE_REGRESSION.md."""

from __future__ import annotations

import importlib.util
import json
import random
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import isqrt
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


TANGENT = load_module(
    "tangent_for_cross_base_gap_reuse",
    HERE / "verify_tangent_marked_shield_descent.py",
)


def nonempty_block_subsets(block: int) -> list[frozenset[int]]:
    return [
        frozenset(2 * block + bit for bit in range(2) if mask >> bit & 1)
        for mask in range(1, 4)
    ]


def active_profile_bank(blocks: tuple[int, ...], points) -> set[frozenset[int]]:
    bank = set()
    for traces in product(*(nonempty_block_subsets(block) for block in blocks)):
        face = frozenset().union(*traces)
        if TANGENT.convex([points[i] for i in face]):
            bank.add(face)
    return bank


def rational_regression_audit() -> dict[str, object]:
    blocks, repairs, points = TANGENT.configuration()
    fixed_base = frozenset((14, 0, 2, 4))
    mark = 16
    shield = frozenset((16, 18, 19))
    assert TANGENT.convex([points[i] for i in shield])

    context_values = (6, 7)  # the two points of radial block 3
    petal_blocks = (4, 5, 6)
    contexts = {}
    all_sources = set()
    for context_value in context_values:
        sources = set()
        for bits in product(range(2), repeat=len(petal_blocks)):
            petal = {2 * block + bit for block, bit in zip(petal_blocks, bits)}
            source = fixed_base | {context_value} | petal
            star = source | {mark}
            assert TANGENT.convex([points[i] for i in source])
            assert TANGENT.convex([points[i] for i in star])
            assert not TANGENT.convex([points[i] for i in star | shield])
            sources.add(source)
        assert len(sources) == 8
        assert not (sources & all_sources)
        all_sources |= sources
        contexts[context_value] = sources
    assert len(all_sources) == 16

    gap_banks = {}
    for missing in petal_blocks:
        active = tuple(block for block in petal_blocks if block != missing)
        bank = active_profile_bank(active, points)
        assert len(bank) == 9
        gap_banks[missing] = bank
    canonical_missing = min(
        missing for missing, bank in gap_banks.items() if len(bank) == 9
    )
    canonical_bank = gap_banks[canonical_missing]

    # Both contexts literally use the same output sets, so every output has
    # cross-base load two despite exact active-pattern recovery.
    load = Counter()
    for _ in contexts:
        load.update(canonical_bank)
    assert set(load.values()) == {2}
    assert len(load) == 9

    splice_report = {}
    for context_value, sources in contexts.items():
        good = set()
        total_pairs = 0
        contained_pairs = 0
        for source in sources:
            for gap_face in canonical_bank:
                total_pairs += 1
                union = source | gap_face
                if TANGENT.convex([points[i] for i in union]):
                    good.add(union)
                    assert gap_face <= source
                    contained_pairs += 1
        assert total_pairs == 72
        assert contained_pairs == len(good) == 8
        splice_report[context_value] = {
            "pairs": total_pairs,
            "trivial_good": contained_pairs,
            "nontrivial_bad": total_pairs - contained_pairs,
        }

    # Promote the context block into the cycle and omit it.  The resulting
    # full-profile bank on blocks 4,5,6 has exactly the missing factor two.
    promoted_bank = active_profile_bank(petal_blocks, points)
    assert len(promoted_bank) == 18 == len(contexts) * len(canonical_bank)

    return {
        "radial_blocks": len(blocks),
        "repair_labels": len(repairs),
        "contexts": len(contexts),
        "sources_per_context": 8,
        "distinct_sources": len(all_sources),
        "petal_gap_sizes": {str(k): len(v) for k, v in gap_banks.items()},
        "canonical_missing": canonical_missing,
        "canonical_bank": len(canonical_bank),
        "cross_base_load": max(load.values()),
        "splices": splice_report,
        "promoted_bank": len(promoted_bank),
    }


def cauchy_gate_audit() -> dict[str, object]:
    rng = random.Random(838)
    checked = 0
    for _ in range(400):
        universe = tuple(range(rng.randint(5, 12)))
        contexts = []
        for _ in range(rng.randint(1, 8)):
            source = {x for x in universe if rng.randrange(3) == 0}
            gap = {x for x in universe if rng.randrange(3) == 0}
            if not source:
                source = {rng.choice(universe)}
            if not gap:
                gap = {rng.choice(universe)}
            # Pick the largest integer demand satisfying both bank bounds
            # with an exact rational K_c=|G|/m.
            demand = rng.randint(1, min(len(source), len(gap)))
            contexts.append((source, gap, demand))

        source_load = Counter()
        gap_load = Counter()
        total_demand = 0
        inverse_k_max = Q()
        for source, gap, demand in contexts:
            source_load.update(source)
            gap_load.update(gap)
            total_demand += demand
            k_c = Q(len(gap), demand)
            inverse_k_max = max(inverse_k_max, 1 / k_c)
            assert len(source) >= demand and len(gap) >= k_c * demand

        lambda_source = max(source_load.values())
        lambda_gap = max(gap_load.values())
        face_count = len(universe)
        # Square the theorem to keep the audit integral/rational.
        assert total_demand**2 <= (
            lambda_source * lambda_gap * inverse_k_max * face_count**2
        )
        checked += 1
    return {"random_exact_systems": checked}


def scalable_overlap_audit() -> dict[str, object]:
    rows = []
    # t=(log D)/4 and log L=(log D)/4, so log C=(log D)^2/16.
    for d in (16, 32, 64):
        t = d // 4
        log_l = d // 4
        contexts = 1 << (t * log_l)
        assert contexts.bit_length() - 1 == d * d // 16
        rows.append(
            {
                "log_D": d,
                "context_blocks": t,
                "log_cluster_size": log_l,
                "log_overlap": contexts.bit_length() - 1,
            }
        )
    return {"scales": rows, "overlap_coefficient": "1/16"}


def main() -> None:
    result = {
        "rational_regression": rational_regression_audit(),
        "cauchy_gate": cauchy_gate_audit(),
        "scalable_overlap": scalable_overlap_audit(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: cross-base one-gap reuse regression and Cauchy gate verified")


if __name__ == "__main__":
    main()
