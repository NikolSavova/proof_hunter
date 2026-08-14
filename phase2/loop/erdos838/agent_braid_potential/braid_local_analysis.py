#!/usr/bin/env python3
"""Exact local-braid identities and adversarial searches for Erdos 838.

The script deliberately imports the independently written Gate-A evaluator and
adds only the long-braid bookkeeping needed here.  All arithmetic used for
reported traces, first moments, and local switch terms is integral.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import random
import sys
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


HERE = Path(__file__).resolve().parent
GATE_PATH = HERE.parent / "agent_reflection_gate" / "reflection_order_gate.py"
SPEC = importlib.util.spec_from_file_location("reflection_order_gate", GATE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {GATE_PATH}")
gate = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = gate
SPEC.loader.exec_module(gate)

Root = tuple[int, int]
Word = tuple[int, ...]
Matrix = list[list[int]]
DualMatrix = tuple[Matrix, Matrix]


def zeros(n: int) -> Matrix:
    return [[0] * n for _ in range(n)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    n = len(left)
    out = zeros(n)
    for i in range(n):
        for k, value in enumerate(left[i]):
            if value:
                for j, other in enumerate(right[k]):
                    out[i][j] += value * other
    return out


def matadd(left: Matrix, right: Matrix) -> Matrix:
    return [[a + b for a, b in zip(x, y)] for x, y in zip(left, right)]


def matsub(left: Matrix, right: Matrix) -> Matrix:
    return [[a - b for a, b in zip(x, y)] for x, y in zip(left, right)]


def matmul_dual(left: DualMatrix, right: DualMatrix) -> DualMatrix:
    values = matmul(left[0], right[0])
    derivatives = matadd(matmul(left[1], right[0]), matmul(left[0], right[1]))
    return values, derivatives


def f_product(n: int, roots: Sequence[Root]) -> DualMatrix:
    """F(roots)=T_last...T_first, together with d/dz at z=1."""
    return gate._value_derivative_product(n, roots)


def g_product(n: int, roots: Sequence[Root]) -> DualMatrix:
    """G(roots)=T_first...T_last, together with d/dz at z=1."""
    return gate._value_derivative_product(n, tuple(reversed(roots)))


def column(matrix: Matrix, j: int) -> list[int]:
    return [row[j] for row in matrix]


def row(matrix: Matrix, i: int) -> list[int]:
    return list(matrix[i])


def outer(left: Sequence[int], right: Sequence[int]) -> Matrix:
    return [[a * b for b in right] for a in left]


def outer_dual(
    left: tuple[list[int], list[int]], right: tuple[list[int], list[int]]
) -> DualMatrix:
    return (
        outer(left[0], right[0]),
        matadd(outer(left[1], right[0]), outer(left[0], right[1])),
    )


def frobenius(left: Matrix, right: Matrix) -> int:
    return sum(a * b for x, y in zip(left, right) for a, b in zip(x, y))


def frobenius_dual(left: DualMatrix, right: DualMatrix) -> tuple[int, int]:
    return (
        frobenius(left[0], right[0]),
        frobenius(left[1], right[0]) + frobenius(left[0], right[1]),
    )


@dataclass(frozen=True)
class Switch:
    """The exact two branches at one exposed long braid.

    ``plus`` has local roots ab,ac,bc and the rank-one bonus in A (cups).
    ``minus`` has roots bc,ac,ab and the rank-one bonus in B (caps).
    ``phi`` and ``psi`` exclude the compulsory z^2 of the local two-edge path.
    Thus the two added-family first moments are 2*value+derivative.
    """

    n: int
    triple: tuple[int, int, int]
    plus_word: Word
    minus_word: Word
    base_trace: int
    base_first_moment: int
    phi: int
    phi_derivative: int
    psi: int
    psi_derivative: int
    alpha: tuple[int, ...]
    beta: tuple[int, ...]
    gamma: tuple[int, ...]
    delta: tuple[int, ...]

    @property
    def plus_trace(self) -> int:
        return self.base_trace + self.phi

    @property
    def minus_trace(self) -> int:
        return self.base_trace + self.psi

    @property
    def plus_first_moment(self) -> int:
        return self.base_first_moment + 2 * self.phi + self.phi_derivative

    @property
    def minus_first_moment(self) -> int:
        return self.base_first_moment + 2 * self.psi + self.psi_derivative

    @property
    def phi_mean(self) -> Fraction:
        return Fraction(2 * self.phi + self.phi_derivative, self.phi)

    @property
    def psi_mean(self) -> Fraction:
        return Fraction(2 * self.psi + self.psi_derivative, self.psi)

    def summary(self, include_words: bool = True) -> dict[str, object]:
        data: dict[str, object] = {
            "n": self.n,
            "triple": self.triple,
            "base_trace": self.base_trace,
            "base_first_moment": self.base_first_moment,
            "phi": self.phi,
            "phi_derivative": self.phi_derivative,
            "phi_added_mean": float(self.phi_mean),
            "psi": self.psi,
            "psi_derivative": self.psi_derivative,
            "psi_added_mean": float(self.psi_mean),
            "plus_trace": self.plus_trace,
            "minus_trace": self.minus_trace,
            "plus_first_moment": self.plus_first_moment,
            "minus_first_moment": self.minus_first_moment,
            "plus_mean": float(Fraction(self.plus_first_moment, self.plus_trace)),
            "minus_mean": float(Fraction(self.minus_first_moment, self.minus_trace)),
            "alpha": self.alpha,
            "beta": self.beta,
            "gamma": self.gamma,
            "delta": self.delta,
        }
        if include_words:
            data["plus_word"] = self.plus_word
            data["minus_word"] = self.minus_word
            data["plus_roots"] = gate.root_sequence(self.n, self.plus_word)
            data["minus_roots"] = gate.root_sequence(self.n, self.minus_word)
        return data


def switch_from_plus_word(n: int, plus_word: Word, position: int) -> Switch:
    """Calculate the exact common base and the two rank-one switch terms."""
    if not (
        plus_word[position] == plus_word[position + 2]
        and plus_word[position + 1] == plus_word[position] + 1
    ):
        raise ValueError("word position is not a plus braid i,i+1,i")
    minus_word = gate.apply_braid(plus_word, position)
    plus_roots = gate.root_sequence(n, plus_word)
    minus_roots = gate.root_sequence(n, minus_word)
    local = plus_roots[position : position + 3]
    labels = tuple(sorted(set(local[0] + local[1] + local[2])))
    if len(labels) != 3:
        raise AssertionError("local braid did not use three wire labels")
    a, b, c = labels
    if local != ((a, b), (a, c), (b, c)):
        raise AssertionError((local, labels))
    if minus_roots[:position] != plus_roots[:position] or minus_roots[position + 3 :] != plus_roots[position + 3 :]:
        raise AssertionError("a long braid unexpectedly changed its context roots")
    prefix = plus_roots[:position]
    suffix = plus_roots[position + 3 :]
    q_local = ((b, c), (a, c), (a, b))

    fp, fs = f_product(n, prefix), f_product(n, suffix)
    gp, gs = g_product(n, prefix), g_product(n, suffix)
    k = f_product(n, q_local)
    # A0=F(S) K F(P), B0=G(P) K G(S).
    a0 = matmul_dual(matmul_dual(fs, k), fp)
    b0 = matmul_dual(matmul_dual(gp, k), gs)

    alpha = (column(fs[0], c), column(fs[1], c))
    beta = (row(fp[0], a), row(fp[1], a))
    gamma = (column(gp[0], c), column(gp[1], c))
    delta = (row(gs[0], a), row(gs[1], a))
    rank_a = outer_dual(alpha, beta)
    rank_b = outer_dual(gamma, delta)
    phi, phi_derivative = frobenius_dual(rank_a, b0)
    psi, psi_derivative = frobenius_dual(a0, rank_b)

    # Z0(z)=nz+<A0,B0>-n.  Its derivative at one is n+<A0,B0>'.
    base_trace, base_pair_derivative = frobenius_dual(a0, b0)
    base_first_moment = n + base_pair_derivative
    result = Switch(
        n,
        labels,
        plus_word,
        minus_word,
        base_trace,
        base_first_moment,
        phi,
        phi_derivative,
        psi,
        psi_derivative,
        tuple(alpha[0]),
        tuple(beta[0]),
        tuple(gamma[0]),
        tuple(delta[0]),
    )

    plus_eval = gate.evaluate_word(n, plus_word)
    minus_eval = gate.evaluate_word(n, minus_word)
    if (result.plus_trace, result.plus_first_moment) != (
        plus_eval.trace,
        plus_eval.first_moment,
    ):
        raise AssertionError((result.summary(), plus_eval.summary()))
    if (result.minus_trace, result.minus_first_moment) != (
        minus_eval.trace,
        minus_eval.first_moment,
    ):
        raise AssertionError((result.summary(), minus_eval.summary()))

    # Endpoint-array rank-one identities at z=1.
    if matsub([list(x) for x in plus_eval.cups], [list(x) for x in minus_eval.cups]) != rank_a[0]:
        raise AssertionError("cup endpoint rank-one identity failed")
    if matsub([list(x) for x in minus_eval.caps], [list(x) for x in plus_eval.caps]) != rank_b[0]:
        raise AssertionError("cap endpoint rank-one identity failed")
    return result


def exposed_switches(n: int, word: Word) -> Iterable[Switch]:
    """Yield each consecutive plus/minus braid of this particular word."""
    for position in gate.coxeter_moves(word)[1]:
        if word[position + 1] == word[position] + 1:
            yield switch_from_plus_word(n, word, position)
        else:
            yield switch_from_plus_word(n, gate.apply_braid(word, position), position)


def sign(value: int | Fraction | float) -> int:
    return (value > 0) - (value < 0)


def profile_degree(evaluation: object) -> int:
    graded = evaluation.graded
    if graded is None:
        return -1
    return len(graded) - 1


def objective_values(evaluation: object) -> dict[str, Fraction | int]:
    cup_total = evaluation.cup_total
    cap_total = evaluation.cap_total
    return {
        "trace": evaluation.trace,
        "first_moment": evaluation.first_moment,
        "mean": Fraction(evaluation.first_moment, evaluation.trace),
        "cup_plus_cap": cup_total + cap_total,
        "cup_times_cap": cup_total * cap_total,
        "cup_cap_imbalance": abs(cup_total - cap_total),
        "endpoint_max": evaluation.endpoint_max,
        # Positive means a worse violation of log V <= mu^2/2.
        "qms_log_ratio": math.log2(evaluation.trace)
        / (0.5 * evaluation.mean_size * evaluation.mean_size),
    }


def class_census(n: int, output: Path | None = None) -> dict[str, object]:
    """Exhaust all commutation classes and audit braid-local monotonicities."""
    initial = gate.canonical_commutation_word(gate.bubble_word(n))
    queue = [initial]
    seen = {initial}
    cursor = 0
    evaluations: dict[Word, object] = {}
    adjacency: dict[Word, set[Word]] = {}
    while cursor < len(queue):
        word = queue[cursor]
        cursor += 1
        evaluations[word] = gate.evaluate_word(n, word, graded=True)
        neighbors = gate.braid_neighbors_mod_commutation(n, word)
        adjacency[word] = neighbors
        for neighbor in neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    objectives = {word: objective_values(value) for word, value in evaluations.items()}
    names = tuple(next(iter(objectives.values())))
    local_minima: dict[str, list[Word]] = {name: [] for name in names}
    weak_local_minima: dict[str, list[Word]] = {name: [] for name in names}
    for word in queue:
        for name in names:
            here = objectives[word][name]
            nearby = [objectives[v][name] for v in adjacency[word]]
            if all(here < value for value in nearby):
                local_minima[name].append(word)
            if all(here <= value for value in nearby):
                weak_local_minima[name].append(word)

    edge_sign_pairs: dict[tuple[str, str], Counter[tuple[int, int]]] = {}
    for first_index, word in enumerate(queue):
        for neighbor in adjacency[word]:
            if word >= neighbor:
                continue
            for i, first in enumerate(names):
                for second in names[i + 1 :]:
                    key = (first, second)
                    edge_sign_pairs.setdefault(key, Counter())[
                        (
                            sign(objectives[neighbor][first] - objectives[word][first]),
                            sign(objectives[neighbor][second] - objectives[word][second]),
                        )
                    ] += 1

    def summarize_minima(words: list[Word]) -> dict[str, object]:
        if not words:
            return {"count": 0}
        traces = [evaluations[w].trace for w in words]
        means = [Fraction(evaluations[w].first_moment, evaluations[w].trace) for w in words]
        degrees = Counter(profile_degree(evaluations[w]) for w in words)
        cups_caps = [
            (evaluations[w].cup_total, evaluations[w].cap_total) for w in words
        ]
        smallest_trace_word = min(words, key=lambda w: evaluations[w].trace)
        smallest_mean_word = min(
            words,
            key=lambda w: Fraction(evaluations[w].first_moment, evaluations[w].trace),
        )
        return {
            "count": len(words),
            "trace_range": [min(traces), max(traces)],
            "mean_range": [float(min(means)), float(max(means))],
            "mean_minus_log2_n_range": [
                float(min(means)) - math.log2(n),
                float(max(means)) - math.log2(n),
            ],
            "profile_degree_histogram": dict(sorted(degrees.items())),
            "cup_cap_ratio_range": [
                min(c / d for c, d in cups_caps), max(c / d for c, d in cups_caps)
            ],
            "smallest_trace_certificate": gate.make_certificate(n, smallest_trace_word),
            "smallest_mean_certificate": gate.make_certificate(n, smallest_mean_word),
        }

    result: dict[str, object] = {
        "mode": "commutation_class_braid_census",
        "n": n,
        "class_count": len(queue),
        "edge_count": sum(map(len, adjacency.values())) // 2,
        "local_minima": {
            name: summarize_minima(words) for name, words in local_minima.items()
        },
        "weak_local_minima": {
            name: summarize_minima(words) for name, words in weak_local_minima.items()
        },
        "edge_sign_pair_histograms": {
            f"{first}__{second}": {
                f"{a},{b}": count for (a, b), count in sorted(histogram.items())
            }
            for (first, second), histogram in edge_sign_pairs.items()
        },
    }
    if output is not None:
        output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def adjacent_context_scan(n: int, output: Path | None = None) -> dict[str, object]:
    """Scan all words for direct braid contexts and keep minimal obstructions."""
    context_signs: dict[tuple[int, int, int], set[int]] = defaultdict(set)
    examples: dict[str, dict[str, object]] = {}
    counters: Counter[str] = Counter()
    seen_edges: set[tuple[Word, Word]] = set()
    switch_summaries: list[Switch] = []

    def keep(label: str, switch: Switch) -> None:
        if label not in examples:
            examples[label] = switch.summary()

    for word in gate.reduced_words(n):
        for switch in exposed_switches(n, word):
            edge = tuple(sorted((switch.plus_word, switch.minus_word)))
            if edge in seen_edges:
                continue
            seen_edges.add(edge)
            switch_summaries.append(switch)
            dv = switch.plus_trace - switch.minus_trace
            dm_num = (
                switch.plus_first_moment * switch.minus_trace
                - switch.minus_first_moment * switch.plus_trace
            )
            dfm = switch.plus_first_moment - switch.minus_first_moment
            d_added_mean = sign(switch.phi_mean - switch.psi_mean)
            context_signs[switch.triple].add(sign(dv))
            counters[f"trace_mean_sign_{sign(dv)},{sign(dm_num)}"] += 1
            counters[f"trace_first_moment_sign_{sign(dv)},{sign(dfm)}"] += 1
            counters[f"trace_added_mean_sign_{sign(dv)},{d_added_mean}"] += 1
            if sign(dv) * sign(dm_num) < 0:
                keep("trace_descent_raises_mean", switch)
            if sign(dv) * sign(dfm) < 0:
                keep("trace_descent_raises_first_moment", switch)
            if sign(dv) * d_added_mean < 0:
                keep("smaller_added_count_has_larger_added_mean", switch)
            if switch.phi == switch.psi and switch.phi_mean != switch.psi_mean:
                keep("trace_tie_changes_mean", switch)

    varying = [triple for triple, signs in context_signs.items() if -1 in signs and 1 in signs]
    if varying:
        wanted = varying[0]
        plus_example = next(
            x for x in switch_summaries if x.triple == wanted and x.plus_trace > x.minus_trace
        )
        minus_example = next(
            x for x in switch_summaries if x.triple == wanted and x.plus_trace < x.minus_trace
        )
        examples["same_triple_context_reversal_positive"] = plus_example.summary()
        examples["same_triple_context_reversal_negative"] = minus_example.summary()

    result: dict[str, object] = {
        "mode": "all_reduced_words_direct_braid_context_scan",
        "n": n,
        "individual_braid_edges": len(seen_edges),
        "triple_trace_delta_signs": {
            str(triple): sorted(signs) for triple, signs in sorted(context_signs.items())
        },
        "triples_with_both_nonzero_trace_directions": varying,
        "counters": dict(sorted(counters.items())),
        "examples": examples,
    }
    if output is not None:
        output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def random_walk_scan(
    n: int, steps: int, restarts: int, seed: int, output: Path | None = None
) -> dict[str, object]:
    """Annealed/random larger search, emphasizing monotonicity obstructions."""
    rng = random.Random(seed)
    best_trace = None
    best_mean = None
    examples: dict[str, dict[str, object]] = {}
    counters: Counter[str] = Counter()
    accepted = 0
    evaluated = 0
    for restart in range(restarts):
        word = gate.random_reduced_word(n, rng)
        current = gate.evaluate_word(n, word)
        for step in range(steps):
            commuting, braids = gate.coxeter_moves(word)
            if not braids or (commuting and rng.random() < 0.55):
                if commuting:
                    word = gate.apply_commutation(word, rng.choice(commuting))
                continue
            position = rng.choice(braids)
            plus_word = word if word[position + 1] == word[position] + 1 else gate.apply_braid(word, position)
            switch = switch_from_plus_word(n, plus_word, position)
            candidate_word = gate.apply_braid(word, position)
            candidate = gate.evaluate_word(n, candidate_word)
            evaluated += 1
            dv = switch.plus_trace - switch.minus_trace
            dm_num = switch.plus_first_moment * switch.minus_trace - switch.minus_first_moment * switch.plus_trace
            counters[f"trace_mean_sign_{sign(dv)},{sign(dm_num)}"] += 1
            if sign(dv) * sign(dm_num) < 0 and "trace_descent_raises_mean" not in examples:
                examples["trace_descent_raises_mean"] = switch.summary()
            # Anneal on mean, with periodic reheat, while also retaining trace records.
            current_score = current.mean_size
            candidate_score = candidate.mean_size
            phase = (step % max(500, steps // 4)) / max(499, steps // 4 - 1)
            temperature = 0.15 * (1 - phase) + 0.001
            if candidate_score <= current_score or rng.random() < math.exp((current_score - candidate_score) / temperature):
                word, current = candidate_word, candidate
                accepted += 1
            if best_trace is None or current.trace < best_trace[0].trace:
                best_trace = (current, word)
            if best_mean is None or current.first_moment * best_mean[0].trace < best_mean[0].first_moment * current.trace:
                best_mean = (current, word)
    if best_trace is None or best_mean is None:
        raise AssertionError("empty random walk")
    result: dict[str, object] = {
        "mode": "annealed_direct_braid_scan",
        "n": n,
        "steps_per_restart": steps,
        "restarts": restarts,
        "seed": seed,
        "evaluated_braids": evaluated,
        "accepted_braids": accepted,
        "best_trace": gate.make_certificate(n, best_trace[1]),
        "best_mean": gate.make_certificate(n, best_mean[1]),
        "counters": dict(sorted(counters.items())),
        "examples": examples,
    }
    if output is not None:
        output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def selftest() -> None:
    rng = random.Random(838)
    tested = 0
    for n in range(3, 9):
        for _ in range(100):
            word = gate.random_reduced_word(n, rng)
            for switch in exposed_switches(n, word):
                # Construction performs all array/trace/moment assertions.
                assert switch.phi > 0 and switch.psi > 0
                tested += 1
                break
    if tested < 100:
        raise AssertionError(f"too few exposed random braid tests: {tested}")
    print(f"rank-one endpoint and first-moment switch identities: PASS ({tested} contexts)")


def slim(result: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in result.items() if key not in {"examples"}}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("selftest")
    classes = sub.add_parser("classes")
    classes.add_argument("n", type=int)
    classes.add_argument("--output", type=Path)
    contexts = sub.add_parser("contexts")
    contexts.add_argument("n", type=int)
    contexts.add_argument("--output", type=Path)
    random_parser = sub.add_parser("random")
    random_parser.add_argument("n", type=int)
    random_parser.add_argument("--steps", type=int, default=10_000)
    random_parser.add_argument("--restarts", type=int, default=4)
    random_parser.add_argument("--seed", type=int, default=838)
    random_parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.command == "selftest":
        selftest()
    elif args.command == "classes":
        print(json.dumps(slim(class_census(args.n, args.output)), indent=2))
    elif args.command == "contexts":
        print(json.dumps(slim(adjacent_context_scan(args.n, args.output)), indent=2))
    elif args.command == "random":
        print(
            json.dumps(
                slim(random_walk_scan(args.n, args.steps, args.restarts, args.seed, args.output)),
                indent=2,
            )
        )


if __name__ == "__main__":
    main()
