#!/usr/bin/env python3
"""Pareto DP for all binary strongly-decomposable point sets.

For P=A prec B, with A left/deep-below B, nonempty cap, cup, and convex
subset counts obey

    C(P) = C(B) + (1+|B|) C(A)
    U(P) = U(A) + (1+|A|) U(B)
    W(P) = W(A) + W(B) + C(A) U(B).

The program enumerates the nondominated (C,U,W) states for every size.  A
state dominates another if it is no larger in all three coordinates.  Such a
state can replace the dominated state in every later construction.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import log2
from typing import TypeAlias


@dataclass(frozen=True)
class State:
    cap: int
    cup: int
    convex: int
    tree: str

    @property
    def key(self) -> tuple[int, int, int]:
        return self.cap, self.cup, self.convex


def glue(a: State, b: State, na: int, nb: int) -> State:
    return State(
        cap=b.cap + (1 + nb) * a.cap,
        cup=a.cup + (1 + na) * b.cup,
        convex=a.convex + b.convex + a.cap * b.cup,
        tree=f"({a.tree}<{b.tree})",
    )


def mirror(s: State) -> State:
    return State(s.cup, s.cap, s.convex, f"R{s.tree}")


Node: TypeAlias = tuple


def parse_tree(text: str, pos: int = 0) -> tuple[Node, int]:
    if text[pos] == "1":
        return ("leaf",), pos + 1
    if text[pos] == "R":
        child, end = parse_tree(text, pos + 1)
        return ("mirror", child), end
    if text[pos] == "(":
        left, middle = parse_tree(text, pos + 1)
        assert text[middle] == "<"
        right, end = parse_tree(text, middle + 1)
        assert text[end] == ")"
        return ("glue", left, right), end + 1
    raise ValueError((text, pos))


def leaf_count(node: Node) -> int:
    if node[0] == "leaf":
        return 1
    if node[0] == "mirror":
        return leaf_count(node[1])
    return leaf_count(node[1]) + leaf_count(node[2])


def evaluate_template(node: Node, base: State, base_size: int) -> tuple[State, int]:
    kind = node[0]
    if kind == "leaf":
        return State(base.cap, base.cup, base.convex, "X"), base_size
    if kind == "mirror":
        state, size = evaluate_template(node[1], base, base_size)
        return State(state.cup, state.cap, state.convex, "X"), size
    a, na = evaluate_template(node[1], base, base_size)
    b, nb = evaluate_template(node[2], base, base_size)
    state = glue(a, b, na, nb)
    return State(state.cap, state.cup, state.convex, "X"), na + nb


def iterated_rate(tree: str, iterations: int) -> tuple[float, State, int]:
    node, end = parse_tree(tree)
    assert end == len(tree)
    q = leaf_count(node)
    state = State(1, 1, 1, "X")
    size = 1
    for _ in range(iterations):
        state, size = evaluate_template(node, state, size)
    rate = log2(state.convex + 1) / log2(size) ** 2
    assert size == q ** iterations
    return rate, state, size


def pareto(states: list[State]) -> list[State]:
    unique: dict[tuple[int, int, int], State] = {}
    for state in states:
        unique.setdefault(state.key, state)
    ordered = sorted(unique.values(), key=lambda s: s.key)
    out: list[State] = []
    for state in ordered:
        if any(
            old.cap <= state.cap
            and old.cup <= state.cup
            and old.convex <= state.convex
            for old in out
        ):
            continue
        out = [
            old for old in out
            if not (
                state.cap <= old.cap
                and state.cup <= old.cup
                and state.convex <= old.convex
            )
        ]
        out.append(state)
    return sorted(out, key=lambda s: s.key)


def solve(nmax: int, scan_templates: bool, iterations: int) -> list[list[State]]:
    fronts: list[list[State]] = [[] for _ in range(nmax + 1)]
    fronts[1] = [State(1, 1, 1, "1")]
    for n in range(2, nmax + 1):
        candidates: list[State] = []
        for na in range(1, n):
            nb = n - na
            for a in fronts[na]:
                for b in fronts[nb]:
                    state = glue(a, b, na, nb)
                    candidates.extend((state, mirror(state)))
        fronts[n] = pareto(candidates)
        best = min(fronts[n], key=lambda s: s.convex)
        rate = log2(best.convex + 1) / log2(n) ** 2 if n > 1 else 0.0
        print(
            f"n={n:3d} frontier={len(fronts[n]):5d} "
            f"W+empty={best.convex + 1} C={best.cap} U={best.cup} "
            f"rate={rate:.9f} tree={best.tree}",
            flush=True,
        )
        if scan_templates:
            scored = [
                (iterated_rate(state.tree, iterations)[0], state)
                for state in fronts[n]
            ]
            template_rate, template = min(scored, key=lambda item: item[0])
            print(
                f"  best_iterated_template rate@{iterations}={template_rate:.9f} "
                f"finite_W={template.convex + 1} tree={template.tree}",
                flush=True,
            )
    return fronts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nmax", type=int, default=20)
    parser.add_argument("--scan-templates", action="store_true")
    parser.add_argument("--iterations", type=int, default=30)
    args = parser.parse_args()
    solve(args.nmax, args.scan_templates, args.iterations)


if __name__ == "__main__":
    main()
