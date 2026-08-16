#!/usr/bin/env python3
"""Exact audit for LAYERED_CHAIN_LABEL_LOSS.md."""

from fractions import Fraction
from math import comb, factorial


Point = tuple[Fraction, Fraction]


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def convex_hull(points: list[Point]) -> list[Point]:
    pts = sorted(set(points))

    def half(seq):
        out: list[Point] = []
        for p in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    return half(pts)[:-1] + half(reversed(pts))[:-1]


def general_position_with(previous: list[Point], p: Point) -> bool:
    return all(
        orient(a, b, p) != 0
        for i, a in enumerate(previous)
        for b in previous[i + 1 :]
    )


def make_instance(k: int, h: int, q: int) -> tuple[list[Point], list[list[Point]]]:
    # Rational lower-parabola base with upper edge from (-1,0) to (1,0).
    base: list[Point] = []
    for i in range(k):
        x = Fraction(-1) + Fraction(2 * i, k - 1)
        base.append((x, x * x - 1))

    previous = list(base)
    clouds: list[list[Point]] = []
    total = h * q
    denominator = 1_000_003 + 100 * total

    # The tiny rational vertical perturbation is chosen greedily only to
    # avoid the finitely many old secant lines.  It stays far inside the
    # open boxes used in the proof.
    for j in range(h):
        cloud: list[Point] = []
        for a in range(q):
            serial = j * q + a + 1
            x = Fraction(2 * a - q + 1, 100 * q) + Fraction(
                j, 1000 * denominator
            )
            for attempt in range(10_000):
                dy = Fraction(
                    serial * serial
                    + attempt * serial
                    + attempt * attempt
                    + 1,
                    denominator * denominator,
                )
                p = (x, Fraction(2**j) + dy)
                if general_position_with(previous, p):
                    break
            else:
                raise AssertionError("generic rational perturbation search failed")
            previous.append(p)
            cloud.append(p)
        clouds.append(cloud)
    return base, clouds


def geometry_audit(k: int, h: int, q: int) -> None:
    base, clouds = make_instance(k, h, q)
    all_points = base + [p for cloud in clouds for p in cloud]
    assert all(
        orient(a, b, c) != 0
        for i, a in enumerate(all_points)
        for j, b in enumerate(all_points[i + 1 :], i + 1)
        for c in all_points[j + 1 :]
    )
    assert set(convex_hull(base)) == set(base)
    for cloud in clouds:
        for x in cloud:
            assert set(convex_hull(base + [x])) == set(base + [x])
    for j in range(h - 1):
        for x in clouds[j]:
            for y in clouds[j + 1]:
                assert set(convex_hull(base + [x, y])) == set(base + [y])
    print(f"geometry k={k} h={h} q={q}: PASS ({len(all_points)} points)")


def ceiling_ratio(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def counting_audit(h: int) -> None:
    k = h
    q = 1 << h
    histories = q**h
    rooted_pool_upper = (1 << k) * (1 + h * q)
    transcript = factorial(h) ** 2 * (8 * (h + 1) ** 4) ** h
    fibre_without_transcript = ceiling_ratio(histories, rooted_pool_upper**2)
    fibre_with_transcript = ceiling_ratio(
        histories, rooted_pool_upper**2 * transcript
    )
    raw_bits = fibre_without_transcript.bit_length() - 1
    tagged_bits = max(0, fibre_with_transcript.bit_length() - 1)
    assert raw_bits >= h * h - 4 * h - 2 * (h + 1).bit_length() - 2
    print(
        f"count h={h}: raw fibre >=2^{raw_bits}, "
        f"with transcript >=2^{tagged_bits}, tagged/h^2={tagged_bits/(h*h):.4f}"
    )


def universal_chain_equivalence_audit(log_n: int) -> None:
    n = 1 << log_n
    histories = comb(n, log_n)
    history_bits = histories.bit_length() - 1
    required_face_bits = history_bits / 2
    ratio = required_face_bits / (log_n * log_n)
    print(
        f"universal chain L={log_n}: log histories >= {history_bits}, "
        f"required log V/L^2 >= {ratio:.6f}"
    )
    assert ratio < 0.5


def main() -> None:
    geometry_audit(k=4, h=4, q=8)
    geometry_audit(k=5, h=5, q=16)
    for h in (32, 64, 128, 256, 512):
        counting_audit(h)
    for log_n in (16, 32, 64, 128, 256):
        universal_chain_equivalence_audit(log_n)
    print("layered insertion-chain label-loss audit: PASS")


if __name__ == "__main__":
    main()
