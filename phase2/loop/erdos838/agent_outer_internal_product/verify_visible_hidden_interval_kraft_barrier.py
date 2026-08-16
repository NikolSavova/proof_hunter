#!/usr/bin/env python3
"""Exact audit for VISIBLE_HIDDEN_INTERVAL_KRAFT_BARRIER.md."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
import json
from math import comb
from pathlib import Path
import sys


Point = tuple[Q, Q]
HERE = Path(__file__).resolve().parent


def cross(a: Point, b: Point, c: Point) -> Q:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def strict_hull(points: tuple[Point, ...] | list[Point]) -> tuple[Point, ...]:
    ordered = sorted(set(points))
    if len(ordered) <= 2:
        return tuple(ordered)
    lower: list[Point] = []
    upper: list[Point] = []
    for point in ordered:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    for point in reversed(ordered):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return tuple(lower[:-1] + upper[:-1])


def convex(points: tuple[Point, ...] | list[Point]) -> bool:
    return len(strict_hull(points)) == len(set(points))


def circle(t: Q) -> Point:
    return (Q(1 - t * t, 1 + t * t), Q(2 * t, 1 + t * t))


def first_bad_four(indices: tuple[int, ...], points: tuple[Point, ...]) -> tuple[int, ...]:
    for candidate in combinations(indices, 4):
        if not convex(tuple(points[i] for i in candidate)):
            return candidate
    raise AssertionError("bad union has no four-circuit")


def conic_rectangle_audit() -> dict[str, object]:
    a = (Q(-1), Q(0))
    b = (Q(1), Q(0))
    forced_parameters = (-20, -15, -12, -10, -8)
    optional_hidden_parameters = (-7, -6, -5, -4, -3, -2)
    visible_parameters = (Q(1, 5), Q(1, 4), Q(1, 3), Q(1, 2), Q(2, 3), Q(3, 4))
    forced_y = tuple(circle(Q(t)) for t in forced_parameters)
    optional_y = tuple(circle(Q(t)) for t in optional_hidden_parameters)
    visible_x = tuple(circle(t) for t in visible_parameters)

    epsilon = Q(1, 1_000_000)
    left = tuple(
        (Q(-2) - i * epsilon,
         Q(-100) - i * i * epsilon**2 - i * epsilon**3)
        for i in range(1, 4)
    )
    right = tuple(
        (Q(2) + i * epsilon,
         Q(7) + 2 * i * i * epsilon**2 + 3 * i * epsilon**3)
        for i in range(1, 4)
    )
    conic = (a, *forced_y, *optional_y, b, *visible_x)
    assert convex(conic)

    points = tuple(sorted((*left, *conic, *right)))
    assert all(cross(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))
    index = {point: i for i, point in enumerate(points)}
    a_id, b_id = index[a], index[b]
    forced_ids = tuple(index[p] for p in forced_y)
    optional_y_ids = tuple(index[p] for p in optional_y)
    x_ids = tuple(index[p] for p in visible_x)
    left_ids = tuple(index[p] for p in left)
    right_ids = tuple(index[p] for p in right)
    fixed_trace = (a_id, forced_ids[0], forced_ids[1])

    all_lower_ids = (*forced_ids, *optional_y_ids)
    for ell in left_ids:
        assert all(
            not convex(tuple(points[i] for i in (ell, *triple)))
            for triple in combinations(all_lower_ids, 3)
        )

    visible_layers = tuple(combinations(x_ids, 2))
    hidden_layers = tuple(combinations(optional_y_ids, 2))
    records = []
    visible_outputs = Counter()
    hidden_outputs = Counter()
    interval_outputs = Counter()
    edge_outputs = Counter()

    for ell in left_ids:
        for r in right_ids:
            edge = (ell, r)
            for x_choice in visible_layers:
                for y_choice in hidden_layers:
                    w = tuple(sorted((a_id, b_id, *forced_ids, *x_choice, *y_choice)))
                    w_points = tuple(points[i] for i in w)
                    assert convex(w_points)
                    full = tuple(sorted((ell, *w, r)))
                    assert not convex(tuple(points[i] for i in full))
                    circuit = first_bad_four(full, points)
                    internal = tuple(i for i in circuit if i in w)
                    external = tuple(i for i in circuit if i in edge)
                    assert internal == fixed_trace
                    assert external == (ell,)

                    visible = tuple(sorted((ell, a_id, b_id, *x_choice)))
                    hidden = tuple(sorted((*forced_ids, *y_choice)))
                    assert set(strict_hull(tuple(points[i] for i in (ell, *w)))) == {
                        points[i] for i in visible
                    }
                    assert convex(tuple(points[i] for i in visible))
                    assert convex(tuple(points[i] for i in hidden))
                    assert set(w) == (set(visible) - {ell}) | set(hidden)

                    # Three forced hidden labels survive deletion of A, so
                    # the preceding complement repair genuinely fails.
                    complement = tuple(i for i in w if i not in fixed_trace)
                    assert not convex(tuple(points[i] for i in (ell, *complement)))

                    records.append((ell, r, x_choice, y_choice))
                    visible_outputs[visible] += 1
                    hidden_outputs[hidden] += 1
                    interval_outputs[w] += 1
                    edge_outputs[edge] += 1

    ax = len(visible_layers)
    ay = len(hidden_layers)
    l_size = len(left_ids)
    r_size = len(right_ids)
    record_count = l_size * r_size * ax * ay
    assert len(records) == record_count

    expected = {
        "visible": (l_size * ax, ay * r_size),
        "hidden": (ay, ax * l_size * r_size),
        "interval": (ax * ay, l_size * r_size),
        "edge": (l_size * r_size, ax * ay),
    }
    banks = {
        "visible": visible_outputs,
        "hidden": hidden_outputs,
        "interval": interval_outputs,
        "edge": edge_outputs,
    }
    for name, counter in banks.items():
        size, load = expected[name]
        assert len(counter) == size
        assert set(counter.values()) == {load}
        assert size * load == record_count

    tagged_capacity = sum(size for size, _ in expected.values())
    fractional_lower_bound = Q(record_count, tagged_capacity)
    assert fractional_lower_bound == Q(675, 98)

    # Actual literal Hall capacities.  At depth zero every record has
    # demand pi(W)/4.  Output capacities are pi(output), so the common
    # factor 1/F cancels from the following exact lower bound.
    interval_rank = next(iter({len(w) for w in interval_outputs}))
    visible_rank = next(iter({len(w) for w in visible_outputs}))
    hidden_rank = next(iter({len(w) for w in hidden_outputs}))
    edge_rank = next(iter({len(w) for w in edge_outputs}))
    total_demand_without_F = Q(record_count, 4 * 2**interval_rank)
    tagged_capacity_without_F = (
        Q(len(visible_outputs), 2**visible_rank)
        + Q(len(hidden_outputs), 2**hidden_rank)
        + Q(len(interval_outputs), 2**interval_rank)
        + Q(len(edge_outputs), 2**edge_rank)
    )
    literal_normalized_lower_bound = total_demand_without_F / tagged_capacity_without_F
    assert literal_normalized_lower_bound == Q(675, 10604)

    # Capacity upper bound for every subset-valued output O contained in
    # its record, not only the four projections.  If O contains ell, the
    # preceding four-set audit shows that it contains at most two lower
    # labels.  We deliberately overcount the other coordinates by full
    # Boolean cubes.
    s = 2
    lower_count = 3 * s + 5
    lower_at_most_two_weight = sum(Q(comb(lower_count, i), 2**i) for i in range(3))
    all_subface_capacity_upper_without_F = (1 + Q(r_size, 2)) * (
        Q(3, 2) ** (6 * s + 7)
        + Q(l_size, 2) * Q(9, 4) * Q(3, 2) ** (3 * s) * lower_at_most_two_weight
    )
    all_subface_normalized_lower_bound = (
        total_demand_without_F / all_subface_capacity_upper_without_F
    )
    assert all_subface_normalized_lower_bound == Q(128, 3_877_551)

    # Depth zero has q_(0,e)=p_e identically, so h_(0,e)=1.  All W have
    # the same rank, hence rescaling their literal pi(W)/4 record weights
    # makes the rectangle exactly uniform.
    interval_ranks = {len(w) for w in interval_outputs}
    assert interval_ranks == {interval_rank}

    return {
        "points": len(points),
        "fixed_trace": list(fixed_trace),
        "left_endpoints": l_size,
        "right_endpoints": r_size,
        "visible_layer_size": ax,
        "hidden_layer_size": ay,
        "interval_rank": next(iter(interval_ranks)),
        "literal_depth_zero_tilt": "1",
        "records": record_count,
        "projection_sizes_and_loads": {
            name: {"outputs": size, "load": load}
            for name, (size, load) in expected.items()
        },
        "unit_record_fractional_projection_load_lower_bound": str(fractional_lower_bound),
        "literal_fractional_normalized_load_lower_bound": str(literal_normalized_lower_bound),
        "all_record_subfaces_fractional_normalized_load_lower_bound": str(
            all_subface_normalized_lower_bound
        ),
        "all_left_plus_three_lower_arc_sets_are_bad": True,
        "output_ranks": {
            "visible": visible_rank,
            "hidden": hidden_rank,
            "interval": interval_rank,
            "edge": edge_rank,
        },
        "all_complement_reattachments_fail": True,
    }


def singleton_universality_stress() -> dict[str, object]:
    universality_dir = HERE.parent / "agent_one_sided_reflection"
    sys.path.insert(0, str(universality_dir))
    try:
        import verify_singleton_reset_universality as universality

        source = universality.random_points(7, 838_151)
        result = universality.audit_source(source, "interval_hidden_child_random_n7")
    finally:
        sys.path.pop(0)
    assert result["n"] == 7
    assert result["rooted_coefficients"] == [1, 7, 0, 0, 0, 0, 0, 0]
    return result


def parabola_visible_path_stress() -> dict[str, object]:
    """Exact finite instance of the successive-visible-pair regression."""
    m = 12
    cloud = tuple((Q(i), Q(i * i)) for i in range(m))
    ell = (Q(-1), Q(-100 * m * m))
    assert convex(cloud)
    triples = tuple(combinations(cloud, 3))
    assert all(not convex((ell, *triple)) for triple in triples)

    max_retained = 0
    visible_profiles: set[tuple[Point, ...]] = set()
    for mask in range(1 << m):
        selected = tuple(cloud[i] for i in range(m) if mask & (1 << i))
        hull = strict_hull((ell, *selected))
        retained = tuple(point for point in hull if point != ell)
        assert len(retained) <= 2
        max_retained = max(max_retained, len(retained))
        visible_profiles.add(retained)
    return {
        "m": m,
        "three_point_traces_checked": len(triples),
        "subsets_checked": 1 << m,
        "maximum_parabola_labels_in_one_ell_retaining_face": max_retained,
        "visible_profiles": len(visible_profiles),
    }


def asymptotic_capacity_audit() -> dict[str, object]:
    """Evaluate the exact formula (20) on the scalable parameter family."""
    samples: dict[str, object] = {}
    for s in (2, 4, 8, 12, 16, 20):
        a_size = comb(3 * s, s)
        l_size = r_size = 2**s
        demand = Q(l_size * r_size * a_size**2, 2 ** (2 * s + 9))
        capacity = (
            Q(l_size * a_size, 2 ** (s + 3))
            + Q(a_size, 2 ** (s + 5))
            + Q(a_size**2, 2 ** (2 * s + 7))
            + Q(l_size * r_size, 4)
        )
        lower_bound = demand / capacity
        ratio_to_four_power = lower_bound / 4**s
        if s >= 8:
            assert ratio_to_four_power > Q(1, 16)
        samples[str(s)] = {
            "A": a_size,
            "normalized_load_lower_bound_decimal": f"{float(lower_bound):.12g}",
            "ratio_to_4_power_s_decimal": f"{float(ratio_to_four_power):.12g}",
        }

        lower_count = 3 * s + 5
        lower_at_most_two_weight = sum(
            Q(comb(lower_count, i), 2**i) for i in range(3)
        )
        all_subface_capacity_upper = (1 + Q(r_size, 2)) * (
            Q(3, 2) ** (6 * s + 7)
            + Q(l_size, 2)
            * Q(9, 4)
            * Q(3, 2) ** (3 * s)
            * lower_at_most_two_weight
        )
        all_subface_lower_bound = demand / all_subface_capacity_upper
        all_subface_scale = all_subface_lower_bound / Q(2**s, s)
        if s >= 20:
            assert all_subface_scale > Q(1, 20_000)
        samples[str(s)]["all_subface_load_lower_bound_decimal"] = (
            f"{float(all_subface_lower_bound):.12g}"
        )
        samples[str(s)]["all_subface_ratio_to_2_power_s_over_s_decimal"] = (
            f"{float(all_subface_scale):.12g}"
        )
    return {
        "parameters": "|X|=|Y|=3s, layer ranks s, |L|=|R|=2^s",
        "samples": samples,
        "verified_lower_bound_for_sampled_s_at_least_8": "T > 4^s/16",
        "verified_all_subface_bound_for_sampled_s_at_least_20": "T > 2^s/(20000s)",
        "external_alphabet_capacity_multiplier": "(3/2)^c for c fixed repair labels",
    }


def main() -> None:
    certificate = {
        "description": "literal visible-hidden interval rectangle and singleton-universal child barrier",
        "conic_rectangle": conic_rectangle_audit(),
        "asymptotic_capacity_formula": asymptotic_capacity_audit(),
        "parabola_visible_path_stress": parabola_visible_path_stress(),
        "singleton_universality_stress": singleton_universality_stress(),
        "claims": [
            "visible and hidden choices form a full realizable Cartesian rectangle",
            "every record has one fixed canonical left-role 1+3 trace",
            "all complement reattachments remain nonconvex",
            "visible, hidden, interval, and endpoint projection sizes and loads are exact",
            "the uniform rectangle is the actual literal depth-zero activity weighting on a constant-rank target layer",
            "fractional routing among all four projections has exact unit and literal half-Gibbs congestion lower bounds",
            "every subset-valued one-face decoder has a fixed-power literal half-Gibbs congestion lower bound",
            "a c-label external repair alphabet and J tags can improve congestion by at most J(3/2)^c",
            "a singleton full-pocket reset transfers an arbitrary child face complex exactly",
        ],
    }
    output = Path(__file__).with_name("visible_hidden_interval_kraft_barrier_certificate.json")
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
