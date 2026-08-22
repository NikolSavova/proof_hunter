#!/usr/bin/env python3
"""Exact checks for SWAP_SELECTED_CORE_K24_CROSS_SUM_NORMAL_FORM.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product


Point = tuple[int, int]
TrackTuple = tuple[Point, Point, Point, Point, Point, Point]
StarKey = tuple[Point, Point, Point, Point]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def negate(point: Point) -> Point:
    return -point[0], -point[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def linear(point: Point) -> Point:
    return point[0] - point[1], point[0] + point[1]


def tracks(
    v_value: Point,
    w_value: Point,
    a_value: Point,
    b_value: Point,
    e_value: Point,
    q_value: Point,
) -> TrackTuple:
    """The six literal D-tracks of one physical-wedge occurrence."""

    return (
        subtract(subtract(v_value, a_value), q_value),
        add(
            subtract(w_value, linear(b_value)),
            add(rotate(q_value), rotate(a_value)),
        ),
        add(
            subtract(w_value, linear(b_value)),
            add(rotate(q_value), linear(a_value)),
        ),
        add(
            subtract(subtract(v_value, a_value), q_value),
            e_value,
        ),
        add(
            subtract(w_value, b_value),
            subtract(rotate(q_value), rotate(e_value)),
        ),
        add(w_value, subtract(rotate(q_value), rotate(e_value))),
    )


def full_table(values: TrackTuple) -> tuple[Point, ...]:
    return tuple(
        add(values[column], rotate(values[row]))
        for row in (0, 3)
        for column in (1, 2, 4, 5)
    )


def star_key(values: TrackTuple) -> StarKey:
    table = full_table(values)
    return table[0], table[1], table[2], table[3]


def recover(key: StarKey) -> tuple[Point, Point, Point, Point]:
    """Recover (R,a,b,e) from the first K_{2,4} row."""

    z1, z2, z4, z5 = key
    a_value = subtract(z2, z1)
    b_value = subtract(z5, z4)
    e_value = add(
        subtract(b_value, a_value),
        rotate(subtract(z4, z1)),
    )
    r_value = add(z1, linear(b_value))
    return r_value, a_value, b_value, e_value


def expected_table(
    r_value: Point,
    a_value: Point,
    b_value: Point,
    e_value: Point,
) -> tuple[Point, ...]:
    first_row = (
        subtract(r_value, linear(b_value)),
        add(subtract(r_value, linear(b_value)), a_value),
        subtract(
            subtract(r_value, b_value),
            rotate(add(a_value, e_value)),
        ),
        subtract(r_value, rotate(add(a_value, e_value))),
    )
    row_shift = rotate(e_value)
    return first_row + tuple(add(value, row_shift) for value in first_row)


def reconstruct_from_key(key: StarKey, first_track: Point) -> TrackTuple:
    _, _, _, e_value = recover(key)
    z1, z2, z4, z5 = key
    return (
        first_track,
        subtract(z1, rotate(first_track)),
        subtract(z2, rotate(first_track)),
        add(first_track, e_value),
        subtract(z4, rotate(first_track)),
        subtract(z5, rotate(first_track)),
    )


def squared_distance_sidon(points: list[Point]) -> bool:
    distances = [
        (left[0] - right[0]) ** 2 + (left[1] - right[1]) ** 2
        for left, right in combinations(points, 2)
    ]
    return len(distances) == len(set(distances))


def difference_endpoint_map(points: list[Point]) -> dict[Point, tuple[Point, Point]]:
    output: dict[Point, tuple[Point, Point]] = {}
    for head in points:
        for tail in points:
            if head == tail:
                continue
            value = subtract(head, tail)
            assert value not in output
            output[value] = head, tail
    return output


def cross_sum_inverse(points: list[Point]) -> dict[Point, tuple[Point, Point]]:
    output: dict[Point, tuple[Point, Point]] = {}
    for first in points:
        for second in points:
            value = add(first, rotate(second))
            assert value not in output
            output[value] = first, second
    return output


Gaussian = tuple[Fraction, Fraction]


def gaussian(real: int = 0, imaginary: int = 0) -> Gaussian:
    return Fraction(real), Fraction(imaginary)


def gadd(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gsubtract(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] - right[0], left[1] - right[1]


def gmultiply(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def ginverse(value: Gaussian) -> Gaussian:
    denominator = value[0] * value[0] + value[1] * value[1]
    assert denominator
    return value[0] / denominator, -value[1] / denominator


def gaussian_rank(matrix: list[list[Gaussian]]) -> int:
    rows = [list(row) for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next(
            (
                index
                for index in range(rank, len(rows))
                if rows[index][column] != gaussian()
            ),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = ginverse(rows[rank][column])
        rows[rank] = [gmultiply(value, inverse) for value in rows[rank]]
        for index in range(len(rows)):
            if index == rank or rows[index][column] == gaussian():
                continue
            factor = rows[index][column]
            rows[index] = [
                gsubtract(value, gmultiply(factor, pivot_value))
                for value, pivot_value in zip(rows[index], rows[rank])
            ]
        rank += 1
    return rank


def check_basis_classification() -> None:
    one = gaussian(1)
    imaginary = gaussian(0, 1)
    linear_coefficient = gaussian(1, 1)
    rows = {
        "01": [one, gaussian(), gmultiply(gaussian(-1), linear_coefficient), gaussian()],
        "02": [one, one, gmultiply(gaussian(-1), linear_coefficient), gaussian()],
        "04": [one, gmultiply(gaussian(-1), imaginary), gaussian(-1), gmultiply(gaussian(-1), imaginary)],
        "05": [one, gmultiply(gaussian(-1), imaginary), gaussian(), gmultiply(gaussian(-1), imaginary)],
        "31": [one, gaussian(), gmultiply(gaussian(-1), linear_coefficient), imaginary],
        "32": [one, one, gmultiply(gaussian(-1), linear_coefficient), imaginary],
        "34": [one, gmultiply(gaussian(-1), imaginary), gaussian(-1), gaussian()],
        "35": [one, gmultiply(gaussian(-1), imaginary), gaussian(), gaussian()],
    }
    invalid = {
        ("01", "02", "31", "32"),
        ("01", "02", "34", "35"),
        ("01", "04", "31", "34"),
        ("01", "05", "31", "35"),
        ("02", "04", "32", "34"),
        ("02", "05", "32", "35"),
        ("04", "05", "34", "35"),
    }
    observed = {
        subset
        for subset in combinations(rows, 4)
        if gaussian_rank([rows[name] for name in subset]) < 4
    }
    assert observed == invalid
    assert len(list(combinations(rows, 4))) - len(observed) == 63


def check_symbolic_normal_form() -> None:
    samples = (
        ((3, -2), (7, 5), (-1, 4), (2, -3), (5, 1)),
        ((-8, 11), (4, -9), (6, 2), (-7, 3), (1, -5)),
    )
    parameters = ((0, 0), (2, -1), (-3, 5), (7, 4))
    for v_value, w_value, a_value, b_value, e_value in samples:
        r_value = add(rotate(v_value), w_value)
        tables = []
        track_rows = []
        for q_value in parameters:
            values = tracks(
                v_value,
                w_value,
                a_value,
                b_value,
                e_value,
                q_value,
            )
            table = full_table(values)
            assert table == expected_table(
                r_value, a_value, b_value, e_value
            )
            assert recover(star_key(values)) == (
                r_value,
                a_value,
                b_value,
                e_value,
            )
            assert reconstruct_from_key(star_key(values), values[0]) == values
            tables.append(table)
            track_rows.append(values)
        assert len(set(tables)) == 1
        for first, second in combinations(track_rows, 2):
            shift = subtract(second[0], first[0])
            assert subtract(second[3], first[3]) == shift
            for role in (1, 2, 4, 5):
                assert subtract(second[role], first[role]) == negate(
                    rotate(shift)
                )


def check_endpoint_anchor(points: list[Point]) -> None:
    for endpoint in points:
        for first_sign in (-1, 1):
            for second_sign in (-1, 1):
                fibres: dict[Point, tuple[Point, Point]] = {}
                for first_other in points:
                    if first_other == endpoint:
                        continue
                    for second_other in points:
                        if second_other == endpoint:
                            continue
                        first_edge = subtract(endpoint, first_other)
                        second_edge = subtract(endpoint, second_other)
                        if first_sign < 0:
                            first_edge = negate(first_edge)
                        if second_sign < 0:
                            second_edge = negate(second_edge)
                        invariant = add(rotate(first_edge), second_edge)
                        previous = fibres.setdefault(
                            invariant, (first_edge, second_edge)
                        )
                        assert previous == (first_edge, second_edge)


def positive_e(positive: tuple[Point, Point, Point, Point]) -> Point:
    first, second, fourth, fifth = positive
    a_value = subtract(second, first)
    b_value = subtract(fifth, fourth)
    return add(
        subtract(b_value, a_value),
        rotate(subtract(fourth, first)),
    )


def positive_parameters(
    positive: tuple[Point, Point, Point, Point]
) -> tuple[Point, Point, Point, Point]:
    first, second, fourth, fifth = positive
    a_value = subtract(second, first)
    b_value = subtract(fifth, fourth)
    e_value = positive_e(positive)
    displacement = rotate(subtract(b_value, add(a_value, e_value)))
    assert fourth == add(first, displacement)
    assert fifth == add(add(first, displacement), b_value)
    return a_value, b_value, e_value, first


def diagonal_shift(
    positive: tuple[Point, Point, Point, Point], shift: Point
) -> tuple[Point, Point, Point, Point]:
    return tuple(add(value, shift) for value in positive)  # type: ignore[return-value]


def check_genuine_cross_sum_and_coloured_energy(points: list[Point]) -> None:
    assert squared_distance_sidon(points)
    endpoint_map = difference_endpoint_map(points)
    psi_inverse = cross_sum_inverse(points)
    differences = set(endpoint_map)

    positive_by_e: dict[
        Point, set[tuple[Point, Point, Point, Point]]
    ] = defaultdict(set)
    positive_by_parameters: dict[
        tuple[Point, Point, Point], set[Point]
    ] = defaultdict(set)
    for positive in product(differences, repeat=4):
        positive_by_e[positive_e(positive)].add(positive)
        a_value, b_value, e_value, first = positive_parameters(positive)
        positive_by_parameters[a_value, b_value, e_value].add(first)

    key_records: dict[
        StarKey,
        list[tuple[Point, tuple[Point, Point, Point, Point], Point]],
    ] = defaultdict(list)
    for e_value, positives in positive_by_e.items():
        negative = {
            first_track
            for first_track in differences
            if add(first_track, e_value) in differences
        }
        for first_track in negative:
            for positive in positives:
                key = tuple(
                    add(value, rotate(first_track)) for value in positive
                )
                key_records[key].append((first_track, positive, e_value))

    # Every key is a complete synchronized-copy invariant.  Its row
    # representations in P-P invert to the original four endpoint pairs.
    for key, records in key_records.items():
        recovered_e = recover(key)[3]
        row_representation_sets = [set() for _ in range(4)]
        for first_track, positive, e_value in records:
            assert e_value == recovered_e
            values = reconstruct_from_key(key, first_track)
            assert (values[1], values[2], values[4], values[5]) == positive
            for column_index, role in enumerate((1, 2, 4, 5)):
                first_head, first_tail = endpoint_map[values[0]]
                other_head, other_tail = endpoint_map[values[role]]
                head_value = add(other_head, rotate(first_head))
                tail_value = add(other_tail, rotate(first_tail))
                assert subtract(head_value, tail_value) == key[column_index]
                assert psi_inverse[head_value] == (other_head, first_head)
                assert psi_inverse[tail_value] == (other_tail, first_tail)
                row_representation_sets[column_index].add(
                    (head_value, tail_value)
                )
        assert all(
            len(representations) == len(records)
            for representations in row_representation_sets
        )

    factorial_second = sum(
        load * (load - 1) for load in map(len, key_records.values())
    )
    factorial_third = sum(
        load * (load - 1) * (load - 2)
        for load in map(len, key_records.values())
    )

    # Lossless coloured diagonal-correlation identities.  The colour e is
    # essential: replacing the positive diagonal correlation by four
    # independent D-overlaps is a strict overcount even in this 4-point set.
    second_correlation = 0
    third_correlation = 0
    for e_value, positives in positive_by_e.items():
        negative = [
            first_track
            for first_track in differences
            if add(first_track, e_value) in differences
        ]
        for first, second in product(negative, repeat=2):
            if first == second:
                continue
            shift = negate(rotate(subtract(second, first)))
            second_correlation += sum(
                diagonal_shift(positive, shift) in positives
                for positive in positives
            )
        for first, second, third in product(negative, repeat=3):
            if len({first, second, third}) < 3:
                continue
            first_shift = negate(rotate(subtract(second, first)))
            second_shift = negate(rotate(subtract(third, first)))
            third_correlation += sum(
                diagonal_shift(positive, first_shift) in positives
                and diagonal_shift(positive, second_shift) in positives
                for positive in positives
            )
    assert factorial_second == second_correlation
    assert factorial_third == third_correlation

    # Stronger three-colour decomposition.  For fixed (a,b,e), the four
    # positive tracks are determined by their first member y in one
    # fourfold intersection P_{a,b,e}.  The key is then determined by the
    # single cross-sum colour z=y+Jf with f in S_e.
    refined_loads: Counter[tuple[Point, Point, Point, Point]] = Counter()
    refined_second = 0
    refined_third = 0
    for (a_value, b_value, e_value), positive_starts in (
        positive_by_parameters.items()
    ):
        negative_starts = {
            first_track
            for first_track in differences
            if add(first_track, e_value) in differences
        }
        displacement = rotate(subtract(b_value, add(a_value, e_value)))
        for first_track in negative_starts:
            for positive_start in positive_starts:
                z_value = add(positive_start, rotate(first_track))
                refined_loads[a_value, b_value, e_value, z_value] += 1
                expected_key = (
                    z_value,
                    add(z_value, a_value),
                    add(z_value, displacement),
                    add(add(z_value, displacement), b_value),
                )
                assert recover(expected_key)[1:] == (
                    a_value,
                    b_value,
                    e_value,
                )
        for first, second in product(negative_starts, repeat=2):
            if first == second:
                continue
            shift = negate(rotate(subtract(second, first)))
            refined_second += sum(
                add(positive_start, shift) in positive_starts
                for positive_start in positive_starts
            )
        for first, second, third in product(negative_starts, repeat=3):
            if len({first, second, third}) < 3:
                continue
            first_shift = negate(rotate(subtract(second, first)))
            second_shift = negate(rotate(subtract(third, first)))
            refined_third += sum(
                add(positive_start, first_shift) in positive_starts
                and add(positive_start, second_shift) in positive_starts
                for positive_start in positive_starts
            )

    assert Counter(
        {
            (*recover(key)[1:], key[0]): len(records)
            for key, records in key_records.items()
        }
    ) == refined_loads
    assert sum(load * (load - 1) for load in refined_loads.values()) == (
        factorial_second
    )
    assert sum(
        load * (load - 1) * (load - 2)
        for load in refined_loads.values()
    ) == factorial_third
    assert refined_second == factorial_second
    assert refined_third == factorial_third

    overlap = Counter(
        subtract(second, first)
        for first in differences
        for second in differences
    )
    anonymous_second = sum(
        overlap[shift] ** 2 * overlap[rotate(shift)] ** 4
        for shift in overlap
        if shift != (0, 0)
    )
    assert anonymous_second > factorial_second

    histogram = Counter(map(len, key_records.values()))
    assert histogram == Counter({1: 14008, 2: 86, 3: 4})
    assert (factorial_second, factorial_third, anonymous_second) == (
        196,
        24,
        3688,
    )


def main() -> None:
    points = [(0, 0), (1, 0), (0, 2), (3, 4)]
    check_basis_classification()
    check_symbolic_normal_form()
    check_endpoint_anchor(points)
    check_genuine_cross_sum_and_coloured_energy(points)
    print("selected-core K2,4 cross-sum normal form: PASS")


if __name__ == "__main__":
    main()
