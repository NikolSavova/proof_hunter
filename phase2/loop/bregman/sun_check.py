#!/usr/bin/env python3
"""Numeric check of a SECOND claim about the Part I example: that C is a right D_f-SUN.

Why this matters. Re-reading Luo, Meng, Wen & Yao, Optimization 68(8) (2019) 1599-1624 for the
Part I novelty gate turned up more than a clearance. Their Theorem 3.13 concludes that a
boundedly compact right-D_f-Chebyshev set is a right-D_f-SUN, and its hypotheses (f totally
convex on U, grad f(U) = U*, f* locally uniformly totally convex on U*) do NOT include U = X.
Our example satisfies all of them. Their Theorem 3.12(3) then gives (i) <=> "grad f(C) convex"
under hypotheses we also satisfy, and our grad f(C) is nonconvex, so (i) FAILS.

So the example should satisfy their (ii) while failing their (i) — which is exactly a
counterexample to the equivalence (i) <=> (ii) asserted in their Theorem 3.12(2) under U = X.
That is a second payload for the note, and it is a claim about OUR example, so it can be tested
directly instead of taken on citation.

Definition 3.11 (Luo et al.), specialised: C is a right-D_f-sun if for every x in U and every
y in C,
        y = P^->_C(x)  ==>  y = P^->_C(z_lambda)  for every lambda >= 0 with z_lambda in U,
where z_lambda := lambda*x + (1-lambda)*y.

For lambda in [0,1] this is their Proposition 3.10(ii) and holds unconditionally, so the content
is entirely in lambda > 1: moving from y THROUGH x and beyond must not change the projection.
This script tests exactly that. A failure here would mean my reading of Theorem 3.13 is wrong
(or one of its total-convexity hypotheses fails for negative entropy) and would kill the second
claim before it reaches the write-up.

Reduction used throughout (Part I, Lemma SOL.4): minimising D_f(z, c(t)) over t in [1,2] is
minimising h_z(t) = e^t + e^{-t^2} - z_1 t + z_2 t^2, which depends on z only through (z_1, z_2).

Usage: ./sun_check.py
"""
import pathlib

from mpmath import mp, mpf, exp

mp.dps = 40
T_LO, T_HI = mpf(1), mpf(2)


def h(t, z):
    return exp(t) + exp(-t * t) - z[0] * t + z[1] * t * t


def dh(t, z):
    return exp(t) - 2 * t * exp(-t * t) - z[0] + 2 * z[1] * t


def argmin_t(z):
    """The unique minimiser of h_z on [1,2]. Strict convexity (Lemma SOL.2 + x_2 > 0) makes h_z'
    strictly increasing, so the three cases below are exhaustive and the root is unique."""
    if dh(T_LO, z) >= 0:
        return T_LO
    if dh(T_HI, z) <= 0:
        return T_HI
    lo, hi = T_LO, T_HI                       # dh(lo) < 0 < dh(hi), dh strictly increasing
    for _ in range(200):                      # plain bisection: 200 halvings of a unit interval
        mid = (lo + hi) / 2
        if dh(mid, z) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def c(t):
    return (exp(t), exp(-t * t))


def lam_max(x, y):
    """sup{lambda >= 0 : z_lambda in U = R^2_++}. z_j = y_j + lambda (x_j - y_j) > 0."""
    best = mpf("1e6")
    for j in (0, 1):
        if x[j] < y[j]:
            best = min(best, y[j] / (y[j] - x[j]))
    return best


def main():
    lines = []

    def log_(s):
        print(s, flush=True)
        lines.append(s)

    log_("Right-D_f-SUN check for C = {(e^t, e^{-t^2}) : t in [1,2]}, f = negative entropy on R^2")
    log_("Definition 3.11 of Luo-Meng-Wen-Yao (2019). Content is lambda > 1; lambda in [0,1] is")
    log_("their Proposition 3.10(ii) and holds for any C.\n")

    # (1) A wide adversarial spread of x in U = R^2_++, near-boundary and far-field.
    xs = []
    for a in ("0.0001", "0.01", "0.3", "1", "2.7", "8", "150", "10000"):
        for b in ("0.0001", "0.01", "0.3", "1", "2.7", "8", "150", "10000"):
            xs.append((mpf(a), mpf(b)))

    # (2) x CONSTRUCTED to project to a prescribed INTERIOR point of the arc. Most of the grid
    # above projects to an endpoint, where the sun condition is slack; the interior case is the
    # sharp one, so we manufacture it. Invert the first-order condition
    #     h_x'(t) = e^t - 2t e^{-t^2} - x_1 + 2 x_2 t = 0
    # for x_1 given a target t in (1,2) and any x_2 > 0.
    for ts in ("1.0000001", "1.05", "1.25", "1.5", "1.75", "1.95", "1.9999999"):
        t = mpf(ts)
        for bs in ("0.000001", "0.001", "0.5", "3", "1000", "100000"):
            b = mpf(bs)
            a = exp(t) - 2 * t * exp(-t * t) + 2 * b * t
            if a > 0:
                xs.append((a, b))

    worst = None          # largest observed |t(z_lambda) - t(x)|
    worst_interior = None  # same, restricted to x whose projection is INTERIOR (the sharp case)
    n_tested = 0
    n_endpoint = 0
    ok = True

    for x in xs:
        tx = argmin_t(x)
        y = c(tx)
        interior = T_LO < tx < T_HI
        if not interior:
            n_endpoint += 1
        lmax = lam_max(x, y)
        # sample lambda > 1 up to just short of leaving U, plus lambda in [0,1] as a control
        lams = [mpf(s) for s in ("0", "0.5", "1")]
        if lmax > 1:
            for frac in ("1.0001", "1.01", "1.2", "2", "5", "20", "100", "1000"):
                L = mpf(frac)
                if L < lmax:
                    lams.append(L)
            # and a lambda that crowds the boundary of U from inside
            if lmax < mpf("1e6"):
                for eps in ("0.9", "0.99", "0.999", "0.99999"):
                    lams.append(1 + (lmax - 1) * mpf(eps))
        for L in lams:
            z = (y[0] + L * (x[0] - y[0]), y[1] + L * (x[1] - y[1]))
            if z[0] <= 0 or z[1] <= 0:
                continue
            tz = argmin_t(z)
            gap = abs(tz - tx)
            n_tested += 1
            if worst is None or gap > worst[0]:
                worst = (gap, x, L, tx, tz)
            if interior and (worst_interior is None or gap > worst_interior[0]):
                worst_interior = (gap, x, L, tx, tz)
            if gap > mpf(10) ** -20:
                ok = False

    log_(f"  {len(xs)} points x in U; {n_tested} (x, lambda) pairs tested "
         f"({n_endpoint} of the x project to an ENDPOINT of the arc)")
    g, x, L, tx, tz = worst
    log_(f"  worst deviation overall:  |t(z_lambda) - t(x)| = {float(g):.3e}")
    log_(f"    at x = ({float(x[0]):g}, {float(x[1]):g}), lambda = {float(L):g}, "
         f"t(x) = {float(tx):.15f}, t(z) = {float(tz):.15f}")
    if worst_interior:
        g2, x2, L2, tx2, tz2 = worst_interior
        log_(f"  worst deviation among INTERIOR projections (the sharp case): {float(g2):.3e}")
        log_(f"    at x = ({float(x2[0]):g}, {float(x2[1]):g}), lambda = {float(L2):g}, "
             f"t(x) = {float(tx2):.15f}")
    log_(f"\n  the projection is INVARIANT along the ray from y through x -> "
         f"{'PASS: C behaves as a right-D_f-sun' if ok else 'FAIL: C is NOT a sun'}")

    log_("\n  Consequence if PASS: Luo et al.'s (ii) HOLDS for our C, while their (iv)")
    log_("  'grad f(C) is convex' FAILS (verify.py block [E]), hence their (i) fails by their")
    log_("  Theorem 3.12(3), whose hypotheses grad f(U) = U* and f* smooth+strictly convex on U*")
    log_("  we satisfy. Their Theorem 3.12(1) gives (i) => (ii) with no domain hypothesis, so no")
    log_("  contradiction arises; what fails is the CONVERSE (ii) => (i), which their Theorem")
    log_("  3.12(2) asserts under U = X. Our U = R^2_++ != R^2 = X. So U = X is essential there.")
    log_("\n  NOTE: this is a FINITE numerical check, exactly like block [D] of verify.py. It")
    log_("  supports the claim and would have refuted it cheaply; it does not certify the")
    log_("  universal quantifier. The paper's Lemma 4.1 carries the proof, and it is DIRECT:")
    log_("  h_w'(t) is affine in w and vanishes at t = s when w = c(s), so h'_{z_lambda}(s) =")
    log_("  lambda * h_x'(s), and the three cases of the endpoint trichotomy close it. That")
    log_("  argument does not go through Theorem 3.13 at all, so the total-convexity")
    log_("  hypotheses never have to be verified.")

    # ---- witness for the failure of Luo et al.'s condition (i), eq. (34) ----
    log_("\nWITNESS for the failure of condition (i) (Luo et al. eq. (34)):")
    s = (T_LO + T_HI) / 2
    eta = exp(-s * s)
    xw = (exp(s) - s * eta, eta / 2)
    log_(f"  s = {float(s)}, x = ({float(xw[0]):.12f}, {float(xw[1]):.12f}) in U: "
         f"{xw[0] > 0 and xw[1] > 0}")
    log_(f"  h_x'(s) = {float(dh(s, xw)):.3e}  (zero => c(s) is the right projection of x)")
    ok_w = abs(dh(s, xw)) < mpf(10) ** -30 and argmin_t(xw) == s
    worst_w = None
    for k in range(0, 41):
        t = T_LO + (T_HI - T_LO) * mpf(k) / 40
        if t == s:
            continue
        y = (exp(s), eta)
        # <grad f(c(s)) - grad f(c(t)), c(s) - x>, using grad f(c(r)) = (r, -r^2)
        lhs = (s - t) * (y[0] - xw[0]) + (t * t - s * s) * (y[1] - xw[1])
        rhs = (s - t) ** 2 * (eta - xw[1])          # the closed form claimed in the paper
        if abs(lhs - rhs) > mpf(10) ** -30 or lhs <= 0:
            ok_w = False
        if worst_w is None or lhs < worst_w[0]:
            worst_w = (lhs, t)
    log_(f"  over 41 values of t in [{float(T_LO)},{float(T_HI)}], the inner product matches")
    log_(f"  the closed form (s-t)^2 (e^-s^2 - x_2) and its SMALLEST value is "
         f"{float(worst_w[0]):.6e} at t = {float(worst_w[1])}")
    log_(f"  condition (i) requires this to be <= 0 for every c in C -> "
         f"{'PASS: (i) FAILS, as claimed' if ok_w else 'FAIL: witness is wrong'}")
    lmax_w = lam_max(xw, (exp(s), eta))
    log_(f"  the ray z_lambda leaves U at lambda = {float(lmax_w):.6f}, so the "
         f"lambda -> infinity step in the proof of Theorem 3.12(2) is unavailable")
    if not ok_w:
        raise SystemExit("witness check FAILED")

    out = pathlib.Path(__file__).resolve().parent / "out_sun_check.txt"
    out.write_text("\n".join(lines) + "\n")
    print(f"\n-> {out.name}")


if __name__ == "__main__":
    main()
