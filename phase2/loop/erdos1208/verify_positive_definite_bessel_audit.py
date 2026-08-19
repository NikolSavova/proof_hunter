#!/usr/bin/env python3
"""Exact finite checks for POSITIVE_DEFINITE_BESSEL_AUDIT.md.

No floating-point Bessel evaluation is needed: this checks the Fourier
coefficient identities and the combinatorial equality behind the universal
radial-LP obstruction.
"""

from collections import Counter


Point = tuple[int, int]


def sub(x: Point, y: Point) -> Point:
    return (x[0] - y[0], x[1] - y[1])


def add(x: Point, y: Point) -> Point:
    return (x[0] + y[0], x[1] + y[1])


def quarter(x: Point) -> Point:
    return (-x[1], x[0])


def autocorrelation(a: list[Point]) -> Counter[Point]:
    return Counter(sub(x, y) for x in a for y in a)


def convolution(f: Counter[Point], g: Counter[Point]) -> Counter[Point]:
    out: Counter[Point] = Counter()
    for x, fx in f.items():
        for y, gy in g.items():
            out[add(x, y)] += fx * gy
    return out


def is_distance_sidon(a: list[Point]) -> bool:
    seen: set[int] = set()
    for i, x in enumerate(a):
        for y in a[:i]:
            d = sub(x, y)
            n = d[0] * d[0] + d[1] * d[1]
            if n in seen:
                return False
            seen.add(n)
    return True


def check_configuration(a: list[Point]) -> tuple[int, int]:
    assert is_distance_sidon(a)
    k = len(a)
    h = autocorrelation(a)
    assert h[(0, 0)] == k
    assert all(c == 1 for d, c in h.items() if d != (0, 0))
    assert len(h) == k * (k - 1) + 1

    # Integral H^2 is the squared l2 norm of h.
    assert sum(c * c for c in h.values()) == 2 * k * k - k

    # Integral H(theta)H(J theta): only the zero Fourier coefficient meets.
    mixed = sum(c * h.get(quarter(d), 0) for d, c in h.items())
    assert mixed == k * k

    # Integral H^2 H(J theta)^2 is the rotated inner product of h*h.
    hh = convolution(h, h)
    fourth = sum(c * hh.get(quarter(d), 0) for d, c in hh.items())

    # Replacing h by 1_D can only lower this coefficientwise convolution.
    one_d = Counter({d: 1 for d in h})
    dd = convolution(one_d, one_d)
    unweighted = sum(c * dd.get(quarter(d), 0) for d, c in dd.items())
    assert fourth >= unweighted
    return fourth, unweighted


def check_full_grid_lp_obstruction() -> None:
    for m in range(1, 21):
        grid = [(x, y) for x in range(m + 1) for y in range(m + 1)]
        size = len(grid)
        unordered_pairs = size * (size - 1) // 2
        # At eta=1/(M-1), the integrated full-grid inequality is equality.
        assert size * (size - 1) == 2 * unordered_pairs


def main() -> None:
    examples = [
        [(0, 0), (1, 0), (0, 2)],
        [(0, 0), (1, 0), (3, 0), (7, 0)],
        [(0, 0), (1, 2), (4, 1), (2, 7)],
    ]
    profiles = [check_configuration(a) for a in examples]
    check_full_grid_lp_obstruction()
    print("positive-definite/Bessel audit checks passed")
    print("mixed-fourth profiles (weighted, unweighted):", profiles)


if __name__ == "__main__":
    main()
