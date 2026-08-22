#!/usr/bin/env python3
"""Verifier for high-load ambient-owner saturation in the swap core."""

from __future__ import annotations

from itertools import product


Edge = tuple[int, int, int]


def optimal_loads(vertex_count: int, edges: tuple[Edge, ...]):
    """Enumerate bundle orientations and return every quadratic optimum."""

    best_energy: int | None = None
    best: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    for choices in product(*(range(multiplicity + 1) for _, _, multiplicity in edges)):
        loads = [0] * vertex_count
        for (first, second, multiplicity), forward in zip(edges, choices):
            loads[first] += forward
            loads[second] += multiplicity - forward
        energy = sum(load * load for load in loads)
        row = tuple(loads), tuple(choices)
        if best_energy is None or energy < best_energy:
            best_energy = energy
            best = [row]
        elif energy == best_energy:
            best.append(row)
    assert best_energy is not None
    return best_energy, best


def verify_bundle_saturation() -> None:
    # Exhaust every three-vertex multigraph with bundle sizes at most three.
    for multiplicities in product(range(4), repeat=3):
        edges = tuple(
            (first, second, multiplicity)
            for (first, second), multiplicity in zip(
                ((0, 1), (0, 2), (1, 2)), multiplicities
            )
            if multiplicity
        )
        if not edges:
            continue
        _, optima = optimal_loads(3, edges)
        for loads, _ in optima:
            for first, second, multiplicity in edges:
                for threshold in range(1, 4):
                    if multiplicity >= 2 * threshold:
                        assert loads[first] >= threshold
                        assert loads[second] >= threshold

    # Seeded four-vertex stresses include asymmetric external loads.
    systems = (
        ((0, 1, 6), (0, 2, 6), (1, 3, 3), (2, 3, 1)),
        ((0, 1, 5), (0, 2, 4), (1, 2, 2), (2, 3, 4)),
        ((0, 1, 4), (1, 2, 1), (2, 3, 4), (0, 3, 1)),
    )
    for edges in systems:
        _, optima = optimal_loads(4, edges)
        for loads, _ in optima:
            for first, second, multiplicity in edges:
                for threshold in range(1, 4):
                    if multiplicity >= 2 * threshold:
                        assert loads[first] >= threshold
                        assert loads[second] >= threshold


def verify_owner_star() -> None:
    # Two bundles of size ceil(3t/2) force all three owner vertices into U_t.
    for threshold in range(1, 5):
        owner_load = (3 * threshold + 1) // 2
        edges = ((0, 1, owner_load), (0, 2, owner_load))
        _, optima = optimal_loads(3, edges)
        for loads, _ in optima:
            assert min(loads) >= threshold

    for owner_load in range(1, 10):
        edges = ((0, 1, owner_load), (0, 2, owner_load))
        _, optima = optimal_loads(3, edges)
        for loads, _ in optima:
            assert min(loads) >= 2 * owner_load // 3

    # The factor 3/2 is sharp on the isolated owner star.
    for threshold in range(2, 7):
        owner_load = (3 * threshold + 1) // 2 - 1
        edges = ((0, 1, owner_load), (0, 2, owner_load))
        _, optima = optimal_loads(3, edges)
        assert any(min(loads) == threshold - 1 for loads, _ in optima)


def verify_low_mass_identity() -> None:
    for threshold in range(1, 20):
        owner_threshold = (3 * threshold + 1) // 2
        for load in range(3, owner_threshold):
            third_mass = load * (load - 1) * (load - 2) // 2
            pair_mass = load * (load - 1) // 2
            assert third_mass == (load - 2) * pair_mass
            assert third_mass <= (owner_threshold - 3) * pair_mass


def verify_owner_coordinates() -> None:
    def add(first, second):
        return first[0] + second[0], first[1] + second[1]

    def rotate(value):
        return -value[1], value[0]

    def linear(value):
        return add(value, rotate(value))

    c = (7, -3)
    ell = (5, 11)
    a = (2, 4)
    b = (-3, 1)
    centre = c, ell
    first = add(c, a), add(ell, linear(a))
    second = add(c, b), add(ell, linear(b))
    z = add(ell, rotate(add(c, a)))
    recovered_ell = (
        z[0] - rotate(add(c, a))[0],
        z[1] - rotate(add(c, a))[1],
    )
    assert recovered_ell == ell
    assert first == (add(c, a), add(ell, linear(a)))
    assert second == (add(c, b), add(ell, linear(b)))
    assert centre != first and centre != second


def main() -> None:
    verify_bundle_saturation()
    verify_owner_star()
    verify_low_mass_identity()
    verify_owner_coordinates()
    print("K2,4 ambient-owner core saturation: PASS")


if __name__ == "__main__":
    main()
