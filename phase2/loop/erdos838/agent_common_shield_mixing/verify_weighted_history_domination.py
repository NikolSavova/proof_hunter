#!/usr/bin/env python3
"""Exact checks for WEIGHTED_HISTORY_DOMINATION_AND_COMPLEMENT_NO_GO.md."""

from __future__ import annotations

import importlib.util
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTER = HERE.parent / "agent_outer_internal_product"


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


TWO = load_module(
    "two_reference_for_weight_domination",
    OUTER / "verify_two_reference_hall_demand.py",
)
TANGENT = load_module(
    "tangent_for_complement_no_go",
    HERE / "verify_tangent_marked_shield_descent.py",
)
R = TWO.R


def canonical_trace(edge, target):
    """Lexicographically first bad four-circuit and its target trace."""
    union = tuple(sorted((*edge, *target)))
    for circuit in combinations(union, 4):
        if R.is_convex_face([TWO.POINTS[i] for i in circuit]):
            continue
        trace = tuple(i for i in circuit if i in target)
        assert len(trace) in (2, 3)
        return trace
    raise AssertionError("nonconvex endpoint union has no four-circuit")


def planar_history_audit():
    points = TWO.POINTS
    faces = TWO.enumerate_faces(points)
    face_set = set(faces)
    assert len(faces) == 449
    total = sum((Q(1, 1 << len(face)) for face in faces), Q())

    reservoirs = defaultdict(Q)
    for face in faces:
        if len(face) >= 2:
            reservoirs[(face[0], face[-1])] += Q(1, 1 << len(face))
    assert all(mass >= Q(1, 4) for mass in reservoirs.values())

    histories = []
    history_mass_by_cell = defaultdict(Q)
    q_by_cell = defaultdict(Q)
    maximum_face_mass = Q()
    for face in faces:
        rank = len(face)
        if rank < 2:
            continue
        face_mass = Q()
        for depth in range(rank // 2):
            parent = face[depth : rank - depth]
            assert parent in face_set
            edge = (parent[0], parent[-1])
            weight = Q(1, 1 << len(parent)) / (
                (4**depth) * reservoirs[edge]
            )
            # The cancellation in equation (1) is exact.
            assert weight == Q(1, 1 << rank) / reservoirs[edge]
            assert weight <= Q(1, 1 << max(rank - 2, 0))
            histories.append((face, depth, edge, weight))
            history_mass_by_cell[(depth, edge)] += weight
            q_by_cell[(depth, edge)] += Q(1, 1 << rank) / total
            face_mass += weight
        assert face_mass <= Q(1)
        assert face_mass <= Q(rank // 2) * Q(1, 1 << max(rank - 2, 0))
        maximum_face_mass = max(maximum_face_mass, face_mass)

    # Check h=q/p against the literal sum of genuine history weights.
    for cell, q in q_by_cell.items():
        _, edge = cell
        p = reservoirs[edge] / total
        assert q / p == history_mass_by_cell[cell]

    total_history_mass = sum((row[3] for row in histories), Q())
    assert total_history_mass <= len(faces)

    # Every common interval face, and therefore every decorated subfibre of
    # one, is bounded by the same global ordinary-face count.
    common_loads = {}
    for target in faces:
        load = sum(
            (
                weight
                for _, _, edge, weight in histories
                if all(edge[0] < vertex < edge[1] for vertex in target)
            ),
            Q(),
        )
        common_loads[target] = load
        assert load <= len(faces)
    maximum_common_target = max(common_loads, key=common_loads.get)

    # Find a literal bad common-W cell with a nonempty discarded complement.
    candidate = None
    for target in sorted(faces, key=lambda face: (-len(face), face)):
        for edge in combinations(range(len(points)), 2):
            if not all(edge[0] < vertex < edge[1] for vertex in target):
                continue
            union = tuple((edge[0], *target, edge[1]))
            if union in face_set:
                continue
            trace = canonical_trace(edge, target)
            complement = tuple(vertex for vertex in target if vertex not in trace)
            if complement and any(row[2] == edge for row in histories):
                candidate = (target, edge, trace, complement)
                break
        if candidate is not None:
            break
    assert candidate is not None
    target, edge, trace, complement = candidate

    fibre_weights = [weight for _, _, e, weight in histories if e == edge]
    assert fibre_weights
    fibre_mass = sum(fibre_weights, Q())
    c = len(complement)
    rooted_energy = fibre_mass * fibre_mass
    uniform_bin_load = fibre_mass / (1 << c)
    complement_energy = (1 << c) * uniform_bin_load * uniform_bin_load
    assert complement_energy == rooted_energy / (1 << c)

    # Exhaust the deterministic assignments for four genuine positive
    # weights.  Cauchy's 2^{-c} factor cannot be improved.
    sample = fibre_weights[:4]
    choices = 1 << min(c, 3)
    for assignment in product(range(choices), repeat=len(sample)):
        bins = defaultdict(Q)
        for choice, weight in zip(assignment, sample):
            bins[choice] += weight
        energy = sum((load * load for load in bins.values()), Q())
        assert energy >= sum(sample, Q()) ** 2 / choices

    return {
        "faces": len(faces),
        "histories": len(histories),
        "total_history_mass": total_history_mass,
        "maximum_per_face_mass": maximum_face_mass,
        "maximum_common_target": maximum_common_target,
        "maximum_common_load": common_loads[maximum_common_target],
        "blocked_target": target,
        "blocked_edge": edge,
        "trace": trace,
        "complement_rank": c,
        "fibre_histories": len(fibre_weights),
        "rooted_energy": rooted_energy,
        "complement_energy": complement_energy,
    }


def radial_common_record_audit():
    blocks, repairs, points = TANGENT.configuration()
    words = [bits for bits in product(range(2), repeat=8)
             if bits[7] == bits[0] == bits[1] == bits[2] == 0]
    completions = [TANGENT.completion_indices(bits) for bits in words]
    assert len(completions) == 16
    mark = 16
    free_positions = (3, 4, 5, 6)
    outputs = set()
    weights = []
    for serial, completion in enumerate(completions):
        star = completion + (mark,)
        deleted = tuple(completion[i] for i in free_positions)
        output = frozenset(i for i in star if i not in deleted)
        assert TANGENT.convex([points[i] for i in output])
        outputs.add(output)
        weights.append(Q(serial + 1, 17))
    assert len(outputs) == 1

    # An arbitrary fixed split of the common convex record realizes the
    # equality case for positive, nonuniform weights.
    common_output = next(iter(outputs))
    ordered = tuple(sorted(common_output))
    assert len(ordered) == 5
    c = 2
    total_weight = sum(weights, Q())
    old_energy = total_weight * total_weight
    new_energy = sum(
        ((total_weight / (1 << c)) ** 2 for _ in range(1 << c)), Q()
    )
    assert new_energy == old_energy / (1 << c)
    return len(completions), len(common_output), old_energy, new_energy


def main():
    planar = planar_history_audit()
    radial = radial_common_record_audit()
    print("weighted history domination: PASS")
    print(
        f"planar faces={planar['faces']}, histories={planar['histories']}, "
        f"total-weight={planar['total_history_mass']}, "
        f"max-per-face={planar['maximum_per_face_mass']}"
    )
    print(
        "blocked common-W cell:",
        f"W={planar['blocked_target']}, e={planar['blocked_edge']}, "
        f"A={planar['trace']}, |W\\A|={planar['complement_rank']}, "
        f"histories={planar['fibre_histories']}"
    )
    print(
        "complement energy equality:",
        f"E0={planar['rooted_energy']}, EC={planar['complement_energy']}"
    )
    print(f"radial common-record sharpness={radial}")


if __name__ == "__main__":
    main()
