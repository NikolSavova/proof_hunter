#!/usr/bin/env python3
"""Checks completion-corner inversion across every metric resonance."""

from __future__ import annotations

from itertools import product
from math import gcd
import random

from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rotate,
    subtract,
)


Point = tuple[int, int]


def dot(first: Point, second: Point) -> int:
    return first[0] * second[0] + first[1] * second[1]


def det(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def norm(value: Point) -> int:
    return dot(value, value)


def scale(coefficient: int, value: Point) -> Point:
    return coefficient * value[0], coefficient * value[1]


def gap(start: Point, displacement: Point) -> int:
    return norm(add(start, displacement)) - norm(start)


def solve_two_projections(
    first_direction: Point,
    first_value: int,
    second_direction: Point,
    second_value: int,
) -> Point:
    determinant = det(first_direction, second_direction)
    assert determinant
    x_numerator = first_value * second_direction[1] - (
        first_direction[1] * second_value
    )
    y_numerator = first_direction[0] * second_value - (
        first_value * second_direction[0]
    )
    assert x_numerator % determinant == 0
    assert y_numerator % determinant == 0
    return x_numerator // determinant, y_numerator // determinant


def recover_case_one(
    p: Point,
    ell: Point,
    gamma: Point,
    u: Point,
    g2: int,
    h2: int,
) -> Point:
    b_value = add(ell, rotate(p))
    c_gamma = (g2 - norm(gamma)) // 2
    c_ju = (norm(u) - h2) // 2
    c_value = solve_two_projections(gamma, c_gamma, rotate(u), c_ju)
    return subtract(c_value, b_value)


def recover_case_two(
    q: Point,
    w_value: Point,
    beta: Point,
    u: Point,
    g1: int,
    h1: int,
) -> Point:
    c_value = add(w_value, rotate(q))
    b_beta = (g1 - norm(beta)) // 2
    b_ju = (norm(u) - h1) // 2
    b_value = solve_two_projections(beta, b_beta, rotate(u), b_ju)
    return subtract(c_value, b_value)


def verify_random_inversions() -> None:
    rng = random.Random(12082026)
    case_one = case_two = 0
    for _ in range(50000):
        s = rng.randrange(-10, 11), rng.randrange(-10, 11)
        d = rng.randrange(-10, 11), rng.randrange(-10, 11)
        u = rng.randrange(-10, 11), rng.randrange(-10, 11)
        if d == (0, 0) or u == (0, 0):
            continue
        gamma = subtract(
            (-rotate(s)[0], -rotate(s)[1]),
            linear(d),
        )
        beta = (-rotate(add(s, d))[0], -rotate(add(s, d))[1])
        c = rng.randrange(-20, 21), rng.randrange(-20, 21)
        ell = rng.randrange(-20, 21), rng.randrange(-20, 21)
        q = rng.randrange(-15, 16), rng.randrange(-15, 16)
        t = rng.randrange(-15, 16), rng.randrange(-15, 16)
        p = add(q, t)
        a_value = subtract(c, q)
        b_value = add(ell, rotate(p))
        c_value = add(b_value, t)
        w_value = add(ell, linear(t))
        assert c_value == add(w_value, rotate(q))
        g1, h1 = gap(b_value, beta), gap(b_value, (-rotate(u)[0], -rotate(u)[1]))
        g2, h2 = gap(c_value, gamma), gap(c_value, (-rotate(u)[0], -rotate(u)[1]))

        if dot(gamma, u):
            recovered = recover_case_one(p, ell, gamma, u, g2, h2)
            assert recovered == t
            assert abs(4 * det(gamma, rotate(u))) == 4 * abs(dot(gamma, u))
            case_one += 1
        elif det(add(s, d), u):
            recovered = recover_case_two(q, w_value, beta, u, g1, h1)
            assert recovered == t
            assert abs(4 * det(beta, rotate(u))) == 4 * abs(det(add(s, d), u))
            case_two += 1
    assert case_one > 10000 and case_two > 100


def verify_resonance_intersections() -> None:
    for u in product(range(-3, 4), repeat=2):
        if u == (0, 0):
            continue
        for s in product(range(-4, 5), repeat=2):
            for d in product(range(-4, 5), repeat=2):
                if d == (0, 0):
                    continue
                gamma = subtract(
                    (-rotate(s)[0], -rotate(s)[1]),
                    linear(d),
                )
                q_resonance = det(s, u) == 0
                p_resonance = det(add(s, d), u) == 0
                d_resonance = dot(gamma, u) == 0
                assert not (q_resonance and p_resonance and d_resonance)
                if q_resonance and p_resonance:
                    assert det(d, u) == 0
                if q_resonance and d_resonance:
                    assert det(d, linear(u)) == 0
                if p_resonance and d_resonance:
                    assert dot(d, u) == 0


def verify_case_three_two_to_one() -> None:
    rng = random.Random(57721566)
    for _ in range(20000):
        u = rng.randrange(-10, 11), rng.randrange(-10, 11)
        if u == (0, 0):
            continue
        c = rng.randrange(-20, 21), rng.randrange(-20, 21)
        t = rng.randrange(-20, 21), rng.randrange(-20, 21)
        projection = dot(t, rotate(u))
        metric_label = norm(add(c, t))
        content = gcd(abs(u[0]), abs(u[1]))
        primitive = u[0] // content, u[1] // content
        candidates = []
        for coefficient in range(-100, 101):
            trial = add(t, scale(coefficient, primitive))
            if dot(trial, rotate(u)) != projection:
                continue
            if norm(add(c, trial)) == metric_label:
                candidates.append(trial)
        assert t in candidates
        assert len(candidates) <= 2


def main() -> None:
    verify_random_inversions()
    verify_resonance_intersections()
    verify_case_three_two_to_one()
    print("SWAP RESONANCE COMPLETION-CORNER METRIC INVERSION: PASS")


if __name__ == "__main__":
    main()
