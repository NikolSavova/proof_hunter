#!/usr/bin/env python3
"""Exact audits for STRICT_PARENT_PROFILE_RIGIDITY_GATE.md."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import importlib.util
import json
import math
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS / "agent_graded_supersat"))

from graded_balanced import central_template, vertical_iterate  # noqa: E402


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def pascal_mutation_and_history_audit() -> dict[str, int]:
    """Reconstruct the exact finite live ledger and weighted failure."""
    k, depth, pocket_k = 12, 3, 24
    q = depth * (2 * k - 4)
    a, cap_profile, cup_profile, face_profile = vertical_iterate(
        central_template(k), depth, q
    )
    b, pocket_caps, pocket_cups, pocket_faces = central_template(pocket_k)
    cap_a = sum(cap_profile)
    cup_a = sum(cup_profile)
    faces_a = sum(face_profile)
    cup_b = sum(pocket_cups)

    # The coarse consequence of the second weighted moment inequality.
    weighted_bound = a + a * cup_a + cup_b * a * a
    assert faces_a > weighted_bound
    mutation_ratio_bits = (faces_a // weighted_bound).bit_length() - 1
    assert mutation_ratio_bits >= 716

    # Reconstruct the localized fixed-edge/downshadow source family.
    top_total = face_profile[q]
    delta = 0
    while a > 1 << (1 << delta):
        delta += 1
    log_floor = a.bit_length() - 1
    rank = log_floor - delta
    directed_edges = a * (a - 1)
    edge_fibre = ceil_div(q * top_total, directed_edges)
    incidence = edge_fibre * math.comb(q - 2, rank - 2)
    maximum_multiplicity = math.comb(a - rank, q - rank)
    source_family = ceil_div(incidence, maximum_multiplicity)

    pocket_top_rank = 2 * pocket_k - 4
    pocket_top = pocket_faces[pocket_top_rank]
    parent_faces = (
        faces_a + sum(pocket_faces) + cap_a * cup_b
    )
    records = source_family * pocket_top
    assert records > parent_faces

    # Release routing has exact load |A| and exactly |H| distinct outputs.
    natural_load = source_family
    assert records // natural_load == pocket_top
    assert pocket_top < parent_faces
    useful_average_load = Fraction(records, parent_faces)
    assert Fraction(natural_load) > useful_average_load
    history_deficit_bits = (parent_faces // pocket_top).bit_length() - 1
    assert history_deficit_bits >= 559

    return {
        "source_size_bits": a.bit_length(),
        "source_cap_bits": cap_a.bit_length(),
        "source_face_bits": faces_a.bit_length(),
        "pocket_cup_bits": cup_b.bit_length(),
        "mutation_ratio_bits": mutation_ratio_bits,
        "source_family_bits": source_family.bit_length(),
        "pocket_top_bits": pocket_top.bit_length(),
        "parent_bits": parent_faces.bit_length(),
        "record_surplus_bits": (records // parent_faces).bit_length() - 1,
        "history_deficit_bits": history_deficit_bits,
    }


def strict_gap_audit() -> int:
    """A strict integer upper never makes a positive mutation safe."""
    checks = 0
    for threshold in (2, 3, 17, 10**6, 1 << 200):
        value = threshold - 1
        assert value < threshold
        assert value + 1 == threshold
        checks += 1
    # The unrounded slack can also be arbitrarily less than one.
    for denominator in (2, 3, 17, 1009):
        value = 10**6
        target = Fraction(value * denominator + 1, denominator)
        assert Fraction(value) < target < value + 1
        assert Fraction(value + 1) >= target
        checks += 1
    return checks


def scalar_survivor_audit() -> list[dict[str, int]]:
    """Check all four weighted moment inequalities and scale separations."""
    rows = []
    for d in (64, 128, 256):
        log_d = d.bit_length() - 1
        assert d == 1 << log_d
        m = 1 << d
        r = d
        h = d * d // 2 - 4 * d * log_d
        # Make log_2(rH/m) even so x=2 sqrt(rH/m) is integral.
        if (log_d + h - d) % 2:
            h += 1
        H = 1 << h
        x = 1 << (1 + (log_d + h - d) // 2)
        y = 4 * r * H // m
        assert x * x == 4 * r * H // m

        ell = m + math.comb(m, 2)
        assert ell <= x <= y <= H
        assert H <= x * y

        mu = r
        moment_c_a = r * x
        moment_u_a = r * y
        lhs = mu * H + x * moment_c_a
        first_branch = (1 + x) * (m + m * x - moment_c_a)
        second_branch = m + m * y - moment_u_a + x * m * m
        assert lhs <= first_branch
        assert lhs <= second_branch
        # The B inequalities are identical after C/U reflection.
        forced_facing_floor = Fraction(r * H, 4 * m)
        assert Fraction(x * x) == 16 * forced_facing_floor

        # Envelope comparison with f=H and p=x is exact.
        f = H
        p = x
        assert x <= p and H - f <= x * (p - x)
        assert y >= x  # reflection is nonimproving at penalty x
        # The all-cup competitor is also nonimproving without constructing
        # the astronomically large integer 2^m explicitly.
        assert h + 2 < m
        assert H + x * x < 1 << (h + 2)

        parent = 2 * H + x * x
        target_exponent = h + d - 8 * log_d
        target = 1 << target_exponent
        wall = y * y - x * x
        assert parent < target
        assert x * x < target
        assert wall > target

        endpoint = (y + (m + 1) * x) ** 2
        assert endpoint >= 4 * (m + 1) * H
        decoder_load = ceil_div(endpoint, parent)
        assert decoder_load > d**10

        # A formal dense all-delete ledger still releases only one bank.
        sources = H - x
        pockets = H - x
        records = sources * pockets
        assert records // sources == pockets
        assert pockets < parent

        rows.append({
            "d": d,
            "h": h,
            "facing_bits": x.bit_length() - 1,
            "opposite_bits": y.bit_length() - 1,
            "parent_bits": parent.bit_length() - 1,
            "target_bits": target_exponent,
            "wall_bits": wall.bit_length() - 1,
            "decoder_load_bits": decoder_load.bit_length() - 1,
        })
    return rows


def subset_is_cap(wrapper, signs, order, subset: tuple[int, ...]) -> bool:
    if len(subset) <= 2:
        return True
    selected = [label for label in order if label in subset]
    return all(
        wrapper.ordered_sign(signs, *triple) < 0
        for triple in combinations(selected, 3)
    )


def subset_is_cup(wrapper, signs, order, subset: tuple[int, ...]) -> bool:
    if len(subset) <= 2:
        return True
    selected = [label for label in order if label in subset]
    return all(
        wrapper.ordered_sign(signs, *triple) > 0
        for triple in combinations(selected, 3)
    )


def nine_point_minimizer_audit() -> dict[str, object]:
    wrapper = load_module(
        "strict_profile_wrapper",
        ERDOS / "agent_shield_circuit_cover" /
        "verify_two_direction_four_point_wrapper.py",
    )
    hull_module = load_module(
        "strict_profile_hull",
        ERDOS / "agent_lex_minimizer_search" / "direct_hull_verify.py",
    )
    data = json.loads(
        (ERDOS / "agent_lex_minimizer_search" /
         "direct_hull_certificates.json").read_text()
    )["9"]
    points = [tuple(map(Fraction, point)) for point in data["coordinates"]]
    signs = wrapper.all_signs(points)
    perturbed = wrapper.generic_perturb(points, signs)
    orders = wrapper.projection_orders(perturbed)
    assert len(orders) == 72
    profiles = [wrapper.chain_counts(signs, order) for order in orders]
    assert min(cap for cap, _ in profiles) == 82
    assert min(cup for _, cup in profiles) == 82
    assert data["nonempty_count"] == 168

    # Any sibling of size at least four has facing penalty t>=10.
    t = 10
    minimizer_objective = 168 + t * 82
    all_cup_objective = (1 << 9) - 1 + t * (9 + math.comb(9, 2))
    decrease = minimizer_objective - all_cup_objective
    assert decrease == 27

    # Precompute intrinsic face status for all nonempty label sets.
    face = {}
    subsets = {}
    for mask in range(1, 1 << 9):
        subset = tuple(label for label in range(9) if mask >> label & 1)
        subsets[mask] = subset
        selected_points = [points[label] for label in subset]
        face[mask] = (
            len(subset) <= 2
            or len(hull_module.hull(selected_points)) == len(subset)
        )

    seams = 0
    minimum_mismatches = 1 << 9
    cuts_checked = 0
    for order in orders:
        cap = {
            mask: subset_is_cap(wrapper, signs, order, subset)
            for mask, subset in subsets.items()
        }
        cup = {
            mask: subset_is_cup(wrapper, signs, order, subset)
            for mask, subset in subsets.items()
        }
        for cut in range(1, 9):
            left_mask = sum(1 << label for label in order[:cut])
            right_mask = ((1 << 9) - 1) ^ left_mask
            mismatches = 0
            for mask in subsets:
                left = mask & left_mask
                right = mask & right_mask
                if not left:
                    predicted = face[right]
                elif not right:
                    predicted = face[left]
                else:
                    predicted = cap[left] and cup[right]
                if predicted != face[mask]:
                    mismatches += 1
            cuts_checked += 1
            minimum_mismatches = min(minimum_mismatches, mismatches)
            if mismatches == 0:
                seams += 1
    assert seams == 0
    assert minimum_mismatches == 10

    return {
        "projection_chambers": len(orders),
        "unique_profiles": len(set(profiles)),
        "minimum_cap": min(cap for cap, _ in profiles),
        "weighted_decrease_at_t10": decrease,
        "cuts_checked": cuts_checked,
        "literal_seams": seams,
        "minimum_mismatches": minimum_mismatches,
    }


def main() -> None:
    pascal = pascal_mutation_and_history_audit()
    gaps = strict_gap_audit()
    scalar = scalar_survivor_audit()
    minimizer = nine_point_minimizer_audit()
    print(
        "PASS: strict-parent/profile rigidity gate; "
        f"pascal={pascal}; gap_checks={gaps}; scalar={scalar}; "
        f"n9={minimizer}"
    )


if __name__ == "__main__":
    main()
