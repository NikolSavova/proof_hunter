#!/usr/bin/env python3
"""Exact checks for CODIM_THREE_ROLE_FOREST_COMPLETION_GATE.md."""

from __future__ import annotations

import itertools
import math
import sys
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))

from agent_outer_internal_product.verify_third_cyclic_merged_downface_history_load_gate import (  # noqa: E402
    add_common_ear,
    is_convex,
)
from agent_outer_internal_product.verify_two_sided_merged_downface_maximum_child_gate import (  # noqa: E402
    role_gadget,
)


def puncture(word, role):
    return role, word[:role] + word[role + 1 :]


def abstract_cube(q: int, d: int):
    words = tuple(itertools.product(range(d), repeat=q))
    loads = Counter()
    for triple in itertools.product(words, repeat=3):
        for roles in itertools.product(range(q), repeat=3):
            output = tuple(puncture(triple[a], roles[a]) for a in range(3))
            loads[output] += 1

    mass = d ** (3 * q)
    incidences = mass * q**3
    outputs = mass * q**3 // d**3
    assert sum(loads.values()) == incidences
    assert len(loads) == outputs
    assert set(loads.values()) == {d**3}

    # Restoring side zero has exact decoder load q: the restored word and
    # the two still-empty roles are visible, and only its restored role is
    # forgotten.
    restored = Counter()
    for output in loads:
        (i, left_puncture), middle, right = output
        for x in range(d):
            full = left_puncture[:i] + (x,) + left_puncture[i:]
            restored[(full, middle, right)] += 1
    assert set(restored.values()) == {q}
    return mass, incidences, outputs, d**3, len(restored), q


def exact_planar_cube(q: int = 2, d: int = 3):
    (points, left_roles, right_roles, left_marks, right_marks,
     left_index, right_index, seam) = role_gadget(q, d)
    points, third_roles, third_index = add_common_ear(
        points, seam, left_marks, right_marks, left_index, right_index,
        role_count=q, alphabet=d,
    )

    loads = Counter()
    for left in itertools.product(*left_roles):
        for right in itertools.product(*right_roles):
            for third in itertools.product(*third_roles):
                for i, j, k in itertools.product(range(q), repeat=3):
                    output = frozenset(
                        seam
                        | {left_index[left[t]] for t in range(q) if t != i}
                        | {right_index[right[t]] for t in range(q) if t != j}
                        | {third_index[third[t]] for t in range(q) if t != k}
                    )
                    assert is_convex([points[p] for p in output])
                    loads[output] += 1

    mass = d ** (3 * q)
    assert sum(loads.values()) == mass * q**3
    assert len(loads) == mass * q**3 // d**3
    assert set(loads.values()) == {d**3}
    return len(points), sum(loads.values()), len(loads), d**3


def prefix_branching_versus_punctures(q: int = 4, d: int = 3):
    cube = tuple(itertools.product(range(d), repeat=q))
    masses = [d ** (q - depth) for depth in range(q + 1)]
    ratios = [masses[depth] // masses[depth + 1] for depth in range(q)]
    assert ratios == [d] * q
    assert math.prod(ratios) == d**q
    assert d**q // math.prod(ratios) == 1  # Q_eff=1.

    cube_degrees = Counter()
    for word in cube:
        for role in range(q):
            cube_degrees[puncture(word, role)] += 1
    assert set(cube_degrees.values()) == {d}

    # A parity/MDS code has essentially the same early uniform prefix
    # branching but every puncture determines its missing coordinate.
    parity = tuple(
        prefix + (sum(prefix) % d,)
        for prefix in itertools.product(range(d), repeat=q - 1)
    )
    parity_degrees = Counter()
    for word in parity:
        for role in range(q):
            parity_degrees[puncture(word, role)] += 1
    assert set(parity_degrees.values()) == {1}
    for depth in range(q - 1):
        prefixes = Counter(word[:depth] for word in parity)
        next_prefixes = Counter(word[: depth + 1] for word in parity)
        assert set(prefixes.values()) == {d ** (q - 1 - depth)}
        assert set(next_prefixes.values()) == {d ** (q - 2 - depth)}
    return len(cube), len(parity), d, 1


def good_load_trichotomy():
    # Exhaust a family of deterministic "geometry" predicates.  Every
    # good incidence is counted once in an actual output load.
    q, d = 2, 2
    words = tuple(itertools.product(range(d), repeat=q))
    records = tuple(itertools.product(words, repeat=3))
    total = len(records) * q**3
    checked = 0
    for modulus in (2, 3, 5, 7):
        loads = Counter()
        good = 0
        for record_id, triple in enumerate(records):
            for roles in itertools.product(range(q), repeat=3):
                signature = record_id + sum((a + 2) * roles[a]
                                            for a in range(3))
                if signature % modulus:
                    output = tuple(puncture(triple[a], roles[a])
                                   for a in range(3))
                    loads[output] += 1
                    good += 1
        assert good + (total - good) == total
        for threshold in range(1, 10):
            low = sum(load for load in loads.values()
                      if load <= threshold)
            high = sum(load for load in loads.values()
                       if load > threshold)
            assert good == low + high
            assert low <= threshold * len(loads)
            if low < good / 2:
                assert high > good / 2
            checked += 1
    return checked


def live_scale_ledger():
    rows = []
    for ell in (36, 48, 60, 72, 96):
        q = ell // 6
        n = 1 << ell
        d = n // (3 * q)
        mass = d ** (3 * q)
        bank = mass * q**3 // d**3
        assert 3 * q * d <= n
        assert bank * d**3 == mass * q**3
        gain_log = math.log2(bank / mass)
        assert abs(gain_log - 3 * (math.log2(q) - math.log2(d))) < 1e-12
        assert gain_log < -2 * ell
        rows.append((ell, q, d, gain_log))
    return rows


def main():
    abstract = [abstract_cube(2, 2), abstract_cube(2, 3), abstract_cube(3, 2)]
    planar = exact_planar_cube()
    mismatch = prefix_branching_versus_punctures()
    trichotomy = good_load_trichotomy()
    ledger = live_scale_ledger()
    print(
        "PASS: codim-three/role-forest completion gate; "
        f"abstract={abstract}; planar={planar}; mismatch={mismatch}; "
        f"trichotomy={trichotomy}; ledger={len(ledger)}"
    )


if __name__ == "__main__":
    main()
