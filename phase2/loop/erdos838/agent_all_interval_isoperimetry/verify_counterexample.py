#!/usr/bin/env python3
"""Exact audit for the ramp--plateau--ramp atomic KIC counterexample."""

from math import comb


def instance(h: int):
    L = 1 << h
    k = L // 2
    ramp = [1 << q for q in range(h)]
    a = ramp + [L] * k + list(reversed(ramp))
    m = [1 << x for x in a]
    b = len(a)
    M = 1
    D = 1
    n0 = 0
    for x in m:
        M *= x
        D *= x + 1
        n0 += x

    prefix = [0]
    optional_prefix = [1]
    for x in a:
        prefix.append(prefix[-1] + x)
    for x in m:
        optional_prefix.append(optional_prefix[-1] * (x + 1))
    S = prefix[-1]

    T = 0
    atomic_full = 1
    endpoint = [x + comb(x, 2) for x in m]
    atomic_full += sum(endpoint)
    max_ratio_numer = 0
    max_potential = -10**100
    for i in range(b):
        for j in range(i + 1, b):
            middle = optional_prefix[j] // optional_prefix[i + 1]
            Tij = comb(m[i], 2) * comb(m[j], 2) * middle
            T += Tij
            atomic_full += endpoint[i] * endpoint[j] * middle
            max_ratio_numer = max(max_ratio_numer, Tij)
            potential = a[i] - prefix[i] + a[j] - (S - prefix[j + 1])
            max_potential = max(max_potential, potential)
            assert potential <= 2
            assert Tij < 21 * M

    ell = (n0 - 1).bit_length()
    d = 1 << (ell - b)
    return {
        "h": h,
        "L": L,
        "b": b,
        "S": S,
        "M": M,
        "D": D,
        "T": T,
        "n0": n0,
        "ell": ell,
        "d": d,
        "max_potential": max_potential,
        "atomic_ratio_lt_poly": D + T < 21 * (1 + comb(b, 2)) * M,
        "root_factor_bound": b * S >= 0 and S * 3 >= 2 * L * b,
        "cap_lower_bound": d * (2 * L) >= (1 << (L // 2)),
        "cap_beats_atomic": d * M > D + T,
        "cap_beats_full_atomic": d * M > atomic_full,
    }


def enriched_profile(h: int):
    """Audit the scalar cap/cup-gradient obstruction in (20)--(25)."""
    L = 1 << h
    k = L // 2
    ramp = [1 << q for q in range(h)]
    a = ramp + [L] * k + list(reversed(ramp))
    m = [1 << x for x in a]
    b = len(a)
    plateau_start = h
    plateau_stop = h + k

    C = []
    U = []
    V = []
    for idx, mi in enumerate(m):
        if plateau_start <= idx < plateau_stop:
            p = idx - plateau_start + 1
            ci = 1 << ((p + 1) * L)
            ui = 1 << ((k - p + 2) * L)
            vi = ci + ui
            # The same-block product exponent is exactly (k+3)L.
            assert (ci * ui).bit_length() - 1 == (k + 3) * L
        else:
            # All one- and two-letter endpoint faces; the two orientations
            # overlap, so their union needs only this many ordinary faces.
            di = mi + comb(mi, 2)
            ci = ui = vi = di
        assert ci <= vi and ui <= vi
        # Every displayed count lies below the Boolean 2^mi ceiling.  Avoid
        # constructing that astronomically large integer.
        assert ci.bit_length() - 1 <= mi
        assert ui.bit_length() - 1 <= mi
        assert vi.bit_length() - 1 <= mi
        C.append(ci)
        U.append(ui)
        V.append(vi)

    M = 1
    n0 = 0
    optional_prefix = [1]
    for mi in m:
        M *= mi
        n0 += mi
        optional_prefix.append(optional_prefix[-1] * (mi + 1))

    E = sum(V)
    for i in range(b):
        for j in range(i + 1, b):
            middle = optional_prefix[j] // optional_prefix[i + 1]
            term = C[i] * U[j] * middle
            assert term < 21 * M
            E += term

    ell = (n0 - 1).bit_length()
    d = 1 << (ell - b)
    K = (k + 1) * L
    a_floor = L
    W = k * L
    R = L - 1
    reset_rhs = K - L * (k - 1) - 2 * R - (
        W - a_floor - L * (k - 1)
    ) // (k - 1)
    assert reset_rhs == 2
    assert E < d * M
    return {
        "h": h,
        "L": L,
        "b": b,
        "ell": ell,
        "same_block_product_exp": (k + 3) * L,
        "reset_rhs": reset_rhs,
        "enriched_cap_beats": d * M > E,
    }


def main():
    rows = []
    # h=6 already has very large exact integers but is inexpensive.  Going
    # through h=8 checks plateau lengths up to 128 and 10,000 intervals.
    for h in range(6, 9):
        row = instance(h)
        assert row["max_potential"] == 2
        assert row["atomic_ratio_lt_poly"]
        assert row["root_factor_bound"]
        assert row["cap_lower_bound"]
        assert row["cap_beats_atomic"]
        assert row["cap_beats_full_atomic"]
        rows.append(row)

    for row in rows:
        print(
            "h={h} L={L} b={b} ell={ell} S={S} "
            "max_interval_potential={max_potential} PASS".format(**row)
        )
    # The enriched exact sums are more expensive; h=6,7 already test up to
    # 3,000 interval products with several-thousand-bit integers.
    for h in range(6, 8):
        row = enriched_profile(h)
        assert row["enriched_cap_beats"]
        print(
            "enriched h={h} L={L} b={b} ell={ell} "
            "log2(C_i U_i)={same_block_product_exp} "
            "reset_rhs={reset_rhs} SCALAR-BARRIER PASS".format(
                **row
            )
        )
    print("ALL ATOMIC KIC COUNTEREXAMPLE CHECKS PASS")


if __name__ == "__main__":
    main()
