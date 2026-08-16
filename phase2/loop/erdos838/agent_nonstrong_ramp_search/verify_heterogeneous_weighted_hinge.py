#!/usr/bin/env python3
"""Verifier for HETEROGENEOUS_WEIGHTED_HINGE_BARRIER.md."""

from __future__ import annotations

import importlib.util
import sys
from decimal import Decimal, getcontext
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, permutations, product
from math import log2
from pathlib import Path


HERE = Path(__file__).resolve().parent
GATE_PATH = HERE.parent / "agent_reflection_gate" / "reflection_order_gate.py"
SPEC = importlib.util.spec_from_file_location("weighted_hinge_gate", GATE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {GATE_PATH}")
gate = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = gate
SPEC.loader.exec_module(gate)


Y = (
    611_223, -321_380, -883_444, -152_693,
    -406_855, -230_093, -115_174, 791_471,
)
POINTS = tuple((i, y) for i, y in enumerate(Y))
ROOTS = (
    (0, 1), (0, 2), (1, 2), (0, 3), (0, 4), (3, 4), (0, 5),
    (0, 6), (3, 5), (1, 4), (3, 6), (1, 5), (0, 7), (1, 6),
    (1, 3), (5, 6), (4, 6), (4, 5), (1, 7), (2, 6), (2, 5),
    (3, 7), (2, 4), (2, 7), (4, 7), (5, 7), (2, 3), (6, 7),
)


def det(a: int, b: int, c: int) -> int:
    xa, ya = POINTS[a]
    xb, yb = POINTS[b]
    xc, yc = POINTS[c]
    return (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa)


def coordinate_roots() -> tuple[tuple[int, int], ...]:
    return tuple(sorted(
        combinations(range(8), 2),
        key=lambda edge: Q(Y[edge[1]] - Y[edge[0]], edge[1] - edge[0]),
    ))


def is_strongly_decomposable() -> tuple[bool, int]:
    @lru_cache(None)
    def decomposes(order: tuple[int, ...]) -> bool:
        if len(order) <= 1:
            return True
        for cut in range(1, len(order)):
            left, right = order[:cut], order[cut:]
            for first_sign in (-1, 1):
                left_rule = all(
                    (1 if det(a, b, c) > 0 else -1) == first_sign
                    for a, b in combinations(left, 2)
                    for c in right
                )
                right_rule = all(
                    (1 if det(a, b, c) > 0 else -1) == -first_sign
                    for a in left
                    for b, c in combinations(right, 2)
                )
                if (left_rule and right_rule
                        and decomposes(left) and decomposes(right)):
                    return True
        return False

    witness = next(
        (order for order in permutations(range(8)) if decomposes(order)),
        None,
    )
    return witness is not None, decomposes.cache_info().currsize


def ln_interval(value: Q, terms: int = 80) -> tuple[Q, Q]:
    """Rigorous rational interval for ln(value), value >= 1."""
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
        for k in range(terms):
            total += power / (2 * k + 1)
            power *= argument * argument
        lower = 2 * total
        tail = 2 * power / ((2 * terms + 1) * (1 - argument * argument))
        return lower, lower + tail

    ln2_lower, ln2_upper = atanh_bounds(Q(1, 3))
    y_lower, y_upper = atanh_bounds(z)
    return (
        exponent * ln2_lower + y_lower,
        exponent * ln2_upper + y_upper,
    )


def log2_interval(value: Q) -> tuple[Q, Q]:
    numerator_lower, numerator_upper = ln_interval(value)
    denominator_lower, denominator_upper = ln_interval(Q(2))
    return (
        numerator_lower / denominator_upper,
        numerator_upper / denominator_lower,
    )


def pair_add(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] + right[0], left[1] + right[1]


def pair_bounds(value: tuple[int, int], log129: tuple[Q, Q]) -> tuple[Q, Q]:
    integer, coefficient = value
    if coefficient >= 0:
        return (
            integer + coefficient * log129[0],
            integer + coefficient * log129[1],
        )
    return (
        integer + coefficient * log129[1],
        integer + coefficient * log129[0],
    )


def pair_max(
    left: tuple[int, int],
    right: tuple[int, int],
    log129: tuple[Q, Q],
) -> tuple[int, int]:
    left_bounds = pair_bounds(left, log129)
    right_bounds = pair_bounds(right, log129)
    if left_bounds[0] > right_bounds[1]:
        return left
    if right_bounds[0] > left_bounds[1]:
        return right
    assert left == right
    return left


def symbolic_weighted_profiles() -> tuple[
    tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]
]:
    # A pair (a,b) denotes a + b*log2(129). Position zero has weight
    # log2(129); the seven singleton children have weight one.
    weights = ((0, 1),) + ((1, 0),) * 7
    cap = [(0, 0)] * 8
    cup = [(0, 0)] * 8
    log129 = log2_interval(Q(129))
    for i, j in ROOTS:
        old_cap_i, old_cap_j = cap[i], cap[j]
        old_cup_i, old_cup_j = cup[i], cup[j]
        cap[i] = pair_max(
            old_cap_i, pair_add(old_cap_j, weights[j]), log129
        )
        cup[j] = pair_max(
            old_cup_j, pair_add(old_cup_i, weights[i]), log129
        )
    return tuple(cap), tuple(cup)


def certify_counterexample() -> tuple[Q, Q]:
    log129 = log2_interval(Q(129))
    log135 = log2_interval(Q(135))
    h = (log135[0] - Q(896, 135), log135[1] - Q(896, 135))
    reward = (
        (Q(150) + 7 * log129[0]) / 135,
        (Q(150) + 7 * log129[1]) / 135,
    )
    exact_offset = Q(896, 135)

    # c_* = offset - reward / h.
    c_lower = exact_offset - reward[1] / h[0]
    c_upper = exact_offset - reward[0] / h[1]
    assert c_lower > Q(3283, 1000)
    assert c_upper < Q(821, 250)  # 3.284

    # Directly certify failure at c=3.
    assert h[0] * (exact_offset - 3) - reward[1] > 0
    return c_lower, c_upper


def weighted_profiles_float(
    n: int,
    roots,
    sizes: tuple[int, ...],
) -> tuple[list[float], list[float]]:
    weights = [log2(1 + value) for value in sizes]
    cap = [0.0] * n
    cup = [0.0] * n
    for i, j in roots:
        old_cap_i, old_cap_j = cap[i], cap[j]
        old_cup_i, old_cup_j = cup[i], cup[j]
        cap[i] = max(old_cap_i, old_cap_j + weights[j])
        cup[j] = max(old_cup_j, old_cup_i + weights[i])
    return cap, cup


def check_wh(n: int, roots, sizes: tuple[int, ...]) -> None:
    cap, cup = weighted_profiles_float(n, roots, sizes)
    total = sum(sizes)
    probabilities = [value / total for value in sizes]
    lhs = sum(
        probabilities[i] * (cap[i] + cup[i]) for i in range(n)
    )
    rhs = sum(
        probabilities[i]
        * log2(sizes[i])
        * log2(total / sizes[i])
        for i in range(n)
    )
    assert lhs + 1e-10 >= rhs

    log_total = log2(total)
    square_mesh = max(
        0.5 * log2(sizes[i]) ** 2 + cap[i] + cup[i]
        for i in range(n)
    )
    assert square_mesh + 1e-10 >= (
        0.5 * log_total ** 2 - 0.5 * log2(n) ** 2
    )


def arbitrary_n4_regression() -> int:
    edges = tuple(combinations(range(4), 2))
    vectors = tuple(product((1, 2, 4, 16, 1024), repeat=4))
    count = 0
    for roots in permutations(edges):
        for sizes in vectors:
            check_wh(4, roots, sizes)
            count += 1
    return count


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


def reflection_n5_regression() -> int:
    roots = reflection_representatives(5)
    assert len(roots) == 62
    vectors = tuple(
        tuple(1 << exponent for exponent in exponents)
        for exponents in product(range(7), repeat=5)
    )
    count = 0
    for row in roots:
        for sizes in vectors:
            check_wh(5, row, sizes)
            count += 1
    return count


def projection_orders() -> tuple[tuple[int, ...], ...]:
    critical = sorted({
        -Q(POINTS[j][0] - POINTS[i][0], POINTS[j][1] - POINTS[i][1])
        for i, j in combinations(range(8), 2)
    })
    probes = [critical[0] - 1]
    probes.extend((a + b) / 2 for a, b in zip(critical, critical[1:]))
    probes.append(critical[-1] + 1)
    answer = []
    seen = set()
    for slope in probes:
        order = tuple(sorted(
            range(8),
            key=lambda i: Q(POINTS[i][0]) + slope * POINTS[i][1],
        ))
        for candidate in (order, order[::-1]):
            if candidate not in seen:
                seen.add(candidate)
                answer.append(candidate)
    assert len(answer) == 56
    return tuple(answer)


def supports(order: tuple[int, ...]):
    caps = []
    cups = []
    for mask in range(1, 1 << 8):
        positions = tuple(i for i in range(8) if mask >> i & 1)
        labels = tuple(order[i] for i in positions)
        signs = tuple(
            det(labels[i], labels[j], labels[k])
            for i, j, k in combinations(range(len(labels)), 3)
        )
        if all(value < 0 for value in signs):
            caps.append(positions)
        if all(value > 0 for value in signs):
            cups.append(positions)
    return tuple(caps), tuple(cups)


def nonstrong_regression() -> int:
    count = 0
    for order in projection_orders():
        caps, cups = supports(order)
        for distinguished in range(8):
            for exponent in range(1, 21):
                sizes = [1] * 8
                sizes[distinguished] = 1 << exponent
                weights = [log2(1 + value) for value in sizes]
                cap_reward = [0.0] * 8
                cup_reward = [0.0] * 8
                for support in caps:
                    cap_reward[support[0]] = max(
                        cap_reward[support[0]],
                        sum(weights[j] for j in support[1:]),
                    )
                for support in cups:
                    cup_reward[support[-1]] = max(
                        cup_reward[support[-1]],
                        sum(weights[j] for j in support[:-1]),
                    )
                total = sum(sizes)
                probabilities = [value / total for value in sizes]
                lhs = sum(
                    probabilities[i] * (cap_reward[i] + cup_reward[i])
                    for i in range(8)
                )
                rhs = sum(
                    probabilities[i]
                    * log2(sizes[i])
                    * log2(total / sizes[i])
                    for i in range(8)
                )
                assert lhs + 1e-10 >= rhs
                mesh = max(
                    0.5 * log2(sizes[i]) ** 2
                    + cap_reward[i] + cup_reward[i]
                    for i in range(8)
                )
                assert mesh + 1e-10 >= (
                    0.5 * log2(total) ** 2 - 4.5
                )
                count += 1
    return count


def martingale_tree_regression() -> int:
    """Audit the exact defect/second-moment telescope on fixed trees."""
    leaf = None
    pair = (leaf, leaf)
    triple = (leaf, leaf, leaf)
    skew = leaf
    trees = [pair, triple]
    for arity in (2, 4, 3, 5, 2, 3):
        skew = (skew,) + (leaf,) * (arity - 1)
        trees.append(skew)
    trees.extend(((pair, leaf, triple), (skew, pair, triple, leaf)))

    def audit(tree) -> tuple[int, float, float, float]:
        if tree is None:
            return 1, 0.0, 0.0, 0.0
        children = [audit(child) for child in tree]
        sizes = tuple(item[0] for item in children)
        arity = len(sizes)
        edges = list(combinations(range(arity), 2))
        if edges:
            shift = sum(sizes) % len(edges)
            edges = edges[shift:] + edges[:shift]
            if sum(value * value for value in sizes) % 2:
                edges.reverse()
        cap, cup = weighted_profiles_float(arity, edges, sizes)
        rewards = [cap[i] + cup[i] for i in range(arity)]
        total = sum(sizes)
        probabilities = [value / total for value in sizes]
        log_total = log2(total)
        child_logs = [log2(value) for value in sizes]
        jumps = [log_total - value for value in child_logs]
        local_target = sum(
            probabilities[i] * child_logs[i] * jumps[i]
            for i in range(arity)
        )
        average_reward = sum(
            probabilities[i] * rewards[i] for i in range(arity)
        )
        defect = max(local_target - average_reward, 0.0)
        square_jump = sum(
            probabilities[i] * jumps[i] ** 2 for i in range(arity)
        )
        assert abs(
            local_target
            - 0.5 * (
                log_total ** 2
                - sum(
                    probabilities[i] * child_logs[i] ** 2
                    for i in range(arity)
                )
                - square_jump
            )
        ) < 1e-10
        energy = max(
            children[i][1] + rewards[i] for i in range(arity)
        )
        expected_square_sum = square_jump + sum(
            probabilities[i] * children[i][2] for i in range(arity)
        )
        expected_defect_sum = defect + sum(
            probabilities[i] * children[i][3] for i in range(arity)
        )
        lower_bound = (
            0.5 * log_total ** 2
            - 0.5 * expected_square_sum
            - expected_defect_sum
        )
        assert energy + 1e-10 >= lower_bound
        return total, energy, expected_square_sum, expected_defect_sum

    for tree in trees:
        audit(tree)
    return len(trees)


def main() -> None:
    determinants = [
        abs(det(i, j, k)) for i, j, k in combinations(range(8), 3)
    ]
    assert min(determinants) == 1430
    assert coordinate_roots() == ROOTS
    assert gate.verify_fixed_x(8, ROOTS, tuple(Q(y) for y in Y))

    decomposable, states = is_strongly_decomposable()
    assert not decomposable
    assert states >= 40_320

    cap, cup = symbolic_weighted_profiles()
    assert cap == (
        (1, 0), (2, 0), (3, 0), (1, 0),
        (2, 0), (1, 0), (1, 0), (0, 0),
    )
    assert cup == (
        (0, 0), (0, 1), (1, 1), (2, 1),
        (2, 1), (2, 1), (2, 1), (3, 1),
    )
    c_lower, c_upper = certify_counterexample()

    martingale_trees = martingale_tree_regression()
    n4 = arbitrary_n4_regression()
    n5 = reflection_n5_regression()
    nonstrong = nonstrong_regression()
    getcontext().prec = 20
    print(
        "PASS: heterogeneous weighted-hinge barrier; "
        f"c_interval=({Decimal(c_lower.numerator) / Decimal(c_lower.denominator)},"
        f"{Decimal(c_upper.numerator) / Decimal(c_upper.denominator)}); "
        f"decomposition_states={states}; martingale_trees={martingale_trees}; "
        f"arbitrary_n4={n4}; "
        f"reflection_n5={n5}; nonstrong_weight_vectors={nonstrong}"
    )


if __name__ == "__main__":
    main()
