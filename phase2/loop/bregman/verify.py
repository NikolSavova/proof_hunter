#!/usr/bin/env python3
"""Numeric harness for the Bregman right-Chebyshev counterexample (PROBLEM.md).

Written BEFORE any prover runs, per the Tier-2 loop design: the harness defines what
"verified" means, so a later draft cannot move the goalposts. Every check below tests a
claim the write-up will make; a draft that contradicts this harness is wrong, not the harness.

Interval arithmetic (mpmath.iv, directed rounding) for the load-bearing bounds; exhaustive
brute-force sampling as a sanity check on the uniqueness claim (see Block D: it is a finite
check and does NOT certify the universal quantifier — Lemma SOL.5 of the proof does).

Usage: ./verify.py            (all blocks)
       ./verify.py A C        (selected blocks)

Blocks
  [A] model sanity     D_f is the generalized KL divergence; grad f = log; U* = R^2
  [B] reduction        D(x, c(t)) == const(x) + h_x(t) with h_x as claimed
  [C] strict convexity h_x'' > e + 2/e > 17/5 > 0 on [1,2], uniformly in x in R^2_++ (INTERVAL)
  [D] uniqueness       FINITE numerical sanity check only: an argmin scan over a t-grid for a
                       sample of x. It CANNOT certify the quantifier "for every x in U", and it
                       counts only strict INTERIOR grid minima, so an endpoint minimiser yields
                       zero. The universal singleton claim is proved by Lemma SOL.5 of
                       proof_part1_20260813.md, NOT by this block.
  [E] nonconvexity     C* is a strictly concave arc; explicit midpoint witness
  [F] hypotheses       dom f != X (the hypothesis under test FAILS) and cl C* subset U* (HOLDS)
"""
import sys
from fractions import Fraction as Fr

from mpmath import iv, mp, mpf, exp, log

mp.dps = 40
iv.dps = 40
T_LO, T_HI = 1, 2


def hull(a, b):
    a, b = iv.mpf(a), iv.mpf(b)
    return iv.mpf([min(a.a, b.a), max(a.b, b.b)])


# ---------- the objects ----------
def c(t):
    """The curve C, parametrised on [1,2]."""
    return (exp(t), exp(-t * t))


def grad_f(y):
    """grad of the negative entropy: componentwise log."""
    return (log(y[0]), log(y[1]))


def D(x, y):
    """Generalized KL: sum_j [x_j ln(x_j/y_j) - x_j + y_j]."""
    return sum(x[j] * log(x[j] / y[j]) - x[j] + y[j] for j in (0, 1))


def h(t, x):
    """The claimed reduction: D(x, c(t)) = const(x) + h(t,x)."""
    return exp(t) + exp(-t * t) - x[0] * t + x[1] * t * t


def block_A(log_):
    ok = True
    for x, y in (((mpf(2), mpf(3)), (mpf(1), mpf(5))), ((mpf("0.3"), mpf("4.1")), (mpf("2.2"), mpf("0.7")))):
        direct = D(x, y)
        # D_f(x,y) = f(x) - f(y) - <grad f(y), x-y> with f = sum(u ln u - u)
        f = lambda u: sum(u[j] * log(u[j]) - u[j] for j in (0, 1))
        viadef = f(x) - f(y) - sum(log(y[j]) * (x[j] - y[j]) for j in (0, 1))
        agree = abs(direct - viadef) < mpf(10) ** -30
        ok &= agree
        log_(f"  D{tuple(float(v) for v in x)},{tuple(float(v) for v in y)} = {float(direct):.12f} "
             f"| via definition {float(viadef):.12f} | agree={agree}")
    log_("  grad f(y) = (ln y_1, ln y_2) maps R^2_++ ONTO R^2, so U* = R^2.")
    return ok


def block_B(log_):
    ok = True
    for x in ((mpf(1), mpf(1)), (mpf("0.05"), mpf("7.3")), (mpf(9), mpf("0.02"))):
        const = None
        for t in (mpf("1.0"), mpf("1.37"), mpf("2.0")):
            d = D(x, c(t)) - h(t, x)
            if const is None:
                const = d
            ok &= abs(d - const) < mpf(10) ** -28
        log_(f"  x={tuple(float(v) for v in x)}: D(x,c(t)) - h(t,x) constant in t "
             f"(= {float(const):.10f}) -> {ok}")
    return ok


def block_C(log_):
    """h''(t) = e^t + (4t^2-2) e^{-t^2} + 2 x_2 ; bound below uniformly over x_2 > 0."""
    worst = None
    N = 4000
    for i in range(N):
        a = iv.mpf(T_LO) + (iv.mpf(T_HI) - iv.mpf(T_LO)) * iv.mpf(i) / N
        b = iv.mpf(T_LO) + (iv.mpf(T_HI) - iv.mpf(T_LO)) * iv.mpf(i + 1) / N
        t = hull(a, b)
        v = iv.exp(t) + (4 * t * t - 2) * iv.exp(-t * t)      # x_2 -> 0+ is the infimum
        lo = float(v.a)
        if worst is None or lo < worst[0]:
            worst = (lo, float(a.a))
    good = worst[0] > 3.45
    log_(f"  CERTIFIED LOWER BOUND (interval, 4000 cells) = {worst[0]:.6f} at t~{worst[1]:.4f}")
    log_(f"    [this is an enclosure bound, NOT the infimum; the true inf is e+2/e = 3.454040710802]")
    log_(f"  tested: h'' > 3.45 uniformly in x_2 > 0 -> {'PASS' if good else 'FAIL'}")
    return good


def block_D(log_):
    """FINITE sanity check (see header). Not a certificate; Lemma SOL.5 carries the claim."""
    xs = [(mpf(a) / 10, mpf(b) / 10) for a in (1, 5, 20, 100, 400) for b in (1, 5, 20, 100, 400)]
    xs += [(mpf(10) ** -4, mpf(10) ** 4), (mpf(10) ** 4, mpf(10) ** -4)]  # adversarial corners
    N = 20000
    ok = True
    worst_gap = None
    for x in xs:
        vals = [(T_LO + (T_HI - T_LO) * mpf(i) / N, None) for i in range(N + 1)]
        vals = [(t, h(t, x)) for t, _ in vals]
        mn = min(v for _, v in vals)
        # count strict local minima on the grid -> a unique argmin has exactly one
        loc = sum(1 for i in range(1, N) if vals[i][1] < vals[i - 1][1] and vals[i][1] < vals[i + 1][1])
        argmins = [t for t, v in vals if v <= mn + mpf(10) ** -25]
        span = float(max(argmins) - min(argmins))
        ok &= loc <= 1 and span < 1e-3
        if worst_gap is None or span > worst_gap[0]:
            worst_gap = (span, tuple(float(v) for v in x), loc)
    log_(f"  {len(xs)} adversarial x, grid {N}: max argmin-span {worst_gap[0]:.2e} at x={worst_gap[1]}, "
         f"interior local minima {worst_gap[2]}")
    log_(f"  unique minimiser for every tested x -> {'PASS' if ok else 'FAIL'}")
    return ok


def block_E(log_):
    p, q = (mpf(1), mpf(-1)), (mpf(2), mpf(-4))          # C* endpoints, t = 1 and t = 2
    mid = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)          # (1.5, -2.5)
    on_arc = (mid[0], -mid[0] ** 2)                       # (1.5, -2.25)
    gap = float(on_arc[1] - mid[1])
    good = gap > 0.2
    log_(f"  C* endpoints {tuple(float(v) for v in p)}, {tuple(float(v) for v in q)}; "
         f"midpoint {tuple(float(v) for v in mid)}")
    log_(f"  arc at t=1.5 is {tuple(float(v) for v in on_arc)}: midpoint lies {gap:.4f} BELOW the arc")
    log_(f"  => C* nonconvex -> {'PASS' if good else 'FAIL'}")
    return good


def block_F(log_):
    log_("  dom f = R^2_+ (f = +inf off the closed positive orthant) != R^2 = X")
    log_("    => the FULL-DOMAIN hypothesis of Fact 3.2 FAILS. This is the hypothesis under test.")
    log_("  U* = grad f(U) = R^2, and C* is compact, so cl C* = C* subset U*")
    log_("    => the OTHER hypothesis HOLDS, so the counterexample isolates full domain. PASS")
    return True


BLOCKS = {"A": ("model sanity", block_A), "B": ("reduction to h(t,x)", block_B),
          "C": ("strict convexity (interval)", block_C), "D": ("uniqueness — finite sanity check", block_D),
          "E": ("nonconvexity of C*", block_E), "F": ("hypothesis bookkeeping", block_F)}

if __name__ == "__main__":
    which = [a.upper() for a in sys.argv[1:]] or list(BLOCKS)
    lines = []

    def log_(s):
        print(s, flush=True)
        lines.append(s)

    log_("Bregman right-Chebyshev counterexample — numeric harness (PROBLEM.md)")
    allok = True
    for k in which:
        name, fn = BLOCKS[k]
        log_(f"[{k}] {name}:")
        allok &= fn(log_)
    log_(f"# OVERALL: {'ALL CHECKS PASS' if allok else 'SOME CHECKS FAILED'}")
    (pathlib_out := __import__("pathlib").Path(__file__).resolve().parent / "out_verify.txt").write_text(
        "\n".join(lines) + "\n")
