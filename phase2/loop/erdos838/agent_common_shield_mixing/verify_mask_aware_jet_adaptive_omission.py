#!/usr/bin/env python3
"""Audit for MASK_AWARE_JET_ADAPTIVE_OMISSION.md."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product


Point = tuple[Q, Q]


def pt(x: int, y: int, denominator: int = 1) -> Point:
    return (Q(x, denominator), Q(y, denominator))


def cross(o: Point, a: Point, b: Point) -> Q:
    return (a[0] - o[0]) * (b[1] - o[1]) - (
        a[1] - o[1]
    ) * (b[0] - o[0])


def hull(points: tuple[Point, ...]) -> tuple[Point, ...]:
    ordered = sorted(set(points))
    if len(ordered) <= 1:
        return tuple(ordered)
    lower: list[Point] = []
    for candidate in ordered:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], candidate) <= 0:
            lower.pop()
        lower.append(candidate)
    upper: list[Point] = []
    for candidate in reversed(ordered):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], candidate) <= 0:
            upper.pop()
        upper.append(candidate)
    return tuple(lower[:-1] + upper[:-1])


def is_convex(points: tuple[Point, ...]) -> bool:
    return len(points) == len(set(points)) == len(hull(points))


def jet_pigeonhole_audit() -> dict[str, object]:
    rows = []
    for size in (4, 6, 8, 10):
        jet_counts: Counter[tuple[int, int, int, int]] = Counter()
        for mask in range(1, 1 << size):
            face = [i for i in range(size) if mask & (1 << i)]
            if len(face) == 1:
                jet = (face[0], -1, -1, face[0])
            else:
                # For ranks two and three the first/last pairs overlap,
                # exactly as the actual boundary jet does.
                jet = (face[0], face[1], face[-2], face[-1])
            jet_counts[jet] += 1
        faces = (1 << size) - 1
        classes = len(jet_counts)
        richest = max(jet_counts.values())
        assert classes <= (size + 1) ** 4
        assert richest * (size + 1) ** 4 >= faces
        rows.append(
            {
                "support": size,
                "faces": faces,
                "jet_classes": classes,
                "richest_class": richest,
                "L_plus_1_fourth": (size + 1) ** 4,
            }
        )
    return {"scales": rows}


def compatible(left: int, right: int, seam: int) -> bool:
    # Alternating exact Ferrers thresholds.
    return left <= right if seam % 2 == 0 else left >= right


def adaptive_omission_audit() -> dict[str, object]:
    alphabet = 4
    rank = 5
    words = [
        word
        for word in product(range(alphabet), repeat=rank)
        if all(
            compatible(word[i], word[(i + 1) % rank], i)
            for i in range(rank)
        )
    ]
    assert words
    gap = 2
    partials = sorted({word[:gap] + word[gap + 1 :] for word in words})
    projection_size = len({word[gap] for word in words})
    assert len(partials) * projection_size >= len(words)

    # Profiles are represented by their fixed seam-anchor integer.  They
    # need not be compatible with either neighboring selected value.
    profiles = tuple(range(7))
    output_load: Counter[tuple[int | None, ...]] = Counter()
    for partial in partials:
        restored = list(partial[:gap]) + [None] + list(partial[gap:])
        for profile in profiles:
            delete_left = not compatible(restored[gap - 1], profile, gap - 1)
            delete_right = not compatible(profile, restored[(gap + 1) % rank], gap)
            output = list(restored)
            output[gap] = 100 + profile
            if delete_left:
                output[gap - 1] = None
            if delete_right:
                output[(gap + 1) % rank] = None

            # Every retained adjacent ear pair is compatible.  Missing
            # positions restore base edges and impose no new ear seam.
            for seam in range(rank):
                left, right = output[seam], output[(seam + 1) % rank]
                if left is None or right is None:
                    continue
                if seam in (gap - 1, gap):
                    raw_left = profile if seam == gap else left
                    raw_right = profile if seam == gap - 1 else right
                    assert compatible(raw_left, raw_right, seam)
                else:
                    assert compatible(left, right, seam)
            output_load[tuple(output)] += 1

    left_size = len({word[gap - 1] for word in words})
    right_size = len({word[(gap + 1) % rank] for word in words})
    decoder_bound = left_size * right_size
    assert max(output_load.values()) <= decoder_bound
    incidences = len(partials) * len(profiles)
    assert len(output_load) * decoder_bound >= incidences
    assert len(output_load) * projection_size * decoder_bound >= len(words) * len(profiles)
    return {
        "rank": rank,
        "alphabet": alphabet,
        "valid_words": len(words),
        "gap_projection": projection_size,
        "partial_words": len(partials),
        "profiles": len(profiles),
        "outputs": len(output_load),
        "maximum_actual_load": max(output_load.values()),
        "decoder_bound": decoder_bound,
    }


def coefficient_audit() -> dict[str, object]:
    a, kappa, c0 = Q(1, 4), Q(1, 4), Q(1, 8)
    coefficient = a + c0 * (a / kappa) ** 2
    assert coefficient == Q(3, 8)
    rows = []
    for d in (64, 128, 256, 512):
        source = a * d * d
        leading_gain = c0 * source**2 / (kappa * d) ** 2
        lower = source + leading_gain - 7 * d
        assert source + leading_gain == Q(3, 8) * d * d
        rows.append(
            {
                "log_D": d,
                "source_bits": int(source),
                "bank_lower_bits": int(lower),
                "linear_jet_and_decoder_loss": 7 * d,
                "leading_coefficient": str(coefficient),
            }
        )
    return {"coefficient": str(coefficient), "scales": rows}


def six_point_audit() -> dict[str, object]:
    left_base = pt(-3, 0)
    z = pt(3, 0)
    top = pt(0, 4)
    left_ear = (pt(-10, -16), pt(-9, -15))
    right_ear = (pt(8, 1),)
    base = (left_base, z, top)
    assert is_convex(base + left_ear)
    assert is_convex(base + right_ear)
    assert not is_convex(base + left_ear + right_ear)
    released = tuple(point for point in base if point != z) + left_ear + right_ear
    assert not is_convex(released)
    adaptive = base + left_ear
    assert is_convex(adaptive)
    all_points = base + left_ear + right_ear
    determinants = [
        cross(all_points[i], all_points[j], all_points[k])
        for i in range(len(all_points))
        for j in range(i + 1, len(all_points))
        for k in range(j + 1, len(all_points))
    ]
    assert all(value != 0 for value in determinants)
    return {
        "general_position_triples": len(determinants),
        "union_hull_size": len(hull(base + left_ear + right_ear)),
        "guard_released_hull_size": len(hull(released)),
        "adaptive_output_size": len(adaptive),
    }


def detached_circuit_audit() -> dict[str, object]:
    u, v = pt(-1, 0), pt(1, 0)
    q = (Q(-19, 20), Q(1, 20))
    x = (Q(-3, 40), Q(7, 8))
    w = (Q(0), Q(10, 11))
    z = (Q(3, 40), Q(7, 8))
    y = (Q(2, 15), Q(8, 9))
    assert is_convex((u, v, q, x, w, z))
    assert is_convex((u, v, q, x, w, y))
    bad = (q, x, z, y)
    assert not is_convex(bad)
    weights = (Q(3, 230), Q(122, 575), Q(891, 1150))
    assert sum(weights, Q()) == 1
    rebuilt = tuple(
        weights[0] * q[i] + weights[1] * x[i] + weights[2] * y[i]
        for i in range(2)
    )
    assert rebuilt == z
    return {
        "selected_words": 2,
        "support_product": 2,
        "redundancy_bits": 0,
        "fixed_replacement_jet": ["z", "y"],
        "bad_hull_size": len(hull(bad)),
    }


def main() -> None:
    result = {
        "jet_pigeonhole": jet_pigeonhole_audit(),
        "adaptive_omission": adaptive_omission_audit(),
        "coefficient": coefficient_audit(),
        "six_point_release": six_point_audit(),
        "detached_mask_circuit": detached_circuit_audit(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: mask-aware jet/adaptive-omission audit verified")


if __name__ == "__main__":
    main()
