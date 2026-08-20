#!/usr/bin/env python3
"""Exact cup-product obstruction to deleting the quadratic-base +1 relation.

For the 227- and 229-prime-ideal Q(sqrt(1949)) prefixes, this reconstructs
the totally-positive/dyadically-unramified Kummer space, all tame local
Hilbert symbols, and the span of localized global cup products.  The latter
has rank |T|-1, proving r(G_T)=d(G_T)+1 exactly.
"""

from __future__ import annotations

import verify_real_quadratic_1949_bounded_inertia as base


UNIT_GENERATORS = [(-1, 0), (81_333, 3_770)]


def nullspace_basis(rows: list[int], column_count: int) -> list[int]:
    reduced = rows[:]
    pivots: list[int] = []
    row_index = 0
    for column in range(column_count):
        source = next(
            (
                index
                for index in range(row_index, len(reduced))
                if (reduced[index] >> column) & 1
            ),
            None,
        )
        if source is None:
            continue
        reduced[row_index], reduced[source] = reduced[source], reduced[row_index]
        for index in range(len(reduced)):
            if index != row_index and ((reduced[index] >> column) & 1):
                reduced[index] ^= reduced[row_index]
        pivots.append(column)
        row_index += 1
        if row_index == len(reduced):
            break

    free_columns = [
        column for column in range(column_count) if column not in pivots
    ]
    basis: list[int] = []
    for free in free_columns:
        vector = 1 << free
        for index, pivot in enumerate(pivots):
            if (reduced[index] >> free) & 1:
                vector |= 1 << pivot
        assert all((vector & row).bit_count() % 2 == 0 for row in rows)
        basis.append(vector)
    return basis


def prime_generators(ideals):
    cache: dict[int, tuple[int, int]] = {}
    generators: list[tuple[int, int]] = []
    for _, p, kind, root in ideals:
        if kind == "inert":
            generator = (p, 0)
        else:
            first = cache.setdefault(p, base.generator_of_prime(p))
            if kind == "ramified":
                generator = first
            else:
                assert root is not None
                second = base.conjugate(first)
                generator = (
                    first
                    if (first[0] + first[1] * root) % p == 0
                    else second
                )
                assert (generator[0] + generator[1] * root) % p == 0
        generators.append(generator)
    return generators


def constraint_rows(generators: list[tuple[int, int]]) -> list[int]:
    units_mod_four = [
        (a, b)
        for a in range(4)
        for b in range(4)
        if base.norm((a, b)) % 2
    ]

    def multiply_mod_four(left, right):
        product = base.multiply(left, right)
        return product[0] % 4, product[1] % 4

    square_residues = frozenset(
        multiply_mod_four(unit, unit) for unit in units_mod_four
    )
    cosets: list[frozenset[tuple[int, int]]] = []
    for unit in units_mod_four:
        coset = frozenset(
            multiply_mod_four(unit, square) for square in square_residues
        )
        if coset not in cosets:
            cosets.append(coset)
    assert len(units_mod_four) == 12
    assert len(square_residues) == 3
    assert len(cosets) == 4

    def coset_index(element):
        residue = element[0] % 4, element[1] % 4
        return next(index for index, coset in enumerate(cosets) if residue in coset)

    identity = cosets.index(square_residues)
    nonidentity = [index for index in range(4) if index != identity]
    coset_bits = {identity: 0, nonidentity[0]: 1, nonidentity[1]: 2}
    representatives = [next(iter(coset)) for coset in cosets]
    product_index = coset_index(
        multiply_mod_four(
            representatives[nonidentity[0]], representatives[nonidentity[1]]
        )
    )
    assert product_index == nonidentity[2]
    coset_bits[product_index] = 3

    def column(element):
        signs = base.negative_at_embedding(element, False)
        signs |= base.negative_at_embedding(element, True) << 1
        return signs | (coset_bits[coset_index(element)] << 2)

    columns = [column(element) for element in generators]
    rows = [
        sum(
            ((value >> bit) & 1) << index
            for index, value in enumerate(columns)
        )
        for bit in range(4)
    ]
    assert base.gf2_rank(rows) == 4
    return rows


def multiply_residue(left, right, p: int):
    constant = base.OMEGA_CONSTANT
    return (
        (left[0] * right[0] + constant * left[1] * right[1]) % p,
        (left[0] * right[1] + left[1] * right[0] + left[1] * right[1]) % p,
    )


def power_residue(element, exponent: int, p: int):
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = multiply_residue(result, element, p)
        element = multiply_residue(element, element, p)
        exponent //= 2
    return result


def local_nonsquare(element, ideal):
    norm_q, p, kind, root = ideal
    if kind in ("split", "ramified"):
        if kind == "ramified":
            assert p == base.FIELD_DISCRIMINANT
            root = (p + 1) // 2
        assert root is not None
        residue = (element[0] + element[1] * root) % p
        if residue == 0:
            return None
        return pow(residue, (p - 1) // 2, p) == p - 1

    assert kind == "inert" and norm_q == p * p
    residue = element[0] % p, element[1] % p
    if residue == (0, 0):
        return None
    sign = power_residue(residue, (p * p - 1) // 2, p)
    assert sign in ((1, 0), (p - 1, 0))
    return sign == (p - 1, 0)


def certify_prefix(ideal_count: int) -> tuple[int, int, int]:
    primes = base.prime_sieve(200_000)
    ideals = base.prime_ideals(primes, 200_000)[:ideal_count]
    generators = UNIT_GENERATORS + prime_generators(ideals)
    rows = constraint_rows(generators)
    kummer_basis = nullspace_basis(rows, len(generators))
    generator_rank = ideal_count - 2
    assert len(kummer_basis) == generator_rank

    # The two unit squareclasses are already separated locally at the
    # displayed primes.  Since h(E)=1, this proves V_T/E^{x2}=0, i.e. T is
    # saturated in the sense of Koch--Shafarevich.
    ideal_five = next(ideal for ideal in ideals if ideal == (5, 5, "split", 2))
    ideal_nineteen = next(
        ideal for ideal in ideals if ideal == (19, 19, "split", 4)
    )
    assert [local_nonsquare(unit, ideal_five) for unit in UNIT_GENERATORS] == [
        False,
        True,
    ]
    assert [
        local_nonsquare(unit, ideal_nineteen) for unit in UNIT_GENERATORS
    ] == [True, False]

    # For each local prime i, store the quadratic residue functional on all
    # global squareclass generators.  The i-th prime generator is our chosen
    # uniformizer, so its unit part is 1 and its diagonal entry is omitted.
    local_characters: list[int] = []
    for ideal_index, ideal in enumerate(ideals):
        character = 0
        for generator_index, generator in enumerate(generators):
            value = local_nonsquare(generator, ideal)
            if generator_index == ideal_index + len(UNIT_GENERATORS):
                assert value is None
                continue
            assert value is not None
            if value:
                character |= 1 << generator_index
        local_characters.append(character)

    unit_local_vectors = [
        sum(
            ((character >> unit_index) & 1) << ideal_index
            for ideal_index, character in enumerate(local_characters)
        )
        for unit_index in range(2)
    ]
    assert base.gf2_rank(unit_local_vectors) == 2

    valuation_mask = (1 << ideal_count) - 1
    valuations: list[int] = []
    unit_characters: list[int] = []
    for squareclass in kummer_basis:
        valuations.append((squareclass >> len(UNIT_GENERATORS)) & valuation_mask)
        local_vector = 0
        for ideal_index, character in enumerate(local_characters):
            if (squareclass & character).bit_count() % 2:
                local_vector |= 1 << ideal_index
        unit_characters.append(local_vector)

    minus_one_nonsquare = sum(
        (ideal[0] % 4 == 3) << index for index, ideal in enumerate(ideals)
    )

    # At an odd local field with residue cardinality Q, the Hilbert-symbol
    # bit for x=pi^a u and y=pi^b v is
    #   ab*(Q-1)/2 + b*Legendre(u) + a*Legendre(v).
    # These are exactly the localizations of the global cup products.
    cup_basis: dict[int, int] = {}
    odd_reciprocity_vectors = 0
    for left in range(generator_rank):
        for right in range(left, generator_rank):
            cup = (
                (
                    valuations[left]
                    & valuations[right]
                    & minus_one_nonsquare
                )
                ^ (valuations[right] & unit_characters[left])
                ^ (valuations[left] & unit_characters[right])
            )
            # The classes are positive and unramified at 2; all omitted
            # local Hilbert symbols vanish.  Global reciprocity is therefore
            # the even-parity identity on these finite tame coordinates.
            if cup.bit_count() % 2:
                odd_reciprocity_vectors += 1
            row = cup
            while row:
                pivot = row.bit_length() - 1
                if pivot in cup_basis:
                    row ^= cup_basis[pivot]
                else:
                    cup_basis[pivot] = row
                    break

    cup_rank = len(cup_basis)
    assert odd_reciprocity_vectors == 0
    assert cup_rank == ideal_count - 1 == generator_rank + 1
    return generator_rank, cup_rank, len(kummer_basis)


def main() -> None:
    assert base.FIELD_DISCRIMINANT == 1_949
    assert base.norm(UNIT_GENERATORS[1]) == -1
    results = {count: certify_prefix(count) for count in (227, 229)}
    assert results == {227: (225, 226, 225), 229: (227, 228, 227)}
    for count, (generator_rank, cup_rank, _) in results.items():
        print(
            "ideals / generators / localized cup rank:",
            count,
            generator_rank,
            cup_rank,
        )
    print("quadratic-1949 base relation excess +1: EXACT AND UNAVOIDABLE")


if __name__ == "__main__":
    main()
