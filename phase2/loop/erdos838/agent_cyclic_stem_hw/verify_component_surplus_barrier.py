#!/usr/bin/env python3
"""Exact verifier for COMPONENT_SURPLUS_PAIR_TELESCOPE_BARRIER.md."""

from __future__ import annotations

from decimal import Decimal, getcontext
from math import isqrt


def inv_mod(a: int, q: int) -> int:
    return pow(a % q, q - 2, q)


def normalized_projective_vectors(q: int) -> list[tuple[int, int, int]]:
    """Canonical representatives of one-dimensional subspaces of F_q^3."""
    out: list[tuple[int, int, int]] = []
    seen: set[tuple[int, int, int]] = set()
    for x in range(q):
        for y in range(q):
            for z in range(q):
                if x == y == z == 0:
                    continue
                v = (x, y, z)
                first = next(t for t in v if t)
                s = inv_mod(first, q)
                w = tuple((s * t) % q for t in v)
                if w not in seen:
                    seen.add(w)
                    out.append(w)
    return sorted(out)


def incidence_graph(q: int) -> list[list[int]]:
    vec = normalized_projective_vectors(q)
    return [
        [int(sum(p[k] * ell[k] for k in range(3)) % q == 0) for ell in vec]
        for p in vec
    ]


def graph_audit(q: int) -> dict[str, int]:
    a = incidence_graph(q)
    n = len(a)
    d = q + 1
    assert n == q * q + q + 1
    assert all(sum(row) == d for row in a)
    assert all(sum(a[i][j] for i in range(n)) == d for j in range(n))

    c4 = 0
    inj = 0
    for i in range(n):
        for k in range(n):
            codeg = sum(a[i][j] * a[k][j] for j in range(n))
            assert codeg == (d if i == k else 1)
            c4 += codeg * codeg
            if i != k:
                inj += codeg * (codeg - 1)
    expected = n * (d * d + n - 1)
    assert c4 == expected
    assert inj == 0
    return {"q": q, "N": n, "d": d, "m": n * d, "C": c4}


def exhaustive_two_thirds() -> int:
    """Check V^6 >= m^4 with V=max(active supports,ceil(sqrt(C4)))."""
    checked = 0
    nl = nr = 3
    for mask in range(1, 1 << (nl * nr)):
        a = [
            [(mask >> (i * nr + j)) & 1 for j in range(nr)]
            for i in range(nl)
        ]
        dl = [sum(row) for row in a]
        dr = [sum(a[i][j] for i in range(nl)) for j in range(nr)]
        m = sum(dl)
        c4 = sum(
            sum(a[i][j] * a[k][j] for j in range(nr)) ** 2
            for i in range(nl)
            for k in range(nl)
        )
        root = isqrt(c4)
        ceil_root = root if root * root == c4 else root + 1
        v = max(sum(d > 0 for d in dl), sum(d > 0 for d in dr), ceil_root)
        assert v**6 >= m**4
        checked += 1
    return checked


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p <= isqrt(n):
        if n % p == 0:
            return False
        p += 2
    return True


def next_prime(n: int) -> int:
    while not is_prime(n):
        n += 1
    return n


def tensor_counts(base: dict[str, int], h: int) -> dict[str, int]:
    return {
        "vertices_one_side": base["N"] ** h,
        "degree": base["d"] ** h,
        "edges": base["m"] ** h,
        "c4": base["C"] ** h,
    }


def exact_capacity_ratio(q: int, h: int) -> tuple[int, int, int]:
    # Formula audit works for every prime power; q is prime here.
    n = q * q + q + 1
    d = q + 1
    m = n * d
    c = n * (d * d + n - 1)
    records_squared = m ** (2 * h)
    component_pairs = 4 * n ** (2 * h)
    rectangles = c**h
    transcript = (2 * h + 1) ** (4 * h)
    certified_capacity = transcript * max(component_pairs, rectangles)
    return records_squared, certified_capacity, records_squared // certified_capacity


def main() -> None:
    getcontext().prec = 50
    checked = exhaustive_two_thirds()
    print("exact 3x3 two-thirds graph audits:", checked)
    for q in (2, 3, 5, 7):
        b = graph_audit(q)
        print("PG", q, b)
        for h in (1, 2, 3):
            t = tensor_counts(b, h)
            assert t["edges"] == t["vertices_one_side"] * t["degree"]
            assert t["c4"] == b["C"] ** h

    print("critical tensor capacity stress")
    previous_bits = -1
    for h in (8, 12, 16, 20, 24, 28, 32):
        q = next_prime(1 << h)
        rec2, cap, quotient = exact_capacity_ratio(q, h)
        # Integer bit-length is a rigorous floor/ceiling proxy for log2.
        deficit_bits = rec2.bit_length() - cap.bit_length()
        if h >= 16:
            assert deficit_bits > 0
        if h >= 20:
            assert deficit_bits > previous_bits
        previous_bits = deficit_bits
        scaled = Decimal(deficit_bits) / Decimal(h * h)
        print(
            "h=",
            h,
            "q=",
            q,
            "deficit_bits=",
            deficit_bits,
            "deficit/h^2=",
            f"{scaled:.8f}",
            "integer_quotient_positive=",
            quotient > 0,
        )

    print("PASS: exact projective-plane tensor component-surplus barrier")


if __name__ == "__main__":
    main()
