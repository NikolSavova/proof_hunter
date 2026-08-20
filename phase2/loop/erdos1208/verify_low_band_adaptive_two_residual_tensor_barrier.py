#!/usr/bin/env python3
"""Exact certificate for the adaptive two-residual tensor barrier.

The example joins the planted isolated scalar pencil to a transformed
finite-field parabola.  The latter supplies enough clean-fibre mass to make
the adaptive quota non-vacuous, while the former retains one decorated tail
occurrence.  For that occurrence the affine residual is constant and the
Gaussian residual runs injectively through all target signed-area cells.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from random import Random

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_low_band_isolated_translation_excess_gate import (
    PAIR_RECORDS,
    RANDOM_SEED,
    VERTICAL_MARKS,
    add,
    distance2,
    planted_candidate,
    subtract,
)
from verify_metric_scalar_endpoint_rich_tail import determinant, edge_data
from verify_metric_scalar_universal_matrix_and_ruler_stress import (
    finite_field_parabola,
    lex_transform,
)
from verify_single_fibre_replacement_transition_barrier import pair_tables


Point = tuple[int, int]
FILLER_PRIME = 31
TRANSLATION_BASE = 10**14
TARGET_GAP = -100


def dot(first: Point, second: Point) -> int:
    return first[0] * second[0] + first[1] * second[1]


def norm2(point: Point) -> int:
    return dot(point, point)


def edge_lookup(points: list[Point]) -> dict[tuple[int, int], tuple[int, Point]]:
    return {
        endpoints: (label, vector)
        for label, endpoints, vector in edge_data(points)
    }


def build_union() -> tuple[
    list[Point],
    tuple,
    int,
    int,
    list[Point],
    int,
    Point,
]:
    """Return a deterministic distance/pair-sum Sidon specialization."""
    random = Random(RANDOM_SEED)
    planted = None
    plant_attempt = 0
    for plant_attempt in range(1, 101):
        candidate = planted_candidate(random, FILLER_PRIME)
        plant_points = candidate[0]
        if len(plant_points) != len(set(plant_points)):
            continue
        try:
            _, plant_distances = pair_tables(plant_points)
        except ValueError:
            continue
        planted = candidate
        break
    assert planted is not None

    plant_points = planted[0]
    filler_base = [
        lex_transform(FILLER_PRIME, point)
        for point in finite_field_parabola(FILLER_PRIME)
    ]
    # Separate the two internal distance spectra before translation.  This
    # is also the finite certificate's specialization of the generic scale.
    plant_labels = set(plant_distances)
    scale = next(
        candidate
        for candidate in range(1, 1_000)
        if plant_labels.isdisjoint({
            candidate * candidate * distance2(first, second)
            for first, second in combinations(filler_base, 2)
        })
    )
    scaled_filler = [(scale * x, scale * y) for x, y in filler_base]

    for offset in range(100):
        parameter = TRANSLATION_BASE + offset
        translation = (parameter, parameter * parameter)
        filler = [add(point, translation) for point in scaled_filler]
        points = plant_points + filler
        if len(points) != len(set(points)):
            continue
        try:
            pair_tables(points)
        except ValueError:
            continue
        return (
            points,
            planted,
            plant_attempt,
            scale,
            filler_base,
            offset,
            translation,
        )
    raise AssertionError("union finite-avoidance specialization exhausted")


def profile() -> tuple[int, ...]:
    (
        points,
        planted,
        plant_attempt,
        scale,
        filler_base,
        translation_offset,
        filler_translation,
    ) = build_union()
    (
        _,
        first_anchor,
        source_pairs,
        target_pairs,
        horizontal_count,
    ) = planted
    k = len(points)
    pair_sums, distances = pair_tables(points)
    edge_count = len(distances)
    assert edge_count == k * (k - 1) // 2

    fibres = clean_start_fibres(points)
    filler_fibres = clean_start_fibres(filler_base)
    filler_qs = {
        (scale * q[0], scale * q[1])
        for q in filler_fibres
    }
    # Every internal clean row remains clean in the union.  Extra cross-arm
    # rows are allowed and are counted in the actual adaptive denominator.
    for q, starts in filler_fibres.items():
        transported_q = (scale * q[0], scale * q[1])
        transported_starts = {
            (
                2 * filler_translation[0] + scale * start[0],
                2 * filler_translation[1] + scale * start[1],
            )
            for start in starts
        }
        assert transported_starts <= set(fibres[transported_q])

    anchor = (first_anchor, first_anchor + 1)
    q = subtract(points[anchor[0]], points[anchor[1]])
    assert q not in filler_qs
    q_collection = filler_qs | {q}
    fibre_mass = sum(len(fibres[translation]) for translation in q_collection)

    pair_sum_edges = {total: tuple(edge) for total, edge in pair_sums.items()}
    source_starts: list[tuple[Point, Point]] = []
    for source_pair, target_pair in zip(source_pairs, target_pairs):
        starts = tuple(
            add(points[edge[0]], points[edge[1]]) for edge in source_pair
        )
        source_starts.append(starts)
        common_translations = {
            translation
            for translation, fibre in fibres.items()
            if starts[0] in fibre and starts[1] in fibre
        }
        assert common_translations == {q}
        for start, target in zip(starts, target_pair):
            assert set(pair_sum_edges[add(start, q)]) == set(target)
            assert len({*anchor, *pair_sum_edges[start], *target}) == 6
        assert set(target_pair[0]).isdisjoint(target_pair[1])
    assert len(fibres[q]) == 2 * PAIR_RECORDS

    edges = edge_data(points)
    lookup = edge_lookup(points)
    target_records: list[tuple[tuple[int, int], tuple[int, int], int]] = []
    for _, first_endpoints, first_vector in edges:
        first_label = lookup[first_endpoints][0]
        for _, second_endpoints, second_vector in edges:
            second_label = lookup[second_endpoints][0]
            signed_area = 2 * determinant(first_vector, second_vector)
            if (
                first_label - second_label == TARGET_GAP
                and abs(signed_area) > edge_count
            ):
                target_records.append(
                    (first_endpoints, second_endpoints, signed_area)
                )
    target_load = len(target_records)

    # The physical wedge used by the planted selector survives the union at
    # the final determinant cutoff.
    origin = horizontal_count + VERTICAL_MARKS.index(0)
    vertical_ten = horizontal_count + VERTICAL_MARKS.index(10)
    fixed_edges = (
        tuple(sorted((origin, 0))),
        tuple(sorted((origin, 1))),
    )
    partner_edges = (
        tuple(sorted((vertical_ten, 0))),
        tuple(sorted((vertical_ten, 1))),
    )
    fixed_gap = lookup[fixed_edges[0]][0] - lookup[fixed_edges[1]][0]
    partner_gap = lookup[partner_edges[0]][0] - lookup[partner_edges[1]][0]
    assert fixed_gap == partner_gap
    for fixed, partner in zip(fixed_edges, partner_edges):
        assert lookup[fixed][0] - lookup[partner][0] == TARGET_GAP
        assert abs(2 * determinant(lookup[fixed][1], lookup[partner][1])) > edge_count

    # All three selected occurrences have the same target load.  The actual
    # size-biased quota is two, so one occurrence remains in the adaptive
    # tail even after removing the largest loads.
    selected_occurrences = len(source_pairs)
    adaptive_quota = (
        k * k * len(fibres[q]) + fibre_mass - 1
    ) // fibre_mass
    adaptive_tail = max(0, selected_occurrences - adaptive_quota)
    adaptive_lift = adaptive_tail * target_load
    assert adaptive_tail == 1

    # Audit both residuals on the retained occurrence.  The affine residual
    # is independent of the external target completion.  The imaginary
    # Gaussian residual is an injective affine function of its signed area.
    source_first, source_second = source_pairs[-1]
    target_first, target_second = target_pairs[-1]
    source_first_label, source_first_vector = lookup[source_first]
    source_second_label, source_second_vector = lookup[source_second]
    source_gap = source_first_label - source_second_label
    source_area = 2 * determinant(source_first_vector, source_second_vector)
    assert source_gap == -18 * TARGET_GAP

    sigma_first, sigma_second = source_starts[-1]
    clean_target_gap = lookup[target_first][0] - lookup[target_second][0]
    affine_residual = (
        clean_target_gap
        - source_gap
        + 2 * dot(q, subtract(sigma_first, sigma_second))
    )
    radii = [norm2(point) for point in points]
    row_on_radii = (
        sum(radii[index] for index in target_first)
        - sum(radii[index] for index in source_first)
        - sum(radii[index] for index in target_second)
        + sum(radii[index] for index in source_second)
    )
    assert affine_residual == 2 * row_on_radii

    area_cells = Counter(area for _, _, area in target_records)
    joint_cells: Counter[tuple[int, int]] = Counter()
    for _, _, target_area in target_records:
        # Real parts of Z_s+18Z_v cancel; the displayed integer is minus its
        # imaginary part.  The affine coordinate stays fixed.
        assert source_gap + 18 * TARGET_GAP == 0
        gaussian_residual = source_area + 18 * target_area
        joint_cells[affine_residual, gaussian_residual] += 1
    assert sorted(area_cells.values()) == sorted(joint_cells.values())

    return (
        plant_attempt,
        scale,
        translation_offset,
        k,
        edge_count,
        sum(len(fibre) for fibre in fibres.values()),
        len(q_collection),
        fibre_mass,
        len(fibres[q]),
        selected_occurrences,
        adaptive_quota,
        adaptive_tail,
        target_load,
        len(area_cells),
        max(area_cells.values()),
        source_area,
        affine_residual,
        len(joint_cells),
        max(joint_cells.values()),
        adaptive_lift,
        max(max(abs(x), abs(y)) for x, y in points),
    )


def main() -> None:
    actual = profile()
    expected = (
        1,
        67,
        0,
        126,
        7_875,
        1_073_106,
        931,
        58_116,
        6,
        3,
        2,
        1,
        126,
        126,
        1,
        -1_674,
        11_289_994_816_436_323_502_108_368,
        126,
        1,
        126,
        10_000_000_000_000_000_000_192_483_228,
    )
    assert actual == expected, (actual, expected)
    print("adaptive two-residual tensor profile", actual)
    print("adaptive two-residual tensor barrier: PASS")


if __name__ == "__main__":
    main()
