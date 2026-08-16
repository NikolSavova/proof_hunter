#!/usr/bin/env python3
"""Exact verifier for synchronized full-ACP singleton reset chains.

The finite geometry uses Fraction throughout.  The scalable history
regression uses exact Pascal-template integer recurrences and exact binomial
counts; floating point is used only to print normalized logarithmic rates.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import ceil, comb, log2
import json
from pathlib import Path

import verify_rooted_hull_kraft_reset as kraft


HERE = Path(__file__).resolve().parent
Point = tuple[Fraction, Fraction]


def projective_chain(source: list[Point]) -> tuple[list[Point], dict[str, str]]:
    source = sorted(source)
    assert kraft.general_position(source)
    slopes = [
        (source[i][1] - source[j][1]) / (source[j][0] - source[i][0])
        for i in range(len(source))
        for j in range(i + 1, len(source))
    ]
    shear = max([Fraction(0), *slopes]) + 1
    increasing_b = [y + shear * x for x, y in source]
    assert all(increasing_b[i] < increasing_b[i + 1] for i in range(len(source) - 1))
    half_c = max(
        [Fraction(0), *(x for x, _ in source), *increasing_b]
    ) + 2
    aa = [half_c - x for x, _ in source]
    bb = [value - half_c for value in increasing_b]
    assert all(aa[i] > aa[i + 1] for i in range(len(aa) - 1))
    assert all(bb[i] < bb[i + 1] for i in range(len(bb) - 1))
    assert all(a > 0 > b and a > b for a, b in zip(aa, bb))
    tips = [(a / (a - b), -Fraction(1, a - b)) for a, b in zip(aa, bb)]
    assert all(0 < x < 1 and y < 0 for x, y in tips)
    assert kraft.general_position(tips)
    return tips, {"shear": str(shear), "half_C": str(half_c)}


def convex_masks(points: list[Point]) -> set[int]:
    return {
        bits
        for bits in range(1 << len(points))
        if kraft.convex(
            points,
            {i for i in range(len(points)) if bits >> i & 1},
        )
    }


def choose_base(tips: list[Point]) -> list[Point]:
    u = (Fraction(0), Fraction(0))
    v = (Fraction(1), Fraction(0))
    for numerator in range(1, 100):
        w = (
            Fraction(numerator, 101),
            Fraction(3, 2) + Fraction(numerator * numerator, 10_201),
        )
        points = [u, v, w, *tips]
        if kraft.general_position(points):
            base = [u, v, w]
            if all(kraft.convex(points, {0, 1, 2, index}) for index in range(3, len(points))):
                return base
    raise AssertionError("failed to choose a general-position outer base")


def hull_equals(points: list[Point], subset: set[int], expected: set[int]) -> None:
    assert kraft.hull_vertices(points, subset) == expected


def finite_geometry_audit() -> dict:
    source = sorted(kraft.pascal_cell(5, 2, Fraction(1, 97)))
    tips, parameters = projective_chain(source)
    assert len(tips) == 10
    base = choose_base(tips)
    points = [*base, *tips]
    base_ids = {0, 1, 2}
    tip_id = lambda index: index + len(base)

    # The arbitrary seed order type is preserved exactly.
    sign_products = set()
    for i, j, k in combinations(range(len(source)), 3):
        left = kraft.cross(source[i], source[j], source[k])
        right = kraft.cross(tips[i], tips[j], tips[k])
        assert left and right
        sign_products.add((left > 0) == (right > 0))
    assert len(sign_products) == 1
    assert convex_masks(source) == convex_masks(tips)

    chain_1 = [0, 2, 4, 6]
    chain_2 = [1, 3, 5, 7]
    blockers = [8, 9]

    # Every global prefix is the full rooted triangle pocket of a later tip.
    containment_checks = 0
    for later in range(1, len(tips)):
        triangle = {0, 1, tip_id(later)}
        for earlier in range(later):
            hull_equals(points, triangle | {tip_id(earlier)}, triangle)
            containment_checks += 1

    def audit_record(earlier: int, later: int) -> None:
        source_ids = base_ids | {tip_id(earlier)}
        target_ids = base_ids | {tip_id(later)}
        union_ids = source_ids | {tip_id(later)}
        assert kraft.convex(points, source_ids)
        assert kraft.convex(points, target_ids)
        assert not kraft.convex(points, union_ids)
        hull_equals(points, union_ids, target_ids)
        assert source_ids - target_ids == {tip_id(earlier)}

    internal_records = []
    for chain in (chain_1, chain_2):
        for left, right in combinations(chain, 2):
            audit_record(left, right)
            internal_records.append((left, right))

    terminal_records = []
    for chain_index, chain in enumerate((chain_1, chain_2), start=1):
        for earlier in chain:
            for blocker in blockers:
                audit_record(earlier, blocker)
                terminal_records.append((chain_index, earlier, blocker))

    # No guarded mixed face contains two cloud labels.
    guarded_mixed_failures = 0
    for left, right in combinations(range(len(tips)), 2):
        subset = base_ids | {tip_id(left), tip_id(right)}
        assert not kraft.convex(points, subset)
        guarded_mixed_failures += 1

    # Every actual fixed-core record maps injectively to its rank-two label pair.
    all_records = [(left, right) for left, right in internal_records]
    all_records += [(earlier, blocker) for _, earlier, blocker in terminal_records]
    assert len(set(all_records)) == len(all_records)
    rank_two_code = Counter(tuple(sorted(record)) for record in all_records)
    assert max(rank_two_code.values()) == 1
    for left, right in rank_two_code:
        assert kraft.convex(points, {tip_id(left), tip_id(right)})

    # Direct cross-chain terminal two-record code has load at most two.
    terminal_code = Counter()
    for left in chain_1:
        for right in chain_2:
            for blocker_1 in blockers:
                for blocker_2 in blockers:
                    output = (
                        tuple(sorted((left, right))),
                        tuple(sorted((blocker_1, blocker_2))),
                    )
                    terminal_code[output] += 1
    assert max(terminal_code.values()) == 2

    # Same marked target and same blocker: (T,{x1,x2}) is injective here.
    same_target_code = Counter()
    for blocker in blockers:
        target = tuple(sorted(base_ids | {tip_id(blocker)}))
        for left in chain_1:
            for right in chain_2:
                output = (target, tuple(sorted((tip_id(left), tip_id(right)))))
                same_target_code[output] += 1
    assert max(same_target_code.values()) == 1

    # All length-two histories are genuine, but terminal incidences repeat.
    history_length = 2
    histories = []
    terminal_multiplicity = Counter()
    for chain_index, chain in enumerate((chain_1, chain_2), start=1):
        for history in combinations(chain, history_length):
            audit_record(history[0], history[1])
            for blocker in blockers:
                audit_record(history[-1], blocker)
                histories.append((chain_index, history, blocker))
                terminal_multiplicity[(chain_index, history[-1], blocker)] += 1
    assert len(histories) == 2 * len(blockers) * comb(4, history_length)
    assert max(terminal_multiplicity.values()) == comb(3, history_length - 1)
    assert len(terminal_records) == len(blockers) * (len(chain_1) + len(chain_2))

    # Adding the three-point base costs at most 2^3 in face count.
    tip_faces = convex_masks(tips)
    total_faces = convex_masks(points)
    assert len(total_faces) <= (1 << len(base)) * len(tip_faces)

    return {
        "seed": "central Pascal T_(5,2)",
        "tip_count": len(tips),
        "chain_sizes": [len(chain_1), len(chain_2)],
        "common_blockers": len(blockers),
        "projective_parameters": parameters,
        "full_pocket_containments": containment_checks,
        "internal_actual_records": len(internal_records),
        "terminal_actual_records": len(terminal_records),
        "length_two_histories": len(histories),
        "maximum_terminal_history_multiplicity": max(terminal_multiplicity.values()),
        "guarded_mixed_nonfaces": guarded_mixed_failures,
        "rank_two_record_code_load": max(rank_two_code.values()),
        "terminal_pair_code_load": max(terminal_code.values()),
        "same_target_pair_code_load": max(same_target_code.values()),
        "tip_convex_subsets": len(tip_faces),
        "total_convex_subsets_with_base": len(total_faces),
        "base_factor_bound": (1 << len(base)) * len(tip_faces),
    }


def variable_core_geometry_audit() -> dict:
    """Audit fixed-mark decoding on compatible and incompatible cores."""
    u = (Fraction(0), Fraction(0))
    v = (Fraction(1), Fraction(0))
    cap_size = 6
    cap = []
    for index in range(1, cap_size + 1):
        parameter = Fraction(index, cap_size + 1)
        cap.append((parameter, parameter * (1 - parameter)))
    ear = (Fraction(2, 5), Fraction(-1, 2))
    blocker = (Fraction(3, 5), Fraction(-2))
    points = [u, v, *cap, ear, blocker]
    assert kraft.general_position(points)
    ear_id = 2 + cap_size
    blocker_id = ear_id + 1

    sources = Counter()
    targets = Counter()
    cores = []
    for bits in range(1 << cap_size):
        core = {0, 1} | {
            2 + index for index in range(cap_size) if bits >> index & 1
        }
        source = core | {ear_id}
        target = core | {blocker_id}
        assert kraft.convex(points, source)
        assert kraft.convex(points, target)
        assert not kraft.convex(points, source | {blocker_id})
        assert kraft.hull_vertices(points, source | {blocker_id}) == target
        sources[tuple(sorted(source))] += 1
        targets[tuple(sorted(target))] += 1
        cores.append(core)
    assert max(sources.values()) == max(targets.values()) == 1
    assert all(
        kraft.convex(points, cores[left] | cores[right])
        for left, right in combinations(range(len(cores)), 2)
    )

    # A separate exact pair whose union is nonconvex.  Target decoding is
    # still injective, showing that core compatibility is irrelevant.
    incompatible_points = [
        u,
        v,
        (Fraction(1, 4), Fraction(1)),
        (Fraction(3, 4), Fraction(11, 10)),
        (Fraction(1, 2), Fraction(2, 5)),
        ear,
        blocker,
    ]
    assert kraft.general_position(incompatible_points)
    outer_core = {0, 1, 2, 3}
    inner_core = {0, 1, 4}
    assert kraft.convex(incompatible_points, outer_core)
    assert kraft.convex(incompatible_points, inner_core)
    assert not kraft.convex(incompatible_points, outer_core | inner_core)
    incompatible_targets = []
    for core in (outer_core, inner_core):
        source = core | {5}
        target = core | {6}
        assert kraft.convex(incompatible_points, source)
        assert kraft.convex(incompatible_points, target)
        assert not kraft.convex(incompatible_points, source | {6})
        assert kraft.hull_vertices(incompatible_points, source | {6}) == target
        incompatible_targets.append(tuple(sorted(target)))
    assert len(set(incompatible_targets)) == 2

    return {
        "boolean_compatible_core_count": len(cores),
        "fixed_pair_source_decoder_load": max(sources.values()),
        "fixed_pair_target_decoder_load": max(targets.values()),
        "all_boolean_core_unions_convex": True,
        "incompatible_core_pair_audited": True,
        "incompatible_pair_target_decoder_load": 1,
    }


def profile(points: list[Point]) -> tuple[list[int], list[int], list[int]]:
    n = len(points)
    caps = [0] * (n + 1)
    cups = [0] * (n + 1)
    convex = [0] * (n + 1)
    for size in range(1, n + 1):
        for subset in combinations(range(n), size):
            signs = [
                kraft.cross(points[i], points[j], points[k])
                for i, j, k in combinations(subset, 3)
            ]
            caps[size] += all(sign < 0 for sign in signs)
            cups[size] += all(sign > 0 for sign in signs)
            convex[size] += kraft.convex(points, set(subset))
    return caps, cups, convex


def evaluate(polynomial: list[int], value: int, shift: int) -> int:
    return sum(
        coefficient * value ** (degree - shift)
        for degree, coefficient in enumerate(polynomial)
        if degree >= shift
    )


def scalable_history_audit() -> dict:
    template = sorted(kraft.pascal_cell(4, 2, Fraction(1, 97)))
    caps, cups, convex_profile = profile(template)
    template_size = len(template)
    largest_cap = max(index for index, value in enumerate(caps) if value)
    largest_cup = max(index for index, value in enumerate(cups) if value)
    assert template_size == 6 and largest_cap == largest_cup == 3

    size = cap_total = cup_total = convex_total = 1
    rows = []
    for depth in range(1, 41):
        old_size = size
        old_cap, old_cup, old_convex = cap_total, cup_total, convex_total
        cap_total = old_cap * evaluate(caps, old_size, 1)
        cup_total = old_cup * evaluate(cups, old_size, 1)
        convex_total = (
            template_size * old_convex
            + old_cap * old_cup * evaluate(convex_profile, old_size, 2)
        )
        size *= template_size
        if depth not in {8, 16, 24, 32, 40}:
            continue
        chain_size = size // 3
        blocker_count = size - 2 * chain_size
        history_length = min(chain_size, int(log2(size)))
        history_pairs = blocker_count**2 * comb(chain_size, history_length) ** 2
        base_rank = ceil(log2(size))
        face_upper = (1 << base_rank) * (convex_total + 1)
        denominator = face_upper**2
        fibre_lower = (history_pairs + denominator - 1) // denominator
        log_size = log2(size)
        rows.append(
            {
                "depth": depth,
                "point_count": size,
                "history_length": history_length,
                "base_rank": base_rank,
                "log2_convex_upper": log2(convex_total + 1),
                "normalized_convex_rate": log2(convex_total + 1) / log_size**2,
                "log2_history_pair_count": log2(history_pairs),
                "log2_two_face_fibre_lower": log2(fibre_lower),
                "normalized_fibre_lower": log2(fibre_lower) / log_size**2,
            }
        )
    limit_rate = (largest_cap + largest_cup - 2) / (2 * log2(template_size))
    assert limit_rate < 0.78
    assert rows[-1]["normalized_fibre_lower"] > 0.30
    return {
        "template": "vertical iterates of central Pascal T_(4,2)",
        "template_size": template_size,
        "cap_profile": caps[1:],
        "cup_profile": cups[1:],
        "convex_profile": convex_profile[1:],
        "exact_limit_convex_rate": limit_rate,
        "audited_depths": rows,
        "interpretation": (
            "history pairs force a quadratic-log two-face fibre even though "
            "the distinct fixed-core incidence support has a rank-two injection"
        ),
    }


def abstract_overlap_audit() -> dict:
    # Exact saturation of the marked-target decoder's |T| ambiguity.
    target = frozenset({100, 101, 102, 103})
    chain_1 = [1, 2, 3]
    chain_2 = [11, 12]
    decoder = Counter()
    for mark in target:
        for left in chain_1:
            for right in chain_2:
                decoder[(target, frozenset({left, right}))] += 1
    assert max(decoder.values()) == len(target)

    # Exact outer-core overlap of the rank-two record code.
    cores = range(7)
    records = [(core, 5, 9) for core in cores]
    pair_code = Counter(frozenset({x, blocker}) for _, x, blocker in records)
    assert max(pair_code.values()) == len(cores)
    return {
        "marked_target_rank": len(target),
        "marked_target_decoder_load": max(decoder.values()),
        "outer_cores_on_one_ear_blocker_pair": len(cores),
        "rank_two_decoder_load": max(pair_code.values()),
    }


def fixed_mark_decoder_audit() -> dict:
    """Saturate the exact rank losses in the source/target decoders."""
    ground = tuple(range(8))
    rank = 5
    fixed_ear = 100
    target_decoder = Counter()
    fixed_ear_records = set()
    for target in combinations(ground, rank):
        target_set = frozenset(target)
        for blocker in target:
            core = target_set - {blocker}
            source = core | {fixed_ear}
            record = (source, blocker, target_set)
            fixed_ear_records.add(record)
            target_decoder[target_set] += 1
    assert max(target_decoder.values()) == rank

    fixed_blocker = 101
    source_decoder = Counter()
    fixed_blocker_records = set()
    for source in combinations(ground, rank):
        source_set = frozenset(source)
        for ear in source:
            core = source_set - {ear}
            target = core | {fixed_blocker}
            record = (source_set, ear, target)
            fixed_blocker_records.add(record)
            source_decoder[source_set] += 1
    assert max(source_decoder.values()) == rank

    fixed_pair_targets = Counter()
    for core in combinations(ground, rank - 1):
        target = frozenset(core) | {fixed_blocker}
        fixed_pair_targets[target] += 1
    assert max(fixed_pair_targets.values()) == 1
    return {
        "rank": rank,
        "fixed_ear_record_count": len(fixed_ear_records),
        "fixed_ear_target_load": max(target_decoder.values()),
        "fixed_blocker_record_count": len(fixed_blocker_records),
        "fixed_blocker_source_load": max(source_decoder.values()),
        "fixed_pair_target_load": max(fixed_pair_targets.values()),
    }


def main() -> None:
    certificate = {
        "description": "two synchronized full-ACP reset chains",
        "arithmetic": "Fraction for geometry; exact integers for histories and Pascal recurrences",
        "finite_geometry": finite_geometry_audit(),
        "variable_core_geometry": variable_core_geometry_audit(),
        "scalable_history_regression": scalable_history_audit(),
        "decoder_overlap": abstract_overlap_audit(),
        "fixed_mark_decoders": fixed_mark_decoder_audit(),
        "assertions": [
            "every selected arrow is an actual exterior repair with its exact source, target, blocker, and singleton hidden ear",
            "the two chains share the complete terminal blocker alphabet",
            "all earlier states satisfy full rooted-triangle pocket containment",
            "fixed-core actual incidences inject into rank-two ordinary faces",
            "quadratic history entropy repeatedly traverses the same actual incidence support",
            "rank-two core multiplicity matters only when neither ear nor blocker mark is fixed",
            "same marked targets have a two-face decoder of load at most target rank",
            "fixed ear labels map all core/blocker variation to targets with rank load",
            "fixed blocker labels map all core/ear variation to sources with rank load",
            "fixed ear-blocker pairs map injectively even for incompatible cores",
        ],
    }
    output = HERE / "two_chain_synchronized_acp_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    finite = certificate["finite_geometry"]
    scalable = certificate["scalable_history_regression"]["audited_depths"][-1]
    print(
        "finite ACP audit: "
        f"{finite['terminal_actual_records']} terminal records, "
        f"rank-two load {finite['rank_two_record_code_load']}"
    )
    print(
        "depth-40 history regression: normalized two-face fibre lower "
        f"{scalable['normalized_fibre_lower']:.6f}"
    )
    print(f"PASS: wrote {output}")


if __name__ == "__main__":
    main()
