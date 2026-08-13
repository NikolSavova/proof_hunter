#!/usr/bin/env python3
"""Broad scan: find EVERY Williamson quadruple in the string, at any length and offset.

find_quads.py tested only the twelve target orders with four consecutive blocks and found five
(892, 1132, 1244, 1948, 1964). Seven orders are unaccounted for, so the layout for those is
different. Rather than guess it, scan all block lengths.

Fast rejection. For four consecutive blocks of length m at offset b, the Williamson condition
requires in particular the j=1 term
        sum over the four blocks of P_X(1) = 0,
where P_X(1) = sum_k X[k] X[(k+1) mod m]. With q[i] = x[i]*x[i+1] and a prefix sum of q, each
block's P_X(1) is one subtraction plus a wraparound term, so the whole offset axis is vectorised
in O(n) per m. Only survivors get the full spectral test, and only those get the exact
integer autocorrelation check.

Usage: ./scan_all.py [mmin] [mmax]
"""
import sys

import numpy as np


def load(path="puzzle.txt"):
    s = open(path).read().strip()
    return np.array([1 if c == "+" else -1 for c in s], dtype=np.int64)


def p1_all(x, m):
    """P_X(1) for every block of length m starting at each offset, vectorised."""
    n = len(x)
    q = x[:-1] * x[1:]                     # adjacent products
    cs = np.concatenate(([0], np.cumsum(q)))
    b = np.arange(0, n - m + 1)
    inner = cs[b + m - 1] - cs[b]          # sum of q over [b, b+m-1)
    wrap = x[b + m - 1] * x[b]
    return inner + wrap


def spectra_ok(blocks, m):
    tot = np.zeros(m)
    for bl in blocks:
        f = np.fft.rfft(bl.astype(float))
        p = (f * f.conj()).real
        tot[: len(p)] += p
        tot[len(p):] += (p[1:-1][::-1] if m % 2 == 0 else p[1:][::-1])
    return np.all(np.abs(tot - 4 * m) < 1e-6 * 4 * m)


def exact_ok(blocks, m):
    tot = np.zeros(m, dtype=np.int64)
    for bl in blocks:
        tot += np.array([int(np.sum(bl * np.roll(bl, j))) for j in range(m)], dtype=np.int64)
    return tot[0] == 4 * m and np.all(tot[1:] == 0)


def main():
    mmin = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    mmax = int(sys.argv[2]) if len(sys.argv) > 2 else 700
    x = load()
    n = len(x)
    print(f"string length {n}; scanning block lengths m = {mmin}..{mmax}\n")
    all_hits = []
    for m in range(mmin, mmax + 1):
        if 4 * m > n:
            break
        p1 = p1_all(x, m)
        limit = n - 4 * m
        b = np.arange(0, limit + 1)
        tot1 = p1[b] + p1[b + m] + p1[b + 2 * m] + p1[b + 3 * m]
        cand = b[tot1 == 0]
        for off in cand:
            blocks = [x[off + i * m: off + (i + 1) * m] for i in range(4)]
            if spectra_ok(blocks, m) and exact_ok(blocks, m):
                all_hits.append((m, int(off)))
                print(f"  m={m:4d} -> order {4*m:5d} at offset {off}")
    print(f"\n{len(all_hits)} quadruple(s) total")
    covered = sorted({4 * m for m, _ in all_hits})
    print("orders realised:", covered)
    targets = [668, 716, 892, 1132, 1244, 1388, 1436, 1676, 1772, 1916, 1948, 1964]
    print("targets hit    :", [t for t in targets if t in covered])
    print("targets MISSING:", [t for t in targets if t not in covered])
    used = sum(4 * m for m, _ in all_hits)
    print(f"characters consumed by quadruples: {used} of {n} ({n-used} unexplained)")


if __name__ == "__main__":
    main()
