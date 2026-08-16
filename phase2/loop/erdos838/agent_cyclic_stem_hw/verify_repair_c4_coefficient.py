#!/usr/bin/env python3
"""Exact finite audit for REPAIR_C4_COEFFICIENT_AUDIT.md.

All combinatorial counts are Python integers.  The entropy form is checked
through the equivalent product inequality

    hom(C4)^m >= product_{xy in E} (d_x e_y)^2,

which contains no floating-point arithmetic.  Decimal logs are used only
for the human-readable stress-family table.
"""

from __future__ import annotations

from decimal import Decimal, getcontext


def graph_stats(a: list[list[int]]) -> dict[str, int]:
    nl = len(a)
    nr = len(a[0])
    dl = [sum(row) for row in a]
    dr = [sum(a[i][j] for i in range(nl)) for j in range(nr)]
    m = sum(dl)
    if not m:
        raise ValueError("graph must be nonempty")

    c4 = 0
    c4_inj = 0
    for i in range(nl):
        for k in range(nl):
            codeg = sum(a[i][j] * a[k][j] for j in range(nr))
            c4 += codeg * codeg
            if i != k:
                c4_inj += codeg * (codeg - 1)

    path3 = sum(
        dl[i] * dr[j]
        for i in range(nl)
        for j in range(nr)
        if a[i][j]
    )
    degree_product = 1
    weighted_c4_numerator = 0
    for i in range(nl):
        for j in range(nr):
            if a[i][j]:
                degree_product *= dl[i] * dr[j]
    for i in range(nl):
        for k in range(nl):
            weighted_codeg = sum(
                a[i][j] * a[k][j] * dr[j] for j in range(nr)
            )
            weighted_c4_numerator += dl[i] * dl[k] * weighted_codeg**2

    return {
        "m": m,
        "c4": c4,
        "c4_inj": c4_inj,
        "path3": path3,
        "degree_product": degree_product,
        "weighted_c4_numerator": weighted_c4_numerator,
    }


def check_entropy_c4_exact(a: list[list[int]]) -> None:
    s = graph_stats(a)
    # Equivalent to C >= (prod_e d_x e_y)^(2/m).
    assert pow(s["c4"], s["m"]) >= pow(s["degree_product"], 2)


def exhaustive(max_cells: int = 16) -> tuple[int, int]:
    graphs = 0
    sharp = 0
    for nl in range(1, 5):
        for nr in range(1, 5):
            if nl * nr > max_cells:
                continue
            for mask in range(1, 1 << (nl * nr)):
                a = [
                    [(mask >> (i * nr + j)) & 1 for j in range(nr)]
                    for i in range(nl)
                ]
                check_entropy_c4_exact(a)
                s = graph_stats(a)
                graphs += 1
                if pow(s["c4"], s["m"]) == pow(s["degree_product"], 2):
                    sharp += 1
    return graphs, sharp


def star(m: int) -> dict[str, int]:
    a = [[1] * m]
    s = graph_stats(a)
    assert s["m"] == m
    assert s["path3"] == m * m  # q=1.
    assert s["weighted_c4_numerator"] == m**4  # W=1.
    assert s["c4"] == m * m
    assert s["c4_inj"] == 0
    check_entropy_c4_exact(a)
    return s


def ferrers(n: int) -> dict[str, int]:
    a = [[int((i + 1) * (j + 1) <= n) for j in range(n)] for i in range(n)]
    s = graph_stats(a)
    check_entropy_c4_exact(a)
    return s


def hub_wing(h: int, w: int) -> dict[str, int]:
    # Left: h hubs followed by h*w leaves owned by right hubs.
    # Right: h hubs followed by h*w leaves owned by left hubs.
    n = h + h * w
    a = [[0] * n for _ in range(n)]
    for i in range(h):
        for j in range(h):
            a[i][j] = 1
        for t in range(w):
            a[i][h + i * w + t] = 1
    for j in range(h):
        for t in range(w):
            a[h + j * w + t][j] = 1
    s = graph_stats(a)
    check_entropy_c4_exact(a)
    return s


def dec_ratio(num: int, den: int) -> str:
    return f"{Decimal(num) / Decimal(den):.12g}"


def main() -> None:
    getcontext().prec = 60
    graphs, sharp = exhaustive()
    print(f"exhaustive nonempty bipartite graphs checked: {graphs}")
    print(f"exact equality cases: {sharp}")

    for m in (1, 2, 5, 32):
        s = star(m)
        print(
            "star",
            m,
            "hom/m^2=",
            dec_ratio(s["c4"], s["m"] ** 2),
            "injective=",
            s["c4_inj"],
        )

    print("harmonic Ferrers stress")
    for n in (4, 8, 16, 32, 64):
        s = ferrers(n)
        print(
            n,
            "edges=",
            s["m"],
            "q=",
            dec_ratio(s["path3"], s["m"] ** 2),
            "hom/m^2=",
            dec_ratio(s["c4"], s["m"] ** 2),
            "weighted W=",
            dec_ratio(s["weighted_c4_numerator"], s["m"] ** 4),
        )

    print("hub-core/wing stress")
    for h, w in ((2, 8), (3, 27), (4, 64), (5, 125)):
        s = hub_wing(h, w)
        print(
            (h, w),
            "edges=",
            s["m"],
            "q=",
            dec_ratio(s["path3"], s["m"] ** 2),
            "hom/m^2=",
            dec_ratio(s["c4"], s["m"] ** 2),
        )

    print("PASS: exact entropy-spectral C4 inequality and stress tests")


if __name__ == "__main__":
    main()
