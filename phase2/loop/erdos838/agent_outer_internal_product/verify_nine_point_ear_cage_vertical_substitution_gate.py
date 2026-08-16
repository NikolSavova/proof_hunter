#!/usr/bin/env python3
"""Exact audit for NINE_POINT_EAR_CAGE_VERTICAL_SUBSTITUTION_GATE.

The audit has four independent parts.

1. Enumerate every shear-projection chamber of the exact nine-point
   minimizer and its cap/cup/face profiles.
2. Apply the exact heterogeneous vertical-substitution recurrence, including
   exhaustive one-, two-, and three-leaf deletion tests at depth two.
3. Count literal lifted three-ear contexts and compare their polynomial
   entropy with the quadratic face entropy of the iterate.
4. Check the already-banked three-map rational IFS at depth three against the
   one-point minimizer inequality.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))
sys.path.insert(0, str(ERDOS / "agent_lex_minimizer_search"))

import reflection_trace as rt  # noqa: E402
import triangular_ifs_probe as ifs  # noqa: E402
from agent_outer_internal_product.verify_fixed_anchor_relocation_cancellation_gate import (  # noqa: E402
    families,
)
from agent_outer_internal_product.verify_three_ear_minimizer_barrier_and_order_three_gate import (  # noqa: E402
    three_ear_check,
)


Stats = tuple[int, int, int, int]  # size, caps, cups, nonempty faces
Masks = tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]


def nine_points():
    data = json.loads(
        (ERDOS / "agent_lex_minimizer_search"
         / "exact_realizable_n9.json").read_text()
    )
    return [tuple(map(Fraction, point))
            for point in data["coordinates_as_stored"]]


def mask_families(points) -> Masks:
    faces, caps, cups = families(points)
    return tuple(faces), tuple(caps), tuple(cups)


def terms(masks):
    return tuple(
        tuple(index for index in range(9) if mask >> index & 1)
        for mask in masks
    )


def compose(macro: Masks, children: list[Stats]) -> Stats:
    """Exact heterogeneous vertical composition, equations (12)--(14)."""
    face_masks, cap_masks, cup_masks = macro
    face_terms, cap_terms, cup_terms = map(
        terms, (face_masks, cap_masks, cup_masks)
    )
    sizes = [row[0] for row in children]
    caps = [row[1] for row in children]
    cups = [row[2] for row in children]
    faces = [row[3] for row in children]

    cap_total = 0
    for indices in cap_terms:
        value = caps[indices[0]]
        for index in indices[1:]:
            value *= sizes[index]
        cap_total += value

    cup_total = 0
    for indices in cup_terms:
        value = cups[indices[-1]]
        for index in indices[:-1]:
            value *= sizes[index]
        cup_total += value

    face_total = sum(faces)
    for indices in face_terms:
        if len(indices) < 2:
            continue
        value = caps[indices[0]] * cups[indices[-1]]
        for index in indices[1:-1]:
            value *= sizes[index]
        face_total += value
    return sum(sizes), cap_total, cup_total, face_total


def projection_chambers(points):
    """One exact shear representative from each generic half-turn chamber."""
    walls = sorted({
        -(points[j][0] - points[i][0]) / (points[j][1] - points[i][1])
        for i in range(9)
        for j in range(i + 1, 9)
        if points[j][1] != points[i][1]
    })
    samples = [walls[0] - 1]
    samples.extend((left + right) / 2
                   for left, right in zip(walls, walls[1:]))
    samples.append(walls[-1] + 1)
    return [
        sorted((x + amount * y, y) for x, y in points)
        for amount in samples
    ]


def rank_profile(masks):
    result = {}
    for mask in masks:
        rank = mask.bit_count()
        result[rank] = result.get(rank, 0) + 1
    return result


def chamber_and_rechart_audit():
    points = nine_points()
    chambers = projection_chambers(points)
    assert len(chambers) == 37
    macros = [mask_families(chamber) for chamber in chambers]
    for face_masks, cap_masks, cup_masks in macros:
        assert len(face_masks) == 168
        assert max(mask.bit_count() for mask in cap_masks) == 5
        assert max(mask.bit_count() for mask in cup_masks) == 5

    one = (1, 1, 1, 1)
    zero = (0, 0, 0, 0)
    seeds = [compose(macro, [one] * 9) for macro in macros]
    deleted = [
        [compose(macro, [zero if i == leaf else one for i in range(9)])
         for leaf in range(9)]
        for macro in macros
    ]

    all_gaps = []
    configuration_worst_gaps = []
    for macro in macros:
        for micro_index, seed in enumerate(seeds):
            full = compose(macro, [seed] * 9)
            gaps = []
            for block in range(9):
                for leaf in range(9):
                    children = [seed] * 9
                    children[block] = deleted[micro_index][leaf]
                    base = compose(macro, children)
                    loss = full[3] - base[3]
                    gap = 1 + min(base[1], base[2]) - loss
                    gaps.append(gap)
            all_gaps.extend(gaps)
            configuration_worst_gaps.append(min(gaps))

    # Every one of the 37^2 independently recharted two-level compositions
    # fails singleton minimality at every one of its 81 physical labels.
    assert max(all_gaps) == -584054
    assert max(configuration_worst_gaps) == -8137810
    return len(chambers), len(macros) ** 2, min(all_gaps), max(all_gaps)


def fixed_chart_deletion_audit():
    macro = mask_families(sorted(nine_points()))
    one = (1, 1, 1, 1)
    zero = (0, 0, 0, 0)

    @lru_cache(None)
    def child(deleted_leaves):
        deleted = set(deleted_leaves)
        return compose(macro, [zero if i in deleted else one
                               for i in range(9)])

    seed = child(())
    assert seed == (9, 115, 90, 168)
    full = compose(macro, [seed] * 9)
    assert full == (81, 2702385, 1641060, 61014762)

    def deletion_stats(deleted_labels):
        by_block = [[] for _ in range(9)]
        for label in deleted_labels:
            by_block[label // 9].append(label % 9)
        return compose(macro, [child(tuple(group)) for group in by_block])

    expected = {
        1: (-10768745, -1300427),
        2: (-18727142, -1608620),
        3: (-24342189, -1728073),
    }
    ranges = {}
    for order in (1, 2, 3):
        gaps = []
        for deleted in combinations(range(81), order):
            base = deletion_stats(deleted)
            loss = full[3] - base[3]
            if order == 1:
                bound = 1 + min(base[1], base[2])
            elif order == 2:
                bound = min(
                    3 + 3 * base[1],
                    3 + 3 * base[2],
                    3 + base[1] + base[2] + base[0],
                )
            else:
                bound = min(
                    7 + 6 * base[1],
                    7 + 6 * base[2],
                    7 + 3 * base[1] + base[2] + 3 * base[0],
                    7 + base[1] + 3 * base[2] + 3 * base[0],
                )
            gaps.append(bound - loss)
        ranges[order] = (min(gaps), max(gaps))
        assert ranges[order] == expected[order]
        assert max(gaps) < 0
    return seed, full, ranges


def convolution(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def add_polynomials(left, right):
    result = [0] * max(len(left), len(right))
    for i, value in enumerate(left):
        result[i] += value
    for i, value in enumerate(right):
        result[i] += value
    return result


def scaled_profile(profile, size, shift):
    result = [0] * (len(profile) - shift)
    for rank in range(shift, len(profile)):
        result[rank - shift] = profile[rank] * size ** (rank - shift)
    return result


def scalar_and_rank_audit():
    face_masks, cap_masks, cup_masks = mask_families(sorted(nine_points()))
    cap_profile = rank_profile(cap_masks)
    cup_profile = rank_profile(cup_masks)
    face_profile = rank_profile(face_masks)
    assert cap_profile == {1: 9, 2: 36, 3: 52, 4: 17, 5: 1}
    assert cup_profile == {1: 9, 2: 36, 3: 32, 4: 12, 5: 1}
    assert face_profile == {1: 9, 2: 36, 3: 84, 4: 36, 5: 3}

    cap_seed = [cap_profile.get(i, 0) for i in range(6)]
    cup_seed = [cup_profile.get(i, 0) for i in range(6)]
    face_seed = [face_profile.get(i, 0) for i in range(6)]
    cap_poly = cup_poly = face_poly = [0, 1]
    size = 1
    totals = []
    means = []
    for depth in range(1, 11):
        old_cap, old_cup, old_face = cap_poly, cup_poly, face_poly
        cap_poly = convolution(
            old_cap, scaled_profile(cap_seed, size, 1)
        )
        cup_poly = convolution(
            old_cup, scaled_profile(cup_seed, size, 1)
        )
        cross = convolution(
            convolution(old_cap, old_cup),
            scaled_profile(face_seed, size, 2),
        )
        face_poly = add_polynomials(
            [9 * coefficient for coefficient in old_face], cross
        )
        size *= 9
        totals.append((size, sum(cap_poly), sum(cup_poly), sum(face_poly)))
        mean = Fraction(
            sum(rank * count for rank, count in enumerate(face_poly)),
            sum(face_poly),
        )
        means.append(mean)
        assert max(i for i, value in enumerate(cap_poly) if value) == 4 * depth + 1
        assert max(i for i, value in enumerate(cup_poly) if value) == 4 * depth + 1
        assert max(i for i, value in enumerate(face_poly) if value) == 8 * depth - 3

    assert totals[0] == (9, 115, 90, 168)
    assert totals[1] == (81, 2702385, 1641060, 61014762)
    assert totals[2][3] == 8148275465027020758
    # Exact rational mean at d=2, and a simple linear rank ceiling at all d.
    assert means[1] == Fraction(456489828, 61014762)
    return cap_profile, cup_profile, face_profile, totals, means


def cage_load_audit(totals):
    # The seed cage itself, including its exact Farkas certificate, is checked
    # by the earlier independent verifier.
    assert three_ear_check() == (3, 3, 3)
    rows = []
    for depth, (_, _, _, face_total) in enumerate(totals, start=1):
        contexts = sum(
            9 ** level * 3 * (9 ** (depth - level - 1)) ** 4
            for level in range(depth)
        )
        cage_triples = sum(
            9 ** level * (9 ** (depth - level - 1)) ** 10
            for level in range(depth)
        )
        rows.append((depth, contexts, cage_triples, face_total))
    assert rows[0] == (1, 3, 1, 168)
    assert rows[1][:3] == (2, 19710, 3486784410)
    # Quadratic face entropy eventually dominates both polynomial literal
    # cage alphabets.  Depth four is already beyond the crossover.
    assert all(face_total > contexts and face_total > triples
               for depth, contexts, triples, face_total in rows
               if depth >= 4)
    return rows


def natural_three_map_ifs_audit():
    points = sorted(nine_points())
    groups = ((0, 1, 5), (2, 3, 4), (6, 7, 8))
    clusters = [[points[i] for i in group] for group in groups]
    macro = [ifs.centroid(cluster) for cluster in clusters]
    certificate = json.loads(
        (ERDOS / "agent_lex_minimizer_search"
         / "triangular_ifs_certificate.json").read_text()
    )
    permutations = tuple(tuple(row)
                         for row in certificate["best_permutations"])
    maps, _ = ifs.make_maps(macro, clusters, permutations, Fraction(1))
    depth_two = ifs.expand(macro, maps)
    depth_three = sorted(ifs.expand(depth_two, maps))
    cap_total, cup_total, face_total, _ = rt.evaluate(depth_three)
    assert (len(depth_three), face_total) == (27, 22862)
    gaps = []
    for deleted in range(27):
        base = depth_three[:deleted] + depth_three[deleted + 1:]
        cap_base, cup_base, face_base, _ = rt.evaluate(base)
        gaps.append(1 + min(cap_base, cup_base) - (face_total - face_base))
    assert (min(gaps), max(gaps), sum(gap < 0 for gap in gaps)) == (-431, 910, 8)
    return cap_total, cup_total, face_total, min(gaps), max(gaps)


def main():
    chambers = chamber_and_rechart_audit()
    seed, full, deletion_ranges = fixed_chart_deletion_audit()
    profiles = scalar_and_rank_audit()
    cage_rows = cage_load_audit(profiles[3])
    ifs_row = natural_three_map_ifs_audit()
    print(
        "PASS: chambers/recharts=%s; seed/full=%s/%s; deletion gaps=%s; "
        "profiles=%s/%s/%s; d10 mean=%.9f; cage d10 logs compared; "
        "IFS27=%s"
        % (
            chambers,
            seed,
            full,
            deletion_ranges,
            profiles[0], profiles[1], profiles[2],
            float(profiles[4][-1]),
            ifs_row,
        )
    )


if __name__ == "__main__":
    main()
