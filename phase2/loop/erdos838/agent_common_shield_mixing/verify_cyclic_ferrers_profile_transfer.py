#!/usr/bin/env python3
"""Exact audit for CYCLIC_FERRERS_PROFILE_TRANSFER.md."""

from __future__ import annotations

import json
import random
from itertools import product


def compatible(edge: int, left: int, right: int) -> bool:
    """Zero-based edge: even means <=, odd means >=."""
    return left <= right if edge % 2 == 0 else left >= right


def valid_word(word: tuple[int, ...]) -> bool:
    q = len(word)
    return all(compatible(i, word[i], word[(i + 1) % q]) for i in range(q))


def exact_transfer_audit() -> dict[str, object]:
    # Profile counts are q-th powers, making the wordwise geometric mean
    # integral.  This verifies the AM--GM transfer without floating point.
    rng = random.Random(838)
    systems = 0
    for _ in range(300):
        q = rng.choice((3, 4, 5))
        alphabet = tuple(range(rng.randint(2, 4)))
        all_words = tuple(product(alphabet, repeat=q))
        selected = tuple(word for word in all_words if rng.randrange(3) != 0)
        if not selected:
            selected = (all_words[0],)

        left_roots = [
            [rng.randint(1, 4) for _ in alphabet] for _ in range(q)
        ]
        right_roots = [
            [rng.randint(1, 4) for _ in alphabet] for _ in range(q)
        ]
        a = [[value**q for value in row] for row in left_roots]
        r = [[value**q for value in row] for row in right_roots]

        banks = []
        for seam in range(q):
            banks.append(
                sum(
                    r[seam][word[seam]]
                    * a[(seam + 1) % q][word[(seam + 1) % q]]
                    for word in selected
                )
            )

        geometric_sum = 0
        for word in selected:
            # Since every a_i and r_i is a q-th power, the q-th root of
            # product_i a_i r_i is the following exact integer.
            term = 1
            for i in range(q):
                term *= left_roots[i][word[i]] * right_roots[i][word[i]]
            geometric_sum += term
        assert max(banks) * q >= sum(banks)
        assert sum(banks) >= q * geometric_sum
        assert max(banks) >= geometric_sum
        systems += 1
    return {"exact_random_systems": systems}


def max_kernel_power_trace(alphabet: int, power: int) -> int:
    """Trace of K^power for K[a,b]=alphabet-max(a,b), zero-based."""
    # Repeated left multiplication by K.  Its nested rows allow each
    # matrix column to be updated in O(alphabet), so the whole exact audit
    # costs O(power*alphabet^2), not dense cubic multiplication.
    matrix = [
        [1 if row == column else 0 for column in range(alphabet)]
        for row in range(alphabet)
    ]
    for _ in range(power):
        updated = [[0] * alphabet for _ in range(alphabet)]
        for column in range(alphabet):
            prefix = [0] * alphabet
            running = 0
            for index in range(alphabet):
                running += matrix[index][column]
                prefix[index] = running
            suffix_weighted = [0] * (alphabet + 1)
            running = 0
            for index in range(alphabet - 1, -1, -1):
                running += (alphabet - index) * matrix[index][column]
                suffix_weighted[index] = running
            for row in range(alphabet):
                updated[row][column] = (
                    (alphabet - row) * prefix[row]
                    + suffix_weighted[row + 1]
                )
        matrix = updated
    return sum(matrix[index][index] for index in range(alphabet))


def direct_alternating_count(alphabet: int, q: int) -> int:
    assert q % 2 == 0
    return sum(1 for word in product(range(1, alphabet + 1), repeat=q) if valid_word(word))


def ferrers_and_barrier_audit() -> dict[str, object]:
    # Literal exhaustive small instance.
    alphabet, q, profiles_per_anchor = 4, 4, 16
    words = tuple(
        word for word in product(range(1, alphabet + 1), repeat=q) if valid_word(word)
    )
    assert len(words) == direct_alternating_count(alphabet, q)
    assert len(words) == max_kernel_power_trace(alphabet, q // 2)

    for seam in range(q):
        neighborhoods = []
        for left in range(1, alphabet + 1):
            neighborhoods.append(
                frozenset(
                    right
                    for right in range(1, alphabet + 1)
                    if compatible(seam, left, right)
                )
            )
        assert all(
            first <= second or second <= first
            for first in neighborhoods
            for second in neighborhoods
        )

    # Every label appears in every position, witnessed already by the
    # constant valid word.
    for position in range(q):
        assert {word[position] for word in words} == set(range(1, alphabet + 1))

    def rich(position: int, value: int) -> bool:
        return value > alphabet // 2 if position % 2 == 0 else value <= alphabet // 2

    directional_total = alphabet // 2 * profiles_per_anchor
    small_directional_total = directional_total
    seam_banks = []
    for seam in range(q):
        bank = 0
        for word in words:
            if rich(seam, word[seam]) and rich(
                (seam + 1) % q, word[(seam + 1) % q]
            ):
                bank += profiles_per_anchor**2
        assert bank == 0
        seam_banks.append(bank)

    # The on-word product is zero for every word, while every unweighted
    # local directional product is large.
    assert all(not all(rich(i, word[i]) for i in range(q)) for word in words)
    local_reservoir = directional_total**2
    small_local_reservoir = local_reservoir
    assert local_reservoir > 0

    scales = []
    for d in (4, 6, 8):
        alphabet = 1 << d
        q = d
        valid_count = max_kernel_power_trace(alphabet, q // 2)
        lower = (alphabet // 2) ** q
        upper = alphabet**q
        assert lower <= valid_count <= upper

        profiles_per_anchor = 1 << (d * d)
        directional_total = alphabet // 2 * profiles_per_anchor
        local_reservoir = directional_total**2
        false_totals_multiplier = profiles_per_anchor**2 // 4
        assert local_reservoir.bit_length() - 1 == 2 * d * d + 2 * d - 2
        assert false_totals_multiplier.bit_length() - 1 == 2 * d * d - 2
        scales.append(
            {
                "log_D": d,
                "cycle_length": q,
                "alphabet": alphabet,
                "valid_words_bits": valid_count.bit_length(),
                "entropy_lower_exponent": d * d - d,
                "entropy_upper_exponent": d * d,
                "local_reservoir_log2": local_reservoir.bit_length() - 1,
                "false_totals_multiplier_log2": (
                    false_totals_multiplier.bit_length() - 1
                ),
                "actual_profile_seam_bank": 0,
            }
        )

    return {
        "small_alphabet": 4,
        "small_cycle": 4,
        "small_valid_words": len(words),
        "small_directional_total": small_directional_total,
        "small_local_reservoir": small_local_reservoir,
        "small_seam_banks": seam_banks,
        "scales": scales,
    }


def independent_ear_audit() -> dict[str, object]:
    rng = random.Random(839)
    systems = 0
    for q in range(3, 13):
        if q % 2 == 0:
            colors = (tuple(range(0, q, 2)), tuple(range(1, q, 2)))
        else:
            # Even/odd coloring of the first q-1 path, with the last vertex
            # alone as the third independent class.
            colors = (
                tuple(range(0, q - 1, 2)),
                tuple(range(1, q - 1, 2)),
                (q - 1,),
            )
        chi = len(colors)
        assert {vertex for color in colors for vertex in color} == set(range(q))
        for color in colors:
            assert all(
                (left - right) % q not in (1, q - 1)
                for left in color
                for right in color
                if left != right
            )

        for _ in range(40):
            a = [rng.randint(1, 20) for _ in range(q)]
            r = [rng.randint(1, 20) for _ in range(q)]
            h = [rng.randint(1, a[i] * r[i]) for i in range(q)]
            banks = []
            for color in colors:
                bank = 1
                for i in color:
                    bank *= max(a[i], r[i])
                banks.append(bank)
            product_h = 1
            for value in h:
                product_h *= value
            assert max(banks) ** (2 * chi) >= product_h
            systems += 1
    return {"exact_colored_systems": systems}


def main() -> None:
    result = {
        "cyclic_transfer": exact_transfer_audit(),
        "ferrers_anti_alignment": ferrers_and_barrier_audit(),
        "conditional_independent_ear": independent_ear_audit(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: cyclic profile transfer and Ferrers anti-alignment verified")


if __name__ == "__main__":
    main()
