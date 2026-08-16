#!/usr/bin/env python3
"""Exact full-spectrum and finite-grammar audit for a nonstrong 8-point macro.

The certificate has three logically independent parts.

1. It proves that the integral order type is not obtainable from singleton
   leaves by recursive strong composition, even after allowing either mirror
   orientation at every node and every one of the 8! leaf orders.
2. It exhausts all 56 oriented generic projection chambers, computes exact
   cap/cup profiles and endpoint rewards, and certifies the local diagonal
   reward floor max_i(alpha_i+beta_i) >= 4 in every chamber.
3. It checks a two-state recursive vertical grammar attaining cap and cup
   maximum cycle means (2,2), runs its exact integer C,U,W recurrence, and
   exhausts all strongly connected two-state grammars after lossless
   edge-signature compression.  Reducible grammars end in a one-state sink,
   whose optimum is checked separately.

Only integer/Fraction arithmetic is used for predicates and recurrences.
Floating point appears only in the final human-readable normalized ratios.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, permutations
from math import log2


Point = tuple[int, int]
Order = tuple[int, ...]


POINTS: tuple[Point, ...] = tuple(
    (i, y)
    for i, y in enumerate(
        (-4_375_003, -2_375_766, -3_908_671, -5_825_945,
         7_932_585, 7_351_545, -2_562_156, -3_105_652)
    )
)

# The sharp two-state grammar.  Labels are state indices in macro order.
GRAMMAR_ORDERS: tuple[Order, Order] = (
    (0, 1, 2, 4, 5, 3, 6, 7),
    (7, 6, 3, 5, 4, 2, 1, 0),
)
GRAMMAR_LABELS: tuple[tuple[int, ...], tuple[int, ...]] = (
    (1, 1, 1, 0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 0, 0, 0),
)


def det(a: Point, b: Point, c: Point) -> int:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def ordered_det(a: int, b: int, c: int) -> int:
    return det(POINTS[a], POINTS[b], POINTS[c])


def projection_orders() -> tuple[Order, ...]:
    """All oriented chambers of functionals x+s*y, exactly."""
    critical = sorted(
        {-Q(POINTS[j][0] - POINTS[i][0],
            POINTS[j][1] - POINTS[i][1])
         for i, j in combinations(range(8), 2)}
    )
    assert len(critical) == 28  # no parallel pair directions
    probes = [critical[0] - 1]
    probes.extend((a + b) / 2 for a, b in zip(critical, critical[1:]))
    probes.append(critical[-1] + 1)
    answer: list[Order] = []
    seen: set[Order] = set()
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


def half_hull(indices, reverse: bool = False) -> list[int]:
    answer: list[int] = []
    iterable = reversed(indices) if reverse else indices
    for i in iterable:
        while (len(answer) >= 2
               and ordered_det(answer[-2], answer[-1], i) <= 0):
            answer.pop()
        answer.append(i)
    return answer


def hull_size(indices: tuple[int, ...]) -> int:
    if len(indices) <= 2:
        return len(indices)
    ordered = tuple(sorted(indices, key=lambda i: POINTS[i]))
    return len(half_hull(ordered)[:-1] + half_hull(ordered, True)[:-1])


def supports(order: Order):
    """Return cap, cup, convex supports as tuples of macro positions."""
    caps = []
    cups = []
    convex = []
    for mask in range(1, 1 << 8):
        positions = tuple(i for i in range(8) if mask >> i & 1)
        labels = tuple(order[i] for i in positions)
        signs = tuple(
            ordered_det(labels[i], labels[j], labels[k])
            for i, j, k in combinations(range(len(labels)), 3)
        )
        if all(value < 0 for value in signs):
            caps.append(positions)
        if all(value > 0 for value in signs):
            cups.append(positions)
        if hull_size(labels) == len(labels):
            convex.append(positions)
    return tuple(caps), tuple(cups), tuple(convex)


def profile(order: Order):
    caps, cups, convex = supports(order)
    alpha = [0] * 8
    beta = [0] * 8
    for support in caps:
        alpha[support[0]] = max(alpha[support[0]], len(support) - 1)
    for support in cups:
        beta[support[-1]] = max(beta[support[-1]], len(support) - 1)
    return (
        len(caps), len(cups), len(convex),
        max(alpha) + 1, max(beta) + 1,
        tuple(alpha), tuple(beta),
    )


def is_strongly_decomposable() -> tuple[bool, int]:
    """Exhaust every leaf order and both mirror signs at every split."""

    @lru_cache(None)
    def decomposes(order: Order) -> bool:
        if len(order) <= 1:
            return True
        for cut in range(1, len(order)):
            left, right = order[:cut], order[cut:]
            for first_sign in (-1, 1):
                left_rule = all(
                    (1 if ordered_det(a, b, c) > 0 else -1) == first_sign
                    for a, b in combinations(left, 2)
                    for c in right
                )
                right_rule = all(
                    (1 if ordered_det(a, b, c) > 0 else -1) == -first_sign
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


def edge_maxima(rewards, labels):
    """Maximum parallel-edge reward for each of the four state edges."""
    out = [[None, None], [None, None]]
    for state in range(2):
        for position, target in enumerate(labels[state]):
            value = rewards[state][position]
            old = out[state][target]
            out[state][target] = value if old is None else max(old, value)
    return tuple(tuple(row) for row in out)


def two_state_cycle_mean(matrix) -> Q:
    candidates = []
    if matrix[0][0] is not None:
        candidates.append(Q(matrix[0][0]))
    if matrix[1][1] is not None:
        candidates.append(Q(matrix[1][1]))
    if matrix[0][1] is not None and matrix[1][0] is not None:
        candidates.append(Q(matrix[0][1] + matrix[1][0], 2))
    return max(candidates)


def compressed_subsets(alpha, beta):
    """Lossless signatures for a nonempty cross-edge position subset."""
    rows = {}
    for mask in range(1, 1 << 8):
        complement = 255 ^ mask
        signature = (
            max(alpha[i] for i in range(8) if mask >> i & 1),
            max(beta[i] for i in range(8) if mask >> i & 1),
            max((alpha[i] for i in range(8) if complement >> i & 1),
                default=-99),
            max((beta[i] for i in range(8) if complement >> i & 1),
                default=-99),
        )
        rows.setdefault(signature, mask)
    return tuple(rows.items())


def exhaustive_two_state_optimum(rows) -> tuple[Q, tuple]:
    """All chart pairs and all binary label maps, after exact compression."""
    signatures = [compressed_subsets(row[5], row[6]) for row in rows]
    best = Q(100)
    witness = None
    for first in range(56):
        for second in range(56):
            for x, xmask in signatures[first]:
                for y, ymask in signatures[second]:
                    cap_mean = max(Q(x[0] + y[0], 2), Q(x[2]), Q(y[2]))
                    cup_mean = max(Q(x[1] + y[1], 2), Q(x[3]), Q(y[3]))
                    value = cap_mean + cup_mean
                    if value < best:
                        best = value
                        witness = (first, second, xmask, ymask,
                                   cap_mean, cup_mean)
    assert witness is not None
    return best, witness


def exact_grammar_recurrence(grammar_supports, depth: int = 12):
    caps = [1, 1]
    cups = [1, 1]
    faces = [1, 1]
    records = []
    for d in range(1, depth + 1):
        child_size = 8 ** (d - 1)
        new_caps = []
        new_cups = []
        new_faces = []
        for state in range(2):
            labels = GRAMMAR_LABELS[state]
            macro_caps, macro_cups, macro_faces = grammar_supports[state]
            new_caps.append(sum(
                caps[labels[support[0]]] * child_size ** (len(support) - 1)
                for support in macro_caps
            ))
            new_cups.append(sum(
                cups[labels[support[-1]]] * child_size ** (len(support) - 1)
                for support in macro_cups
            ))
            new_faces.append(
                sum(faces[labels[i]] for i in range(8))
                + sum(
                    caps[labels[support[0]]]
                    * cups[labels[support[-1]]]
                    * child_size ** (len(support) - 2)
                    for support in macro_faces if len(support) >= 2
                )
            )
        caps, cups, faces = new_caps, new_cups, new_faces
        assert caps[0] == cups[1] and caps[1] == cups[0]
        assert faces[0] == faces[1]
        records.append({
            "depth": d,
            "size": 8 ** d,
            "cap_bits_ratio": log2(caps[0]) / (3 * d) ** 2,
            "cup_bits_ratio": log2(cups[0]) / (3 * d) ** 2,
            "face_bits_ratio": log2(faces[0]) / (3 * d) ** 2,
        })
    return records


def main() -> None:
    determinants = [
        abs(ordered_det(i, j, k))
        for i, j, k in combinations(range(8), 3)
    ]
    assert min(determinants) == 384_369

    decomposable, checked_subproblems = is_strongly_decomposable()
    assert not decomposable
    assert checked_subproblems >= 40_320

    orders = projection_orders()
    rows = [profile(order) for order in orders]
    assert GRAMMAR_ORDERS[0] == orders[28]
    assert GRAMMAR_ORDERS[1] == orders[29]
    assert {row[2] for row in rows} == {145}
    assert len({(row[0], row[1]) for row in rows}) == 47
    assert Counter((row[3], row[4]) for row in rows) == Counter({
        (4, 4): 36, (5, 4): 6, (4, 5): 6,
        (4, 3): 3, (3, 4): 3, (3, 5): 1, (5, 3): 1,
    })
    diagonal = [max(a + b for a, b in zip(row[5], row[6]))
                for row in rows]
    assert Counter(diagonal) == Counter({4: 48, 5: 8})

    grammar_rows = [profile(order) for order in GRAMMAR_ORDERS]
    assert [(row[0], row[1]) for row in grammar_rows] == [(82, 57), (57, 82)]
    cap_matrix = edge_maxima(
        tuple(row[5] for row in grammar_rows), GRAMMAR_LABELS)
    cup_matrix = edge_maxima(
        tuple(row[6] for row in grammar_rows), GRAMMAR_LABELS)
    assert cap_matrix == ((2, 3), (1, 2))
    assert cup_matrix == ((2, 1), (3, 2))
    assert two_state_cycle_mean(cap_matrix) == 2
    assert two_state_cycle_mean(cup_matrix) == 2

    optimum, two_state_witness = exhaustive_two_state_optimum(rows)
    assert optimum == 4
    assert two_state_witness[:4] == (28, 29, 7, 224)
    one_state_optimum = min(
        max(row[5]) + max(row[6])
        for row in rows
    )
    assert one_state_optimum == 5

    grammar_supports = tuple(supports(order) for order in GRAMMAR_ORDERS)
    records = exact_grammar_recurrence(grammar_supports)
    assert records[0]["size"] == 8 and records[-1]["size"] == 8 ** 12
    assert records[-1]["face_bits_ratio"] < Q(2, 3)
    assert abs(records[-1]["face_bits_ratio"] - 2 / 3) < 0.002

    print(
        "PASS: nonstrong integral n=8 macro; "
        f"leaf_orders=40320; ordered_subproblems={checked_subproblems}; "
        f"chambers={len(orders)}; "
        "profiles=47; rank_hist="
        f"{dict(sorted(Counter((r[3], r[4]) for r in rows).items()))}; "
        "diagonal_floor=4; exact finite-grammar optimum=4; "
        f"one_state_optimum={one_state_optimum}; "
        "sharp cycle means=(2,2); coefficient=2/3; "
        f"depth12_ratio={records[-1]['face_bits_ratio']:.12f}"
    )


if __name__ == "__main__":
    main()
