#!/usr/bin/env python3
"""Exact set-system audit for COMMON_CORE_COMPLETION_PRIVATE_PETAL_TRICHOTOMY."""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb


def private_bank(carrier, tag):
    carrier = tuple(carrier)
    return {
        frozenset(subset)
        for rank in range(1, len(carrier) + 1)
        for subset in combinations(carrier, rank)
        if tag in subset
    }


def four_covered(carriers):
    support = set().union(*map(set, carriers))
    for four in combinations(support, 4):
        if not any(set(four) <= set(carrier) for carrier in carriers):
            return False, frozenset(four)
    return True, None


def main():
    # Private petals over one common two-label core.
    core = (0, 1)
    carriers = []
    tags = []
    for index in range(4):
        petal = tuple(range(2 + 3 * index, 5 + 3 * index))
        carriers.append(frozenset(core + petal))
        tags.append(petal[0])
    q, r = 5, 2
    banks = [private_bank(carrier, tag) for carrier, tag in zip(carriers, tags)]
    assert all(len(bank) == 2 ** (q - 1) for bank in banks)
    loads = Counter(face for bank in banks for face in bank)
    assert max(loads.values()) == 1
    mass = len(carriers) * comb(q, r)
    assert len(loads) == len(carriers) * 2 ** (q - 1)
    assert Fraction(len(loads), mass) == Fraction(2 ** (q - 1), comb(q, r))

    # Five distinct missing labels four-cover a six-label completion support.
    core = (100, 101)
    completion_support = tuple(range(6))
    deletion_carriers = [
        frozenset(core + tuple(x for x in completion_support if x != missing))
        for missing in range(5)
    ]
    covered, witness = four_covered(deletion_carriers)
    assert covered and witness is None
    union = set().union(*map(set, deletion_carriers))
    assert len(union) == 8
    assert all(
        any(set(trace) <= set(carrier) for carrier in deletion_carriers)
        for size in range(5)
        for trace in combinations(union, size)
    )

    # Two separated petals have an uncovered mixed four-set. Every carrier
    # omits at least one witness label, and canonical first omission partitions
    # arbitrary rational carrier mass without loss.
    split_carriers = [
        frozenset((200, 201, 0, 1, 2)),
        frozenset((200, 201, 3, 4, 5)),
    ]
    covered, witness = four_covered(split_carriers)
    assert not covered and len(witness) == 4
    weights = [Fraction(2, 5), Fraction(3, 5)]
    ordered_witness = sorted(witness)
    children = Counter()
    for carrier, weight in zip(split_carriers, weights):
        omitted = next(label for label in ordered_witness if label not in carrier)
        children[omitted] += weight
    assert sum(children.values(), Fraction()) == 1
    assert max(children.values()) >= Fraction(1, 4)
    assert all(
        label not in set().union(
            *(set(carrier) for carrier, weight in zip(split_carriers, weights)
              if next(x for x in ordered_witness if x not in carrier) == label)
        )
        for label in children
    )

    print(
        "PASS: private banks=%d load=1; four-cover union=8; "
        "deletion children=%d" % (len(banks), len(children))
    )


if __name__ == "__main__":
    main()
