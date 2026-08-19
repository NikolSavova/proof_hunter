#!/usr/bin/env python3
"""Explore the nine cross-pair D^2 charges for Erdős 1208.

For a fixed rich fibre, each q-dependent D-form and each p-dependent D-form
recover their respective shifts.  Their ordered pair is therefore a
fibre-injective charge.  This script measures the minimum global degree over
the nine resulting projections.  It is an exact diagnostic, not a proof of
the missing adaptive load estimate.
"""

from __future__ import annotations

from collections import Counter

from analyze_affine_costas_energy import welch
from verify_determinant_prime_costas_resonance import ROWS, apply
from verify_orthogonal_two_support_gate import difference_set
from verify_seven_incidence_opposite_endpoint_charge import (
    POINTS,
    add,
    linear,
    rich_fibres,
    subtract,
)


Point = tuple[int, int]
Cell = tuple[int, int, Point, Point]
Charge = tuple[int, int, Point, Point]


def iter_records(differences: set[Point]):
    fibres, _, _ = rich_fibres(differences, adaptive=True)
    for fibre_label, fibre in fibres.items():
        base, ordinary_sum = fibre_label
        w_value = subtract(ordinary_sum, base)
        for q_value in fibre:
            q_forms = (
                add(base, q_value),
                subtract(w_value, q_value),
                subtract(w_value, linear(q_value)),
            )
            for p_value in fibre:
                if q_value == p_value:
                    continue
                p_forms = (
                    add(base, p_value),
                    subtract(w_value, p_value),
                    subtract(w_value, linear(p_value)),
                )
                yield fibre_label, q_forms, p_forms


def profile_differences(
    differences: set[Point],
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    _, support, _ = rich_fibres(differences, adaptive=True)
    degrees: Counter[Cell] = Counter()
    local_keys: dict[
        tuple[Point, Point], list[set[tuple[Point, Point]]]
    ] = {}
    mass = 0

    for fibre_label, q_forms, p_forms in iter_records(differences):
        route_sets = local_keys.setdefault(
            fibre_label, [set() for _ in range(9)]
        )
        for q_role, q_form in enumerate(q_forms):
            for p_role, p_form in enumerate(p_forms):
                route = 3 * q_role + p_role
                key = q_form, p_form
                assert key not in route_sets[route]
                route_sets[route].add(key)
                degrees[(q_role, p_role, q_form, p_form)] += 1
        mass += 1

    loads: Counter[Charge] = Counter()
    degree_envelope = 0
    max_min_degree = 0
    for _, q_forms, p_forms in iter_records(differences):
        candidates: list[tuple[int, int, int, Point, Point]] = []
        for q_role, q_form in enumerate(q_forms):
            for p_role, p_form in enumerate(p_forms):
                degree = degrees[(q_role, p_role, q_form, p_form)]
                candidates.append(
                    (degree, q_role, p_role, q_form, p_form)
                )
        degree, q_role, p_role, q_form, p_form = min(candidates)
        degree_envelope += degree
        max_min_degree = max(max_min_degree, degree)
        loads[(q_role, p_role, q_form, p_form)] += 1

    charge_second = sum(value * value for value in loads.values())
    assert charge_second <= degree_envelope
    n_value = len(differences)
    s_value = support
    route_moments = tuple(
        sum(
            multiplicity * multiplicity
            for (q_role, p_role, _, _), multiplicity in degrees.items()
            if 3 * q_role + p_role == route
        )
        for route in range(9)
    )
    route_maxima = tuple(
        max(
            (
                multiplicity
                for (q_role, p_role, _, _), multiplicity in degrees.items()
                if 3 * q_role + p_role == route
            ),
            default=0,
        )
        for route in range(9)
    )
    return (
        n_value,
        s_value,
        mass,
        len(loads),
        charge_second,
        max(loads.values(), default=0),
        degree_envelope,
        max_min_degree,
        max(degrees.values(), default=0),
    ), route_moments, route_maxima


def profile(
    points: list[Point],
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    return profile_differences(difference_set(points))


def main() -> None:
    families: list[tuple[str, list[Point]]] = [
        ("closure-30", POINTS[:30]),
        ("closure-40", POINTS[:40]),
    ]
    for prime in (11, 17, 23, 31):
        matrix, _ = ROWS[prime]
        families.append(
            (f"Costas-{prime}", [apply(matrix, point) for point in welch(prime)])
        )
    for name, points in families:
        values, route_moments, route_maxima = profile(points)
        adaptive_k = values[1] / values[0]
        print(
            name,
            values,
            "K",
            adaptive_k,
            "charge-load",
            values[4] / values[2] if values[2] else 0.0,
            "degree-load/K",
            values[6] / values[2] / adaptive_k
            if values[2] and adaptive_k
            else 0.0,
            "route-moments/K",
            tuple(
                round(moment / values[2] / adaptive_k, 6)
                if values[2] and adaptive_k
                else 0.0
                for moment in route_moments
            ),
            "route-max",
            route_maxima,
        )

    from verify_radial_orthogonal_product_barrier import radial_set

    for side in (8, 12):
        values, route_moments, route_maxima = profile_differences(
            radial_set(side)
        )
        adaptive_k = values[1] / values[0]
        print(
            f"radial-{side}",
            values,
            "K",
            adaptive_k,
            "charge-load",
            values[4] / values[2] if values[2] else 0.0,
            "degree-load/K",
            values[6] / values[2] / adaptive_k
            if values[2] and adaptive_k
            else 0.0,
            "route-moments/K",
            tuple(
                round(moment / values[2] / adaptive_k, 6)
                if values[2] and adaptive_k
                else 0.0
                for moment in route_moments
            ),
            "route-max",
            route_maxima,
        )


if __name__ == "__main__":
    main()
