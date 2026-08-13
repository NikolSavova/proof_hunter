#!/usr/bin/env python3
"""Exact coordinate audit of heterogeneous vertical blow-up identities.

The macro set is nonconvex, the two child types have unequal sizes and opposite
orientation profiles, and the four blocks receive the mixed labels A,B,B,A.
We find a rational epsilon realizing the intended mixed signs, enumerate every
subset of the resulting 14-point set from exact coordinates, and compare with
the heterogeneous substitution formulas.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations

from multitype_search import Macro, Point, classify, orient


def expected_sign(
    macro: tuple[Point, ...], children: tuple[tuple[Point, ...], ...],
    labelled: list[tuple[Point, int, int]], a: int, b: int, c: int,
) -> int:
    _, ia, ja = labelled[a]
    _, ib, jb = labelled[b]
    _, ic, jc = labelled[c]
    if ia == ic:
        return orient(children[ia][ja], children[ib][jb], children[ic][jc])
    if ia == ib:
        return -1
    if ib == ic:
        return 1
    return orient(macro[ia], macro[ib], macro[ic])


def realize(
    macro: tuple[Point, ...], children: tuple[tuple[Point, ...], ...]
) -> tuple[tuple[Point, ...], F]:
    for exponent in range(1, 20):
        eps = F(1, 10**exponent)
        labelled = [
            ((F(x) + eps * eps * F(u), F(y) + eps * F(v)), i, j)
            for i, (x, y) in enumerate(macro)
            for j, (u, v) in enumerate(children[i])
        ]
        points = tuple(item[0] for item in labelled)
        if not all(
            points[t][0] < points[t + 1][0] and points[t][1] < points[t + 1][1]
            for t in range(len(points) - 1)
        ):
            continue
        if all(
            orient(points[a], points[b], points[c])
            == expected_sign(macro, children, labelled, a, b, c)
            for a, b, c in combinations(range(len(points)), 3)
        ):
            return points, eps
    raise AssertionError("no audited epsilon found")


def totals(macro: Macro) -> tuple[int, int, int]:
    return len(macro.caps), len(macro.cups), len(macro.convex)


def predicted(
    macro: Macro, child_macros: tuple[Macro, ...]
) -> tuple[int, int, int]:
    sizes = [m.r for m in child_macros]
    cs = [len(m.caps) for m in child_macros]
    us = [len(m.cups) for m in child_macros]
    ws = [len(m.convex) for m in child_macros]
    cap = sum(cs[b[0]] * prod(sizes[i] for i in b[1:]) for b in macro.caps)
    cup = sum(us[b[-1]] * prod(sizes[i] for i in b[:-1]) for b in macro.cups)
    convex = sum(ws)
    convex += sum(
        cs[b[0]] * us[b[-1]] * prod(sizes[i] for i in b[1:-1])
        for b in macro.convex
        if len(b) >= 2
    )
    return cap, cup, convex


def prod(values) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def main() -> None:
    # The shear terms make both coordinates increase without changing signs.
    macro = ((0, 0), (1, 13), (2, 21), (3, 30))
    child_a = ((0, 0), (1, 1), (2, 4))       # cup
    child_b = ((0, 0), (1, 9), (2, 16), (3, 21))  # 4-cap
    labels = (child_a, child_b, child_b, child_a)
    points, eps = realize(macro, labels)
    macro_data = classify(macro)
    child_data = tuple(classify(q) for q in labels)
    got = totals(classify(points))
    want = predicted(macro_data, child_data)
    print(f"epsilon={eps}")
    print(f"macro convex profile={[len(b) for b in macro_data.convex]}")
    print(f"direct C,U,W={got}")
    print(f"formula C,U,W={want}")
    assert got == want
    print("PASS")


if __name__ == "__main__":
    main()
