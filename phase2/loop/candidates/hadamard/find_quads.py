#!/usr/bin/env python3
"""Search the posted string for Williamson-type quadruples, then BUILD and VERIFY the matrices.

The claim (Alpoge, Voinov, Reynolds-Haertle + Claude, ~2026-08-11) is that this string encodes
Hadamard matrices for all twelve admissible orders below 2000 that had none:
668, 716, 892, 1132, 1244, 1388, 1436, 1676, 1772, 1916, 1948, 1964.

The string is 23828 characters over {+,-}. Note 4 * sum(n/4) = 16752 != 23828, so it is NOT a
plain concatenation of four length-n/4 sequences per order. We therefore do not guess the layout;
we search for it.

THE TEST. Four +/-1 sequences A,B,C,D of length m form a Williamson-type quadruple iff their
periodic autocorrelations satisfy
        P_A(j) + P_B(j) + P_C(j) + P_D(j) = 0   for every j = 1..m-1.
Equivalently, by Wiener-Khinchin, their power spectra satisfy
        |A^(f)|^2 + |B^(f)|^2 + |C^(f)|^2 + |D^(f)|^2 = 4m   at every frequency f.
The spectral form is what we test: one FFT per block, exact-integer check on the result.

Such a quadruple yields a Hadamard matrix of order 4m via the Goethals-Seidel array
        [ A    BR    CR    DR  ]
        [-BR   A    -D^T R  C^T R]   ... (see gs_array below for the exact form used)
so a hit at m = 167 is a Hadamard matrix of order 668.

Nothing is believed on the strength of the spectral test alone: every hit is expanded into the
full matrix and checked against H H^T = 4m I in exact integer arithmetic.

Usage: ./find_quads.py
"""
import numpy as np

ORDERS = [668, 716, 892, 1132, 1244, 1388, 1436, 1676, 1772, 1916, 1948, 1964]
TOL = 1e-6


def load(path="puzzle.txt"):
    s = open(path).read().strip()
    return np.array([1 if c == "+" else -1 for c in s], dtype=np.int64), s


def spectra_ok(blocks, m):
    """|A^|^2 + ... + |D^|^2 == 4m at every frequency?"""
    tot = np.zeros(m)
    for b in blocks:
        f = np.fft.rfft(b.astype(float))
        p = (f * f.conj()).real
        tot[: len(p)] += p
        # mirror for the negative frequencies
        if m % 2 == 0:
            tot[len(p):] += p[1:-1][::-1]
        else:
            tot[len(p):] += p[1:][::-1]
    return np.all(np.abs(tot - 4 * m) < 1e-6 * 4 * m)


def periodic_autocorr(x, m):
    return np.array([int(np.sum(x * np.roll(x, j))) for j in range(m)], dtype=np.int64)


def williamson_exact(blocks, m):
    """Exact integer confirmation of the autocorrelation condition."""
    tot = sum(periodic_autocorr(b, m) for b in blocks)
    return tot[0] == 4 * m and np.all(tot[1:] == 0)


def circ(v):
    m = len(v)
    return np.array([[v[(j - i) % m] for j in range(m)] for i in range(m)], dtype=np.int64)


def gs_array(A, B, C, D):
    """Goethals-Seidel array. R is the back-diagonal permutation.
    H = [[ A,    B R,   C R,   D R  ],
         [-B R,  A,     D^T R,-C^T R],
         [-C R, -D^T R, A,     B^T R],
         [-D R,  C^T R,-B^T R, A    ]]"""
    m = A.shape[0]
    R = np.eye(m, dtype=np.int64)[::-1].copy()
    def T(X):
        return X.T
    top = [A, B @ R, C @ R, D @ R]
    row2 = [-(B @ R), A, T(D) @ R, -(T(C) @ R)]
    row3 = [-(C @ R), -(T(D) @ R), A, T(B) @ R]
    row4 = [-(D @ R), T(C) @ R, -(T(B) @ R), A]
    return np.block([top, row2, row3, row4])


def main():
    x, s = load()
    n = len(x)
    print(f"string length {n}\n")

    hits = []
    for order in ORDERS:
        m = order // 4
        found = []
        # slide a window of 4m and split it into four consecutive blocks
        for off in range(0, n - 4 * m + 1):
            w = x[off: off + 4 * m]
            blocks = [w[i * m:(i + 1) * m] for i in range(4)]
            if spectra_ok(blocks, m):
                if williamson_exact(blocks, m):
                    found.append(off)
        print(f"order {order:5d} (m={m:4d}): {len(found)} Williamson quadruple(s)"
              + (f" at offsets {found[:5]}" if found else ""))
        if found:
            hits.append((order, m, found[0]))

    if not hits:
        print("\nNo Williamson quadruple found at any offset for any of the twelve orders.")
        print("The layout is something else; see notes.")
        return

    print("\nBuilding and verifying matrices in exact integer arithmetic:")
    for order, m, off in hits:
        w = x[off: off + 4 * m]
        A, B, C, D = (circ(w[i * m:(i + 1) * m]) for i in range(4))
        H = gs_array(A, B, C, D)
        ok_entries = np.all(np.abs(H) == 1)
        G = H @ H.T
        ok = ok_entries and np.array_equal(G, order * np.eye(order, dtype=np.int64))
        print(f"  order {order}: shape {H.shape}, entries +/-1: {ok_entries}, "
              f"H H^T == {order} I : {np.array_equal(G, order*np.eye(order,dtype=np.int64))}"
              f"  -> {'HADAMARD' if ok else 'NOT HADAMARD'}")


if __name__ == "__main__":
    main()
