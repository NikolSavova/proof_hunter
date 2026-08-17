#!/usr/bin/env python3
"""Exact countercertificate to weighted hinge and square-mesh regressions."""

from __future__ import annotations

import importlib.util
import sys
from decimal import Decimal, getcontext
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import log2
from pathlib import Path


HERE = Path(__file__).resolve().parent
GATE_PATH = HERE.parent / "agent_reflection_gate" / "reflection_order_gate.py"
SPEC = importlib.util.spec_from_file_location("weighted_hinge_false_gate", GATE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {GATE_PATH}")
gate = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = gate
SPEC.loader.exec_module(gate)


POINTS = ((0, -3), (1, -9003), (2, -8003), (3, -9003), (4, -2))
ROOTS = (
    (0, 1), (0, 2), (0, 3), (2, 3), (1, 3),
    (0, 4), (1, 2), (1, 4), (2, 4), (3, 4),
)
WORD = (0, 1, 2, 1, 0, 3, 1, 2, 1, 0)
SIZES = (4250, 1000, 1000, 1000, 1000)


def determinant(points, i: int, j: int, k: int) -> int:
    xi, yi = points[i]
    xj, yj = points[j]
    xk, yk = points[k]
    return (xj - xi) * (yk - yi) - (yj - yi) * (xk - xi)


def coordinate_roots(points):
    return tuple(sorted(
        combinations(range(len(points)), 2),
        key=lambda edge: Q(
            points[edge[1]][1] - points[edge[0]][1],
            points[edge[1]][0] - points[edge[0]][0],
        ),
    ))


def ln_interval(value: Q, terms: int = 90) -> tuple[Q, Q]:
    """Rigorous rational interval for the natural logarithm."""
    if value < 1:
        lower, upper = ln_interval(1 / value, terms)
        return -upper, -lower
    exponent = 0
    while value >= 2:
        value /= 2
        exponent += 1
    z = (value - 1) / (value + 1)

    def atanh_bounds(argument: Q) -> tuple[Q, Q]:
        total = Q(0)
        power = argument
        for index in range(terms):
            total += power / (2 * index + 1)
            power *= argument * argument
        lower = 2 * total
        tail = 2 * power / (
            (2 * terms + 1) * (1 - argument * argument)
        )
        return lower, lower + tail

    ln2_lower, ln2_upper = atanh_bounds(Q(1, 3))
    value_lower, value_upper = atanh_bounds(z)
    return (
        exponent * ln2_lower + value_lower,
        exponent * ln2_upper + value_upper,
    )


def log2_interval(value: Q) -> tuple[Q, Q]:
    numerator_lower, numerator_upper = ln_interval(value)
    denominator_lower, denominator_upper = ln_interval(Q(2))
    return (
        numerator_lower / denominator_upper,
        numerator_upper / denominator_lower,
    )


def interval_add(*values: tuple[Q, Q]) -> tuple[Q, Q]:
    return sum((value[0] for value in values), Q(0)), sum(
        (value[1] for value in values), Q(0)
    )


def interval_scale(scale: Q, value: tuple[Q, Q]) -> tuple[Q, Q]:
    if scale >= 0:
        return scale * value[0], scale * value[1]
    return scale * value[1], scale * value[0]


def interval_product(
    left: tuple[Q, Q], right: tuple[Q, Q]
) -> tuple[Q, Q]:
    candidates = tuple(
        a * b for a in left for b in right
    )
    return min(candidates), max(candidates)


def interval_square(value: tuple[Q, Q]) -> tuple[Q, Q]:
    assert value[0] >= 0
    return value[0] * value[0], value[1] * value[1]


def symbolic_profiles():
    # A pair (low, high) denotes low*log2(1001)+high*log2(4251).
    weights = ((0, 1),) + ((1, 0),) * 4
    cap = [(0, 0)] * 5
    cup = [(0, 0)] * 5
    low_log = log2_interval(Q(1001))
    high_log = log2_interval(Q(4251))

    def bounds(pair):
        return interval_add(
            interval_scale(Q(pair[0]), low_log),
            interval_scale(Q(pair[1]), high_log),
        )

    def add(left, right):
        return left[0] + right[0], left[1] + right[1]

    def maximum(left, right):
        left_bounds, right_bounds = bounds(left), bounds(right)
        if left_bounds[0] > right_bounds[1]:
            return left
        if right_bounds[0] > left_bounds[1]:
            return right
        assert left == right
        return left

    for i, j in ROOTS:
        old_cap_i, old_cap_j = cap[i], cap[j]
        old_cup_i, old_cup_j = cup[i], cup[j]
        cap[i] = maximum(old_cap_i, add(old_cap_j, weights[j]))
        cup[j] = maximum(old_cup_j, add(old_cup_i, weights[i]))
    return tuple(cap), tuple(cup)


def exact_log_certificates() -> tuple[tuple[Q, Q], tuple[Q, Q]]:
    log4250 = log2_interval(Q(4250))
    log1000 = log2_interval(Q(1000))
    log4251 = log2_interval(Q(4251))
    log1001 = log2_interval(Q(1001))
    high_jump = log2_interval(Q(33, 17))
    low_jump = log2_interval(Q(33, 4))
    log8250 = log2_interval(Q(8250))
    log5 = log2_interval(Q(5))

    target_numerator = interval_add(
        interval_scale(Q(4250), interval_product(log4250, high_jump)),
        interval_scale(Q(4000), interval_product(log1000, low_jump)),
    )
    target = interval_scale(Q(1, 8250), target_numerator)
    reward_numerator = interval_add(
        interval_scale(Q(12250), log1001),
        interval_scale(Q(4000), log4251),
    )
    reward = interval_scale(Q(1, 8250), reward_numerator)
    defect = target[0] - reward[1], target[1] - reward[0]
    assert defect[0] > Q(803, 100000)
    assert defect[1] < Q(201, 25000)  # 0.00804

    # The large child fails pointwise weighted hinge.
    high_target = interval_product(log4250, high_jump)
    assert high_target[0] > log1001[1]

    large_child_bank = interval_add(
        interval_scale(Q(1, 2), interval_square(log4250)), log1001
    )
    square_target = interval_add(
        interval_scale(Q(1, 2), interval_square(log8250)),
        interval_scale(Q(-1, 2), interval_square(log5)),
    )
    square_margin = (
        large_child_bank[0] - square_target[1],
        large_child_bank[1] - square_target[0],
    )
    assert square_margin[0] > Q(67, 100)
    return defect, square_margin


def nested_threshold_obstruction() -> None:
    points = ((0, 0), (1, -1), (2, -3), (3, 0))
    roots = coordinate_roots(points)
    assert roots == ((1, 2), (0, 2), (0, 1), (0, 3), (1, 3), (2, 3))
    assert gate.word_from_roots(4, roots) == (1, 0, 1, 2, 1, 0)
    assert min(
        abs(determinant(points, i, j, k))
        for i, j, k in combinations(range(4), 3)
    ) == 1
    edge_time = {edge: index for index, edge in enumerate(roots)}
    caps = []
    for length in range(1, 5):
        for support in combinations(range(4), length):
            if support[0] != 0:
                continue
            times = [
                edge_time[support[index], support[index + 1]]
                for index in range(length - 1)
            ]
            if all(times[index] > times[index + 1]
                   for index in range(len(times) - 1)):
                caps.append(support)
    full_maximum = max(map(len, caps))
    full_paths = tuple(path for path in caps if len(path) == full_maximum)
    assert full_paths == ((0, 1, 2),)
    high_set = {0, 3}
    high_caps = tuple(path for path in caps if set(path) <= high_set)
    assert max(map(len, high_caps)) == 2
    assert all(len(tuple(value for value in path if value in high_set)) == 1
               for path in full_paths)


def weighted_profiles_float(n: int, roots, sizes):
    weights = [log2(1 + value) for value in sizes]
    cap = [0.0] * n
    cup = [0.0] * n
    for i, j in roots:
        cap[i] = max(cap[i], cap[j] + weights[j])
        cup[j] = max(cup[j], cup[i] + weights[i])
    return cap, cup


def check_average_square(n: int, roots, sizes) -> bool:
    cap, cup = weighted_profiles_float(n, roots, sizes)
    total = sum(sizes)
    probabilities = [value / total for value in sizes]
    log_total = log2(total)
    average = sum(
        probabilities[i]
        * (0.5 * log2(sizes[i]) ** 2 + cap[i] + cup[i])
        for i in range(n)
    )
    target = 0.5 * log_total ** 2 - 0.5 * log2(n) ** 2
    assert average + 1e-10 >= target

    # The proved dyadic-bucket approximation to the pointwise square mesh.
    buckets: dict[int, int] = {}
    for size in sizes:
        exponent = size.bit_length() - 1
        buckets[exponent] = buckets.get(exponent, 0) + 1
    bucket_count = len(buckets)
    bucket_floor = (
        0.5
        * max(0.0, log_total - 1.0 - log2(bucket_count)) ** 2
        - 0.5 * log2(n) ** 2
    )
    pointwise = max(
        0.5 * log2(sizes[i]) ** 2 + cap[i] + cup[i]
        for i in range(n)
    )
    assert pointwise + 1e-10 >= bucket_floor

    # General bounded-range row theorem, equation (28).  This holds for
    # every row; the polynomial-imbalance hypothesis is needed only to sum
    # the row losses through an arbitrary-depth tree.
    q = log2(n)
    range_log = log2(max(sizes) / min(sizes))
    general_loss = 0.5 * q**2 + q * range_log
    assert average + 1e-10 >= 0.5 * log_total**2 - general_loss
    probabilities = [value / total for value in sizes]
    entropy = -sum(
        probability * log2(probability)
        for probability in probabilities
    )
    if range_log <= q:
        assert entropy + 1e-12 >= q - range_log

    # Proved factor-two averaged square theorem, equation (3b).
    balanced = max(sizes) <= 2 * min(sizes)
    if balanced:
        row_loss = 0.5 * log2(n) ** 2 + log2(n)
        assert average + 1e-10 >= 0.5 * log_total ** 2 - row_loss
        assert entropy + 1e-12 >= 0.5 * log2(n)
    return balanced


def arbitrary_n4_regression() -> tuple[int, int]:
    edges = tuple(combinations(range(4), 2))
    vectors = tuple(product((1, 2, 4, 16, 1024), repeat=4))
    count = 0
    balanced = 0
    for roots in permutations(edges):
        for sizes in vectors:
            balanced += check_average_square(4, roots, sizes)
            count += 1
    return count, balanced


def reflection_representatives(n: int):
    initial = gate.canonical_commutation_word(gate.bubble_word(n))
    seen = {initial}
    pending = [initial]
    answer = []
    while pending:
        word = pending.pop()
        answer.append(gate.root_sequence(n, word))
        for neighbor in gate.braid_neighbors_mod_commutation(n, word):
            if neighbor not in seen:
                seen.add(neighbor)
                pending.append(neighbor)
    return tuple(answer)


def reflection_n5_regression() -> tuple[int, int]:
    roots = reflection_representatives(5)
    assert len(roots) == 62
    vectors = tuple(
        tuple(1 << exponent for exponent in exponents)
        for exponents in product(range(7), repeat=5)
    )
    count = 0
    balanced = 0
    for row in roots:
        for sizes in vectors:
            balanced += check_average_square(5, row, sizes)
            count += 1
    return count, balanced


def main() -> None:
    assert coordinate_roots(POINTS) == ROOTS
    assert gate.root_sequence(5, WORD) == ROOTS
    determinants = [
        abs(determinant(POINTS, i, j, k))
        for i, j, k in combinations(range(5), 3)
    ]
    assert min(determinants) == 2000
    assert len({
        Q(POINTS[j][1] - POINTS[i][1], j - i)
        for i, j in combinations(range(5), 2)
    }) == 10

    cap, cup = symbolic_profiles()
    assert cap == ((1, 0), (2, 0), (1, 0), (1, 0), (0, 0))
    assert cup == ((0, 0), (0, 1), (1, 1), (1, 1), (2, 1))
    defect, square_margin = exact_log_certificates()
    nested_threshold_obstruction()
    arbitrary, arbitrary_balanced = arbitrary_n4_regression()
    reflection, reflection_balanced = reflection_n5_regression()

    getcontext().prec = 18
    decimal = lambda value: Decimal(value.numerator) / Decimal(value.denominator)
    print(
        "PASS: stretchable weighted-hinge counterexample; "
        f"defect=({decimal(defect[0])},{decimal(defect[1])}); "
        f"square_margin=({decimal(square_margin[0])},"
        f"{decimal(square_margin[1])}); "
        "nested_threshold_counter=n4; dyadic_bucket_square=PASS; "
        "factor_two_telescope=PASS; polynomial_range_telescope=PASS; "
        f"average_square_arbitrary_n4={arbitrary} "
        f"(balanced={arbitrary_balanced}); "
        f"average_square_reflection_n5={reflection} "
        f"(balanced={reflection_balanced})"
    )


if __name__ == "__main__":
    main()
