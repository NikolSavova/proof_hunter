#!/usr/bin/env python3
"""Exact small checks for the bipartite blow-up certificate.

For a finite interval basis A, a state unused/V/H/B on every element is valid
when each covered sum has a representation with one endpoint carrying V and
the other H.  B carries both roles.  The script enumerates all extremal bases
through k=7 and minimizes the total role cost |V|+|H|.
"""

from __future__ import annotations

from itertools import combinations, product
import json
from pathlib import Path


V, H, BOTH = 1, 2, 3


def representation_lists(a: tuple[int, ...], n: int) -> list[list[tuple[int, int]]]:
    reps: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for i, x in enumerate(a):
        for j in range(i, len(a)):
            s = x + a[j]
            if s <= n:
                reps[s].append((i, j))
    return reps


def is_basis(a: tuple[int, ...], n: int) -> bool:
    return all(representation_lists(a, n))


def valid_states(reps: list[list[tuple[int, int]]], states: tuple[int, ...]) -> bool:
    return all(
        any((states[i] & V and states[j] & H) or
            (states[i] & H and states[j] & V) for i, j in pairs)
        for pairs in reps
    )


def minimum_duplication(a: tuple[int, ...], n: int) -> tuple[int, tuple[int, ...]]:
    reps = representation_lists(a, n)
    k = len(a)
    # Sum zero forces the element 0 to carry both roles, so start at d=1.
    for d in range(1, k + 1):
        for duplicate in combinations(range(k), d):
            duplicate_set = set(duplicate)
            if 0 not in duplicate_set:
                continue
            plain = [i for i in range(k) if i not in duplicate_set]
            for colors in product((V, H), repeat=len(plain)):
                states = [BOTH if i in duplicate_set else 0 for i in range(k)]
                for i, color in zip(plain, colors):
                    states[i] = color
                state_tuple = tuple(states)
                if valid_states(reps, state_tuple):
                    return d, state_tuple
    raise AssertionError("all-BOTH is always valid")


def role_cost(states: tuple[int, ...]) -> int:
    return sum(bool(state & V) + bool(state & H) for state in states)


def minimum_cross_cover(a: tuple[int, ...], n: int) -> tuple[int, tuple[int, ...]]:
    """Minimize |V|+|H|; state zero permits an unused element of A."""
    reps = representation_lists(a, n)
    best = None
    for states in product((0, V, H, BOTH), repeat=len(a)):
        cost = role_cost(states)
        if best is not None and cost >= best[0]:
            continue
        if valid_states(reps, states):
            best = (cost, states)
    if best is None:
        raise AssertionError("all-BOTH is always valid")
    return best


def bases_of_size_for_range(k: int, n: int):
    if k == 1:
        if n == 0:
            yield (0,)
        return
    # Covering 0 and 1 forces 0,1 in every basis with n>=1.
    if n == 0:
        return
    for tail in combinations(range(2, n + 1), k - 2):
        a = (0, 1) + tail
        if is_basis(a, n):
            yield a


def extremal_bases(k: int) -> tuple[int, list[tuple[int, ...]]]:
    if k == 1:
        return 0, [(0,)]
    pair_bound = k * (k + 1) // 2 - 1
    for n in range(pair_bound, 0, -1):
        found = list(bases_of_size_for_range(k, n))
        if found:
            return n, found
    raise AssertionError(k)


def direct_blowup(a: tuple[int, ...], n: int, states: tuple[int, ...], q: int) -> tuple[int, ...]:
    vertical = tuple(range(q))
    horizontal = tuple(q * j for j in range(q))
    out: set[int] = set()
    for x, state in zip(a, states):
        offset = x * q * q
        if state & V:
            out.update(offset + z for z in vertical)
        if state & H:
            out.update(offset + z for z in horizontal)
    return tuple(sorted(out))


def covers(a: tuple[int, ...], n: int) -> bool:
    sums = {x + y for x in a for y in a}
    return all(s in sums for s in range(n + 1))


def main() -> None:
    rows = []
    explicit_checks = 0
    for k in range(1, 8):
        n, bases = extremal_bases(k)
        audited = []
        for a in bases:
            cost, states = minimum_cross_cover(a, n)
            audited.append((cost, a, states))
        best = min(audited)
        worst_cost = max(row[0] for row in audited)

        # Directly check the best certificate for several blow-up scales.
        cost, a, states = best
        for q in range(1, 8):
            blown = direct_blowup(a, n, states, q)
            assert covers(blown, (n + 1) * q * q - 1)
            assert len(blown) <= cost * q
            explicit_checks += 1

        rows.append({
            "k": k,
            "R_k": n,
            "number_of_extremal_bases": len(bases),
            "minimum_cross_cover_cost_over_extremizers": cost,
            "maximum_minimum_cross_cover_cost_over_extremizers": worst_cost,
            "effective_duplication_cost_minus_k": cost - k,
            "best_basis": a,
            "best_states_0unused_1V_2H_3B": states,
            "certified_asymptotic_ratio": (n + 1) / cost ** 2,
        })

    elementary_rows = []
    for t in range(1, 9):
        a = tuple(range(t)) + tuple(j * t for j in range(1, t + 1))
        n = t * t + t - 1
        # Explicit certificate: the shared zero has both roles, the remaining
        # short interval is vertical, and the positive multiples are horizontal.
        states = (BOTH,) + (V,) * (t - 1) + (H,) * t
        cost = role_cost(states)
        assert valid_states(representation_lists(a, n), states)
        elementary_rows.append({
            "t": t,
            "size": len(a),
            "range": n,
            "explicit_cross_cover_cost": cost,
            "cost_minus_basis_size": cost - len(a),
            "states_0unused_1V_2H_3B": states,
        })

    output = {
        "status": "PASS",
        "scope": "all extremal bases for 1<=k<=7; direct blow-ups q<=7",
        "direct_blowups_checked": explicit_checks,
        "rows": rows,
        "elementary_family_rows": elementary_rows,
    }
    target = Path(__file__).with_name("BIPARTITE_BLOWUP_CHECK.json")
    target.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
