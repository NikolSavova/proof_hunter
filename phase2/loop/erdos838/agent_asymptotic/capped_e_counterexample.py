#!/usr/bin/env python3
"""Exact valid counterexample family for the capped-E local Bellman lemma.

Integer recurrences generate every state.  Floating point is used only for
logs of positive integers and the final diagnostic gap.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True)
class State:
    cap: int
    cup: int
    convex: int
    endpoint: int


LEAF = State(1, 1, 1, 1)


def glue(left: State, right: State, a: int, b: int) -> State:
    return State(
        right.cap + (b + 1) * left.cap,
        left.cup + (a + 1) * right.cup,
        left.convex + right.convex + left.cap * right.cup,
        (b + 1) * left.endpoint + (a + 1) * right.endpoint - a * b,
    )


def mirror(state: State) -> State:
    return State(state.cup, state.cap, state.convex, state.endpoint)


def log2_int(value: int) -> float:
    bits = value.bit_length()
    kept = min(bits, 53)
    return bits - kept + math.log2(value >> (bits - kept))


def logsumexp2(values: list[float]) -> float:
    maximum = max(values)
    return maximum + math.log2(sum(2.0 ** (x - maximum) for x in values))


@dataclass(frozen=True)
class PrefixPascal:
    m: int
    i: int
    keep: int

    def evaluate(self, base: State, base_size: int) -> tuple[State, int]:
        @lru_cache(maxsize=None)
        def rec(m: int, i: int, keep: int) -> tuple[State, int]:
            if keep == 1 or i == 0 or i == m:
                return base, base_size
            left_capacity = math.comb(m - 1, i - 1)
            if keep <= left_capacity:
                return rec(m - 1, i - 1, keep)
            left, a = rec(m - 1, i - 1, left_capacity)
            right, b = rec(m - 1, i, keep - left_capacity)
            return glue(left, right, a, b), a + b

        return rec(self.m, self.i, self.keep)


def reserve(log_n: float, constant: float) -> float:
    return constant * log_n * math.log2(max(2.0, log_n))


def capped_value(size: int, endpoint: int, constant: float) -> float:
    log_n = math.log2(size)
    return (
        min(log2_int(endpoint), 0.5 * log_n * log_n)
        - reserve(log_n, constant)
    )


def main() -> None:
    template = PrefixPascal(41, 27, 1 << 35)
    state = LEAF
    size = 1
    for iteration in range(1, 16):
        state, size = template.evaluate(state, size)
        parent = glue(mirror(state), state, size, size)
        for constant in (4.0, 10.0):
            child_value = capped_value(size, state.endpoint, constant)
            parent_value = capped_value(2 * size, parent.endpoint, constant)
            lhs = logsumexp2(
                [child_value, child_value, 2.0 * log2_int(state.cup)]
            )
            gap = lhs - parent_value
            if iteration in {1, 5, 10, 11, 12, 15}:
                print(
                    f"K={constant:4.1f} t={iteration:2d} "
                    f"child_log_n={math.log2(size):5.0f} "
                    f"logE/L^2={log2_int(state.endpoint)/math.log2(size)**2:.9f} "
                    f"logU/L^2={log2_int(state.cup)/math.log2(size)**2:.9f} "
                    f"Bellman_gap={gap: .9f}"
                )


if __name__ == "__main__":
    main()
