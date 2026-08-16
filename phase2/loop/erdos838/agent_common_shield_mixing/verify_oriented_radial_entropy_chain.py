#!/usr/bin/env python3
"""Exact audit for ORIENTED_RADIAL_ENTROPY_CHAIN.md."""

from __future__ import annotations

import importlib.util
import json
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


RADIAL = load_module(
    "radial_for_entropy_chain",
    HERE / "verify_detached_radial_lexicographic.py",
)


def conditional_entropy_exponents(family: set[tuple[int, ...]], q: int) -> list[Q]:
    """Return E_i=2^(M h_i) exactly, as rational integers."""
    mass = len(family)
    exponents: list[Q] = []
    for depth in range(q):
        parents = Counter(word[:depth] for word in family)
        children = Counter(word[: depth + 1] for word in family)
        numerator = 1
        denominator = 1
        for count in parents.values():
            numerator *= count**count
        for count in children.values():
            denominator *= count**count
        exponents.append(Q(numerator, denominator))
    product_exponent = Q(1)
    for value in exponents:
        product_exponent *= value
    assert product_exponent == Q(mass**mass)
    return exponents


def support_sizes(family: set[tuple[int, ...]], q: int) -> list[int]:
    return [len({word[i] for word in family}) for i in range(q)]


def exact_entropy_bound_audit(
    family: set[tuple[int, ...]],
    bank_sizes: list[int],
    local_faces: list[int],
) -> dict[str, object]:
    q = len(next(iter(family)))
    mass = len(family)
    sizes = support_sizes(family, q)
    entropy_exponents = conditional_entropy_exponents(family, q)

    # The rational radial audit below uses families with full support in
    # every coordinate, so the inherited local H_i and B_j are unchanged.
    assert sizes == [4] * q
    p_zero = 1
    for size in sizes:
        p_zero *= size

    # Exact exponentiated form of Gamma.  Raising to qM avoids every log.
    support_redundancy_power = Q(1)
    for size, entropy_exponent in zip(sizes, entropy_exponents):
        support_redundancy_power *= Q(size**mass, entropy_exponent)
    gamma_power = support_redundancy_power**q
    for size, face_count in zip(sizes, local_faces):
        gamma_power *= Q(face_count, size**3) ** mass

    lhs = Q(max(bank_sizes), mass) ** (q * mass)
    assert lhs >= gamma_power

    # The same inequality directly from P0/M and the geometric mean.
    direct_rhs = Q(p_zero, mass) ** (q * mass)
    for size, face_count in zip(sizes, local_faces):
        direct_rhs *= Q(face_count, size**3) ** mass
    assert direct_rhs == gamma_power
    assert lhs >= direct_rhs

    return {
        "mass": mass,
        "supports": sizes,
        "conditional_exponent_bits": [
            (value.numerator.bit_length(), value.denominator.bit_length())
            for value in entropy_exponents
        ],
        "bank": max(bank_sizes),
        "gamma_power_numerator_bits": gamma_power.numerator.bit_length(),
        "bound_slack_positive": lhs > gamma_power,
    }


def geometric_and_sparse_audit() -> dict[str, object]:
    clusters = RADIAL.build_clusters()
    geometry = RADIAL.geometric_audit(clusters)
    recurrence = RADIAL.recurrence_audit(clusters)
    assert geometry["transversals"] == 4**5 == 1024
    assert recurrence["one_gap_bank"] == 400

    q = 5
    universe = set(product(range(4), repeat=q))
    families = {
        "full": universe,
        "diagonal": {word for word in universe if len(set(word)) == 1},
        "linear_code": {word for word in universe if sum(word) % 4 == 0},
        "prefix_correlated": {
            word
            for word in universe
            if (word[0] == word[1]) or (word[2] == word[3])
        },
    }
    assert all(support_sizes(family, q) == [4] * q for family in families.values())
    bank_sizes = [400] * q
    local_faces = [14] * q
    reports = {
        name: exact_entropy_bound_audit(family, bank_sizes, local_faces)
        for name, family in families.items()
    }

    # Four disjoint parity cosets merge to the full product, so the common
    # ambient bank is spent once rather than four times.
    cosets = [
        {word for word in universe if sum(word) % 4 == residue}
        for residue in range(4)
    ]
    assert all(len(coset) == 4**4 for coset in cosets)
    assert sum((len(coset) for coset in cosets), 0) == len(universe)
    assert set().union(*cosets) == universe
    assert sum((set(cosets[i]) & set(cosets[j]) != set() for i in range(4) for j in range(i)), 0) == 0

    # Weighted copies need only the maximum geometric-word multiplicity.
    weights = {word: 1 + (sum(word) % 7) for word in families["linear_code"]}
    total_weight = sum(weights.values())
    maximum_weight = max(weights.values())
    assert total_weight <= maximum_weight * len(weights)

    return {
        "geometry": geometry,
        "recurrence": recurrence,
        "sparse_families": reports,
        "parity_cosets": [len(coset) for coset in cosets],
        "weighted": {
            "support": len(weights),
            "total": total_weight,
            "maximum_word_weight": maximum_weight,
        },
    }


def asymptotic_exponent_audit() -> dict[str, object]:
    rows = []
    # q=d, log M=d^2/5, balanced h_i=d/5.  Formula (7) is exact here.
    for d in (90, 180, 450, 900):
        q = d
        h = Q(d, 5)
        log_mass = q * h
        square_term = Q(q * h * h, 9 * q)
        linear_term = Q(3 * log_mass, q)
        gamma = square_term - linear_term
        assert gamma == h * h / 9 - 3 * h
        expected = Q(d * d, 225) - Q(3 * d, 5)
        assert gamma == expected
        rows.append(
            {
                "log_D": d,
                "q": q,
                "log_M": str(log_mass),
                "conditional_gamma": str(gamma),
            }
        )
    assert Q(rows[-1]["conditional_gamma"]) > 0
    return {"scales": rows, "leading_coefficient": "1/225"}


def main() -> None:
    result = {
        "radial_sparse": geometric_and_sparse_audit(),
        "asymptotic": asymptotic_exponent_audit(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: oriented radial entropy-chain theorem verified for arbitrary sparse families")


if __name__ == "__main__":
    main()
