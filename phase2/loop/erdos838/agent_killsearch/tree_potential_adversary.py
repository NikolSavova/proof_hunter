#!/usr/bin/env python3
"""Exact adversarial tests for the Erdős-838 strong-glue tree potential.

Counts are nonempty cap, cup, and convex-subset counts.  At a strong glue
T=A<B with a,b leaves the only arithmetic used is

    C = C_B + (b+1) C_A
    U = U_A + (a+1) U_B
    W = W_A + W_B + C_A U_B.

The default run constructs a 2^35-leaf prefix of the Pascal cell T(41,27),
iterates it by leaf substitution, and checks the proposed inequality

    H = W sqrt(min(C,U)/max(C,U)) >= 2^((log_2 n)^2/2).

Since n=2^(35t), its square is an exact integer comparison:

    W^2 min(C,U) >= max(C,U) * 2^(35t)^2.

No floating-point computation enters the pass/fail certificate.
"""

from __future__ import annotations

import argparse
import hashlib
import math
from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True)
class State:
    cap: int
    cup: int
    convex: int


LEAF = State(1, 1, 1)
KAPPA = 1.0 / (2.0 * math.log(2.0))


def glue(left: State, right: State, a: int, b: int) -> State:
    """Exact strong-glue recurrence."""
    return State(
        right.cap + (b + 1) * left.cap,
        left.cup + (a + 1) * right.cup,
        left.convex + right.convex + left.cap * right.cup,
    )


def log2_int(value: int) -> float:
    """Accurate-enough log for diagnostics; never used for certification."""
    bits = value.bit_length()
    kept = min(bits, 53)
    return bits - kept + math.log2(value >> (bits - kept))


def digest(value: int) -> str:
    raw = value.to_bytes((value.bit_length() + 7) // 8, "big")
    return hashlib.sha256(raw).hexdigest()[:20]


@dataclass(frozen=True)
class PrefixPascal:
    """The first `keep` leaves of the ordered Pascal cell T(m,i).

    The full cell has binom(m,i) leaves and satisfies

        T(m,i) = T(m-1,i-1) < T(m-1,i).

    Removing a suffix of leaves and suppressing unary vertices leaves another
    valid ordered full strong-decomposition tree.  The representation below
    is compressed: evaluating it takes O(m^2) recursive states, even when
    `keep` is in the billions.
    """

    m: int
    i: int
    keep: int

    def __post_init__(self) -> None:
        if not (0 <= self.i <= self.m):
            raise ValueError("need 0 <= i <= m")
        if not (1 <= self.keep <= math.comb(self.m, self.i)):
            raise ValueError("invalid retained leaf count")

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

    def degrees(self) -> tuple[int, int]:
        """Degrees of the cap and cup substitution polynomials."""
        @lru_cache(maxsize=None)
        def rec(m: int, i: int, keep: int) -> tuple[int, int]:
            if keep == 1 or i == 0 or i == m:
                return 0, 0
            left_capacity = math.comb(m - 1, i - 1)
            if keep <= left_capacity:
                return rec(m - 1, i - 1, keep)
            pc_a, pc_u = rec(m - 1, i - 1, left_capacity)
            qc_a, qc_u = rec(m - 1, i, keep - left_capacity)
            return max(qc_a, pc_a + 1), max(pc_u, qc_u + 1)

        return rec(self.m, self.i, self.keep)


def h_deficit(state: State, log_n: float) -> float:
    lc = log2_int(state.cap)
    lu = log2_int(state.cup)
    return 0.5 * log_n * log_n - log2_int(state.convex) + 0.5 * abs(lc - lu)


def quadratic_deficit(state: State, log_n: float) -> float:
    """Deficit of the exploratory quadratic-imbalance profile."""
    lc = log2_int(state.cap)
    lu = log2_int(state.cup)
    correction = KAPPA * (lc - lu) ** 2 / (lc + lu)
    return 0.5 * log_n * log_n - log2_int(state.convex) + correction


def exact_h_holds(state: State, log_n_integer: int) -> bool:
    """Certify H >= target when n is a power of two."""
    smaller = min(state.cap, state.cup)
    larger = max(state.cap, state.cup)
    lhs = state.convex * state.convex * smaller
    rhs = larger << (log_n_integer * log_n_integer)
    return lhs >= rhs


def exact_witness(iterations: int = 20) -> None:
    template = PrefixPascal(41, 27, 1 << 35)
    p, q = template.degrees()
    assert (p, q) == (27, 14)
    print(
        "template: prefix(T(41,27),2^35); "
        f"degrees=(p,q)=({p},{q}); asymptotic H-rate="
        f"{(p + 3*q)/(4*35):.12f}"
    )
    state = LEAF
    size = 1
    first_failure = None
    for t in range(1, iterations + 1):
        state, size = template.evaluate(state, size)
        assert size == 1 << (35 * t)
        holds = exact_h_holds(state, 35 * t)
        print(
            f"t={t:2d} log2(n)={35*t:4d} "
            f"bits(C,U,W)=({state.cap.bit_length()},"
            f"{state.cup.bit_length()},{state.convex.bit_length()}) "
            f"H_deficit={h_deficit(state,35*t): .9f} "
            f"quadratic_deficit={quadratic_deficit(state,35*t): .9f} "
            f"H_holds_exactly={holds}"
        )
        if not holds and first_failure is None:
            first_failure = t
            smaller = min(state.cap, state.cup)
            larger = max(state.cap, state.cup)
            lhs = state.convex * state.convex * smaller
            rhs = larger << ((35 * t) ** 2)
            print(
                "exact failure certificate: "
                f"W^2*min(C,U) < max(C,U)*2^({(35*t)**2}); "
                f"bitlengths=({lhs.bit_length()},{rhs.bit_length()}); "
                f"sha256-prefixes=({digest(lhs)},{digest(rhs)})"
            )
            break
    if first_failure is None:
        raise RuntimeError("increase --iterations; expected a failure")
    assert first_failure == 13


def binary_entropy(x: float) -> float:
    if x == 0.0 or x == 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def scan_asymptotic(grid: int = 1_000_000) -> None:
    """Optimize the homogeneous full-Pascal-cell asymptotic H rate."""
    best_rate = math.inf
    best_x = None
    for j in range(grid // 2 + 1, grid):
        x = j / grid
        rate = (3.0 - 2.0 * x) / (4.0 * binary_entropy(x))
        if rate < best_rate:
            best_rate, best_x = rate, x
    # Newton refinement of 2h(x)+(3-2x)h'(x)=0.
    x = best_x
    for _ in range(12):
        entropy = binary_entropy(x)
        derivative = math.log2((1.0 - x) / x)
        second = -1.0 / (math.log(2.0) * x * (1.0 - x))
        equation = 2.0 * entropy + (3.0 - 2.0 * x) * derivative
        equation_derivative = (3.0 - 2.0 * x) * second
        x -= equation / equation_derivative
    best_x = x
    best_rate = (3.0 - 2.0 * x) / (4.0 * binary_entropy(x))
    print(
        f"continuous Pascal optimum: x={best_x:.6f}, "
        f"H-rate={best_rate:.12f}"
    )
    finite = (math.inf, None)
    for m in range(2, 301):
        for i in range((m + 1) // 2, m):
            log_r = math.log2(math.comb(m, i))
            rate = (i + 3 * (m - i)) / (4.0 * log_r)
            finite = min(finite, (rate, (m, i, math.comb(m, i))))
    print(f"best full cell through m=300: rate={finite[0]:.12f}, data={finite[1]}")


def exhaustive(nmax: int = 13) -> None:
    """Enumerate every distinct exact (C,U,W) state through `nmax`."""
    states: list[set[tuple[int, int, int]]] = [set() for _ in range(nmax + 1)]
    states[1].add((1, 1, 1))
    for n in range(2, nmax + 1):
        current: set[tuple[int, int, int]] = set()
        for a in range(1, n):
            b = n - a
            for ca, ua, wa in states[a]:
                for cb, ub, wb in states[b]:
                    current.add(
                        (
                            cb + (b + 1) * ca,
                            ua + (a + 1) * ub,
                            wa + wb + ca * ub,
                        )
                    )
        states[n] = current
        worst_h = max(h_deficit(State(*s), math.log2(n)) for s in current)
        worst_q = max(quadratic_deficit(State(*s), math.log2(n)) for s in current)
        print(
            f"n={n:2d} states={len(current):7d} "
            f"max_H_deficit={worst_h: .9f} "
            f"max_quadratic_deficit={worst_q: .9f}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--iterations", type=int, default=20)
    parser.add_argument("--scan-asymptotic", action="store_true")
    parser.add_argument("--exhaustive", type=int, default=0, metavar="N")
    args = parser.parse_args()
    exact_witness(args.iterations)
    if args.scan_asymptotic:
        scan_asymptotic()
    if args.exhaustive:
        exhaustive(args.exhaustive)


if __name__ == "__main__":
    main()
