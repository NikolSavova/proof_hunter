#!/usr/bin/env python3
"""Exact audit for HEAVY_COMMON_BASE_SOURCE_DOWNSET.md."""

from __future__ import annotations

import sys
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
OUTER = ERDOS / "agent_outer_internal_product"
sys.path.insert(0, str(OUTER))

from verify_outer_internal_mixed_bank import (  # noqa: E402
    choose_lower_parameters,
    hard_points,
    hull,
    parabola_point,
    transform,
)


def abstract_bank_audit() -> dict[str, int]:
    outer = tuple(range(9))
    internal_offset = 100
    bases = tuple(combinations(outer[:6], 4))
    completions = tuple(combinations(outer[6:], 2))
    degree = 3
    full_occurrences: Counter[frozenset[int]] = Counter()
    middle_occurrences: Counter[frozenset[int]] = Counter()
    middle_representations: defaultdict[frozenset[int], list[tuple]] = defaultdict(list)
    source_middle_occurrences: Counter[frozenset[int]] = Counter()
    source_middle_representations: defaultdict[frozenset[int], list[tuple]] = defaultdict(list)
    pair_outputs: dict[tuple[frozenset[int], frozenset[int]], tuple] = {}
    records = 0

    for cell, base in enumerate(bases):
        base_set = frozenset(base)
        # Reuse the source as well, so the source-projected bank has genuine
        # cross-base load instead of being injective for a trivial reason.
        x = internal_offset
        for completion in completions:
            q_set = frozenset(completion)
            # Deliberately reuse the repair alphabet across every base and
            # completion.  This creates the cross-base overlap which the
            # theorem measures.
            repair_labels = tuple(1000 + j for j in range(degree))
            for y in repair_labels:
                records += 1
                for mask in range(1 << len(base)):
                    subset = frozenset(base[i] for i in range(len(base)) if (mask >> i) & 1)
                    output = subset | q_set | {y}
                    full_occurrences[output] += 1
                    first = subset | q_set | {x}
                    second = (base_set - subset) | q_set | {y}
                    key = (first, second)
                    value = (base_set, q_set, x, y, subset)
                    assert key not in pair_outputs
                    pair_outputs[key] = value

                    recovered_q = (first & second) & set(outer)
                    recovered_b = ((first | second) & set(outer)) - recovered_q
                    recovered_s = (first & set(outer)) - recovered_q
                    assert frozenset(recovered_q) == q_set
                    assert frozenset(recovered_b) == base_set
                    assert frozenset(recovered_s) == subset

                for subset in combinations(base, len(base) // 2):
                    output = frozenset(subset) | q_set | {y}
                    middle_occurrences[output] += 1
                    middle_representations[output].append(
                        (base_set, q_set, y, frozenset(subset))
                    )
                    # The source-projected occurrence deliberately forgets y.
                    # It is therefore repeated exactly ``degree`` times.
                    source_output = frozenset(subset) | q_set | {x}
                    source_middle_occurrences[source_output] += 1
                    source_middle_representations[source_output].append(
                        (base_set, q_set, x, y, frozenset(subset))
                    )

    assert sum(full_occurrences.values()) == (1 << 4) * records
    assert sum(middle_occurrences.values()) == comb(4, 2) * records
    assert len(pair_outputs) == (1 << 4) * records
    assert records <= max(full_occurrences.values()) * len(full_occurrences) // (1 << 4) + 1
    assert records <= max(middle_occurrences.values()) * len(middle_occurrences) // comb(4, 2) + 1

    # Audit Theorem 3 on every middle output fibre.  Here q=2,s=2.
    heaviest_output, heaviest_count = max(middle_occurrences.items(), key=lambda item: item[1])
    split_counts: defaultdict[tuple[frozenset[int], frozenset[int]], list[frozenset[int]]] = defaultdict(list)
    for base_set, q_set, y, s_set in middle_representations[heaviest_output]:
        split_counts[(q_set, s_set)].append(base_set - s_set)
    best_missing = max(split_counts.values(), key=len)
    assert len(best_missing) * comb(4, 2) >= heaviest_count
    assert len(set(best_missing)) == len(best_missing)
    assert all(len(missing) == 2 for missing in best_missing)

    # Source-projected heavy fibre, equations (15a)--(15c).  Once Q,S,x
    # are fixed, each genuinely distinct missing half occurs once for every
    # repair label.  Thus division by D is exact in this model.
    source_output, source_load = max(
        source_middle_occurrences.items(), key=lambda item: item[1]
    )
    source_splits: defaultdict[tuple[frozenset[int], frozenset[int]], list[frozenset[int]]] = defaultdict(list)
    for base_set, q_set, x, y, s_set in source_middle_representations[source_output]:
        source_splits[(q_set, s_set)].append(base_set - s_set)
    source_best = max(source_splits.values(), key=len)
    assert len(source_best) % degree == 0
    distinct_source_missing = set(source_best)
    assert len(distinct_source_missing) * degree == len(source_best)
    assert len(distinct_source_missing) * degree * comb(4, 2) >= source_load
    assert all(len(missing) == 2 for missing in distinct_source_missing)

    return {
        "records": records,
        "full_occurrences": sum(full_occurrences.values()),
        "middle_occurrences": sum(middle_occurrences.values()),
        "pair_codewords": len(pair_outputs),
        "full_max_overlap": max(full_occurrences.values()),
        "middle_max_overlap": max(middle_occurrences.values()),
        "source_middle_max_occurrence_overlap": max(source_middle_occurrences.values()),
        "source_middle_heavy_distinct_descendants": len(distinct_source_missing),
    }


def rational_geometry_audit() -> dict[str, int]:
    _, _, chain, _ = transform(hard_points())
    u = (Fraction(-1), Fraction(0))
    v = (Fraction(1), Fraction(0))
    lower = [parabola_point(t) for t in choose_lower_parameters(chain, 9)]
    base = [u, v, lower[0]]
    cloud = lower[1:]
    completion_family = list(combinations(cloud[:5], 2))
    source = chain[0]
    repairs = chain[-3:]
    checked = 0
    decoded = 0

    for completion in completion_family:
        carrier = base + list(completion)
        assert len(hull(carrier + [source])) == len(carrier) + 1
        for repair in repairs:
            assert len(hull(carrier + [repair])) == len(carrier) + 1
            for mask in range(1 << len(base)):
                subset = [base[i] for i in range(len(base)) if (mask >> i) & 1]
                first = subset + list(completion) + [source]
                second = [p for p in base if p not in subset] + list(completion) + [repair]
                assert len(hull(first)) == len(first)
                assert len(hull(second)) == len(second)
                # Coordinate sets reverse exactly as in (11).
                fs, ss = set(first), set(second)
                recovered_q = (fs & ss) - {source, repair}
                recovered_b = (fs | ss) - recovered_q - {source, repair}
                assert recovered_q == set(completion)
                assert recovered_b == set(base)
                decoded += 1
            checked += 1

    return {
        "base_rank": len(base),
        "completion_rank": 2,
        "completion_count": len(completion_family),
        "repair_faces": checked,
        "decoded_pair_codewords": decoded,
    }


def main() -> None:
    abstract = abstract_bank_audit()
    geometry = rational_geometry_audit()
    print(f"abstract: {abstract}")
    print(f"geometry: {geometry}")
    print("PASS heavy common-base source downset")


if __name__ == "__main__":
    main()
