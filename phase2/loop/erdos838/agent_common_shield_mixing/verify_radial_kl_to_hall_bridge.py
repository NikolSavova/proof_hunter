#!/usr/bin/env python3
"""Verifier for the exact radial-KL/half-Gibbs Hall bridge."""

from fractions import Fraction
from math import log2


def endpoint_fixture():
    # Ordinary faces are represented only by labels and their exact
    # half-weights.  Their total is F, so pi is an exact probability law.
    face_weights = {
        "empty": Fraction(1),
        "a": Fraction(1, 2),
        "b": Fraction(1, 4),
        "c": Fraction(1, 8),
    }
    F = sum(face_weights.values(), Fraction(0))
    intervals = {
        "e0": ("a", "b"),
        "e1": ("b", "c"),
    }
    G = {"e0": Fraction(1, 4), "e1": Fraction(1, 8)}
    depths = {
        0: {"e0": Fraction(1, 10), "e1": Fraction(1, 20)},
        1: {"e0": Fraction(1, 40), "e1": Fraction(1, 80)},
    }
    return face_weights, F, intervals, G, depths


def exact_routing_check():
    face_weights, F, intervals, G, depths = endpoint_fixture()
    F_e = {endpoint: sum((face_weights[face] for face in bank), Fraction(0))
           for endpoint, bank in intervals.items()}
    lambdas = {endpoint: 4 * G[endpoint] / F_e[endpoint]
               for endpoint in intervals}

    routed = Fraction(0)
    loads = {face: Fraction(0) for face in face_weights}
    expected_loads = {face: Fraction(0) for face in face_weights}
    S = Fraction(0)
    M = Fraction(0)
    divergence = 0.0
    for depth in depths.values():
        for endpoint, q in depth.items():
            M += q
            S += q / lambdas[endpoint]
            divergence += float(q) * log2(float(1 / lambdas[endpoint]))
            h = q * F / G[endpoint]
            for face in intervals[endpoint]:
                atom = q * face_weights[face] / (4 * G[endpoint])
                routed += atom
                loads[face] += atom / (face_weights[face] / F)
                expected_loads[face] += h / 4

    assert routed == S
    assert loads == expected_loads
    average_load = sum((face_weights[face] / F) * loads[face]
                       for face in face_weights)
    assert average_load == S
    assert max(loads.values()) >= S
    assert divergence <= float(M) * log2(float(S / M)) + 1e-12
    return F, S, M, max(loads.values())


def weighted_marked_localization_check():
    # Three occurrences with rational weights, four ordinary target faces,
    # at least K=3 marked targets each, mark rank b=2, and T=2 states.
    weights = (Fraction(2), Fraction(3), Fraction(5))
    banks = (
        (("p", "F0", 0), ("p", "F1", 0), ("q", "F2", 1)),
        (("p", "F0", 0), ("q", "F1", 1), ("q", "F3", 1)),
        (("p", "F0", 0), ("p", "F2", 1), ("q", "F3", 1)),
    )
    loads = {}
    for weight, bank in zip(weights, banks):
        assert len(bank) >= 3
        for target in bank:
            loads[target] = loads.get(target, Fraction(0)) + weight
    K, b, T, U = 3, 2, 2, 4
    lower = Fraction(K * sum(weights), b * T * U)
    maximum = max(loads.values())
    assert maximum >= lower
    assert lower == Fraction(15, 8)
    assert maximum == 10
    return lower, maximum


def genuine_history_weight_check():
    F = Fraction(19, 7)
    G = Fraction(5, 8)
    for depth in range(4):
        parents = ((2, 3), (5, 7), (8, 2))  # (rank, radial degree)
        q = sum((Fraction(degree, (4 ** depth) * (2 ** rank) * F)
                 for rank, degree in parents), Fraction(0))
        h = q * F / G
        history_weight = sum(
            (Fraction(degree, (4 ** depth) * (2 ** rank)) / G
             for rank, degree in parents), Fraction(0)
        )
        assert history_weight == h


def rank_resolved_check():
    F = Fraction(37, 5)
    for depth in range(4):
        for parent_rank in range(2, 9):
            for baseline_rank in range(2, 13):
                for histories in (1, 3, 11):
                    for baseline_faces in (1, 2, 7):
                        q = (Fraction(histories, 1 << parent_rank)
                             / (F * (4 ** depth)))
                        p = Fraction(baseline_faces, 1 << baseline_rank) / F
                        exponent = parent_rank + 2 * depth - baseline_rank
                        power = (Fraction(2 ** exponent) if exponent >= 0
                                 else Fraction(1, 2 ** (-exponent)))
                        recovered = (q / p) * power
                        assert recovered == Fraction(histories, baseline_faces)


def main():
    F, S, M, maximum = exact_routing_check()
    lower, marked_maximum = weighted_marked_localization_check()
    genuine_history_weight_check()
    rank_resolved_check()
    print(f"PASS: exact half-Gibbs routing F={F}, demand={S}, mass={M}, "
          f"max-load={maximum}")
    print(f"PASS: weighted marked localization lower={lower}, actual={marked_maximum}")
    print("PASS: endpoint tilt expands exactly into genuine radial-history weights")
    print("PASS: exact rank-resolved q/G-to-raw-Hall identity")


if __name__ == "__main__":
    main()
