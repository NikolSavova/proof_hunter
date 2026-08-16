#!/usr/bin/env python3
"""Exact audit of the aggregate raw-rank and completion-density bridge."""

from __future__ import annotations

import importlib.util
import json
from collections import Counter, defaultdict
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


T = load_module("two_reference_data_for_raw_bridge", HERE / "verify_two_reference_hall_demand.py")


def audit() -> dict[str, object]:
    faces = T.enumerate_faces(T.POINTS)
    total = sum((Q(1, 1 << len(face)) for face in faces), Q())
    nontrivial = [face for face in faces if len(face) >= 2]

    # Compatible endpoint completion banks, resolved by rank.
    completion_ranks: defaultdict[tuple[int, int], Counter[int]] = defaultdict(Counter)
    completion_faces: defaultdict[tuple[int, int], set[tuple[int, ...]]] = defaultdict(set)
    for face in nontrivial:
        edge = (face[0], face[-1])
        completion_ranks[edge][len(face)] += 1
        completion_faces[edge].add(face)

    assert sum(len(bank) for bank in completion_faces.values()) == len(nontrivial)
    assert len(set().union(*completion_faces.values())) == len(nontrivial)

    # Raw histories at every radial depth, resolved by parent rank.
    histories: defaultdict[tuple[int, tuple[int, int]], Counter[int]] = defaultdict(Counter)
    history_records = []
    max_depth = max(map(len, faces)) // 2
    for source in faces:
        for depth in range(max_depth):
            if len(source) < 2 * depth + 2:
                continue
            parent = source[depth : len(source) - depth]
            edge = (parent[0], parent[-1])
            rank = len(parent)
            histories[depth, edge][rank] += 1
            history_records.append((source, depth, parent, edge))

    cells = []
    radial_weight_total = Q()
    for (depth, edge), rank_counts in sorted(histories.items()):
        completion_counts = completion_ranks[edge]
        raw_histories = sum(rank_counts.values())
        raw_completions = sum(completion_counts.values())

        q_by_rank = {
            rank: Q(count, 1 << rank) / (total * (4**depth))
            for rank, count in rank_counts.items()
        }
        p_by_rank = {
            rank: Q(count, 1 << rank) / total
            for rank, count in completion_counts.items()
        }
        q_mass = sum(q_by_rank.values(), Q())
        p_mass = sum(p_by_rank.values(), Q())
        tilt = q_mass / p_mass

        expected_source_power = sum(
            (mass / q_mass) * (2 ** (rank + 2 * depth))
            for rank, mass in q_by_rank.items()
        )
        expected_completion_power = sum(
            (mass / p_mass) * (2**rank)
            for rank, mass in p_by_rank.items()
        )
        assert Q(raw_histories, raw_completions) == (
            tilt * expected_source_power / expected_completion_power
        )

        compatible_half_weight = sum(
            (Q(count, 1 << rank) for rank, count in completion_counts.items()), Q()
        )
        assert compatible_half_weight >= Q(1, 4)
        cell_weight = Q()
        for rank, count in rank_counts.items():
            source_rank = rank + 2 * depth
            history_weight = Q(1, (1 << rank) * (4**depth)) / compatible_half_weight
            assert history_weight == Q(1, 1 << source_rank) / compatible_half_weight
            assert history_weight <= Q(4, 1 << source_rank)
            cell_weight += count * history_weight
        assert cell_weight == tilt
        radial_weight_total += cell_weight

        cells.append(
            {
                "depth": depth,
                "edge": list(edge),
                "raw_histories": raw_histories,
                "raw_completions": raw_completions,
                "raw_density": Q(raw_histories, raw_completions),
                "tilt": tilt,
            }
        )

    # The same endpoint completion bank is used at most once per depth.
    aggregate_bank_spend = sum(row["raw_completions"] for row in cells)
    active_depths = len({row["depth"] for row in cells})
    assert aggregate_bank_spend <= active_depths * len(nontrivial)

    # Audit Theorem 2 at all discontinuity thresholds and at two off-grid values.
    thresholds = {row["raw_density"] for row in cells}
    thresholds.update({Q(1, 2), Q(2), Q(7, 3)})
    density_audits = []
    for threshold in sorted(thresholds):
        low = [row for row in cells if row["raw_density"] <= threshold]
        low_mass = sum(row["raw_histories"] for row in low)
        low_bank_spend = sum(row["raw_completions"] for row in low)
        assert low_mass <= threshold * low_bank_spend
        assert low_mass <= threshold * active_depths * len(nontrivial)
        density_audits.append(
            {
                "threshold": str(threshold),
                "low_raw_mass": low_mass,
                "low_bank_spend": low_bank_spend,
            }
        )

    # A finite exact audit of the high-rank counting implication (11).
    synthetic_rank_cutoff = 7
    synthetic_weights = [Q(4, 1 << rank) for rank in (7, 8, 10, 12)]
    synthetic_raw_mass = len(synthetic_weights)
    synthetic_weight = sum(synthetic_weights, Q())
    assert Q(synthetic_raw_mass) >= (2 ** (synthetic_rank_cutoff - 2)) * synthetic_weight

    # Exact finite coefficient-gap interface regression from Section 5.
    scale_log = 12
    reservoir_numerator = 1
    reservoir_denominator = 4
    face_numerator = 1
    face_denominator = 2
    guaranteed_weight = 1 << (
        reservoir_numerator * scale_log * scale_log // reservoir_denominator
    )
    ambient_faces = 1 << (
        face_numerator * scale_log * scale_log // face_denominator
    )
    regression_rank = reservoir_numerator * scale_log // reservoir_denominator
    regression_raw_histories = guaranteed_weight * (1 << regression_rank)
    regression_history_weight = Q(1, 1 << regression_rank)
    assert regression_raw_histories * regression_history_weight == guaranteed_weight
    assert regression_history_weight <= Q(4, 1 << regression_rank)
    regression_raw_density = Q(regression_raw_histories, ambient_faces)
    assert regression_raw_density == Q(1, 1 << 33)

    certificate: dict[str, object] = {
        "description": "aggregate raw-rank identity and raw completion-density dichotomy",
        "n": len(T.POINTS),
        "faces": len(faces),
        "nontrivial_faces": len(nontrivial),
        "half_partition_function": str(total),
        "radial_cells": len(cells),
        "active_depths": active_depths,
        "raw_history_occurrences": len(history_records),
        "aggregate_radial_tilt": str(radial_weight_total),
        "aggregate_completion_bank_spend": aggregate_bank_spend,
        "completion_load_upper_bound": active_depths * len(nontrivial),
        "density_thresholds_audited": len(density_audits),
        "maximum_raw_density": str(max(row["raw_density"] for row in cells)),
        "coefficient_gap_regression": {
            "L": scale_log,
            "reservoir_coefficient": "1/4",
            "face_coefficient": "1/2",
            "weighted_fibre": guaranteed_weight,
            "history_rank": regression_rank,
            "raw_histories": regression_raw_histories,
            "ambient_completion_bank": ambient_faces,
            "raw_density": str(regression_raw_density),
        },
        "claims": [
            "endpoint completion banks partition all nontrivial faces",
            "the aggregate raw-rank identity holds in every radial cell",
            "every radial history weight equals 2^-source-rank divided by endpoint half-weight",
            "every radial history weight is at most four times 2^-source-rank",
            "endpoint completion-bank aggregate load is at most the number of active depths",
            "the raw low-density payment holds at every audited threshold",
            "the high-rank weighted-to-raw count inequality holds exactly",
            "a coefficient one-quarter fibre versus coefficient one-half bank has exponentially vanishing raw density",
        ],
    }
    output = HERE / "raw_completion_density_bridge_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    return certificate


def main() -> None:
    certificate = audit()
    print("raw completion density bridge audit: PASS")
    print(
        "n=", certificate["n"],
        "faces=", certificate["faces"],
        "cells=", certificate["radial_cells"],
    )
    print(
        "histories=", certificate["raw_history_occurrences"],
        "max raw density=", certificate["maximum_raw_density"],
    )


if __name__ == "__main__":
    main()
