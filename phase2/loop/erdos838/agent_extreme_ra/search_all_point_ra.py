#!/usr/bin/env python3
"""Anneal the all-point averaged RA inequality on reflection orders."""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
GATE = ROOT / "agent_reflection_gate"
sys.path.insert(0, str(GATE))
import reflection_order_gate as gate  # noqa: E402


def partition_value(n, roots, activity):
    def product(sequence):
        matrix = [[float(i == j) for j in range(n)] for i in range(n)]
        for i, j in sequence:
            matrix[j] = [a + activity * b for a, b in zip(matrix[j], matrix[i])]
        return matrix

    forward = product(roots)
    reverse = product(reversed(roots))
    return (
        1
        + n * activity
        + sum(forward[i][j] * reverse[i][j] for i in range(n) for j in range(n))
        - n
    )


def delete_wire(roots, deleted, n):
    keep = [i for i in range(n) if i != deleted]
    relabel = {old: new for new, old in enumerate(keep)}
    return tuple(
        (relabel[a], relabel[b])
        for a, b in roots
        if a != deleted and b != deleted
    )


def value_moment(n, roots, activity):
    def product(sequence):
        values = [[float(i == j) for j in range(n)] for i in range(n)]
        derivatives = [[0.0] * n for _ in range(n)]
        for i, j in sequence:
            old_i = values[i]
            derivative_i = derivatives[i]
            values[j] = [a + activity * b for a, b in zip(values[j], old_i)]
            derivatives[j] = [
                a + b + activity * c
                for a, b, c in zip(derivatives[j], old_i, derivative_i)
            ]
        return values, derivatives

    forward, forward_d = product(roots)
    reverse, reverse_d = product(reversed(roots))
    value = (
        1
        + n * activity
        + sum(forward[i][j] * reverse[i][j] for i in range(n) for j in range(n))
        - n
    )
    derivative = n + sum(
        forward_d[i][j] * reverse[i][j] + forward[i][j] * reverse_d[i][j]
        for i in range(n)
        for j in range(n)
    )
    return value, activity * derivative


def score(n, word):
    roots = gate.root_sequence(n, word)
    half, half_moment = value_moment(n, roots, 0.5)
    _, unit_moment = value_moment(n, roots, 1.0)
    return (n * half + (n - 1) * half_moment) / (2 * unit_moment)


def existential_score(n, word):
    roots = gate.root_sequence(n, word)
    parent_unit = partition_value(n, roots, 1.0)
    parent_half = partition_value(n, roots, 0.5)
    ratios = []
    for e in range(n):
        child_roots = delete_wire(roots, e, n)
        child_unit = partition_value(n - 1, child_roots, 1.0)
        child_half = partition_value(n - 1, child_roots, 0.5)
        rooted_unit = parent_unit - child_unit
        rooted_half_mass = parent_half - child_half
        ratios.append(
            (parent_half + (n - 1) * rooted_half_mass) / (2 * rooted_unit)
        )
    return min(ratios), ratios


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("seed_file", type=Path)
    parser.add_argument("--steps", type=int, default=100_000)
    parser.add_argument("--seed", type=int, default=838)
    parser.add_argument("--temperature", type=float, default=0.004)
    parser.add_argument("--objective", choices=("average", "existential"), default="average")
    parser.add_argument("--output", type=Path, default=Path("/tmp/apa_best.json"))
    args = parser.parse_args()
    data = json.loads(args.seed_file.read_text())
    n = data["n"]
    word = tuple(data["word_zero_based"])
    rng = random.Random(args.seed)
    evaluate = (
        (lambda candidate: existential_score(n, candidate)[0])
        if args.objective == "existential"
        else (lambda candidate: score(n, candidate))
    )
    current = evaluate(word)
    best_score, best_word = current, word
    evaluated = accepted = 0
    print(f"start n={n} score={current:.12g}", flush=True)
    for step in range(args.steps):
        commuting, braids = gate.coxeter_moves(word)
        if commuting and (not braids or rng.random() < 0.8):
            word = gate.apply_commutation(word, rng.choice(commuting))
            continue
        candidate_word = gate.apply_braid(word, rng.choice(braids))
        candidate = evaluate(candidate_word)
        evaluated += 1
        phase = (step % 20_000) / 19_999
        temperature = args.temperature * (1 - phase) + 0.000001
        difference = candidate - current
        if difference >= 0 or rng.random() < math.exp(difference / temperature):
            word, current = candidate_word, candidate
            accepted += 1
        if current > best_score:
            best_score, best_word = current, word
        if (step + 1) % 20_000 == 0:
            print(
                f"step={step+1} evaluated={evaluated} current={current:.12g} "
                f"best={best_score:.12g}",
                flush=True,
            )
    result = {
        "n": n,
        "score": best_score,
        "word_zero_based": list(best_word),
        "steps": args.steps,
        "evaluated_braids": evaluated,
        "accepted_braids": accepted,
        "seed": args.seed,
        "objective": args.objective,
    }
    if args.objective == "existential":
        _, ratios = existential_score(n, best_word)
        result["individual_ratios"] = ratios
        result["passing_points"] = sum(value <= 1 for value in ratios)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "word_zero_based"}), flush=True)


if __name__ == "__main__":
    main()
