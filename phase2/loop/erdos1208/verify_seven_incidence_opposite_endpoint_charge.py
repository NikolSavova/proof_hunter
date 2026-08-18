#!/usr/bin/env python3
"""Exact checks for SEVEN_INCIDENCE_OPPOSITE_ENDPOINT_CHARGE.md."""

from __future__ import annotations

from collections import Counter, defaultdict

from analyze_affine_costas_energy import smallest_transform, welch
from verify_endpoint_midpoint_sidon_ruler_barrier import construction
from verify_orthogonal_switching_rich_tail import concrete_quadratic_instance
from verify_orthogonal_two_support_gate import difference_set
from verify_radial_orthogonal_product_barrier import radial_set
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Label = tuple[Point, Point]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def linear(point: Point) -> Point:
    """Apply L=I+J."""
    return point[0] - point[1], point[0] + point[1]


def conjugate_linear(point: Point) -> Point:
    """Apply I-J."""
    return point[0] + point[1], point[1] - point[0]


def scale(coefficient: int, point: Point) -> Point:
    return coefficient * point[0], coefficient * point[1]


def overlap_table(differences: set[Point]) -> dict[Point, list[Point]]:
    overlaps: dict[Point, list[Point]] = defaultdict(list)
    for endpoint in differences:
        for start in differences:
            overlaps[subtract(endpoint, start)].append(start)
    return overlaps


def rich_fibres(
    differences: set[Point], adaptive: bool
) -> tuple[dict[Label, set[Point]], int, set[Point]]:
    overlaps = overlap_table(differences)
    number = len(differences)
    support = len(overlaps)
    if adaptive:
        shifts = {
            shift
            for shift, starts in overlaps.items()
            if shift != (0, 0)
            and len(starts) * number > support
            and len(overlaps.get(rotate(shift), ())) * number > support
        }
    else:
        shifts = {
            shift
            for shift, starts in overlaps.items()
            if starts and overlaps.get(rotate(shift))
        }

    fibres: dict[Label, set[Point]] = defaultdict(set)
    for shift in shifts:
        rotated = rotate(shift)
        for first_start in overlaps[shift]:
            first_endpoint = add(first_start, shift)
            for second_start in overlaps[rotated]:
                second_endpoint = add(second_start, rotated)
                fibres[first_start, add(first_endpoint, second_endpoint)].add(
                    shift
                )
    return fibres, support, shifts


def charge_profile(
    differences: set[Point], adaptive: bool
) -> tuple[int, int, int, int]:
    fibres, _, shifts = rich_fibres(differences, adaptive)
    loads: Counter[Label] = Counter()
    first_preimages: dict[Label, list[tuple[Point, Point]]] = defaultdict(list)
    pair_count = 0

    for (start, ordinary_sum), fibre in fibres.items():
        other_label = subtract(ordinary_sum, start)
        local_keys: set[Label] = set()
        for shift in fibre:
            first_endpoint = add(start, shift)
            first_second_start = subtract(other_label, linear(shift))
            assert first_endpoint in differences
            assert first_second_start in differences
            for other_shift in fibre:
                if shift == other_shift:
                    continue
                other_endpoint = add(start, other_shift)
                charge = (
                    first_second_start,
                    add(start, other_endpoint),
                )
                assert charge not in local_keys
                local_keys.add(charge)

                # Verify the fixed-key preimage system (4.3)--(4.5).
                fixed_v, fixed_t = charge
                a_value = start
                b_value = first_endpoint
                recovered_shift = subtract(b_value, a_value)
                recovered_other = subtract(
                    fixed_t, scale(2, a_value)
                )
                assert recovered_shift == shift
                assert recovered_other == other_shift
                assert recovered_shift in shifts
                assert recovered_other in shifts

                six_values = (
                    a_value,
                    b_value,
                    subtract(fixed_t, a_value),
                    add(fixed_v, rotate(subtract(b_value, a_value))),
                    subtract(
                        add(
                            fixed_v,
                            add(
                                conjugate_linear(a_value),
                                linear(b_value),
                            ),
                        ),
                        fixed_t,
                    ),
                    add(
                        fixed_v,
                        linear(
                            subtract(
                                add(a_value, b_value), fixed_t
                            )
                        ),
                    ),
                )
                assert all(value in differences for value in six_values)
                loads[charge] += 1
                if len(first_preimages[charge]) < 2:
                    first_preimages[charge].append((a_value, b_value))
                pair_count += 1

        assert len(local_keys) == len(fibre) * (len(fibre) - 1)

    assert pair_count == sum(
        len(fibre) * (len(fibre) - 1) for fibre in fibres.values()
    )
    for (fixed_v, fixed_t), preimages in first_preimages.items():
        if len(preimages) < 2:
            continue
        (a_value, b_value), (other_a, other_b) = preimages
        delta = subtract(other_a, a_value)
        epsilon = subtract(other_b, b_value)
        first_forms = (
            a_value,
            b_value,
            subtract(fixed_t, a_value),
            add(fixed_v, rotate(subtract(b_value, a_value))),
            subtract(
                add(
                    fixed_v,
                    add(conjugate_linear(a_value), linear(b_value)),
                ),
                fixed_t,
            ),
            add(
                fixed_v,
                linear(subtract(add(a_value, b_value), fixed_t)),
            ),
        )
        second_forms = (
            other_a,
            other_b,
            subtract(fixed_t, other_a),
            add(fixed_v, rotate(subtract(other_b, other_a))),
            subtract(
                add(
                    fixed_v,
                    add(conjugate_linear(other_a), linear(other_b)),
                ),
                fixed_t,
            ),
            add(
                fixed_v,
                linear(subtract(add(other_a, other_b), fixed_t)),
            ),
        )
        actual_displacements = tuple(
            subtract(second, first)
            for first, second in zip(first_forms, second_forms)
        )
        expected_displacements = (
            delta,
            epsilon,
            scale(-1, delta),
            rotate(subtract(epsilon, delta)),
            add(conjugate_linear(delta), linear(epsilon)),
            linear(add(delta, epsilon)),
        )
        assert actual_displacements == expected_displacements
    return (
        pair_count,
        len(loads),
        max(loads.values(), default=0),
        sum(value * value for value in loads.values()),
    )


def verify_adaptive_profiles() -> None:
    expected = {
        "closure-30": (1_420, 1_420, 1, 1_420),
        "closure-40": (370_516, 329_141, 9, 475_112),
        "Costas-11": (160, 160, 1, 160),
        "Costas-17": (76, 76, 1, 76),
        "Costas-23": (14_296, 13_320, 3, 16_296),
        "Costas-31": (7_912, 7_638, 2, 8_460),
        "radial-8": (555_948, 24_542, 98, 20_561_936),
        "radial-12": (8_516_236, 110_306, 391, 1_142_996_544),
    }
    families: list[tuple[str, set[Point]]] = [
        ("closure-30", difference_set(POINTS[:30])),
        ("closure-40", difference_set(POINTS[:40])),
    ]
    for prime in (11, 17, 23, 31):
        points = welch(prime)
        shear, stretch = smallest_transform(points)
        points = [(x + shear * y, stretch * y) for x, y in points]
        families.append((f"Costas-{prime}", difference_set(points)))
    for side in (8, 12):
        families.append((f"radial-{side}", radial_set(side)))

    for name, differences in families:
        profile = charge_profile(differences, adaptive=True)
        assert profile == expected[name]
        number = len(differences)
        support = len(overlap_table(differences))
        pairs, image, maximum, second_moment = profile
        print(
            name,
            "N", number,
            "S", support,
            "profile", profile,
            "average", pairs / image if image else 0.0,
            "image/(NS)", image / (number * support),
            "charge-second/pairs", second_moment / pairs if pairs else 0.0,
        )


def verify_quadratic_barrier() -> None:
    points, _ = concrete_quadratic_instance()
    profile = charge_profile(difference_set(points), adaptive=False)
    assert profile == (10_888, 9_952, 2, 12_760)
    print("unrestricted quadratic-18", profile)


def verify_ruler_barrier() -> None:
    for side in (4, 8, 12, 20, 50):
        _, base, first_copy, second_copy, selected, _ = construction(side)
        fibre: list[tuple[Point, Point]] = []
        for first_index, first in enumerate(base[:side]):
            for second_index, second in enumerate(base[side:]):
                fibre_value = subtract(first, second)
                second_start = subtract(
                    first_copy[first_index], second_copy[second_index]
                )
                fibre.append((fibre_value, second_start))

        charges: Counter[Label] = Counter()
        for first_value, first_second_start in fibre:
            for other_value, _ in fibre:
                if first_value == other_value:
                    continue
                charges[
                    first_second_start,
                    add(selected, other_value),
                ] += 1
        expected = side * side * (side * side - 1)
        assert sum(charges.values()) == expected
        assert len(charges) == expected
        assert max(charges.values()) == 1
        print("Sidon-ruler intended fibre", side, expected, "injective")


def main() -> None:
    verify_adaptive_profiles()
    verify_quadratic_barrier()
    verify_ruler_barrier()
    print("opposite-endpoint charge: PASS")


if __name__ == "__main__":
    main()
