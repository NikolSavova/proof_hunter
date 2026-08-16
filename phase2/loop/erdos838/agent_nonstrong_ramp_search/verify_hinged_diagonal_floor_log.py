#!/usr/bin/env python3
"""Exact regression for the universal hinged diagonal Kraft theorem.

For an x-ordered point set, alpha(i) is the largest number of edges in a
cap whose left endpoint is i, and beta(i) is the largest number of edges in
a cup whose right endpoint is i.  The mathematical proof in the companion
report gives the stronger Kraft inequality

    sum_i 2**(-alpha(i)-beta(i)) <= 1,

and hence max_i(alpha(i) + beta(i)) >= ceil(log_2(n)).

This verifier checks four independent pieces of the accompanying audit:

* the older Pascal-cell floor-log arithmetic as a regression;
* every reflection-order commutation class through n=7;
* a sharp n=8 reduced-word certificate with hinged value 3; and
* an exact fixed-x integral realization of that certificate, cross-checked
  both by slope dynamic programming and direct subset enumeration.

For every tested order, the verifier explicitly constructs the prefix-free
profile words used in the proof and checks the pairwise slope witnesses.

All geometric predicates and slope comparisons are exact integers/Fractions.
"""

from __future__ import annotations

import importlib.util
import sys
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import ceil, comb, floor, log2
from pathlib import Path


HERE = Path(__file__).resolve().parent
GATE_PATH = HERE.parent / "agent_reflection_gate" / "reflection_order_gate.py"
SPEC = importlib.util.spec_from_file_location("reflection_order_gate_hinged", GATE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {GATE_PATH}")
gate = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = gate
SPEC.loader.exec_module(gate)


N8_WORD = (
    3, 4, 5, 4, 2, 1, 2, 0, 6, 1, 2, 5, 4, 3,
    2, 4, 3, 1, 2, 5, 0, 6, 4, 1, 3, 2, 5, 4,
)
N8_ROOTS = (
    (3, 4), (3, 5), (3, 6), (5, 6), (2, 4), (1, 4), (1, 2),
    (0, 4), (3, 7), (0, 2), (0, 1), (5, 7), (6, 7), (0, 7),
    (1, 7), (0, 6), (1, 6), (2, 7), (2, 6), (0, 5), (4, 7),
    (0, 3), (1, 5), (4, 6), (2, 5), (4, 5), (1, 3), (2, 3),
)
N8_Y = (0, -6857, -15714, 33429, -39429, 9714, 857, -6000)
N8_ALPHA = (3, 2, 2, 1, 2, 1, 1, 0)
N8_BETA = (0, 1, 1, 2, 1, 2, 2, 3)

N6_VARIABLE_WORD = (1, 0, 2, 1, 2, 3, 2, 1, 0, 1, 4, 3, 2, 1, 0)

EXPECTED_CLASS_DATA = {
    2: (1, {1: 1}),
    3: (2, {2: 2}),
    4: (8, {2: 3, 3: 5}),
    5: (62, {3: 46, 4: 16}),
    6: (908, {3: 325, 4: 517, 5: 66}),
    7: (24698, {3: 2132, 4: 16206, 5: 6008, 6: 352}),
}


def endpoint_ranks(n: int, roots) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Longest monotone-slope endpoint paths, in one chronological sweep."""
    alpha = [0] * n
    beta = [0] * n
    for i, j in roots:
        # The old values must be read before either assignment.  In fact the
        # two updates touch different coordinates, but spelling this out also
        # records the temporal-path recurrence used in the report.
        old_ai, old_aj = alpha[i], alpha[j]
        old_bi, old_bj = beta[i], beta[j]
        alpha[i] = max(old_ai, old_aj + 1)
        beta[j] = max(old_bj, old_bi + 1)
    return tuple(alpha), tuple(beta)


def profile_codes(n: int, roots):
    """Construct the mixed endpoint-threshold code at every vertex.

    ``cup_last[i][r-1]`` is the least edge time that can be the last edge
    of an r-edge increasing path ending at i.  ``cap_first[i][r-1]`` is the
    least edge time that can be the first edge of an r-edge decreasing path
    starting at i.  Both are recorded at the first chronological activation
    of the corresponding dynamic-programming rank.
    """
    roots = tuple(roots)
    alpha = [0] * n
    beta = [0] * n
    cup_last = [[] for _ in range(n)]
    cap_first = [[] for _ in range(n)]
    for time, (i, j) in enumerate(roots):
        old_ai, old_aj = alpha[i], alpha[j]
        old_bi, old_bj = beta[i], beta[j]

        # Every shorter path exists by taking a suffix/prefix of a longest
        # one.  Since times are swept increasingly, the first activation is
        # exactly the minimum possible terminal/initial edge time.
        while len(cup_last[j]) < old_bi + 1:
            cup_last[j].append(time)
        while len(cap_first[i]) < old_aj + 1:
            cap_first[i].append(time)

        alpha[i] = max(old_ai, old_aj + 1)
        beta[j] = max(old_bj, old_bi + 1)

    assert all(len(cup_last[i]) == beta[i] for i in range(n))
    assert all(len(cap_first[i]) == alpha[i] for i in range(n))
    words = []
    for i in range(n):
        tagged = [(time, 0) for time in cup_last[i]]
        tagged += [(time, 1) for time in cap_first[i]]
        tagged.sort()
        words.append(tuple(tag for _, tag in tagged))
    return (
        tuple(alpha), tuple(beta),
        tuple(tuple(row) for row in cup_last),
        tuple(tuple(row) for row in cap_first),
        tuple(words),
    )


def verify_prefix_code(n: int, roots) -> tuple[tuple[int, ...], ...]:
    """Check every local threshold witness and global prefix relation."""
    roots = tuple(roots)
    position = {edge: time for time, edge in enumerate(roots)}
    assert len(position) == n * (n - 1) // 2
    alpha, beta, cup_last, cap_first, words = profile_codes(n, roots)
    assert (alpha, beta) == endpoint_ranks(n, roots)
    assert all(len(words[i]) == alpha[i] + beta[i] for i in range(n))
    sentinel = len(roots) + 1

    for i, j in combinations(range(n), 2):
        edge_time = position[i, j]
        x = next(
            (r for r, value in enumerate(cup_last[i], 1) if value > edge_time),
            len(cup_last[i]) + 1,
        )
        y = next(
            (r for r, value in enumerate(cap_first[j], 1) if value > edge_time),
            len(cap_first[j]) + 1,
        )
        ui_x = cup_last[i][x - 1] if x <= len(cup_last[i]) else sentinel
        dj_y = cap_first[j][y - 1] if y <= len(cap_first[j]) else sentinel

        # Append ij to an (x-1)-edge cup ending at i, and prepend it to a
        # (y-1)-edge cap starting at j.  These are the two extension steps in
        # the proof.
        assert ui_x > edge_time
        assert dj_y > edge_time
        assert x <= len(cup_last[j])
        assert y <= len(cap_first[i])
        assert cup_last[j][x - 1] <= edge_time
        assert cap_first[i][y - 1] <= edge_time

        common_length = x + y - 1
        assert common_length <= len(words[i])
        assert common_length <= len(words[j])
        prefix_i = words[i][:common_length]
        prefix_j = words[j][:common_length]
        assert prefix_i.count(0) <= x - 1 and prefix_i.count(1) >= y
        assert prefix_j.count(0) >= x and prefix_j.count(1) <= y - 1
        assert prefix_i != prefix_j

        # The displayed witness is stronger than a bare inequality: neither
        # complete word can be a prefix of the other.
        assert words[i][:len(words[j])] != words[j]
        assert words[j][:len(words[i])] != words[i]

    kraft_sum = sum(Q(1, 2 ** len(word)) for word in words)
    assert kraft_sum <= 1
    assert max(map(len, words)) >= ceil(log2(n)) if n > 1 else True
    return words


def determinant(i: int, j: int, k: int) -> int:
    return (j - i) * (N8_Y[k] - N8_Y[i]) - (k - i) * (N8_Y[j] - N8_Y[i])


def coordinate_slope_order():
    return tuple(sorted(
        combinations(range(8), 2),
        key=lambda edge: Q(
            N8_Y[edge[1]] - N8_Y[edge[0]], edge[1] - edge[0]
        ),
    ))


def direct_coordinate_ranks() -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Enumerate all subsets; no path-DP assumptions enter this check."""
    alpha = [0] * 8
    beta = [0] * 8
    for mask in range(1, 1 << 8):
        support = tuple(i for i in range(8) if mask >> i & 1)
        signs = tuple(determinant(i, j, k) for i, j, k in combinations(support, 3))
        if all(value < 0 for value in signs):
            alpha[support[0]] = max(alpha[support[0]], len(support) - 1)
        if all(value > 0 for value in signs):
            beta[support[-1]] = max(beta[support[-1]], len(support) - 1)
    return tuple(alpha), tuple(beta)


def verify_pascal_arithmetic() -> None:
    """Check the finite summation and floor-log inversion used in the proof."""
    for h in range(65):
        cell_sum = sum(comb(p + q, p) for p in range(h + 1) for q in range(h + 1 - p))
        assert cell_sum == 2 ** (h + 1) - 1
    for n in range(1, 1 << 16):
        least_h = next(h for h in range(32) if n <= 2 ** (h + 1) - 1)
        assert least_h == floor(log2(n))


def exhaustive_reflection_classes() -> tuple[dict[int, Counter[int]], dict[int, int]]:
    """One representative per commutation class; disjoint roots commute."""
    answer = {}
    kraft_equalities = {}
    for n, (expected_count, expected_histogram) in EXPECTED_CLASS_DATA.items():
        initial = gate.canonical_commutation_word(gate.bubble_word(n))
        queue = [initial]
        seen = {initial}
        histogram: Counter[int] = Counter()
        equality_count = 0
        for word in queue:
            roots = gate.root_sequence(n, word)
            alpha, beta = endpoint_ranks(n, roots)
            words = verify_prefix_code(n, roots)
            h = max(a + b for a, b in zip(alpha, beta))
            histogram[h] += 1
            assert h >= ceil(log2(n))
            kraft_sum = sum(
                Q(1, 2 ** len(code)) for code in words
            )
            assert kraft_sum <= 1
            equality_count += kraft_sum == 1

            # Every exact rank cell obeys the cups-caps binomial capacity.
            rank_cells = Counter(zip(alpha, beta))
            for (p, q), multiplicity in rank_cells.items():
                assert multiplicity <= comb(p + q, p)

            for neighbor in gate.braid_neighbors_mod_commutation(n, word):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        assert len(seen) == expected_count
        assert histogram == Counter(expected_histogram)
        answer[n] = histogram
        kraft_equalities[n] = equality_count
    return answer, kraft_equalities


def exhaustive_arbitrary_n4() -> int:
    """The theorem is edge-order, not reflection-order, specific."""
    edges = tuple(combinations(range(4), 2))
    count = 0
    for roots in permutations(edges):
        verify_prefix_code(4, roots)
        count += 1
    assert count == 720
    return count


def two_state_cycle_mean(rows, coordinate: int) -> Q:
    """Maximum cycle mean after maximizing parallel edges."""
    matrix = [[None, None], [None, None]]
    for source, row in enumerate(rows):
        for target, alpha, beta in row:
            value = (alpha, beta, alpha + beta)[coordinate]
            old = matrix[source][target]
            matrix[source][target] = value if old is None else max(old, value)
    candidates = []
    if matrix[0][0] is not None:
        candidates.append(Q(matrix[0][0]))
    if matrix[1][1] is not None:
        candidates.append(Q(matrix[1][1]))
    if matrix[0][1] is not None and matrix[1][0] is not None:
        candidates.append(Q(matrix[0][1] + matrix[1][0], 2))
    return max(candidates)


def verify_variable_arity_spectral_example():
    """Exact sharp regression for the Markov/Kraft spectral step.

    The two geometric rows have arities three and six.  Their transition
    count matrix [[2,1],[4,2]] has Perron root four.  The profile lengths
    make both row Kraft sums, the Parry entropy, and the maximum length-cycle
    inequality exact.
    """
    roots3 = gate.root_sequence(3, (0, 1, 0))
    alpha3, beta3 = endpoint_ranks(3, roots3)
    assert tuple(a + b for a, b in zip(alpha3, beta3)) == (1, 2, 2)
    # The unique length-one position goes to state 1; the others go to 0.
    targets3 = (1, 0, 0)
    row0 = tuple(
        (targets3[i], alpha3[i], beta3[i]) for i in range(3)
    )

    roots6 = gate.root_sequence(6, N6_VARIABLE_WORD)
    alpha6, beta6 = endpoint_ranks(6, roots6)
    assert tuple(a + b for a, b in zip(alpha6, beta6)) == (2, 2, 3, 3, 3, 3)
    # The two length-two positions go to state 1; the others go to 0.
    targets6 = (1, 1, 0, 0, 0, 0)
    row1 = tuple(
        (targets6[i], alpha6[i], beta6[i]) for i in range(6)
    )
    rows = (row0, row1)

    assert [Counter(target for target, _, _ in row) for row in rows] == [
        Counter({0: 2, 1: 1}), Counter({0: 4, 1: 2})
    ]
    assert all(
        sum(Q(1, 2 ** (alpha + beta)) for _, alpha, beta in row) == 1
        for row in rows
    )

    # M(1,2)^T = 4(1,2)^T.  Individual-edge Parry probabilities are
    # r_target/(4*r_source); both aggregate transition rows are (1/2,1/2),
    # so the stationary vertex law is also (1/2,1/2).
    right = (Q(1), Q(2))
    stationary = (Q(1, 2), Q(1, 2))
    entropy = Q(0)
    expected_length = Q(0)
    for source, row in enumerate(rows):
        for target, alpha, beta in row:
            probability = right[target] / (4 * right[source])
            assert probability.numerator == 1
            information = probability.denominator.bit_length() - 1
            assert probability.denominator == 2 ** information
            edge_mass = stationary[source] * probability
            entropy += edge_mass * information
            expected_length += edge_mass * (alpha + beta)
    assert entropy == expected_length == 2

    length_mean = two_state_cycle_mean(rows, 2)
    cap_mean = two_state_cycle_mean(rows, 0)
    cup_mean = two_state_cycle_mean(rows, 1)
    assert length_mean == entropy == 2
    assert cap_mean + cup_mean >= length_mean
    return 4, entropy, length_mean, cap_mean, cup_mean


def verify_n8_sharp_stretchable() -> tuple[int, int]:
    assert gate.root_sequence(8, N8_WORD) == N8_ROOTS
    alpha, beta = endpoint_ranks(8, N8_ROOTS)
    assert alpha == N8_ALPHA and beta == N8_BETA
    assert tuple(a + b for a, b in zip(alpha, beta)) == (3,) * 8
    assert sum(Q(1, 2 ** (a + b)) for a, b in zip(alpha, beta)) == 1

    triple_determinants = [
        determinant(i, j, k) for i, j, k in combinations(range(8), 3)
    ]
    assert all(triple_determinants)
    minimum_margin = min(map(abs, triple_determinants))
    assert minimum_margin == 2000

    geometric_roots = coordinate_slope_order()
    # A fixed-x realization need only agree modulo swaps of disjoint roots.
    # Such swaps commute in the endpoint DP, and the direct support audit below
    # independently checks the geometric cap/cup meanings.
    geometric_alpha, geometric_beta = endpoint_ranks(8, geometric_roots)
    assert (geometric_alpha, geometric_beta) == (alpha, beta)
    codes = verify_prefix_code(8, geometric_roots)
    assert set(codes) == {
        tuple(int(bit) for bit in f"{value:03b}") for value in range(8)
    }
    assert direct_coordinate_ranks() == (alpha, beta)
    assert gate.canonical_commutation_word(
        gate.word_from_roots(8, geometric_roots)
    ) == gate.canonical_commutation_word(N8_WORD)
    return max(a + b for a, b in zip(alpha, beta)), minimum_margin


def main() -> None:
    verify_pascal_arithmetic()
    arbitrary_count = exhaustive_arbitrary_n4()
    spectral = verify_variable_arity_spectral_example()
    histograms, kraft_equalities = exhaustive_reflection_classes()
    n8_h, margin = verify_n8_sharp_stretchable()
    compact = {n: dict(sorted(hist.items())) for n, hist in histograms.items()}
    print(
        "PASS: universal hinged Kraft regression; "
        f"arbitrary_n4_edge_orders={arbitrary_count}; "
        f"variable_arity=(rho,entropy,length_cycle,cap_cycle,cup_cycle)={spectral}; "
        f"reflection_histograms={compact}; "
        f"kraft_equality_classes={kraft_equalities}; "
        f"n8_stretchable_h={n8_h}; n8_min_determinant={margin}; "
        "n8_kraft_sum=1"
    )


if __name__ == "__main__":
    main()
