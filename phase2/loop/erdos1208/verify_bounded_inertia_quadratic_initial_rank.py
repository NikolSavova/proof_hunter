#!/usr/bin/env python3
"""Exact quadratic-initial-form rank for the rank-221 capped tower."""

from __future__ import annotations

from fractions import Fraction

from verify_bounded_inertia_rank221 import RANK, USEFUL_COUNT, prime_sieve


def gf2_incremental_rank(rows: list[tuple[int, str]]) -> tuple[int, dict[str, int]]:
    basis: dict[int, int] = {}
    dependencies: dict[str, int] = {}
    for row, category in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in basis:
                row ^= basis[pivot]
            else:
                basis[pivot] = row
                break
        if not row:
            dependencies[category] = dependencies.get(category, 0) + 1
    return len(basis), dependencies


def main() -> None:
    primes = prime_sieve(200_000)
    ramified = [p for p in primes if p != 2][: RANK + 1]
    ramified_set = set(ramified)

    # Eliminate the inertia generator at e=3 using the unique positive
    # squareclass relation.  The remaining d inertia generators are the
    # degree-one basis.
    eliminated = ramified.index(3)
    retained = [i for i in range(RANK + 1) if i != eliminated]
    position = {old: new for new, old in enumerate(retained)}
    is_three_mod_four = [p % 4 == 3 for p in ramified]

    # Coordinate the commutator part of the degree-two restricted Lie
    # algebra by lexicographically ordered pairs 0<=i<j<d.
    offsets: list[int] = []
    commutator_dimension = 0
    for i in range(RANK):
        offsets.append(commutator_dimension)
        commutator_dimension += RANK - i - 1
    assert commutator_dimension == RANK * (RANK - 1) // 2

    def pair_coordinate(a: int, b: int) -> int:
        if a > b:
            a, b = b, a
        assert a < b
        return offsets[a] + b - a - 1

    def clique(vector: int) -> int:
        """Commutator part of the restricted square vector^[2]."""
        row = 0
        remaining = vector
        while remaining:
            low_bit = remaining & -remaining
            i = low_bit.bit_length() - 1
            row ^= (vector >> (i + 1)) << offsets[i]
            remaining -= low_bit
        return row

    rows: list[tuple[int, str]] = []

    # The d retained inertia-square caps give d independent pure-square
    # coordinates.  Work modulo that direct summand below.  The eliminated
    # inertia has Frattini vector equal to the sum of all retained 3 mod 4
    # inertia vectors; its square leaves this clique commutator part.
    eliminated_vector = 0
    for old in retained:
        if is_three_mod_four[old]:
            eliminated_vector ^= 1 << position[old]
    rows.append((clique(eliminated_vector), "eliminated inertia cap"))

    # Koch's quadratic local relation at p_i is
    # X_i^[2 a_i] + sum_j ell_ij [X_i,X_j], with ell_ij=1 iff
    # p_i is a nonsquare modulo p_j.  The retained inertia caps remove the
    # pure-square terms.  Substituting the eliminated generator adds
    # ell_i,e to every retained 3 mod 4 column.
    for old_i in retained:
        row = 0
        link_to_eliminated = (
            pow(
                ramified[old_i],
                (ramified[eliminated] - 1) // 2,
                ramified[eliminated],
            )
            == ramified[eliminated] - 1
        )
        for old_j in retained:
            if old_i == old_j:
                continue
            linking = (
                pow(
                    ramified[old_i],
                    (ramified[old_j] - 1) // 2,
                    ramified[old_j],
                )
                == ramified[old_j] - 1
            )
            coefficient = linking ^ (
                link_to_eliminated and is_three_mod_four[old_j]
            )
            if coefficient:
                row ^= 1 << pair_coordinate(
                    position[old_i], position[old_j]
                )
        rows.append((row, "base linking relator"))

    base_commutator_rank, base_dependencies = gf2_incremental_rank(rows)
    assert base_commutator_rank == RANK + 1
    assert not base_dependencies

    # The dual positive squareclass basis is p_i for p_i=1 mod 4 and
    # 3*p_i for retained p_i=3 mod 4.  Its Legendre values give the
    # Frattini vector of an unramified Frobenius element.
    useful: list[int] = []
    zero_vectors = 0
    for q in primes:
        if q == 2 or q in ramified_set:
            continue
        vector = 0
        for old in retained:
            radicand = ramified[old]
            if is_three_mod_four[old]:
                radicand *= ramified[eliminated]
            if pow(radicand, (q - 1) // 2, q) == q - 1:
                vector ^= 1 << position[old]
        if q % 4 == 1 or vector:
            useful.append(q)
            if not vector:
                zero_vectors += 1
            rows.append((clique(vector), "useful Frobenius cap"))
        if len(useful) == USEFUL_COUNT:
            break

    assert useful[0] == 1_423 and useful[-1] == 128_047
    assert zero_vectors == 0

    commutator_rank, dependencies = gf2_incremental_rank(rows)
    assert commutator_rank == (RANK + 1) + USEFUL_COUNT == 11_989
    assert not dependencies

    # Restore the direct pure-square summand from the d retained inertia
    # caps.  Every displayed relation has an independent quadratic initial
    # form; none can be promoted to Zassenhaus degree three by row reduction.
    total_quadratic_rank = RANK + commutator_rank
    total_relation_count = RANK + (RANK + 1) + USEFUL_COUNT
    assert total_quadratic_rank == total_relation_count == 12_210

    # A deliberately zero-linking comparison: these 19 primes are 1 mod 4
    # and pairwise quadratic residues.  It verifies that the mechanism is
    # real, while recording how rapidly the smallest greedy example grows.
    residue_clique = [
        5,
        29,
        109,
        281,
        349,
        1_601,
        1_889,
        5_581,
        12_421,
        14_389,
        16_829,
        89_501,
        294_761,
        471_781,
        1_134_389,
        2_465_081,
        2_708_941,
        4_695_809,
        9_594_709,
    ]

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        divisor = 3
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 2
        return True

    assert all(is_prime(p) for p in residue_clique)
    assert all(p % 4 == 1 for p in residue_clique)
    for i, p in enumerate(residue_clique):
        for q in residue_clique[i + 1 :]:
            assert pow(p, (q - 1) // 2, q) == 1

    # With the additional prime 3 eliminated, the safe weighted polynomial
    # is 1-dt+(d+N)t^2+d t^3+t^4.  This exact stress shows that 69 useful
    # caps fit at d=19, versus only 51 under the all-quadratic count.
    structured_rank = len(residue_clique)
    structured_useful = 69
    test_t = Fraction(261, 2_500)  # 0.1044
    structured_polynomial = (
        1
        - structured_rank * test_t
        + (structured_rank + structured_useful) * test_t**2
        + structured_rank * test_t**3
        + test_t**4
    )
    assert structured_polynomial < 0

    print("rank / ramified / useful:", RANK, len(ramified), len(useful))
    print("commutator dimension:", commutator_dimension)
    print("base capped commutator rank:", base_commutator_rank)
    print("full commutator rank:", commutator_rank)
    print("pure-square rank:", RANK)
    print("total quadratic rank / relations:", total_quadratic_rank, total_relation_count)
    print("zero Frattini useful vectors:", zero_vectors)
    print("zero-linking stress clique size / last:", len(residue_clique), residue_clique[-1])
    print("zero-linking d=19 / useful=69 weighted P(0.1044):", structured_polynomial)
    print("bounded-inertia quadratic initial forms: FULL RANK")


if __name__ == "__main__":
    main()
