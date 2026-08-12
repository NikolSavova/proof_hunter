#!/usr/bin/env python3
"""NC-P3 (wp3-a2): handoff quantities.

(a) Tilt cap (Lemma P.8): lam(c*m) <= log(1 + 1/c), measured by solving
    mu(lam) = c*m with the T2 closed form (2.2); c in {0.5, 0.7, 1.0},
    m in {30, 100, 300, 1000, 3000}.
(b) Certified LOWER decimals for E(u) = sum_{n>=1} 2(3 v_n^2 + u^2) /
    (v_n^2 (v_n^2 + u^2)^2), v_n = 2 pi n  (partial sums of positive terms
    => rigorous lower bounds; 50000 terms + printed first-omitted-term size),
    at u = 1..8; and the P.7 floor rho(w0) = 1 - 6.85 w0^2 E(w0).
(c) P.7 consistency: true deficit 1 - s2/lambda at |w| = w0 vs floor
    6.85 w0^2 E(w0)  (must exceed the floor), m in {60, 120}, w0 in {2,3,4,5,6}.
(d) Deep-band truth from exact Mahonian rows, m in {30, 60, 100, 140}:
    eps(k) := |s2(k)(r(k)-1) - 1| with s2 from the closed form at lam(k);
    reports: max eps over the band k in [0.7m, k_w(4)] (w >= 4 side), and the
    minimal S such that all k with s2 >= S have eps <= 0.25 ("true C_0 at
    eps = 0.25"), plus max eps at s2 >= 50.
Floats here are measurement, not proof (the proved chain is in the draft).
"""
from math import pi, exp, log, expm1
from fractions import Fraction

def g(u):
    if abs(u) < 1e-4:
        return 0.5 - u / 12 + u**3 / 720 - u**5 / 30240
    if u > 500:
        return 1.0 / u
    return 1.0 / u - 1.0 / expm1(u)

def q(u):  # -g'(u) = 1/u^2 - e^u/(e^u-1)^2
    if abs(u) < 1e-3:
        return 1.0 / 12 - u * u / 240 + u**4 / 6048 - u**6 / 172800
    if u > 500:
        return 1.0 / (u * u)
    e = expm1(u)
    return 1.0 / (u * u) - (e + 1.0) / (e * e)

def mu(lam, m):
    return sum(j * g(lam * j) for j in range(1, m + 1)) - m * g(lam)

def s2f(lam, m):
    return sum(j * j * q(lam * j) for j in range(1, m + 1)) - m * q(lam)

def lam_of_k(k, m):
    lo, hi = 1e-14, 40.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if mu(mid, m) > k: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)

def E(u, N=50000):
    s = 0.0
    for n in range(1, N + 1):
        v2 = (2 * pi * n) ** 2
        s += 2 * (3 * v2 + u * u) / (v2 * (v2 + u * u) ** 2)
    # first omitted term (upper bound on truncation, for the report)
    v2 = (2 * pi * (N + 1)) ** 2
    omit = 2 * (3 * v2 + u * u) / (v2 * (v2 + u * u) ** 2) * 3  # crude tail ~ 3x first
    return s, omit

def main():
    print("== (a) tilt cap: lam(c*m) vs log(1+1/c) ==")
    for c in (0.5, 0.7, 1.0):
        cap = log(1 + 1 / c)
        line = f"  c={c:.1f} cap={cap:.4f}:"
        for m in (30, 100, 300, 1000, 3000):
            k = c * m if c < 1 else m - 1
            lam = lam_of_k(k, m)
            line += f"  m={m}:{lam:.4f}{'<=cap' if lam <= cap + 1e-9 else ' VIOL'}"
        print(line)

    print("== (b) certified lower decimals for E(u); floor rho(w0) ==")
    for u in range(1, 9):
        s, omit = E(u)
        print(f"  E({u}) >= {s:.8f}   (omitted tail ~{omit:.1e});  "
              f"floor deficit >= 6.85*{u}^2*E = {6.85*u*u*s:.4f};  rho({u}) <= {1-6.85*u*u*s:.4f}")

    print("== (c) true deficit vs P.7 floor at |w| = w0 ==")
    for m in (60, 120):
        lamb = m * (m - 1) * (2 * m + 5) / 72.0
        line = f"  m={m}:"
        for w0 in (2, 3, 4, 5, 6):
            lam = w0 / m
            d_true = 1 - s2f(lam, m) / lamb
            fl = 6.85 * w0 * w0 * E(w0, 20000)[0]
            ok = "ok" if d_true >= fl else "VIOL"
            line += f"  w0={w0}: {d_true:.4f}>={fl:.4f}{ok};"
        print(line)

    print("== (d) deep-band truth from exact rows ==")
    poly = [1]
    rows = {}
    for m in range(1, 141):
        old = poly; n_new = len(old) + m - 1; new = [0] * n_new; run = 0
        for k in range(n_new):
            if k < len(old): run += old[k]
            if 0 <= k - m < len(old): run -= old[k - m]
            new[k] = run
        poly = new
        if m in (30, 60, 100, 140): rows[m] = list(poly)
    print("   m   max_eps(band k in [0.7m, w=4 edge])   trueC0(eps<=0.25)   max_eps(s2>=50)")
    for m in (30, 60, 100, 140):
        row = rows[m]; N = m * (m - 1) // 2
        # w=4 edge: k with lam(k) = 4/m  <=> mu(4/m)
        k_edge = int(mu(4.0 / m, m))
        k_lo = max(2, int(0.7 * m))
        max_eps_band = 0.0; arg = None
        eps_by_s2 = []
        for k in range(2, N // 2 + 1):
            lam = lam_of_k(k, m)
            s2 = s2f(lam, m)
            r1 = row[k] * row[k] / (row[k - 1] * row[k + 1]) - 1.0  # float fine
            eps = abs(s2 * r1 - 1.0)
            eps_by_s2.append((s2, eps, k))
            if k_lo <= k <= k_edge and eps > max_eps_band:
                max_eps_band, arg = eps, k
        # true C0 at eps 0.25: minimal S s.t. all k with s2 >= S have eps <= 0.25
        eps_by_s2.sort()
        worst_above = 0.0; trueC0 = 0.0
        for s2, eps, k in reversed(eps_by_s2):
            worst_above = max(worst_above, eps)
            if worst_above > 0.25:
                trueC0 = s2; break
        max50 = max((eps for s2, eps, k in eps_by_s2 if s2 >= 50), default=0.0)
        print(f"  {m:4d}   {max_eps_band:.4f} (k={arg}, edge k={k_edge})          "
              f"{trueC0:8.2f}        {max50:.4f}")

if __name__ == "__main__":
    main()
