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


def solve(nmax: int) -> list[list[State]]:
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
    return fronts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nmax", type=int, default=20)
    args = parser.parse_args()
    solve(args.nmax)


if __name__ == "__main__":
    main()
