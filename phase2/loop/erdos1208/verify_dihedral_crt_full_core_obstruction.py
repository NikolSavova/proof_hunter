#!/usr/bin/env python3
"""Exact checks for the generalized-dihedral full-core obstruction."""

from __future__ import annotations

from math import gcd

from search_full_eight_corner_core import analyze_mod_coalesced, components, relation_tuples
from search_matching_switch_full_core import is_linear_full_core


Matching = tuple[int, ...]


def crt_shifts(p: int, q: int, r: int) -> tuple[int, ...]:
    return tuple(
        (i * q * r + j * p * r + k * p * q) % (p * q * r)
        for k in (0, 1)
        for j in (0, 1)
        for i in (0, 1)
    )


def ordinary_dihedral_matchings(p: int, q: int, r: int) -> tuple[Matching, ...]:
    n = p * q * r
    answer = []
    for shift in crt_shifts(p, q, r):
        # Encode (x,sigma) as 2*x+sigma.  Right multiplication by the
        # reflection (shift,1) sends it to
        # (x+(-1)^sigma shift, sigma+1).
        answer.append(
            tuple(
                2 * ((x + (shift if sigma == 0 else -shift)) % n)
                + (sigma ^ 1)
                for x in range(n)
                for sigma in range(2)
            )
        )
    return tuple(answer)


def ordinary_endpoint_map(
    p: int, q: int, r: int, role: int, bit: int
) -> tuple[int, ...]:
    n = p * q * r
    moduli = (p, q, r)
    coefficients = (q * r, p * r, p * q)
    modulus = moduli[role]
    offset = bit * coefficients[role]
    return tuple(
        (x - sigma * offset) % modulus
        for x in range(n)
        for sigma in range(2)
    )


def product_index(
    x: int, y: int, z: int, sigma: int, q: int, r: int
) -> int:
    return 2 * ((x * q + y) * r + z) + sigma


def generalized_dihedral_matchings(
    p: int, q: int, r: int
) -> tuple[Matching, ...]:
    """Right multiplication by the eight reflections of
    (Z_p x Z_q x Z_r) semidirect {+1,-1}.
    """
    answer = []
    for k in (0, 1):
        for j in (0, 1):
            for i in (0, 1):
                answer.append(
                    tuple(
                        product_index(
                            (x + (i if sigma == 0 else -i)) % p,
                            (y + (j if sigma == 0 else -j)) % q,
                            (z + (k if sigma == 0 else -k)) % r,
                            sigma ^ 1,
                            q,
                            r,
                        )
                        for x in range(p)
                        for y in range(q)
                        for z in range(r)
                        for sigma in range(2)
                    )
                )
    return tuple(answer)


def product_endpoint_map(
    p: int, q: int, r: int, role: int, bit: int
) -> tuple[int, ...]:
    moduli = (p, q, r)
    return tuple(
        ((x, y, z)[role] - sigma * bit) % moduli[role]
        for x in range(p)
        for y in range(q)
        for z in range(r)
        for sigma in range(2)
    )


def canonicalize(values: tuple[int, ...]) -> tuple[int, ...]:
    names: dict[int, int] = {}
    return tuple(names.setdefault(value, len(names)) for value in values)


def verify(p: int, q: int, r: int) -> None:
    assert p >= 2 and q >= 2 and r >= 2
    matchings = generalized_dihedral_matchings(p, q, r)
    assert all(
        matching[matching[record]] == record
        and matching[record] != record
        for matching in matchings
        for record in range(len(matching))
    )
    assert is_linear_full_core(matchings)

    # The connected components of each four-colour face are exactly the
    # displayed product-coordinate labels.
    for role in range(3):
        for bit in range(2):
            selected = tuple(
                matchings[mask]
                for mask in range(8)
                if ((mask >> role) & 1) == bit
            )
            actual = canonicalize(components(selected))
            expected = canonicalize(product_endpoint_map(p, q, r, role, bit))
            assert actual == expected

    data = relation_tuples(matchings)
    assert data is not None
    relations, variables = data
    assert len(relations) == 2 * p * q * r
    assert variables == 2 * (p + q + r)
    assert analyze_mod_coalesced(matchings) == (
        variables,
        6,
        5,
        0,
        1,
        0,
    )

    # When the moduli are pairwise coprime, the product group is cyclic and
    # the same construction is the ordinary dihedral CRT model.  Check that
    # presentation independently, including its scalar face labels.
    if gcd(p, q) == gcd(p, r) == gcd(q, r) == 1:
        ordinary = ordinary_dihedral_matchings(p, q, r)
        shift_values = crt_shifts(p, q, r)
        assert len(set(shift_values)) == 8
        assert is_linear_full_core(ordinary)
        for role in range(3):
            for bit in range(2):
                selected = tuple(
                    ordinary[mask]
                    for mask in range(8)
                    if ((mask >> role) & 1) == bit
                )
                assert canonicalize(components(selected)) == canonicalize(
                    ordinary_endpoint_map(p, q, r, role, bit)
                )
        assert analyze_mod_coalesced(ordinary) == (
            variables,
            6,
            5,
            0,
            1,
            0,
        )
    print((p, q, r), "records", len(relations), "formal points", variables)


def main() -> None:
    for parameters in (
        (2, 2, 2),
        (2, 3, 4),
        (2, 4, 6),
        (2, 3, 5),
        (3, 4, 5),
        (2, 5, 7),
        (3, 5, 7),
        (5, 7, 11),
    ):
        verify(*parameters)
    print("generalized-dihedral full-core obstruction: PASS")


if __name__ == "__main__":
    main()
