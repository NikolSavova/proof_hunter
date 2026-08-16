#!/usr/bin/env python3
"""Exact audit for literal interval loads and the bounded-rank trichotomy."""

from __future__ import annotations

import importlib.util
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


T = load_module("two_reference_data_for_load", HERE / "verify_two_reference_hall_demand.py")
R = T.R


def circuit_profile(
    edge: tuple[int, int], face: tuple[int, ...]
) -> tuple[object, ...]:
    union = tuple(sorted((*edge, *face)))
    for candidate in combinations(union, 4):
        if R.is_convex_face([T.POINTS[i] for i in candidate]):
            continue
        internal = tuple(vertex for vertex in candidate if vertex in face)
        external = tuple(vertex for vertex in candidate if vertex in edge)
        assert len(internal) in (2, 3)
        assert len(internal) + len(external) == 4
        if len(internal) == 2:
            assert len(external) == 2
            return (2, *internal)
        assert len(external) == 1
        role = "left" if external[0] == edge[0] else "right"
        return (3, *internal, role)
    raise AssertionError("bad endpoint union has no four-circuit")


def audit() -> dict[str, object]:
    points = T.POINTS
    n = len(points)
    faces = T.enumerate_faces(points)
    face_set = set(faces)
    total = sum((Q(1, 1 << len(face)) for face in faces), Q())

    cells: defaultdict[tuple[int, int], Q] = defaultdict(Q)
    for face in faces:
        if len(face) >= 2:
            cells[face[0], face[-1]] += Q(1, 1 << len(face))
    p = {edge: mass / total for edge, mass in cells.items()}
    capture = {}
    for edge in combinations(range(n), 2):
        i, j = edge
        interval_total = sum(
            (
                Q(1, 1 << len(face))
                for face in faces
                if all(i < vertex < j for vertex in face)
            ),
            Q(),
        )
        capture[edge] = 4 * cells[edge] / interval_total

    max_radius = max(map(len, faces)) // 2
    cell_weights: list[dict[tuple[int, int], Q]] = []
    radial_degrees: list[Counter[tuple[int, ...]]] = []
    tail_probabilities = []
    demands = []
    for depth in range(max_radius):
        q: defaultdict[tuple[int, int], Q] = defaultdict(Q)
        degrees: Counter[tuple[int, ...]] = Counter()
        for face in faces:
            if len(face) >= 2 * depth + 2:
                q[face[depth], face[-1 - depth]] += Q(1, 1 << len(face)) / total
                degrees[face[depth : len(face) - depth]] += 1
        tau = sum(q.values(), Q())
        if not tau:
            continue
        tail_probabilities.append(tau)
        weights = {edge: (mass / p[edge]) / 4 for edge, mass in q.items()}
        cell_weights.append(weights)
        radial_degrees.append(degrees)
        demands.append(sum((mass / capture[edge] for edge, mass in q.items()), Q()))

    mean_radius = sum(tail_probabilities, Q())
    total_demand = sum(demands, Q())

    loads: dict[tuple[int, ...], Q] = {}
    good_loads: dict[tuple[int, ...], Q] = {}
    bad_loads: dict[tuple[int, ...], Q] = {}
    target_audits = []
    for target in faces:
        load = Q()
        good = Q()
        bad = Q()
        active_cells = []
        for depth, weights in enumerate(cell_weights):
            for edge, weight in weights.items():
                if not all(edge[0] < vertex < edge[1] for vertex in target):
                    continue
                load += weight
                parent = tuple((edge[0], *target, edge[1]))
                is_good = parent in face_set
                if is_good:
                    good += weight
                else:
                    bad += weight
                active_cells.append((depth, edge, weight, is_good))
        loads[target] = load
        good_loads[target] = good
        bad_loads[target] = bad
        if not active_cells:
            continue

        # Aggregate all depths over an endpoint pair, as in Theorem 2.
        endpoint_tilts: defaultdict[tuple[int, int], Q] = defaultdict(Q)
        for _, edge, weight, _ in active_cells:
            endpoint_tilts[edge] += 4 * weight
        total_tilt = sum(endpoint_tilts.values(), Q())
        assert total_tilt == 4 * load
        maximum_endpoint_tilt = max(endpoint_tilts.values())
        depth_count = len(cell_weights)
        good_tilt = 4 * good
        bad_tilt = 4 * bad

        # The aggregate endpoint tilt also gives the heavy-fibre conclusion.
        for edge, endpoint_tilt in endpoint_tilts.items():
            heavy_witnessed = False
            for depth, candidate_edge, weight, _ in active_cells:
                if candidate_edge != edge:
                    continue
                endpoint_parents = [
                    (parent, degree)
                    for parent, degree in radial_degrees[depth].items()
                    if (parent[0], parent[-1]) == edge
                ]
                if endpoint_parents and max(degree for _, degree in endpoint_parents) >= (
                    (4**depth) * endpoint_tilt / depth_count
                ):
                    heavy_witnessed = True
                    break
            assert heavy_witnessed

        if good_tilt >= total_tilt / 2:
            good_edges = {edge for _, edge, _, is_good in active_cells if is_good}
            assert Q(len(good_edges)) >= total_tilt / (2 * maximum_endpoint_tilt)
            for edge in good_edges:
                output = tuple((edge[0], *target, edge[1]))
                assert output in face_set
                assert output[0] == edge[0] and output[-1] == edge[1]
            branch = "tagged_mixed_outputs"
            branch_count = len(good_edges)
        else:
            profiles: defaultdict[tuple[object, ...], Q] = defaultdict(Q)
            profile_edges: defaultdict[tuple[object, ...], set[tuple[int, int]]] = defaultdict(set)
            for _, edge, weight, is_good in active_cells:
                if is_good:
                    continue
                profile = circuit_profile(edge, target)
                profiles[profile] += 4 * weight
                profile_edges[profile].add(edge)
            profile, profile_mass = max(profiles.items(), key=lambda item: item[1])
            profile_cap = math.comb(len(target), 2) + 2 * math.comb(len(target), 3)
            assert profile_cap > 0
            assert profile_mass >= bad_tilt / profile_cap
            assert profile_mass >= total_tilt / (2 * profile_cap)
            assert Q(len(profile_edges[profile])) >= total_tilt / (
                2 * profile_cap * maximum_endpoint_tilt
            )
            branch = "common_circuit_fibre"
            branch_count = len(profile_edges[profile])

        rank_free_branch = "not_blocked"
        rank_free_profiles = 0
        if bad_tilt:
            all_profiles: defaultdict[tuple[object, ...], Q] = defaultdict(Q)
            all_profile_edges: defaultdict[
                tuple[object, ...], set[tuple[int, int]]
            ] = defaultdict(set)
            for _, edge, weight, is_good in active_cells:
                if is_good:
                    continue
                profile = circuit_profile(edge, target)
                all_profiles[profile] += 4 * weight
                all_profile_edges[profile].add(edge)
            largest_profile, largest_profile_tilt = max(
                all_profiles.items(), key=lambda item: item[1]
            )
            rank_free_profiles = len(all_profiles)
            trace_keys = {
                profile if profile[0] == 2 else profile[:-1]
                for profile in all_profiles
            }
            rank_free_traces = len(trace_keys)
            assert 2 * rank_free_traces >= rank_free_profiles
            largest_profile_support = len(all_profile_edges[largest_profile])
            assert Q(rank_free_profiles) >= bad_tilt / largest_profile_tilt
            assert Q(largest_profile_support) >= (
                largest_profile_tilt / maximum_endpoint_tilt
            )

            # Exact cubed comparisons avoid floating-point cube roots.
            if maximum_endpoint_tilt**3 >= bad_tilt:
                rank_free_branch = "heavy_endpoint_fibre"
            elif Q(rank_free_traces * 2) ** 3 >= bad_tilt:
                rank_free_branch = "many_circuit_traces"
            else:
                assert Q(largest_profile_support) ** 3 >= bad_tilt
                rank_free_branch = "common_low_rank_profile"

            # The support graph has either a square-root star or matching.
            support_edges = sorted(all_profile_edges[largest_profile])
            degrees = Counter(vertex for edge in support_edges for vertex in edge)
            maximum_degree = max(degrees.values())
            used: set[int] = set()
            maximal_matching = []
            for edge in support_edges:
                if edge[0] in used or edge[1] in used:
                    continue
                maximal_matching.append(edge)
                used.update(edge)
            support_size = len(support_edges)
            assert maximum_degree**2 >= support_size or (
                2 * len(maximal_matching)
            ) ** 2 >= support_size
        target_audits.append(
            {
                "target": list(target),
                "rank": len(target),
                "load": str(load),
                "good_load": str(good),
                "bad_load": str(bad),
                "maximum_endpoint_tilt": str(maximum_endpoint_tilt),
                "certified_branch": branch,
                "branch_distinct_endpoint_count": branch_count,
                "rank_free_branch": rank_free_branch,
                "rank_free_profile_count": rank_free_profiles,
                "rank_free_trace_count": rank_free_traces if bad_tilt else 0,
            }
        )

    # Exact load identities (5) and compatible/blocked split (11).
    expected_load = sum(
        (Q(1, 1 << len(face)) / total * loads[face] for face in faces), Q()
    )
    expected_good = sum(
        (Q(1, 1 << len(face)) / total * good_loads[face] for face in faces), Q()
    )
    expected_bad = sum(
        (Q(1, 1 << len(face)) / total * bad_loads[face] for face in faces), Q()
    )
    assert expected_load == total_demand
    assert expected_good == mean_radius
    assert expected_bad == total_demand - mean_radius

    heaviest = max(faces, key=lambda face: loads[face])
    heaviest_blocked = max(faces, key=lambda face: bad_loads[face])
    assert loads[heaviest] >= total_demand
    assert bad_loads[heaviest_blocked] >= total_demand - mean_radius
    assert len(heaviest_blocked) >= 2
    assert bad_loads[()] == 0
    assert all(loads[()] >= load for load in loads.values())
    branch_counts = Counter(row["certified_branch"] for row in target_audits)
    assert branch_counts["tagged_mixed_outputs"] > 0
    assert branch_counts["common_circuit_fibre"] > 0

    certificate: dict[str, object] = {
        "description": "literal interval load localization and bounded-rank circuit trichotomy",
        "n": n,
        "faces": len(faces),
        "half_partition_function": str(total),
        "active_depths": len(cell_weights),
        "mean_radial_depth": str(mean_radius),
        "total_inverse_capture_demand": str(total_demand),
        "expected_literal_load": str(expected_load),
        "expected_compatible_load": str(expected_good),
        "expected_blocked_load": str(expected_bad),
        "heaviest_target": list(heaviest),
        "heaviest_target_rank": len(heaviest),
        "heaviest_target_load": str(loads[heaviest]),
        "heaviest_blocked_target": list(heaviest_blocked),
        "heaviest_blocked_target_rank": len(heaviest_blocked),
        "heaviest_blocked_target_load": str(bad_loads[heaviest_blocked]),
        "branch_counts": dict(branch_counts),
        "targets_audited": len(target_audits),
        "claims": [
            "ordinary-face normalized load equals one quarter of cumulative radial endpoint tilt",
            "expected literal load equals total inverse-capture demand",
            "compatible records have expected load exactly equal to mean radial depth",
            "blocked records carry exactly the excess inverse-capture demand",
            "the empty face maximizes total load but has zero blocked load",
            "maximum blocked load is at least total demand minus mean radial depth",
            "tagged mixed outputs recover their endpoint intervals",
            "every bad endpoint union has a canonical two-plus-two or one-plus-three circuit profile",
            "the bounded-rank trichotomy holds target by target",
            "blocked load has a rank-free heavy-endpoint/many-traces/common-profile compression",
            "a common-profile endpoint graph has a square-root star or matching",
        ],
    }
    output = HERE / "literal_interval_load_dichotomy_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    return certificate


def main() -> None:
    certificate = audit()
    print("literal interval load dichotomy audit: PASS")
    print(
        "n=", certificate["n"],
        "faces=", certificate["faces"],
        "demand=", certificate["total_inverse_capture_demand"],
    )
    print(
        "heaviest target/rank/load=",
        certificate["heaviest_target"],
        certificate["heaviest_target_rank"],
        certificate["heaviest_target_load"],
    )


if __name__ == "__main__":
    main()
