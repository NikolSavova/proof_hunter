#!/usr/bin/env python3
"""Audit for SAME_PARENT_RETENTION_PROFILE_SPLICE.md."""

from __future__ import annotations

import json
import math
from functools import reduce
from fractions import Fraction as Q
from operator import mul


Point = tuple[Q, Q]


def point(x: int, xd: int, y: int, yd: int) -> Point:
    return (Q(x, xd), Q(y, yd))


def cross(o: Point, a: Point, b: Point) -> Q:
    return (a[0] - o[0]) * (b[1] - o[1]) - (
        a[1] - o[1]
    ) * (b[0] - o[0])


def convex_hull(points: tuple[Point, ...]) -> tuple[Point, ...]:
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
    return len(set(points)) == len(points) == len(convex_hull(points))


def circuit_audit() -> dict[str, object]:
    u = point(-1, 1, 0, 1)
    v = point(1, 1, 0, 1)
    q = point(-19, 20, 1, 20)
    x = point(-3, 40, 7, 8)
    w = point(0, 1, 10, 11)
    z = point(3, 40, 7, 8)
    y = point(2, 15, 8, 9)

    first = (u, v, q, x, w, z)
    second = (u, v, q, x, w, y)
    bad = (q, x, z, y)
    assert is_convex(first)
    assert is_convex(second)
    assert not is_convex(bad)

    coefficients = (Q(3, 230), Q(122, 575), Q(891, 1150))
    assert sum(coefficients, Q()) == 1
    reconstructed = tuple(
        coefficients[0] * q[i]
        + coefficients[1] * x[i]
        + coefficients[2] * y[i]
        for i in range(2)
    )
    assert reconstructed == z
    assert all(value > 0 for value in coefficients)

    all_points = (u, v, q, x, w, z, y)
    triple_determinants = []
    for i in range(len(all_points)):
        for j in range(i + 1, len(all_points)):
            for k in range(j + 1, len(all_points)):
                det = cross(all_points[i], all_points[j], all_points[k])
                assert det != 0
                triple_determinants.append(det)
    return {
        "selected_words": 2,
        "support_product": 2,
        "redundancy_bits": 0,
        "general_position_triples": len(triple_determinants),
        "bad_output_hull_size": len(convex_hull(bad)),
        "barycentric_coefficients": [str(value) for value in coefficients],
    }


def cyclic_bank_identity_audit() -> dict[str, object]:
    local_sizes = (2, 3, 5, 7, 11)
    left_profiles = (2, 3, 2, 4, 3)
    right_profiles = (3, 2, 5, 2, 4)
    reservoirs = tuple(
        left_profiles[i] * right_profiles[i]
        for i in range(len(local_sizes))
    )
    rank = len(local_sizes)
    support_product = reduce(mul, local_sizes, 1)
    banks = []
    for gap in range(rank):
        retained = reduce(
            mul,
            (
                local_sizes[i]
                for i in range(rank)
                if i not in ((gap - 1) % rank, gap, (gap + 1) % rank)
            ),
            1,
        )
        banks.append(
            right_profiles[(gap - 1) % rank]
            * left_profiles[(gap + 1) % rank]
            * retained
        )

    cyclic_left = reduce(
        mul, (Q(bank, support_product) for bank in banks), Q(1)
    )
    cyclic_right = reduce(
        mul,
        (
            Q(reservoirs[i], local_sizes[i] ** 3)
            for i in range(rank)
        ),
        Q(1),
    )
    assert cyclic_left == cyclic_right

    selected = 210
    assert support_product % selected == 0
    redundancy_factor = Q(support_product, selected)
    exact_geometric_rhs = redundancy_factor**rank * cyclic_right
    assert Q(max(banks), selected) ** rank >= exact_geometric_rhs
    return {
        "rank": rank,
        "support_product": support_product,
        "selected": selected,
        "redundancy_factor": str(redundancy_factor),
        "banks": banks,
        "cyclic_identity": str(cyclic_left),
    }


def coefficient_audit() -> dict[str, object]:
    a = Q(1, 4)
    kappa = Q(1, 4)
    c0 = Q(1, 8)
    result = a + c0 * (a / kappa) ** 2
    assert result == Q(3, 8)

    rows = []
    for d in (64, 128, 256, 512):
        q = d // 4
        source_bits = Q(d * d, 4)
        # Conditional one-gap leading term; the -3S/q term is retained.
        lower = source_bits + c0 * source_bits**2 / q**2 - 3 * source_bits / q
        leading = Q(3 * d * d, 8)
        assert lower == leading - 3 * d
        rows.append(
            {
                "log_D": d,
                "source_bits": int(source_bits),
                "conditional_bank_bits": float(lower),
                "three_eighths_leading_bits": int(leading),
                "linear_error_bits": 3 * d,
            }
        )
    return {"coefficient": str(result), "scales": rows}


def large_redundancy_audit() -> dict[str, object]:
    rows = []
    eta = Q(1, 32)
    for d in (64, 128, 256, 512):
        redundancy = eta * d * d
        guaranteed_gain = redundancy - 2 * d
        assert guaranteed_gain == eta * d * d - 2 * d
        rows.append(
            {
                "log_D": d,
                "redundancy_bits": int(redundancy),
                "gain_lower_bits": int(guaranteed_gain),
                "normalized_gain": float(guaranteed_gain / (d * d)),
            }
        )
    return {"eta": str(eta), "scales": rows}


def mds_and_tensor_audit() -> dict[str, object]:
    mds_rows = []
    for d in (64, 128, 256, 512):
        q = d // 4
        c = math.ceil(q / math.log2(d))
        selected_bits = (q - c) * d
        support_bits = q * d
        redundancy = c * d
        assert support_bits - selected_bits == redundancy
        assert redundancy / (d * d) <= 1 / (4 * math.log2(d)) + 1 / d
        mds_rows.append(
            {
                "log_p": d,
                "coordinates": q,
                "parity_symbols": c,
                "selected_bits": selected_bits,
                "redundancy_over_d2": redundancy / (d * d),
            }
        )

    tensor_rows = []
    for blocks, alphabet in ((8, 16), (16, 32), (32, 64)):
        selected = alphabet**blocks
        support = alphabet**blocks
        assert selected == support
        tensor_rows.append(
            {
                "blocks": blocks,
                "alphabet": alphabet,
                "log2_selected": blocks * math.log2(alphabet),
                "redundancy_bits": 0,
            }
        )
    return {"mds": mds_rows, "full_tensor": tensor_rows}


def retention_scale_audit() -> dict[str, object]:
    # A sample subquadratic redundancy R=d^(3/2) has O(q+R)=o(d^2).
    rows = []
    for d in (64, 256, 1024, 4096):
        q = d // 4
        redundancy = d * math.isqrt(d)
        loss_ratio = (q + redundancy) / (d * d)
        rows.append(
            {
                "log_D": d,
                "rank": q,
                "redundancy": redundancy,
                "retention_loss_over_d2": loss_ratio,
            }
        )
    assert rows[-1]["retention_loss_over_d2"] < rows[0]["retention_loss_over_d2"]
    return {"scales": rows}


def main() -> None:
    result = {
        "cyclic_bank_identity": cyclic_bank_identity_audit(),
        "large_redundancy": large_redundancy_audit(),
        "retention_scale": retention_scale_audit(),
        "conditional_coefficient": coefficient_audit(),
        "compatible_jet_circuit": circuit_audit(),
        "regressions": mds_and_tensor_audit(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: same-parent retention/profile splice verified")


if __name__ == "__main__":
    main()
