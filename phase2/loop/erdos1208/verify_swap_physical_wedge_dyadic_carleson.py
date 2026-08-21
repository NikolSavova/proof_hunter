#!/usr/bin/env python3
"""Verify the physical-wedge dyadic decomposition."""

from __future__ import annotations

from collections import defaultdict
from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from itertools import combinations, product
from math import comb, prod
from random import Random

Wedge = tuple[int, int, int, int, int]
Point = tuple[int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def sub(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def rotate(value: Point) -> Point:
    return -value[1], value[0]


def linear(value: Point) -> Point:
    return add(value, rotate(value))


def neg(value: Point) -> Point:
    return -value[0], -value[1]


def wedges(k: int) -> list[Wedge]:
    return [
        (endpoint, first_other, second_other, first_role, second_role)
        for endpoint in range(k)
        for first_other in range(k)
        if first_other != endpoint
        for second_other in range(k)
        if second_other != endpoint
        for first_role in (0, 1)
        for second_role in (2, 3)
    ]


def mass(load: int) -> int:
    return 3 * comb(load, 3)


def audit_counts() -> None:
    for k in range(2, 12):
        all_wedges = wedges(k)
        assert len(all_wedges) == 4 * k * (k - 1) ** 2
        same_edge = [row for row in all_wedges if row[1] == row[2]]
        one_endpoint = [row for row in all_wedges if row[1] != row[2]]
        assert len(same_edge) == 4 * k * (k - 1)
        assert len(one_endpoint) == 4 * k * (k - 1) * (k - 2)


def audit_decomposition() -> None:
    rng = Random(1208)
    for k in range(3, 11):
        universe = wedges(k)
        for _ in range(100):
            cells: dict[Wedge, list[int]] = defaultdict(list)
            for wedge in rng.sample(universe, rng.randrange(len(universe) + 1)):
                cells[wedge] = [rng.randrange(1, 13) for _ in range(rng.randrange(7))]

            wedge_mass = {
                wedge: sum(mass(load) for load in loads)
                for wedge, loads in cells.items()
            }
            centre_mass = sum(wedge_mass.values())
            physical_second = sum(
                comb(load, 2) for loads in cells.values() for load in loads
            )
            assert centre_mass == sum(
                (load - 2) * comb(load, 2)
                for loads in cells.values()
                for load in loads
            )

            for threshold in (0, 1, 5, 20, 100):
                for rich_load in (3, 4, 7, 13):
                    rich_wedge_mass = {
                        wedge: sum(
                            mass(load) for load in loads if load >= rich_load
                        )
                        for wedge, loads in cells.items()
                    }
                    heavy = sum(
                        value
                        for value in rich_wedge_mass.values()
                        if value > threshold
                    )
                    positive_light_rich_wedges = sum(
                        1
                        for value in rich_wedge_mass.values()
                        if 0 < value <= threshold
                    )
                    rich_pair_cost = comb(rich_load, 2)
                    assert (
                        rich_pair_cost * positive_light_rich_wedges
                        <= physical_second
                    )
                    assert rich_pair_cost * (centre_mass - heavy) <= (
                        (rich_pair_cost * (rich_load - 3) + threshold)
                        * physical_second
                    )

                    same_low = sum(
                        wedge_mass[wedge]
                        for wedge in cells
                        if wedge[1] == wedge[2]
                        and wedge_mass[wedge] <= threshold
                    )
                    one_low = sum(
                        wedge_mass[wedge]
                        for wedge in cells
                        if wedge[1] != wedge[2]
                        and wedge_mass[wedge] <= threshold
                    )
                    assert same_low <= 4 * threshold * k * (k - 1)
                    assert one_low <= 4 * threshold * k * (k - 1) * (k - 2)


def audit_stored_stress() -> None:
    rows = {
        23: (204, 68, 3, 24, 180),
        29: (4857, 945, 48, 774, 4083),
        31: (5058, 418, 123, 1992, 3066),
        37: (4896, 1102, 45, 936, 3960),
    }
    for prime, (total, support, maximum, same_edge, one_endpoint) in rows.items():
        k = prime - 1
        assert total == same_edge + one_endpoint
        assert support <= 4 * k * (k - 1) ** 2
        assert maximum <= total
    assert (93 + 30, 87 + 21) == (123, 108)
    assert mass(6) == 60
    triple_rows = {
        23: (68, 1, 1, 0),
        29: (1583, 15, 2, 36),
        31: (1386, 32, 4, 366),
        37: (1604, 15, 2, 28),
    }
    for prime, (support, wedge_support, maximum, collisions) in triple_rows.items():
        assert support > 0 and wedge_support >= 1, prime
        assert maximum >= 1 and collisions >= 0, prime
    assert triple_rows[31][2] > 1  # Literal triple rigidity is false.
    assert triple_rows[31][1] > 1  # Pointwise wedge support is nonconstant.
    zero_masks = {
        29: {(0, 1, 2): 28, (0, 3, 5): 4, (2, 5): 4},
        31: {
            (0,): 14,
            (0, 1, 2): 258,
            (0, 3, 5): 20,
            (2,): 12,
            (2, 3): 10,
            (2, 4): 4,
            (2, 5): 18,
            (4,): 2,
            (4, 5): 28,
        },
        37: {(0, 1, 2): 24, (0, 3, 5): 2, (2, 5): 2},
    }
    for prime, profile in zero_masks.items():
        assert () not in profile
        assert sum(profile.values()) == triple_rows[prime][3]
    invariant_rows = {
        29: (816, 4, 23, 3, 143, 1321, 1295, 115, 1180),
        31: (332, 4, 68, 2, 254, 878, 770, 60, 710),
        37: (960, 4, 30, 2, 152, 1300, 1280, 120, 1160),
    }
    for prime, (
        invariant_support,
        maximum_wedges,
        maximum_keys,
        maximum_parameter_codegree,
        parameter_collisions,
        singleton_edges,
        terminal_unique,
        terminal_collinear,
        terminal_noncollinear,
    ) in invariant_rows.items():
        total_edges = triple_rows[prime][0]
        assert invariant_support > 0 and maximum_wedges >= 1
        assert maximum_keys >= 1 and maximum_parameter_codegree >= 1
        assert singleton_edges <= total_edges
        assert total_edges - singleton_edges <= 2 * parameter_collisions
        assert terminal_unique == terminal_collinear + terminal_noncollinear
        assert terminal_unique <= singleton_edges
        assert 9 * terminal_noncollinear > 8 * terminal_unique
    coarse_rows = {
        29: (1448, 4, 193, 1295),
        31: (1132, 8, 916, 770),
        37: (1452, 4, 192, 1280),
    }
    for prime, (support, maximum, collisions, singleton_cells) in (
        coarse_rows.items()
    ):
        assert support <= triple_rows[prime][0]
        assert maximum >= 1 and collisions >= 0
        assert singleton_cells == invariant_rows[prime][6]
        assert singleton_cells <= support
        incidence = rows[prime][0] // 3
        assert 3 * incidence == rows[prime][0]
        assert incidence * incidence <= support * (incidence + 2 * collisions)


def audit_support_collision_gate() -> None:
    rng = Random(1208202601)
    for _ in range(1000):
        multiplicities = [
            rng.randrange(1, 12) for _ in range(rng.randrange(1, 80))
        ]
        incidence = sum(multiplicities)
        support = len(multiplicities)
        collisions = sum(comb(value, 2) for value in multiplicities)
        assert incidence * incidence <= support * (
            incidence + 2 * collisions
        )
        common_budget = max(support, collisions, 1)
        assert 3 * incidence <= 6 * common_budget


def add_linear(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(first + second for first, second in zip(left, right))


def scale_linear(coefficient: int, value: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(coefficient * entry for entry in value)


def symbolic_wedge_points(
    blocks: int, invariant: Point
) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    dimension = 4 * blocks + 1
    constant_x = (0,) * (dimension - 1) + (invariant[0],)
    constant_y = (0,) * (dimension - 1) + (invariant[1],)
    points = []
    for block in range(blocks):
        basis = []
        for coordinate in range(4):
            vector = [0] * dimension
            vector[4 * block + coordinate] = 1
            basis.append(tuple(vector))
        p_x, p_y, u_x, u_y = basis
        z_x = add_linear(
            add_linear(add_linear(p_x, scale_linear(-1, p_y)), u_y),
            constant_x,
        )
        z_y = add_linear(
            add_linear(add_linear(p_x, p_y), scale_linear(-1, u_x)),
            constant_y,
        )
        points.extend(((p_x, p_y), (u_x, u_y), (z_x, z_y)))
    return points


def squared_distance_polynomial(
    first: tuple[tuple[int, ...], tuple[int, ...]],
    second: tuple[tuple[int, ...], tuple[int, ...]],
) -> tuple[tuple[tuple[int, int], int], ...]:
    coefficients: dict[tuple[int, int], int] = defaultdict(int)
    for first_coordinate, second_coordinate in zip(first, second):
        difference = tuple(
            left - right
            for left, right in zip(first_coordinate, second_coordinate)
        )
        for first_index, first_value in enumerate(difference):
            if first_value == 0:
                continue
            for second_index in range(first_index, len(difference)):
                second_value = difference[second_index]
                if second_value == 0:
                    continue
                coefficients[first_index, second_index] += (
                    first_value
                    * second_value
                    * (1 if first_index == second_index else 2)
                )
    return tuple(
        sorted((key, value) for key, value in coefficients.items() if value)
    )


def audit_physical_invariant_barrier() -> None:
    symbolic_points = symbolic_wedge_points(4, (1, 0))
    squared_polynomials = {
        squared_distance_polynomial(first, second)
        for first, second in combinations(symbolic_points, 2)
    }
    assert len(squared_polynomials) == comb(len(symbolic_points), 2)

    points = [
        (2417, 4293),
        (7, -3784),
        (-5643, 6714),
        (-1337, 611),
        (323, -4677),
        (-6608, -1038),
        (4542, -1748),
        (1938, 1569),
        (7876, 867),
        (-1070, 4038),
        (1021, 4848),
        (-243, 1958),
        (2066, 3614),
        (4405, -2269),
        (-3800, 1286),
        (1665, -4692),
        (4280, -381),
        (5993, -7296),
    ]
    squared_distances = []
    for first, second in combinations(points, 2):
        difference = sub(first, second)
        squared_distances.append(
            difference[0] * difference[0] + difference[1] * difference[1]
        )
    assert len(set(squared_distances)) == comb(len(points), 2)
    invariants = []
    for index in range(0, len(points), 3):
        p_value, u_value, z_value = points[index : index + 3]
        first_edge = sub(u_value, p_value)
        second_edge = sub(z_value, p_value)
        invariants.append(add(rotate(first_edge), second_edge))
    assert invariants == [(17, 11)] * 6


def audit_owner_switch_normal_form() -> None:
    rng = Random(12082026)
    for _ in range(1000):
        c_first = rng.randrange(-20, 21), rng.randrange(-20, 21)
        ell_first = rng.randrange(-20, 21), rng.randrange(-20, 21)
        a_first = rng.randrange(-20, 21), rng.randrange(-20, 21)
        b_first = rng.randrange(-20, 21), rng.randrange(-20, 21)
        eta_first = rng.randrange(-20, 21), rng.randrange(-20, 21)
        centre_shift = rng.randrange(-8, 9), rng.randrange(-8, 9)
        second_shift = rng.randrange(-8, 9), rng.randrange(-8, 9)
        eta_shift = rng.randrange(-8, 9), rng.randrange(-8, 9)

        c_second = add(c_first, centre_shift)
        a_second = sub(a_first, centre_shift)
        b_second = add(b_first, second_shift)
        ell_second = sub(ell_first, linear(second_shift))
        eta_second = add(eta_first, eta_shift)
        assert add(c_first, a_first) == add(c_second, a_second)
        assert add(ell_first, linear(b_first)) == add(
            ell_second, linear(b_second)
        )

        previous_q: Point | None = None
        previous_tracks: tuple[Point, ...] | None = None
        for _ in range(5):
            q_value = rng.randrange(-20, 21), rng.randrange(-20, 21)

            def tracks(
                centre: Point,
                ell: Point,
                first_displacement: Point,
                second_displacement: Point,
                eta: Point,
            ) -> tuple[Point, ...]:
                first_x = sub(centre, q_value)
                first_y = add(ell, rotate(add(q_value, first_displacement)))
                first_z = add(add(ell, rotate(q_value)), linear(first_displacement))
                second_q = sub(q_value, eta)
                second_x = sub(centre, second_q)
                second_y = add(
                    ell, rotate(add(second_q, second_displacement))
                )
                second_z = add(
                    add(ell, rotate(second_q)), linear(second_displacement)
                )
                return first_x, first_y, first_z, second_x, second_y, second_z

            first_tracks = tracks(
                c_first, ell_first, a_first, b_first, eta_first
            )
            second_tracks = tracks(
                c_second, ell_second, a_second, b_second, eta_second
            )
            actual = tuple(
                sub(second, first)
                for first, second in zip(first_tracks, second_tracks)
            )
            expected = (
                centre_shift,
                neg(add(linear(second_shift), rotate(centre_shift))),
                neg(linear(add(centre_shift, second_shift))),
                add(centre_shift, eta_shift),
                neg(add(second_shift, rotate(eta_shift))),
                neg(rotate(eta_shift)),
            )
            assert actual == expected

            physical_v = add(c_first, a_first)
            physical_w = add(ell_first, linear(b_first))
            invariant = add(rotate(physical_v), physical_w)
            first_relation = add(
                sub(
                    add(rotate(first_tracks[0]), first_tracks[1]),
                    linear(first_tracks[4]),
                ),
                linear(first_tracks[5]),
            )
            second_relation = add(
                sub(
                    add(
                        add(rotate(first_tracks[0]), first_tracks[2]),
                        first_tracks[3],
                    ),
                    linear(first_tracks[4]),
                ),
                first_tracks[5],
            )
            assert first_relation == invariant
            assert second_relation == sub(invariant, rotate(invariant))

            if previous_q is not None and previous_tracks is not None:
                q_shift = sub(q_value, previous_q)
                track_shifts = tuple(
                    sub(current, previous)
                    for current, previous in zip(first_tracks, previous_tracks)
                )
                assert track_shifts == (
                    neg(q_shift),
                    rotate(q_shift),
                    rotate(q_shift),
                    neg(q_shift),
                    rotate(q_shift),
                    rotate(q_shift),
                )
            previous_q = q_value
            previous_tracks = first_tracks


def linear_tracks(
    first_displacement: Point,
    second_displacement: Point,
    eta: Point,
    q_value: Point,
) -> tuple[Point, ...]:
    return (
        neg(add(first_displacement, q_value)),
        add(neg(linear(second_displacement)), rotate(add(q_value, first_displacement))),
        add(
            neg(linear(second_displacement)),
            add(rotate(q_value), linear(first_displacement)),
        ),
        add(neg(add(first_displacement, q_value)), eta),
        add(neg(second_displacement), rotate(sub(q_value, eta))),
        rotate(sub(q_value, eta)),
    )


def physical_tracks(
    physical_v: Point,
    physical_w: Point,
    first_displacement: Point,
    second_displacement: Point,
    eta: Point,
    q_value: Point,
) -> tuple[Point, ...]:
    return tuple(
        add(translation, value)
        for translation, value in zip(
            (
                physical_v,
                physical_w,
                physical_w,
                physical_v,
                physical_w,
                physical_w,
            ),
            linear_tracks(
                first_displacement,
                second_displacement,
                eta,
                q_value,
            ),
        )
    )


def audit_same_invariant_wedge_switch() -> None:
    rng = Random(1208202602)
    for _ in range(1000):
        first_v = rng.randrange(-20, 21), rng.randrange(-20, 21)
        first_w = rng.randrange(-20, 21), rng.randrange(-20, 21)
        first_a = rng.randrange(-20, 21), rng.randrange(-20, 21)
        first_b = rng.randrange(-20, 21), rng.randrange(-20, 21)
        first_e = rng.randrange(-20, 21), rng.randrange(-20, 21)
        wedge_shift = rng.randrange(-8, 9), rng.randrange(-8, 9)
        a_shift = rng.randrange(-8, 9), rng.randrange(-8, 9)
        b_shift = rng.randrange(-8, 9), rng.randrange(-8, 9)
        e_shift = rng.randrange(-8, 9), rng.randrange(-8, 9)

        second_v = add(first_v, wedge_shift)
        second_w = sub(first_w, rotate(wedge_shift))
        second_a = add(first_a, a_shift)
        second_b = add(first_b, b_shift)
        second_e = add(first_e, e_shift)
        assert add(rotate(first_v), first_w) == add(
            rotate(second_v), second_w
        )

        expected = linear_tracks(a_shift, b_shift, e_shift, neg(wedge_shift))
        for _ in range(5):
            q_value = rng.randrange(-20, 21), rng.randrange(-20, 21)
            first = physical_tracks(
                first_v, first_w, first_a, first_b, first_e, q_value
            )
            second = physical_tracks(
                second_v, second_w, second_a, second_b, second_e, q_value
            )
            actual = tuple(
                sub(second_value, first_value)
                for first_value, second_value in zip(first, second)
            )
            assert actual == expected

    for _ in range(1000):
        codegrees = [rng.randrange(1, 12) for _ in range(rng.randrange(80))]
        nonsingleton_incidence = sum(value for value in codegrees if value >= 2)
        collision_mass = sum(comb(value, 2) for value in codegrees)
        assert nonsingleton_incidence <= 2 * collision_mass


def rational_rank(rows: list[list[int]]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    output = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (
                row
                for row in range(output, len(matrix))
                if matrix[row][column]
            ),
            None,
        )
        if pivot is None:
            continue
        matrix[output], matrix[pivot] = matrix[pivot], matrix[output]
        scale = matrix[output][column]
        matrix[output] = [value / scale for value in matrix[output]]
        for row in range(len(matrix)):
            if row == output or not matrix[row][column]:
                continue
            scale = matrix[row][column]
            matrix[row] = [
                value - scale * base
                for value, base in zip(matrix[row], matrix[output])
            ]
        output += 1
    return output


def audit_fractional_basis() -> None:
    variable_basis: list[tuple[Point, Point, Point, Point]] = []
    for variable in range(4):
        for coordinate in range(2):
            values = [(0, 0)] * 4
            values[variable] = (1, 0) if coordinate == 0 else (0, 1)
            variable_basis.append(tuple(values))  # type: ignore[arg-type]
    coefficient_rows: list[list[int]] = [[] for _ in range(12)]
    for basis in variable_basis:
        outputs = linear_tracks(*basis)
        for form, output in enumerate(outputs):
            coefficient_rows[2 * form].append(output[0])
            coefficient_rows[2 * form + 1].append(output[1])

    valid: list[tuple[int, ...]] = []
    invalid: list[tuple[int, ...]] = []
    for forms in combinations(range(6), 4):
        rows = [
            coefficient_rows[2 * form + coordinate]
            for form in forms
            for coordinate in range(2)
        ]
        (valid if rational_rank(rows) == 8 else invalid).append(forms)
    assert invalid == [(0, 1, 4, 5), (1, 2, 3, 5)]
    assert len(valid) == 13

    heavy = {
        (0, 1, 2, 5),
        (0, 1, 3, 5),
        (1, 2, 4, 5),
        (1, 3, 4, 5),
    }
    weights = {
        forms: Fraction(1, 10) if forms in heavy else Fraction(1, 15)
        for forms in valid
    }
    assert sum(weights.values()) == 1
    assert all(
        sum(weight for forms, weight in weights.items() if form in forms)
        == Fraction(2, 3)
        for form in range(6)
    )

    rng = Random(12081208)
    values = [
        (x, y) for x in range(-1, 2) for y in range(-1, 2)
    ]
    box = [(x, y) for x in range(-5, 6) for y in range(-5, 6)]
    for _ in range(12):
        differences = {value for value in box if rng.randrange(4) == 0}
        centre_shift = rng.choice(values)
        second_shift = rng.choice(values)
        eta_shift = rng.choice(values)
        directions = (
            centre_shift,
            neg(add(linear(second_shift), rotate(centre_shift))),
            neg(linear(add(centre_shift, second_shift))),
            add(centre_shift, eta_shift),
            neg(add(second_shift, rotate(eta_shift))),
            neg(rotate(eta_shift)),
        )
        overlaps = [
            {
                start
                for start in differences
                if add(start, direction) in differences
            }
            for direction in directions
        ]
        count = 0
        for variables in product(values, repeat=4):
            outputs = linear_tracks(*variables)
            if all(output in overlap for output, overlap in zip(outputs, overlaps)):
                count += 1
        for forms in valid:
            assert count <= prod(
                len(overlaps[form]) for form in forms
            )
        assert count**3 <= prod(
            len(overlap) ** 2 for overlap in overlaps
        )


def audit_genuine_zero_controls() -> None:
    from analyze_swap_optimal_nested_cores import difference_set, profile
    from search_rotated_support import mian_chowla
    from verify_closed_fibre_q_height_layered_barrier import (
        lifted_residue_parabola,
    )

    families = (
        ([(mark, 0) for mark in mian_chowla(14)], "Golomb-14"),
        (lifted_residue_parabola(17), "lifted-parabola-17"),
    )
    for points, name in families:
        _, summary, _ = profile(difference_set(points), points)
        repeated = dict(
            summary["matching_projected_mixed_repeated_pair_cells"]
        )["same_centre_cross_difference_energy"]
        assert repeated[1] == 0, name
        assert repeated[6][0] == 0, name

    # Importing the certificate performs its own full exact audit and prints
    # a profile.  Silence that independent output here, then test the new
    # same-centre statistic on the certified point set.
    with redirect_stdout(StringIO()):
        from verify_high_codegree_transverse_equal_area_rank_flat_barrier import (
            POINTS as rank_flat_points,
        )

    _, summary, _ = profile(
        difference_set(rank_flat_points), rank_flat_points
    )
    repeated = dict(
        summary["matching_projected_mixed_repeated_pair_cells"]
    )["same_centre_cross_difference_energy"]
    assert repeated[1] == 0
    assert repeated[6][0] == 0


def main() -> None:
    audit_counts()
    audit_decomposition()
    audit_stored_stress()
    audit_support_collision_gate()
    audit_physical_invariant_barrier()
    audit_owner_switch_normal_form()
    audit_same_invariant_wedge_switch()
    audit_fractional_basis()
    audit_genuine_zero_controls()
    print("SWAP PHYSICAL-WEDGE DYADIC CARLESON GATE: PASS")


if __name__ == "__main__":
    main()
