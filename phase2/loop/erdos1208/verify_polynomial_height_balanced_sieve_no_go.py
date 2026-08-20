#!/usr/bin/env python3
"""Checks for POLYNOMIAL_HEIGHT_BALANCED_SIEVE_GLOBAL_DIRECTIONAL_NO_GO.md."""

from __future__ import annotations

from itertools import combinations
from math import gcd, isqrt
import sys

sys.path.insert(0, "phase2/loop/erdos1208")

from verify_ambient_centroid_endpoint_difference_hypergraph_gate import (  # noqa: E402
    direction_occupancies,
    is_distance_sidon,
    residue_parabola,
    sub,
)
from verify_global_directional_short_compensator_no_go import (  # noqa: E402
    balanced_transform,
    collision_signature,
)

Point = tuple[int, int]


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\1") * (limit + 1)
    sieve[:2] = b"\0\0"
    for prime in range(2, isqrt(limit) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\0" * (
                (limit - prime * prime) // prime + 1
            )
    return [number for number in range(2, limit + 1) if sieve[number]]


def root_count(prime: int) -> int:
    return sum(
        (residue * residue + residue + 1) % prime == 0
        for residue in range(prime)
    )


def is_vector_sidon(points: list[Point]) -> bool:
    seen: set[Point] = set()
    for first, second in combinations(points, 2):
        vector = sub(second, first)
        canonical = min(vector, (-vector[0], -vector[1]))
        if canonical in seen:
            return False
        seen.add(canonical)
    return True


def check_certificate(prime: int, parameter: int) -> None:
    base = residue_parabola(prime)
    points = balanced_transform(base, parameter)
    delta = parameter * parameter + parameter + 1

    assert is_vector_sidon(base)
    assert is_distance_sidon(points)
    assert all(delta % ell for ell in primes_up_to(4 * prime * prime - 1))

    signatures: dict[tuple[int, int, int], Point] = {}
    for first, second in combinations(range(prime), 2):
        vector = sub(base[second], base[first])
        signature = collision_signature(vector)
        assert signature not in signatures
        signatures[signature] = vector

    for a, b in direction_occupancies(base):
        image = (
            parameter * a - b,
            a + (parameter + 1) * b,
        )
        content = gcd(abs(image[0]), abs(image[1]))
        eisenstein_norm = a * a + a * b + b * b

        assert (parameter + 1) * image[0] + image[1] == delta * a
        assert -image[0] + parameter * image[1] == delta * b
        assert a * image[1] - b * image[0] == eisenstein_norm
        assert delta % content == 0
        assert eisenstein_norm % content == 0
        assert 0 < eisenstein_norm < 3 * prime * prime
        assert content == 1


def main() -> None:
    for prime in primes_up_to(200):
        if prime == 2:
            continue
        actual = root_count(prime)
        expected = 1 if prime == 3 else (2 if prime % 3 == 1 else 0)
        assert actual == expected

    certificates = {
        7: 14,
        11: 24,
        13: 27,
        17: 38,
    }
    expected_deltas = {
        7: 211,
        11: 601,
        13: 757,
        17: 1483,
    }
    for prime, parameter in certificates.items():
        assert parameter * parameter + parameter + 1 == expected_deltas[prime]
        check_certificate(prime, parameter)

    print("polynomial-height balanced sieve no-go: PASS")
    print("rough genuine certificates:", certificates)


if __name__ == "__main__":
    main()
