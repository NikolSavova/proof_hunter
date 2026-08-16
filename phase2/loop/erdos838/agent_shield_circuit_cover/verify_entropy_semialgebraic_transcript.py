#!/usr/bin/env python3
"""Numerical/exact audit for ENTROPY_SEMIALGEBRAIC_TRANSCRIPT.md."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import product
import json
import math
from pathlib import Path
import random


def entropy(probabilities):
    return -sum(float(p) * math.log2(float(p)) for p in probabilities if p)


def kl(p, q):
    value = 0.0
    for left, right in zip(p, q):
        if left:
            assert right
            value += float(left) * math.log2(float(left / right))
    return value


def marginal_3(law, axis):
    output = [Q(0), Q(0)]
    for state, probability in law.items():
        output[state[axis]] += probability
    return output


def total_correlation_3(law):
    marginals = [marginal_3(law, axis) for axis in range(3)]
    states = tuple(product((0, 1), repeat=3))
    p = [law.get(state, Q(0)) for state in states]
    q = [marginals[0][state[0]] * marginals[1][state[1]] * marginals[2][state[2]]
         for state in states]
    return kl(p, q)


def kl_partition_audit():
    rng = random.Random(8838)
    maximum_error = 0.0
    minimum_correction = float("inf")
    for _ in range(400):
        raw = {state: rng.randint(0, 15) for state in product((0, 1), repeat=3)}
        if sum(raw.values()) == 0:
            raw[(0, 0, 0)] = 1
        total = sum(raw.values())
        law = {state: Q(weight, total) for state, weight in raw.items() if weight}
        marginals = [marginal_3(law, axis) for axis in range(3)]

        # Product rectangle partition: x=0 is one rectangle; x=1 is split by
        # y, and the final y=1 cell is split by z.  This is deliberately not
        # a single Cartesian grid transcript.
        rectangles = (
            lambda s: s[0] == 0,
            lambda s: s[0] == 1 and s[1] == 0,
            lambda s: s[0] == 1 and s[1] == 1 and s[2] == 0,
            lambda s: s[0] == 1 and s[1] == 1 and s[2] == 1,
        )
        p_cells, q_cells = [], []
        child_parent_divergence = 0.0
        child_tc_average = 0.0
        for predicate in rectangles:
            states = tuple(state for state in product((0, 1), repeat=3) if predicate(state))
            p_mass = sum((law.get(state, Q(0)) for state in states), Q(0))
            q_mass = sum((marginals[0][state[0]] * marginals[1][state[1]] * marginals[2][state[2]]
                          for state in states), Q(0))
            p_cells.append(p_mass)
            q_cells.append(q_mass)
            if not p_mass:
                continue
            conditional = {state: law.get(state, Q(0)) / p_mass
                           for state in states if law.get(state, Q(0))}
            q_conditional = [
                marginals[0][state[0]] * marginals[1][state[1]] * marginals[2][state[2]] / q_mass
                for state in states
            ]
            p_conditional = [conditional.get(state, Q(0)) for state in states]
            parent_divergence = kl(p_conditional, q_conditional)
            child_tc = total_correlation_3(conditional)
            assert parent_divergence + 1e-11 >= child_tc
            minimum_correction = min(minimum_correction, parent_divergence - child_tc)
            child_parent_divergence += float(p_mass) * parent_divergence
            child_tc_average += float(p_mass) * child_tc

        root_tc = total_correlation_3(law)
        partition_divergence = kl(p_cells, q_cells)
        error = abs(root_tc - partition_divergence - child_parent_divergence)
        maximum_error = max(maximum_error, error)
        assert error < 1e-10
        assert root_tc + 1e-10 >= partition_divergence + child_tc_average
    return {
        "random_laws": 400,
        "maximum_chain_rule_error": maximum_error,
        "minimum_child_product_correction": minimum_correction,
    }


def entropy_of_joint(law, indices):
    marginal = {}
    for state, probability in law.items():
        key = tuple(state[index] for index in indices)
        marginal[key] = marginal.get(key, Q(0)) + probability
    return entropy(marginal.values())


def global_total_correlation(law, rank):
    singles = sum(entropy_of_joint(law, (index,)) for index in range(rank))
    return singles - entropy(law.values())


def window_total_correlation(law, start):
    singles = sum(entropy_of_joint(law, (index,)) for index in range(start, start + 3))
    return singles - entropy_of_joint(law, tuple(range(start, start + 3)))


def window_tc_audit():
    rng = random.Random(8839)
    rows = []
    maximum_ratio = 0.0
    for rank in range(3, 9):
        for _ in range(80):
            raw = {state: rng.randint(0, 9) for state in product((0, 1), repeat=rank)}
            total = sum(raw.values())
            law = {state: Q(weight, total) for state, weight in raw.items() if weight}
            redundancy = global_total_correlation(law, rank)
            window_sum = sum(window_total_correlation(law, start) for start in range(rank - 2))
            assert window_sum <= 2 * redundancy + 1e-9
            if redundancy > 1e-12:
                maximum_ratio = max(maximum_ratio, window_sum / redundancy)
        rows.append({"rank": rank, "random_laws": 80})

    # Independent diagonal blocks are the concentration stress used in the
    # geometric audit.  Exact entropy values are integral here.
    diagonal_rows = []
    for blocks in range(1, 5):
        rank = 3 * blocks
        law = {}
        for block_bits in product((0, 1), repeat=blocks):
            state = tuple(bit for bit in block_bits for _ in range(3))
            law[state] = Q(1, 1 << blocks)
        redundancy = global_total_correlation(law, rank)
        window_sum = sum(window_total_correlation(law, start) for start in range(rank - 2))
        assert abs(redundancy - 2 * blocks) < 1e-12
        assert window_sum <= 2 * redundancy + 1e-12
        diagonal_rows.append({
            "blocks": blocks,
            "rank": rank,
            "global_TC": redundancy,
            "window_TC_sum": window_sum,
        })
    return {
        "random_rows": rows,
        "maximum_random_window_over_global_TC": maximum_ratio,
        "diagonal_blocks": diagonal_rows,
    }


def high_node_and_entropy_audit():
    c_star = Q(1, 2) * math.log2(Q(4, 3))
    assert c_star > 0
    minimum = float("inf")
    for theta_num in range(51, 101):
        theta = Q(theta_num, 100)
        for eta_num in range(1, 26):
            eta = Q(eta_num, 100)
            divergence = kl((theta, 1 - theta), (eta, 1 - eta))
            minimum = min(minimum, divergence)
            assert divergence + 1e-12 >= c_star

    rng = random.Random(8840)
    transcript_trials = 300
    for _ in range(transcript_trials):
        counts = [rng.randint(0, 100) for _ in range(rng.randint(2, 30))]
        if sum(counts) == 0:
            counts[0] = 1
        probabilities = [Q(value, sum(counts)) for value in counts if value]
        h = entropy(probabilities)
        p_max = max(probabilities)
        assert float(p_max) + 1e-12 >= 2 ** (-h)
        population = rng.randint(1, 10000)
        # A transcript atom of probability p under a uniform population has
        # exactly population*p words whenever the synthetic counts divide.
        atom_counts = [value * population for value in probabilities]
        assert max(atom_counts) + 1e-9 >= population * 2 ** (-h)
    return {
        "c_star_bits": c_star,
        "grid_minimum_high_node_divergence": minimum,
        "entropy_atom_trials": transcript_trials,
    }


def main():
    certificate = {
        "artifact": "ENTROPY_SEMIALGEBRAIC_TRANSCRIPT",
        "kl_partition": kl_partition_audit(),
        "overlapping_windows": window_tc_audit(),
        "high_node_and_entropy": high_node_and_entropy_audit(),
        "status": "PASS",
    }
    output = Path(__file__).with_name("entropy_semialgebraic_transcript_certificate.json")
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
