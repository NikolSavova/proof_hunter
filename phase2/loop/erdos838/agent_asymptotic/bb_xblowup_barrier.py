#!/usr/bin/env python3
"""Exact lower certificates for the Baek--Balko new x-blow-up.

This does not enumerate every convex subset.  It exactly counts two disjointly
described subfamilies sufficient to rule out a sub-1/2 coefficient for the
canonical Pascal-cell instantiation:

* one-point-per-layer transversals in one Pascal-row half of M;
* all convex subsets inside a score-2 Pascal cluster.

All combinatorial counts use Python integers.  Floating point is used only
for logarithms and the displayed limiting entropy integrals.
"""

from __future__ import annotations

import argparse
import math


def log2_int(value: int) -> float:
    if value <= 0:
        raise ValueError("expected a positive integer")
    bits = value.bit_length()
    shift = max(0, bits - 53)
    return math.log2(value >> shift) + shift


def entropy(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def entropy_integral(a: float, b: float, steps: int = 20_000) -> float:
    """Composite Simpson integral of binary entropy on [a,b]."""
    if not 0.0 <= a <= b <= 1.0:
        raise ValueError("invalid entropy integration interval")
    if a == b:
        return 0.0
    if steps % 2:
        steps += 1
    width = (b - a) / steps
    total = entropy(a) + entropy(b)
    for i in range(1, steps):
        total += (4 if i % 2 else 2) * entropy(a + i * width)
    return total * width / 3.0


def transversal_count(k: int, x: int) -> int:
    """Exact product of weighted one-per-layer choices in the left half.

    Put d=m-3=k-2x-3.  In layer h>=1, points with score t+1 are
    indexed by h-subsets of [t] having maximum t, hence occur
    binom(t-1,h-1) times.  A score-(t+1) point receives a cluster of
    size binom(k-t-2,x).
    """
    d = k - 2 * x - 3
    if x < 1 or d < 0:
        raise ValueError("Theorem 19 requires x>=1 and k>=2x+3")

    # The empty-subset layer is the leftmost point of M and hence receives
    # the special P(k,x+2,k) cluster.
    first_mass = sum(math.comb(k - 2, ell) for ell in range(x + 1))
    masses = [first_mass]
    product = first_mass
    for h in range(1, d + 1):
        layer_mass = sum(
            math.comb(t - 1, h - 1) * math.comb(k - t - 2, x)
            for t in range(h, d + 1)
        )
        masses.append(layer_mass)
        product *= layer_mass
    # One half of the Baek--Balko blow-up has exactly half of 2^(k-2)
    # points.  This identity is a useful independent check on the refined
    # score-by-layer distribution used above.
    assert sum(masses) == 2 ** (k - 3)
    return product


def pascal_cell_convex(depth: int, index: int) -> int:
    """Exact W[depth,index] for the standard strong Pascal cell."""
    if not 0 <= index <= depth:
        raise ValueError("invalid Pascal-cell index")
    sizes = [1]
    caps = [1]
    cups = [1]
    convex = [1]
    for d in range(1, depth + 1):
        new_sizes = [1] * (d + 1)
        new_caps = [1] * (d + 1)
        new_cups = [1] * (d + 1)
        new_convex = [1] * (d + 1)
        for i in range(1, d):
            # T[d,i] = T[d-1,i-1] prec T[d-1,i].
            left_size, right_size = sizes[i - 1], sizes[i]
            new_sizes[i] = left_size + right_size
            new_caps[i] = caps[i - 1] * (1 + right_size) + caps[i]
            new_cups[i] = cups[i - 1] + (1 + left_size) * cups[i]
            new_convex[i] = (
                convex[i - 1] + convex[i] + caps[i - 1] * cups[i]
            )
        sizes, caps, cups, convex = (
            new_sizes,
            new_caps,
            new_cups,
            new_convex,
        )
    return convex[index]


def internal_score_two_count(k: int, x: int) -> int:
    """Convex count in a canonical score-2 cluster.

    Such a left cluster is a rotated P(k-x-1,x+2), hence is the Pascal
    cell of depth k-3 and index x, up to reflection.
    """
    return pascal_cell_convex(k - 3, x)


def transversal_limit(theta: float) -> float:
    mu = 1.0 - 2.0 * theta
    return (
        entropy_integral(theta, 0.5)
        + mu * mu / (4.0 * math.log(2.0))
        + theta * mu
    )


def internal_limit(theta: float) -> float:
    return entropy(theta) - theta * (1.0 - theta) / math.log(2.0)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int, default=120)
    parser.add_argument(
        "--fractions",
        default="0.10,0.15,0.20,0.21,0.22,0.25,0.30,0.40",
        help="comma-separated target x/k ratios",
    )
    args = parser.parse_args()

    print(" k   x    x/k     transversal/k^2  cell/k^2   limiting T   limiting I")
    for raw in args.fractions.split(","):
        theta_target = float(raw)
        x = max(1, round(theta_target * args.k))
        if args.k < 2 * x + 3:
            continue
        theta = x / args.k
        trans = transversal_count(args.k, x)
        cell = internal_score_two_count(args.k, x)
        print(
            f"{args.k:3d} {x:3d} {theta:8.5f}"
            f" {log2_int(trans)/(args.k*args.k):17.9f}"
            f" {log2_int(cell)/(args.k*args.k):11.9f}"
            f" {transversal_limit(theta):12.9f}"
            f" {internal_limit(theta):12.9f}"
        )

    pivot = 0.21
    print()
    print(f"pivot theta={pivot:.2f}")
    print(f"T(theta)={transversal_limit(pivot):.12f}")
    print(f"I(theta)={internal_limit(pivot):.12f}")
    print(
        "certified asymptotic cover = "
        f"{min(transversal_limit(pivot), internal_limit(pivot)):.12f}"
    )


if __name__ == "__main__":
    main()
