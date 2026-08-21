#!/usr/bin/env python3
"""Verify the fixed-invariant local-owner support barrier."""

from __future__ import annotations

from itertools import combinations
from random import Random

Point = tuple[int, int]
Form = dict[int, int]
FormalPoint = tuple[Form, Form]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def neg(value: Point) -> Point:
    return -value[0], -value[1]


def sub(left: Point, right: Point) -> Point:
    return add(left, neg(right))


def rotate(value: Point) -> Point:
    return -value[1], value[0]


def linear(value: Point) -> Point:
    return add(value, rotate(value))


def form_add(*forms: Form) -> Form:
    result: Form = {}
    for form in forms:
        for variable, coefficient in form.items():
            result[variable] = result.get(variable, 0) + coefficient
    return {variable: value for variable, value in result.items() if value}


def form_neg(form: Form) -> Form:
    return {variable: -coefficient for variable, coefficient in form.items()}


def vector_add(*vectors: FormalPoint) -> FormalPoint:
    return (
        form_add(*(vector[0] for vector in vectors)),
        form_add(*(vector[1] for vector in vectors)),
    )


def vector_neg(vector: FormalPoint) -> FormalPoint:
    return form_neg(vector[0]), form_neg(vector[1])


def vector_sub(left: FormalPoint, right: FormalPoint) -> FormalPoint:
    return vector_add(left, vector_neg(right))


def vector_rotate(vector: FormalPoint) -> FormalPoint:
    return form_neg(vector[1]), vector[0]


def vector_linear(vector: FormalPoint) -> FormalPoint:
    return vector_add(vector, vector_rotate(vector))


def formal_variable(index: int) -> FormalPoint:
    return {2 * index: 1}, {2 * index + 1: 1}


def formal_constant(value: Point) -> FormalPoint:
    return ({-1: value[0]} if value[0] else {}), (
        {-1: value[1]} if value[1] else {}
    )


def formal_tracks(
    physical_v: FormalPoint,
    physical_w: FormalPoint,
    first_displacement: FormalPoint,
    second_displacement: FormalPoint,
    eta: FormalPoint,
    q_value: FormalPoint,
) -> tuple[FormalPoint, ...]:
    return (
        vector_sub(vector_sub(physical_v, first_displacement), q_value),
        vector_add(
            vector_sub(physical_w, vector_linear(second_displacement)),
            vector_rotate(vector_add(q_value, first_displacement)),
        ),
        vector_add(
            vector_sub(physical_w, vector_linear(second_displacement)),
            vector_rotate(q_value),
            vector_linear(first_displacement),
        ),
        vector_add(
            vector_sub(vector_sub(physical_v, first_displacement), q_value),
            eta,
        ),
        vector_add(
            vector_sub(physical_w, second_displacement),
            vector_rotate(vector_sub(q_value, eta)),
        ),
        vector_add(physical_w, vector_rotate(vector_sub(q_value, eta))),
    )


def squared_norm_polynomial(
    vector: FormalPoint,
) -> tuple[tuple[tuple[int, int], int], ...]:
    coefficients: dict[tuple[int, int], int] = {}
    for coordinate in vector:
        items = sorted(coordinate.items())
        for first_position, (first_variable, first_value) in enumerate(items):
            for second_variable, second_value in items[first_position:]:
                key = first_variable, second_variable
                coefficients[key] = coefficients.get(key, 0) + (
                    first_value
                    * second_value
                    * (1 if first_variable == second_variable else 2)
                )
    return tuple(
        sorted((key, value) for key, value in coefficients.items() if value)
    )


def formal_points(blocks: int) -> list[FormalPoint]:
    points: list[FormalPoint] = []
    next_variable = 0
    invariant = formal_constant((1, 0))
    for _ in range(blocks):
        variables = [
            formal_variable(next_variable + index) for index in range(26)
        ]
        next_variable += 26
        (
            physical_point,
            physical_v,
            first_displacement,
            second_displacement,
            eta,
            first_q,
            second_q,
            third_q,
            *bases,
        ) = variables
        physical_w = vector_sub(invariant, vector_rotate(physical_v))
        points.extend(
            (
                physical_point,
                vector_add(physical_point, physical_v),
                vector_add(physical_point, physical_w),
            )
        )
        tracks = []
        for q_value in (first_q, second_q, third_q):
            tracks.extend(
                formal_tracks(
                    physical_v,
                    physical_w,
                    first_displacement,
                    second_displacement,
                    eta,
                    q_value,
                )
            )
        assert len(bases) == len(tracks) == 18
        for base, track in zip(bases, tracks):
            points.extend((base, vector_add(base, track)))
    return points


def audit_symbolic_coefficients() -> None:
    points = formal_points(4)
    squared_distances = {
        squared_norm_polynomial(vector_sub(first, second))
        for first, second in combinations(points, 2)
    }
    assert len(points) == 156
    assert len(squared_distances) == len(points) * (len(points) - 1) // 2


def integer_tracks(
    physical_v: Point,
    physical_w: Point,
    first_displacement: Point,
    second_displacement: Point,
    eta: Point,
    q_value: Point,
) -> tuple[Point, ...]:
    return (
        sub(sub(physical_v, first_displacement), q_value),
        add(
            sub(physical_w, linear(second_displacement)),
            rotate(add(q_value, first_displacement)),
        ),
        add(
            add(
                sub(physical_w, linear(second_displacement)),
                rotate(q_value),
            ),
            linear(first_displacement),
        ),
        add(sub(sub(physical_v, first_displacement), q_value), eta),
        add(
            sub(physical_w, second_displacement),
            rotate(sub(q_value, eta)),
        ),
        add(physical_w, rotate(sub(q_value, eta))),
    )


def build_integer_certificate(
    blocks: int = 4, seed: int = 1208, radius: int = 1_000_000
) -> tuple[list[Point], list[tuple[object, ...]]]:
    rng = Random(seed)
    invariant = (17, 11)
    points: list[Point] = []
    records = []

    def random_point() -> Point:
        return (
            rng.randrange(-radius, radius + 1),
            rng.randrange(-radius, radius + 1),
        )

    for _ in range(blocks):
        physical_point = random_point()
        physical_v = random_point()
        first_displacement = random_point()
        second_displacement = random_point()
        eta = random_point()
        parameter_triangle = (
            random_point(),
            random_point(),
            random_point(),
        )
        physical_w = sub(invariant, rotate(physical_v))
        points.extend(
            (
                physical_point,
                add(physical_point, physical_v),
                add(physical_point, physical_w),
            )
        )
        all_tracks = []
        for q_value in parameter_triangle:
            all_tracks.extend(
                integer_tracks(
                    physical_v,
                    physical_w,
                    first_displacement,
                    second_displacement,
                    eta,
                    q_value,
                )
            )
        for track in all_tracks:
            base = random_point()
            points.extend((base, add(base, track)))
        records.append(
            (
                physical_v,
                first_displacement,
                second_displacement,
                eta,
                parameter_triangle,
                tuple(all_tracks),
            )
        )
    return points, records


def audit_integer_certificate() -> None:
    points, records = build_integer_certificate()
    assert len(points) == 156 and len(set(points)) == 156
    squared_distances = []
    for first, second in combinations(points, 2):
        difference = sub(first, second)
        squared_distances.append(
            difference[0] * difference[0] + difference[1] * difference[1]
        )
    assert len(set(squared_distances)) == len(squared_distances) == 12090

    triangles = set()
    for (
        physical_v,
        first_displacement,
        second_displacement,
        eta,
        parameter_triangle,
        tracks,
    ) in records:
        physical_w = sub((17, 11), rotate(physical_v))
        assert add(rotate(physical_v), physical_w) == (17, 11)
        assert len(tracks) == 18
        recomputed_tracks = tuple(
            track
            for q_value in parameter_triangle
            for track in integer_tracks(
                physical_v,
                physical_w,
                first_displacement,
                second_displacement,
                eta,
                q_value,
            )
        )
        assert tracks == recomputed_tracks
        assert len(set(parameter_triangle)) == 3
        first_side = sub(parameter_triangle[1], parameter_triangle[0])
        second_side = sub(parameter_triangle[2], parameter_triangle[0])
        assert (
            first_side[0] * second_side[1]
            - first_side[1] * second_side[0]
        ) != 0
        triangles.add(tuple(sorted(parameter_triangle)))
    assert len(triangles) == 4


def main() -> None:
    audit_symbolic_coefficients()
    audit_integer_certificate()
    print("COARSE INVARIANT POINTWISE OWNER SUPPORT BARRIER: PASS")


if __name__ == "__main__":
    main()
