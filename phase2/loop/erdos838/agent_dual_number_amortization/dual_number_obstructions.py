#!/usr/bin/env python3
"""Exact certificates for the dual-number braid-amortization attack on 838.

The two main checks are deliberately independent in scale:

* an exhaustive six-wire commutation-class census certifies the exposure
  obstruction at a genuine global lexicographic minimum;
* one direct ten-wire long braid certifies failure of half-weight monotonicity
  while retaining value and derivative boundary vectors.

All partition-function and boundary calculations use Python integers.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT838 = HERE.parent
GATE_DIR = ROOT838 / "agent_reflection_gate"
BRAID_DIR = ROOT838 / "agent_braid_potential"
PLATEAU_DIR = ROOT838 / "agent_global_braid_plateau"
sys.path[:0] = [str(GATE_DIR), str(BRAID_DIR), str(PLATEAU_DIR)]

import braid_local_analysis as braid  # noqa: E402
import plateau_census as plateau  # noqa: E402
import reflection_order_gate as gate  # noqa: E402


Word = tuple[int, ...]
Triple = tuple[int, int, int]


N6_MINIMUM: Word = (
    0, 1, 2, 3, 2, 4, 3, 2, 1, 0, 2, 1, 2, 3, 2,
)

N6_EXPOSURE_PATH: tuple[Word, ...] = (
    N6_MINIMUM,
    (0, 1, 3, 2, 3, 4, 3, 2, 1, 0, 2, 1, 2, 3, 2),
    (0, 1, 3, 2, 4, 3, 2, 1, 0, 2, 1, 2, 4, 3, 2),
    (0, 1, 3, 4, 3, 2, 1, 0, 3, 2, 1, 2, 4, 3, 2),
    (0, 3, 4, 3, 2, 1, 0, 2, 3, 2, 1, 2, 4, 3, 2),
)

N6_TARGET_FLIP: Word = (
    3, 4, 3, 2, 1, 0, 1, 2, 3, 2, 1, 2, 4, 3, 2,
)

N10_PLUS: Word = (
    1, 7, 2, 3, 2, 4, 5, 4, 3, 6, 1, 4, 2, 1, 8,
    3, 7, 8, 5, 4, 0, 3, 2, 1, 5, 6, 5, 2, 3, 2,
    4, 7, 6, 3, 2, 5, 0, 6, 7, 4, 1, 3, 0, 2, 8,
)
N10_MINUS: Word = (
    1, 7, 2, 3, 2, 5, 4, 5, 3, 6, 1, 4, 2, 1, 8,
    3, 7, 8, 5, 4, 0, 3, 2, 1, 5, 6, 5, 2, 3, 2,
    4, 7, 6, 3, 2, 5, 0, 6, 7, 4, 1, 3, 0, 2, 8,
)

N20_Y: tuple[int, ...] = (
    358329966, -198927971, -63719209, 217376688, -90978114,
    -51535675, -10240197, 35270977, 81248315, 1125190,
    13012406, -271597462, 170081922, -21479979, 270310124,
    -492940940, -549521438, -607603894, 412455433, 450382350,
)


def root_orientation(n: int, word: Word, triple: Triple) -> bool:
    positions = {root: i for i, root in enumerate(gate.root_sequence(n, word))}
    a, b, c = triple
    return positions[(a, b)] < positions[(a, c)] < positions[(b, c)]


def edge_triple(n: int, first: Word, second: Word) -> Triple:
    changed = [
        triple
        for triple in itertools.combinations(range(n), 3)
        if root_orientation(n, first, triple) != root_orientation(n, second, triple)
    ]
    if len(changed) != 1:
        raise AssertionError(f"edge changed {len(changed)} packets")
    return changed[0]


def dyadic_value(profile: tuple[int, ...], q_power: int = 1) -> Fraction:
    """Evaluate a coefficient tuple at z=2^{-q_power}."""
    return sum(
        (Fraction(coefficient, 2 ** (q_power * degree)) for degree, coefficient in enumerate(profile)),
        Fraction(0),
    )


def vector_duals(n: int, plus_word: Word, position: int) -> dict[str, list[list[int]]]:
    roots = gate.root_sequence(n, plus_word)
    local = roots[position : position + 3]
    labels = tuple(sorted(set(local[0] + local[1] + local[2])))
    a, _, c = labels
    prefix, suffix = roots[:position], roots[position + 3 :]
    fp, fs = braid.f_product(n, prefix), braid.f_product(n, suffix)
    gp, gs = braid.g_product(n, prefix), braid.g_product(n, suffix)
    return {
        "alpha": [braid.column(fs[0], c), braid.column(fs[1], c)],
        "beta": [braid.row(fp[0], a), braid.row(fp[1], a)],
        "gamma": [braid.column(gp[0], c), braid.column(gp[1], c)],
        "delta": [braid.row(gs[0], a), braid.row(gs[1], a)],
    }


def check_six_wire_obstruction() -> dict[str, object]:
    words, adjacency, evaluations = plateau.enumerate_graph(6)
    best_pair = min((e.trace, e.first_moment) for e in evaluations.values())
    value = evaluations[N6_MINIMUM]
    if (value.trace, value.first_moment) != best_pair or value.graded != (0, 6, 15, 20, 3):
        raise AssertionError("saved state is not a global (V,M) minimum")

    global_minima = [
        word
        for word in words
        if (evaluations[word].trace, evaluations[word].first_moment) == best_pair
    ]
    exposed: set[Triple] = set()
    for word in global_minima:
        for neighbor in adjacency[word]:
            exposed.add(edge_triple(6, word, neighbor))
    missing = set(itertools.combinations(range(6), 3)) - exposed
    expected_missing = {(0, b, 5) for b in range(1, 5)}
    if missing != expected_missing:
        raise AssertionError((missing, expected_missing))

    target = (0, 1, 5)
    path_rows: list[dict[str, object]] = []
    previous = None
    for word in N6_EXPOSURE_PATH:
        if previous is not None:
            if gate.canonical_commutation_word(word) not in adjacency[gate.canonical_commutation_word(previous)]:
                raise AssertionError("saved exposure path has a nonedge")
            packet = edge_triple(6, previous, word)
            if packet == target:
                raise AssertionError("target packet was changed before its exposure")
        else:
            packet = None
        item = gate.evaluate_word(6, word, graded=True)
        realization = gate.fixed_x_realization(6, gate.root_sequence(6, word))
        if realization is None:
            raise AssertionError("saved exposure-path state is not fixed-x realizable")
        path_rows.append(
            {
                "word": list(word),
                "packet_from_previous": list(packet) if packet else None,
                "V": item.trace,
                "M": item.first_moment,
                "profile": list(item.graded or ()),
                "fixed_x_y": [[y.numerator, y.denominator] for y in realization],
            }
        )
        previous = word

    if edge_triple(6, N6_EXPOSURE_PATH[-1], N6_TARGET_FLIP) != target:
        raise AssertionError("terminal edge is not the target packet")
    before = gate.evaluate_word(6, N6_EXPOSURE_PATH[-1], graded=True)
    after = gate.evaluate_word(6, N6_TARGET_FLIP, graded=True)
    after_realization = gate.fixed_x_realization(
        6, gate.root_sequence(6, N6_TARGET_FLIP)
    )
    if after_realization is None:
        raise AssertionError("target-flipped state is not fixed-x realizable")
    if not (before.trace, before.first_moment) == (48, 124):
        raise AssertionError("bad pre-flip objective")
    if not (after.trace, after.first_moment) == (45, 112):
        raise AssertionError("target packet did not reverse its preference")
    if root_orientation(6, N6_MINIMUM, target) != root_orientation(6, N6_EXPOSURE_PATH[-1], target):
        raise AssertionError("target orientation changed along the avoiding path")

    reversed_roots = tuple(reversed(gate.root_sequence(6, N6_MINIMUM)))
    reversed_word = gate.word_from_roots(6, reversed_roots)
    reversed_value = gate.evaluate_word(6, reversed_word, graded=True)
    if reversed_value.graded != value.graded:
        raise AssertionError("root-order reversal did not preserve Z(z)")

    return {
        "class_count": len(words),
        "global_lex_objective": list(best_pair),
        "global_lex_minimum_count": len(global_minima),
        "exposed_packet_union_size": len(exposed),
        "missing_packets": [list(x) for x in sorted(missing)],
        "target": list(target),
        "avoiding_path": path_rows,
        "target_flip": {
            "word": list(N6_TARGET_FLIP),
            "V": after.trace,
            "M": after.first_moment,
            "profile": list(after.graded or ()),
            "fixed_x_y": [
                [y.numerator, y.denominator] for y in after_realization
            ],
        },
        "reversal_word": list(reversed_word),
        "reversal_profile": list(reversed_value.graded or ()),
    }


def check_ten_wire_half_weight_obstruction() -> dict[str, object]:
    switch = braid.switch_from_plus_word(10, N10_PLUS, 5)
    if switch.minus_word != N10_MINUS or switch.triple != (1, 5, 6):
        raise AssertionError("saved direct braid does not reconstruct")
    plus = gate.evaluate_word(10, N10_PLUS, graded=True)
    minus = gate.evaluate_word(10, N10_MINUS, graded=True)
    expected_plus = (0, 10, 45, 120, 147, 88, 24, 2)
    expected_minus = (0, 10, 45, 120, 148, 87, 23, 2)
    if plus.graded != expected_plus or minus.graded != expected_minus:
        raise AssertionError("saved profiles changed")
    if not (minus.trace < plus.trace and minus.first_moment < plus.first_moment):
        raise AssertionError("minus is not lexicographically preferred")
    half_difference = dyadic_value(expected_minus) - dyadic_value(expected_plus)
    if half_difference != Fraction(1, 64):
        raise AssertionError(half_difference)

    duals = vector_duals(10, N10_PLUS, 5)
    expected_duals = {
        "alpha": [[0, 0, 0, 0, 0, 0, 1, 1, 1, 2], [0, 0, 0, 0, 0, 0, 0, 1, 1, 3]],
        "beta": [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0] * 10],
        "gamma": [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0] * 10],
        "delta": [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    }
    if duals != expected_duals:
        raise AssertionError("full dual boundary vectors changed")
    realizations = {
        "plus": gate.fixed_x_realization(10, gate.root_sequence(10, N10_PLUS)),
        "minus": gate.fixed_x_realization(10, gate.root_sequence(10, N10_MINUS)),
    }
    if any(value is None for value in realizations.values()):
        raise AssertionError("half-weight switch is not fixed-x realizable")

    return {
        "n": 10,
        "position": 5,
        "triple": list(switch.triple),
        "plus_word": list(N10_PLUS),
        "minus_word": list(N10_MINUS),
        "plus_profile": list(expected_plus),
        "minus_profile": list(expected_minus),
        "plus_V_M": [plus.trace, plus.first_moment],
        "minus_V_M": [minus.trace, minus.first_moment],
        "Zminus_half_minus_Zplus_half": [half_difference.numerator, half_difference.denominator],
        "base_V_M": [switch.base_trace, switch.base_first_moment],
        "phi_phi_prime": [switch.phi, switch.phi_derivative],
        "psi_psi_prime": [switch.psi, switch.psi_derivative],
        "boundary_vectors_value_derivative": duals,
        "fixed_x_realizations": {
            key: [[y.numerator, y.denominator] for y in value]
            for key, value in realizations.items()
            if value is not None
        },
    }


def empty_profile(evaluation: object) -> tuple[int, ...]:
    graded = tuple(evaluation.graded or ())
    if not graded or graded[0] != 0:
        raise AssertionError("expected a nonempty rank profile")
    return (1,) + graded[1:]


def half_statistic(profile: tuple[int, ...]) -> Fraction:
    n = profile[1]
    return Fraction(n) * dyadic_value(profile) / sum(profile)


def check_exact_half_weight_census() -> dict[str, object]:
    expected = {
        3: Fraction(81, 64),
        4: Fraction(4, 3),
        5: Fraction(65, 48),
        6: Fraction(167, 120),
        7: Fraction(1645, 1168),
    }
    rows = []
    for n in range(3, 8):
        words, _, evaluations = plateau.enumerate_graph(n)
        values = {
            word: half_statistic(empty_profile(evaluations[word]))
            for word in words
        }
        maximum = max(values.values())
        if maximum != expected[n]:
            raise AssertionError((n, maximum, expected[n]))
        maximizers = {word for word in words if values[word] == maximum}
        minimum_trace = min(e.trace for e in evaluations.values())
        trace_minimizers = {
            word for word in words if evaluations[word].trace == minimum_trace
        }
        if maximizers != trace_minimizers:
            raise AssertionError("H maximizers and trace minimizers differ")
        representative = min(maximizers)
        rows.append(
            {
                "n": n,
                "commutation_classes": len(words),
                "maximum_H": [maximum.numerator, maximum.denominator],
                "maximizer_count": len(maximizers),
                "minimum_nonempty_trace": minimum_trace,
                "profile": list(empty_profile(evaluations[representative])),
            }
        )

    finite_minima = []
    for n, profile in (
        (8, (1, 8, 28, 56, 21)),
        (9, (1, 9, 36, 84, 36, 3)),
    ):
        statistic = half_statistic(profile)
        finite_minima.append(
            {
                "n": n,
                "profile": list(profile),
                "H": [statistic.numerator, statistic.denominator],
            }
        )
    return {"exact_all_classes": rows, "exact_realizable_minima": finite_minima}


def check_n20_coordinate_record() -> dict[str, object]:
    n = len(N20_Y)
    slopes = sorted(
        (Fraction(N20_Y[j] - N20_Y[i], j - i), i, j)
        for i in range(n)
        for j in range(i + 1, n)
    )
    for first, second in zip(slopes, slopes[1:]):
        if first[0] == second[0] and len({first[1], first[2], second[1], second[2]}) < 4:
            raise AssertionError("n=20 record has a collinear triple")
    roots = tuple((i, j) for _, i, j in slopes)
    word = gate.word_from_roots(n, roots)
    evaluation = gate.evaluate_word(n, word, graded=True)
    profile = empty_profile(evaluation)
    expected = (1, 20, 190, 1140, 2415, 866, 135, 8)
    if profile != expected:
        raise AssertionError((profile, expected))
    if sum(profile) != 4775 or evaluation.first_moment != 18676:
        raise AssertionError("n=20 objective changed")
    statistic = half_statistic(profile)
    if statistic != Fraction(4879, 3056):
        raise AssertionError(statistic)
    return {
        "points": [[i, y] for i, y in enumerate(N20_Y)],
        "general_position": True,
        "word_zero_based": list(word),
        "profile_including_empty": list(profile),
        "V_including_empty": sum(profile),
        "M": evaluation.first_moment,
        "H": [statistic.numerator, statistic.denominator],
        "previous_best_all_inclusive_V": 5156,
        "improvement": 5156 - sum(profile),
    }


def weighted_product(n: int, roots: tuple[tuple[int, int], ...]) -> list[list[Fraction]]:
    matrix = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for i, j in roots:
        matrix[j] = [x + y / 2 for x, y in zip(matrix[j], matrix[i])]
    return matrix


def check_saved_large_coordinate_records() -> list[dict[str, object]]:
    saved = json.loads((HERE / "half_weight_search_records.json").read_text())
    rows = []
    for key in ("24", "30"):
        record = saved["exact_records"][key]
        ys = tuple(map(int, record[f"y_at_x_0_through_{int(key)-1}"]))
        n = len(ys)
        slopes = sorted(
            (Fraction(ys[j] - ys[i], j - i), i, j)
            for i in range(n)
            for j in range(i + 1, n)
        )
        for first, second in zip(slopes, slopes[1:]):
            if first[0] == second[0] and len({first[1], first[2], second[1], second[2]}) < 4:
                raise AssertionError(f"saved n={n} record is not in general position")
        roots = tuple((i, j) for _, i, j in slopes)
        word = gate.word_from_roots(n, roots)
        evaluation = gate.evaluate_word(n, word)
        V = evaluation.trace + 1
        if [V, evaluation.first_moment] != [record["V"], record["M"]]:
            raise AssertionError(f"saved n={n} objective changed")
        cups = weighted_product(n, roots)
        caps = weighted_product(n, tuple(reversed(roots)))
        Z_half = (
            1
            + Fraction(n, 2)
            + sum(
                (cups[i][j] * caps[i][j] for i in range(n) for j in range(n)),
                Fraction(0),
            )
            - n
        )
        H = Fraction(n) * Z_half / V
        if [Z_half.numerator, Z_half.denominator] != record["Z_half_fraction"]:
            raise AssertionError(f"saved n={n} half partition changed")
        if [H.numerator, H.denominator] != record["H_fraction"]:
            raise AssertionError(f"saved n={n} H changed")
        rows.append(
            {
                "n": n,
                "general_position": True,
                "V": V,
                "M": evaluation.first_moment,
                "Z_half": [Z_half.numerator, Z_half.denominator],
                "H": [H.numerator, H.denominator],
            }
        )
    return rows


def check_profile_identities(profile: tuple[int, ...]) -> dict[str, object]:
    """Check the algebra behind the deletion/variance and Jensen reductions."""
    n = 6
    V = sum(profile)
    first = sum(k * a for k, a in enumerate(profile))
    second = sum(k * k * a for k, a in enumerate(profile))
    mu = Fraction(first, V)
    variance = Fraction(second, V) - mu * mu
    # Sums over deletions, after double-counting a k-face n-k times.
    deletion_mass = sum((n - k) * a for k, a in enumerate(profile))
    deletion_moment = sum((n - k) * k * a for k, a in enumerate(profile))
    if deletion_mass != (Fraction(n) - mu) * V:
        raise AssertionError("deletion mass identity failed")
    weighted_deletion_mean = Fraction(deletion_moment, deletion_mass)
    if mu - weighted_deletion_mean != variance / (n - mu):
        raise AssertionError("variance increment identity failed")
    half = dyadic_value(profile)
    # Jensen itself is analytic; this exact inequality is its specialization.
    if float(half / V) + 1e-15 < 2.0 ** (-float(mu)):
        raise AssertionError("Jensen specialization failed")
    return {
        "empty_inclusive_profile": list(profile),
        "V": V,
        "mu": [mu.numerator, mu.denominator],
        "variance": [variance.numerator, variance.denominator],
        "weighted_deletion_mean": [weighted_deletion_mean.numerator, weighted_deletion_mean.denominator],
        "Z_half": [half.numerator, half.denominator],
        "n_Z_half_over_V": [
            (n * half / V).numerator,
            (n * half / V).denominator,
        ],
    }


def run_all() -> dict[str, object]:
    return {
        "mode": "exact_dual_number_amortization_obstructions",
        "six_wire_exposure": check_six_wire_obstruction(),
        "ten_wire_half_weight": check_ten_wire_half_weight_obstruction(),
        "half_weight_census": check_exact_half_weight_census(),
        "new_n20_coordinate_record": check_n20_coordinate_record(),
        "large_coordinate_replays": check_saved_large_coordinate_records(),
        "deletion_variance": check_profile_identities((1, 6, 15, 20, 3)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-certificate", type=Path)
    args = parser.parse_args()
    result = run_all()
    if args.write_certificate:
        args.write_certificate.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
